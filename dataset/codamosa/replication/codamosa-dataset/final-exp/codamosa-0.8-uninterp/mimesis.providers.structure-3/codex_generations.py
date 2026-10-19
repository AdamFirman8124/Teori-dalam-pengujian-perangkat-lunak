

# Generated at 2022-06-14 00:52:10.327386
# Unit test for method css_property of class Structure
def test_Structure_css_property(): # pragma: no cover
    """Unit test for method css_property of class Structure."""
    structure = Structure()
    print(structure.css_property())


# Generated at 2022-06-14 00:52:17.841870
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """
    Generate a random snippet of HTML with attributes set to random values.
    """
    from mimesis.enums import Gender
    from mimesis.providers import Structure

    structure = Structure(seed=123)

    for _ in range(3):
        tag = structure.random.choice(
            list(structure.HTML_CONTAINER_TAGS))
        attr = structure.random.choice(
            list(structure.HTML_CONTAINER_TAGS[tag]))
        print('\nTag {}'.format(tag))
        print('Attribute {}'.format(attr))
        print(structure.html_attribute_value(tag, attr))


# Generated at 2022-06-14 00:52:29.353948
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from collections import defaultdict
    from mimesis.builtins import HTML_CONTAINER_TAGS
    import pytest

    # Generating a tag and its attribute
    tag = Structure().random.choice(list(HTML_CONTAINER_TAGS))
    attribute = Structure().random.choice(
        list(HTML_CONTAINER_TAGS[tag]),  # type: ignore
    )

    # Generating n values of the given attribute
    n = 10
    generated_values = defaultdict(int)
    structure = Structure()
    for _ in range(n):
        generated_values[structure.html_attribute_value(tag, attribute)] += 1

    # If all values are generated according to their probability,
    # the amount of generated values should be close to the theoretical
    # amounts of values for each value type

# Generated at 2022-06-14 00:52:35.574547
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    dp = Structure()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()
    assert dp.css_property()


# Generated at 2022-06-14 00:52:39.307322
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    i = 0
    while i < 1000:
        assert len(s.css_property().split(':')) == 2
        i += 1


# Generated at 2022-06-14 00:52:41.779479
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    pass

# Generated at 2022-06-14 00:52:49.912218
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    from mimesis.enums import CSSProperty
    from mimesis.enums import CSSSelector
    from mimesis.enums import CSSSizeUnit
    from mimesis.enums import HTMLAttribute
    from mimesis.enums import HTMLTag
    from mimesis.enums import MarkupContainerTag
    from mimesis.enums import MarkupTag

    # Test that CSSProperty is the same as CSS_PROPERTIES
    assert set(CSSProperty) == set(CSS_PROPERTIES)

    # Test that CSSSelector is the same as CSS_SELECTORS
    assert set(CSSSelector) == set(CSS_SELECTORS)

    # Test that CSSSizeUnit is the same as CSS_SIZE_UNITS
    assert set(CSSSizeUnit) == set(CSS_SIZE_UNITS)

    # Test that HTML

# Generated at 2022-06-14 00:52:57.772920
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Test for method html_attribute_value of class Structure."""
    s = Structure()
    htmls = []
    for tag in HTML_CONTAINER_TAGS.keys():
        for attribute, value in HTML_CONTAINER_TAGS[tag].items():
            if attribute == 'class' or attribute == 'style':
                values = value * 2
            else:
                values = value
            htmls.append(s.html_attribute_value(tag, attribute))
            htmls.append(s.html_attribute_value(tag, attribute, values))

    assert len(htmls) > 0

# Generated at 2022-06-14 00:53:03.133699
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # 1. Input:
    # Expected Output:
    # 2. Input:
    # Expected Output:
    # 3. Input:
    # Expected Output:
    # 4. Input:
    # Expected Output:
    # 5. Input:
    # Expected Output:

    # Arrange
    structure = Structure()

    # Act

    # Assert



# Generated at 2022-06-14 00:53:11.990996
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.enums import HTMLLangAttributes as HLAttr
    from mimesis.enums import HTMLTagAttributes as HTAttr
    s = Structure()

    # test with a not implemented tag
    tag = 'fake_tag'
    try:
        s.html_attribute_value(tag)
    except NotImplementedError:
        assert True

    # test with a not implemented attribute for tag 'a'
    tag = 'a'
    attribute = 'fake_attribute'
    try:
        s.html_attribute_value(tag, attribute)
    except NotImplementedError:
        assert True

    # test with a tag 'a' and an attribute 'href'
    tag = 'a'
    attribute = HTAttr.HREF

# Generated at 2022-06-14 00:53:30.850697
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    """Test for css_property method."""
    struct = Structure('ru')
    assert struct.css_property() in CSS_PROPERTIES

# Generated at 2022-06-14 00:53:42.351800
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    """Test if given attribute belongs to the given tag"""
    assert 'class' == list(HTML_CONTAINER_TAGS['div'].keys())[0]
    """Test if given the tag and attribute generate an attribute value"""
    assert isinstance(s.html_attribute_value('div', 'class'), str)
    assert len(s.html_attribute_value('div', 'class')) > 0
    """Test if given the tag and attribute generate an attribute value with
    the right type according to the metadata"""
    assert 'color' == HTML_CONTAINER_TAGS['span']['style']
    assert isinstance(s.html_attribute_value('span', 'style'), str)
    assert len(s.html_attribute_value('span', 'style')) > 0

# Generated at 2022-06-14 00:53:46.759704
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure."""
    _Structure = Structure()
    _tag = 'a'
    _attribute = 'href'
    __result = _Structure.html_attribute_value(_tag, _attribute)
    assert isinstance(__result, str)
    assert _tag == 'a'
    assert _attribute == 'href'
    assert __result is not None
    assert __result != ' '
    assert __result != ''


