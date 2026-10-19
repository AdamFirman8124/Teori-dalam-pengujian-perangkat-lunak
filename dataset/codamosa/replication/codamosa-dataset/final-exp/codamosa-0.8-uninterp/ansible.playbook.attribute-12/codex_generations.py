

# Generated at 2022-06-13 07:48:59.797959
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute=FieldAttribute()
    assert attribute is not None


# Generated at 2022-06-13 07:49:11.180760
# Unit test for constructor of class Attribute
def test_Attribute():
    # Constructor call without arguments
    obj = Attribute()
    assert obj.isa is None
    assert obj.default is None
    assert obj.required == False
    assert obj.listof is None
    assert obj.priority == 0
    assert obj.class_type is None
    assert obj.always_post_validate == False
    assert obj.inherit == True
    assert obj.alias is None
    assert obj.extend == False
    assert obj.prepend == False
    assert obj.static == False

    # Constructor call with arguments
    obj = Attribute("example", False, "default", True, "listof", 2, "class_type", True, False, "alias", True, False, True)
    assert obj.isa == "example"
    assert obj.default == "default"
    assert obj.required == True


# Generated at 2022-06-13 07:49:14.208697
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = FieldAttribute()
    assert isinstance(a1, FieldAttribute)
    assert isinstance(a1, Attribute)
    # assert a1.isa == None


# Generated at 2022-06-13 07:49:19.917700
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute().default is None
    assert Attribute().inherit is True
    assert Attribute(default=5).default == 5
    assert Attribute(inherit=False).inherit is False
    assert Attribute().priority == 0
    assert Attribute(priority=1).priority == 1
    assert Attribute(required=False).required is False
    assert Attribute(required=True).required is True


# Generated at 2022-06-13 07:49:30.696171
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute ()
    a1.isa = 'test'
    assert a1.isa == 'test'
    assert a1.private == False
    assert a1.default == None
    assert a1.required == False
    assert a1.listof == None
    assert a1.priority == 0
    assert a1.class_type == None
    assert a1.always_post_validate == False
    assert a1.inherit == True
    assert a1.alias == None

    a2 = Attribute (isa="test", private=True, default=1, required=True, listof="list",
        priority=1, class_type="class", always_post_validate=True, inherit=False, alias="test1")
    assert a2.isa == "test"
    assert a2.private == True


# Generated at 2022-06-13 07:49:35.425986
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import pytest
    def test_constructor():
        a = FieldAttribute(isa='raw', listof='str')
        assert a.isa == 'raw'
        assert a.listof == 'str'
    test_constructor()
    def test_constructor_mutable_default():
        with pytest.raises(TypeError):
            FieldAttribute(isa='raw', listof='str', default={})
    test_constructor_mutable_default()

# Generated at 2022-06-13 07:49:36.236159
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()



# Generated at 2022-06-13 07:49:39.480135
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        attribute_object = FieldAttribute(isa='int', default=[2, 3])
    except TypeError:
        print("FieldAttribute cannot have a mutable 'default'")
        assert True
    else:
        print("FieldAttribute has a valid 'default' value")
        assert False



# Generated at 2022-06-13 07:49:46.390153
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        a=Attribute()
    except:
        print('Attribute initialized with no arguments')
    try:
        a=Attribute(isa='list', default=None, required=False, inherit=True)
    except:
        print('Attribute initialized with some arguments')
    try:
        a=Attribute(isa='list', default=dict(), required=False, inherit=True)
        print('Attribute initialized with mutable default')
    except:
        print('Attribute initialized with mutable default, exception detected')

test_Attribute()

# Generated at 2022-06-13 07:49:49.237063
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='list') == Attribute(isa='list')
    assert Attribute(isa='list') != Attribute(isa='str')
    assert Attribute(isa='list') < Attribute(isa='str')
    assert Attribute(isa='list') <= Attribute(isa='str')
    assert Attribute(isa='str') > Attribute(isa='list')
    assert Attribute(isa='str') >= Attribute(isa='list')

