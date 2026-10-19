

# Generated at 2022-06-13 07:49:03.373835
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    c = FieldAttribute(isa='string', private=False, default=None, required=False, priority=0)



# Generated at 2022-06-13 07:49:17.213892
# Unit test for constructor of class Attribute
def test_Attribute():
    # Tests for boolean flags
    import pytest
    # No arguments
    attr = Attribute()
    assert attr.isa is None
    assert not attr.private
    assert attr.default is None
    assert not attr.required
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert not attr.always_post_validate
    assert attr.inherit
    assert attr.alias is None

    attr = Attribute(isa='str')
    assert attr.isa == 'str'
    assert not attr.private
    assert attr.default is None
    assert not attr.required
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
   

# Generated at 2022-06-13 07:49:26.976326
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:49:30.393719
# Unit test for constructor of class Attribute
def test_Attribute():
    expected_default = '"default value of \'name\' attribute"'
    assert Attribute(alias='name', default=expected_default).default == expected_default



# Generated at 2022-06-13 07:49:38.587771
# Unit test for constructor of class Attribute
def test_Attribute():
    # Define an Attribute object
    attr = Attribute(isa='dict', private=True, default='foo', required=True, listof='str', priority=1, class_type='int', always_post_validate=True)

    # Assert if the properties are set correctly
    assert attr.isa == 'dict'
    assert attr.private == True
    assert attr.default == 'foo'
    assert attr.required == True
    assert attr.listof == 'str'
    assert attr.priority == 1
    assert attr.class_type == 'int'
    assert attr.always_post_validate == True

    # Test if an exception is raised if default is set
    try:
        attr1 = Attribute(default='error')
    except TypeError as e:
        pass


#

# Generated at 2022-06-13 07:49:49.634986
# Unit test for constructor of class Attribute
def test_Attribute():
    # Constructor successfully creates an instance of Attribute
    new_attr = Attribute('string')
    assert isinstance(new_attr, Attribute)

    # isa defaults to None
    new_attr = Attribute()
    assert new_attr.isa is None

    # private defaults to False
    new_attr = Attribute()
    assert new_attr.private == False

    # default defaults to None
    new_attr = Attribute()
    assert new_attr.default is None

    # required defaults to False
    new_attr = Attribute()
    assert new_attr.required == False

    # listof defaults to None
    new_attr = Attribute()
    assert new_attr.listof is None

    # priority defaults to 0
    new_attr = Attribute()
    assert new_attr.priority == 0

    # class_

# Generated at 2022-06-13 07:49:55.846166
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
    assert isinstance(obj, Attribute)
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

# Generated at 2022-06-13 07:50:06.428511
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(
        isa='dict',
        private=False,
        default={'b': 2},
        required=False,
        listof='dict',
        priority=10,
        class_type='dict',
        always_post_validate=True,
        inherit=False,
        alias='alias',
        extend=True,
        prepend=True,
        static=True,
    )

    # test getter of class FieldAttribute
    assert field.alias == 'alias'

    # test setter of class FieldAttribute
    field.alias = 'aliases'
    assert field.alias == 'aliases'