# Generated at 2022-06-14 00:53:51.654897
# Unit test for method css_property of class Structure
def test_Structure_css_property():
	# Arrange
	structure = Structure()
	# Act
	actual = structure.css_property()
	# Assert
	assert actual is not None
	assert actual != ''


# Generated at 2022-06-14 00:53:59.298360
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    to_test = Structure()
    for tag in HTML_CONTAINER_TAGS:
        for attribute in list(HTML_CONTAINER_TAGS[tag]):
            if to_test.html_attribute_value(tag, attribute) == None:
                print('tag: {}, attribute: {}'.format(tag, attribute))
                to_test.html_attribute_value(tag, attribute)
                return False
    print('Done testing method html_attribute_value')
    return True

# Main.
if __name__ == '__main__':
    # Test all class members of Structure.
    test = Structure()
    test.css()
    test.css_property()
    test.html()
    

# Generated at 2022-06-14 00:54:08.249097
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test"""
    # Test (a) without tag
    value = Structure.html_attribute_value()
    assert type(value) is str
    # Test (b) without any parameters
    html = Structure.html_attribute_value()
    assert type(html) is str
    # Test (c) an unsupported tag
    try:
        html = Structure.html_attribute_value(tag='unsupported_tag')
    except Exception as e:
        assert 'Tag unsupported_tag or attribute' in str(e)
    # Test (d) an unsupported attribute
    try:
        html = Structure.html_attribute_value(attribute='unsupported_attribute')
    except Exception as e:
        assert 'Tag unsupported_attribute or attribute' in str(e)
    # Test (e) an unsupported both tag and attribute

# Generated at 2022-06-14 00:54:09.408554
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    assert len(Structure().html_attribute_value())>0

# Generated at 2022-06-14 00:54:12.312863
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure()
    tag = 'div'
    attr = 'class'
    assert struct.html_attribute_value(tag, attr)

# Generated at 2022-06-14 00:54:14.680332
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    print(s.css_property())


# Generated at 2022-06-14 00:54:18.507109
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure"""
    strt = Structure()
    print(strt.html_attribute_value('a', 'href'))

# Generated at 2022-06-14 00:54:38.384094
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    provider = Structure()
    css_property = provider.css_property()
    print(css_property)


# Generated at 2022-06-14 00:54:50.784455
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.providers.structure import Structure
    structure = Structure(seed=123456789)
    value1 = structure.html_attribute_value('a', 'href')
    assert value1 == 'http://www.sahney-klinge.org/entrance.php'
    value2 = structure.html_attribute_value('a', 'href')
    assert value2 == 'http://www.sahney-klinge.org/entrance.php'
    value3 = structure.html_attribute_value('a', 'href')
    assert value3 == 'http://www.sahney-klinge.org/entrance.php'
    value4 = structure.html_attribute_value('a', 'rel')
    assert value4 == 'cite'

# Generated at 2022-06-14 00:54:56.043504
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure('en')
    for i in range(0, 100):
        css_property = structure.css_property()
        assert(css_property == '' or css_property[len(css_property) - 1] == ';')


# Generated at 2022-06-14 00:55:05.449920
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    _ = Structure()
    assert _.html_attribute_value('a', 'class') == 'word'
    assert _.html_attribute_value('a', 'href') == 'url'
    assert _.html_attribute_value('a', 'style') == 'css'
    assert _.html_attribute_value('a', 'id') == 'word'


