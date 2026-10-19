

# Generated at 2022-06-13 07:49:06.765826
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # make sure FieldAttribute constructor works without isa, private, default and required kwargs
    test_field = FieldAttribute()
    assert test_field



# Generated at 2022-06-13 07:49:20.276212
# Unit test for constructor of class Attribute
def test_Attribute():

    class TestClassA(object):
        pass

    class TestClassB(object):
        pass

    class TestClassC(object):
        pass

    class TestClassD(object):
        pass

    class TestClassE(object):
        def __init__(self):
            pass

    test_class_a = TestClassA()
    test_class_b = TestClassB()
    test_class_c = TestClassC()
    test_class_d = TestClassD()
    test_class_e = TestClassE()

    # Call without args, defaults
    attr = Attribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0

# Generated at 2022-06-13 07:49:30.943884
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import copy

    attr = FieldAttribute(
        isa='list',
        alias='something_else',
        inherit=False,
    )
    assert attr.isa == 'list'
    assert attr.alias == 'something_else'
    assert not attr.inherit

    attr = FieldAttribute(default=10)
    assert attr.default == 10

    def test_default():
        return copy.deepcopy([])
    attr = FieldAttribute(default=test_default)
    assert callable(attr.default)
    assert attr.default() == []

    try:
        attr = FieldAttribute(default={})
        assert False, 'Should not be able to set default to a mutable container'
    except TypeError as e:
        assert True


# Generated at 2022-06-13 07:49:37.569288
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(listof='foo')
    attr2 = Attribute(listof='foo')
    assert attr == attr2
    assert attr is not attr2

    attr3 = Attribute(listof='foo', default=[])
    attr4 = Attribute(listof='foo', default=[])
    assert attr3 == attr4
    assert attr3 is not attr4

    # test implicit type conversion of class_types
    attr5 = Attribute(listof='foo', class_type=['foo'])
    assert attr5.class_type == ['foo']



# Generated at 2022-06-13 07:49:48.214111
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=False, default=None, required=False)
    assert a.isa=='str'
    assert a.private==False
    assert a.default==None
    assert a.required==False
    assert a.listof==None
    assert a.priority==0
    assert a.class_type==None
    assert a.always_post_validate==False
    assert a.inherit==True

    # Test mutable defaults are not allowed
    try:
        a = Attribute(isa='list', default={})
    except TypeError:
        a = None

    # Test that mutable defaults are allowed if they're the result of a callable

# Generated at 2022-06-13 07:49:50.028378
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute()



# Generated at 2022-06-13 07:49:50.828285
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='TestAttr')

    assert attr.isa == 'TestAttr'


# Generated at 2022-06-13 07:49:52.117384
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    foo = FieldAttribute()


# Generated at 2022-06-13 07:50:06.428809
# Unit test for constructor of class Attribute
def test_Attribute():
    #dict_a = {}
    #dict_b = {}
    #assert(dict_a == dict_b)
    #assert(dict_a is not dict_a)
    str_a = 'test'
    str_b = 'test'
    assert(str_a == str_b)
    assert(str_a is not str_b)

    attr1 = FieldAttribute(isa='test')
    attr2 = FieldAttribute(isa='test')
    attr3 = attr1
    assert(attr1 == attr2)
    assert(attr1 is not attr2)
    assert(attr1 == attr3)
    assert(attr1 is attr3)
    assert(attr1.default is None)
    assert(attr2.default is None)
    assert(attr3.default is None)



# Generated at 2022-06-13 07:50:07.348663
# Unit test for constructor of class Attribute
def test_Attribute():
  a = Attribute(isa="int")

# Generated at 2022-06-13 07:50:17.647086
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
    assert obj.isa == None
    assert obj.private == False
    assert obj.default == None
    assert obj.required == False
    assert obj.listof == None
    assert obj.priority == 0
    assert obj.class_type == None
    assert obj.always_post_validate == False
    assert obj.inherit == True
    assert obj.alias == None
    assert obj.extend == False
    assert obj.prepend == False
    assert obj.static == False
    assert str(obj) == '<FieldAttribute: default=None "None">'



