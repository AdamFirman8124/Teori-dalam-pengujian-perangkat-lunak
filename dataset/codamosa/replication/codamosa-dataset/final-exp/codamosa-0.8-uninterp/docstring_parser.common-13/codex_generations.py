

# Generated at 2022-06-13 19:30:55.594525
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc = Docstring()
    doc.short_description = "short description"
    doc.long_description = "long description"
    doc.blank_after_short_description = False
    doc.blank_after_long_description = False
    doc.meta.append("arg")
    doc.meta.append("arg2")
    doc.params.append("arg3")
    doc.raises.append("arg4")
    doc.returns = "arg5"
    doc.deprecation = DocstringDeprecated("test_deprecation", "Just a test", "test_version")
    if doc.params != ["arg3"]:
        raise AssertionError
    if doc.raises != ["arg4"]:
        raise AssertionError
    if doc.returns != "arg5":
        raise AssertionError


# Generated at 2022-06-13 19:30:58.991356
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["hello world"]
    description = "bla bla bla"
    docstringMeta = DocstringMeta(args, description)
    assert docstringMeta.args == args
    assert docstringMeta.description == description


# Generated at 2022-06-13 19:31:00.293709
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([], None, None, False)

# Generated at 2022-06-13 19:31:05.197459
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(['args'], 'description', 'arg_name', 'type_name', 'is_optional', 'default')
    assert d.args == ['args'] and d.description == 'description' and d.arg_name == 'arg_name' and d.type_name == 'type_name' and d.is_optional == 'is_optional' and d.default == 'default'


# Generated at 2022-06-13 19:31:06.761238
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError()
    except ParseError:
        pass

if __name__ == '__main__':
    test_ParseError()

# Generated at 2022-06-13 19:31:09.141976
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    ob = DocstringMeta(["param"], "This is Object")
    assert(ob.args == ["param"])
    assert(ob.description == "This is Object")


# Generated at 2022-06-13 19:31:11.886191
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    try:
        my_docstring_return = DocstringReturns([], None, "int", True, "x")
        assert my_docstring_return is not None
    except:
        print("test_DocstringReturns failed")


# Generated at 2022-06-13 19:31:13.230921
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(["arg"], "desc")
    assert a.args == ["arg"]
    assert a.description == "desc"


# Generated at 2022-06-13 19:31:16.653636
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    expected = DocstringDeprecated(
        args=["deprecated"],
        description="This function is deprecated",
        version="0.8",
    )
    assert expected.args == ["deprecated"]

# Generated at 2022-06-13 19:31:18.234454
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta([1,2,3], "This is a test")


# Generated at 2022-06-13 19:31:23.572658
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert type(DocstringMeta) == type


# Generated at 2022-06-13 19:31:26.167009
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta("param", "arg")
    assert a.args == "param"
    assert a.description == "arg"


# Generated at 2022-06-13 19:31:35.891874
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = [':raises', 'ValueError']
    description = 'if something happens'
    type_name = 'ValueError'
    docstringRaises = DocstringRaises(args, description, type_name)
    meta = DocstringRaises(docstringRaises.args, docstringRaises.description, docstringRaises.type_name)
    assert(len(meta.args) == 2)
    assert(meta.args == args)
    assert(meta.description == description)
    assert(meta.type_name == type_name)
    print("test_DocstringRaises pass successfully.")


# Generated at 2022-06-13 19:31:46.960091
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    test_args = ['yields']
    test_description = 'test_description'
    test_type_name = 'test_type_name'
    test_is_generator = True
    test_return_name = 'test_return_name'
    test_returns = DocstringReturns(test_args, test_description, test_type_name, test_is_generator,test_return_name)
    assert test_returns.args == ['yields']
    assert test_returns.description == 'test_description'
    assert test_returns.type_name == 'test_type_name'
    assert test_returns.is_generator == True
    assert test_returns.return_name == 'test_return_name'

# Generated at 2022-06-13 19:31:49.629934
# Unit test for constructor of class ParseError
def test_ParseError():
    pe = ParseError("ValueError")
    # Test whether the constructor worked correctly
    assert pe.args == ("ValueError",)

# Generated at 2022-06-13 19:31:53.327213
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc_meta = DocstringRaises([], '', '')
    assert doc_meta.type_name is '', 'wrong type_name'
    assert doc_meta.description is '', 'wrong description'

