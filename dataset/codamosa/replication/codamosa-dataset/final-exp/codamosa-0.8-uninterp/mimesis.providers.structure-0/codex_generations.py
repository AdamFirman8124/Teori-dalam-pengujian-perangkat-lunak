

# Generated at 2022-06-14 00:52:08.558260
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()

    i = 1
    while i < 10:
        css_prop = s.css_property()
        assert isinstance(css_prop, str)
        i += 1
 

# Generated at 2022-06-14 00:52:10.367938
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    assert Structure().html_attribute_value('img') == 'url'



# Generated at 2022-06-14 00:52:18.783798
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():

    def _test_html_attribute_value(seed, expected):
        structure = Structure(seed=seed)

        tag = structure.random.choice(list(HTML_CONTAINER_TAGS.keys()))
        attribute = structure.random.choice(
            list(HTML_CONTAINER_TAGS[tag]),  # type: ignore
        )

        result = structure.html_attribute_value(tag, attribute)
        assert result == expected

    _test_html_attribute_value(1, 'http://example.com/')
    _test_html_attribute_value(2, '#f4d3a1')
    _test_html_attribute_value(3, 'bgcolor="none"')
    _test_html_attribute_value(4, 'word')

# Generated at 2022-06-14 00:52:20.905585
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    attr_value = s.html_attribute_value(tag='a', attribute='class')
    assert isinstance(attr_value, str)

# Generated at 2022-06-14 00:52:26.389246
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    structure.html_attribute_value()
    structure.html_attribute_value('div')
    structure.html_attribute_value(attribute='id')

    try:
        structure.html_attribute_value(attribute='idk')
    except NotImplementedError:
        print('Tag or attribute is not supported')


# Generated at 2022-06-14 00:52:34.211219
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    print("Testing Structure.html_attribute_value()")
    from mimesis.enums import Attribute
    from mimesis.enums import Tag

    struct = Structure()

    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)
    struct.html_attribute_value(Tag.A, Attribute.TARGET)

# Generated at 2022-06-14 00:52:38.365661
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    tag = 'img'
    assert structure.html_attribute_value(tag = tag, attribute = 'src') != None
    return 'OK'


# Generated at 2022-06-14 00:52:42.409155
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struc = Structure()
    css_property = struc.css_property()
    print(css_property)
    assert css_property == 'stroke-width: 36'


# Generated at 2022-06-14 00:52:49.912317
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    import pytest
    from mimesis.providers.structure import Structure
    
    s = Structure(seed=123)
    # test default value
    assert s.html_attribute_value() in list(HTML_CONTAINER_TAGS)
    # test for using tag as input
    for tag in list(HTML_CONTAINER_TAGS):
        assert s.html_attribute_value(tag=tag) in list(HTML_CONTAINER_TAGS[tag])
    # test for input that is not supported
    with pytest.raises(NotImplementedError):
        s.html_attribute_value(tag='head')

# Generated at 2022-06-14 00:52:51.352751
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    print(s.html_attribute_value(tag='input', attribute='type'))


# Generated at 2022-06-14 00:53:03.260443
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    inv = Structure() 
    result = inv.css_property()
    assert (not (result == ""))


# Generated at 2022-06-14 00:53:05.940761
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    s.html_attribute_value(tag='a', attribute='href') == 'http://example.com/'

# Generated at 2022-06-14 00:53:10.754745
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    St = Structure()
    property = St.css_property()
    assert isinstance(property, str)
    assert len(property.split(': ')) == 2
    assert property.split(': ')[1] == '#f4d3a1'
    assert property.split(': ')[0] in CSS_PROPERTIES.keys()


# Generated at 2022-06-14 00:53:17.020369
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.enums import Attribute, Tag

    structure = Structure('en')
    # Test for input argument tag
    assert structure.html_attribute_value(
        tag='a',
    )
    assert structure.html_attribute_value(
        tag=Tag.A,
    )
    # Test for input argument attribute
    assert structure.html_attribute_value(
        attribute='href',
    )
    assert structure.html_attribute_value(
        attribute=Attribute.HREF,
    )
    # Test for two input arguments
    assert structure.html_attribute_value(
        tag='input',
        attribute='required',
    )
    assert structure.html_attribute_value(
        tag=Tag.INPUT,
        attribute=Attribute.REQUIRED,
    )
    # Test for not existing attribute
   

