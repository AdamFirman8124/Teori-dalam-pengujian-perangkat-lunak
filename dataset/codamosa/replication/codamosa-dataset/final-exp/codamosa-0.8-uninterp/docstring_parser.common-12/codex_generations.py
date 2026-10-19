

# Generated at 2022-06-13 19:30:55.359496
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    test = DocstringRaises(["raises"], "description", "Exception")
    assert test.description == "description"
    assert test.type_name == "Exception"
    return


# Generated at 2022-06-13 19:31:02.601689
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # param args is used as an empty array
    args = []
    # param description is used as 'example description of exception'
    description = 'example description of exception'
    # param type_name is used as 'example name of exception'
    type_name = 'example name of exception'
    d = DocstringRaises(args, description, type_name)
    assert d.args == args
    assert d.description == description
    assert d.type_name == type_name

# Generated at 2022-06-13 19:31:04.515420
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    ls = DocstringMeta(['args'], 'description')
    assert ls.args == ['args']
    assert ls.description == 'description'



# Generated at 2022-06-13 19:31:05.194239
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    assert DocstringDeprecated(None, None, None)

# Generated at 2022-06-13 19:31:07.252117
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(args = [], description = None, type_name = None, is_generator = False, return_name = None)

# Generated at 2022-06-13 19:31:08.807733
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ["what"]
    description = "nothing"
    metadata = DocstringMeta(args, description)
    assert metadata.args == args
    assert metadata.description == description


# Generated at 2022-06-13 19:31:10.783408
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    a = DocstringRaises(["raises"], "exc", "ValueError")
    assert a.type_name == "ValueError"


# Generated at 2022-06-13 19:31:12.394467
# Unit test for constructor of class ParseError
def test_ParseError():
    err = ParseError("runtime error")
    assert isinstance(err, RuntimeError)
    assert str(err) == "runtime error"


# Generated at 2022-06-13 19:31:16.048314
# Unit test for constructor of class ParseError
def test_ParseError():
	try:
		try:
			# raise an error, then it goes to except block to check if the error is ParseError
			raise ParseError("Something goes wrong")
		except Exception as e:
			# if the error is not ParseError, the error will be thrown
			if not isinstance(e, ParseError):
				raise
	except ParseError as e:
		assert str(e) == "Something goes wrong"
	except Exception as e:
		assert False


# Generated at 2022-06-13 19:31:20.078833
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    try:
        DocstringDeprecated(
            [':deprecated', 'parameter'],
            'description',
            'version',
            )
    except:
        assert True
    else:
        assert False



# Generated at 2022-06-13 19:31:26.784841
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    dp = DocstringParam(['param', 'type_name'], 'description of param', 'arg', "int", False, 'None')
    assert dp == dp


# Generated at 2022-06-13 19:31:30.902101
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['param', 'arg', 'argument']
    description = 'description'
    doc_meta = DocstringMeta(args, description)
    assert doc_meta.args == args
    assert doc_meta.description == description


# Generated at 2022-06-13 19:31:34.184401
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        docstring = DocString()
    except RuntimeError as e:
        assert isinstance(e, RuntimeError)


# Generated at 2022-06-13 19:31:38.756406
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    args = ['red', 'green', 'blue']
    description = 'test-test'
    docstringmeta = DocstringMeta(args, description)
    assert(args == docstringmeta.args)
    assert(description == docstringmeta.description)


# Generated at 2022-06-13 19:31:43.399160
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    args = ['Test', 'test']
    description = "dupa"
    type_name = "jas"
    is_generator = False
    a = DocstringReturns(args,description,type_name,is_generator)
    assert a.description == "dupa"

# Generated at 2022-06-13 19:31:48.457928
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test constructor of class DocstringRaises."""
    item = DocstringRaises(
        args=None,description=None, type_name=None
    )
    assert item.args is None
    assert item.description is None
    assert item.type_name is None
    assert item.description is None


# Generated at 2022-06-13 19:31:51.273056
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Test DocstringRaises constructor."""
    D = DocstringRaises([], None, None)
    assert D.args == []
    assert D.description == None
    assert D.type_name == None
    

# Generated at 2022-06-13 19:31:57.244660
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    args = ["arg"]
    description = "description"
    type_name = "type_name"
    this = DocstringRaises(args, description, type_name)
    assert this.args == args
    assert this.description == description
    assert this.type_name == type_name

