

# Generated at 2022-06-13 19:30:50.648123
# Unit test for constructor of class ParseError
def test_ParseError():
    x = ParseError("foo")
    assert(x.args == ("foo",))


# Generated at 2022-06-13 19:30:57.918629
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    d = DocstringParam(["param"], "parameter description", "arg_name", "int", True, "3")
    assert(d.args == ["param"])
    assert(d.description == "parameter description")
    assert(d.arg_name == "arg_name")
    assert(d.type_name == "int")
    assert(d.is_optional == True)
    assert(d.default == "3")
    return

'''
print("Testing class constructor DocstringParam!")
test_DocstringParam()
'''


# Generated at 2022-06-13 19:31:05.891100
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ["returns", "Résumé"]
    type_name = "str"
    is_generator = False
    return_name = None
    description = "A summary of the subject."
    return_item=DocstringReturns(args,description,type_name,is_generator,return_name)
    assert return_item.args == ["returns", "Résumé"] and return_item.type_name == "str" and return_item.is_generator == False and return_item.return_name == None and return_item.description == "A summary of the subject."

print('Testing DocstringReturns:')
test_DocstringReturns()



# Generated at 2022-06-13 19:31:11.816079
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert(doc.short_description is None)
    assert(doc.long_description is None)
    assert(not doc.blank_after_short_description)
    assert(not doc.blank_after_long_description)
    assert(doc.meta == [])
    assert(doc.params == [])
    assert(doc.raises == [])
    assert(doc.returns is None)
    assert(doc.deprecation is None)


# Generated at 2022-06-13 19:31:14.779806
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(["a", "b"], "c", "d", "e")
    assert a.description == "c"
    assert a.return_name == "e"
    assert a.type_name == "d"


# Generated at 2022-06-13 19:31:16.170628
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(['a'], 'b')
    assert a.args == ['a']
    assert a.description == 'b'


# Generated at 2022-06-13 19:31:26.573217
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['param', 'arg', 'argument', 'argument', 'argument']
    description = "returns the square of a given integer"
    type_name = None
    is_generator = False
    return_name = "square"
    # Test the __init__ method
    test = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert test.args == ['param', 'arg', 'argument', 'argument', 'argument']
    assert test.description == "returns the square of a given integer"
    assert test.type_name == None
    assert test.is_generator == False
    assert test.return_name == "square"

# Generated at 2022-06-13 19:31:28.880763
# Unit test for constructor of class ParseError
def test_ParseError():
    pe = ParseError()
    assert isinstance(pe, ParseError)


# Generated at 2022-06-13 19:31:34.429565
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.meta == []


# Generated at 2022-06-13 19:31:40.465185
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["arg", "arg1"]
    description = "description string"
    type_name = typename
    d1 = DocstringRaises(args, description, type_name)
    assert d1.args == ["arg", "arg1"]
    assert d1.description == "description string"
    assert d1.type_name == "typename"


# Generated at 2022-06-13 19:31:45.856170
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam([":param arg1: description"], "description", "arg1", "arg1", "true", "None")

# Generated at 2022-06-13 19:31:50.594706
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc_string = DocstringDeprecated(['param', 'name'], "desc", 'version')
    assert isinstance (doc_string, DocstringDeprecated)
    assert doc_string.args == ['param', 'name']
    assert doc_string.description == "desc"
    assert doc_string.version == 'version'

# Generated at 2022-06-13 19:31:58.691923
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    # test the input of this class is initialized to None
    assert doc is not None
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert doc.meta == []


# Generated at 2022-06-13 19:32:01.188147
# Unit test for constructor of class Docstring
def test_Docstring():
    """Test constructor of class Docstring."""
    ds = Docstring()
    assert ds


# Generated at 2022-06-13 19:32:06.489742
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(["deprecated"], "This is deprecated", "1.2.3")
    assert d.args == ["deprecated"]
    assert d.description == "This is deprecated"
    assert d.version == "1.2.3"

# Generated at 2022-06-13 19:32:09.457668
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    ok = DocstringDeprecated(['deprecated'], 'description', '3.4')
    assert ok.args[0] == 'deprecated'
    assert ok.description == 'description'
    assert ok.version == '3.4'