# Generated at 2022-06-13 07:49:58.363700
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = {
        'isa': 'dict',
        'private': False,
        'default': None,
        'required': False,
        'listof': None,
        'priority': 0,
        'class_type': None,
        'always_post_validate': False,
        'inherit': True,
        'alias': None,
        'extend': False,
        'prepend': False,
        'static': False,
    }


# Generated at 2022-06-13 07:50:06.368563
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(
        isa='str',
        private=True,
        default=None,
        required=False,
        listof='str',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    print("Your test passed!")
    return attribute


# Generated at 2022-06-13 07:50:07.303266
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute()



# Generated at 2022-06-13 07:50:12.299484
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(isa=list)
    assert attribute.isa == list
    attribute = Attribute(isa=list, required=True)
    assert attribute.isa == list
    assert attribute.required
    attribute = Attribute(isa=list, required=False)
    assert attribute.isa == list
    assert not attribute.required

# Generated at 2022-06-13 07:50:17.165504
# Unit test for constructor of class Attribute
def test_Attribute():
    class AttributeTest(Attribute):
        pass
    # normal constructor
    try:
        a = AttributeTest(
            isa='str',
            private=False,
            default=None,
            required=False,
            listof='str',
            priority=0,
            class_type=None,
            always_post_validate=False,
            inherit=True,
            alias=None,
            extend=False,
            prepend=False,
            static=False,
        )
    except Exception as e:
        raise e

    # constructor with wrong 'isa' and 'listof' type

# Generated at 2022-06-13 07:50:26.979203
# Unit test for constructor of class Attribute
def test_Attribute():
    # Default values
    class TestAttribute:
        _test_attr = Attribute()
    test_object = TestAttribute()
    assert test_object._test_attr.isa == None
    assert test_object._test_attr.private == False
    assert test_object._test_attr.default == None
    assert test_object._test_attr.required == False
    assert test_object._test_attr.listof == None
    assert test_object._test_attr.priority == 0
    assert test_object._test_attr.class_type == None
    assert test_object._test_attr.always_post_validate == False
    assert test_object._test_attr.inherit == True


# Generated at 2022-06-13 07:50:34.404958
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = Attribute(isa='int', private=False, default=1, required=False, priority=0)
    assert not a.private, "FieldAttribute a's private should be False"
    assert a.isa == 'int', "FieldAttribute a's isa should be 'int'"
    assert a.default == 1, "FieldAttribute a's default should be 1"
    assert not a.required, "FieldAttribute a's required should be False"
    assert a.priority == 0, "FieldAttribute a's priority should be 0"



# Generated at 2022-06-13 07:50:41.624840
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
    assert attr.alias is None
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False



# Generated at 2022-06-13 07:50:54.589866
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # All valid
    assert FieldAttribute(isa='list').isa == 'list'
    assert FieldAttribute(isa='dict').isa == 'dict'
    assert FieldAttribute(isa='set').isa == 'set'
    assert FieldAttribute(isa='str').isa == 'str'
    assert FieldAttribute(isa='bool').isa == 'bool'
    assert FieldAttribute(isa='int').isa == 'int'
    assert FieldAttribute(isa='float').isa == 'float'
    assert FieldAttribute(isa='complex').isa == 'complex'
    assert FieldAttribute(isa='listof').isa == 'listof'
    assert FieldAttribute(isa='class').isa == 'class'

    # Invalid isa
    try:
        FieldAttribute(isa='foobar')
        assert False, 'should have raised an exception'
    except TypeError:
        pass

   

# Generated at 2022-06-13 07:50:56.683823
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='foo')
    assert field.isa == 'foo'


# Generated at 2022-06-13 07:51:01.483279
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='dict', private=False, default=dict()) == Attribute(isa='dict', private=False, default=dict())


# Generated at 2022-06-13 07:51:07.713331
# Unit test for constructor of class Attribute
def test_Attribute():
    field = Attribute(isa='bool')
    assert field.isa == 'bool'
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


