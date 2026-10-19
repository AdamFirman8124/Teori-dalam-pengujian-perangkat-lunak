

# Generated at 2022-06-13 19:30:51.587732
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert isinstance(DocstringDeprecated([], '', '1.0.0'), DocstringDeprecated)

# Generated at 2022-06-13 19:30:54.451014
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    ds = DocstringRaises([], "", "")
    assert(ds.args == [], "constructor DocstringRaises failed")
    assert(ds.description == "", "constructor DocstringRaises failed")
    assert(ds.type_name == "", "constructor DocstringRaises failed")


# Generated at 2022-06-13 19:30:59.906407
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    obj = DocstringParam([], "Description", "arg_name", "type_name", True, "default")
    assert obj.args == []
    assert obj.description == "Description"
    assert obj.arg_name == "arg_name"
    assert obj.type_name == "type_name"
    assert obj.is_optional == True
    assert obj.default == "default"


# Generated at 2022-06-13 19:31:04.578219
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(["arg"], None, None, False)
    DocstringReturns(["arg"], None, None, False, return_name="return_name")
    DocstringReturns(["arg"], None, "type_name", False)
    DocstringReturns(["arg"], None, "type_name", False, return_name="return_name")

# Generated at 2022-06-13 19:31:05.963624
# Unit test for constructor of class ParseError
def test_ParseError():
    print("Unit test for constructor of class ParseError")

    err = ParseError()
    assert isinstance(err, RuntimeError)



# Generated at 2022-06-13 19:31:08.684305
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['tests']
    description = "testing"
    docstringMeta = DocstringMeta(args, description)
    assert docstringMeta.args == args
    assert docstringMeta.description == description


# Generated at 2022-06-13 19:31:09.723893
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError("")


# Generated at 2022-06-13 19:31:12.056447
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    ret = DocstringReturns(['ret', 'returns'], '', 'int', False, 'return')
    assert ret == DocstringReturns(['ret', 'returns'], '', 'int', False, 'return')

# Generated at 2022-06-13 19:31:12.956039
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(["1", "2"], None)


# Generated at 2022-06-13 19:31:16.446093
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # test variables
    args = ["arg1", "arg2", "arg3"]
    description = "this is a test"

    # test constructor
    meta = DocstringMeta(args, description)

    # assert that constructor assigns variables correctly
    assert meta.args == args
    assert meta.description == description



# Generated at 2022-06-13 19:31:28.978948
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d1 = DocstringRaises(args=['raises'], description="Some error", type_name='error')
    d2 = DocstringRaises(args=['raises'], description=None, type_name=None)
    assert d1.args == ['raises']
    assert d1.description == 'Some error'
    assert d1.type_name == 'error'
    assert d2.args == ['raises']
    assert d2.description == None
    assert d2.type_name == None


# Generated at 2022-06-13 19:31:31.064880
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns(['return'], 'some value', 'str', True, None)



# Generated at 2022-06-13 19:31:37.142068
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test_object = DocstringRaises(
        args = ['a','b','c'],
        description = 'testing description',
        type_name = 'testing type name'
    )
    assert test_object.args == ['a','b','c']
    assert test_object.description == 'testing description'
    assert test_object.type_name == 'testing type name'


# Generated at 2022-06-13 19:31:40.864699
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["arg"]
    description = "Some description"
    dm = DocstringMeta(args, description)
    assert dm.args == args
    assert dm.description == description

# Generated at 2022-06-13 19:31:47.041327
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    dm = DocstringMeta (args = ['This', 'is', 'just', 'a', 'test'], description = 'This is the description for DocstringMeta')
    assert dm.args == ['This', 'is', 'just', 'a', 'test']
    assert dm.description == 'This is the description for DocstringMeta'

if __name__ == '__main__':
    test_DocstringMeta()

# Generated at 2022-06-13 19:31:50.791103
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
	"""unit test for constructor of DocstringMeta"""
	d = DocstringMeta(['asd'], 'ggg')
	assert d.args == ['asd']
	assert d.description == 'ggg'


# Generated at 2022-06-13 19:31:54.517045
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["param"], "description", "arg_name", "type_name",
                   True, "default")


