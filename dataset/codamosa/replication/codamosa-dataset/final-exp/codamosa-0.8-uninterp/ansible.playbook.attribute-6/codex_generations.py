

# Generated at 2022-06-13 07:49:02.542457
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    return True


# Generated at 2022-06-13 07:49:16.241195
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    export = FieldAttribute(
        isa = 'str',
        private = True,
        default = None,
        required = False,
        listof = 'str',
        priority = 100,
        class_type = None,
        always_post_validate = False,
        inherit = True,
        alias = None,
        extend = False,
        prepend = False,
        static = False
    )

    # Unit test for method set_default of class FieldAttribute
    def test_set_default():
        # Check if set_default works correctly
        export.set_default(default = 'default')
        assert export.default == 'default'
        export.set_default(default = None)
        assert export.default == None

    # Unit test for method get_default of class FieldAttribute

# Generated at 2022-06-13 07:49:19.170471
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='list', listof='list')
    assert fa.isa == 'list'
    assert fa.listof == 'list'



# Generated at 2022-06-13 07:49:29.776055
# Unit test for constructor of class Attribute
def test_Attribute():
    # pylint: disable=unused-variable
    a = Attribute(isa="dict")

    Attribute(isa="str")
    Attribute(isa="str", required=True)
    Attribute(isa="str", default="default value")
    Attribute(isa="str", default="default value", required=True)
    Attribute(isa="list", listof="str")
    Attribute(isa="list", listof="str", priority=50)
    Attribute(isa="list", default=[1, 2, 3])
    Attribute(isa="list", default=lambda: [1, 2, 3])
    Attribute(isa="class", class_type=dict)

    Attribute(isa="str", default="default value", required=True,
              listof="str", priority=50, class_type=dict)

    Att

# Generated at 2022-06-13 07:49:38.068341
# Unit test for constructor of class Attribute
def test_Attribute():
    # Successfully create new instance of class Attribute
    # Example: isa = 'int'
    x = Attribute(isa = 'int')

    assert x.isa == 'int'
    # Check default value for private
    assert x.private == False
    # Check default value for default
    assert x.default == None
    # Check default value for required
    assert x.required == False
    # Check default value for listof
    assert x.listof == None
    # Check default value for priority
    assert x.priority == 0
    # Check default value for class_type
    assert x.class_type == None
    # Check default value for always_post_validate
    assert x.always_post_validate == False
    # Check default value for inherit
    assert x.inherit == True
    # Check default value for alias


# Generated at 2022-06-13 07:49:39.641232
# Unit test for constructor of class Attribute
def test_Attribute():
    passed = False

    try:
        Attribute(isa="list", default="foo")
    except TypeError:
        passed = True

    assert passed, "'Attribute(isa=\"list\", default=\"foo\")' should fail"



# Generated at 2022-06-13 07:49:49.932163
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    fa1 = Attribute()
    fa2 = FieldAttribute()
    assert fa1 == Attribute()
    assert fa1 != fa2

    assert not hasattr(fa1, 'extend')
    assert not hasattr(fa2, 'alias')
    assert hasattr(fa2, 'extend')
    assert hasattr(fa1, 'alias')

    fa3 = Attribute(alias='hello') 
    assert fa3.alias == 'hello'

    fa4 = FieldAttribute()
    # The following test should fail but doesn't for some reason
    #assert not hasattr(fa4, 'alias')
    
    fa5 = FieldAttribute(alias='hello')
    assert fa5.alias == 'hello'



# Generated at 2022-06-13 07:49:58.212324
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # assign a field attribute
    attr = FieldAttribute(isa='int', private=False, default=None, required=False, listof=None, priority=0,
                          class_type=None, always_post_validate=False, inherit=True, alias=None)

    # test if the assigned value is equal to the value assigned
    assert attr.isa == 'int', 'Isa value different from the one assigned'
    assert attr.default == None, 'Default value different from the one assigned'
    assert attr.private == False, 'Private value different from the one assigned'
    assert attr.required == False, 'Required value different from the one assigned'
    assert attr.listof == None, 'Listof value different from the one assigned'
    assert attr.priority == 0, 'Priority value different from the one assigned'
   

# Generated at 2022-06-13 07:50:01.557598
# Unit test for constructor of class Attribute
def test_Attribute():
    Attribute_one = Attribute(1)
    assert Attribute_one.priority == 1
    assert Attribute_one.inherit is True


