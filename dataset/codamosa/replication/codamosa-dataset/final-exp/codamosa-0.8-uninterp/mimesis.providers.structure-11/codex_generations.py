

# Generated at 2022-06-14 00:52:34.071790
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    str = Structure()
    print(str.html_attribute_value(tag='link',attribute='href'))


# Generated at 2022-06-14 00:52:40.863854
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    print("Unit test for method html_attribute_value of class Structure")
    structure_provider = Structure()
    html_attribute_value = structure_provider.html_attribute_value()
    if isinstance(html_attribute_value, str):
        print("Pass")
    else:
        print("Fail")



# Generated at 2022-06-14 00:52:44.139351
# Unit test for method html_attribute_value of class Structure
def test_Structure_html_attribute_value():
    provider = Structure()
    assert isinstance(provider.html_attribute_value(), str)
    assert isinstance(provider.html_attribute_value(tag="div", attribute="class"), str)