# Generated at 2022-06-13 07:50:22.307322
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(None) == FieldAttribute(None)
    assert FieldAttribute(required=True) != FieldAttribute(required=False)
    assert FieldAttribute(priority=1) > FieldAttribute(priority=0)
    assert FieldAttribute(priority=0) < FieldAttribute(priority=1)
    assert FieldAttribute(priority=0) >= FieldAttribute(priority=1)
    assert FieldAttribute(priority=1) <= FieldAttribute(priority=0)



# Generated at 2022-06-13 07:50:30.420391
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa="int")
    assert fa.isa == "int"
    assert fa.private == False
    assert fa.default == None
    assert fa.required == False
    assert fa.listof == None
    assert fa.priority == 0    
    assert fa.class_type == None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias == None
    assert fa.extend == False
    assert fa.prepend == False
    assert fa.static == False


# Generated at 2022-06-13 07:50:34.662889
# Unit test for constructor of class Attribute
def test_Attribute():
    f = Attribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert f.isa == 'str'

# Generated at 2022-06-13 07:50:42.363897
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', private=True, default=None, required=True,
                  listof=None, priority=3, class_type=None, always_post_validate=True,
                  inherit=False, alias=None)
    assert a.isa == 'dict'
    assert a.private == True
    assert a.default == None
    assert a.required == True
    assert a.listof == None
    assert a.priority == 3
    assert a.class_type == None
    assert a.always_post_validate == True
    assert a.inherit == False
    assert a.alias == None



# Generated at 2022-06-13 07:50:46.872060
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.utils.vars import combine_hash
    attr = Attribute(isa='dict', default=dict())
    assert combine_hash(attr) == combine_hash({'isa': 'dict', 'default': dict()})


# Generated at 2022-06-13 07:50:50.158215
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=int, required=True)
    assert(a.isa == int)
    assert(a.required == True)
    assert(a.default == None)

# Generated at 2022-06-13 07:50:59.749178
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr is not None
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


# Generated at 2022-06-13 07:51:02.908635
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(isa='list', default=list(), required=True, inherit=True,
                          class_type=None, listof=None, always_post_validate=False, alias=None)

# Generated at 2022-06-13 07:51:11.171613
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute('int', True, 12)
    assert attr == attr
    assert attr != Attribute('int', True, 12, priority=1)

    attr = Attribute('list', False, default=[])
    assert attr.isa and attr.isa == 'list'
    assert not attr.private and attr.private is False
    assert attr.default == []

    def f():
        return []

    attr = Attribute('list', False, default=f)
    assert attr.default == f

    def g():
        return {}

    attr = Attribute('dict', False, default=g)
    assert attr.default == g

    def h():
        return set()

    attr = Attribute('set', False, default=h)
    assert attr.default == h



# Generated at 2022-06-13 07:51:22.794261
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', listof='percent', private=False, default=None, required=False, priority=0)
    assert a.isa is 'dict'
    assert a.listof is 'percent'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.priority is 0

    # test for constructor with different types of inputs
    a = Attribute(isa='class', listof='percent', private=False, default=None, required=False, priority=0, class_type=dict)
    assert a.isa is 'class'
    assert a.listof is 'percent'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.priority is 0
    assert a.class_type is dict

    a

# Generated at 2022-06-13 07:51:32.151984
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    data = {
        'isa': 'string',
        'private': True,
        'default': "test",
        'required': False,
        'listof': None,
        'priority': 0,
        'always_post_validate': False,
        'inherit': True,
        'alias': None
    }

    a = Attribute(**data)

    assert a.isa == data['isa']
    assert a.private == data['private']
    assert a.default == data['default']
    assert a.required == data['required']
    assert a.listof == data['listof']
    assert a.priority == data['priority']
    assert a.always_post_validate == data['always_post_validate']
    assert a.inherit == data['inherit']
    assert a.alias