# Generated at 2022-06-13 07:51:13.529852
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute()

    assert FA.isa is None
    assert FA.private is False
    assert FA.required is False
    assert FA.listof is None
    assert FA.priority is 0
    assert FA.class_type is None
    assert FA.always_post_validate is False
    assert FA.inherit is True
    assert FA.alias is None
    assert FA.extend is False
    assert FA.prepend is False
    assert FA.static is False


Attribute = FieldAttribute



# Generated at 2022-06-13 07:51:22.283781
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='test', default='test_default', required=True, listof=True, priority=0, class_type=True, always_post_validate=False, inherit=True, alias='alias')
    assert attr.isa == 'test'
    assert attr.private == False
    assert attr.default == 'test_default'
    assert attr.required == True
    assert attr.listof == True
    assert attr.priority == 0
    assert attr.class_type == True
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == 'alias'

# Generated at 2022-06-13 07:51:28.475087
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='string', default='value')
    assert field.isa == 'string'
    assert field.default == 'value'
    assert field.private is False
    assert field.required is False
    assert field.listof is None
    assert field.priority == 0
    assert field.class_type is None
    assert field.inherit is True
    assert field.alias is None
    assert field.extend is False
    assert field.prepend is False



# Generated at 2022-06-13 07:51:34.324374
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(default=True, isa='bool', extend=False)
    assert a.static == False
    assert a.default == True
    assert a.isa == 'bool'
    assert a.inherit == True
    assert a.extend == False
    assert a.prepend == False
    assert not a.private
    assert not a.required
    assert not a.always_post_validate



# Generated at 2022-06-13 07:51:40.135269
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert field.isa is None
    assert field.private == False
    assert field.default is None
    assert field.required == False
    assert field.priority == 0
    assert field.inherit is True
    assert field.alias is None
    assert field.extend == False
    assert field.prepend == False

# Generated at 2022-06-13 07:51:51.953892
# Unit test for constructor of class Attribute
def test_Attribute():

    # Attributes data to be used as arguments
    # Use all attributes with different types
    __dict_attr1 = {'isa': 'dict', 'private': False, 'default': None,
                    'required': False, 'listof': 'string', 'priority': 2,
                    'class_type': 'dict', 'always_post_validate': False,
                    'inherit': True, 'alias': 'dict1', 'extend': False,
                    'prepend': False, 'static': False}


# Generated at 2022-06-13 07:51:56.501412
# Unit test for constructor of class Attribute
def test_Attribute():
    class Attr(object):
        a = Attribute(default='foo')

    o = Attr()
    print(o.a)
    assert o.a == 'foo'
    o = Attr(a='bar')
    print(o.a)
    assert o.a == 'bar'
    o.a = 'baz'
    print(o.a)
    assert o.a == 'baz'


# Generated at 2022-06-13 07:52:09.249900
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()
    assert f1.isa is None

    f2 = FieldAttribute(isa='boolean')
    assert f2.isa == 'boolean'

    f3 = FieldAttribute(isa='boolean', default=True)
    assert f3.isa == 'boolean'
    assert f3.default == True

    f4 = FieldAttribute(isa='boolean', private=True, default=True)
    assert f4.isa == 'boolean'
    assert f4.private == True
    assert f4.default == True

    f5 = FieldAttribute(isa='boolean', private=True, default=True, extend=True)
    assert f5.isa == 'boolean'
    assert f5.private == True
    assert f5.default == True
    assert f5.extend == True

    f6

# Generated at 2022-06-13 07:52:24.022134
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test with no defaults
    fa = FieldAttribute()
    assert fa.isa is None
    assert not fa.private
    assert fa.default is None
    assert not fa.required
    assert fa.listof is None
    assert fa.priority == 0
    assert fa.class_type is None
    assert not fa.always_post_validate
    assert fa.inherit
    assert fa.alias is None
    assert not fa.extend
    assert not fa.prepend
    assert not fa.static

    # Test with all defaults

