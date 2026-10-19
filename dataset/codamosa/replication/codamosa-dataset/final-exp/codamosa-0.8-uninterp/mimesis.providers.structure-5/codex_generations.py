

# Generated at 2022-06-14 00:52:02.012869
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure=Structure()
    structure.css_property()


# Generated at 2022-06-14 00:52:12.876045
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    print('Testing method html_attribute_value of class Structure')
    for i in range(4):
        print(Structure().html_attribute_value())
    print(Structure().html_attribute_value('a', 'href'))
    print(Structure().html_attribute_value('a', 'href', 'mailto:xxx@xxx.com'))

    try:
        Structure().html_attribute_value('x', 'y')
        print('Test failed!')
    except NotImplementedError:
        print('Test passed!')

    try:
        Structure().html_attribute_value('a', 'x')
        print('Test failed!')
    except NotImplementedError:
        print('Test passed!')
# Test end.


# Generated at 2022-06-14 00:52:23.155251
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    flag = False
    for _ in range(100):
        struct = Structure()
        tag = struct.random.choice(list(HTML_CONTAINER_TAGS.keys()))
        attrs = list(HTML_CONTAINER_TAGS[tag])
        attr = struct.random.choice(attrs)
        value = struct.html_attribute_value(tag, attr)
        if value in HTML_CONTAINER_TAGS[tag][attr]:
            flag = True
        else:
            flag = False
            break
    assert flag == True

# Generated at 2022-06-14 00:52:33.993755
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # Initialize
    #   instance of attribute
    #   looper
    #   dictionary of tags
    #   dictionary of attributes
    #   number of attributes
    #   list of dictionaries of attributes
    s_instance = Structure()
    looper = 50
    tags = HTML_CONTAINER_TAGS
    attributes = dict()
    dict_attributes = list()
    n = len(tags)
    # Create a dictionary of attributes
    for tag in tags:
        attributes[tag] = list(tags[tag])
    # Create a list of dictionaries of attributes
    for _ in range(looper):
        dict_attributes.append(attributes)
    # For each list of dictionaries of attributes
    for dict_attribute in dict_attributes:
        # Pick random tag and attribute
        dict_attribute_pairs = list

# Generated at 2022-06-14 00:52:46.468763
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.data import HTML_CONTAINER_TAGS
    from random import Random, choice
    from string import ascii_letters

    for key in HTML_CONTAINER_TAGS.keys():
        for attribute in HTML_CONTAINER_TAGS[key]:
            test_Structure = Structure()
            result = test_Structure.html_attribute_value(key, attribute)

            if isinstance(HTML_CONTAINER_TAGS[key][attribute], list):
                assert result in HTML_CONTAINER_TAGS[key][attribute]
            elif HTML_CONTAINER_TAGS[key][attribute] == 'word':
                assert len(result) > 0
                result = result.lower()
                flag = False
                for letter in result:
                    if not letter.isalnum():
                        flag = True
               

# Generated at 2022-06-14 00:52:52.291180
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():

    S1 = Structure(seed=1234)

    assert S1.html_attribute_value() == '0.5'
    assert S1.html_attribute_value() == 'url(#idOfAnotherGradient)'
    assert S1.html_attribute_value() == 'url(#otherRibbon)'



# Generated at 2022-06-14 00:52:56.875505
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure('ru')
    assert s.html_attribute_value('a', 'href') in [
        'http://dwyer-may.com/blog/',
        'https://www.lynch.com/',
        'https://www.www.wisoky-zieme.net/'
    ]


# Generated at 2022-06-14 00:53:02.653897
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    assert Structure().html_attribute_value('a') == 'a'
    assert Structure().html_attribute_value('blockquote') == 'blockquote'
    assert Structure().html_attribute_value('img', 'title') == 'word'
    assert Structure().html_attribute_value('input', 'type') == 'text'
    assert Structure().html_attribute_value('input', 'placeholder') == 'word'