# Generated at 2022-06-13 07:51:41.999506
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    obj = AnsibleBaseYAMLObject()
    a1 = FieldAttribute(isa='str', required=True, default='foo')
    a2 = FieldAttribute(isa='str', required=True, default='foo')
    a3 = FieldAttribute(isa='str', required=True, default='bar')
    a4 = FieldAttribute(isa='str', required=True, default='bar', priority=1)

    assert(a1 == a2)
    assert(a1 != a3)
    assert(a2 < a4)
    assert(a4 > a3)
    assert(a1 <= a2)
    assert(a4 >= a3)


# Generated at 2022-06-13 07:51:53.313689
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    attr = Attribute()
    assert attr.isa is None
    assert attr.private == False
    assert attr.default is None
    assert attr.required == False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias is None

    attr = Attribute(isa=AnsibleUnicode)
    assert attr.isa == AnsibleUnicode

    attr = Attribute(private=True)
    assert attr.private == True


# Generated at 2022-06-13 07:52:05.969251
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    #test for isa, private, default, required, listof
    a = FieldAttribute(isa='str', private=True, default='test', required=True, listof=True)
    assert a.isa == 'str'
    assert a.private == True
    assert a.default == 'test'
    assert a.required == True
    assert a.listof == True

    #test for priority, class_type, always_post_validate, inherit, alias
    b = FieldAttribute(priority=1, class_type="test", always_post_validate=False, inherit=True, alias="alias")
    assert b.priority == 1
    assert b.class_type == "test"
    assert b.always_post_validate == False
    assert b.inherit == True
    assert b.alias == "alias"

    #

# Generated at 2022-06-13 07:52:16.325832
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(
        isa='list',
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
    )

    assert attr.isa == 'list'
    assert not attr.private
    assert not attr.default
    assert not attr.required
    assert not attr.listof
    assert not attr.class_type
    assert not attr.always_post_validate
    assert attr.inherit
    assert attr.priority == 0
    assert not attr.alias


# Generated at 2022-06-13 07:52:26.094560
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    print("In test_FieldAttribute")

    # Check simple constructor
    attr = FieldAttribute(isa='int')
    assert isinstance(attr, FieldAttribute)
    assert attr.isa == 'int'
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

    # Check required constructor

# Generated at 2022-06-13 07:52:26.973984
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="str")

# Generated at 2022-06-13 07:52:31.889403
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='int')
    assert a.isa == 'int'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.alias is None

    a = Attribute(isa='int', private=True, default=1, required=True, listof=int, priority=1,
                  class_type=None, always_post_validate=True, inherit=False)
    assert a.isa == 'int'
    assert a.private is True
    assert a.default == 1
    assert a.required is True
    assert a.listof == int


# Generated at 2022-06-13 07:52:37.841308
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Successful initialization of the constructor
    fa = FieldAttribute(isa='list',
                        private=False,
                        default=None,
                        required=False,
                        listof=None,
                        priority=0,
                        class_type=None,
                        always_post_validate=False,
                        inherit=True,
                        alias=None)
    # Exception case
    fa = FieldAttribute(isa='list',
                        private=False,
                        default='True',
                        required=False,
                        listof=None,
                        priority=0,
                        class_type=None,
                        always_post_validate=False,
                        inherit=True,
                        alias=None)


# Generated at 2022-06-13 07:52:50.192910
# Unit test for constructor of class Attribute
def test_Attribute():

    attribute = Attribute(isa='dict', required=True, default=dict())
    assert(attribute.default == attribute.__init__.default)
    assert(attribute.isa == attribute.__init__.isa)
    assert(attribute.required == attribute.__init__.required)

    attribute = Attribute(isa='list', required=True, default=list())
    if callable(attribute.default):
        assert(True)
    else:
        assert(False)

    # When an attribute is required and default value is not provided,
    # the constructor should raise TypeError
    exception_raised = False
    try:
        attribute = Attribute(isa='dict', required=True)
    except TypeError as e:
        exception_raised = True
    assert(exception_raised == True)

    # Validation for the Attribute constructor
   

