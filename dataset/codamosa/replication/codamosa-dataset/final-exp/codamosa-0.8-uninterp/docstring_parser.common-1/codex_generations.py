

# Generated at 2022-06-13 19:30:58.153158
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test for DocstringMeta."""
    try:
        assert (
            DocstringMeta(["param"], "description").args == ["param"]
        ), "DocstringMeta constructor failed."
        assert (
            DocstringMeta(["param"], "description").description
            == "description"
        ), "DocstringMeta constructor failed."
    except:
        raise AssertionError


# Generated at 2022-06-13 19:31:00.600497
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("test")
    assert err.args[0] == "test"



# Generated at 2022-06-13 19:31:03.820010
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test = DocstringDeprecated([":"], "description", "version")
    assert test.args == [":"]
    assert test.description == "description"
    assert test.version == "version"


# Generated at 2022-06-13 19:31:08.599825
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc_depr = DocstringDeprecated(args=['param'],description='description',version='1.0')
    assert doc_depr.args == ['param']
    assert doc_depr.description == 'description'
    assert doc_depr.version == '1.0'

# Generated at 2022-06-13 19:31:11.062582
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(args=None, description=None, version=None)
    assert d.version is None
    assert d.description is None
    assert d.args is None

# Generated at 2022-06-13 19:31:13.297171
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(args = ['a', 'b', 'c'],
                         description = 'meta information')
    assert meta.args == ['a', 'b', 'c']
    assert meta.description == 'meta information'


# Generated at 2022-06-13 19:31:13.851624
# Unit test for constructor of class ParseError
def test_ParseError():
    assert True


# Generated at 2022-06-13 19:31:18.716912
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    obj = DocstringParam(args=["param"],
                         description="description",
                         arg_name="arg",
                         type_name=None,
                         is_optional=True,
                         default=None)
    assert(obj.args == ["param"])
    assert(obj.description == "description")
    assert(obj.arg_name == "arg")
    assert(obj.type_name is None)
    assert(obj.is_optional == True)
    assert(obj.default is None)


# Generated at 2022-06-13 19:31:23.406940
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = [':param', 'arg']
    description = "description"
    arg_name = "arg"
    arg = DocstringParam(args, description, arg_name,
                         type_name=None, is_optional=None, default=None)



# Generated at 2022-06-13 19:31:26.447889
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    s = "Doc string :param arg: description"
    lines = []
    lines.append(s)
    r = DocstringReturns(lines, "desc", "str")


# Generated at 2022-06-13 19:31:31.437181
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for DocstringRaises."""
    pass

# Generated at 2022-06-13 19:31:34.693465
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(["param"], "description")
    assert d.args == ["param"]
    assert d.description == "description"


# Generated at 2022-06-13 19:31:37.362769
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError_obj = ParseError()
    assert isinstance(ParseError_obj, ParseError)

# Generated at 2022-06-13 19:31:39.047834
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(['a'],'asdf',"b","c")

# Generated at 2022-06-13 19:31:43.565143
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(args,description,version).args == args
    assert DocstringDeprecated(args,description,version).description == description
    assert DocstringDeprecated(args,description,version).version == version


# Generated at 2022-06-13 19:31:46.747338
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    value1 = ["a", "b"]
    value2 = "test"
    DocstringMeta(value1, value2)

test_DocstringMeta()


# Generated at 2022-06-13 19:31:55.217311
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = Docstring()
    docstring.short_description = "short description"
    docstring.long_description = "long description"
    docstring.blank_after_short_description = False
    docstring.blank_after_long_description = False
    docstring.meta = []

    assert docstring.short_description == "short description"
    assert docstring.long_description == "long description"
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

# Generated at 2022-06-13 19:32:07.266472
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["param", "arg", "argument", "attribute", "key", "keyword"]
    description = "Docstring description"
    return_name = "return_name"
    type_name = "type_name"
    is_generator = "is_generator"
    r = DocstringReturns(args=args,
                         description=description,
                         return_name=return_name,
                         type_name=type_name,
                         is_generator=is_generator)
    assert r.args == args
    assert r.description == description
    assert r.return_name == return_name
    assert r.type_name == type_name
    assert r.is_generator == is_generator