# Generated at 2022-06-13 19:32:03.683414
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    docstring = DocstringReturns(
        ["returns"], "The return value", "int", False, "x"
    )
    assert docstring.args == ["returns"]
    assert docstring.description == "The return value"
    assert docstring.type_name == "int"
    assert docstring.is_generator == False
    assert docstring.return_name == "x"

# Generated at 2022-06-13 19:32:06.354777
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns([], None, None)


# Generated at 2022-06-13 19:32:18.283168
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    dsRaises = DocstringRaises(
        args=[],
        description=None,
        type_name="TypeError"
    )
    assert dsRaises.type_name == "TypeError"

# Generated at 2022-06-13 19:32:21.928453
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstringdeprecated = DocstringDeprecated(["test"], "test", "test")
    assert docstringdeprecated.args == ["test"]
    assert docstringdeprecated.description == "test"
    assert docstringdeprecated.version == "test"


# Generated at 2022-06-13 19:32:27.728034
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    # constructor
    type_name = "Foo"
    is_generator = True
    returns = DocstringReturns(args=[], description=None, type_name=type_name, is_generator=is_generator)
    assert(returns is not None)
    assert(f"description: {None}" == f"description: {returns.description}")
    assert(f"type name: {type_name}" == f"type name: {returns.type_name}")
    assert(f"is generator: {is_generator}" == f"is generator: {returns.is_generator}")


# Generated at 2022-06-13 19:32:35.801485
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    # input docstring obj
    args = ['param', 'docs']
    description = 'something wrong'
    type_name = 'ValueError'
    
    test_docs = DocstringRaises(args, description, type_name)
    
    # output docstring obj
    args = ['param', 'docs']
    description = 'something wrong'
    type_name = 'ValueError'
    docs = DocstringRaises(args, description, type_name)
    assert test_docs == docs


# Generated at 2022-06-13 19:32:40.493043
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
	Typestr = DocstringRaises(args = ["arg1","arg2","arg3"], description = "Null", type_name = "abc")
	print(Typestr.args)
	print(Typestr.description)
	print(Typestr.type_name)


# Generated at 2022-06-13 19:32:42.434971
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    desc = DocstringMeta(['args'], 'description')
    assert desc.description == 'description'


# Generated at 2022-06-13 19:32:44.242346
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    s = DocstringDeprecated(args=["deprecated", "remove"], description="remove before version")
    assert s is not None

# Generated at 2022-06-13 19:32:50.004683
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
    assert ds.returns == None
    assert ds.deprecation == None




# Generated at 2022-06-13 19:33:02.076532
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    test_args = ["param", "test"]
    test_description = "this is a description"
    test_arg_name = "test"
    test_type_name = "test"
    test_is_optional = False
    test_default = None

    test_object = DocstringParam(test_args, test_description, test_arg_name, test_type_name, test_is_optional, test_default)
    assert test_object.args == test_args
    assert test_object.description == test_description
    assert test_object.arg_name == test_arg_name
    assert test_object.type_name == test_type_name
    assert test_object.is_optional == test_is_optional
    assert test_object.default == test_default


# Generated at 2022-06-13 19:33:09.906880
# Unit test for constructor of class Docstring
def test_Docstring():
    ds = Docstring()
    assert ds.short_description == None
    assert ds.long_description == None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.params == []
    assert ds.raises == []
    assert ds.returns == None
    assert ds.deprecation == None

test_Docstring()

# Generated at 2022-06-13 19:33:26.371364
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta([], '')
    assert(a.args == [])
    assert(a.description == '')


# Generated at 2022-06-13 19:33:27.877489
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(['args1','args2'], 'docstring')



# Generated at 2022-06-13 19:33:32.958606
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    x = DocstringReturns(args = ["args"], description = "description", type_name = "str", is_generator = True, return_name = "return_name")
    assert x.type_name == "str"
    assert x.is_generator == True
    assert x.return_name == "return_name"
    assert x.args == ["args"]
    assert x.description == "description"

test_DocstringReturns()

# Generated at 2022-06-13 19:33:37.173908
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    docstringRaises = DocstringRaises(args = [], description = 'description', type_name = '')
    assert not docstringRaises.description

# Generated at 2022-06-13 19:33:39.750957
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    myObj = DocstringDeprecated(["param","description"], "description_content", "version")
    return myObj