# Generated at 2022-06-14 00:53:11.596169
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struc = Structure('en', True)

    # pass empty parameter
    result = struc.html_attribute_value()

    # pass valid parameters
    result = struc.html_attribute_value("span", "class")

    # catch NotImplementedError
    try:
        struc.html_attribute_value("span", "id")
        result = None
    except NotImplementedError:
        result = "NotImplementedError"

    try:
        struc.html_attribute_value("span", "blabla")
        result = None
    except NotImplementedError:
        result = "NotImplementedError"

# Generated at 2022-06-14 00:53:20.698758
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    attribute = Structure()
    tag = 'a'
    attribute_name = 'href'
    assert attribute.html_attribute_value(tag, attribute_name)
    tag = 'a'
    attribute_name = 'class'
    assert attribute.html_attribute_value(tag, attribute_name)
    tag = 'a'
    attribute_name = 'name'
    assert attribute.html_attribute_value(tag, attribute_name)
    tag = 'a'
    attribute_name = 'data-track'
    assert attribute.html_attribute_value(tag, attribute_name)
    tag = 'a'
    attribute_name = 'onclick'
    assert attribute.html_attribute_value(tag, attribute_name)
    tag = 'meta'
    attribute_name = 'charset'
    assert attribute.html_attribute

# Generated at 2022-06-14 00:53:45.189821
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    result = structure.css_property()
    assert ":" in result


# Generated at 2022-06-14 00:53:50.576272
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert(len(s.css_property().split(': '))==2)


# Generated at 2022-06-14 00:53:53.852561
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure."""
    structure = Structure()
    assert len(structure.html_attribute_value()) > 0, \
        'html_attribute_value does not work'


# Generated at 2022-06-14 00:54:03.939421
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Test for method html_attribute_value of class Structure"""
    s = Structure(seed=5160739)
    assert s.html_attribute_value('a', 'href') == 'css'
    assert s.html_attribute_value('a', 'href') == 'color: #f4d3a1'
    assert s.html_attribute_value('a', 'href') == 'color: #f4d3a1'
    assert s.html_attribute_value('a', 'href') == 'color: #f4d3a1'
    assert s.html_attribute_value('script', 'src') == 'css'
    assert s.html_attribute_value('script', 'src') == 'color: #b1a3aa'

# Generated at 2022-06-14 00:54:09.509481
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure_provider = Structure()
    print('---- Test method html_attribute_value of class Structure ----')
    print('Test value of html_attribute_value is as expected')
    assert structure_provider.html_attribute_value('a', 'href') == 'url'
    print('Test value of html_attribute_value is not as expected')
    assert not structure_provider.html_attribute_value('a', 'href') != 'url'
    print('Test if an exception message is thrown when tag is unsupported')
    try:
        structure_provider.html_attribute_value('test', 'href')
    except NotImplementedError as error:
        assert 'Tag test is not supported' == str(error)
    print('Test if an exception message is thrown when attribute is unsupported')

# Generated at 2022-06-14 00:54:17.169390
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Language
    from mimesis.providers.misc import Misc
    from mimesis.providers.structure import Structure

    seed = 130
    rus_spec = RussiaSpecProvider(seed=seed)
    misc = Misc(seed=seed)
    structure = Structure(seed=seed)
    structure.add_provider(rus_spec)
    structure.add_provider(misc)
    structure.set_language(Language.RU)

    result = structure.html_attribute_value(attribute='style')
    expected = 'background-color: #f3c01d'

    assert result == expected

# Generated at 2022-06-14 00:54:23.750927
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure_provider = Structure(locale='en')
    attribute_value = structure_provider.html_attribute_value('p','id')
    assert isinstance(attribute_value, str), \
        "Expected type string, got {}".format(type(attribute_value))
    assert attribute_value, "Expected non-empty string"

# Generated at 2022-06-14 00:54:25.919854
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    from mimesis.enums import CSSProperty
    s = Structure()
    assert s.css_property() in CSSProperty.values()


