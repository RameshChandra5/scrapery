Usage Guide
===========

Installation
------------

Install the package using pip:

.. code-block:: bash

    pip install scrapery

-------------------------------
HTML Example
-------------------------------

.. code-block:: python

    from scrapery import *

    html_content = """
    <html>
        <body>
            <h1>Welcome</h1>
            <p>Hello<br>World</p>
            <a href="/about">About Us</a>
            <img src="/images/logo.png">
            <table>
                <tr><th>Name</th><th>Age</th></tr>
                <tr><td>John</td><td>30</td></tr>
                <tr><td>Jane</td><td>25</td></tr>
            </table>
        </body>
    </html>
    """

    # Parse HTML content
    html_doc = parse_html(html_content)

    # Pretty print HTML
    print(prettify(html_doc))

    # Get all table rows
    rows = select_all(html_doc, "table tr")
    for row in rows:
        print(selector_content(row))

    # Get first paragraph
    paragraph = select_one(html_doc, "p")
    print("Paragraph:", selector_content(paragraph))

    # CSS and XPath Selectors
    print(selector_content(html_doc, selector="h1"))        # CSS
    print(selector_content(html_doc, selector="//h1"))      # XPath
    print(selector_content(html_doc, selector="a", attr="href"))  # CSS attr
    print(selector_content(html_doc, selector="//a", attr="href"))  # XPath attr

    # Get specific table cells
    print(selector_content(html_doc, selector="td"))          # First <td>
    print(selector_content(html_doc, selector="//td[2]"))     # Second <td>
    print(selector_content(html_doc, selector="//tr[3]/td[2]"))  # Jane's age

    # Full text content
    print(selector_content(html_doc))

    # Root attribute
    print(selector_content(html_doc, attr="lang"))


Embedded Data
-------------

.. code-block:: python

    html_content = """
    <html>
    <head>
      <script>
        window.__INITIAL_STATE__ = {
          "user": {"id": 1, "name": "Alice"},
          "isLoggedIn": true
        };
      </script>
    </head>
    </html>
    """

    json_data = get_embedded_json(page_source=html_content, is_ld_json=False)
    print(json_data)

.. code-block:: python

    html_with_ldjson = """
    <html>
      <head>
        <script type="application/ld+json">
          {
            "@context": "http://schema.org",
            "@type": "Person",
            "name": "Alice"
          }
        </script>
      </head>
    </html>
    """

    ld_json = get_embedded_json(page_source=html_with_ldjson, is_ld_json=True)
    print(ld_json)


DOM Navigation
--------------

.. code-block:: python

    p_elem = select_one(html_doc, "p")
    print("Parent:", parent(p_elem).tag)
    print("Children:", [c.tag for c in children(p_elem)])
    print("Siblings:", [s.tag for s in siblings(p_elem)])

    print("Next sibling of <p>:", next_sibling(p_elem).tag)
    h1_elem = select_one(html_doc, "h1")
    print("Previous sibling of <h1>:", next_sibling(h1_elem))

    ancs = ancestors(p_elem)
    print("Ancestors:", [a.tag for a in ancs])
    desc = descendants(select_one(html_doc, "table"))
    print("Descendants:", [d.tag for d in desc])


Class Utilities
---------------

.. code-block:: python

    div_html = '<div class="card primary"></div>'
    div_elem = parse_html(div_html)
    print("Has class 'card'? ->", has_class(div_elem, "card"))
    print("Classes:", get_classes(div_elem))


Resolve Relative URLs
----------------------

.. code-block:: python

    base = "https://example.com"
    print(absolute_url(html_doc, "a", base_url=base))
    print(absolute_url(html_doc, "img", base_url=base, attr="src"))


XML Example
-----------

.. code-block:: python

    xml_content = "<root><child>Test</child></root>"
    xml_doc = parse_xml(xml_content)
    print(prettify(xml_doc))

    all_elements = select_all(xml_doc, "child")
    print(all_elements)

    child = select_one(xml_doc, "//child")
    print(child)

    print(selector_content(xml_doc, "child"))
    print(parent(child))
    print(children(xml_doc))

    print(xml_find(xml_doc, "child"))
    print(xml_find_all(xml_doc, "child"))

    print(xml_xpath(xml_doc, "//child"))

    xslt = """<?xml version="1.0"?>
    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
        <xsl:template match="/">
            <html><body><xsl:value-of select="/root/child"/></body></html>
        </xsl:template>
    </xsl:stylesheet>"""

    transformed = xml_transform(xml_doc, xslt)
    print(prettify(transformed))

    # Validate (requires schema file)
    is_valid = xml_validate_xsd(xml_doc, Path("schema.xsd"))
    print(is_valid)

    new_element = xml_create_element("newTag", text="This is new", id="123")
    xml_add_child(xml_doc, new_element)
    xml_set_attr(new_element, "id", "456")
    print(prettify(xml_doc))


JSON Example
------------

.. code-block:: python

    json_str = '{"user": {"profile": {"name": "Alice"}}}'
    print(json_content(json_str, keys=["name"], position="first"))
    print(json_content(json_str, keys=["user", "profile", "name"], position="last"))


Utilities
---------

Create a Directory
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scrapery import create_directory

    create_directory("new_folder")
    create_directory("parent_folder/sub_folder")

Standardize a String
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scrapery import standardized_string

    input_string = "<html><body>  Hello \nWorld!  \tThis is a test.  </body></html>"
    print(standardized_string(input_string))

Read CSV
^^^^^^^^

.. code-block:: python

    from scrapery import read_csv

    result = read_csv('data.csv', 'URL', 'Category', ['Tech'])
    print(result)

Save to CSV
^^^^^^^^^^^

.. code-block:: python

    from scrapery import save_to_csv

    list_data = [[1, 'Alice', 23], [2, 'Bob', 30], [3, 'Charlie', 25]]
    headers = ['ID', 'Name', 'Age']
    output_file_path = 'output.csv'
    save_to_csv(list_data, headers, output_file_path)

Save to Excel
^^^^^^^^^^^^^

.. code-block:: python

    from scrapery import save_to_xls

    save_to_xls(list_data, headers, 'output.xlsx')

List Files in a Directory
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scrapery import list_files

    files = list_files(directory="output", extension="csv")
    print(files)

Read File Content
^^^^^^^^^^^^^^^^^

.. code-block:: python

    from scrapery import read_file_content

    small_json = read_file_content("small.json", stream_json=False)
    print(small_json)

    stream = read_file_content("large.json", stream_json=True)
    for obj in stream:
        print(obj)

    text = read_file_content("large_text.txt")
    print(text[:500])

Save to File
^^^^^^^^^^^^

.. code-block:: python

    from scrapery import save_file_content

    save_file_content("output.txt", "Hello World")
    save_file_content("data.json", {"name": "Alice"})
    save_file_content("append.txt", "\nAnother line", mode="a")