# Generated at 2022-06-14 00:53:26.396052
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert s.html_attribute_value()
    assert s.html_attribute_value('table')
    assert s.html_attribute_value('table', 'summary')
    assert s.html_attribute_value('a')
    assert s.html_attribute_value('a', 'href')
    assert s.html_attribute_value('a', 'rel')
    assert s.html_attribute_value('a', 'target')
    assert s.html_attribute_value('body')
    assert s.html_attribute_value('body', 'background')
    assert s.html_attribute_value('body', 'bgcolor')
    assert s.html_attribute_value('img')
    assert s.html_attribute_value('img', 'longdesc')
    assert s.html_attribute_value('img', 'src')


# Generated at 2022-06-14 00:53:29.894787
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struct = Structure(seed=42)
    result = struct.css_property()
    assert result == 'font-family: serif'

# Generated at 2022-06-14 00:53:32.698096
# Unit test for method css_property of class Structure
def test_Structure_css_property():

    t = Structure(seed=1)
    print(t.css_property())


# Generated at 2022-06-14 00:53:34.343614
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    class_instance = Structure()
    assert len(class_instance.css_property()) > 0


# Generated at 2022-06-14 00:53:40.245314
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    from pprint import pprint
    from random import choice
    s = Structure()
    for _ in range(5):
        pprint(s.css_property())
    for _ in range(5):
        pprint(s.css_property(choice(list(CSS_PROPERTIES))))


# Generated at 2022-06-14 00:53:43.953486
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # tag = 'button'
    # attribute = 'class'
    # class_val = ['btn', 'btn-default', 'btn-primary',
    #              'btn-secondary', 'btn-info']
    # assert value in class_val
    print('test_Structure_html_attribute_value() is called')

# Generated at 2022-06-14 00:54:10.911227
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s=Structure()
    d=[s.html_attribute_value(s.random.choice(list(HTML_CONTAINER_TAGS.keys())),s.random.choice(list(HTML_CONTAINER_TAGS[tag]))) for _ in range(10)]
    for i in range(10):
        print(d[i])

# Generated at 2022-06-14 00:54:24.595903
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    import pytest

    sl = Structure()
    pattern = '\s*background-color:\s*#[0-9a-f]{3,6}\s*'
    assert sl.regex(pattern).search(sl.css_property()) is not None

    # Test for tag names that are not currently supported.
    with pytest.raises(NotImplementedError):
        sl.html_attribute_value('bombast', 'quisquam') is None

    # Test for attribute names that are not currently supported.
    with pytest.raises(NotImplementedError):
        sl.html_attribute_value('dl', 'quisquam') is None

# Generated at 2022-06-14 00:54:26.872966
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis import Structure
    structure = Structure()
    a = structure.html_attribute_value(tag='p', attribute='class')
    print(a)