# Generated at 2022-06-14 00:54:27.376278
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # Arrange
    # Act

    # Assert
    assert True is True

# Generated at 2022-06-14 00:54:30.602690
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert s.html_attribute_value() is not None


# Generated at 2022-06-14 00:54:47.292635
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Tests for method html_attribute_value of class Structure"""
    structure = Structure('en')
    value = structure.html_attribute_value('a')
    assert value == '#'
    value = structure.html_attribute_value('a', 'href')
    assert value == '#'
    assert type(value) == str

# Generated at 2022-06-14 00:54:51.157502
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    result = Structure().css_property()
    assert isinstance(result, str)
    assert len(result) > 0
    assert ":" in result


# Generated at 2022-06-14 00:54:56.460481
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    assert Structure().css_property() == 'background-color: #aa71b0'
    assert Structure().css_property() == 'background-color: #e8dcf0'
    assert Structure().css_property() == 'background-color: #9e0e53'
    

# Generated at 2022-06-14 00:54:59.672553
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    css = structure.css_property()
    assert css is not None

# Generated at 2022-06-14 00:55:08.066140
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    import mimesis
    structure = mimesis.Structure('en', seed=1)
    tag = 'button'
    tag_attrs = HTML_CONTAINER_TAGS[tag]
    for attr in tag_attrs:
        assert structure.html_attribute_value(tag, attr)
    assert structure.html_attribute_value()


# Generated at 2022-06-14 00:55:12.904285
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=123)
    assert s.html_attribute_value(tag="a", attribute="download") == "filename"
    assert s.html_attribute_value(tag="a", attribute="href") == "http://www.pilgrim.name"
    assert s.html_attribute_value(tag="a", attribute="rel") == "alternate"
    assert s.html_attribute_value(tag="a", attribute="target") == "_parent"
    assert s.html_attribute_value(tag="a", attribute="type") == "video/mp4"
    assert s.html_attribute_value(tag="a", attribute="media") == "screen"
    assert s.html_attribute_value(tag="a", attribute="charset") == "utf-8"

# Generated at 2022-06-14 00:55:14.284272
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    random = Random()
    s = Structure(random)
    assert (s.css_property() in str(CSS_PROPERTIES.values()))

# Generated at 2022-06-14 00:55:15.405905
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    assert structure.html_attribute_value()

# Generated at 2022-06-14 00:55:18.100541
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    st = Structure('en')
    print(st.css_property())
    

# Generated at 2022-06-14 00:55:23.087185
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Get a random HTML tag attribute value.

    :return: HTML.
    """
    html = Structure()
    tag_attribute = html.html_attribute_value()
    print(tag_attribute)

# Generated at 2022-06-14 00:55:39.597242
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struct = Structure()
    struct.css_property()

# Generated at 2022-06-14 00:55:48.472158
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    html_tag_list = ['a', 'div', 'h2', 'span', 'form', 'input']
    for tag in html_tag_list:
        assert len(Structure().html_attribute_value(tag).split()) == 1
    # Test with random attribute
    assert len(Structure().html_attribute_value("a").split()) == 1
    assert len(Structure().html_attribute_value("div").split()) == 1
    assert len(Structure().html_attribute_value("h2").split()) == 1
    assert len(Structure().html_attribute_value("span").split()) == 1
    assert len(Structure().html_attribute_value("form").split()) == 1
    assert len(Structure().html_attribute_value("input").split()) == 1
    # Test with attribute accept

# Generated at 2022-06-14 00:55:52.727131
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure(seed=123)
    css_property = structure.css_property()
    assert css_property == 'z-index: 4'


# Generated at 2022-06-14 00:55:59.907984
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=12345)
    assert s.html_attribute_value() == 'inverted'
    assert s.html_attribute_value('a', 'target') == '_self'
    assert s.html_attribute_value('link', 'rel') == 'shortlink'
    assert s.html_attribute_value('link', 'rev') == 'made'