# Generated at 2022-06-13 07:53:01.529191
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.isa is None
    assert attr.default is None
    assert attr.private
    assert not attr.required

    attr = Attribute(isa='list')
    assert attr.isa is 'list'
    assert attr.private
    assert not attr.required

    attr = Attribute(isa=list)
    assert attr.isa is list
    assert attr.private
    assert not attr.required

    attr = Attribute(isa='list', default=[])
    assert attr.isa is 'list'
    assert attr.default == []
    assert attr.private
    assert not attr.required

    attr = Attribute(isa='list', default=set())
    assert attr.isa is 'list'

# Generated at 2022-06-13 07:53:13.436396
# Unit test for constructor of class Attribute
def test_Attribute():
    a =  Attribute('str', default='a', required=True)
    a.isa = 'str'
    a.private = False
    a.default = 'a'
    a.required = True
    a.listof = None
    a.priority = 0
    a.class_type = None
    a.always_post_validate = False
    a.inherit = True
    a.alias = None
    a.extend = False
    a.prepend = False
    a.static = False
    assert a.isa == 'str'
    assert a.private == False
    assert a.default == 'a'
    assert a.required == True
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None

# Generated at 2022-06-13 07:53:21.449224
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict')
    assert a.isa == 'dict'
    assert a.private == False
    assert a.default is None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias is None



# Generated at 2022-06-13 07:53:31.142899
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attr = FieldAttribute()
    assert field_attr
    assert field_attr.isa == None
    assert field_attr.private == False
    assert field_attr.default == None
    assert field_attr.required == False
    assert field_attr.listof == None
    assert field_attr.priority == 0
    assert field_attr.class_type == None
    assert field_attr.always_post_validate == False
    assert field_attr.inherit == True
    assert field_attr.alias == None



# Generated at 2022-06-13 07:53:40.385159
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute1 = FieldAttribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False)
    attribute2 = FieldAttribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False)

    assert attribute1
    assert attribute2
    assert attribute1 == attribute1
    assert attribute1 == attribute2
    assert attribute1 <= attribute1
    assert attribute1 <= attribute2
    assert attribute1 >= attribute1
    assert attribute1 >= attribute2
    assert attribute1 < attribute2
    assert attribute2 > attribute1

# Generated at 2022-06-13 07:53:48.583981
# Unit test for constructor of class Attribute
def test_Attribute():
    at = Attribute(isa='integer', private=False, default=1, required=False, listof=None,
        priority=0, class_type=None, always_post_validate=False, inherit=True,
        alias=None, static=False)
    assert at.isa == 'integer'

# Generated at 2022-06-13 07:53:50.300363
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa=list, private=True)
    assert isinstance(a, Attribute)



# Generated at 2022-06-13 07:53:57.121131
# Unit test for constructor of class Attribute
def test_Attribute():

    attr = Attribute(isa='foo', required=True, alias='bar')
    assert attr.isa == 'foo'
    assert attr.required is True
    assert attr.alias == 'bar'
    assert attr.default is None
    assert attr.private is False
    assert attr.priority == 0
    assert attr.inherit is True

    attr = Attribute(isa='list', listof=int, static=True)
    assert attr.isa == 'list'
    assert attr.listof == int
    assert attr.static is True

    # test bad defaults
    try:
        Attribute(isa='dict', default='foo')
        raise AssertionError('dict default did not fail')
    except TypeError:
        pass


# Generated at 2022-06-13 07:54:03.533541
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list')
    assert a.isa == 'list'
    assert isinstance(a.default, type(None))
    assert a.private == False
    assert a.required == False
    assert isinstance(a.listof, type(None))
    assert a.priority == 0
    assert isinstance(a.class_type, type(None))
    assert a.always_post_validate == False
    assert a.inherit == True
    assert isinstance(a.alias, type(None))