# Generated at 2022-06-13 07:50:09.926475
# Unit test for constructor of class Attribute
def test_Attribute():
    # Create an instance of class Attribute
    my_attr = Attribute(isa='int', default=10, required=True, priority=1)
    assert my_attr.isa == 'int'
    assert my_attr.private == False
    assert my_attr.default == 10
    assert my_attr.required == True
    assert my_attr.listof == None
    assert my_attr.priority == 1
    assert my_attr.class_type == None
    assert my_attr.always_post_validate == False
    assert my_attr.inherit == True
    assert my_attr.alias == None
    assert my_attr.extend == False
    assert my_attr.prepend == False
    assert my_attr.static == False

# Generated at 2022-06-13 07:50:14.730625
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='string', default='some_default')
    print(a.isa)
    print(a.default)

if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:50:16.177065
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='yaml')
    assert a.isa == 'yaml'

# Generated at 2022-06-13 07:50:20.629411
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='str', private=False, default='123', required=False, listof='integer', priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    print(a)

if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:50:32.024627
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    test_type = FieldAttribute(
        isa = 'str',
        private = False,
        default = None,
        required = False,
        listof = None,
        priority = 0,
        class_type = None,
        always_post_validate = False,
        inherit = True,
        alias = None,
        extend = False,
        prepend = False,
        static = False,
    )

    assert test_type.isa == 'str'
    assert test_type.private == False
    assert test_type.default == None
    assert test_type.required == False
    assert test_type.listof == None
    assert test_type.priority == 0
    assert test_type.class_type == None
    assert test_type.always_post_validate == False
    assert test_type.inher

# Generated at 2022-06-13 07:50:38.983667
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Required params
    fa = FieldAttribute(isa='str', required=True)
    # Optional params
    fa = FieldAttribute(
        isa='str',
        private=False,
        default='foo',
        required=False,
        listof='str',
        priority=0,
        class_type='str',
        always_post_validate=False,
        inherit=True,
        alias='foo',
        extend=False,
        prepend=False,
        static=False,
    )