# Generated at 2022-06-13 19:31:59.051039
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    my_instance = DocstringMeta(["param"], "descr")
    assert isinstance(my_instance, DocstringMeta)
    assert my_instance.args == ["param"]
    assert my_instance.description == "descr"


# Generated at 2022-06-13 19:32:02.271158
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    example_meta = DocstringMeta(['param'], 'description')
    assert example_meta.args == ['param']
    assert example_meta.description == 'description'


# Generated at 2022-06-13 19:32:04.917000
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated([":deprecated", "Test", "1.0"], "Some description", "1.0")



# Generated at 2022-06-13 19:32:19.139792
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
	"""Test for constructor."""
	self = DocstringReturns(['returns'], 'description', 'str', False)
	assert self.args == ['returns']
	assert self.description == 'description'
	assert self.type_name == 'str'
	assert self.is_generator == False


# Generated at 2022-06-13 19:32:20.064938
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises()

# Generated at 2022-06-13 19:32:20.628339
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert False

# Generated at 2022-06-13 19:32:23.432251
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(['param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'], 'description', 'version')
    assert docstring.description == 'description'
    assert docstring.version == 'version'

# Generated at 2022-06-13 19:32:24.977408
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("test")
    except ParseError as error:
        assert error.args == ("test",)


# Generated at 2022-06-13 19:32:33.007878
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    dsr = DocstringReturns(['returns'], 'the return values', 'int', False)
    assert dsr.args == ['returns']
    assert dsr.description == 'the return values'
    assert dsr.type_name == 'int'
    assert dsr.is_generator == False
    assert dsr.return_name == None

if __name__ == "__main__":
    test_DocstringReturns()

# Generated at 2022-06-13 19:32:38.717163
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """For testing constructor of class DocstringReturns"""
    test_args = ["Returns", "return", "yield", "yields"]
    test_description = "description"
    test_type_name = "int"
    test_is_generator = True
    test_return_name = "ret"
    test_docstring_returns_obj = DocstringReturns(test_args, test_description, test_type_name, test_is_generator, test_return_name)


# Generated at 2022-06-13 19:32:41.967573
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc = DocstringRaises(['param', 'description'], 'description', 'description')
    assert doc.description, 'description'


if __name__ == '__main__':
    test_DocstringRaises()

# Generated at 2022-06-13 19:32:45.805697
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
	temp=DocstringDeprecated([":deprecated"], "hello", "1.3")
	assert(temp.args==[":deprecated"])
	assert(temp.description=="hello")
	assert(temp.version=="1.3")

test_DocstringDeprecated()

# Generated at 2022-06-13 19:32:54.123705
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # 1. Test init function to set up the new instance
    docstring_para = DocstringParam(
        args=['arg1', 'arg2'],
        description='docstring description',
        arg_name='first_arg_name',
        type_name='str',
        is_optional=False,
        default=None,
    )

    # 2. Check the value of all attributes
    assert docstring_para.args == ['arg1', 'arg2']
    assert docstring_para.description == 'docstring description'
    assert docstring_para.arg_name == 'first_arg_name'
    assert docstring_para.type_name == 'str'
    assert docstring_para.is_optional == False
    assert docstring_para.default == None

# Generated at 2022-06-13 19:33:05.984747
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Unit test for constructor of class DocstringReturns."""
    docstringReturns = DocstringReturns([], "", "")


# Generated at 2022-06-13 19:33:13.051970
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring = DocstringParam(['args', 'arg'], 'description', 'arg_name', 'type_name', 'is_optional', 'default')

    assert docstring.args == ['args', 'arg']
    assert docstring.description == 'description'
    assert docstring.arg_name == 'arg_name'
    assert docstring.type_name == 'type_name'
    assert docstring.is_optional == 'is_optional'
    assert docstring.default == 'default'

# Generated at 2022-06-13 19:33:18.968853
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    doc.short_description = "Describe the function"
    doc.long_description = "More detailed explaination"
    param1 = DocstringParam(
        args=["param"], description="input arg1", arg_name="arg1",
        type_name=None, is_optional=None, default=None)
    doc.meta = [param1]
    assert doc.params[0].arg_name == "arg1"

# Generated at 2022-06-13 19:33:24.945841
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Constructor Test for DocstringMeta."""
    try:
        DocstringMeta(['1', '2', '3'], 'test')
        print("constructor is ok")
        test_DocstringMeta.passed = 1
    except:
        print("constructor is not ok")
        test_DocstringMeta.passed = 0