# Generated at 2022-06-14 00:54:37.016197
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Test method html_attribute_value of class Structure."""
    structure = Structure(seed=42)
    html_attribute_value = structure.html_attribute_value
    html_attribute_value("p", "align") == "center"
    html_attribute_value("span", "contenteditable") == "true"
    html_attribute_value("span", "dir") == "rtl"
    html_attribute_value("p", "hidden") == "hidden"
    html_attribute_value("span", "id") == "dark"
    html_attribute_value("span", "spellcheck") == "true"
    html_attribute_value("p", "style") == "width: 23px; height: 5px;"


# Generated at 2022-06-14 00:54:38.782225
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert s.css_property() == 'display: block'

# Generated at 2022-06-14 00:54:41.840521
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert s.css_property() in CSS_PROPERTIES


# Generated at 2022-06-14 00:54:46.840748
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure('zh')
    for i in range(1, 10):
        css_property = structure.css_property()
        assert css_property != None
        assert type(css_property) == str
        print(css_property)



# Generated at 2022-06-14 00:54:57.057180
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()

    # Test all combinations of tag and attr for cases where
    # HTML_CONTAINER_TAGS[tag][attr] is a list

    for tag in list(HTML_CONTAINER_TAGS):
        for attribute in list(HTML_CONTAINER_TAGS[tag]):
            value = HTML_CONTAINER_TAGS[tag][attribute]
            if isinstance(value, list):
                generated_value = structure.html_attribute_value(tag, attribute)
                assert generated_value in value, 'generated_value not in value'

    # Test all combinations of tag and attr for cases where
    # HTML_CONTAINER_TAGS[tag][attr] is a string


# Generated at 2022-06-14 00:55:01.051070
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    for i in range(1000):
        assert isinstance(structure.css_property(), str)


# Generated at 2022-06-14 00:55:07.405234
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for Structure.html_attribute_value()."""
    for i in range(10):
        if '#' not in Structure().html_attribute_value():
            assert False
        if 'http' not in Structure().html_attribute_value():
            assert False

# Generated at 2022-06-14 00:55:35.047472
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=0)
    assert s.html_attribute_value() == 'cyan'
    assert s.html_attribute_value(attribute='rel') == 'new'
    assert s.html_attribute_value(tag='link', attribute='rel') == 'new'
    try:
        s.html_attribute_value(tag='link')
    except Exception:
        assert True


if __name__ == "__main__":
    s = Structure(seed=0)
    print(s.html())

# Generated at 2022-06-14 00:55:39.657759
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure('en')
    assert structure.html_attribute_value('a', 'href')
    assert structure.html_attribute_value('a', 'rel')



# Generated at 2022-06-14 00:55:45.294874
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    import mimesis
    from mimesis.builtins import CustomProvider
    structure = mimesis.Structure()
    structure.add_provider(CustomProvider)
    prop = structure.css_property()
    assert type(prop) is str
    assert prop    # Ensure prop not empty
    assert ':' in prop
    assert prop.find(':') < prop.rfind(';') or prop.rfind(';') == -1


# Generated at 2022-06-14 00:55:46.314548
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    assert Structure().html_attribute_value()


# Generated at 2022-06-14 00:55:51.701114
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure."""

    structure = Structure()
    attribute = structure.html_attribute_value('a', 'href')
    assert isinstance(attribute, str)
    assert attribute != ''
    assert attribute.startswith('http')


# Generated at 2022-06-14 00:56:00.074027
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    tags = list(HTML_CONTAINER_TAGS.keys())
    tag_random_index = s.random.randint(0,len(tags))
    tag = tags[tag_random_index]
    attributes = list(HTML_CONTAINER_TAGS[tag])  # type: ignore
    attribute_random_index = s.random.randint(0, len(attributes))
    attribute = attributes[attribute_random_index]
    s.html_attribute_value(tag, attribute)

# Generated at 2022-06-14 00:56:05.396038
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    generated = Structure.css_property(en)
    assert generated == 'background-color: #f4d3a1'


# Generated at 2022-06-14 00:56:16.463012
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure.

    Generates random value for specified HTML tag attribute.
    """
    tag_list = list(HTML_CONTAINER_TAGS)  # type: ignore
    tag = random.choice(tag_list)

    attribute_list = list(HTML_CONTAINER_TAGS[tag])  # type: ignore
    attribute = random.choice(attribute_list)

    value = HTML_CONTAINER_TAGS[tag]['attribute']  # type: ignore

    assert type(Struct.html_attribute_value(tag, attribute)) == str

# Generated at 2022-06-14 00:56:19.753241
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    result = structure.html_attribute_value('img', 'alt')
    assert isinstance(result, str), "Expected string"
    assert result != '', "Expected non-empty string"

# Generated at 2022-06-14 00:56:23.390984
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    css_gen = Structure()
    prop = css_gen.css_property()
    assert prop in CSS_PROPERTIES
