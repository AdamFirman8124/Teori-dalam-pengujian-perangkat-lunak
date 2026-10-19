

# Generated at 2022-06-13 19:30:52.067387
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError()  # There is no need to initialize the attributes
    return error

# Generated at 2022-06-13 19:30:52.800833
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    pass


# Generated at 2022-06-13 19:30:57.018520
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    params = ["param", "arg"]
    description = "description"
    docstringmeta = DocstringMeta(params, description)
    assert docstringmeta.args == params
    assert docstringmeta.description == description


# Generated at 2022-06-13 19:30:58.610442
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam([':param'], 'description', 'arg', 'type_name', True, 'default')


# Generated at 2022-06-13 19:31:01.143196
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(['param'], 'this is a test', 'arg', 'int', True, 'None')



# Generated at 2022-06-13 19:31:03.819283
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.meta == []


# Generated at 2022-06-13 19:31:06.431990
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    f = DocstringReturns(["abc", "123"], "hello world", "abc", False)
    assert f != None

# Generated at 2022-06-13 19:31:08.467912
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test constructor of class DocstringRaises."""
    DocstringRaises(['a'], 'b', 'c')

# Generated at 2022-06-13 19:31:10.421541
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated("arg: blah blah blah ; blah blah blah", "description","version")


# unit test for constructor of class DocstringMeta

# Generated at 2022-06-13 19:31:13.415894
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    version = '0.0.1'
    description = 'description'
    args = ['args']
    docstring_deprecated = DocstringDeprecated(args, description, version)
    assert docstring_deprecated.args == args
    assert docstring_deprecated.description == description
    assert docstring_deprecated.version == version


# Generated at 2022-06-13 19:31:25.999234
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['raises', 'exception', 'error']
    description = 'error occurred'
    type_name =  None
    test_obj = DocstringRaises(args, description, type_name)
    expected = ['raises', 'exception', 'error']
    assert test_obj.args == expected, "Failed to initialize args"
    expected = 'error occurred'
    assert test_obj.description == expected, "Failed to initialize description"
    expected = None
    assert test_obj.type_name == expected, "Failed to initialize type_name"


# Generated at 2022-06-13 19:31:28.305846
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(args = [], description = None, type_name = None)


# Generated at 2022-06-13 19:31:35.553204
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstr = DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    assert docstr.args == ['arg']
    assert docstr.description == 'description'
    assert docstr.arg_name == 'arg_name'
    assert docstr.type_name == 'type_name'
    assert docstr.is_optional == True
    assert docstr.default == 'default'


# Generated at 2022-06-13 19:31:47.220862
# Unit test for constructor of class Docstring
def test_Docstring():
    test_Docstring = Docstring()
    assert test_Docstring.short_description == None, "short description should be None"
    assert test_Docstring.long_description == None, "long description should be None"
    assert test_Docstring.blank_after_short_description == False, "blank after short description should be False"
    assert test_Docstring.blank_after_long_description == False, "blank after long description should be False"
    assert test_Docstring.meta == [], "meta should be an empty list"
    assert test_Docstring.params == [], "params should be an empty list"
    assert test_Docstring.raises == [], "raises should be an empty list"
    assert test_Docstring.returns == None, "returns should be None"

# Generated at 2022-06-13 19:31:50.938483
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    ds = DocstringDeprecated(["deprecated"], "This function is deprecated")
    assert ds.args == ["deprecated"]
    assert ds.description == "This function is deprecated"
    assert ds.version == None


# Generated at 2022-06-13 19:31:58.243965
# Unit test for constructor of class Docstring
def test_Docstring():
    """Unit test for constructor of class Docstring"""
    x = Docstring()
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description == False
    assert x.blank_after_long_description == False
    assert x.meta == []


# Generated at 2022-06-13 19:32:02.734160
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Unit test for constructor of class DocstringParam"""
    obj = DocstringParam(["param"], None, 'keyword', 'int', True, 0)
    assert obj.is_optional == True
    assert obj.return_name == None


# Generated at 2022-06-13 19:32:08.385980
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = parse_docstring('''
    A docstring
    
    :param arg_name: arg description
    :param arg_name2: arg description2
    :raises TypeError: if something happens
    :return: value description
    ''')
    print(docstring)