# Generated at 2022-06-13 19:32:14.135786
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["args"]
    description = "some description"
    # test initialization
    ds = DocstringMeta(args, description)
    # test that all attributes were assigned correctly
    assert isinstance(ds, DocstringMeta)
    assert ds.args == args
    assert ds.description == description



# Generated at 2022-06-13 19:32:23.257164
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():

    # The description of the deprecation is not added
    args = ["param", "argument", "attribute", "key", "keyword"]
    description = "this is the reason"
    version = "3.0"
    docstring_deprecated = DocstringDeprecated(args, description, version)
    assert docstring_deprecated.version == version
    assert docstring_deprecated.description == None


# Unit tests for class DocstringMeta

# Generated at 2022-06-13 19:32:26.081753
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("parse error")
    except ParseError as err:
        if str(err) != "parse error":
            print(str(err))
            print("Failed to create ParseError.")
        else:
            print("Created ParseError.")


# Generated at 2022-06-13 19:32:30.638314
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["args", "args2"]
    description = "description"
    myMeta = DocstringMeta(args, description)
    assert myMeta.args == args
    assert myMeta.description == description


# Generated at 2022-06-13 19:32:38.460333
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated([1,2], "hello", "world")
    assert a.args == [1,2]
    assert a.description == "hello"
    assert a.version == "world"


# Generated at 2022-06-13 19:32:48.140246
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
	DocstringParam(args, description, arg_name, type_name, is_optional, default)
	# no exceptions are raised

	DocstringParam(2, 3, 4, 5, 6, 7)
	# TypeError is raised

	DocstringParam("a", "b", "c", "d", "e", "f")
	# TypeError is raised

	DocstringParam(["a", "b", "c"], "d", "e", "f", "g", "h")
	# TypeError is raised

	DocstringParam(["a", "b", "c"], "d", "e", "f", True, "h")
	# no exceptions are raised

	DocstringParam(["a", "b", "c"], "d", "e", None, False, "h")
	# no exceptions are raised


# Generated at 2022-06-13 19:32:52.028585
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    a = DocstringReturns(['a'], 'desc', 'integer', True, 'a')
    assert a.args == ['a']
    assert a.description == 'desc'
    assert a.type_name == 'integer'
    assert a.is_generator == True
    assert a.return_name == 'a'


# Generated at 2022-06-13 19:32:54.193937
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    args = []
    description = ""
    version = "12.3"
    DocstringDeprecated(args, description, version)


# Generated at 2022-06-13 19:32:58.997914
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    
    args = ["arg1", "arg2", "arg3"]
    description = "test"
    myObj = DocstringMeta(args, description)

    assert len(myObj.args) == len(args)
    assert myObj.description == description


# Generated at 2022-06-13 19:33:02.131430
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    assert doc.short_description == None and doc.long_description == None and doc.blank_after_short_description == False and doc.blank_after_long_description == False and doc.meta == []



# Generated at 2022-06-13 19:33:07.745199
# Unit test for constructor of class Docstring
def test_Docstring():
    obj = Docstring()
    assert obj.short_description == None
    assert obj.long_description == None
    assert obj.blank_after_short_description == False
    assert obj.blank_after_long_description == False
    assert obj.meta == []


# Generated at 2022-06-13 19:33:11.984553
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(['a', 'b'], 'test')
    assert(a.args == ['a', 'b'])
    assert(a.description == 'test')



# Generated at 2022-06-13 19:33:15.896240
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(args = ['param', 'str', 'name'], description = 'description')
    assert d.args == ['param', 'str', 'name']
    assert d.description == 'description'


# Generated at 2022-06-13 19:33:20.605177
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    item = DocstringParam(
        ["parameter"], "description", "arg_name", "type_name", True, "default")
    assert item.args == ["parameter"]
    assert item.description == "description"
    assert item.arg_name == "arg_name"
    assert item.type_name == "type_name"
    assert item.is_optional == True
    assert item.default == "default"


# Generated at 2022-06-13 19:33:29.566231
# Unit test for constructor of class Docstring
def test_Docstring():
    assert Docstring()




