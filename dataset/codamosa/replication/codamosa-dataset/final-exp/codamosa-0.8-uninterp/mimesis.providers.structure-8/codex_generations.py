

# Generated at 2022-06-14 00:52:21.093382
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    import unittest
    import random
    from mimesis.providers.structure import Structure
    s = Structure(seed = random.randint(1, 1000))
    tag = 'a'
    attr = 'href'
    value = s.html_attribute_value(tag, attr)
    assert value != None
    assert value != ''
    assert value != ' '

# Generated at 2022-06-14 00:52:27.551318
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    """Test method css_property of class Structure."""
    test_property = Structure().css_property()
    assert test_property[0] in CSS_PROPERTIES
    assert test_property[1] == ':'
    assert test_property[2] == ' '


# Generated at 2022-06-14 00:52:32.184881
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    assert Structure().html_attribute_value() == '#f4d3a1'
    assert Structure().html_attribute_value() == CSS_PROPERTIES['background-color']
    assert Structure().html_attribute_value(tag='span', attribute='style') == CSS_PROPERTIES['background-color']

# Generated at 2022-06-14 00:52:34.563564
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # Given
    structure = Structure()
    # When
    result = structure.css_property()
    # Then
    assert result
    assert isinstance(result, str)


# Generated at 2022-06-14 00:52:41.300309
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
        # Check that a structure element can be generated from the list of css
        # with the given tag and attribute
        test_tag = "a"
        test_attribute = "style"
        testing_element = Structure()
        generated_element = testing_element.html_attribute_value(
            tag=test_tag, attribute=test_attribute)
        print(generated_element)


# Generated at 2022-06-14 00:52:44.580385
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    tag = "a"
    attribute = "href"
    value = "http://www.gates.com/"
    assert value == Structure().html_attribute_value(tag, attribute)


# Generated at 2022-06-14 00:52:47.390228
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    print(s.html_attribute_value('div'))


# Generated at 2022-06-14 00:52:54.134012
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    import random
    from mimesis.seed import Seed
    '''
    seed = Seed(45679)
    random.seed(seed)
    random.seed()
    '''
    seed = Seed(45679)
    random.seed(seed)
    css_obj = Structure(seed=seed)
    assert css_obj.css_property() == 'color: #c6fe68'

# Generated at 2022-06-14 00:52:57.410436
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    S = Structure()
    S.html_attribute_value('a', 'href')
    S.html_attribute_value('br')
    S.html_attribute_value('div', 'class')
    S.html_attribute_value()
    
    

# Generated at 2022-06-14 00:53:01.056062
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure_provider = Structure(seed=42)
    tag = 'a'
    attribute = 'href'
    value = structure_provider.html_attribute_value(tag, attribute)
    assert value == 'http://www.elissa.biz'