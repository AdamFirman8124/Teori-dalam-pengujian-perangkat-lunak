

# Generated at 2022-06-13 19:30:57.560774
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d_param = DocstringParam(
        args=[":param"],
        description="Example Description",
        arg_name="Example Name",
        type_name="Example Type",
        is_optional=True,
        default="Example Default Value"
    )


# Generated at 2022-06-13 19:30:59.649764
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated([], 'docstring Deprecated', 'version') is not None
    

# Generated at 2022-06-13 19:31:04.190102
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:31:07.150948
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(None, None, None)
    assert a.type_name is None and a.description is None
    assert a.args is None



# Generated at 2022-06-13 19:31:16.966953
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """DocstringParam constructor should not raise a TypeError."""
    param = DocstringParam(
        args=[
            'param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'
        ],
        description='',
        arg_name='',
        type_name=None,
        is_optional=None,
        default=None,
    )
    assert param.args == [
        'param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'
    ]
    assert param.description == ''
    assert param.arg_name == ''
    assert param.type_name is None
    assert param.is_optional is None
    assert param.default is None


# Generated at 2022-06-13 19:31:20.600192
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    new_DocstringMeta = DocstringMeta(["args"], "description")
    assert(new_DocstringMeta.description == "description")
    assert(new_DocstringMeta.args == ["args"])



# Generated at 2022-06-13 19:31:27.196042
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ['deprecated']
    description = 'if something happens'
    version = '1.0'
    deprecation = DocstringDeprecated(args, description, version)
    assert deprecation.type_name == 'deprecated'
    assert deprecation.description == 'if something happens'
    assert deprecation.version ==  '1.0'

test_DocstringDeprecated()

# Generated at 2022-06-13 19:31:29.272958
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(['None', 'exception'], "if something happens")
    return d


# Generated at 2022-06-13 19:31:34.823204
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []



# Generated at 2022-06-13 19:31:46.932871
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "arg", "attribute"]
    description = "some description"
    arg_name = "arg"
    type_name = "str"
    is_optional = True
    default = "foobar"
    docstring = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docstring.args == args, "docstring.args is not the args variable given in constructor"
    assert docstring.description == description, "docstring.description is not the description variable given in constructor"
    assert docstring.arg_name == arg_name, "docstring.arg_name is not the arg_name variable given in constructor"
    assert docstring.type_name == type_name, "docstring.type_name is not the type_name variable given in constructor"

# Generated at 2022-06-13 19:31:54.824211
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Errore di tipo ParseError")
    except ParseError:
        pass


# Generated at 2022-06-13 19:31:56.124919
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta


# Generated at 2022-06-13 19:32:01.913816
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Constructor test
    DocstringMeta(None, None)
    # Type test, coverage test
    assert isinstance(DocstringMeta(None, None), DocstringMeta)
    assert isinstance(DocstringMeta(None, None).args, list)
    assert isinstance(DocstringMeta(None, None).description, str)


# Generated at 2022-06-13 19:32:08.327679
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    name = ['hello']
    description = 'This is deprecated'
    version = '1.1.0'
    doc_object = DocstringDeprecated(name, description, version)
    assert doc_object.args == ['hello']
    assert doc_object.description == description
    assert doc_object.version == version
    assert doc_object != None


# Generated at 2022-06-13 19:32:09.240976
# Unit test for constructor of class ParseError
def test_ParseError():
    pass



# Generated at 2022-06-13 19:32:14.299540
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc = DocstringReturns(["returns"],
                           "test",
                           "test",
                           "test",
                           "test")
    print(doc.args)
    print(doc.description)
    print(doc.type_name)
    print(doc.is_generator)
    print(doc.return_name)