# Generated at 2022-06-13 07:50:09.853041
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    >>> a = Attribute(isa='dict', required=True, default={})
    >>> a.isa, a.required, a.default
    ('dict', True, {})
    """
    pass


# Generated at 2022-06-13 07:50:20.408247
# Unit test for constructor of class Attribute
def test_Attribute():    
    attribute1 = Attribute(isa="list",
        private=False,
        default=["12", "24"],
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,)
    print(attribute1.isa)
    print(attribute1.private)
    print(attribute1.default)
    print(attribute1.required)
    print(attribute1.listof)
    print(attribute1.priority)
    print(attribute1.class_type)
    print(attribute1.always_post_validate)
    print(attribute1.inherit)
    print(attribute1.alias)
   

# Generated at 2022-06-13 07:50:27.448175
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FieldAttribute(isa='list', default=list, required=True)
    FieldAttribute(isa='dict', default=dict)
    FieldAttribute(isa='set', default=set)
    try:
        FieldAttribute(isa='dict', default={})
        assert False, 'FieldAttribute default was not immutable'
    except TypeError:
        pass



# Generated at 2022-06-13 07:50:29.975251
# Unit test for constructor of class Attribute
def test_Attribute():
    f = Attribute(isa='dict')
    assert isinstance(f, Attribute)
    assert f.isa == 'dict'

# Generated at 2022-06-13 07:50:33.390363
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert f == f
    assert f != None
    assert f > None
    assert f < None
    assert f >= None
    assert f <= None


# Generated at 2022-06-13 07:50:42.381796
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # does isa work?
    try:
        a = FieldAttribute(isa=int)
    except TypeError:
        raise Exception("isa didn't work")

    # does private work?
    try:
        a = FieldAttribute(private=True)
    except TypeError:
        raise Exception("private didn't work")

    # does default work?
    try:
        a = FieldAttribute(default=1)
    except TypeError:
        raise Exception("default didn't work")

    # does required work?
    try:
        a = FieldAttribute(required=True)
    except TypeError:
        raise Exception("required didn't work")

    # does static work?
    try:
        a = FieldAttribute(static=True)
    except TypeError:
        raise Exception("static didn't work")

    # does listof work?


# Generated at 2022-06-13 07:50:44.266663
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    print("test_FieldAttribute")
    a = FieldAttribute()



# Generated at 2022-06-13 07:50:48.232673
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
        isa='bool',
        default=True
    )

    assert field_attribute.isa == 'bool'
    assert field_attribute.default == True



# Generated at 2022-06-13 07:50:49.980354
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list')
    assert a.isa == 'list'

# Generated at 2022-06-13 07:50:51.943474
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute()
    FA.isa
test_FieldAttribute()



# Generated at 2022-06-13 07:50:58.448563
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=0
    )
    assert field_attribute.private is False
    assert field_attribute.default is None
    assert field_attribute.required is False
    assert field_attribute.listof is None
    assert field_attribute.priority == 0



# Generated at 2022-06-13 07:50:59.640945
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fi = FieldAttribute()



# Generated at 2022-06-13 07:51:08.974561
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', default='foo')
    assert a.isa == 'list'
    assert a.private == False
    assert a.default == 'foo'
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False
    assert a.static == False


# Generated at 2022-06-13 07:51:16.424515
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert field.isa == None
    assert field.private == False
    assert field.default == None
    assert field.required == False
    assert field.listof == None
    assert field.priority == 0
    assert field.class_type == None
    assert field.always_post_validate == False
    assert field.inherit == True
    assert field.alias == None
    assert field.extend == False
    assert field.prepend == False
    assert field.static == False

# Generated at 2022-06-13 07:51:26.552319
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        fa = FieldAttribute(isa='dict', default={})
        assert False, "Failed to raise exception for FieldAttribute with non-callable default"
    except TypeError:
        pass
    try:
        fa = FieldAttribute(isa='list', default=[])
        assert False, "Failed to raise exception for FieldAttribute with non-callable default"
    except TypeError:
        pass
    try:
        fa = FieldAttribute(isa='set', default=set())
        assert False, "Failed to raise exception for FieldAttribute with non-callable default"
    except TypeError:
        pass
    try:
        fa = FieldAttribute(isa='dict', default=lambda: {})
        assert True, "Failed to accept callable default"
    except:
        assert False, "Something else went wrong trying to create FieldAttribute"

# Generated at 2022-06-13 07:51:34.735865
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa = 'str') is not None
    assert Attribute(isa = 'str', private = True) is not None
    assert Attribute(isa = 'str', default = 'hello') is not None
    assert Attribute(isa = 'str', required = True) is not None
    assert Attribute(isa = 'str', listof = 'str') is not None
    assert Attribute(isa = 'str', priority = 3) is not None
    assert Attribute(isa = 'str', class_type = str) is not None
    assert Attribute(isa = 'str', always_post_validate = True) is not None
    assert Attribute(isa = 'str', inherit = True) is not None
    assert Attribute(isa = 'str', alias = 'myalias') is not None

# Generated at 2022-06-13 07:51:38.537522
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        Attribute(isa='list', default=['a','b'])
    except TypeError:
        print("Test passed")
    else:
        print("Test failed")

# Generated at 2022-06-13 07:51:50.769683
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa=None,
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

#class BaseAttribute(Attribute):
#    def __init__(self, *args, **kwargs):
#        super(BaseAttribute, self).__init__(*args, **kwargs)
#        self.

# TODO: make a FieldAttribute class which inherits from Attribute class
# and adds additional functionality

# default values are a bit tricky as they may be a simple value or a callable
# which returns the default value

# Generated at 2022-06-13 07:51:52.809045
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='int', default=1, inherit=False)
    assert fa.isa == 'int'
    assert fa.default == 1
    assert fa.inherit is False



# Generated at 2022-06-13 07:52:00.693700
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(isa='dict')
    assert foo.isa == 'dict'
    assert foo.private == False
    assert foo.default == None
    assert foo.required == False
    assert foo.listof == None
    assert foo.priority == 0
    assert foo.class_type == None
    assert foo.always_post_validate == False
    assert foo.inherit == True
    assert foo.alias == None

# Unit test to check constructor logic and comparison of two Attribute objects

# Generated at 2022-06-13 07:52:13.322262
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute()
    assert foo.isa == None
    assert foo.private == False
    assert foo.default == None
    assert foo.required == False
    assert foo.listof == None
    assert foo.priority == 0
    assert foo.class_type == None
    assert foo.always_post_validate == False
    assert foo.inherit == True
    assert foo.alias == None
    assert foo.extend == False
    assert foo.prepend == False
    assert foo.static == False

    foo = Attribute(isa = 'foo')
    assert foo.isa == 'foo'
    assert foo.private == False
    assert foo.default == None
    assert foo.required == False
    assert foo.listof == None
    assert foo.priority == 0
    assert foo.class_type == None
    assert foo

# Generated at 2022-06-13 07:52:23.941509
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import types

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
    assert attr.alias is None
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False


# Generated at 2022-06-13 07:52:37.649114
# Unit test for constructor of class Attribute
def test_Attribute():
    # Minimum valid
    a = Attribute(isa='int', private=False, default=None, required=False, listof=None,
                  priority=0, class_type=None, always_post_validate=False, inherit=True,
                  alias=None, extend=False, prepend=False, static=False)
    assert a is not None
    assert a.isa == 'int'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False
    assert a.static

# Generated at 2022-06-13 07:52:48.365472
# Unit test for constructor of class Attribute
def test_Attribute():
    import ansible.parsing.yaml.objects

    data = dict(
        isa='string',
        private=True,
        default='test',
        required=True,
    )
    obj = Attribute(**data)
    assert obj.isa == 'string'
    assert obj.private == True
    assert obj.default == 'test'
    assert obj.required == True
    assert obj.listof == None
    assert obj.priority == 0

    data['isa'] = 'list'
    data['listof'] = 'string'
    obj = Attribute(**data)
    assert obj.isa == 'list'
    assert obj.listof == 'string'

    data['isa'] = 'list'
    data['listof'] = 'dict'
    obj = Attribute(**data)
    assert obj.isa

# Generated at 2022-06-13 07:52:59.500604
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # default value
    test_attr = FieldAttribute()
    assert test_attr.isa is None
    assert test_attr.private is False
    assert test_attr.default is None
    assert test_attr.required is False
    assert test_attr.listof is None
    assert test_attr.priority == 0
    assert test_attr.class_type is None
    assert test_attr.always_post_validate is False
    assert test_attr.inherit is True
    assert test_attr.alias is None

    # customized value
    test_attr = FieldAttribute(isa='str', private=True, default=True,
                           required=True, listof='str', priority=1, class_type='ABC',
                           always_post_validate=True, inherit=False, alias='alias_name')
    assert test_attr

# Generated at 2022-06-13 07:53:11.651252
# Unit test for constructor of class Attribute
def test_Attribute():
    Attribute(isa='str')
    Attribute(isa='str', alias='var')
    Attribute(isa='int', alias='var')
    Attribute(isa='float', alias='var')
    Attribute(isa='list', alias='var')
    Attribute(isa='dict', alias='var')
    Attribute(isa='bool', alias='var')
    Attribute(isa='raw', alias='var')
    Attribute(isa='path', alias='var')
    Attribute(isa='template', alias='var')
    Attribute(isa='str', default='foo', alias='var')
    Attribute(isa='str', alias='var', listof='str')
    Attribute(isa='str', alias='var', listof='list')
    Attribute(isa='str', alias='var', listof='dict')
    Att

# Generated at 2022-06-13 07:53:21.786194
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', required=True, default='yaml_field')
    assert a.isa == 'str'
    assert a.required == True
    assert a.default == 'yaml_field'

    a.isa = 'dict'
    assert a.isa == 'dict'

    # set default to a mutable value, then catch the exception
    caught = False
    try:
        a.default = dict(a='b')
    except TypeError:
        caught = True
    assert caught

    # set the FieldAttribute.default to a callable value, then test if it works
    a.default = lambda: dict(a='b')
    assert a.default() == dict(a='b')


# Generated at 2022-06-13 07:53:32.924847
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert callable(attr.class_type) is False
    assert attr.always_post_validate is False

    attr = FieldAttribute(isa='string', private=True, default='foo', required=True, listof='string', class_type='string', always_post_validate=True)
    assert attr.isa == 'string'
    assert attr.private is True
    assert attr.default == 'foo'
    assert attr.required is True
    assert attr.listof == 'string'
    assert attr.priority == 0
    assert att

# Generated at 2022-06-13 07:53:36.485559
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # as a class
    assert FieldAttribute(default=[]).default == []
    assert callable(FieldAttribute(default=list).default)
    assert FieldAttribute(default=list).default() == []



# Generated at 2022-06-13 07:53:42.605339
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fieldAttribute = FieldAttribute(private=True,required=True,default=True,extend=True,listof=True,priority=0, prepend=True,inherit=True )
    assert fieldAttribute is not None
    assert fieldAttribute.private == True
    assert fieldAttribute.required == True
    assert fieldAttribute.inherit == True
    assert fieldAttribute.default == True
    assert fieldAttribute.priority == 0
    assert fieldAttribute.extend == True
    assert fieldAttribute.listof == True
    assert fieldAttribute.prepend == True


# Generated at 2022-06-13 07:53:47.742760
# Unit test for constructor of class Attribute
def test_Attribute():
    # for the following python string, no error should be raised.
    Attribute()

    # for the following python string, an error should be raised.
    # Attribute(5)

    # for the following python string, an error should be raised.
    # Attribute(1, 2, 3, 4, 5)

# Generated at 2022-06-13 07:53:55.696410
# Unit test for constructor of class Attribute
def test_Attribute():

    a1 = Attribute(isa='bool')
    assert a1.isa == 'bool'
    assert not hasattr(a1, 'default')
    assert not hasattr(a1, 'required')
    assert not hasattr(a1, 'listof')
    assert not hasattr(a1, 'priority')
    assert not hasattr(a1, 'class_type')
    assert not hasattr(a1, 'always_post_validate')
    assert a1.inherit == True
    assert not hasattr(a1, 'alias')

    a2 = Attribute(isa='bool', default='default', required=True, listof='listof',
                   class_type='class_type', inherit=False, alias='alias')
    assert a2.isa == 'bool'
    assert a2.default == 'default'


# Generated at 2022-06-13 07:54:19.994055
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import inspect
    import unittest
    import sys
    # def __init__(
    #     self,
    #     isa=None,
    #     private=False,
    #     default=None,
    #     required=False,
    #     listof=None,
    #     priority=0,
    #     cls=None,
    #     always_post_validate=False,
    #     inherit=True,
    #     alias=None,
    #     extend=False,
    #     prepend=False,
    #     static=False,
    # ):

    isa = "type"
    private = False
    default = "foo"
    required = False
    listof = None
    priority = 0
    cls = None
    always_post_validate = False
    inherit

# Generated at 2022-06-13 07:54:30.562008
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FieldAttribute(
            isa='dict',
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
    except TypeError as e:
        assert False, e
    else:
        assert True

# Generated at 2022-06-13 07:54:33.408654
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    fieldAttribute = FieldAttribute(isa='str')
    assert isinstance(fieldAttribute, FieldAttribute)
    assert isinstance(fieldAttribute, Attribute)
    assert isinstance(fieldAttribute, object)
    return True


# Generated at 2022-06-13 07:54:36.014294
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert (FieldAttribute().priority == 0)
    assert (FieldAttribute(priority=2).priority == 2)
    assert (FieldAttribute(priority=1, inherit=False).inherit == False)



# Generated at 2022-06-13 07:54:46.950413
# Unit test for constructor of class Attribute
def test_Attribute():
    # test alias
    a = Attribute(alias='test_alias')
    assert a.alias == 'test_alias'

    # test inherit
    b = Attribute(inherit=True)
    assert b.inherit == True

    # test prepend
    c = Attribute(prepend=True)
    assert c.prepend == True

    # test extend
    d = Attribute(extend=True)
    assert d.extend == True

    # test static
    e = Attribute(static=True)
    assert e.static == True

    # test listof
    f = Attribute(listof='list_test')
    assert f.listof == 'list_test'

    # test default
    g = Attribute(default='default_test')
    assert g.default == 'default_test'

   

# Generated at 2022-06-13 07:54:51.746966
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = FieldAttribute(isa='int', required=True)
    assert a1.alias is None
    assert a1.extend is False
    assert a1.prepend is False
    assert a1.static is False
    assert a1.inherit is True
    assert a1.always_post_validate is False
    assert a1.class_type is None



# Generated at 2022-06-13 07:54:56.795787
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from units.mock.loader import DummyModule
    from ansible.playbook.role.definition import RoleDefinition

    foo = DummyModule(params={'foo': 'bar'}, args=dict())

    obj = RoleDefinition.load(foo)
    assert obj.foo == 'bar'
    # default is None
    assert obj.baz is None

# Generated at 2022-06-13 07:54:57.652799
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FieldAttribute()


# Generated at 2022-06-13 07:55:07.795129
# Unit test for constructor of class Attribute
def test_Attribute():
    import unittest

    class AttributeTest(unittest.TestCase):

        def test_mutable_defaults(self):
            self.assertRaises(
                TypeError,
                Attribute,
                default={}
            )

            self.assertRaises(
                TypeError,
                Attribute,
                default=set(),
            )

            self.assertRaises(
                TypeError,
                Attribute,
                default=[]
            )

        def test_basic_equality(self):
            a = Attribute()
            b = Attribute()

            self.assertEqual(a, b)

        def test_priority_equality(self):
            a = Attribute(priority=0)
            b = Attribute()

            self.assertEqual(a, b)

# Generated at 2022-06-13 07:55:11.418479
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
        isa='bool',
        default=False,
        required=False
    )
    assert f.isa == 'bool'
    assert not f.private
    assert not f.default
    assert not f.required


# Generated at 2022-06-13 07:55:29.934387
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa is None
    assert attr.default is None


# Generated at 2022-06-13 07:55:32.665344
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(default='123')
    assert f.default == '123'



# Generated at 2022-06-13 07:55:40.334090
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    tor = FieldAttribute()
    assert tor.__dict__ == {'class_type': None, 'default': None, 'isa': None, 'listof': None, 'private': False, 'priority': 0, 'required': False, 'always_post_validate': False, 'inherit': True, 'alias': None, 'extend': False, 'prepend': False, 'static': False}


# Generated at 2022-06-13 07:55:51.142914
# Unit test for constructor of class Attribute
def test_Attribute():
    ''' attribute.py:Attribute unit test '''

    test_attr = Attribute()
    assert test_attr != None 

    try:
        test_attr = Attribute(default='oops')
        assert False
    except TypeError:
        pass

    try:
        test_attr = Attribute(default=['oops'])
        assert False
    except TypeError:
        pass

    try:
        test_attr = Attribute(default={'oops': 'oops'})
        assert False
    except TypeError:
        pass

    try:
        test_attr = Attribute(default=set())
        assert False
    except TypeError:
        pass

    test_attr = Attribute(default=1)
    assert test_attr != None 

    test_attr = Attribute(default='oops')

# Generated at 2022-06-13 07:55:56.517910
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert field.isa == None
    assert field.private == False
    assert field.default == None
    assert field.required == False
    assert field.listof == None
    assert field.priority == 0
    assert field.class_type == None
    assert field.always_post_validate == False
    assert field.inherit == True
    assert field.alias == None

# Generated at 2022-06-13 07:55:57.068538
# Unit test for constructor of class Attribute
def test_Attribute():
    pass

# Generated at 2022-06-13 07:55:58.950262
# Unit test for constructor of class Attribute
def test_Attribute():
    assert isinstance(Attribute(), Attribute)



# Generated at 2022-06-13 07:56:07.103304
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test for invalid value for default
    # default must be callable if field type is list, dict or set
    # (it is assigned using the 'default()' method)
    # Note : we don't test 'default' for field type 'str' because it is mutable
    # (we don't use it this way for field type 'str')
    for container_type in ['list', 'dict', 'set']:
        test_attr = Attribute(isa=container_type, default=set(["test"]))

# Generated at 2022-06-13 07:56:14.672236
# Unit test for constructor of class Attribute
def test_Attribute():
    test_attribute = Attribute(
        isa='foo',
        private=True,
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

    assert test_attribute.isa == 'foo'
    assert test_attribute.private == True
    assert test_attribute.default == None
    assert test_attribute.required == False
    assert test_attribute.listof == None
    assert test_attribute.priority == 0
    assert test_attribute.class_type == None
    assert test_attribute.always_post_validate == False
    assert test_attribute.inherit

# Generated at 2022-06-13 07:56:25.384204
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Ensure constructor for Attribute class works as expected
    """

    # try some allowed values for kwarg isa
    Attribute(isa = "string")
    Attribute(isa = "{'allowed_keys': ['value1']}")
    Attribute(isa = "dict")
    Attribute(isa = "int")
    Attribute(isa = "float")
    Attribute(isa = "bool")
    Attribute(isa = "list")
    Attribute(isa = "set")
    Attribute(isa = "class")
    Attribute(isa = "%")
    Attribute(isa = "")
    Attribute(isa = None)

    # try some allowed values for kwarg private
    Attribute(private = False)
    Attribute(private = True)

    # try some allowed values for kwarg default
   