# Generated at 2022-06-13 19:33:32.696137
# Unit test for constructor of class Docstring
def test_Docstring():
    x = Docstring()
    assert x.short_description == None
    assert x.long_description == None
    assert x.blank_after_short_description == False
    assert x.blank_after_long_description == False
    assert x.meta == []


# Generated at 2022-06-13 19:33:34.277877
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(['deprecated'], 'description', '1.0') is not None

# Unit tests for constructor of class DocstringRaises

# Generated at 2022-06-13 19:33:38.566943
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    doc = DocstringDeprecated(args = ["param"], description = "abc", version = "1.0")
    assert doc.description == "abc"
    assert doc.version == "1.0"


# Generated at 2022-06-13 19:33:45.365953
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """
    Test if DocstringDeprecated is initialized properly by constructor.
    """
    docstring_deprecated = DocstringDeprecated(['deprecated'], "bla bla", "1.2.3")
    assert docstring_deprecated.args == ['deprecated']
    assert docstring_deprecated.description == "bla bla"
    assert docstring_deprecated.version == "1.2.3"


# Generated at 2022-06-13 19:33:51.020559
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    obj = DocstringDeprecated(args=['test'], description='test', version='test')
    print(obj.args)
    print(obj.description)
    print(obj.version)
    print(obj.meta)

# Main function
if __name__ == '__main__':
	test_DocstringDeprecated()

# Generated at 2022-06-13 19:33:52.192583
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert(DocstringRaises.__init__)

# Generated at 2022-06-13 19:33:56.662597
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    temp_list=["test1","test2"]
    temp_ds = DocstringMeta(temp_list, "this is a test")
    assert (temp_ds.args == temp_list)
    assert (temp_ds.description == "this is a test")


# Generated at 2022-06-13 19:34:00.972858
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    item = DocstringDeprecated(["param"], "description", "ver")
    assert item is not None
    assert item.args == ["param"]
    assert item.description == "description"
    assert item.version == "ver"



# Generated at 2022-06-13 19:34:02.782520
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(["raises", "ValueError"], "if something happens", "1.9")


# Generated at 2022-06-13 19:34:13.920260
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    param = DocstringMeta([], None)
    assert param.args == []
    assert param.description is None


# Generated at 2022-06-13 19:34:22.417988
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test_name = "test_name"
    test_description = "test description"
    test_type = "test type"
    test_default = "test_default"
    test_param = DocstringParam(["parameter"], test_description, test_name, test_type, True, test_default)
    assert test_param.args == ["parameter"]
    assert test_param.description == test_description
    assert test_param.arg_name == test_name
    assert test_param.type_name == test_type
    assert test_param.is_optional == True
    assert test_param.default == test_default

# Generated at 2022-06-13 19:34:28.934181
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # DEFINE STRUCTURE OF test_DocstringRaises
    docstring_raises = DocstringRaises(["raises"], "if something happens", "ValueError")
    # DEFINE UNIT TESTS
    assert docstring_raises.args == ["raises"]
    assert docstring_raises.description == "if something happens"
    assert docstring_raises.type_name == "ValueError"
    print("\nDocstringRaises constructed with no errors")


# Generated at 2022-06-13 19:34:30.192178
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises("E1","E2","E3")

# Generated at 2022-06-13 19:34:34.992220
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    item = DocstringReturns(args=["return", "returns"], description=None, type_name=None, is_generator=False, return_name=None)
    # no return name
    assert item.return_name == None


# Generated at 2022-06-13 19:34:39.717957
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns(args=['returns'], description='returns a string', type_name= 'str', is_generator=False, return_name = 'hi') != None 


# Generated at 2022-06-13 19:34:40.655613
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated("args","description","version") != None

# Generated at 2022-06-13 19:34:45.552848
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Unit test for constructor of class DocstringDeprecated
    a=DocstringDeprecated(["var1", "var2"], "description", "version")
    assert type(a) == DocstringDeprecated

# Generated at 2022-06-13 19:34:48.216641
# Unit test for constructor of class ParseError
def test_ParseError():
    er = ParseError("test")
    assert str(er) == "test"