# Generated at 2022-06-13 19:32:21.770047
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    from typing import Optional
    docstring_param = DocstringParam(["arg", "description"], "arg_name", "type", Optional[bool], "default")
    assert docstring_param.args == ["arg", "description"]
    assert docstring_param.description == "arg_name"
    assert docstring_param.arg_name == "type"
    assert docstring_param.type_name == Optional[bool]
    assert docstring_param.is_optional == "default"
    assert docstring_param.default == "default"


# Generated at 2022-06-13 19:32:23.092314
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    x = DocstringRaises([],"","")
    assert x.args == []
    assert x.description == ""
    assert x.type_name == ""


# Generated at 2022-06-13 19:32:27.415741
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Unit test for constructor of class DocstringReturns."""
    # Works fine
    assert DocstringReturns(["return", "returns"], "desc", "int", False) is not None

    # Fail because return/returns not in args
    try:
        DocstringReturns(["return", "return"], "desc", "int", False)
        assert False
    except TypeError:
        assert True

    # Fail because description is None
    try:
        DocstringReturns(["return", "returns"], None, "int", False)
        assert False
    except TypeError:
        assert True

    # Fail because type_name is None
    try:
        DocstringReturns(["return", "returns"], "desc", None, False)
        assert False
    except TypeError:
        assert True

    # Fail because is_generator is None


# Generated at 2022-06-13 19:32:29.565068
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd = DocstringDeprecated('This is a parameter', 'This is a description', 'This is version')
    assert dd.args == ['This is a parameter']
    assert dd.description == 'This is a description'
    assert dd.version == 'This is version'


# Generated at 2022-06-13 19:32:44.507241
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Arrange
    args = ["param","argument"]
    description = "I am a parameter"
    arg_name = "b"
    type_name = "int"
    is_optional = "True"
    default = "0"

    # Act
    t_DocstringParam = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    # Assert
    assert t_DocstringParam.args == args
    assert t_DocstringParam.description == description
    assert t_DocstringParam.arg_name == arg_name
    assert t_DocstringParam.type_name == type_name
    assert t_DocstringParam.is_optional == is_optional
    assert t_DocstringParam.default == default



# Generated at 2022-06-13 19:32:47.422994
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc_string = DocstringDeprecated(["deprecate", "2.2", "my_arg"], None, "2.2")
    assert("2.2" == doc_string.version)



# Generated at 2022-06-13 19:32:52.673590
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(["deprecated"], "Use :class:`NewClass` instead", "3.0").description == "Use :class:`NewClass` instead" and \
    DocstringDeprecated(["deprecated"], "Use :class:`NewClass` instead", "3.0").args == ["deprecated"] and \
    DocstringDeprecated(["deprecated"], "Use :class:`NewClass` instead", "3.0").version == "3.0"


# Generated at 2022-06-13 19:33:04.165162
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    arguments = []
    description = "a description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = True
    default = "default"
    a = DocstringParam(arguments,description,arg_name,type_name,is_optional,default)
    if a.args != arguments:
        print("arguments fail")
    if a.description != description:
        print("description fail")
    if a.arg_name != arg_name:
        print("arg_name fail")
    if a.type_name != type_name:
        print("type_name fail")
    if a.is_optional != is_optional:
        print("is_optional fail")
    if a.default != default:
        print("default fail")


# Generated at 2022-06-13 19:33:09.267415
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []


# Generated at 2022-06-13 19:33:12.136221
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(['hello', 'world'], 'description')
    assert 'description' == d.description
    assert ['hello', 'world'] == d.args


# Generated at 2022-06-13 19:33:13.967021
# Unit test for constructor of class Docstring
def test_Docstring():
    try:
        docstring = Docstring()
        assert (isinstance(docstring, Docstring))
    except TypeError:
        assert False

# Generated at 2022-06-13 19:33:19.771351
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["arg1", "arg2"]
    description = "description"
    type_name = "type1"
    docstring_raises = DocstringRaises(args, description, type_name)
    assert docstring_raises.args[0] == args[0]
    assert docstring_raises.args[1] == args[1]
    assert docstring_raises.description == description
    assert docstring_raises.type_name == type_name


# Generated at 2022-06-13 19:33:21.242720
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError()
    assert(err)



# Generated at 2022-06-13 19:33:31.595037
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(args = [], description=None, type_name=None, is_generator=False, return_name=None)
    # Unit test for constructor of class DocstringMeta
    def test_DocstringMeta():
        DocstringMeta(args = [], description=None)
    # Unit test for constructor of class DocstringParam
    def test_DocstringParam():
        DocstringParam(args = [], description=None, arg_name=None, type_name=None, is_optional=bool(0) , default=None)
    # Unit test for constructor of class DocstringRaises
    def test_DocstringRaises():
        DocstringRaises(args = [], description=None, type_name=None)
    # Unit test for constructor of class DocstringDeprecated
    def test_DocstringDeprecated():
        DocstringDep

# Generated at 2022-06-13 19:33:41.709219
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError('test') is not None


# Generated at 2022-06-13 19:33:50.433033
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    new_docstring_meta1 = DocstringMeta(['param', 'arg'], 'why are you so beautiful?')
    assert new_docstring_meta1.args == ['param', 'arg']
    assert new_docstring_meta1.description == 'why are you so beautiful?'
    new_docstring_meta2 = DocstringMeta(['annotation', 'mark'], 'Keep going')
    assert new_docstring_meta2.args == ['annotation', 'mark']
    assert new_docstring_meta2.description == 'Keep going'



# Generated at 2022-06-13 19:33:58.304191
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = []
    description = "This is a description"
    arg_name = "arg"
    type_name = "type"
    is_optional = True
    default = "default"
    param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert param.args == args
    assert param.description == description
    assert param.arg_name == arg_name
    assert param.type_name == type_name
    assert param.is_optional == is_optional
    assert param.default == default


# Generated at 2022-06-13 19:33:59.957474
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta([], "")
    assert a


# Generated at 2022-06-13 19:34:02.678875
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    doc = DocstringMeta(['a'], 'b')
    assert doc.args == ['a']
    assert doc.description == 'b'


# Generated at 2022-06-13 19:34:11.711180
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    ds = DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    assert ds.args == ['arg'], "args in DocstringParam should be the same"
    assert ds.description == 'description', "description in DocstringParam should be the same"
    assert ds.arg_name == 'arg_name', "arg_name in DocstringParam should be the same"
    assert ds.type_name == 'type_name', "type_name in DocstringParam should be the same"
    assert ds.is_optional == True, "is_optional in DocstringParam should be the same"
    assert ds.default == 'default', "default in DocstringParam should be the same"

# Generated at 2022-06-13 19:34:15.945617
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    x = DocstringDeprecated(args=['deprecated'], description = 'bla', version = '1.0')
    assert x.args == ['deprecated']
    assert x.description == 'bla'
    assert x.version == '1.0'


# Generated at 2022-06-13 19:34:17.143624
# Unit test for constructor of class ParseError
def test_ParseError():
   pe = ParseError()


# Generated at 2022-06-13 19:34:21.296315
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstring = DocstringRaises(['a', 'b'], "c", "d")
    assert docstring.args == ['a', 'b'] and docstring.description == "c" and docstring.type_name == "d"
    

# Generated at 2022-06-13 19:34:23.013407
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = [":param"]
    description = ":param"
    d = DocstringMeta(args, description)
    assert d.args == [":param"]
    assert d.description == ":param"


# Generated at 2022-06-13 19:34:44.252369
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringParams = DocstringParam(
        ['param'], "param description", "paramName", "int", True, "5")

    assert docstringParams.args == ['param']
    assert docstringParams.arg_name == "paramName"
    assert docstringParams.type_name == "int"
    assert docstringParams.is_optional == True
    assert docstringParams.default == '5'
    assert docstringParams.description == "param description"


# Generated at 2022-06-13 19:34:52.541362
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('1st test')
    except ParseError as err:
        assert str(err) == '1st test'
    try:
        raise ParseError('2nd test', 123)
    except ParseError as err:
        assert str(err) == '2nd test'
        assert repr(err) == '2nd test'
    try:
        raise ParseError('3rd test') from err
    except ParseError as err:
        assert str(err) == '3rd test'
        assert repr(err) == 'ParseError(\'3rd test\',)'


# Generated at 2022-06-13 19:34:57.869818
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['2']
    description = 'test'
    type_name = 'int'
    test_DocstringRaises = DocstringRaises(args,description,type_name)
    assert test_DocstringRaises.args == ['2']

# Generated at 2022-06-13 19:35:04.504809
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated", "version: 3.0"]
    description = "do not use"
    version = "3.0"
    a = DocstringDeprecated(args, description, version)
    assert a.args == args
    assert a.description == description
    assert a.version == version
    
    

# Generated at 2022-06-13 19:35:09.448774
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description is False
    assert x.blank_after_long_description is False
    assert x.meta == []


# Generated at 2022-06-13 19:35:12.032163
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['args']
    description = 'description'
    assert DocstringMeta(args, description).args == args
    assert DocstringMeta(args, description).description == description


# Generated at 2022-06-13 19:35:14.751234
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(['args'], 'description', 'arg_name', 'type_name', None, 'default')
    assert isinstance(a, DocstringParam)
    assert a.args == ['args']


# Generated at 2022-06-13 19:35:22.182039
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    """Unit test for constructor of class DocstringParam"""
    meta = DocstringParam(["param"], "description", "arg", "int", True, 0)
    assert meta.args == ["param"], "Should be [param]"
    assert meta.description == "description", "Should be description"
    assert meta.arg_name == "arg", "Should be arg"
    assert meta.type_name == "int", "Should be int"
    assert meta.is_optional == True, "Should be True"
    assert meta.default == 0, "Should be 0"


# Generated at 2022-06-13 19:35:26.507563
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    r = DocstringRaises([], None, None)
    assert r.args == []
    assert r.description == None
    assert r.type_name == None


# Generated at 2022-06-13 19:35:31.112929
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for ParseError constructor."""
    import pytest
    error = ParseError("This is a test")
    assert error.args == ("This is a test",)
    with pytest.raises(TypeError):
        error = ParseError()
    with pytest.raises(TypeError):
        error = ParseError("Message", "Extra arg")