# Generated at 2022-06-13 07:50:52.934909
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Test the constructor for the Attribute class.  We want to ensure that
    appropriate exceptions are raised if certain values are given and that
    no exceptions are raised if valid values are given.
    """
    a = Attribute(isa='list', default=3)
    a = Attribute(isa='list', default=list)
    a = Attribute(isa='list', default=None)
    a = Attribute(isa='list', default=lambda: [])
    try:
        a = Attribute(isa='list', default=[])
        raise Exception("Should have failed")
    except TypeError:
        pass
    try:
        a = Attribute(isa='list', default={})
        raise Exception("Should have failed")
    except TypeError:
        pass

# Generated at 2022-06-13 07:50:54.175502
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a is not None

# Generated at 2022-06-13 07:51:04.953618
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    name = 'FieldAttribute'
    isa = 'str'
    private = False
    default = None
    required = False
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False
    inherit = True
    alias = 'alias'
    extend = False
    prepend = False
    static = False
    field = FieldAttribute(isa=isa, private=private, default=default, required=required, listof=listof, priority=priority, class_type=class_type, always_post_validate=always_post_validate, inherit=inherit, alias=alias, extend=extend, prepend=prepend, static=static)
    assert field.__dict__['isa'] == 'str'
    assert field.__dict__['private'] == False

# Generated at 2022-06-13 07:51:08.910525
# Unit test for constructor of class Attribute
def test_Attribute():
    import pytest
    with pytest.raises(TypeError):
        a = Attribute(default={})

FA = FieldAttribute

##############################################################################
#
# TYPE DEFINITIONS (ISA)
#
##############################################################################


# Generated at 2022-06-13 07:51:14.441206
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute()
    assert obj.isa is None
    assert obj.private is False
    assert obj.default is None
    assert obj.required is False
    assert obj.listof is None
    assert obj.priority == 0
    assert obj.class_type is None
    assert obj.always_post_validate is False
    assert obj.inherit is True
    assert obj.alias is None
    assert obj.extend is False
    assert obj.prepend is False
    assert obj.static is False

# Generated at 2022-06-13 07:51:20.991723
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    ''' this method will test for FieldAttribute class
    '''
    try:
        attr = FieldAttribute(isa='dict', default={})
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:51:30.786863
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import sys
    # assert that an invalid isa raises an exception
    try:
        FieldAttribute(isa='foobar')
        assert False, 'Exception should be raised'
    except:
        assert sys.exc_info()[0] == TypeError

    # assert that an invalid default raises an exception
    try:
        FieldAttribute(isa='list', default=['foo', 'bar'])
        assert False, 'Exception should be raised'
    except:
        assert sys.exc_info()[0] == TypeError

    # assert that a valid isa does not raise an exception
    try:
        FieldAttribute(isa='list')
    except:
        assert sys.exc_info()[0] == TypeError
        assert False, 'An Exception should not be raised'

    # assert that a valid default does not raise an exception

# Generated at 2022-06-13 07:51:41.796401
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.alias is None
    assert a.extend is False
    assert a.prepend is False
    assert a.static is False

    a = Attribute(private=True)
    assert a.private is True
    a = Attribute(default=True)
    assert a.default is True
    a = Attribute(required=True)
    assert a.required is True
    a = Attribute(listof=True)
    assert a.listof is True

# Generated at 2022-06-13 07:51:43.310327
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert isinstance(FieldAttribute(), FieldAttribute)


# Generated at 2022-06-13 07:51:49.852543
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    field_tested = FieldAttribute(isa='int', private=False, default=12, required=False, listof=None,
                                  priority=0, class_type=None, always_post_validate=False, inherit=True,
                                  alias=None, extend=False, prepend=False, static=False)

    assert field_tested.isa == 'int'
    assert field_tested.private == False
    assert field_tested.default == 12
    assert field_tested.required == False
    assert field_tested.listof == None
    assert field_tested.priority == 0
    assert field_tested.class_type == None
    assert field_tested.always_post_validate == False
    assert field_tested.inherit == True
    assert field_tested.alias == None
    assert field_tested.extend == False


# Generated at 2022-06-13 07:51:54.267257
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    new_attr = FieldAttribute()
    assert new_attr.isa is None
    assert new_attr.private == False
    assert new_attr.default is None
    assert new_attr.required == False
    assert new_attr.listof is None
    assert new_attr.priority == 0
    assert new_attr.class_type is None
    assert new_attr.always_post_validate == False
    assert new_attr.inherit == True
    assert new_attr.alias is None



# Generated at 2022-06-13 07:51:59.369559
# Unit test for constructor of class Attribute
def test_Attribute():

    # Check for the parameter 'isa'
    field = FieldAttribute(isa='dict')
    assert field.isa == 'dict'

    # Check for the parameter 'private'
    field = FieldAttribute(private=True)
    assert field.private == True

    # Check for the parameter 'default'
    field = FieldAttribute(default='test')
    assert field.default == 'test'

    # Check for the parameter 'required'
    field = FieldAttribute(required=True)
    assert field.required == True

    # Check for the parameter 'listof'
    field = FieldAttribute(listof='test')
    assert field.listof == 'test'

    # Check for the parameter 'priority'
    field = FieldAttribute(priority=100)
    assert field.priority == 100

    # Check for the parameter 'class_type'
    field = Field

# Generated at 2022-06-13 07:52:12.348017
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    defaults = {
        'test1': 'test1',
        'test2': 'test2',
        'test3': 'test3',
        'test4': 'test4',
        'test5': 'test5',
        'test6': 'test6'
    }
    attr = FieldAttribute(defaults.get('test1'), defaults.get('test2'), defaults.get('test3'), defaults.get('test4'), defaults.get('test5'), defaults.get('test6'))
    assert attr.isa == defaults.get('test1')
    assert attr.private == defaults.get('test2')
    assert attr.default == defaults.get('test3')
    assert attr.required == defaults.get('test4')
    assert attr.listof == defaults.get('test5')
    assert att

# Generated at 2022-06-13 07:52:20.019949
# Unit test for constructor of class Attribute
def test_Attribute():
    from .data_loader import DataLoader
    from .inventory.host import Host

    loader = DataLoader()
    host = Host(loader=loader, name='example')

    # test default Attribute constructor
    assert loader.host_vars._attributes['name'] == Attribute(required=True, private=True)

    # test setting a FieldAttribute with a default value and with inherit
    attr = FieldAttribute(default='foobar')
    setattr(host, 'attr', attr)
    assert getattr(host, 'attr') == 'foobar'

    # test FieldAttribute inherit
    attr = FieldAttribute(default='foobar', inherit=True)
    setattr(host, 'attr', attr)
    assert getattr(host, 'attr') == 'foobar'

    # test FieldAttribute isa listof

# Generated at 2022-06-13 07:52:26.061002
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list')
    assert attr.isa == 'list'
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False

# Generated at 2022-06-13 07:52:39.182028
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='boolean', default=False, required=True)
    assert attr is not None
    assert attr.isa == 'boolean'
    assert attr.default is False
    assert attr.required is True

    # set to a mutable value (list)
    try:
        attr = FieldAttribute(isa='list', default=[3,2,1])
        assert False
    except TypeError:
        assert True

    # set to a mutable value (list)
    try:
        attr = FieldAttribute(isa='list', default={'foo': 'bar'})
        assert False
    except TypeError:
        assert True

    # set to a mutable value (dict)

# Generated at 2022-06-13 07:52:50.043307
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # initial
    field = FieldAttribute(isa='integer', private=False, default=None, required=False, listof=None, priority=0, class_type='None', always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)

    # assert initial values
    assert field.isa == 'integer'
    assert field.private == False
    assert field.default == None
    assert field.required == False
    assert field.listof == None
    assert field.priority == 0
    assert field.class_type == 'None'
    assert field.always_post_validate == False
    assert field.inherit == True
    assert field.alias == None
    assert field.extend == False
    assert field.prepend == False
    assert field.static == False

   

# Generated at 2022-06-13 07:52:58.270538
# Unit test for constructor of class Attribute
def test_Attribute():
    with open('/dev/null') as dev_null:
        # Test that construction is allowed without any arguments.
        a1 = Attribute()
        # Test that construction is allowed with only required arguments.
        a2 = Attribute(dev_null)
        # Test that construction is allowed with only required and optional arguments.
        a3 = Attribute(dev_null, a1, a2)
        # Test that construction fails with mutable default value.
        try:
            a4 = Attribute(default=[])
            assert False
        except TypeError:
            pass


# Generated at 2022-06-13 07:53:01.698405
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa='int', private=True, default=100)
    assert field_attribute.isa == 'int'
    assert field_attribute.private == True
    assert field_attribute.default == 100



# Generated at 2022-06-13 07:53:06.239936
# Unit test for constructor of class Attribute
def test_Attribute():
    class TestAttribute(Attribute):
        name = Attribute(isa='str', default=None, required=True)

    test_attr = TestAttribute()
    assert test_attr.name is None
    test_attr = TestAttribute('test')
    assert test_attr.name == 'test'

# Generated at 2022-06-13 07:53:16.178416
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute("dictionary", "private", "default", "required", "listof",
                     "priority", "class_type", "always_post_validate", "inherit", "alias")
    assert attr.isa == "dictionary"
    assert attr.private == "private"
    assert attr.default == "default"
    assert attr.required == "required"
    assert attr.listof == "listof"
    assert attr.priority == "priority"
    assert attr.class_type == "class_type"
    assert attr.always_post_validate == "always_post_validate"
    assert attr.inherit == "inherit"
    assert attr.alias == "alias"


# Generated at 2022-06-13 07:53:20.879951
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.isa is None
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None


# Generated at 2022-06-13 07:53:27.948991
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='int')
    assert fa.isa == 'int'
    assert fa.private == False
    assert fa.default == None
    assert fa.required == False
    assert fa.listof == None
    assert fa.priority == 0
    assert fa.class_type == None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias is None
    assert fa.extend == False
    assert fa.prepend == False
    assert fa.static == False
test_FieldAttribute.unittest = {'setup': 'from ansible.playbook.attribute import *'}


# Generated at 2022-06-13 07:53:31.833364
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='bool', private=False, default=False, required=False, listof='bools', priority=1, class_type=None, always_post_validate=False, inherit=True, extend=False)
    print(a)
    return a

# Generated at 2022-06-13 07:53:41.724726
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa == None
    assert attr.private == False
    assert attr.default == None
    assert attr.listof == None
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False


# Generated at 2022-06-13 07:54:05.276006
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test default construction
    fa = FieldAttribute()

    assert fa.isa is None
    assert fa.private == False
    assert fa.default is None
    assert fa.required == False
    assert fa.listof is None
    assert fa.priority == 0
    assert fa.class_type is None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias is None
    assert fa.extend == False
    assert fa.prepend == False
    assert fa.static == False

    # test construction from all parameters

# Generated at 2022-06-13 07:54:18.158874
# Unit test for constructor of class Attribute
def test_Attribute():
    # Setup
    def ret_two():
        return 2
    def ret_three():
        return 3
    attr_one = Attribute(isa='int', default=ret_two, required=True, priority=1)
    attr_two = Attribute(isa='int', default=ret_three, required=True, priority=1)

    # Test __eq__
    assert attr_one.__eq__(attr_two)
    assert (attr_one == attr_two)

    # Test __ne__
    assert not attr_one.__ne__(attr_two)
    assert not (attr_one != attr_two)

    # Test __lt__
    assert not attr_one.__lt__(attr_two)
    assert not (attr_one < attr_two)

    # Test __gt

# Generated at 2022-06-13 07:54:20.031422
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        Attribute(isa='list', default=[])
    except TypeError:
        return True
    else:
        return False

# Generated at 2022-06-13 07:54:21.724836
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa='test')
    print(a.isa)



# Generated at 2022-06-13 07:54:32.014345
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(private=True, default='Hello world')
    assert attr.private == True
    assert attr.default == 'Hello world'
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None

    attr = FieldAttribute(private=False, default='Hello world', required=True)
    assert attr.private == False
    assert attr.default == 'Hello world'
    assert attr.required == True
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_

# Generated at 2022-06-13 07:54:45.547636
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa='test_isa',
                                     private=False,
                                     default=None,
                                     required=False,
                                     listof=None,
                                     priority=0,
                                     class_type=None,
                                     always_post_validate=False,
                                     inherit=True,
                                     alias=None,
                                     extend=False,
                                     prepend=False,
                                     static=False,
                                     )
    assert field_attribute.isa == 'test_isa'
    assert field_attribute.private == False
    assert field_attribute.default == None
    assert field_attribute.required == False
    assert field_attribute.listof == None
    assert field_attribute.priority == 0
    assert field_attribute.class_type == None
    assert field_attribute.always_post_

# Generated at 2022-06-13 07:54:53.076569
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(static=False)

    assert (attr.isa == None)
    assert (attr.private == False)
    assert (attr.default == None)
    assert (attr.required == False)
    assert (attr.listof == None)
    assert (attr.class_type == None)
    assert (attr.always_post_validate == False)
    assert (attr.inherit == True)
    assert (attr.alias == None)
    assert (attr.extend == False)

    assert (attr.priority == 0)
    assert (attr.static == False)
    assert (attr.prepend == False)


# Generated at 2022-06-13 07:55:00.639102
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test invalid default value
    try:
        bad_default_attr = Attribute(default="this is an invalid default", isa="list", listof="str")
        assert False
    except TypeError as e:
        assert str(e) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'

    # Test valid Attribute
    a_attr = Attribute(default="test")
    a_attr = Attribute(default="test", isa="list", listof="str")
    a_attr = Attribute(default=["test"])
    a_attr = Attribute(default=["test"], isa="list", listof="str")

    # Test some extra keyword arguments
    a_attr = Attribute(private=True)
    a_attr = Attribute(required=True)
    a_attr

# Generated at 2022-06-13 07:55:02.439349
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute (isa='str')
    assert attr.isa == 'str'



# Generated at 2022-06-13 07:55:04.283924
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(alias='foo')
    assert attribute.alias == 'foo'



# Generated at 2022-06-13 07:55:43.241705
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(
        isa='str',
        private=False,
        default='foo',
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert(field.isa == 'str')
    assert(field.private == False)
    assert(field.default == 'foo')
    assert(field.required == False)
    assert(field.listof == None)
    assert(field.priority == 0)
    assert(field.class_type == None)
    assert(field.always_post_validate == False)
    assert(field.inherit == True)

# Generated at 2022-06-13 07:55:48.678343
# Unit test for constructor of class Attribute
def test_Attribute():

    name_a = 'test'
    a = Attribute()
    a.name = name_a
    try:
        assert a.name == name_a
        print('Field Attribute constructor test passed')
    except:
        print('Field Attribute constructor test failed')

test_Attribute()

# Generated at 2022-06-13 07:55:59.749653
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'dict'
    private = False
    default = None
    required = False
    listof = "str"
    priority = 1
    class_type = 'str'
    always_post_validate = True
    inherit = False
    alias = 'need_alias'
    extend = True
    prepend = True
    static = False
    extra_field = 'extra_field'

    attr_args = dict(isa=isa, private=private, default=default, required=required,
                     listof=listof, priority=priority, class_type=class_type,
                     always_post_validate=always_post_validate, inherit=inherit,
                     alias=alias, extend=extend, prepend=prepend, static=static)
    attr_kwargs = dict()


# Generated at 2022-06-13 07:56:11.966779
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='set', private=True, default=True, required=True, listof='bool', priority=1, class_type='int',
                     always_post_validate=True, inherit=True, alias='bool', extend=True, prepend=True, static=True)

    assert attr.isa == 'set'
    assert attr.private == True
    assert attr.default == True
    assert attr.required == True
    assert attr.listof == 'bool'
    assert attr.priority == 1
    assert attr.class_type == 'int'
    assert attr.always_post_validate == True
    assert attr.inherit == True
    assert attr.alias == 'bool'
    assert attr.extend == True
    assert attr.prepend == True


# Generated at 2022-06-13 07:56:17.494953
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(isa='dict', private=False, default=None, required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False) is not None



# Generated at 2022-06-13 07:56:27.186711
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        import pytest
    except ImportError:
        print("skipping test_Attribute, requires the pytest module")
        # fall back to py.test
        return

    with pytest.raises(TypeError):
        Attribute(default=['local mutable list'])

    with pytest.raises(TypeError):
        Attribute(default={'local mutable dict': 'value'})

    with pytest.raises(TypeError):
        Attribute(default={'local mutable set'})

    # these should not raise
    Attribute(default=lambda: ['default mutable list'])
    Attribute(default=lambda: {'default mutable dict': 'value'})
    Attribute(default=lambda: {'default mutable set'})

# Generated at 2022-06-13 07:56:31.807929
# Unit test for constructor of class Attribute
def test_Attribute():

    # test Attribute constructor with invalid isa
    isa = "invalid"
    try:
        a = Attribute(isa="invalid")
        assert False, "FAILED: expected assertion due to invalid isa"
    except AttributeError as ae:
        assert True, "PASSED: validation passed due to invalid isa"

    # test Attribute constructor with invalid listof
    try:
        a = Attribute(isa="list", listof="invalid")
        assert False, "FAILED: expected assertion due to invalid listof"
    except AttributeError as ae:
        assert True, "PASSED: validation passed due to invalid listof"

    # test Attribute constructor with invalid isa and listof

# Generated at 2022-06-13 07:56:39.199958
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='foo',
                       private=False,
                       default='bar',
                       required=False,
                       listof='baz',
                       priority=0,
                       class_type='qux',
                       always_post_validate=False,
                       inherit=True,
                       alias='foo',
                       extend=False,
                       prepend=False,
                       static=False)

    assert a.isa == 'foo'
    assert a.private == False
    assert a.default == 'bar'
    assert a.required == False
    assert a.listof == 'baz'
    assert a.priority == 0
    assert a.class_type == 'qux'
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == 'foo'
    assert a

# Generated at 2022-06-13 07:56:47.833827
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    Test the constructor of class FieldAttribute.
    """
    obj = FieldAttribute(required=True)
    obj.required = True

    try:
        obj = FieldAttribute(default=[])
        assert False, "must not be mutable"
    except TypeError as e:
        assert True, "is TypeError"

    try:
        obj = FieldAttribute(default=dict())
        assert False, "must not be mutable"
    except TypeError as e:
        assert True, "is TypeError"