# Generated at 2022-06-13 19:34:53.294368
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    """Unit test for constructor of class DocstringDeprecated."""
    doc_string_deprecation = DocstringDeprecated(["deprecated"], "Deprecated Test Function", "3.0")
    assert doc_string_deprecation.args == ["deprecated"]
    assert doc_string_deprecation.description == "Deprecated Test Function"
    assert doc_string_deprecation.version == "3.0"



# Generated at 2022-06-13 19:35:12.491536
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    DocstringRaises(
        args = ['a', 'b', 'c'],
        description = 'testing',
        type_name = 'test_type_name'
    )



# Generated at 2022-06-13 19:35:16.589803
# Unit test for constructor of class Docstring
def test_Docstring():
    a = Docstring()
    assert a.short_description == None
    assert a.long_description == None
    assert a.blank_after_short_description == False
    assert a.blank_after_long_description == False
    assert a.meta == []
    assert a.params == []
    assert a.raises == []
    assert a.returns == None
    assert a.deprecation == None

# Generated at 2022-06-13 19:35:21.164389
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    # Private method to test constructor of DocstringDeprecated class
    def __test_DocstringDeprecated():
        # Testing constructor of class DocstringDeprecated
        test_meta = DocstringDeprecated([], None, "")
        test_meta.__init__(["test_arg"], "test_description", "test_version")

    __test_DocstringDeprecated()

# Generated at 2022-06-13 19:35:24.481919
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError("Test")
    except ParseError as e:
        assert str(e) == "Test"

if __name__ == "__main__":
    test_ParseError()

# Generated at 2022-06-13 19:35:26.378933
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    assert(DocstringMeta(['param', 'arg'], 'description') is not None)
 

# Generated at 2022-06-13 19:35:31.445232
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert docstring.meta == []


# Generated at 2022-06-13 19:35:42.087681
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ['arg1','arg2','arg3']
    description = 'This is a description'
    type_name = 'type_name'
    value = 5
    docstring_raises = DocstringRaises(
        args = args,
        description = description,
        type_name = type_name,
    )
    assert docstring_raises.args == args
    assert docstring_raises.description == description
    assert docstring_raises.type_name == type_name