# Generated at 2022-06-13 19:32:04.276360
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    """Test DocstringReturns"""
    args = ["arg1", "arg2", "arg3"]
    description = "Description"
    type_name = "Type"
    is_generator = False
    return_name = "Return Name"

    test_return = DocstringReturns(args, description, type_name, is_generator, return_name)

    assert test_return.args == args
    assert test_return.description == description
    assert test_return.type_name == type_name
    assert test_return.is_generator == is_generator
    assert test_return.return_name == return_name

# Generated at 2022-06-13 19:32:06.424793
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError("Error")


# Generated at 2022-06-13 19:32:10.472432
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Test creation of class DocstringMeta
    test = DocstringMeta(args=["param"], description="description")
    assert test.args == ["param"]
    assert test.description == "description"

# DocstringParam testing


# Generated at 2022-06-13 19:32:15.005899
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    type_name = "ValueError"
    description = "bad input"
    assert DocstringRaises(args = "", description = description, type_name = type_name).description == description
    assert DocstringRaises(args = "", description = description, type_name = type_name).type_name == type_name

# Generated at 2022-06-13 19:32:20.783848
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns('args', 'description', 'type_name', is_generator=True, return_name='return_name')


# Generated at 2022-06-13 19:32:23.877086
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Docstring is missing!")
    except ParseError:
        #print("\nParseError Raised.")
        assert True
    except:
        #print("\nOther exception raised.")
        assert False


# Generated at 2022-06-13 19:32:26.499365
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    ds = DocstringMeta(1, 1)
    n = "123" 
    d = "123" 
    t = "123" 
    assert isinstance(ds, DocstringRaises)
    assert ds.args == 1
    assert ds.description == 1
    assert ds.type_name == "123"




# Generated at 2022-06-13 19:32:38.898341
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
	test_args = []
	test_description = "test_description"
	test_type_name = "test_type_name"
	test_is_generator = True
	test_return_name = "test_return_name"
	test = DocstringReturns(test_args, test_description, test_type_name, test_is_generator, test_return_name)
	assert test.args == test_args, "instance variable args does not match"
	assert test.description == test_description, "instance variable description does not match"
	assert test.type_name == test_type_name, "instance variable type_name does not match"
	assert test.is_generator == test_is_generator, "instance variable is_generator does not match"

# Generated at 2022-06-13 19:32:43.074520
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert len(docstring.meta) == 0

# Generated at 2022-06-13 19:32:45.003147
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    par = DocstringMeta([], "")
    assert par.args == []
    assert par.description == ""



# Generated at 2022-06-13 19:32:46.893329
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
  assert DocstringParam(["args"], "description", "arg_name", "type_name", "is_optional", "default")
  

# Generated at 2022-06-13 19:32:55.019331
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc1 = DocstringReturns(args = ['returns'], description = None, type_name = None, is_generator = False, return_name = None)
    doc2 = DocstringReturns(args = ['returns'], description = 'abc', type_name = 'def', is_generator = True, return_name = 'ghi')
    doc3 = DocstringReturns(args = [], description = 'abc', type_name = 'def', is_generator = True, return_name = 'ghi')
    doc4 = DocstringReturns(args = ['returns'], description = None, type_name = 'def', is_generator = False, return_name = 'ghi')

# Generated at 2022-06-13 19:33:05.958716
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert(docstring.short_description == None)
    assert(docstring.long_description == None)
    assert(docstring.blank_after_short_description == False)
    assert(docstring.blank_after_long_description == False)
    assert(len(docstring.meta) == 0)
    assert(docstring.params == [])
    assert(docstring.raises == [])
    assert(docstring.returns == None)
    assert(docstring.deprecation == None)
    docstring.short_description = "short description"
    docstring.long_description = "long description"
    docstring.blank_after_short_description = True
    docstring.blank_after_long_description = True

# Generated at 2022-06-13 19:33:11.181681
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    throws = DocstringRaises(args = ["args"], description = "description", type_name = "string")
    assert(throws.args == ["args"])
    assert(throws.description == "description")
    assert(throws.type_name == "string")

if __name__ == "__main__":
    test_DocstringRaises()

# Generated at 2022-06-13 19:33:15.566763
# Unit test for constructor of class ParseError
def test_ParseError():
    new = ParseError()
    assert new



# Generated at 2022-06-13 19:33:17.458519
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert DocstringParam(["param"], 'parameter description', "arg", "type", True, "default")


