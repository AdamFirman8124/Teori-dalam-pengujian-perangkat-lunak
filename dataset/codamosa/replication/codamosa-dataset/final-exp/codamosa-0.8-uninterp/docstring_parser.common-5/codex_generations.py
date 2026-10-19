

# Generated at 2022-06-13 19:30:56.052531
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # Set up
    args = ['arg1', 'arg2']
    description = 'some description'
    type_name = 'str'

    # Test
    t1 = DocstringRaises(args, description, type_name)

    # Verify final result
    assert t1.args == ['arg1', 'arg2']
    assert t1.description == 'some description'
    assert t1.type_name == 'str'



# Generated at 2022-06-13 19:30:58.662190
# Unit test for constructor of class ParseError
def test_ParseError():
    """Test constructor of ParseError class."""
    error = ParseError("test")
    assert error.__str__() == "test"

# Unit tests for constructors of class Docstring

# Generated at 2022-06-13 19:31:03.076408
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(
        args=[],
        description="a string of file name",
        arg_name="file_name",
        type_name=None,
        is_optional=False,
        default=None
    )



# Generated at 2022-06-13 19:31:08.851504
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert ds.meta is not None
    assert len(ds.meta) is 0

# Generated at 2022-06-13 19:31:11.755005
# Unit test for constructor of class Docstring
def test_Docstring():
    dict = Docstring()
    dict.short_description = "abc"
    dict.long_description = "abc"
    assert dict.short_description == "abc"
    assert dict.long_description == "abc"


# Generated at 2022-06-13 19:31:14.327671
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    ds = DocstringDeprecated(description=":param a: desc", args="a", version="100.0")
    print(ds.description)
    print(ds.args)
    print(ds.version)



# Generated at 2022-06-13 19:31:16.992486
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
  args = "a"
  description = "a"
  type_name = "a"
  DocstringRaises(args, description, type_name )
  print("test_DocstringRaises: DocstringRaises() instantiated")

# Generated at 2022-06-13 19:31:26.055585
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args=['return', 'type']
    description="the return type of x is int"
    type_name="int"
    is_generator=False
    return_name="x"
    a=DocstringReturns(args,description,type_name,is_generator,return_name)
    assert a.args==['return', 'type']
    assert a.description=="the return type of x is int"
    assert a.type_name=="int"
    assert a.is_generator==False
    assert a.return_name=="x"


# Generated at 2022-06-13 19:31:29.176124
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(
        args=["param"],
        description="description",
        version="1.0.0",
    )
    assert d is not None

# Generated at 2022-06-13 19:31:35.997132
# Unit test for constructor of class Docstring
def test_Docstring():
    obj = Docstring()
    # tests if the docstring has the expected attributes
    obj_attrs = [
        "short_description",
        "long_description",
        "blank_after_short_description",
        "blank_after_long_description",
        "meta",
    ]
    for attr in obj_attrs:
        assert hasattr(obj, attr)



# Generated at 2022-06-13 19:31:43.565096
# Unit test for constructor of class Docstring
def test_Docstring():

    doc_obj = Docstring()



# Generated at 2022-06-13 19:31:47.121876
# Unit test for constructor of class ParseError
def test_ParseError():
    a = None
    try:
        raise ParseError('test')
    except ParseError as e:
        print('exception caught')
        a = e
    assert a.__str__() == 'brief [0]: test'


# Generated at 2022-06-13 19:31:51.153497
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description == None
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []


# Generated at 2022-06-13 19:31:54.887780
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError("this is an error!")
    assert error.args[0] == "this is an error!"


# Generated at 2022-06-13 19:32:00.111414
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    """Test of DocstringMeta."""
    args = ["one", "two", "three"]
    description = "the description"
    docmet = DocstringMeta(args, description)
    assert docmet.args == args
    assert docmet.description == description


# Generated at 2022-06-13 19:32:04.489453
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['raises', 'ValueError']
    description = None
    type_name = 'ValueError'
    raise_Obj = DocstringRaises(args, description, type_name)
    assert raise_Obj.args == ['raises', 'ValueError']

# Generated at 2022-06-13 19:32:09.692265
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['arg1', 'arg2']
    description = 'The description'
    type_name = 'int'
    t = DocstringRaises(args, description, type_name)
    print(t.args, t.description, t.type_name)

if __name__ == "__main__":
    test_DocstringRaises()

