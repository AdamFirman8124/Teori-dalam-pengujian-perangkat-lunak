

# Generated at 2022-06-14 00:52:14.473908
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert s.html_attribute_value(tag='p') in HTML_CONTAINER_TAGS['p']
    assert s.html_attribute_value(attribute='class') in HTML_CONTAINER_TAGS['p']['class']

# Generated at 2022-06-14 00:52:18.461071
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    instance = Structure('en')
    html_tag = 'img'
    html_attribute = 'src'
    result = instance.html_attribute_value(html_tag, html_attribute)
    assert len(result) > 5

# Generated at 2022-06-14 00:52:22.870241
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    value = structure.html_attribute_value('?', '?')
    if isinstance(value, str):
        print('Method html_attribute_value of class Structure is correct')
    else:
        print('Method html_attribute_value of class Structure is not correct')

# Generated at 2022-06-14 00:52:33.750545
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    """Test for method css_property of class Structure"""
    seed = 12
    locale = 'en'
    structure = Structure(locale=locale, seed=seed)
    css = structure.css_property()
    css_property_list = css.split(':')

    assert (len(css_property_list)) == 2

    assert (css_property_list[0].strip() in CSS_PROPERTIES)

    if (CSS_PROPERTIES[css_property_list[0].strip()] in
            ["background_color", "color", "border_color", "outline_color",
             "text_color"]):
        assert (len(css_property_list[1].strip()) == 7)
        assert css_property_list[1].strip()[0] == '#'

# Generated at 2022-06-14 00:52:45.637682
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # Tests for method html_attribute_value of class Structure
    structure = Structure('ru')
    tag = 'link'
    attribute = 'charset'
    expected = 'charset="utf-8"'
    result = structure.html_attribute_value(tag=tag, attribute=attribute)
    assert result == expected

    tag = 'input'
    attribute = 'type'
    expected = 'type="radio"'
    result = structure.html_attribute_value(tag=tag, attribute=attribute)
    assert result == expected

    tag = 'div'
    attribute = 'class'
    expected = 'class="cmd"'
    result = structure.html_attribute_value(tag=tag, attribute=attribute)
    assert result == expected



# Generated at 2022-06-14 00:52:57.149084
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    """Test for method css_property of class Structure."""

# Generated at 2022-06-14 00:53:06.851195
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # create instance of Structure class
    create = Structure()
    # create list of keys of dict CSS_PROPERTIES
    list_keys_CSS_PROPERTIES = list(CSS_PROPERTIES.keys())
    # take item of list_keys_CSS_PROPERTIES
    item_list_keys_CSS_PROPERTIES = create.random.choice(list_keys_CSS_PROPERTIES)
    # take value by dict CSS_PROPERTIES
    value_CSS_PROPERTIES = CSS_PROPERTIES[item_list_keys_CSS_PROPERTIES]
    # create list
    array_CSS_SIZE_UNITS = list(CSS_SIZE_UNITS)
    # create list of values of dict HTML_CONTAINER_TAGS
    list_values_HTML_CONTAINER_TAG

# Generated at 2022-06-14 00:53:13.820903
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # This test verifies correctness of method css_property()
    # It verifies if method returns property in form of string
    # It verifies if property is in CSS_PROPERTIES
    # It verifies if property is in CSS_PROPERTIES
    structure = Structure()
    structure.random.seed(1)
    property_str = structure.css_property()
    property_str_name = property_str.split(': ')[0]
    assert isinstance(property_str, str)
    assert property_str_name in CSS_PROPERTIES.keys()
    assert property_str in CSS_PROPERTIES.values()


# Generated at 2022-06-14 00:53:15.138838
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert isinstance(s.css_property(), str)
    print(s.css_property())


# Generated at 2022-06-14 00:53:19.500412
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    print("Testing function css_property of class Structure...")

    structure = Structure(seed=22)
    print("structure.css_property() = " + structure.css_property())