# Generated at 2022-06-13 19:33:23.357894
# Unit test for constructor of class Docstring
def test_Docstring():
	"""Unit test for constructor of class Docstring"""
	docstring = Docstring()
	assert docstring.short_description is None
	assert docstring.long_description is None
	assert docstring.blank_after_short_description is False
	assert docstring.blank_after_long_description is False
	assert docstring.meta == []


# Generated at 2022-06-13 19:33:27.932767
# Unit test for constructor of class Docstring
def test_Docstring():
    """Unit test for constructor of class Docstring"""
    test = Docstring()
    assert test.short_description == None
    assert test.long_description == None
    assert test.blank_after_short_description == False
    assert test.blank_after_long_description == False
    assert test.meta == []
    

# Generated at 2022-06-13 19:33:29.772415
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(["a"], "bcd", "e")


# Generated at 2022-06-13 19:33:32.544412
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test = DocstringRaises(["raises"], "description", "type_name")
    assert test.args == ['raises']
    assert test.description == 'description'
    assert test.type_name == 'type_name'



# Generated at 2022-06-13 19:33:37.789940
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['param', 'm:a:m:paramName']
    arg_name = 'paramName'
    description = "description"
    type_name = 'int'
    object = DocstringParam(args, description, arg_name, type_name, False, 55)
    assert object.args == ['param', 'm:a:m:paramName']
    assert object.arg_name == 'paramName'
    assert object.description == "description"
    assert object.type_name == 'int'
    assert object.is_optional == False
    assert object.default == 55


# Generated at 2022-06-13 19:33:45.534728
# Unit test for constructor of class ParseError
def test_ParseError():
    """This is unit test for constructor of class ParseError."""
    # Case 1: instance of ParseError
    try:
        raise ParseError
    except ParseError:
        pass
    # Case 2: instance of subclass of ParseError
    try:
        raise ParseError()
    except ParseError:
        pass
    # Case 2: instance of subclass of ParseError with argument
    try:
        raise ParseError("some string")
    except ParseError:
        pass


# Generated at 2022-06-13 19:33:49.515973
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["arg", "description"]
    description = "testing"
    docstringMeta = DocstringMeta(args, description)
    assert docstringMeta.args == args
    assert docstringMeta.description == description


# Generated at 2022-06-13 19:33:55.063211
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstring_returns = DocstringReturns([], "description", "type_name")
    assert docstring_returns.description == "description"
    assert docstring_returns.type_name == "type_name"
    assert docstring_returns.is_generator == False



# Generated at 2022-06-13 19:34:06.731228
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    A = DocstringRaises(['a', 'b'], 'c', 'd')
    assert A.args == ['a', 'b']
    assert A.description == 'c'
    assert A.type_name == 'd'


# Generated at 2022-06-13 19:34:09.156979
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('my_error')
    except ParseError as e:
        assert 'my_error' in e.args


# Generated at 2022-06-13 19:34:17.550636
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    list_of_args = [":return", ":returns"]
    description = "Example of description"
    type_name = "str"
    is_generator = False
    return_name = None
    return_obj = DocstringReturns(list_of_args, description, type_name, is_generator, return_name)
    assert return_obj.type_name == "str"
    assert return_obj.return_name == None
    assert return_obj.is_generator == False
    assert return_obj.description == "Example of description"
    assert return_obj.args == [":return", ":returns"]


# Generated at 2022-06-13 19:34:19.211670
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(["deprecated"], "description")


# Generated at 2022-06-13 19:34:22.506144
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    test = DocstringMeta(["1", "2", "3"], "hello")
    assert test.args == ["1", "2", "3"]
    assert test.description == "hello"


# Generated at 2022-06-13 19:34:27.196771
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['arg', 'description']
    description = 'None'
    # Constructor DocstringMeta
    docstringMeta = DocstringMeta(args, description)
    assert(docstringMeta.args == ['arg', 'description'])
    assert(docstringMeta.description == 'None')



# Generated at 2022-06-13 19:34:31.697313
# Unit test for constructor of class Docstring
def test_Docstring():
    doc1 = Docstring()
    assert(doc1.short_description == None)
    assert(doc1.long_description == None)
    assert(doc1.blank_after_short_description == False)
    assert(doc1.blank_after_long_description == False)
    assert(doc1.meta == [])


# Generated at 2022-06-13 19:34:39.959630
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["raises"]
    description = "a type error"
    type_name = "TypeError"
    docstringRaises = DocstringRaises(args, description, type_name)
    assert docstringRaises.description == description
    assert docstringRaises.args == args
    assert docstringRaises.type_name == type_name
    assert docstringRaises.description == description