# Generated at 2022-06-14 00:56:07.310061
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    assert(structure.html_attribute_value()[0:4] == 'http')
    assert(structure.html_attribute_value('a')[0:4] == 'http')
    assert(structure.html_attribute_value('div')[0:4] != 'http')
    assert(structure.html_attribute_value('a', 'href')[0:4] == 'http')
    assert(structure.html_attribute_value('a', 'href')[-1] == 'r')
    assert(structure.html_attribute_value('a', 'target') == '_blank')
    assert(structure.html_attribute_value('a', 'title')[0].isupper())

# Generated at 2022-06-14 00:56:16.696474
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structure = Structure()
    assert structure.html_attribute_value(
        'div', 'align') in HTML_CONTAINER_TAGS['div']['align']
    assert structure.html_attribute_value(
        'div', 'class') == 'css'
    assert structure.html_attribute_value(
        tag=None, attribute=None) == 'word'
    assert structure.html_attribute_value(
        'a', 'href') == 'url'
    assert structure.html_attribute_value(
        'a', 'href') == 'url'

test_Structure_html_attribute_value()

# Generated at 2022-06-14 00:56:25.088663
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
  assert Structure().html_attribute_value(tag='button', attribute='aria-disabled') != None
  assert Structure().html_attribute_value(tag='button', attribute='autofocus') != None
  assert Structure().html_attribute_value(tag='button', attribute='disabled') != None
  assert Structure().html_attribute_value(tag='button', attribute='form') != None
  assert Structure().html_attribute_value(tag='button', attribute='formaction') != None
  assert Structure().html_attribute_value(tag='button', attribute='formenctype') != None
  assert Structure().html_attribute_value(tag='button', attribute='formmethod') != None
  assert Structure().html_attribute_value(tag='button', attribute='formnovalidate') != None
  assert Structure().html_attribute_value(tag='button', attribute='formtarget')

# Generated at 2022-06-14 00:56:28.368349
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    structureData = Structure()
    structureData.html_attribute_value('a', 'href')
    structureData.html_attribute_value('a', 'title')
    structureData.html_attribute_value('a', 'content')
    structureData.html_attribute_value('a', 'download')

# Generated at 2022-06-14 00:56:30.507813
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    result = structure.css_property()
    print(result)
    assert result != None


# Generated at 2022-06-14 00:56:34.195562
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # Initialize new object of class Structure
    css_property_obj = Structure()
    assert css_property_obj.css_property() != None

# Generated at 2022-06-14 00:56:57.887059
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    results = []
    structure = Structure('en')
    tags = list(HTML_CONTAINER_TAGS.keys())
    # tags = ['a', 'base', 'meta']
    for tag in tags:
        attributes = list(HTML_CONTAINER_TAGS[tag])   # type: ignore
        # attributes = ['href']
        for attribute in attributes:
            result = structure.html_attribute_value(tag, attribute)
            print("Test: Structure_html_attribute_value (tag: " + tag + ", attribute: " +  attribute + "): " + str(result))
            results.append("Test: Structure_html_attribute_value (tag: " + tag + ", attribute: " +  attribute + "): " + str(result))
    return results


# Generated at 2022-06-14 00:57:01.427532
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert isinstance(s.css_property(), str)



# Generated at 2022-06-14 00:57:10.894109
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    assert (s.html_attribute_value(tag='a', attribute='href') == 'url')
    assert (s.html_attribute_value(tag='a', attribute='class') == 'css')
    assert (s.html_attribute_value(tag='a', attribute='style') == 'css')
    assert (s.html_attribute_value(tag='a', attribute='name') == 'word')
    try:
        s.html_attribute_value(tag='a', attribute='test')
    except NotImplementedError:
        pass
    try:
        s.html_attribute_value(tag='test', attribute='href')
    except NotImplementedError:
        pass



# Generated at 2022-06-14 00:57:15.125272
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    metadata = Structure.Meta()
    assert metadata.name == 'structure'
    structure = Structure(seed = 5)
    assert structure.css_property() == "float: left"