# Generated at 2022-06-13 07:52:25.863362
# Unit test for constructor of class Attribute
def test_Attribute():
    # assert instantiation with un-callable mutable default works
    Attribute(default=[])



# Generated at 2022-06-13 07:52:27.423765
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute(isa='str')
    assert obj.isa == 'str'


# Helper converters

# Generated at 2022-06-13 07:52:35.487093
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.utils.typecheck import InvalidAttributeException
    try:
        Attribute(default=list())
        assert False, "default must be a callable"
    except TypeError:
        assert True, "default must not be callable"
    except:
        assert False, "default must be a callable"

    testInitialized = Attribute(isa='asdf', default=None, required=True)
    assert testInitialized.isa == 'asdf'
    assert testInitialized.default == None
    assert testInitialized.required == True

    try:
        testInitialized1 = Attribute(isa='asdf', default=None, required=True, listof='foo')
        assert False, "listof and isa both can't be specified"
    except InvalidAttributeException:
        assert True, "listof and isa both can't be specified"


# Generated at 2022-06-13 07:52:38.389350
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
   """Test case for FieldAttribute constructor."""
   attrs = FieldAttribute(isa='list',listof='str')
   assert isinstance(attrs, FieldAttribute)
   assert isinstance(attrs, list)
   assert attrs.isa == 'list'
   assert attrs.listof == 'str'

# Generated at 2022-06-13 07:52:49.197357
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()

    assert(attr.isa is None)
    assert(attr.private == False)
    assert(attr.default is None)
    assert(attr.required == False)
    assert(attr.listof is None)
    assert(attr.priority == 0)
    assert(attr.class_type is None)
    assert(attr.always_post_validate == False)
    assert(attr.inherit == True)
    assert(attr.alias is None)
    assert(attr.extend == False)
    assert(attr.prepend == False)
    assert(attr.static == False)


# Generated at 2022-06-13 07:53:00.482814
# Unit test for constructor of class Attribute
def test_Attribute():

    # TODO: private field is not tested
    # TODO: default value is not tested
    # TODO: required field is not tested
    # TODO: listof field is not tested
    # TODO: priority field is not tested
    # TODO: class_type field is not tested
    # TODO: always_post_validate field is not tested
    # TODO: inherit field is not tested

    # all valid isa arguments of the constructor
    # TODO: add more valid isa arguments
    isa_valid_list = ['dict', 'list', 'set', 'bool', 'int', 'float', 'string']

    # TODO: add a class to check if the isa is a class, too
    # TODO: add a syntax check for percent isa

    # assert with the constructor with all valid isa arguments

# Generated at 2022-06-13 07:53:09.291031
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Verify the constructor of class FieldAttribute
    assert FieldAttribute.__init__
    fa1=FieldAttribute()
    fa2=FieldAttribute()
    assert fa1.priority == 0
    assert fa2.priority == 0
    assert fa1 == fa2
    assert fa1.__eq__(fa2)
    assert fa1 != fa1
    assert fa1.__ne__(fa1)
    assert not fa1 == None
    assert not fa1.__eq__(None)
    assert fa1 != len
    assert fa1.__ne__(len)
    
    

# Generated at 2022-06-13 07:53:15.973856
# Unit test for constructor of class Attribute
def test_Attribute():
    # default, no error
    a1 = Attribute()
    print("Class Attribute, default, no error:", a1)
    # explicit, no error
    a2 = Attribute("class", False, None, False, "str", 1, None, True)
    print("Class Attribute, explicit, no error:", a2)
    # default, with error
    try:
        a3 = Attribute(default='test')
    except TypeError:
        print("Class Attribute, default, with TypeError:", a3)



# Generated at 2022-06-13 07:53:23.156533
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', default=None, required=False)
    assert a.isa == 'list'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    a = Attribute(isa='foo', default=None, required=False,static=True)
    assert a.isa == 'foo'
    assert a.private == False
    assert a.default == None
    assert a.required == False