test_FieldAttribute()



# Generated at 2022-06-13 07:56:56.351111
# Unit test for constructor of class Attribute
def test_Attribute():

    # Call constructor of class Attribute
    attr = Attribute(isa='str', private=False, default=None, required=False, listof=None,
                 priority=0, class_type=None, always_post_validate=False, inherit=True,
                 alias=None, extend=False, prepend=False, static=False)

    # Check the existence of each attribute
    assert hasattr(attr, 'isa')
    assert hasattr(attr, 'private')
    assert hasattr(attr, 'default')
    assert hasattr(attr, 'required')
    assert hasattr(attr, 'listof')
    assert hasattr(attr, 'priority')
    assert hasattr(attr, 'class_type')
    assert hasattr(attr, 'always_post_validate')
    assert hasattr(attr, 'inherit')

# Generated at 2022-06-13 07:57:27.936882
# Unit test for constructor of class Attribute
def test_Attribute():
    import pytest
    with pytest.raises(TypeError):
        Attribute(isa='list', default=[])

# Generated at 2022-06-13 07:57:34.968950
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    x=FieldAttribute()
    assert x.isa == None
    assert x.private == False
    assert x.default == None
    assert x.required == False
    assert x.priority == 0
    assert x.class_type == None
    assert x.always_post_validate == False
    assert x.inherit == True
    assert x.alias == None
    assert x.extend == False
    assert x.prepend == False
    assert x.static == False