# Generated at 2022-06-14 00:55:14.029722
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert s.html_attribute_value(
        tag='a', attribute='class') in CSS_SELECTORS,\
        'Asserting if the generated value is a CSS selector'\
        ' for tag "a", attribute "class"'
    assert s.html_attribute_value(
        tag='a', attribute='id') not in CSS_SELECTORS,\
        'Asserting if the generated value is not a CSS selector'\
        ' for tag "a", attribute "id"'

    assert s.html_attribute_value(
        tag='div', attribute='class') in CSS_SELECTORS,\
        'Asserting if the generated value is a CSS selector'\
        ' for tag "a", attribute "class"'
    assert s.html_attribute_value(
        tag='div', attribute='id') not in CSS

# Generated at 2022-06-14 00:55:15.910538
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    test = Structure(seed=1)
    result = test.css_property()
    expected = 'text-decoration: overline'
    assert result == expected


# Generated at 2022-06-14 00:55:20.509838
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    _s = Structure()
    _html_attribute_value = _s.html_attribute_value(tag='html', attribute='lang')
    assert _html_attribute_value == 'en'

# Generated at 2022-06-14 00:55:21.593520
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert s.css_property() in CSS_PROPERTIES

# Generated at 2022-06-14 00:55:25.636551
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    for _ in range(100):
        assert len(s.css_property()['background-color']) == 7


# Generated at 2022-06-14 00:55:28.292728
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    for i in range(1,10):
        assert len(s.css_property()) > 0

# Generated at 2022-06-14 00:55:49.454117
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    html_str = Structure()
    assert html_str.html_attribute_value('a', 'href') == 'url'
    assert html_str.html_attribute_value('a', 'class') == 'css'
    assert html_str.html_attribute_value('a', 'rel') == 'word'

    assert html_str.html_attribute_value('img', 'src') == 'url'
    assert html_str.html_attribute_value('img', 'class') == 'css'
    assert html_str.html_attribute_value('img', 'alt') == 'word'

    assert html_str.html_attribute_value('div', 'class') == 'css'
    assert html_str.html_attribute_value('div', 'id') == 'word'

# Generated at 2022-06-14 00:55:52.767256
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    print(s.html_attribute_value('link', 'rel'))
    print(s.html_attribute_value('input', 'type'))


# Generated at 2022-06-14 00:55:57.973872
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    tag = 'a'
    attribute = 'rel'
    value = structure.html_attribute_value(tag, attribute)
    assert value in HTML_CONTAINER_TAGS[tag][attribute]

# Generated at 2022-06-14 00:55:59.825240
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure()
    if struct.html_attribute_value() == None:
        raise NotImplementedError

# Generated at 2022-06-14 00:56:08.966343
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()

    num_tests = 100
    for _ in range(num_tests):
        property = structure.css_property()
        property_name = property.split(':')[0].strip()
        property_value = property.split(':')[1].strip()

        assert property_name in list(CSS_PROPERTIES.keys())
        assert (
            property_value in CSS_PROPERTIES[property_name] or
            property_value.startswith('#') or
            property_value.endswith('px') or
            property_value.endswith('%')
        )
    


# Generated at 2022-06-14 00:56:13.763830
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure("en")
    tag = "link"
    attribute = "type"
    test_value = [
        "text/css",
        "text/javascript",
    ]
    assert structure.html_attribute_value(tag, attribute) in test_value

# Generated at 2022-06-14 00:56:15.167081
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struct = Structure()
    struct.css_property()

# Generated at 2022-06-14 00:56:16.987793
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    result = Structure().html_attribute_value(tag="img",
                                              attribute="alt")
    assert result in [text.word() for text in Text('en')]

# Generated at 2022-06-14 00:56:20.010984
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    generator = Structure()
    for _ in range(10000):
        # print(generator.css_property())
        assert generator.css_property() is not None


# Generated at 2022-06-14 00:56:29.918919
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure('en')
    for tag in s.Meta.tags:
        for attribute in HTML_CONTAINER_TAGS[tag]:
            try:
                s.html_attribute_value(tag, attribute)
            except NotImplementedError:
                assert False

    for attribute in s.Meta.attributes:
        try:
            s.html_attribute_value(None, attribute)
        except NotImplementedError:
            assert False

    # Test Unsupported tag and attribute
    try:
        s.html_attribute_value('foo', 'bar')
    except NotImplementedError:
        assert True