# Generated at 2022-06-13 19:32:13.179324
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []


# Generated at 2022-06-13 19:32:18.593941
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    instance = DocstringReturns(["param", "type", "default"], "description", "type", False)
    assert instance.type_name == "type"
    assert instance.is_generator == False
    assert instance.return_name == None

# Generated at 2022-06-13 19:32:33.606146
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test for constructor of class DocstringRaises"""
    args = ['ba']
    description = 'This is a test'
    type_name = 'int'
    d=DocstringRaises(args, description, type_name)
    an= d.args == ['ba']
    bn = d.description == 'This is a test'
    cn = d.type_name == 'int'
    assert an and bn and cn
    

# Generated at 2022-06-13 19:32:42.242733
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    rtype = "Dict[str, str]"
    rname = "result"
    rdesc = "The result is a dictionary containing all results from the query."
    return_item = DocstringReturns(
        args=[":returns", rtype],
        description=rdesc,
        type_name=rtype,
        is_generator=False,
        return_name=rname,
    )
    assert return_item.type_name == rtype
    assert return_item.description == rdesc
    assert return_item.return_name == rname



# Generated at 2022-06-13 19:32:45.639742
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    doc = DocstringMeta(["para", "parameter", "arg", "argument"], "describes parameters")
    assert doc.args == ["para", "parameter", "arg", "argument"]
    assert doc.description == "describes parameters"


# Generated at 2022-06-13 19:32:47.507231
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("error")
    except ParseError as e:
        assert e.args == ("error",)


# Generated at 2022-06-13 19:32:50.446130
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    exception = DocstringRaises(["raises"], "description", "ValueError")
    assert exception.args == ["raises"]
    assert exception.description == "description"
    assert exception.type_name == "ValueError"


# Generated at 2022-06-13 19:32:52.664553
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(['returns'], "description", "type_name", True)


# Generated at 2022-06-13 19:32:55.082837
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    s = "My description"
    t = "Some type"
    r = DocstringRaises(["a"], s, t)
    assert r.args == ["a"]
    assert r.description == s
    assert r.type_name == t

# Generated at 2022-06-13 19:33:00.057961
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert isinstance(DocstringReturns([], ""), object)
    assert DocstringReturns([], "").type_name == None
    assert DocstringReturns([], "").is_generator == None
    assert DocstringReturns([], "").description == None


# Generated at 2022-06-13 19:33:06.551623
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert(DocstringMeta([':param'], 'description') == DocstringMeta([':param'], 'description'))
    assert(DocstringMeta([':param'], 'description') != DocstringMeta([':raises'], 'description'))
    assert(DocstringMeta([':param'], 'descrip') != DocstringMeta([':param'], 'description'))


# Generated at 2022-06-13 19:33:14.527290
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    meta = DocstringRaises([], "", "")
    assert meta.type_name == ""
    assert meta.description == ""
    
    meta = DocstringRaises([], "desc", "type")
    assert meta.type_name == "type"
    assert meta.description == "desc"
    
    meta = DocstringRaises(["arg1", "arg2"], "desc", "type_name")
    assert meta.type_name == "type_name"
    assert meta.description == "desc"


# Generated at 2022-06-13 19:33:32.133550
# Unit test for constructor of class ParseError
def test_ParseError():
    a = ParseError()
    assert(type(a) == ParseError)
    b = ParseError("dummy_msg")
    assert(type(b) == ParseError)
    c = ParseError(Raises_Keywords_msg="dummy_msg")
    assert(type(c) == ParseError)


# Generated at 2022-06-13 19:33:35.381375
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    meta_info = DocstringDeprecated(args=["dummy_args"], description="dummy_description", version="dummy_version")
    assert meta_info.args[0] == "dummy_args"
    assert meta_info.description == "dummy_description"
    assert meta_info.version == "dummy_version"


# Generated at 2022-06-13 19:33:47.953708
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam('args: str, description: str, arg_name: str, type_name: str, is_optional: bool, default: str', 'test description', 'test arg_name', 'test type_name', 'test is_optional', 'test default')
    assert(dp.args == 'args: str, description: str, arg_name: str, type_name: str, is_optional: bool, default: str')
    assert(dp.description == 'test description')
    assert(dp.arg_name == 'test arg_name')
    assert(dp.type_name == 'test type_name')
    assert(dp.is_optional == 'test is_optional')
    assert(dp.default == 'test default')

if __name__ == '__main__': test_DocstringParam()

# Generated at 2022-06-13 19:33:58.795920
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    # Test short_description
    assert docstring.short_description is None
    docstring.short_description = "short_description"
    assert docstring.short_description == "short_description"
    # Test blank_after_short_description
    assert docstring.blank_after_short_description is False
    docstring.blank_after_short_description = True
    assert docstring.blank_after_short_description is True
    # Test long_description
    assert docstring.long_description is None
    docstring.long_description = "long_description"
    assert docstring.long_description == "long_description"
    # Test blank_after_long_description
    assert docstring.blank_after_long_description is False
    docstring.blank_after_long_description = True

# Generated at 2022-06-13 19:34:00.974363
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert isinstance(DocstringMeta([1, 2, 3], "description"), DocstringMeta)


# Generated at 2022-06-13 19:34:02.783624
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["param", "x", ":", "the", "parameter"], "A parameter called x")

# Generated at 2022-06-13 19:34:05.436544
# Unit test for constructor of class ParseError
def test_ParseError():
    exception = ParseError('testing')
    assert(exception is not None)


# Generated at 2022-06-13 19:34:08.670687
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert doc.meta == []

# Generated at 2022-06-13 19:34:10.101558
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(['deprecated'], 'This is why something is deprecated', '2.0')


# Generated at 2022-06-13 19:34:15.742192
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(args=["description"],description="description",version="1.0")
    assert docstring.description == "description"
    assert docstring.version == "1.0"
    docstring = DocstringDeprecated(args=["description"],description="description",version=None)
    assert docstring.description == "description"
    assert docstring.version is None


# Generated at 2022-06-13 19:34:46.425980
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    myDocstringReturns = DocstringReturns(args=["Param1", "Param2"], description="This is a description", type_name="int", is_generator=False, return_name="some_name")
    assert myDocstringReturns.description == "This is a description"

# Generated at 2022-06-13 19:34:50.275264
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd = DocstringDeprecated(['deprecated'], 'description', 'version')
    assert dd.args == ['deprecated']
    assert dd.description == 'description'
    assert dd.version == 'version'


# Generated at 2022-06-13 19:34:53.822877
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
  docstringRaises = DocstringRaises(["test1", "test2"], "test", "test")
  assert(docstringRaises.args == ["test1", "test2"])
  assert(docstringRaises.description == "test")
  assert(docstringRaises.type_name == "test")


# Generated at 2022-06-13 19:34:56.875658
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises([], 'test_description', 'test_type_name')



# Generated at 2022-06-13 19:35:02.980552
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(['deprecated', 'since'], 'description', '2.0')
    assert a.version == '2.0'
    b = DocstringDeprecated(['deprecated'], 'description', '3.0')
    assert b.description == 'description'


# Generated at 2022-06-13 19:35:05.916117
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    def test_function(a):
        """Return nothing."""
        return None

    assert test_function.__doc__ == 'Return nothing.'

# Generated at 2022-06-13 19:35:09.600083
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Test initialization
    param = DocstringParam(["param"], "b is a parameter", "b", "int", True, 5)
    # Test assertion
    assert isinstance(param, DocstringParam)


# Generated at 2022-06-13 19:35:11.152889
# Unit test for constructor of class ParseError
def test_ParseError():
    
    with pytest.raises(ParseError):
        ValueError("test")


# Generated at 2022-06-13 19:35:19.291005
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = [':param']
    dsc = 'desc'
    arg_name = 'arg_name'
    type_name = 'type_name'
    is_optional = True
    default = 'default'
    docstring = DocstringParam(args, dsc, arg_name, type_name, is_optional, default)
    print(docstring)
test_DocstringParam()


# Generated at 2022-06-13 19:35:27.464738
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
  p = DocstringParam(['param'], 'description', 'arg_name', 'type_name', True, 'default')
  assert p.description == 'description'
  assert p.arg_name == 'arg_name'
  assert p.type_name == 'type_name'
  assert p.is_optional == True
  assert p.default == 'default'


# Generated at 2022-06-13 19:36:26.191447
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    item = DocstringMeta(args=['param'], description=' some description')
    assert item.args == ['param']
    assert item.description == ' some description'


# Generated at 2022-06-13 19:36:30.055203
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError(RuntimeError)
    assert type(err) is ParseError
    assert err.args[0] == RuntimeError


# Generated at 2022-06-13 19:36:32.648818
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('test error')
        assert False
    except ParseError as e:
        assert str(e) == 'test error'


# Generated at 2022-06-13 19:36:34.288164
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(RuntimeError):
        raise(ParseError("Oops!"))


# Generated at 2022-06-13 19:36:37.496789
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = []
    description = 'hello'
    version = '0.0.1'
    docstringDeprecated = DocstringDeprecated(args, description, version)
    assert docstringDeprecated.version == version


# Generated at 2022-06-13 19:36:39.523919
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    metadata = DocstringMeta(["a","b"], "This is a description")
    assert metadata.args == ["a","b"]
    assert metadata.description == "This is a description"
    

# Generated at 2022-06-13 19:36:44.561775
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = []
    type_name = "TypeName"
    desc = "This is a description"
    doc_meta = DocstringRaises(args,type_name,desc)
    assert doc_meta.args == args
    assert doc_meta.description == desc
    assert doc_meta.type_name == type_name


# Generated at 2022-06-13 19:36:47.075157
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("this is a test")
    assert err.args[0] == "this is a test"


# Generated at 2022-06-13 19:36:53.786435
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    met1 = DocstringRaises(["raises"], "description", "ValueError")
    assert met1.description == "description"
    assert met1.type_name == "ValueError"
    assert met1.args[0] == "raises"
    assert isinstance(met1, DocstringRaises)


# Generated at 2022-06-13 19:36:56.424284
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("Testing ParseError")
    assert error.args[0] == "Testing ParseError"


# Generated at 2022-06-13 19:38:51.656175
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Test Branch Coverage
    args = ["param"]
    description = "description"
    DocstringMeta(args, description)

# Generated at 2022-06-13 19:38:52.925547
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('test')
    except ParseError:
        pass


# Generated at 2022-06-13 19:38:55.693957
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = []
    description = 'this is a test'
    test = DocstringMeta(args, description)
    assert test.args == args and test.description == description


# Generated at 2022-06-13 19:38:57.916960
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    arg = ["param"]
    description = "implementation"
    meta = DocstringMeta(arg, description)
    assert meta.args == arg
    assert meta.description == description


# Generated at 2022-06-13 19:39:03.044247
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['param']
    description = "Test object"
    arg_name = "test"
    type_name = "Test"
    is_optional = False
    default = "None"
    test_instance = DocstringParam(args, description, arg_name, type_name, is_optional, default)


# Generated at 2022-06-13 19:39:11.997975
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test DocstringRaises constructor"""

# Generated at 2022-06-13 19:39:15.998659
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert isinstance(DocstringMeta, object)
    dm = DocstringMeta(['a', 'b', 'c'], 'd')
    assert dm.args == ['a', 'b', 'c']
    assert dm.description == 'd'


# Generated at 2022-06-13 19:39:17.928545
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    dsRaises = DocstringRaises([], None, None)
    assert dsRaises


# Generated at 2022-06-13 19:39:25.303925
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param_1 = DocstringParam([], str, "firstArg", "int", True, "firstArgDefault")
    assert param_1.args == []
    assert param_1.arg_name == "firstArg"
    assert param_1.default == "firstArgDefault"
    assert param_1.type_name == "int"

    param_2 = DocstringParam([], str, "firstArg", "int", True, "firstArgDefault")
    assert param_2.args == []
    assert param_2.arg_name == "firstArg"
    assert param_2.default == "firstArgDefault"
    assert param_2.type_name == "int"

    param_3 = DocstringParam([], str, "secondArg", "float", True, "secondArgDefault")
    assert param_3.args == []

# Generated at 2022-06-13 19:39:27.299082
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    c =DocstringRaises(None,None)
    assert c.get() == None
    print("Test passed.")