test_DocstringMeta.passed = 0


# Generated at 2022-06-13 19:33:29.151995
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    a = DocstringParam(['a','b','c'],None,'arg','TypeName',True,'1')
    assert a.arg_name == 'arg'
    assert a.type_name == 'TypeName'
    assert a.is_optional == True
    assert a.default == '1'


# Generated at 2022-06-13 19:33:30.510297
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError()
    assert type(error) == ParseError

# Generated at 2022-06-13 19:33:36.808818
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()

    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []

# Generated at 2022-06-13 19:33:48.738874
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # constructor(args, description, type_name, is_generator, return_name)
    # test 1: arg is list
    # test 2: description is string
    # test 3: type_name is string
    # test 4: is_generator is True (is_generator = True)
    # test 5: return_name is None
    docstring_return = DocstringReturns(
        ['param', 'parameter', 'arg', 'argument', 'attribute',
         'key', 'keyword'], 'this is a test', 'type name', True, None)
    assert type(docstring_return) == DocstringReturns
    assert type(docstring_return.args) == list
    assert type(docstring_return.description) == str
    assert type(docstring_return.type_name) == str

# Generated at 2022-06-13 19:33:51.976028
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for constructor of class ParseError"""
    e = ParseError("An error occured")
    assert str(e) == "An error occured"


# Generated at 2022-06-13 19:34:00.718997
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam([], "desc", "x", "int", True, "1").arg_name == "x"
    assert DocstringParam([], "desc", "x", "int", True, "1").type_name == "int"
    assert DocstringParam([], "desc", "x", "int", True, "1").is_optional == True
    assert DocstringParam([], "desc", "x", "int", True, "1").default == "1"
    assert DocstringParam([], "desc", "x", "int", True, "1").args == []
    assert DocstringParam([], "desc", "x", "int", True, "1").description == "desc"
    assert DocstringParam([], "desc", "x", None, None, None).arg_name == "x"

# Generated at 2022-06-13 19:34:18.872253
# Unit test for constructor of class ParseError
def test_ParseError():
    my_error = ParseError("Fatal error")
    assert isinstance(my_error,RuntimeError)


# Generated at 2022-06-13 19:34:25.975328
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['args','args']
    arg_name = 'arg_name'
    type_name = 'type_name'
    is_optional = False
    default = 'default'
    dp = DocstringParam(args,None,arg_name,type_name,is_optional,default)
    assert dp.args == args
    assert dp.arg_name == arg_name
    assert dp.type_name == type_name
    assert dp.is_optional == is_optional
    assert dp.default == default
    print("DocstringParam Constructor is working as expected")


# Generated at 2022-06-13 19:34:27.228008
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    pass


# Generated at 2022-06-13 19:34:32.389842
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args=['deprecated']
    description='this module is deprecated'
    version='1.2.3'
    a = DocstringDeprecated(args, description, version)
    assert isinstance(a, DocstringDeprecated)
    assert a.args == ['deprecated']
    assert a.description == 'this module is deprecated'
    assert a.version == '1.2.3'


# Generated at 2022-06-13 19:34:37.553683
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    import doctrans.parsers.napoleon as np
    test = np.DocstringReturns(['param'], 'this is the test', 'int', 'False')
    if test.args != ['param']:
        raise Exception
    if test.type_name != 'int':
        raise Exception
    if test.is_generator != 'False':
        raise Exception
    if test.return_name != None:
        raise Exception


# Generated at 2022-06-13 19:34:40.455183
# Unit test for constructor of class ParseError
def test_ParseError():
    from pytest import raises
    with raises(ParseError):
        raise ParseError("message")


# Generated at 2022-06-13 19:34:41.979715
# Unit test for constructor of class Docstring
def test_Docstring():
    test = Docstring()


# Generated at 2022-06-13 19:34:42.744892
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError("Error")


# Generated at 2022-06-13 19:34:45.344360
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam([], 'description', 'arg_name', 'type_name', 'is_optional', 'default')
    print(param.description)
test_DocstringParam()


# Generated at 2022-06-13 19:34:51.398393
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    x = DocstringReturns(args=['a'], description='description', type_name='x', is_generator='False', return_name='a')
    assert x.args == ['a']
    assert x.description == 'description'
    assert x.type_name == 'x'
    assert x.is_generator == False
    assert x.return_name == 'a'

test_DocstringReturns()

# Generated at 2022-06-13 19:35:29.769168
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc_string = DocstringDeprecated(["deprecated"], "This method is now deprecated", "1.0.0")
    assert doc_string.args == ["deprecated"]
    assert doc_string.description == "This method is now deprecated"
    assert doc_string.version == "1.0.0"


# Generated at 2022-06-13 19:35:32.878637
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ':param X: This is the description of X'
    description = 'This is the description of X'
    type_name = float
    is_generator = True
    return_name = 'Y'
    assert DocstringReturns(args, description, type_name, is_generator, return_name)

# Generated at 2022-06-13 19:35:34.321121
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstring_meta = DocstringMeta(["param"], "")
    return docstring_meta


# Generated at 2022-06-13 19:35:37.287845
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test constructor of class DocstringDeprecated."""
    d=DocstringDeprecated(["hello","world"], "this is deprecated", "0.1")
    assert d.args == ["hello","world"]
    assert d.description == "this is deprecated"
    assert d.version == "0.1"