# Generated at 2022-06-14 00:57:21.214356
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    a = Structure('en')
    c1 = a.html_attribute_value('img','width')
    c2 = a.html_attribute_value('img','height')
    assert type(c1) == str and type(c2) == str


# Generated at 2022-06-14 00:57:25.403994
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    ls = []
    for _ in range(10):
        ls.append(s.css_property())
    return ls
print(test_Structure_css_property())

# Generated at 2022-06-14 00:57:26.692304
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struct = Structure()
    struct.css_property()


# Generated at 2022-06-14 00:57:28.044914
# Unit test for method css_property of class Structure
def test_Structure_css_property():
  for i in range(10):
    print(Structure().css_property())


# Generated at 2022-06-14 00:57:31.084072
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    print ('test_Structure_css_property', structure.css_property())
    
    

# Generated at 2022-06-14 00:57:36.842010
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    p = Structure()
    result = p._Structure__text.word()
    try:
        assert isinstance(p.css_property(), str)
        assert p.css_property() == result
    except:
        print("Method css_property is broken.")


# Generated at 2022-06-14 00:58:03.993322
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    html_tag = 'a'
    html_attribute = 'href'
    value = 'http://www.internet.org'
    assert Structure().html_attribute_value(html_tag, html_attribute)==value


# Generated at 2022-06-14 00:58:06.594751
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    result = structure.css_property()
    print(result)


# Generated at 2022-06-14 00:58:08.363469
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    st = Structure()
    tag = 'a'
    attribute = 'rel'
    print(st.html_attribute_value(tag,attribute))


# Generated at 2022-06-14 00:58:18.251272
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    new_Structure = Structure()

# Generated at 2022-06-14 00:58:27.805639
# Unit test for method html_attribute_value of class Structure

# Generated at 2022-06-14 00:58:29.427207
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    struct = Structure()
    struct.css_property()
    

# Generated at 2022-06-14 00:58:40.453976
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=1)

# Generated at 2022-06-14 00:58:46.047711
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure"""
    struc = Structure(seed=1)
    assert struc.html_attribute_value() == 'background-color: #f4d3a1'
    assert struc.html_attribute_value(tag='span',attribute='id') == 'heart'
    try:
        struc.html_attribute_value('strong','number')
        assert False
    except NotImplementedError:
        assert True


# Generated at 2022-06-14 00:58:55.952510
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Test method html_attribute_value of class Structure."""
    s = Structure()
    html_tag = 'a'
    attr_name = 'href'
    assert s.html_attribute_value(html_tag, attr_name) == 'https://github.com/'
    attr_name = 'accesskey'
    assert s.html_attribute_value(html_tag, attr_name) == 's'
    attr_name = 'data-mimesis'
    assert s.html_attribute_value(html_tag, attr_name) == 'mimesis'
    attr_name = 'data-mimesis'
    assert s.html_attribute_value(html_tag, attr_name) == 'mimesis'
    attr_name = 'size'
    assert s.html

# Generated at 2022-06-14 00:59:05.469039
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    from mimesis.enums import CSSProperty, CSSSelector
    from mimesis.typing import CSSPropertyType, CSSSelectorType

    s = Structure('en')
    assert s._can_be_instantiated()
    for css_prop, css_val in s._get_choices(CSSProperty).items():
        if (css_prop in CSSProperty.length_properties or
                css_prop in CSSProperty.fixed_properties):
            assert s.css_property() == '{}: {}'.format(css_prop, css_val)

# Generated at 2022-06-14 00:59:59.536113
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure('en','seed')
    print(struct.html())



# Generated at 2022-06-14 01:00:02.616976
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    prop = ""
    for _ in range(1000):
        prop = structure.css_property()
        assert ':' in prop
        assert prop.count(':') == 1 and ';' not in prop

# Generated at 2022-06-14 01:00:06.636367
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure('zh')
    assert structure.css_property() == 'position: relative'
    assert 'color: ' in structure.css_property()