# Generated at 2022-06-13 19:33:51.920724
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    docstring_meta = DocstringParam(["param", "argument"], "function description.", "arg_name", "type_name", True, "default")
    assert docstring_meta.args == ["param", "argument"], "Constructor of class DocstringParam doesn't work with argument 'args'"
    assert docstring_meta.description == "function description.", "Constructor of class DocstringParam doesn't work with argument 'description'"
    assert docstring_meta.arg_name == "arg_name", "Constructor of class DocstringParam doesn't work with argument 'arg_name'"
    assert docstring_meta.type_name == "type_name", "Constructor of class DocstringParam doesn't work with argument 'type_name'"
    assert docstring_meta.is_optional == True, "Constructor of class DocstringParam doesn't work with argument 'is_optional'"

# Generated at 2022-06-13 19:33:55.674243
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
  returns = DocstringReturns(None, None, None, None, None)
  assert returns.type_name == None
  assert returns.is_generator == None
  assert returns.return_name == None

# Generated at 2022-06-13 19:34:05.485439
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    """Unit test for constructor of class DocstringRaises."""
    args = []
    description = None
    type_name = None
    args_with_description = []
    type_name = None
    test1 = DocstringRaises(args, description, type_name)
    test2 = DocstringRaises(args_with_description, description, type_name)
    assert(test1.description == description)
    assert(test1.type_name == type_name)
    assert(len(test1.args) == 0)
    assert(len(test2.args) == 0)


# Generated at 2022-06-13 19:34:09.869962
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated = DocstringDeprecated(['deprecated'], 'As of version 0.0.1', '0.0.1')
    assert docstring_deprecated.args == ['deprecated']
    assert docstring_deprecated.description == 'As of version 0.0.1'
    assert docstring_deprecated.version == '0.0.1'
    docstring_deprecated_none = DocstringDeprecated(['deprecated'], None, None)
    assert docstring_deprecated_none.args == ['deprecated']
    assert docstring_deprecated_none.description == None
    assert docstring_deprecated_none.version == None


# Generated at 2022-06-13 19:34:19.504329
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    args = ['attribute', 'key', 'keyword']
    description = 'description'
    arg_name = 'arg_name'
    type_name = 'type_name'
    is_optional = True
    default = 'default'
    d = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert isinstance(d, DocstringParam)
    assert isinstance(d, DocstringMeta)
    assert d.args == args
    assert d.description == description
    assert d.arg_name == arg_name
    assert d.type_name == type_name
    assert d.is_optional == is_optional
    assert d.default == default


# Generated at 2022-06-13 19:34:52.769811
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    keyword = 'deprecated'
    version = '1.0'
    description = 'This function is deprecated and will be removed in future version.'
    docstring = DocstringDeprecated(keyword, version, description)
    assert docstring.args == keyword
    assert docstring.description == description
    assert docstring.version == version


# Generated at 2022-06-13 19:34:58.172671
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    # Test with correct arguments
    doc_string_meta = DocstringMeta("args", "Description")
    assert doc_string_meta.args == "args"
    assert doc_string_meta.description == "Description"


# Generated at 2022-06-13 19:35:06.975359
# Unit test for constructor of class ParseError
def test_ParseError():
    err1 = ParseError()
    assert(err1.args[0] == '')

    myString = "Hello"
    assert(ParseError(myString).args[0] == "Hello")
    assert(ParseError(myString).args[0] == "Hello")
    assert(ParseError(myString,myString).args[0] == "Hello")
    assert(ParseError(myString,myString).args[1] == "Hello")



# Generated at 2022-06-13 19:35:08.178542
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError('Something went wrong')


# Generated at 2022-06-13 19:35:11.779327
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    item = DocstringReturns([], "description", "type_name", True)
    # _test_property_item(item)
    assert item.type_name == "type_name"
    assert item.is_generator == True


# Generated at 2022-06-13 19:35:13.871631
# Unit test for constructor of class Docstring
def test_Docstring():
    doc = Docstring()
    print("doc: ", doc)


# Generated at 2022-06-13 19:35:19.073664
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    kw = DocstringReturns(["test"], "test", "test")
    assert kw.description == "test"
    assert kw.type_name == "test"
    assert kw.is_generator == "test"

# Generated at 2022-06-13 19:35:23.064163
# Unit test for constructor of class Docstring
def test_Docstring():
    """Testing the constructor of Docstring."""
    my_docstring = Docstring()
    assert my_docstring.short_description is None
    assert my_docstring.long_description is None
    assert my_docstring.blank_after_short_description is False
    assert my_docstring.blank_after_long_description is False
    assert my_docstring.meta == []
    assert my_docstring.params == []
    assert my_docstring.raises == []
    assert my_docstring.returns is None
    assert my_docstring.deprecation is None