# Generated at 2022-06-13 19:32:17.063116
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    ds.short_description = "foo"
    ds.long_description = "bar"
    ds.blank_after_short_description = True
    ds.blank_after_long_description = True
    # Test _get_params on empty Docstring
    assert ds.params == []
    # Test _get_raises on empty Docstring
    assert ds.raises == []
    # Test _get_returns on empty Docstring
    assert ds.returns == None
    # Test _get_deprecation on empty Docstring
    assert ds.deprecation == None
    meta = DocstringMeta([], "")
    ds.meta.append(meta)
    # Test _get_params on Docstring with DocstringMeta
    assert ds.params == []
   

# Generated at 2022-06-13 19:32:24.019299
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["args"]
    description = "description"
    type_name = "type_name"
    is_generator = False
    return_name = None
    test_object = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert(test_object.args == ["args"])
    assert(test_object.description == "description")
    assert(test_object.type_name == "type_name")
    assert(test_object.is_generator == False)
    assert(test_object.return_name == None)

# Generated at 2022-06-13 19:32:35.550660
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    res = DocstringReturns(["a","b"],None,None,False)
    assert res.args == ["a","b"]
    assert res.description == None
    assert res.type_name == None
    assert res.is_generator == False
    assert res.return_name == None

# Generated at 2022-06-13 19:32:38.756076
# Unit test for constructor of class Docstring
def test_Docstring():
	a = Docstring()
	assert(a.params is not None)
	assert(a.raises is not None)
	assert(a.returns is not None)
	assert(a.deprecation is not None)

# Generated at 2022-06-13 19:32:42.587863
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta_Test = DocstringMeta(['args'], 'Docstring description')
    assert DocstringMeta_Test.args == ['args']
    assert DocstringMeta_Test.description == 'Docstring description'


# Generated at 2022-06-13 19:32:51.922295
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc_string1 = "Return values are not known before calling the method."
    doc_string2 = "Return values are not known before calling the method."
    DocstringReturns1 = DocstringReturns(["return"], doc_string1, "", "", True)
    DocstringReturns2 = DocstringReturns(["return"], doc_string2, "", "", True)
    assert DocstringReturns1.args == ["return"]
    assert DocstringReturns1.description == doc_string1
    assert DocstringReturns1.type_name == ""
    assert DocstringReturns1.is_generator == True
    assert DocstringReturns1.return_name == None
    assert DocstringReturns1 == DocstringReturns2
    DocstringReturns3 = DocstringReturns(["return"], doc_string1, "", "", True, None)

# Generated at 2022-06-13 19:32:57.208542
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dstringparam = DocstringParam([],None, "arg_name", None, None, None)
    assert dstringparam.args == [], "test_DocstringParam failed!"
    assert dstringparam.description == None, "test_DocstringParam failed!"
    assert dstringparam.arg_name == "arg_name", "test_DocstringParam failed!"
    assert dstringparam.type_name == None, "test_DocstringParam failed!"
    assert dstringparam.is_optional == None, "test_DocstringParam failed!"
    assert dstringparam.default == None, "test_DocstringParam failed!"


