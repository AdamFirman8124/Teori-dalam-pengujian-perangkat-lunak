

# Generated at 2022-06-14 00:52:38.250659
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure(locale='en')
    s.css_property()


# Generated at 2022-06-14 00:52:40.391851
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    assert Structure().css_property() == 'background-color: #f4d3a1'


# Generated at 2022-06-14 00:52:42.465980
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure()
    struct.html_attribute_value('a', 'href')


# Generated at 2022-06-14 00:52:44.318062
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    print("Structure.html_attribute_value()", end=" => ")
    s = Structure()
    assert s.html_attribute_value()
    print("ok")


# Generated at 2022-06-14 00:52:51.537904
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure."""
    structure = Structure()
    attr_dict = {"a": {"href": "url"},
                 "img": {"src": "url"},
                 "script": {"type": ["text/javascript", "text/ecmascript"]},
                 "link": {"type": ["text/css", "text/ecmascript"]},
                 "div": {"style": "css"},
                 "img": {"alt": "word"}
                 }
    for tag, attrs in attr_dict.items():
        for attr, _ in attrs.items():
            assert structure.html_attribute_value(tag, attr)