# Generated at 2022-06-13 19:36:06.181156
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(['param'], 'if something happens', '8.5')


# Generated at 2022-06-13 19:36:10.311891
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated"]
    description = "something"
    version = "2"

    new_item = DocstringDeprecated(args, description, version)

    assert new_item.description == description
    assert new_item.version == version


# Generated at 2022-06-13 19:36:16.056904
# Unit test for constructor of class Docstring
def test_Docstring():
    # Initialize self with two instance variables
    test_doc = Docstring()
    test_doc.short_description = "Constructor of Docstring"
    test_doc.long_description = "This is a class Docstring"
    test_doc.blank_after_short_description = False
    test_doc.blank_after_long_description = True
    test_doc.meta = ["something"]
    print(test_doc.short_description)
    print(test_doc.long_description)
    print(test_doc.blank_after_short_description)
    print(test_doc.blank_after_long_description)
    print(test_doc.meta)


# Generated at 2022-06-13 19:36:17.377397
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(args = ['first', 'second'], description = 'metadata')

# Generated at 2022-06-13 19:36:22.620169
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    item_name = "args"
    description = "description"
    type_name = "Optional[str]"
    raises = DocstringRaises(item_name, description, type_name)
    assert raises.args == item_name
    assert raises.description == description
    assert raises.type_name == type_name