# Generated at 2022-06-13 19:35:46.970621
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args=["args", "argssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "argssssssssssssssssssssssssssssssssssssssssssssssssss"]
    description="description"
    doc=DocstringMeta(args,description)
    assert doc.args==args
    assert doc.description==description

# Generated at 2022-06-13 19:35:50.200879
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = DocstringDeprecated(['deprecated'], "This method is deprecated", "v1.0")
    assert d.args == ['deprecated']
    assert d.description == "This method is deprecated"
    assert d.version == "v1.0"
    assert isinstance(d, DocstringDeprecated)
    assert isinstance(d, DocstringMeta)


# Generated at 2022-06-13 19:35:54.353459
# Unit test for constructor of class Docstring
def test_Docstring():
    d1 = Docstring()
    assert d1.short_description is None
    assert d1.long_description is None
    assert d1.blank_after_short_description is False
    assert d1.blank_after_long_description is False
    assert len(d1.meta) == 0


# Generated at 2022-06-13 19:36:31.939386
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    c = DocstringDeprecated(['param', 'a'], "Some text", "1.2")
    assert c.args == ['param', 'a']
    assert c.description == "Some text"
    assert c.version == "1.2"

# Generated at 2022-06-13 19:36:37.992126
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    param  = DocstringParam(
                            args=[':param'],
                            description='description',
                            arg_name='arg_name',
                            type_name='type_name',
                            is_optional=True,
                            default = 'default'
                            )

    assert param.description == "description"
    assert param.arg_name == "arg_name"
    assert param.type_name == "type_name"
    assert param.is_optional == True
    assert param.default == "default"


# Generated at 2022-06-13 19:36:38.675954
# Unit test for constructor of class Docstring
def test_Docstring():
    pass



# Generated at 2022-06-13 19:36:41.924387
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring = DocstringDeprecated(["deprecated", "since", "1.0.0"], "", "1.0.0")
    assert docstring.description == ""
    assert docstring.args == ["deprecated", "since", "1.0.0"]

# Generated at 2022-06-13 19:36:44.327625
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    descr = DocstringDeprecated(["deprecated"], None, None)
    assert descr.args == ["deprecated"]
    assert descr.description == None
    assert descr.version == None
    return

# Generated at 2022-06-13 19:36:55.481362
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = []
    description = "Some description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = True
    default = "default"
    obj = DocstringParam(args,description,arg_name,type_name,is_optional,default)
    assert obj.args == args
    assert obj.description == description
    assert obj.arg_name == arg_name
    assert obj.type_name == type_name
    assert obj.is_optional == is_optional
    assert obj.default == default
    helper_test_docstring_meta(args, description, obj)


# Generated at 2022-06-13 19:36:59.108464
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring_test = Docstring()
    assert docstring_test.short_description is None
    assert docstring_test.long_description is None
    assert docstring_test.meta == []


if __name__ == "__main__":
    test_Docstring()

# Generated at 2022-06-13 19:37:04.032814
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    meta_deprecate = DocstringDeprecated(['deprecated'], 'test', '1.0')
    assert meta_deprecate.args == ['deprecated']
    assert meta_deprecate.description == 'test'
    assert meta_deprecate.version == '1.0'


# Generated at 2022-06-13 19:37:08.774804
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    test_args = ['a', 'b']
    test_description = 'test description'
    a = DocstringMeta(test_args, test_description)
    assert a.args == test_args
    assert a.description == test_description


# Generated at 2022-06-13 19:37:16.877139
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    '''
    This function will test a constructor of the DocstringDeprecated class
    '''
    # This is a constructor we want to test in this function:
    # def __init__(self, args: T.List[str], description: T.Optional[str], version: T.Optional[str]) -> None:

    # create an instance of DocstringDeprecated class
    # DocstringDeprecated(args: T.List[str], description: T.Optional[str], version: T.Optional[str]) -> None
    my_docstring_deprecated = DocstringDeprecated(["param", "argument"], "description", "version")
    # check if we have all the attributes in our DocstringDeprecated class
    assert hasattr(my_docstring_deprecated, 'args')
    assert hasattr(my_docstring_deprecated, 'description')


# Generated at 2022-06-13 19:38:30.596786
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    dr = DocstringReturns(["arg"], "description", "String", False)
    assert dr.args == ["arg"] and dr.description == "description" and dr.type_name == "String"


# Generated at 2022-06-13 19:38:37.915165
# Unit test for constructor of class Docstring
def test_Docstring():
    # test initialized correctly
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []
    # test getters
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.deprecation is None

# Generated at 2022-06-13 19:38:40.492458
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
	DocstringReturns(args, description, type_name, is_generator, return_name)


# Generated at 2022-06-13 19:38:45.278409
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta([""], "")
    assert a.description == ""
    assert a.args == [""]


# Generated at 2022-06-13 19:38:47.470138
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None



# Generated at 2022-06-13 19:38:49.618151
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    DocstringParam(["param"], "this is a description", "arg", "str", True, "0")


# Generated at 2022-06-13 19:38:54.334314
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():

    params = ["param", "arg"]
    description = "The position of a result block relative to the current search result set."
    test_meta = DocstringMeta(params, description)
    assert_list_eq(test_meta.args, params)
    assert_string_eq(test_meta.description, description)



# Generated at 2022-06-13 19:38:55.195247
# Unit test for constructor of class ParseError
def test_ParseError():
    assert str(ParseError("test error")) == "test error"


# Generated at 2022-06-13 19:39:00.671949
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta
    assert d.__init__([], "")
    assert d.__init__(["param"], "")
    assert d.__init__(["yields"], "")
    assert d.__init__(["argument"], "")
    assert d.__init__(["keyword"], "")
    assert d.__init__(["raises"], "")
    assert d.__init__(["return"], "")
    assert d.__init__(["returns"], "")
    assert d.__init__(["except"], "")
    assert d.__init__(["exception"], "")


# Generated at 2022-06-13 19:39:03.094716
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated = DocstringDeprecated(["deprecated"], "description", "version")
    assert docstring_deprecated != None