# Generated at 2022-06-13 07:53:33.906721
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='list')
    assert field.isa == 'list'

# Generated at 2022-06-13 07:53:37.884287
# Unit test for constructor of class Attribute
def test_Attribute():
    err = None
    try:
        Attribute(isa='list', default=['foo', 'bar'])
    except TypeError as e:
        err = e
    assert str(err) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'

# Generated at 2022-06-13 07:53:49.335943
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # initialize an attribute object
    a = FieldAttribute()

    # test getters and setters
    # a.private = True
    # assert(a.private == True)
    # a.default = 'something'
    # assert(a.default == 'something')
    # a.required = False
    # assert(a.required == False)
    # a.listof = None
    # assert(a.listof == None)
    # a.priority = 2
    # assert(a.priority == 2)
    # a.class_type = 'class'
    # assert(a.class_type == 'class')
    # a.always_post_validate = False
    # assert(a.always_post_validate == False)
    # a.inherit = True
    # assert(a.inherit == True

# Generated at 2022-06-13 07:53:54.897772
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='dict')
    assert attr.isa == 'dict'
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


# Generated at 2022-06-13 07:53:59.583199
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="dict", default=dict(), always_post_validate=True)
    b = Attribute(isa="dict", default=dict(), always_post_validate=True)

    assert a == b
    assert not a != b

    a.default['test'] = 1
    a.default['test'] = 2

    assert a != b
    assert not a == b

    attr = Attribute(isa="list", default=lambda: list(), listof="dict")

    assert isinstance(attr.default(), list)
    assert isinstance(attr.default()[0], dict)



# Generated at 2022-06-13 07:54:03.374112
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='str')
    assert field.isa == 'str'
    assert field.private == False
    assert field.default is None
    assert field.required == False
    assert field.listof is None
    assert field.priority == 0
    assert field.class_type is None
    assert field.always_post_validate == False
    assert field.inherit == True
    assert field.alias is None
    assert field.extend == False
    assert field.prepend == False
    assert field.static == False

# Generated at 2022-06-13 07:54:15.531051
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import sys

    class Test(AnsibleBaseYAMLObject):
        yaml_tag = u'!Test'
        yaml_loader = AnsibleBaseYAMLObject.yaml_loader
        yaml_dumper = AnsibleBaseYAMLObject.yaml_dumper

        def __init__(self, a=None):
            super(Test, self).__init__()
            self.a = a

    # test default
    f1 = FieldAttribute(
        isa='str',
        default='f1'
    )

    test = Test()
    assert test.a == 'f1'

    # test valid attr

# Generated at 2022-06-13 07:54:17.205294
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert not attr is None


# Generated at 2022-06-13 07:54:21.395005
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='string')
    assert a.isa == 'string'
    a = FieldAttribute(isa='string', private=False, default='abc', required=False, listof=None,\
                       priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert a.default == 'abc'


# Generated at 2022-06-13 07:54:31.972499
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.playbook.base import Base
    from ansible.playbook.attribute import Attribute
    import ansible.playbook.role
    import ansible.playbook.block

    foo = FieldAttribute()
    assert foo is not None
    assert isinstance(foo, Attribute)

    foo = FieldAttribute(
        inherit=False,
        default="something"
    )
    assert foo is not None
    assert foo.inherit == False
    assert foo.default == "something"

    foo = FieldAttribute(
        inherit=True,
        default="something",
        always_post_validate=True,
        class_type=ansible.playbook.role.Role
    )
    assert foo is not None
    assert foo.inherit == True
    assert foo.default == "something"
    assert foo.always

# Generated at 2022-06-13 07:54:57.731180
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()
    assert fa.isa == None
    assert fa.private == False
    assert fa.default == None
    assert fa.required == False
    assert fa.listof == None
    assert fa.priority == 0
    assert fa.class_type == None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias == None

    fa = FieldAttribute(isa='bool', private=True, default=True, required=True, listof='bool',
                    priority=10, class_type=bool, always_post_validate=True, inherit=False, alias='afield')
    assert fa.isa == 'bool'
    assert fa.private == True
    assert fa.default == True
    assert fa.required == True
    assert fa.listof == 'bool'

# Generated at 2022-06-13 07:55:07.839037
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.task import Task

    # default constructor
    a = FieldAttribute()

    # construct a FieldAttribute with all possible options/arguments
    b = FieldAttribute(
        isa='str',
        private=True,
        default=True,
        required=False,
        listof='dict',
        priority=0,
        class_type=Task,
        always_post_validate=True,
        inherit=False,
        alias='a_string',
        extend=True,
        prepend=True,
        static=True,
    )

    assert a.isa == None
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a

# Generated at 2022-06-13 07:55:13.131863
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='int', default=5)
    a1 = Attribute(isa='list')
    try:
        a2 = Attribute(isa='list', default=list())
        fail("'Attribute' constructor failed")
    except TypeError as e:
        if str(e) != 'defaults for FieldAttribute may not be mutable, please provide a callable instead':
            fail("'Attribute' constructor failed")