# Generated at 2022-06-13 19:32:13.562653
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    print("Testing DocstringParam")
    a = DocstringParam("", "", "", "", "", "")
    print("DocstringParam: " + str(vars(a)))
    print("----------------\n")


# Generated at 2022-06-13 19:32:24.037127
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test the constructor of Docstring."""
    docstring1 = Docstring()
    assert docstring1.short_description is None
    assert docstring1.long_description is None
    assert not docstring1.blank_after_short_description
    assert not docstring1.blank_after_long_description
    assert not docstring1.meta
    assert not docstring1.params
    assert not docstring1.raises
    assert not docstring1.returns
    assert not docstring1.deprecation

# Generated at 2022-06-13 19:32:29.001405
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
  e1 = DocstringParam(['my parameter'], 'is optional', 'my parameter',
                      'str', True, None)

  e2 = DocstringParam(['first', 'second'], 'is optional', 'first',
                      'str', True, None)
  return e1.arg_name == 'my parameter' and e1.type_name == 'str' and \
  e1.is_optional == True and e1.default == None and \
  e2.arg_name == 'first' and e2.type_name == 'str' and \
  e2.description == 'is optional'

# Generated at 2022-06-13 19:32:37.125564
# Unit test for constructor of class ParseError
def test_ParseError():
  p = ParseError("this is an error")
  assert(p.args[0] == "this is an error")

# Generated at 2022-06-13 19:32:38.997446
# Unit test for constructor of class ParseError
def test_ParseError():
    e = ParseError('test')
    assert e.args == ('test',)


# Generated at 2022-06-13 19:32:43.576808
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    d = DocstringRaises(["Raises"], "If no arguments are given", "Exception")
    if (d.args == ["Raises"] and d.description == "If no arguments are given"):
        print("docstring raises unit test pass")
    else:
        print("docstring raises unit test fail")


# Generated at 2022-06-13 19:32:44.200024
# Unit test for constructor of class Docstring
def test_Docstring():
    Docstring()

# Generated at 2022-06-13 19:32:47.944682
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []



# Generated at 2022-06-13 19:32:48.832229
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert 1

# Generated at 2022-06-13 19:32:50.364873
# Unit test for constructor of class ParseError
def test_ParseError():
    p = ParseError("abc")
    assert p.__str__() == "abc"  


# Generated at 2022-06-13 19:32:53.812980
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("boo!")
    except ParseError as e:
        assert e.args == ("boo!",)
        assert str(e) == "boo!"



# Generated at 2022-06-13 19:33:04.795460
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["param", "arg", "argument", "attribute", "key", "keyword"]
    description = "this is a description"
    type_name = "int"
    is_generator = True
    return_name = "returnvalue"
    return_obj = DocstringReturns(args, description, type_name, is_generator, return_name)
    # Test all attributes have the expected value
    assert return_obj.args == ["param", "arg", "argument", "attribute", "key", "keyword"]
    assert return_obj.description == "this is a description"
    assert return_obj.type_name == "int"
    assert return_obj.is_generator == True
    assert return_obj.return_name == "returnvalue"


# Generated at 2022-06-13 19:33:07.861657
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    obj = DocstringDeprecated('s', 's', 's')
    if obj.version != 's':
        raise ValueError('not same')
        

# Generated at 2022-06-13 19:33:19.988467
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    print ("\n--- Unit test for constructor of class DocstringRaises ---")
    
    args = ["raises"]
    description = "something"
    type_name = "TypeError"
    raises = DocstringRaises(args, description, type_name)

    print("args = ", raises.args)
    print("description = ", raises.description)
    print("type_name = ", raises.type_name)
    print("\n")
    

# Generated at 2022-06-13 19:33:22.597402
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("Some message")
    assert isinstance(err, RuntimeError)
    assert str(err) == "Some message"


# Generated at 2022-06-13 19:33:28.324196
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
  #Test that raises works
  test_doc = DocstringRaises(["raises"], "Error", "ValueError")
  assert type(test_doc) == DocstringRaises
  assert test_doc.args == ["raises"], "failed to match list of arguments"
  assert test_doc.description == "Error", "failed to match description"
  assert test_doc.type_name == "ValueError", "failed to match ValueError"
  

# Generated at 2022-06-13 19:33:32.397752
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = ["deprecated", "test"]
    description = "Test description"
    version = "1.0.0"
    test_deprecation = DocstringDeprecated(args, description, version)
    assert test_deprecation.args == args
    assert test_deprecation.description == description
    assert test_deprecation.version == version

# Generated at 2022-06-13 19:33:35.594818
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    meta_deprecated = DocstringDeprecated(['version', 'deprecated'], 'This module is deprecated', '0.0')
    assert meta_deprecated.args == ['version', 'deprecated']
    assert meta_deprecated.description == 'This module is deprecated'
    assert meta_deprecated.version == '0.0'


# Generated at 2022-06-13 19:33:38.299342
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    doc_string = DocstringRaises(["raises"], "bad argument exception", "ValueError")
    expected_string = 'DocstringRaises(args=\'raises\', description = \'bad argument exception\', type_name = \'ValueError\')'
    assert repr(doc_string) == expected_string


# Generated at 2022-06-13 19:33:40.554713
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(["a"], "b", "1.0")
    assert a


# Generated at 2022-06-13 19:33:43.172465
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError('test')
    assert isinstance(err, RuntimeError)
    assert err.args[0] == 'test'

# Generated at 2022-06-13 19:33:48.479228
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    description = "this is a description"
    version = "1.0"
    args = ["deprecated"]
    meta = DocstringDeprecated(args, description, version)
    assert isinstance(meta, DocstringDeprecated)
    assert meta.description == description
    assert meta.version == version
    assert meta.args == args


# Generated at 2022-06-13 19:33:51.668885
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert len(Docstring().meta) == 0
    assert Docstring().short_description is None
    assert Docstring().long_description is None

# Generated at 2022-06-13 19:34:08.475715
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """
    Testing the constructor of class DocstringDeprecated
    """
    args = ['param', 'description']
    version = '0.0.1'
    doc = DocstringDeprecated(args, 'description', version)
    assert doc.args == args
    assert doc.description == 'description'
    assert doc.version == '0.0.1'

# Generated at 2022-06-13 19:34:15.401694
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    parameters = []
    description = "desc"
    str_type = "str"
    is_generator = True
    return_name = "return"
    test_object = DocstringReturns(
        parameters, description, str_type, is_generator, return_name
    )
    assert test_object.args == parameters
    assert test_object.description == description
    assert test_object.type_name == str_type
    assert test_object.is_generator == is_generator
    assert test_object.return_name == return_name



# Generated at 2022-06-13 19:34:18.113539
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["param", "arg"], "This is a test", "arg", None, None, None)
    assert True


# Generated at 2022-06-13 19:34:24.005248
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # Arrange
    doc = DocstringRaises(args = ['raises', 'some_exception'], 
                        description = 'some_description', 
                        type_name = 'some_type')
    # Act
    # Assert
    assert doc.args == ['raises', 'some_exception']
    assert doc.description == 'some_description'
    assert doc.type_name == 'some_type'
    

# Generated at 2022-06-13 19:34:29.882329
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # verify object type
    docstringReturns = DocstringReturns(['', ''], '', '')
    assert type(docstringReturns) == DocstringReturns
    # verify the construction
    assert docstringReturns.args == ['', '']
    assert docstringReturns.description == ''
    assert docstringReturns.type_name == ''
    assert docstringReturns.is_generator == False
    assert docstringReturns.return_name == None


# Generated at 2022-06-13 19:34:38.877494
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Empty docstring
    assert DocstringParam([], 1, 2, 3, 4).description == 1
    # Empty docstring
    assert DocstringParam((), 1, 2, 3, 4).description == 1
    # Empty docstring
    assert DocstringParam([], "", 2, 3, 4).description == ""
    # Empty docstring
    assert DocstringParam((), "", 2, 3, 4).description == ""
    # Empty docstring
    assert DocstringParam([], None, 2, 3, 4).description == None
    # Empty docstring
    assert DocstringParam((), None, 2, 3, 4).description == None
    # Empty docstring
    assert DocstringParam([], "1", 2, 3, 4).description == "1"
    # Empty docstring

# Generated at 2022-06-13 19:34:41.963268
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = "args"
    description = "descriptions"
    type_name = "type_name"
    d = DocstringRaises(args, description, type_name)
    assert d.args == args
    assert d.description == description
    assert d.type_name == type_name



# Generated at 2022-06-13 19:34:46.819704
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstringMeta = DocstringMeta(['a','b'], 'description')
    assert docstringMeta.args == ['a','b']
    assert docstringMeta.description == 'description'


# Generated at 2022-06-13 19:34:51.563424
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc_param=DocstringParam([], "The range in which this function is valid. ")
    assert doc_param.arg_name == arg_name
    assert doc_param.type_name == type_name
    assert doc_param.is_optional == is_optional
    assert doc_param.default == default


# Generated at 2022-06-13 19:34:55.751056
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstringparam = DocstringParam(
        ["param"], "description", "arg", "type", False, None)
    assert docstringparam is not None



# Generated at 2022-06-13 19:35:30.885046
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    doc_ = DocstringReturns(["hello"], "a", "str", True, "return_name")
    assert doc_.description == "a"
    assert doc_.return_name == "return_name"
    assert doc_.args == ["hello"]
    assert doc_.type_name == "str"
    assert doc_.is_generator == True


# Generated at 2022-06-13 19:35:36.794015
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Test DocstringMeta.__init__
    docstringMetaInstance = DocstringMeta(["a","b"],"This is a test.")
    assert docstringMetaInstance.args == ["a","b"]
    assert docstringMetaInstance.description == "This is a test."


# Generated at 2022-06-13 19:35:45.005450
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    # Arrange use given arguments
    args = ["param", "arg"]
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = False
    default = "default"
    # Act create instance for class DocstringParam
    instance = DocstringParam(args, description, arg_name, type_name, is_optional, default)

    # Assert to ensure that instance parameters are equal to given arguments
    assert instance.args == args
    assert instance.description == description
    assert instance.arg_name == arg_name
    assert instance.type_name == type_name
    assert instance.is_optional == is_optional
    assert instance.default == default

# Generated at 2022-06-13 19:35:49.436021
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Test default constructor
    d1 = DocstringMeta([], 'This is a default constructor')

    # Test if the constructor correctly returns an object of type DocstringMeta
    assert isinstance(d1, DocstringMeta) == True

    # Test if the constructor correctly sets the arguments to []
    assert d1.args == []

    # Test if the constructor correctly sets the docstring to "This is a default constructor"
    assert d1.description == 'This is a default constructor'


# Generated at 2022-06-13 19:35:51.498102
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["arg"], None, "arg_name", "type_name", False, "default")


# Generated at 2022-06-13 19:35:54.836253
# Unit test for constructor of class ParseError
def test_ParseError():
    pE = ParseError("Error Generated")
    assert(pE.args == "Error Generated")
    pE.args="Different Error Generated"
    assert(pE.args == "Different Error Generated")


test_ParseError()


# Generated at 2022-06-13 19:35:59.378834
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring=DocstringParam(['attr.x'], 'description', 'arg_name'
                    , 'type_name', 'is_optional','default')
    print(docstring.args)
    print(docstring.description)
    print(docstring.arg_name)
    print(docstring.type_name)
    print(docstring.is_optional)
    print(docstring.default)
test_DocstringParam()



# Generated at 2022-06-13 19:36:00.389464
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test = DocstringRaises(['param','test'],"This is a test", "Test")

# Generated at 2022-06-13 19:36:04.317268
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param = DocstringParam(['param', 'arg1'], 'desc', 'arg1', 'int', True, 10)
    assert param.arg_name == 'arg1', "Name of argument is not as expected"
    assert param.description == 'desc', "Description is not as expected"
    assert param.type_name == 'int', "Type of arg is not as expected"
    assert param.is_optional == True, "is_optional is not as expected"
    assert param.default == '10', "Default value is not as expected"

if __name__ == "__main__":
    test_DocstringParam()

# Generated at 2022-06-13 19:36:11.174178
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test constructor of class DocstringDeprecated."""
    # Arrange
    args = ["deprecated", "deprecation"]
    description = "Deprecation of a function."
    version = "3.3.7"
    docstring = DocstringDeprecated(args, description, version)
    # Act
    # Assert
    assert docstring.args == ["deprecated", "deprecation"]
    assert docstring.description == "Deprecation of a function."
    assert docstring.version == "3.3.7"