# Generated at 2022-06-13 19:35:38.759724
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstring = DocstringReturns(None,None,None,None)


# Generated at 2022-06-13 19:35:43.159045
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    doc = Docstring()
    assert doc.params == []
    assert doc.raises == []
    assert doc.returns == None
    assert doc.deprecation == None
    doc.short_description = None
    assert doc.short_description == None
    doc.long_description = None
    assert doc.long_description == None


# Generated at 2022-06-13 19:35:46.438581
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args=["param"]
    description="description"
    type_name=None
    instance = DocstringRaises(args, description, type_name)
    expected = DocstringRaises(args, description, type_name)
    assert isinstance(instance, DocstringRaises)


# Generated at 2022-06-13 19:35:48.190058
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('Test')
        assert False
    except ParseError:
        pass
    except:
        assert False

# Generated at 2022-06-13 19:35:50.541949
# Unit test for constructor of class ParseError
def test_ParseError():
    """
    Testing constructor of class ParseError
    """
    try:
        raise ParseError('test message')
    except ParseError as e:
        assert e.args[0] == 'test message'
    else:
        assert False, 'test failed'



# Generated at 2022-06-13 19:35:55.310999
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstringRaisesTest = DocstringRaises('docstringRaisesTest', 'docstringRaisesTest', 'docstringRaisesTest')
    assert docstringRaisesTest.args == 'docstringRaisesTest'
    assert docstringRaisesTest.description == 'docstringRaisesTest'
    assert docstringRaisesTest.type_name == 'docstringRaisesTest'


# Generated at 2022-06-13 19:37:03.536326
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(["a"], "b")

    assert d.args == ["a"]
    assert d.description == "b"

# Generated at 2022-06-13 19:37:08.420621
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.meta == []

# Generated at 2022-06-13 19:37:09.949052
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(['deprecated'], None, '3.3')
    assert not docstring.description


# Generated at 2022-06-13 19:37:11.741216
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    try:
        # Initiate the DocstringReturns class
        DocstringReturns([], "", "", "")
    except:
        assert(False)
    else:
        assert(True)

# Generated at 2022-06-13 19:37:18.257992
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated(): 
    dep_str = ":deprecation note: version"
    output = DocstringDeprecated(list(map(str, dep_str.split(':'))), "description", "version")
    assert output.description == 'description'
    assert output.version == 'version'
    assert output.args == ['', 'deprecation note', '', '', '', '', 'version']


