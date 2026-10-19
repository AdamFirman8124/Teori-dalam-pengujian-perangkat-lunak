

# Generated at 2022-06-14 00:52:14.935002
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure('en')
    assert len(structure.css_property()) > 0


# Generated at 2022-06-14 00:52:27.185674
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    a = Structure()
    assert 'style' in a.html_attribute_value(tag='p', attribute='style')
    assert a.html_attribute_value(tag='p', attribute='href')
    assert a.html_attribute_value(tag='p', attribute='rel')
    assert '#' in a.html_attribute_value(tag='p', attribute='id')
    assert '#' in a.html_attribute_value(tag='p', attribute='class')
    assert a.html_attribute_value(tag='p', attribute='title')
    assert a.html_attribute_value(tag='p', attribute='src')
    assert a.html_attribute_value(tag='p', attribute='alt')
    assert a.html_attribute_value(tag='p', attribute='type')

# Generated at 2022-06-14 00:52:30.540391
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value
    of class Structure
    """
    s = Structure(seed=1)
    assert(s.html_attribute_value() == 'nav')

# Generated at 2022-06-14 00:52:40.469391
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # Testing tag <a>
    s = Structure()
    assert s.html_attribute_value(tag='a', attribute='href') == 'url'
    assert s.html_attribute_value(tag='a', attribute='target') == '_blank'
    assert s.html_attribute_value(tag='a', attribute='rel') == 'noopener'
    # Testing tag <img>
    assert s.html_attribute_value(tag='img', attribute='alt') == 'word'
    assert s.html_attribute_value(tag='img', attribute='title') == 'word'
    # Testing tag <div>
    assert s.html_attribute_value(tag='div', attribute='id') == 'word'
    assert s.html_attribute_value(tag='div', attribute='class') == 'word'
    # Testing tag <

# Generated at 2022-06-14 00:52:42.622612
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure(seed=42)

    result = structure.css_property()
    assert result == 'background-color: #f4d3a1'

# Generated at 2022-06-14 00:52:46.003444
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure('ru')
    type_list = ['css', 'word', 'url']
    for i in range(0, len(type_list)):
        assert isinstance(struct.html_attribute_value('html'), str)


# Generated at 2022-06-14 00:52:54.135468
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure"""
    structure = Structure()

    # Test when tag not in list
    tag = 'span'
    attribute = 'lang'
    result = structure.html_attribute_value(tag, attribute)
    assert isinstance(result, str) is True

    # Test when attribute not in list
    tag = 'span'
    attribute = 'test'
    result = structure.html_attribute_value(tag, attribute)
    assert isinstance(result, str) is True

# Generated at 2022-06-14 00:52:56.368145
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    res = s.html_attribute_value('a', 'href')
    assert(isinstance(res, str))

# Generated at 2022-06-14 00:52:58.294626
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    obj = Structure()
    assert obj.html_attribute_value() is not None
    assert obj.html_attribute_value(tag='a', attribute='href') is not None


# Generated at 2022-06-14 00:53:08.780125
# Unit test for method html_attribute_value of class Structure