# Generated at 2022-06-13 07:54:18.559079
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='list',
        private=False,
        default=None,
        required=True,
        listof='str',
        priority=0,
        class_type='dict',
        always_post_validate=False,
        inherit=True,
        alias=None,
    )
    assert fa.isa == 'list'
    assert fa.private == False
    assert fa.default is None
    assert fa.required
    assert fa.listof == 'str'
    assert fa.priority == 0
    assert fa.class_type == 'dict'
    assert fa.always_post_validate == False
    assert fa.inherit
    assert fa.alias is None
    assert isinstance(fa, FieldAttribute)



# Generated at 2022-06-13 07:54:24.731707
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa1 = FieldAttribute(isa='str', private=False, default='test_default', required=False, listof=None, priority='0', class_type='str', always_post_validate=False, inherit=True, alias='test_alias', extend=False, prepend=False, static=False)
    assert fa1.isa == 'str'
    assert fa1.private == False
    assert fa1.default == 'test_default'
    assert fa1.required == False
    assert fa1.listof == None
    assert fa1.priority == '0'
    assert fa1.class_type == 'str'
    assert fa1.always_post_validate == False
    assert fa1.inherit == True
    assert fa1.alias == 'test_alias'
    assert fa1.extend == False

# Generated at 2022-06-13 07:54:34.496648
# Unit test for constructor of class Attribute
def test_Attribute():

    attr_test = Attribute(
        isa='dict',
        private=False,
        default={},
        required=False,
        listof='str',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=None,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    assert attr_test.isa == 'dict'
    assert attr_test.private == False
    assert attr_test.default == {}
    assert attr_test.required == False
    assert attr_test.listof == 'str'
    assert attr_test.priority == 0
    assert attr_test.class_type == None
    assert attr_test.always_post_validate == False

# Generated at 2022-06-13 07:54:37.708782
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        field_attribute = FieldAttribute(listof="string", default="foo")
        assert(field_attribute.default() == "foo")
    except TypeError:
        assert(False)


# Generated at 2022-06-13 07:54:44.863370
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert field.isa is None
    assert field.private is False
    assert field.default is None
    assert field.required is False
    assert field.listof is None
    assert field.priority == 0
    assert field.class_type is None
    assert field.always_post_validate is False
    assert field.inherit is True
    assert field.alias is None
    assert field.extend is False
    assert field.prepend is False
    assert field.static is False



# Generated at 2022-06-13 07:54:51.810688
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    isa = None
    private = False
    default = None
    required = False
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False
    inherit = True
    alias = None
    extend = False
    prepend = False
    static = False
    FieldAttribute(isa, private, default, required, listof, priority, class_type,
                    always_post_validate, inherit, alias, extend, prepend, static)



# Generated at 2022-06-13 07:54:58.742923
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list', default=[])
    assert attr.isa == 'list'
    assert attr.default == []
    try:
        attr = FieldAttribute(isa='dict', default={})
        assert False, "Should have failed"
    except TypeError:
        pass
    attr = FieldAttribute(isa='dict', default=lambda: {})
    attr = FieldAttribute(isa='dict', default=lambda: {}, private=True)
    assert attr.private is True
    assert attr.default() == ({})



# Generated at 2022-06-13 07:55:08.848660
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute()
    assert x.isa is None
    assert x.private is False
    assert x.default is None
    assert x.required is False
    assert x.listof is None
    assert x.priority == 0
    assert x.class_type is None
    assert x.always_post_validate is False
    assert x.inherit is True
    assert x.alias is None
    assert x.extend is False
    assert x.prepend is False
    assert x.static is False


# Generated at 2022-06-13 07:55:17.624779
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
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False
    attr = FieldAttribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type

# Generated at 2022-06-13 07:55:19.539097
# Unit test for constructor of class Attribute
def test_Attribute():
    # Attribute constructor works without optional arguments
    Attribute(isa='string')
    # Attribute constructor works with optional arguments
    Attribute(isa='list', default='test', required=True)