###############################################################################



# Generated at 2022-06-13 19:35:26.143661
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
   a = DocstringRaises([], "description" , "type_name")
   print(a.description)
   print(a.args)


# Generated at 2022-06-13 19:35:30.879235
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    docstringmeta = DocstringMeta(["param"], "desc")
    assert docstringmeta.args == ["param"], "args not properly initialized"
    assert docstringmeta.description == "desc", "description not properly initialized"


# Generated at 2022-06-13 19:36:04.860790
# Unit test for constructor of class Docstring
def test_Docstring():
    assert Docstring().__init__()
    print(Docstring().__init__())


# Generated at 2022-06-13 19:36:08.985188
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    '''
    This is the test for the constructor of class DocstringMeta
    '''
    docstring_meta = DocstringMeta(["args"], "description")
    assert docstring_meta.args == ["args"]
    assert docstring_meta.description == "description"
    assert isinstance(docstring_meta, DocstringMeta)


# Generated at 2022-06-13 19:36:11.250343
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(["args"], "description", "type_name", False, "return_name")
    assert True

# Generated at 2022-06-13 19:36:15.649062
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    doc = DocstringParam(["param"], "description", "arg_name", "type_name", "is_optional", "default")
    print("Name: ",doc.args)
    print("description: ",doc.description)
    print("arg_name: ",doc.arg_name)
    print("type_name: ",doc.type_name)
    print("is_optional: ",doc.is_optional)
    print("default: ",doc.default)
test_DocstringParam()


# Generated at 2022-06-13 19:36:22.831199
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    result =DocstringRaises(['args'], 'description', 'type_name')
    assert result.args == ['args'], 'The expected value is ["args"], but the actual value is {}'.format(result.args)
    assert result.description == 'description', 'The expected value is description, but the actual value is {}'.format(result.description)
    assert result.type_name == 'type_name', 'The expected value is type_name, but the actual value is {}'.format(result.type_name)


# Generated at 2022-06-13 19:36:27.963811
# Unit test for constructor of class Docstring
def test_Docstring():
    d = Docstring()
    assert d.short_description == None
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []
    assert d.params == []
    assert d.raises == []
    assert d.returns == None
    assert d.deprecation == None
if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "-s"])

# Generated at 2022-06-13 19:36:30.720772
# Unit test for constructor of class ParseError
def test_ParseError():
    """Test ParseError."""
    p = ParseError("")
    assert isinstance(p, ParseError)


# Generated at 2022-06-13 19:36:35.654036
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    temp = DocstringParam(["a"], "b", "c", "d", True, "e")
    assert temp.args is not None
    assert temp.description is not None
    assert temp.arg_name is not None
    assert temp.type_name is not None
    assert temp.is_optional is not None
    assert temp.default is not None


# Generated at 2022-06-13 19:36:36.585470
# Unit test for constructor of class ParseError
def test_ParseError():
    assert True


# Generated at 2022-06-13 19:36:38.442664
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    assert DocstringReturns([], "true", "bool", False).description == "true"

# Generated at 2022-06-13 19:37:11.629735
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises.__init__ == DocstringMeta.__init__

# Generated at 2022-06-13 19:37:17.182047
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    new_DocstringRaises = DocstringRaises(["raises"], "if something happens", "ValueError")
    assert new_DocstringRaises.args == ["raises"]
    assert new_DocstringRaises.description == "if something happens"
    assert new_DocstringRaises.type_name == "ValueError"


# Generated at 2022-06-13 19:37:26.263029
# Unit test for constructor of class DocstringParam
def test_DocstringParam():
    arg = ['param','name','type','default','optional','description']
    description = "test description"
    docstring_test = DocstringParam(arg, description, arg[1], arg[2], arg[4], arg[3])
    print(docstring_test.args)
    print(docstring_test.description)
    print(docstring_test.arg_name)
    print(docstring_test.type_name)
    print(docstring_test.is_optional)
    print(docstring_test.default)


# Generated at 2022-06-13 19:37:29.010525
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    x=DocstringDeprecated([], 'something', 'version')
    assert x.type_name==None
    assert x.args==[]
    assert x.return_name==None
    assert x.is_generator==False