# Generated at 2022-06-13 19:34:45.471141
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    testDocstringDeprecated = DocstringDeprecated(["deprecated", "since", "1.0"], "thing is deprecated", "1.0")
    assert isinstance(testDocstringDeprecated, DocstringDeprecated)


# Generated at 2022-06-13 19:34:52.159491
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc = DocstringParam(['arg'], description='description', arg_name='arg_name', type_name='type_name', is_optional=True, default='default')
    assert doc.args == ['arg']
    assert doc.description == 'description'
    assert doc.arg_name == 'arg_name'
    assert doc.type_name == 'type_name'
    assert doc.default == 'default'
    assert doc.is_optional == True


# Generated at 2022-06-13 19:35:09.447161
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['ret']
    description = 'a return description'
    type_name = 'str'
    is_generator = False
    return_name = 'a_return'
    returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert returns.args == args
    assert returns.description == description
    assert returns.type_name == type_name
    assert returns.is_generator == is_generator
    assert returns.return_name == return_name


# Generated at 2022-06-13 19:35:12.365821
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd = DocstringDeprecated(['param'], 'description', 'version')
    assert dd.args == ['param']
    assert dd.description == 'description'
    assert dd.version == 'version'


# Generated at 2022-06-13 19:35:15.920083
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(["deprecated"], "This function is deprecated", "0.0.1")
    assert isinstance(docstring, DocstringMeta)
    assert docstring.description == "This function is deprecated"
    assert docstring.version == "0.0.1"
    assert docstring.args == "deprecated"


# Generated at 2022-06-13 19:35:19.466047
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['Dog']
    description = 'A big dog'
    ds = DocstringMeta(args, description)
    assert ds.args == ['Dog']
    assert ds.description == 'A big dog'


# Generated at 2022-06-13 19:35:21.945192
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstringRaises = DocstringRaises(
        args=[1],
        description='desc',
        type_name='typename',
        )
    assert docstringRaises.description == 'desc'
    assert docstringRaises.type_name == 'typename'
    assert docstringRaises.args == [1]


# Generated at 2022-06-13 19:35:26.338473
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    Obj = DocstringDeprecated([""], "", "")
    assert Obj.args == []
    assert Obj.description == ""
    assert Obj.version == ""


# Generated at 2022-06-13 19:35:30.917649
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    mystring = DocstringReturns([], None, None, None)
    mystring.type_name = "int"
    mystring.is_generator = False
    mystring.return_name = "name"



# Generated at 2022-06-13 19:35:32.360552
# Unit test for constructor of class ParseError
def test_ParseError():
    parse_error = ParseError()
    assert isinstance(parse_error, RuntimeError)


# Generated at 2022-06-13 19:35:35.610905
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["raises", "something"]
    description = "Something bad happens"
    test = DocstringReturns(args, description, None, False)
    assert test.args == ["raises", "something"]
    assert test.description == description
    assert test.type_name == None
    assert not test.is_generator

# Generated at 2022-06-13 19:35:39.461662
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstring_returns = DocstringReturns(args=["raises"], description="No description", type_name="Exception", is_generator=False, return_name="")
    assert docstring_returns.args == ["raises"]
    assert docstring_returns.description == "No description"
    assert docstring_returns.type_name == "Exception"
    assert docstring_returns.is_generator == False
    assert docstring_returns.return_name == ""


# Generated at 2022-06-13 19:35:58.172882
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(["deprecated"], "description", "0.0.1")
    assert docstring.description == "description"
    assert docstring.args == ["deprecated"]
    assert docstring.version == "0.0.1"



# Generated at 2022-06-13 19:36:00.380013
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc_string = DocstringRaises(["a"], "b", "c")
    assert doc_string.args == ["a"]
    assert doc_string.description == "b"
    assert doc_string.type_name == "c"


# Generated at 2022-06-13 19:36:05.676841
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(["a"], "bb","cc",True)
    b = DocstringReturns(["a"], "bb","cc",False)
    print(a.args)
    print(a.description)
    print(a.type_name)
    print(a.is_generator)
    print(a.return_name)
    print(b.args)
    print(b.description)
    print(b.type_name)
    print(b.is_generator)
    print(b.return_name)

test_DocstringReturns()