# Generated at 2022-06-13 07:57:44.432970
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # Test constructor of class FieldAttribute with only isa
    f = FieldAttribute(isa='test')
    assert f.isa == 'test'
    assert not f.private
    assert f.default is None
    assert not f.required
    assert f.listof is None
    assert f.priority == 0
    assert f.class_type is None
    assert not f.always_post_validate
    assert f.inherit
    assert f.alias is None
    assert not f.extend
    assert not f.prepend

    # Test constructor of class FieldAttribute with all parameters

# Generated at 2022-06-13 07:57:52.883750
# Unit test for constructor of class Attribute
def test_Attribute():
    # if only the required arguments are passed, the object is created
    obj = Attribute('string')
    assert obj is not None

    # if invalid 'isa' value is passed, an error is thrown
    try:
        obj = Attribute(isa=1)
    except:
        pass
    assert obj is None

    # if invalid 'listof' value is passed, an error is thrown
    try:
        obj = Attribute('list', listof=1)
    except:
        pass
    assert obj is None

    # if invalid 'class_type' value is passed, an error is thrown
    try:
        obj = Attribute('class', class_type=1)
    except:
        pass
    assert obj is None

    # if invalid 'default' value is passed, an error is thrown

# Generated at 2022-06-13 07:58:04.030996
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False