# Generated at 2022-06-13 07:55:17.040627
# Unit test for constructor of class Attribute
def test_Attribute():
    attr1 = Attribute(isa='list')
    attr2 = Attribute(isa='list', default=lambda: [])
    attr3 = Attribute(isa='list', default=[])
    try:
        attr4 = Attribute(isa='list', default={})
    except:
        pass
    else:
        raise Exception('expected error')


# Generated at 2022-06-13 07:55:29.082785
# Unit test for constructor of class Attribute

# Generated at 2022-06-13 07:55:36.523169
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_kwargs = dict(
        isa=type(None),
        private=False,
        default=None,
        required=False,
        listof=(type(None), 'list'),
        priority=5,
        class_type=type(None),
        always_post_validate=False,
        inherit=True,
        alias='alias',
        extend=True,
        prepend=True,
    )
    assert FieldAttribute(**test_kwargs)



# Generated at 2022-06-13 07:55:44.852531
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list')
    assert a.isa == 'list'
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
    assert a.static == False


# Generated at 2022-06-13 07:55:56.057823
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:56:02.577238
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list', default=[]);
    assert attr.isa == 'list'
    assert attr.default == []
    assert attr.priority == 0
    assert attr.private == False
    assert attr.required == False
    assert attr.listof == None
    assert attr.class_type == None
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False


# Generated at 2022-06-13 07:56:14.363968
# Unit test for constructor of class Attribute
def test_Attribute():

    # improper instantiation of Attribute object
    try:
        Attribute()
    except TypeError:
        pass
    else:
        raise AssertionError('Attribute constructor should throw TypeError with no args')

    # proper instantiation of Attribute object
    a = Attribute(
        isa='string',
        private=False,
        default='foobar',
        listof='foobar',
        required=True,
        priority=10,
        class_type='foobar',
        always_post_validate=False,
        inherit=False,
        alias='foobar',
        extend=False,
        prepend=True,
    )

    # assert that all of the Attribute members are of the correct type

# Generated at 2022-06-13 07:57:01.827569
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(
        isa='class',
        default=None,
        required=False,
        priority=1,
    )
    assert isinstance(field, FieldAttribute)


# TODO: add a testcase to test the error case of FieldAttribute not handling mutable defaults


# Generated at 2022-06-13 07:57:13.451861
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play_context.remote_addr = '127.0.0.1'
    class TestYAMLObject(AnsibleBaseYAMLObject):
        _test = FieldAttribute(isa='string')

    play_context.network_os = 'test'
    test_object = TestYAMLObject.load(dict(test='test'), play_context)
    assert type(test_object._test) is AnsibleUnsafeText
    assert test_object._test == 'test'