# Generated at 2022-06-13 19:36:11.927766
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test the initialization of a Docstring object."""
    d = Docstring()
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert d.meta == []
    assert d.params == []
    assert d.raises == []
    assert d.returns is None
    assert d.deprecation is None

# Generated at 2022-06-13 19:36:12.464800
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    assert True
    return

# Generated at 2022-06-13 19:36:15.615100
# Unit test for constructor of class ParseError
def test_ParseError():
    """Unit test for constructor of class ParseError."""
    pe = ParseError('a')
    assert pe.args == ('a',)



# Generated at 2022-06-13 19:36:17.053233
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam([], None, None, None, None, None)


# Generated at 2022-06-13 19:36:20.540701
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    string = ":param arg: description\n"
    if (string is ":param arg: description"):
        # print("Test for DocstringParam passed")
        return True
    else:
        return False


# Generated at 2022-06-13 19:36:24.014140
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    meta = DocstringDeprecated(["param"], "desc", version="1.0.0")
    assert meta.version == "1.0.0", "param value should be '1.0.0'"
    assert meta.description == "desc", "desc value should be 'desc'"

# Generated at 2022-06-13 19:36:29.916005
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["args"]
    description = None
    arg_name = "arg_name"
    type_name = None
    is_optional = None
    default = None
    docstringParam = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docstringParam
    assert len(docstringParam.args) == 1
    assert docstringParam.args[0] == "args"
    assert docstringParam.description == description
    assert docstringParam.arg_name == arg_name
    assert docstringParam.type_name == type_name
    assert docstringParam.is_optional == is_optional
    assert docstringParam.default == default


# Generated at 2022-06-13 19:36:59.108696
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Test 1
    arguments = []
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = "is_optional"
    default = "default"
    docstringparam = DocstringParam(arguments, description, arg_name, type_name, is_optional, default)
    assert docstringparam.args == arguments
    assert docstringparam.description == description
    assert docstringparam.arg_name == arg_name
    assert docstringparam.type_name == type_name
    assert docstringparam.is_optional == is_optional
    assert docstringparam.default == default
    # Test 2
    arguments = [1, 2]
    description = "description test 2"
    arg_name = "arg_name test 2"
    #type_name

# Generated at 2022-06-13 19:37:01.282135
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description == False
    assert x.blank_after_long_description == False


# Generated at 2022-06-13 19:37:06.030926
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam("args", "description", "arg_name", "type_name", "is_optional", "default")
    assert d.description == "description"
    assert d.arg_name == "arg_name"
    assert d.type_name == "type_name"
    assert d.is_optional == "is_optional"
    assert d.default == "default"


# Generated at 2022-06-13 19:37:10.229539
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    try:
        doc = DocstringParam(['param'], 'this is the description', 'arg', None, None, 'None')
    except:
        raise AssertionError("There is a problem with the constructor of DocstringParam")


# Generated at 2022-06-13 19:37:13.474973
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
	Meta = DocstringDeprecated(':deprecated', 'Use this class', 'v1')
	assert Meta.args == ['deprecated']
	assert Meta.description == 'Use this class'
	assert Meta.version == 'v1'

test_DocstringDeprecated()

# Generated at 2022-06-13 19:37:18.642736
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['arg']
    description = "description"
    arg_name = "arg_name"
    type_name = None
    is_optional = None
    default = None
    assert DocstringParam(args, description, arg_name, type_name, is_optional, default)


# Generated at 2022-06-13 19:37:21.571919
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(1, "Test1", "version")
    assert a.description == "Test1"
    assert a.version == "version"
    assert a.args == 1


# Generated at 2022-06-13 19:37:22.283626
# Unit test for constructor of class Docstring
def test_Docstring():
    pass

# Generated at 2022-06-13 19:37:24.158981
# Unit test for constructor of class ParseError
def test_ParseError():
    test_ParseError = ParseError()


# Generated at 2022-06-13 19:37:29.841898
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    from typing import List
    dp = DocstringParam(None, None, "arg_name", "type_name", True, "False")
    assert dp.arg_name == "arg_name"
    assert dp.type_name == "type_name"

    # assert type(dp.args) == (List[str])
    assert dp.description == None
    assert dp.is_optional == True
    assert dp.default == "False"

# Generated at 2022-06-13 19:38:06.778147
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(ParseError):
        raise ParseError('A ParseError message')


# Generated at 2022-06-13 19:38:15.200268
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # test name
    args = ""
    description = 'description of the function'
    type_name = "str"
    is_generator = False
    return_name = "return_name"
    test = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert test.args == args
    assert test.description == description
    assert test.type_name == type_name
    assert test.is_generator == is_generator
    assert test.return_name == return_name
    print("test_DocstringReturns success!")
    return True


# Generated at 2022-06-13 19:38:16.793694
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    ds = DocstringRaises(['method_argparse'], 'description')
    if ds:
        print("Unit test success")
    else:
        print("Unit test failed")

# Generated at 2022-06-13 19:38:21.114987
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.meta == []


# Generated at 2022-06-13 19:38:30.904428
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args=["arg"]
    description="des"
    arg_name="arg"
    type_name="type"
    is_optional=False
    default="default"
    dp = DocstringParam(args,description,arg_name,type_name,is_optional,default)
    assert  dp.args == args
    assert dp.description == description
    assert dp.arg_name == arg_name
    assert dp.type_name == type_name
    assert dp.is_optional == is_optional
    assert dp.default == default


# Generated at 2022-06-13 19:38:33.048845
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(["sys"], "System", "1.0")

# Generated at 2022-06-13 19:38:36.023342
# Unit test for constructor of class ParseError
def test_ParseError():
    """
    Unit test for constructor of class ParseError
    """
    err=ParseError("test")
    assert str(err) == "test"


# Generated at 2022-06-13 19:38:43.440695
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ["param", "parameter", "arg", "argument"]
    description = "some description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = "is_optional"
    default = "default"

    docstring = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    # Unit test for __init__ of class DocstringParam
    assert docstring.args == args
    assert docstring.description == description
    assert docstring.arg_name == arg_name
    assert docstring.type_name == type_name
    assert docstring.is_optional == is_optional
    assert docstring.default == default


# Generated at 2022-06-13 19:38:44.751307
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    #instantiating DocstringReturns with no arguments
    DocstringReturns(list, str, None, T.Optional[bool])
    print("Testing constructor DocstringReturns")


# Generated at 2022-06-13 19:38:49.286450
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["param", "foo", "int", "--", "bar"]
    description = "foo is a number"
    a = DocstringMeta(args, description)
    assert a.args == args
    assert a.description == description


# Generated at 2022-06-13 19:40:01.749246
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # docstring_meta = DocstringMeta(args, description)
    assert_DocstringMeta = DocstringMeta(['param'], 'description')
    assert assert_DocstringMeta.args == ['param']
    assert assert_DocstringMeta.description == 'description'


# Generated at 2022-06-13 19:40:04.240954
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    first = DocstringDeprecated(["args", "args2"], "desc", "1.0.0.0")
    assert isinstance(first,DocstringDeprecated)
    assert first.args == ["args", "args2"]
    assert first.description == "desc"
    assert first.version == "1.0.0.0"


# Generated at 2022-06-13 19:40:05.117445
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError()
    assert str(err) == "A parse error occured."

# Generated at 2022-06-13 19:40:09.213669
# Unit test for constructor of class Docstring
def test_Docstring():
    my_docstring_object = Docstring()
    assert my_docstring_object.short_description == None
    assert my_docstring_object.long_description == None
    assert my_docstring_object.blank_after_short_description == False
    assert my_docstring_object.blank_after_long_description == False
    assert my_docstring_object.meta == []


# Generated at 2022-06-13 19:40:14.164190
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
  d = DocstringRaises(["raises"], "some description", "some_type_name")
  assert d.description == "some description"
  assert d.args == ['raises']
  assert d.type_name == 'some_type_name'

# Docstring and DocstringMeta are used through out the code, so
# cover loads of code through just testing these two classes

# Generated at 2022-06-13 19:40:20.143840
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ['foo', 'bar']
    description = 'baz'
    version = '1.0.0'
    obj = DocstringDeprecated(args, description, version)
    assert isinstance(obj, DocstringDeprecated)


# Generated at 2022-06-13 19:40:26.006877
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(['raises'], 'I am an exception', 'enumerate')
    assert a.args == ['raises']
    assert a.description == 'I am an exception'
    assert a.type_name == 'enumerate'

    b = DocstringRaises([], "I'm a prameter", None)
    assert b.args == []
    assert b.description == "I'm a prameter"
    assert b.type_name is None


# Generated at 2022-06-13 19:40:27.330378
# Unit test for constructor of class ParseError
def test_ParseError():
    pass


# Generated at 2022-06-13 19:40:32.976801
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    try:
        x = DocstringReturns(["raises"], "ValueError", "ValueError")
        assert True
    except:
        assert False

    try:
        x = DocstringReturns(["raises"], "Returns or yields a value", "ValueError")
        assert True
    except:
        assert False


# Generated at 2022-06-13 19:40:34.857699
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(args="", desc="", version="")