# Generated at 2022-06-13 19:36:25.824039
# Unit test for constructor of class ParseError
def test_ParseError():
    pe = ParseError()
    assert isinstance(pe, RuntimeError), "The object is not ParseError class"
    

# Generated at 2022-06-13 19:36:31.254124
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert d.meta == []


# Generated at 2022-06-13 19:36:37.771775
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(
        ["param"],
        "gets the number of the current hour",
        arg_name="hour",
        type_name="int",
        is_optional=False,
        default="None",
    )
    assert param.args == ["param"]
    assert param.description == "gets the number of the current hour"
    assert param.arg_name == "hour"
    assert param.type_name == "int"
    assert param.is_optional == False
    assert param.default == "None"


# Generated at 2022-06-13 19:36:40.478321
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring = DocstringMeta(args = ["a", "b"], description = "description")
    assert docstring.description == "description"
    assert docstring.args == ["a", "b"]


# Generated at 2022-06-13 19:36:46.552373
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    
    args = ['arg']
    description = 'description'
    arg_name = 'argname'
    type_name = 'argtype'
    is_optional = True
    default = 'default value'
    
    
    a=DocstringParam(args,description,arg_name,type_name,is_optional,default)
    
    assert a.args[0] == args[0]
    assert a.description == description
    assert a.arg_name == arg_name
    assert a.type_name == type_name
    assert a.is_optional == is_optional
    assert a.default == default
    
    