# Generated at 2022-06-13 07:57:19.715371
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Basic test of constructor
    fa = FieldAttribute(isa='string')
    assert fa.isa == 'string', "Isa not correct"
    assert fa.private == False, "Private not correct"
    assert fa.default == None, "Default should be None"
    assert fa.required == False, "Required not correct"
    assert fa.listof == None, "Listof should be None"
    assert fa.priority == 0, "Priority not correct"
    assert fa.class_type == None, "Class type should be None"
    assert fa.always_post_validate == False, "Always post validate not correct"
    assert fa.inherit == True, "Inherit not correct"
    assert fa.alias == None, "Alias should be None"

# Generated at 2022-06-13 07:57:33.609062
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'test_isa'
    private = True
    default = 'test_default'
    required = True
    listof = 'test_listof'
    priority = 'test_priority'
    class_type = 'test_class_type'
    always_post_validate = True
    inherit = False
    alias = 'test_alias'
    extend = True
    prepend = True

    attribute = Attribute(isa, private, default, required, listof, priority, class_type, always_post_validate, inherit, alias, extend, prepend)

    assert attribute.isa == isa
    assert attribute.private == private
    assert attribute.default == default
    assert attribute.required == required
    assert attribute.listof == listof
    assert attribute.priority == priority
    assert attribute.class_type == class_type

# Generated at 2022-06-13 07:57:43.924314
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='boolean',
            private=False,
            default='False',
            required=False,
            listof='string',
            priority=0,
            class_type='string',
            always_post_validate=False,
            inherit=True,
            alias='alias',
            extend=False,
            prepend=False)
    attr_copy = deepcopy(attr)
    assert attr == attr_copy
    assert not attr != attr_copy
    attr_copy.priority = 1
    assert attr != attr_copy
    assert attr < attr_copy
    assert attr_copy > attr
    assert attr <= attr_copy
    assert attr_copy >= attr
    assert attr_copy.priority == 1


# Generated at 2022-06-13 07:57:51.035156
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert(f.isa is None)
    assert(f.private == False)
    assert(f.default is None)
    assert(f.required == False)
    assert(f.listof is None)
    assert(f.priority == 0)
    assert(f.class_type is None)
    assert(f.always_post_validate == False)
    assert(f.inherit == True)
    assert(f.alias is None)
    assert(f.extend == False)
    assert(f.prepend == False)
    assert(f.static == False)



# Generated at 2022-06-13 07:57:52.091500
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='int')
    assert f.isa == 'int'

# Generated at 2022-06-13 07:57:57.646464
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
        isa         = bool,
        private     = False,
        default     = True,
        required    = False,
        listof      = None,
        priority    = 0,
        class_type  = None,
        always_post_validate = False,
        inherit     = True,
        alias       = None,
        extend      = False,
        prepend     = False,
        static      = False,
    )
    assert field_attribute.isa is bool
    assert field_attribute.private is False
    assert field_attribute.default is True
    assert field_attribute.required is False
    assert field_attribute.listof is None
    assert field_attribute.priority is 0
    assert field_attribute.class_type is None
    assert field_attribute.always_post_validate is False

# Generated at 2022-06-13 07:58:09.065996
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
        isa = 'int'
        private = False
        default = None
        required = True
        listof = 'list'
        priority = 0
        class_type = 'dict'
        always_post_validate = True
        inherit = True
        alias = 'ali'
        extend = False
        prepend = True
        static = True
        a = FieldAttribute(isa, private, default, required, listof, priority, class_type, always_post_validate,
                           inherit, alias, extend, prepend, static)
        assert a.isa == isa
        assert a.private == private
        assert a.default == default
        assert a.required == required
        assert a.listof == listof
        assert a.priority == priority
        assert a.class_type == class_type
        assert a.always_post_

# Generated at 2022-06-13 07:58:18.252516
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # class FieldAttribute(Attribute):
    attribute = FieldAttribute(
        isa='str',
        private=False,
        default='',
        required=False,
        listof=None,
        # priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    assert attribute.isa == 'str'
    assert attribute.private == False
    assert attribute.default == ''
    assert attribute.required == False
    assert attribute.listof is None
    # assert attribute.priority == 0
    assert attribute.class_type is None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias is None