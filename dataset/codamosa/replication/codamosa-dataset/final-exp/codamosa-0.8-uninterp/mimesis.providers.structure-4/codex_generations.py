

# Generated at 2022-06-14 00:52:27.309761
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    struct = Structure()
    # Test case when tag is None
    try:
        struct.html_attribute_value()
    except NotImplementedError:
        # Test case when attribute is None
        try:
            struct.html_attribute_value("div")
        except NotImplementedError:
            # Test case when tag is not supported
            try:
                struct.html_attribute_value("Unsupported_tag")
            except NotImplementedError:
                # Test case when attribute is not supported
                try:
                    struct.html_attribute_value("Unsupported_tag","Unsupport_attr")
                except NotImplementedError:
                    pass

# Generated at 2022-06-14 00:52:32.213007
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    from mimesis.builtins import RussiaSpecProvider
    from mimesis.enums import Gender

    s = Structure(RussiaSpecProvider)
    for _ in range(10):
        c = s.css_property()
        assert isinstance(c, str)
        assert len(c.split(':')) == 2


# Generated at 2022-06-14 00:52:33.993066
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    x = Structure()
    assert x.css_property() in CSS_PROPERTIES.keys()


# Generated at 2022-06-14 00:52:38.863450
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Check if method html_attribute_value of class Structure
    returns a string.
    """
    structure = Structure()
    result = structure.html_attribute_value()
    assert isinstance(result, str)

# Generated at 2022-06-14 00:52:41.997119
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
	pass



# Generated at 2022-06-14 00:52:49.912234
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure(seed=1)
    text = 'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur blandit'
    assert s.html_attribute_value() == '#ffffff'    
    assert s.html_attribute_value() == '#ff0000'    
    assert s.html_attribute_value() == '#ff0000'    
    assert s.html_attribute_value() == '#ff0000'    
    assert s.html_attribute_value() == '#cccccc'    
    assert s.html_attribute_value() == '#cccccc'    
    assert s.html_attribute_value() == '#cccccc'    
    assert s.html_attribute_value() == '#cccccc'    

# Generated at 2022-06-14 00:52:52.787510
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    locale = 'en'
    seed = 10

    struc = Structure(locale, seed)

    tag_name = 'a'
    attr_name = 'target'

    exp_result = '_blank'
    check_result = struc.html_attribute_value(tag_name,attr_name)

    assert check_result == exp_result

# Generated at 2022-06-14 00:52:55.766595
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    assert len(s.css_property()) > 0
    assert s.css_property() == 'color: #6a33ed'


# Generated at 2022-06-14 00:52:56.816956
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    print(structure.css_property())

# Generated at 2022-06-14 00:53:06.483699
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    # without args
    htag = HTML_CONTAINER_TAGS.keys()
    attrs = htag.copy()
    for i in htag:
        if isinstance(i, (str)):
            attrs.remove(i)
    values = []
    for i in attrs:
        if isinstance(i, (str)):
            values.append(i)
    attributes = values.copy()
    for i in values:
        if isinstance(i, (str)):
            attributes.remove(i)
    for i in range(10):
        tag = Structure().random.sample(values, k=1)
        assert Structure().html_attribute_value() == tag[0]

    # with args
    for i in range(10):
        structure = Structure()