# Generated at 2022-06-13 07:57:07.065754
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int', default='name', private=False, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=None, prepend=None, static=None)
    assert attr.isa == 'int'
    assert attr.default == 'name'
    assert attr.private == False
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == None
    assert attr.prepend == None
    assert attr.static

# Generated at 2022-06-13 07:57:17.365308
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None

    attr = Attribute(isa='str', private=True, default='default', required=True,
                     listof='str', priority=1, class_type='str',
                     always_post_validate=True, inherit=False, extend=True, prepend=True, alias='name')
    assert attr.isa == 'str'
    assert attr.private is True

# Generated at 2022-06-13 07:57:18.164242
# Unit test for constructor of class Attribute
def test_Attribute():
    pass


# Generated at 2022-06-13 07:57:28.457717
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert f.isa == None
    assert f.private == False
    assert f.default == None
    assert f.required == False
    assert f.listof == None
    assert f.priority == 0
    assert f.class_type == None
    assert f.always_post_validate == False
    assert f.inherit == True
    assert f.alias == None
    assert f.extend == False
    assert f.prepend == False
    assert f.static == False

# Simple function to test FieldAttribute in a list

# Generated at 2022-06-13 07:57:38.283742
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', private=True, default='str1', required=True, listof='str', priority=3, class_type=Attribute, always_post_validate=True, inherit=False, alias='str2', extend=True, prepend=True, static=True)

    assert attr.isa == 'str'
    assert attr.private == True
    assert attr.default == 'str1'
    assert attr.required == True
    assert attr.listof == 'str'
    assert attr.priority == 3
    assert attr.class_type == Attribute
    assert attr.always_post_validate == True
    assert attr.inherit == False
    assert attr.alias == 'str2'
    assert attr.extend == True
    assert attr.prepend

