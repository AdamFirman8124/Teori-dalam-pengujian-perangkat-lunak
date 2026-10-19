

# Generated at 2022-06-14 00:52:12.128904
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    tag = 'a'
    attribute = 'href'
    value = s.html_attribute_value(tag=tag, attribute=attribute)
    assert value.startswith('http')

# Generated at 2022-06-14 00:52:14.009801
# Unit test for method css_property of class Structure
def test_Structure_css_property():

	# Test
	structure = Structure()
	result = structure.css_property()

	# Verify
	assert result



# Generated at 2022-06-14 00:52:23.306132
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    s = Structure()
    tag_names = list(HTML_CONTAINER_TAGS.keys())
    attr_names = list(HTML_CONTAINER_TAGS[tag_names[0]])
    res = s.html_attribute_value(tag_names[0], attr_names[0])
    assert len(res) > 0
    res = s.html_attribute_value(attr_names[0])
    assert len(res) > 0
    res = s.html_attribute_value()
    assert len(res) > 0
    

# Generated at 2022-06-14 00:52:28.448033
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # string = ""
    # for i in range(1,30):
    #     string += str(Structure().css_property()) + "\n"
    # print(string)
    # print(Structure().css_property())
    assert Structure().css_property() == "left: auto"


test_Structure_css_property()



# Generated at 2022-06-14 00:52:30.898783
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    structure = Structure()
    i = 0
    while i < 5:
        print (structure.css_property())
        i += 1

# Generated at 2022-06-14 00:52:40.748284
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    provider = Structure()
    assert 'itemprop="name"' in provider.html_attribute_value('meta', 'itemprop')
    assert 'property="og:description"' in provider.html_attribute_value('meta', 'property')
    assert 'href="http://www.example.com"' in provider.html_attribute_value('link', 'href')
    assert 'rel="stylesheet"' in provider.html_attribute_value('link', 'rel')
    assert 'src="http://www.example.com/style.css"' in provider.html_attribute_value('link', 'src')
    assert 'type="text/css"' in provider.html_attribute_value('link', 'type')
    assert 'media="screen, projection"' in provider.html_attribute_value('link', 'media')

# Generated at 2022-06-14 00:52:43.315146
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    S1 = Structure()

    for i in range(1000):
        for i in range(1, 7):
            assert '; ' in S1.css()

# Generated at 2022-06-14 00:52:44.883510
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    s = Structure()
    print(s.css_property())


# Generated at 2022-06-14 00:52:52.484370
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    """Unit test for method html_attribute_value of class Structure"""
    structure = Structure()

    # Test html_attribute_value when tag is None and attribute is None
    tag_attribute_value = structure.html_attribute_value()
    assert tag_attribute_value.find(': ') != -1
    # Test html_attribute_value when tag is not None and attribute is None
    tag = list(HTML_CONTAINER_TAGS)[0]
    tag_attribute_value = structure.html_attribute_value(tag, attribute=None)
    assert tag_attribute_value.find(': ') != -1
    # Test html_attribute_value when tag is None and attribute is not None
    attribute = list(HTML_CONTAINER_TAGS[tag])[0]

# Generated at 2022-06-14 00:52:55.766167
# Unit test for method css_property of class Structure
def test_Structure_css_property():
    # SUT
    s = Structure()

    # run test
    result = s.css_property()

    # assert
    assert isinstance(result, str)