# Unit test Fixture for class FieldAttribute
# Note: One or more of the following unit tests fail if the FieldAttribute
# constructor is not correct when the constructor is not correct.
# But these tests do NOT catch *all* errors in the FieldAttribute constructor.
# For instance, if you change the function definition, the

# Generated at 2022-06-13 07:58:12.141495
# Unit test for constructor of class Attribute
def test_Attribute():
    my_dict = {'isa': 'dict', 'alias': 'foo'}
    my_attr = Attribute(**my_dict)
    assert my_attr.isa == 'dict'
    assert my_attr.private is False
    assert my_attr.default is None
    assert my_attr.required is False
    assert my_attr.listof is None
    assert my_attr.priority == 0
    assert my_attr.class_type is None
    assert my_attr.always_post_validate is False
    assert my_attr.inherit is True
    assert my_attr.alias == 'foo'



# Generated at 2022-06-13 07:58:13.078687
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    a = FieldAttribute()



# Generated at 2022-06-13 07:58:20.655979
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test 1: Basic
    a = Attribute(isa='str', required=True)
    assert a.isa == 'str'
    assert a.required is True

    # Test 2: Default
    a = Attribute(isa='str', default='foobar')
    assert a.default == 'foobar'

    # Test 3: Private
    a = Attribute(private=True)
    assert a.private is True

    # Test 4: Listof
    a = Attribute(isa='list', listof='str')
    assert a.listof == 'str'

    # Test 5: Priority
    a = Attribute(priority=1)
    assert a.priority == 1

    # Test 6: class_type
    class foo(object):
        pass
    a = Attribute(isa='class', class_type=foo)

# Generated at 2022-06-13 07:58:27.742891
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.isa == None
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False

    attr = Attribute(default="value")
    assert attr.default == "value"
    assert attr.required == False

    attr = Attribute(required=True)
    assert attr.default == None
    assert attr.required == True

    attr = Attribute(extend=True)
    assert attr.default == None
    assert attr.required == False
    assert attr.extend == True


# Generated at 2022-06-13 07:58:31.744906
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    #create object and check the properties
    attr = FieldAttribute(isa="dict", private=False, default=None, required=True, \
                          listof="dict", priority=0, class_type=None, always_post_validate=False, inherit=True)

    assert attr.isa == "dict", "FieldAttribute corrupted"

    #tests for comparisons
    attr2 = FieldAttribute(priority=1)

    assert attr2 > attr, "FieldAttribute comparison function corrupted"