# Generated at 2022-06-13 19:37:24.584138
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Unit test for constructor of class DocstringMeta."""
    assert DocstringMeta([':arg arg: arg description'], 'arg description').args == [':arg arg: arg description']
    assert DocstringMeta([':arg arg: arg description'], 'arg description').description == 'arg description'


# Generated at 2022-06-13 19:37:27.437746
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises(T.List[str],T.Optional[str],T.Optional[str]) != None

# Generated at 2022-06-13 19:37:32.104933
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = [] # type: T.List[str]
    description = "" # type: T.Optional[str]
    arg_name = "" # type: str
    type_name = "" # type: T.Optional[str]
    is_optional = False  # type: T.Optional[bool]
    default = "" # type: T.Optional[str]
    param = DocstringParam(args, description, arg_name, type_name, is_optional, default) # type: DocstringParam
    assert param.args == []


# Generated at 2022-06-13 19:37:35.962571
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    item = DocstringMeta(['Arg1'], 'Hi')
    assert item.args == ['Arg1']
    assert item.description == 'Hi'


# Generated at 2022-06-13 19:37:41.801550
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(args=['version'], description=None, version="1.0.0")
    assert a.__dict__ == {
        'args': ['version'],
        'description': None,
        'version': '1.0.0'
    }

# Generated at 2022-06-13 19:40:04.757504
# Unit test for constructor of class Docstring
def test_Docstring():
    print("")
    print("test Docstring")
    docstring = Docstring()
    print("docstring")
    print(docstring)
    print("docstring.params")
    print(docstring.params)
    print("docstring.raises")
    print(docstring.raises)
    print("docstring.returns")
    print(docstring.returns)
    print("docstring.deprecation")
    print(docstring.deprecation)


# Generated at 2022-06-13 19:40:09.213407
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test_arg1 = ['arg1']
    test_description = 'description'
    test_type_name = 'type_name'
    test_instance = DocstringRaises(test_arg1, test_description, test_type_name)
    assert test_instance.args == test_arg1
    assert test_instance.description == test_description
    assert test_instance.type_name == test_type_name


# Generated at 2022-06-13 19:40:12.600332
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(['arg'], 'hello', 'world')
    assert a.args == ['arg']
    assert a.description == 'hello'
    assert a.type_name == 'world'


# Generated at 2022-06-13 19:40:15.422154
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated("args", "description", "version")



# Generated at 2022-06-13 19:40:19.400574
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    D = DocstringMeta(["param"], "description")
    assert D.args == ["param"]
    assert D.description == "description"


# Generated at 2022-06-13 19:40:25.046196
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test_args = ["arg"]
    test_description = "description"
    test_type_name = "type"
    test_value = DocstringRaises(test_args, test_description, test_type_name)
    assert test_value.args == test_args
    assert test_value.description == test_description
    assert test_value.type_name == test_type_name
    assert test_value.args == test_args

# Generated at 2022-06-13 19:40:27.813772
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    x = DocstringMeta(['a', 'b'], 'c')
    assert x.args == ['a', 'b']
    assert x.description == 'c'


# Generated at 2022-06-13 19:40:32.355517
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():

    test_raises = DocstringReturns([], "", "", True)
    test_raises.type_name == None
    test_raises.is_generator == None
    test_raises.return_name == None


# Generated at 2022-06-13 19:40:38.550987
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # create a instance from class DocstringParam
    DocstringParam_test = DocstringParam(['a'], 'b', 'c', 'd', 'e', 'f')
    # create a instance from class DocstringParam
    DocstringParam_test2 = DocstringParam(['a'], 'b', 'c', 'd', 'e', 'f')
    if (DocstringParam_test != DocstringParam_test2):
        print("not equal")
    if (DocstringParam_test == DocstringParam_test2):
        print("equal")


# Generated at 2022-06-13 19:40:43.950233
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Test case 1
    args = ["deprecated"]
    description = "This method has been deprecated in release 1.1"
    version = "1.1"

    docstring_deprecated = DocstringDeprecated(args, description, version)

    assert docstring_deprecated.args == args
    assert docstring_deprecated.description == description
    assert docstring_deprecated.version == version