# Generated at 2022-06-13 19:37:09.919206
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(args=["version"], description=None, version=None)


# Generated at 2022-06-13 19:37:16.153678
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Test constructor for DocstringDeprecated class."""
    # Empty values for args, description and version
    args = []
    description = None
    version = None
    d = DocstringDeprecated(args, description, version)
    # Make sure constructor does not raise error
    assert d

    # Non-empty values for args, description, and version
    args = ['a1','a2']
    description = 'test description'
    version = 'v1.0'
    d = DocstringDeprecated(args, description, version)
    # Make sure constructor does not raise error
    assert d


# Generated at 2022-06-13 19:37:17.869898
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert DocstringMeta(args=["param"], description="description") != None

# Generated at 2022-06-13 19:37:29.522704
# Unit test for constructor of class ParseError

# Generated at 2022-06-13 19:37:34.259111
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam_instance = DocstringParam([], "", "", None, None, None)
    assert DocstringParam_instance.args == []
    assert DocstringParam_instance.description == ""
    assert DocstringParam_instance.arg_name == ""
    assert DocstringParam_instance.type_name is None
    assert DocstringParam_instance.is_optional is None
    assert DocstringParam_instance.default is None


# Generated at 2022-06-13 19:37:36.294516
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(["a","b"], "good");
    assert d.args[0] == "a"
    assert d.args[1] == "b"
    assert d.description == "good"


# Generated at 2022-06-13 19:37:39.827352
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test_args = ["Test", "test", "v1.2.3"]
    test_description = "Test"
    test_version = "v1.2.3"
    test_docstringdep = DocstringDeprecated(test_args, test_description, test_version)
    assert test_docstringdep.args == ["Test", "test", "v1.2.3"]
    assert test_docstringdep.description == "Test"
    assert test_docstringdep.version == "v1.2.3"

# Generated at 2022-06-13 19:37:45.079234
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstringDeprecated = DocstringDeprecated(["deprecated"], "Description", "0.1")
    assert docstringDeprecated.args == ["deprecated"]
    assert docstringDeprecated.description == "Description"
    return docstringDeprecated


# Generated at 2022-06-13 19:37:46.975897
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError('error')
    except ParseError:
        print('success')


# Generated at 2022-06-13 19:37:47.697801
# Unit test for constructor of class ParseError
def test_ParseError():
	pass


# Generated at 2022-06-13 19:39:52.770598
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(None, None, None, None, None, None)

    assert d.args is None
    assert d.description is None
    assert d.arg_name is None
    assert d.type_name is None
    assert d.is_optional is None
    assert d.default is None


# Generated at 2022-06-13 19:39:54.150648
# Unit test for constructor of class ParseError

# Generated at 2022-06-13 19:39:56.022002
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError()
    except RuntimeError as e:
        assert e


# Generated at 2022-06-13 19:40:06.195841
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    # assert ds.__doc__ == 'Docstring object representation.'
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert ds.meta == []
    assert ds.params == []
    assert ds.raises == []
    assert ds.returns is None
    assert ds.deprecation is None

# Generated at 2022-06-13 19:40:09.063747
# Unit test for constructor of class ParseError
def test_ParseError():
    error=ParseError()
    assert error is not None, "ParseError has a constructor"


# Generated at 2022-06-13 19:40:13.413899
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test_obj = DocstringDeprecated(["deprecated"], "Deprecated description", "0.1")
    assert(test_obj.args[0] == "deprecated")
    assert(test_obj.description == "Deprecated description")
    assert(test_obj.version == "0.1")


# Generated at 2022-06-13 19:40:20.115408
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        a = 1 / 2
    except Exception as e:
        #print(type(e))
        #print(str(e))
        #print(e.args)
        err = ParseError(str(e))
        print(type(err))




# Generated at 2022-06-13 19:40:26.006498
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(['raises'], 'description', 'NameError')
    b = DocstringRaises(['raises', 'k'], 'description', 'NameError')
    assert(a.args[0] == 'raises' and b.args[1] == 'k')
    assert(a.type_name == 'NameError' and b.type_name == 'NameError')
    assert(a.description == 'description' and b.description == 'description')


# Generated at 2022-06-13 19:40:31.221727
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d=DocstringDeprecated(["deprecated"], "deprecated", "1.5.5")
    assert d.args==["deprecated"]
    assert d.description=="deprecated"
    assert d.version=="1.5.5"


# Generated at 2022-06-13 19:40:34.209211
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # Test 1
    DocstringRaises("parameter", "description", "type")
    # Test 2
    DocstringRaises("parameter", None, None)