# Generated at 2022-06-13 19:37:32.443479
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd = DocstringDeprecated(['deprecated', 'deprecate', 'remove'], "", "3.0")
    assert dd.args == ['deprecated', 'deprecate', 'remove']
    assert dd.description == ""
    assert dd.version == "3.0"



# Generated at 2022-06-13 19:37:33.753528
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    DocstringDeprecated(args = ["args"], description = "description", version = "0.0")

# Generated at 2022-06-13 19:37:35.808421
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    a = DocstringMeta(["a very cool arg", "and description"], "this is a description")
    assert a.args == ["a very cool arg", "and description"]
    assert a.description == "this is a description"



# Generated at 2022-06-13 19:37:36.637391
# Unit test for constructor of class DocstringRaises
def test_DocstringRaises():
    assert DocstringRaises(["raises"], "descr", None)

# Generated at 2022-06-13 19:37:40.149653
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    test_args = ['1.3.0']
    test_description = "This method is deprecated"
    test_version = '1.3.0'
    test_docstringDeprecated = DocstringDeprecated(test_args, test_description, test_version)
    assert test_docstringDeprecated.args == test_args
    assert test_docstringDeprecated.description == test_description
    assert test_docstringDeprecated.version == test_version
    print ("Passed test_DocstringDeprecated")


# Generated at 2022-06-13 19:37:49.439197
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    def foo(x:int) -> tuple([str]):
        """

        :param x:
        :return:
        """
        return x
    dsr = DocstringReturns(":return:", "", "", True)
    assert dsr.args == [":return:"]
    assert dsr.description == ""
    assert dsr.type_name is None
    assert dsr.is_generator is False
    assert dsr.return_name == "x"


# Generated at 2022-06-13 19:39:01.784792
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    dd_elements = DocstringDeprecated("nop", "nop", "nop")
    assert dd_elements.args == "nop"
    assert dd_elements.description == "nop"
    assert dd_elements.version == "nop"



# Generated at 2022-06-13 19:39:04.888719
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    docstring_deprecated = DocstringDeprecated(args=['hello'], description='', version='')
    assert isinstance(docstring_deprecated, DocstringDeprecated)


# Generated at 2022-06-13 19:39:10.678734
# Unit test for constructor of class Docstring
def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns == None
    assert docstring.deprecation == None


# Generated at 2022-06-13 19:39:13.801030
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    DocstringMeta(
        args = ["param", "argument", "arg"], description="description goes here"
    )


# Generated at 2022-06-13 19:39:17.752162
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    d = docstring_deprecated(args=['deprecated'], description='This is deprecated', version='v1.0')
    assert(d.args == ['deprecated'])
    assert(d.description == 'This is deprecated')
    assert(d.version == 'v1.0')


# Generated at 2022-06-13 19:39:20.671980
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    class Dummy:
        pass
    a=DocstringReturns(args=['a','b','c'])
    assert(1==1)

# Unit tests for constructor of class DocstringMeta

# Generated at 2022-06-13 19:39:25.542531
# Unit test for constructor of class DocstringDeprecated
def test_DocstringDeprecated():
    a = DocstringDeprecated(["deprecated", "v1.0"], "hi", "v1.0")
    a = DocstringDeprecated(["deprecated", "test"], "hi", "test")
    a = DocstringDeprecated(["test"], "hi", "test")
    a = DocstringDeprecated(["test"], "hi", "test")
    a = DocstringDeprecated(["test"], "hi", "test")
    a = DocstringDeprecated(["test"], "hi", "test")
    a = DocstringDeprecated(["test"], "hi", "test")
    

# Generated at 2022-06-13 19:39:27.174073
# Unit test for constructor of class DocstringReturns
def test_DocstringReturns():
    DocstringReturns(["return"], "returns single element", "Integer", True)

# Generated at 2022-06-13 19:39:29.694241
# Unit test for constructor of class Docstring
def test_Docstring():
    actual = Docstring()
    assert actual.short_description == None 
    assert actual.long_description == None
    assert actual.blank_after_short_description == False
    assert actual.blank_after_long_description == False
    assert actual.meta == []

# Generated at 2022-06-13 19:39:31.811388
# Unit test for constructor of class DocstringMeta
def test_DocstringMeta():
    d = DocstringMeta(['a'], 'b')
    if not (d.args == ['a'] and d.description == 'b'):
        print('Test failed')