# Generated at 2022-06-13 07:57:44.838330
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    fields = vars(f)
    assert fields['isa'] == None
    assert fields['private'] == False
    assert fields['default'] == None
    assert fields['required'] == False
    assert fields['listof'] == None
    assert fields['priority'] == 0
    assert fields['class_type'] == None
    assert fields['always_post_validate'] == False
    assert fields['inherit'] == True
    assert fields['alias'] == None
    assert fields['extend'] == False
    assert fields['prepend'] == False
    assert fields['static'] == False



# Generated at 2022-06-13 07:57:53.110855
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='list',
        private=False,
        default=None,
        required=False,
        listof='dict',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert a.isa == 'list'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == 'dict'
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None

# Generated at 2022-06-13 07:57:59.948198
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa="string")
    assert attr.isa == "string"
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None



# Generated at 2022-06-13 07:58:10.700039
# Unit test for constructor of class Attribute
def test_Attribute():
    '''
    Attribute.__init__() accepts all of its parameters.
    '''

    # test valid combinations of parameters
    attrs = dict(
        isa='str',
        private=True,
        default='bar',
        required=True,
        listof='str',
        priority=2,
        class_type='int',
        always_post_validate=True,
        inherit=True,
        alias='x',
    )

    # each should work fine
    Attribute(**attrs)
    attrs['listof'] = None
    attrs['priority'] = None
    attrs['class_type'] = None
    Attribute(**attrs)

    # test invalid combinations of parameters, value for 'isa' not allowed
    for invalid in ('dict', 'set', 'list'):
        attrs

# Generated at 2022-06-13 07:58:12.958030
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test to make sure that the constructor of FieldAttribute does not
    # allow collections to be set as defaults
    # raises a TypeError, so the test should fail if this code is removed
    attr = FieldAttribute(default={'foo': 'bar'})
    attr.default