# Generated at 2022-06-13 19:37:57.902807
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(["param"], "description", "arg_name", "typename", "optional", "default")
    assert param.args == ["param"]
    assert param.description == "description"
    assert param.arg_name == "arg_name"
    assert param.type_name == "typename"
    assert param.is_optional == "optional"
    assert param.default == "default"


# Generated at 2022-06-13 19:37:59.927392
# Unit test for constructor of class ParseError
def test_ParseError():
    e = ParseError()
    assert e.args == ("",)
    assert e.__class__.__name__ == 'ParseError'
    return e


# Generated at 2022-06-13 19:38:01.677073
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(["args"], "description")



# Generated at 2022-06-13 19:38:05.177111
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['param', 'type_name', 'description']
    description = "This is description"
    type_name = "type_name"
    docstringRaises = DocstringRaises(args, description, type_name)
    assert docstringRaises.args == args
    assert docstringRaises.description == description
    assert docstringRaises.type_name == type_name

# Generated at 2022-06-13 19:38:07.782239
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    d = DocstringReturns(['a', 'b', 'c'], 'Test Description', None, False, 'a')
    assert d.is_generator == False
    assert d.args == ['a', 'b', 'c']
    assert d.description == 'Test Description'


# Generated at 2022-06-13 19:38:15.940105
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["return"]
    description = "The value returned from function"
    return_name = "return_value"
    type_name = "int"
    is_generator = False

    ds = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert ds.args == args
    assert ds.description == description
    assert ds.return_name == return_name
    assert ds.type_name == type_name
    assert ds.is_generator == is_generator

test_DocstringReturns()

# Generated at 2022-06-13 19:38:19.651487
# Unit test for constructor of class Docstring
def test_Docstring():
    """Unit test for constructor of class Docstring"""
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []



# Generated at 2022-06-13 19:38:29.073212
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    p = DocstringParam(
        arg_name="arg_name",
        description="description",
        args=["param"],
        type_name="type_name",
        is_optional=True,
        default="default",
    )
    assert p.args == ["param"]
    assert p.description == "description"
    assert p.arg_name == "arg_name"
    assert p.type_name == "type_name"
    assert p.is_optional
    assert p.default == "default"



# Generated at 2022-06-13 19:38:33.927520
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises(['param', 'arg'], 'description', 'type_name') == DocstringRaises(['param', 'arg'], 'description', 'type_name')

# Generated at 2022-06-13 19:38:39.115351
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.meta == []
    assert ds.params == []
    assert ds.raises == []
    assert ds.deprecation == None
    assert ds.returns == None