# Generated at 2022-06-14 00:56:53.059896
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    print('\u001b[1;37;44m Test method Structure::css_property() \u001b[0m')
    s = Structure()
    print(s.css_property())


# Generated at 2022-06-14 00:57:02.879369
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=0)
    tag_names_list = ['div', 'span', 'li', 'title']
    tag_attributes_list = ['class', 'id']
    tag = s.random.choice(tag_names_list)
    attribute = s.random.choice(tag_attributes_list)
    expected_attrib_value = s.html_attribute_value(tag,attribute)
    assert len(expected_attrib_value) > 0, 'Expected attribute value is empty'


# Generated at 2022-06-14 00:57:12.330556
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert (s.html_attribute_value('a', 'download') != None)
    assert (s.html_attribute_value('a', 'href') != None)
    assert (s.html_attribute_value('a', 'href') != 'href')
    assert (s.html_attribute_value('a', 'href') != 'download')
    assert (s.html_attribute_value('img', 'src') != None)
    assert (s.html_attribute_value('img', 'src') != 'src')
    assert (s.html_attribute_value('img', 'src') != 'alt')
    assert (s.html_attribute_value('div', 'id') != None)
    assert (s.html_attribute_value('div', 'id') != 'id')

# Generated at 2022-06-14 00:57:14.188634
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    css_p = Structure()
    count = 0
    for i in range(0, 100):
        count += 1
        result = css_p.css_property()
        assert result.find(':') != -1
    assert count == 100

# Generated at 2022-06-14 00:57:27.759116
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.core import Mimesis
    from mimesis.structures import Structure

    mimesis: Mimesis = Mimesis()
    mimesis.add_provider(Structure)
    tags = ['html', 'meta', 'link', 'body', 'div',
            'span', 'strong', 'p', 'i', 'b', 'a',
            'img', 'h1', 'h2', 'h3', 'h4', 'h5',
            'h6', 'textarea', 'input', 'header',
            'footer', 'section', 'article', 'table',
            'tr', 'td', 'th', 'tbody', 'ul', 'ol',
            'li', 'form', 'option', 'select', 'video',
            'audio', 'style']

# Generated at 2022-06-14 00:57:39.249612
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    cnt_right = 0
    cnt_wrong = 0
    for tag in HTML_CONTAINER_TAGS.keys():
        for attribute in HTML_CONTAINER_TAGS[tag].keys():  # type: ignore
            if isinstance(HTML_CONTAINER_TAGS[tag][attribute], str):
                try:
                    s.html_attribute_value(tag = tag, attribute = attribute)
                    cnt_right += 1
                except:
                    cnt_wrong += 1
    print("Right: ", cnt_right)
    print("Wrong: ", cnt_wrong)

# Generated at 2022-06-14 00:57:46.124844
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    tag = 'span'
    attribute = 'class'
    generated_value = s.html_attribute_value(tag, attribute)
    expected_value = 'select'
    assert generated_value == expected_value

# Generated at 2022-06-14 00:57:54.527971
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # Check class structure
    assert (type(Structure(seed = 0)).__name__ == 'Structure')
    # Check method html_attribute_value for correct execution
    assert (Structure(seed = 0).html_attribute_value(tag = 'a', attribute = 'href') != None)
    # Check method html_attribute_value for correct execution
    assert (Structure(seed = 0).html_attribute_value(tag = 'abbr', attribute = 'title') != None)
    # Check method html_attribute_value for correct execution
    assert (Structure(seed = 0).html_attribute_value(tag = 'address', attribute = 'class') != None)
    # Check method html_attribute_value for correct execution
    assert (Structure(seed = 0).html_attribute_value(tag = 'area') != None)
    # Check method

# Generated at 2022-06-14 00:58:00.803037
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Test structure's html_attribute_value function."""
    s = Structure()
    assert s.html_attribute_value('div', 'class')
    assert s.html_attribute_value('div', 'id')
    assert s.html_attribute_value('p', 'lang')
    assert s.html_attribute_value('a', 'href')
    assert s.html_attribute_value('form', 'action')
    assert s.html_attribute_value()

if __name__ == "__main__":
    test_Structure_html_attribute_value()

# Generated at 2022-06-14 00:58:04.799687
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    print("\nStructure.html_attribute_value")
    structure = Structure()
    print(structure.html_attribute_value())
    structure = Structure()
    print(structure.html_attribute_value(tag='input', attribute='name'))
    print(structure.html_attribute_value(tag='input', attribute='type'))
    """
    Structure.html_attribute_value
    <input id="desert">
    username
    password
    """