# Generated at 2022-06-13 19:33:00.408851
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for constructor of class ParseError."""
    try:
        raise ParseError("Test")
    except ParseError as e:
        assert e.args == ("Test",)

# Generated at 2022-06-13 19:33:09.291365
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """
    DocstringRaises(args, description, type_name):

    :param args: list of arguments. The exact content of this variable is
                 dependent on the kind of docstring; it's used to distinguish between
                 custom docstring meta information items.
    :param description: associated docstring description.
    :param type_name:
    """
    args = ["param", "arg"]
    description = "DocstringRaises class unit test"
    type_name = "TypeError"
    try:
        DocstringRaises(args, description, type_name)
    except ParseError as e:
        print("Parsing error:", e)



# Generated at 2022-06-13 19:33:14.994299
# Unit test for constructor of class Docstring
def test_Docstring():
    # instantiate a Docstring object
    docstring = Docstring()

    # assert the values are empty
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description 
    assert not docstring.blank_after_long_description
    assert docstring.meta == []


# Generated at 2022-06-13 19:33:21.893966
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert [0, 0, 1] == DocstringReturns([0, 0, 1], 'None', 'None', False).args
    assert 'None' == DocstringReturns([0, 0, 1], 'None', 'None', False).description
    assert 'None' == DocstringReturns([0, 0, 1], 'None', 'None', False).type_name
    assert False == DocstringReturns([0, 0, 1], 'None', 'None', False).is_generator
    assert 'None' == DocstringReturns([0, 0, 1], 'None', 'None', False).return_name



# Generated at 2022-06-13 19:33:25.342045
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    meta = DocstringMeta(['Hello'], 'World')
    assert isinstance(meta, DocstringMeta)
    assert meta.args == ['Hello']
    assert meta.description == 'World'


# Generated at 2022-06-13 19:33:50.075695
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # test if constructor of DocstringRaises creates a proper object
    args = ["a", "b", "c"]
    description = "test"
    type_name = "float"
    test_obj = DocstringRaises(args, description, type_name)
    assert test_obj.args == args
    assert test_obj.description == description
    assert test_obj.type_name == type_name
    # test if constructor of DocstringRaises raises TypeError when the description is not a string
    args = ["a", "b", "c"]
    description = 5
    type_name = "float"
    with pytest.raises(TypeError):
        test_obj = DocstringRaises(args, description, type_name)


# Generated at 2022-06-13 19:33:54.212104
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    str = DocstringRaises(":raises", "type_name", "description")
    assert str.args == ":raises"
    assert str.type_name == "type_name"
    assert str.description == "description"


# Generated at 2022-06-13 19:33:59.762095
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    str = "a"
    docstring_param = DocstringParam([str], "the a parameter.", "a", "str", True, None)
    assert docstring_param.args[0] == str
    assert docstring_param.description == "the a parameter."
    assert docstring_param.arg_name == "a"
    assert docstring_param.type_name == "str"
    assert docstring_param.is_optional == True
    assert docstring_param.default == None


# Generated at 2022-06-13 19:34:03.692902
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    item = DocstringRaises(None, "ArgumentError", "This argument is not a boolean")
    print(item)

if __name__ == "__main__":
    test_DocstringRaises()


# Generated at 2022-06-13 19:34:09.280649
# Unit test for constructor of class Docstring
def test_Docstring():
    test_docstring = Docstring()
    assert test_docstring.short_description == None
    assert test_docstring.long_description == None
    assert test_docstring.blank_after_short_description == False
    assert test_docstring.blank_after_long_description == False
    assert isinstance(test_docstring.meta, list)
    assert test_docstring.meta == []


# Generated at 2022-06-13 19:34:10.029321
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError()


# Generated at 2022-06-13 19:34:11.326700
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([], None, None, False) != None

# Generated at 2022-06-13 19:34:13.165460
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(["raises"], "desc", "vector")


# Generated at 2022-06-13 19:34:15.739156
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['args'], 'description', 'version')
    assert d.description == 'description'
    assert d.version == 'version'


# Generated at 2022-06-13 19:34:25.752013
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    expected_short_description = 'A long time ago in a galaxy far, far away...'
    expected_long_description = 'It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.'
    expected_blank_after_short_description = False
    expected_blank_after_long_description = False
    expected_param = [DocstringParam(['param', 'arg', 'arguments'], 'description', 'arg_name', 'type_name', 'is_optional', 'default')]
    expected_raise = [DocstringRaises(['raises', 'raise', 'except', 'exception'], 'ValueError', 'if something happens')]

# Generated at 2022-06-13 19:34:57.344514
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam([], None, '' , "", None, "")
    assert DocstringParam('', None, '', "", None, "")


# Generated at 2022-06-13 19:35:10.280098
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    print("Testing DocStringParam")
    DocstringParam([":param"], "type", "name", "int", True, "123")
    DocstringParam([":param"], "type", "name", "int", True, None)
    DocstringParam([":param"], "type", "name", "int", False, "123")
    DocstringParam([":param"], "type", "name", "int", False, None)

    DocstringParam([":param"], None, "name", "int", True, "123")
    DocstringParam([":param"], None, "name", "int", True, None)
    DocstringParam([":param"], None, "name", "int", False, "123")
    DocstringParam([":param"], None, "name", "int", False, None)


# Generated at 2022-06-13 19:35:13.419227
# Unit test for constructor of class ParseError
def test_ParseError():
    
    # Make sure the constructor does not crash
    ParseError('error')

# UT for constructor of class DocstringMeta

# Generated at 2022-06-13 19:35:15.357593
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises(["the","args"], "the description", "the type name")


# Generated at 2022-06-13 19:35:17.180793
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test_docstring_deprecated = DocstringDeprecated(['param'], 'test', '1.0')
    print(test_docstring_deprecated.version)


# Generated at 2022-06-13 19:35:18.909961
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(['raises ValueError: '], ' if something happens', 'ValueError')
    assert True

# Generated at 2022-06-13 19:35:22.911689
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    arg_name = "test_arg"
    type_name = "int"
    is_optional = True
    default = 42

    dict_test_param = DocstringParam(["param"], "test description", arg_name, type_name, is_optional, default)

    assert(dict_test_param.arg_name == arg_name)
    assert(dict_test_param.type_name == type_name)
    assert(dict_test_param.is_optional == is_optional)
    assert(dict_test_param.default == default)


# Generated at 2022-06-13 19:35:27.792467
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ret = DocstringReturns(["return"], "", None, False)
    assert ret.type_name is None, "type_name should be None"
    assert ret.is_generator is False, "is_generator should be False"
    assert ret.return_name is None, "return_name name should be None"



# Generated at 2022-06-13 19:35:32.471388
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated([""], "", None)
    assert a.version is None
    assert a.description == ""
    assert a.args == [""]
    b = DocstringDeprecated(["", "", "", "", ""], "", "")
    assert b.version == ""
    assert b.description == ""
    assert b.args == ["", "", "", "", ""]
    c = DocstringDeprecated("", "", "")
    assert c.version == ""
    assert c.description == ""
    assert c.args == []
    d = DocstringDeprecated("", None, None)
    assert d.version is None
    assert d.description == ""
    assert d.args == []


# Generated at 2022-06-13 19:35:38.842068
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test_name = 'test_name'
    test_type = 'test_type'
    test_description = 'test_description'
    test_is_optional = False
    test_default = 'test_default'
    docstring_param = DocstringParam('test_param', test_description, test_name, test_type, test_is_optional, test_default)
    assert docstring_param.args == 'test_param'
    assert docstring_param.description == test_description
    assert docstring_param.arg_name == test_name
    assert docstring_param.type_name == test_type
    assert docstring_param.is_optional == test_is_optional
    assert docstring_param.default == test_default



# Generated at 2022-06-13 19:36:37.402151
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(['arg'], 'desc').args == ['arg']
    assert DocstringMeta(['arg'], 'desc').description == 'desc'


# Generated at 2022-06-13 19:36:39.251130
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(["a", "b", "c"], "d", "e", False)  # noqa: B014

# Generated at 2022-06-13 19:36:47.965040
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    val = DocstringReturns(args = ["arg1", "arg2"], description = "this is a test", 
    type_name = "str", is_generator = False, return_name = "ret")
    assert val.args == ["arg1", "arg2"]
    assert val.description == "this is a test"
    assert val.type_name == "str"
    assert val.is_generator == False
    assert val.return_name == "ret"
if __name__ == "__main__":
    test_DocstringReturns()


# Generated at 2022-06-13 19:36:52.717414
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    obj = DocstringMeta(args=["param", "arg", "argument"], description=":test")
    assert obj.args == ["param", "arg", "argument"]
    assert obj.description == ":test"


# Generated at 2022-06-13 19:36:58.743420
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(["param", "y"], "Description", "x", "int", True, "0")
    assert a.args == ["param", "y"]
    assert a.description == "Description"
    assert a.arg_name == "x"
    assert a.type_name == "int"
    assert a.is_optional == True
    assert a.default == "0"


# Generated at 2022-06-13 19:37:04.033379
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    meta = DocstringDeprecated(['deprecated', 'since', '1.0'], 'this is deprecated', '1.0')
    assert meta.args == ['deprecated', 'since', '1.0']
    assert meta.description == 'this is deprecated'
    assert meta.version == '1.0'


# Generated at 2022-06-13 19:37:09.245881
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    '''Docstring:
    :param arg: description
    '''
    test_meta = DocstringMeta([':param', 'arg'], 'description')
    assert test_meta.args == [':param', 'arg']
    assert test_meta.description == 'description'



# Generated at 2022-06-13 19:37:10.890037
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(RuntimeError):
        raise ParseError("Error message")



# Generated at 2022-06-13 19:37:13.431992
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dsd = DocstringDeprecated(['a'], '', 'b')
    assert(dsd.args == ['a'])
    assert(dsd.description == '')
    assert(dsd.version == 'b')

# Generated at 2022-06-13 19:37:16.063718
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns.__init__(self, args, description, type_name, is_generator, return_name)


# Generated at 2022-06-13 19:39:16.501902
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert isinstance(DocstringRaises(['a'], 'a', 'a').args, list)
    assert isinstance(DocstringRaises(['a'], 'a', 'a').description, str)
    assert isinstance(DocstringRaises(['a'], 'a', 'a').type_name, str)


# Generated at 2022-06-13 19:39:23.008141
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_param = DocstringParam(args=["param", "arg"], description="Description", arg_name="arg_name", type_name="type_name", is_optional=True, default="blabla")

    assert docstring_param.args == ["param", "arg"]
    assert docstring_param.description == "Description"
    assert docstring_param.arg_name == "arg_name"
    assert docstring_param.type_name == "type_name"
    assert docstring_param.is_optional == True
    assert docstring_param.default == "blabla"

# Generated at 2022-06-13 19:39:28.444791
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    try:
        DocstringReturns(None, None, None, None, None)
        print('Success')
    except Exception:
        print('Error: Wrong constructor')
    try:
        DocstringReturns([], None, None, None, None)
        print('Success')
    except Exception:
        print('Error: Wrong constructor')
    try:
        DocstringReturns([], [], [], [], [])
        print('Success')
    except Exception:
        print('Error: Wrong constructor')
    try:
        DocstringReturns(['a'], 'b', 'c', 'd', 'e')
        print('Success')
    except Exception:
        print('Error: Wrong constructor')

# Generated at 2022-06-13 19:39:31.605594
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []



# Generated at 2022-06-13 19:39:33.670892
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated([":deprecated", ":depr", ":rm"], "description", "1.0")

# Generated at 2022-06-13 19:39:37.579743
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated"]
    description = "description"
    version = "version"
    doc = DocstringDeprecated(args, description, version)
    assert doc.args == ["deprecated"]
    assert doc.description == description
    assert doc.version == version


# Generated at 2022-06-13 19:39:39.189906
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["param", "fname"]
    description = "The name of the file"
    doc_str = DocstringMeta(args, description)
    assert doc_str.args == args
    assert doc_str.description == description


# Generated at 2022-06-13 19:39:41.535619
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(["1","2"], "3")
    assert d.args == ["1", "2"]
    assert d.description == "3"


# Generated at 2022-06-13 19:39:42.469082
# Unit test for constructor of class ParseError
def test_ParseError():
    exc = ParseError('')



# Generated at 2022-06-13 19:39:43.679365
# Unit test for constructor of class ParseError
def test_ParseError():
    text = "Sample"
    e = ParseError(text)
    assert(e.args[0] == text)
