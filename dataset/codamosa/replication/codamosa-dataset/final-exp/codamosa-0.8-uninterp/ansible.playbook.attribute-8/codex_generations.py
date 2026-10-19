

# Generated at 2022-06-13 07:49:13.122124
# Unit test for constructor of class Attribute
def test_Attribute():
    test_case1 = Attribute(listof="str", default=[1,2,3])
    assert test_case1.listof == "str"
    assert test_case1.default == [1,2,3]

    test_case2 = Attribute(listof="str", default=lambda: [1,2,3])
    assert test_case2.listof == "str"
    assert test_case2.default() == [1,2,3]


# Generated at 2022-06-13 07:49:22.648055
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        isa='str',
        private=True,
        default='abc',
        required=True,
        listof='str',
        priority=10,
        class_type='str',
        always_post_validate=True,
        inherit=False,
        alias='alias_attr',
        extend=True,
        prepend=True,
        static=True,
    )

# Generated at 2022-06-13 07:49:32.876480
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute()
    assert FA.__dict__ == {'isa': None,
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
                           'static': False}


# Generated at 2022-06-13 07:49:34.678807
# Unit test for constructor of class Attribute
def test_Attribute():
    import pytest
    with pytest.raises(TypeError):
        Attribute(default=dict())
        Attribute(default=list())

# Generated at 2022-06-13 07:49:41.953346
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(always_post_validate=True, class_type=list, isa="list")
    assert a.isa == "list"
    assert a.class_type == list
    assert a.always_post_validate == True
    a = Attribute(always_post_validate=True, isa="list")
    assert a.isa == "list"
    assert a.class_type == None
    assert a.always_post_validate == True
    a = Attribute(always_post_validate=True, class_type=list)
    assert a.isa == None
    assert a.class_type == list
    assert a.always_post_validate == True
    a = Attribute()
    assert a.isa == None
    assert a.class_type == None

# Generated at 2022-06-13 07:49:47.741860
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.module_utils.six import assertRaisesRegex
    from ansible.utils.boolean import boolean
    from ansible.parsing.yaml.objects import AnsibleUnicode

    attr = dict(
        isa=AnsibleUnicode,
        private=boolean(False),
        default='default value',
        required=boolean(False),
        listof=[],
        priority=1,
        class_type=None,
        always_post_validate=boolean(False),
        inherit=boolean(True),
        alias='test'
    )

    attr2 = Attribute(**attr)
    assert attr2.isa is AnsibleUnicode
    assert attr2.private is False
    assert attr2.default == 'default value'
    assert attr2

# Generated at 2022-06-13 07:49:57.493092
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    class test_class(object):
        foo = FieldAttribute(isa='str', required=True)
        bar = FieldAttribute(isa='list', default=lambda: [])
        baz = FieldAttribute(isa='bool', default=True)
        qux = FieldAttribute(isa='dict', default=lambda: {})
        quux = FieldAttribute(isa='bool', default=False)
        quuz = FieldAttribute(isa='list', default=[])
        corge = FieldAttribute(isa='dict', default={})
        grault = FieldAttribute(isa='list', required=True)
        garply = FieldAttribute(isa='bool', default=False)

    tc = test_class()
    tc.foo = 'abc'
    assert tc.bar == []
    assert tc.baz == True
    assert tc.qux == {}
    assert tc

# Generated at 2022-06-13 07:50:06.984726
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='dict', default={}, required=False)
    assert f.isa == 'dict'
    assert f.private == False
    assert f.default == {}
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


# Generated at 2022-06-13 07:50:18.250871
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Make sure that all fields are initialized properly and that exceptions are raised when wrong values are passed in.
    """
    # Test the initializer of Attribute
    a = Attribute(
        isa='dict',
        private=True,
        default='',
        required=True,
        listof='list',
        priority=0,
        class_type=list,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert a.isa == 'dict'
    assert a.private == True
    assert a.default == ''
    assert a.required == True
    assert a.listof == 'list'
    assert a.priority == 0
    assert a.class_type == list
   

# Generated at 2022-06-13 07:50:25.163418
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
    field = FieldAttribute(
        isa='dict',
        private=True,
        default=dict,
        required=True,
        listof='list',
        priority=1,
        class_type=dict,
        always_post_validate=True,
        inherit=False,
        alias='a_dict',
    )

    assert field.isa == 'dict'
    assert field.private is True
    assert field

# Generated at 2022-06-13 07:50:37.951171
# Unit test for constructor of class Attribute
def test_Attribute():
    f1 = Attribute(isa=str, private=False, default=None, required=False, listof=None, priority=0,
                   class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False)
    f2 = Attribute(isa=str, private=False, default=None, required=False, listof=None, priority=0,
                   class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False)

# Generated at 2022-06-13 07:50:48.967250
# Unit test for constructor of class Attribute
def test_Attribute():
    class Test(object):
        test1 = FieldAttribute(isa='test', priority=1)
        test2 = FieldAttribute(isa='test', priority=2)
        test3 = FieldAttribute(isa='test', priority=3)
    assert Test.test1 < Test.test2
    assert Test.test2 < Test.test3
    assert Test.test1 < Test.test3
    attr_list = [ Test.test1, Test.test2, Test.test3 ]
    attr_list.sort()
    assert attr_list[0] == Test.test3
    assert attr_list[1] == Test.test2
    assert attr_list[2] == Test.test1


# Generated at 2022-06-13 07:51:01.392357
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list')
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


# Generated at 2022-06-13 07:51:03.193974
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # make sure we can construct it without any parameters, without raising an error
    foo = FieldAttribute()


# Generated at 2022-06-13 07:51:06.634241
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert a.isa == None
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



# Generated at 2022-06-13 07:51:15.227956
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # normal case
    FieldAttribute(
        isa='integer',
        private=True,
        default=None,
        required=True,
        listof='integers',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    # default is mutable (this is not allowed)
    try:
        FieldAttribute(
            default={}
        )
    except TypeError as e:
        assert 'defaults for FieldAttribute may not be mutable' in str(e)

    # class C is used as class_type, but isa is not set to 'class'

# Generated at 2022-06-13 07:51:21.177179
# Unit test for constructor of class Attribute
def test_Attribute():
    some_attribute = Attribute(isa='some_type', required=True, default=True, class_type=dict)

    for k in ('isa', 'required', 'default', 'class_type'):
        assert getattr(some_attribute, k) == locals()[k]

    some_attribute = Attribute(isa='some_type', required=True, default=True)
    assert not hasattr(some_attribute, 'class_type')



# Generated at 2022-06-13 07:51:23.565707
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute('const')
    assert attr.isa == 'const'
    assert attr.class_type == None


# Generated at 2022-06-13 07:51:31.382340
# Unit test for constructor of class Attribute
def test_Attribute():

    assert(Attribute() is not None)

    assert(Attribute(isa="list") is not None)

    # Test all the different types of valid parameters
    test_params = {
        'isa': 'list',
        'private': True,
        'default': [],
        'required': False,
        'listof': 'str',
        'priority': 0,
        'class_type': None,
        'always_post_validate': False,
        'inherit': True,
        'alias': None,
        'extend': False,
        'prepend': False
    }

    assert(Attribute(**test_params) is not None)


# Generated at 2022-06-13 07:51:38.537879
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FA = FieldAttribute(isa='list', default=['a', 'b'])
    except TypeError as e:
        print('FAIL: exception raised')
        print(e)

    try:
        FA = FieldAttribute(isa='list', default=lambda: ['a', 'b'])
    except TypeError as e:
        print('FAIL: exception raised')
        print(e)

    print('PASS')


# Generated at 2022-06-13 07:51:44.345916
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='list',listof='Foo',isa='list')
    assert isinstance(fa, Attribute)



# Generated at 2022-06-13 07:51:46.175489
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()
#    fa = FieldAttribute(isa='str')
    assert fa.isa is None, "Failed to construct a FieldAttribute object"



# Generated at 2022-06-13 07:51:47.395750
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute() is not None



# Generated at 2022-06-13 07:51:54.527579
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # sucessful instantiation of FieldAttribute
    field = FieldAttribute(isa=str)
    assert field.isa == str

    # trying to set default value to a mutable container
    with pytest.raises(TypeError):
        field = FieldAttribute(isa='list', default=['some'])

    # trying to set default value to a dictionary
    with pytest.raises(TypeError):
        field = FieldAttribute(isa='dict', default={'some': 'thing'})

    # trying to set default value to a set
    with pytest.raises(TypeError):
        field = FieldAttribute(isa='set', default=set('some'))

    # successful instantiation of FieldAttribute using a callable for default
    def some_callable():
        return ['some_val']

# Generated at 2022-06-13 07:52:05.038659
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute(isa='str', required=True, listof='str', priority=1, private=True, inherit=False)
    if x.isa != 'str':
        raise ValueError('test_Attribute isa failed')
    if x.required != True:
        raise ValueError('test_Attribute required failed')
    if x.listof != 'str':
        raise ValueError('test_Attribute listof failed')
    if x.priority != 1:
        raise ValueError('test_Attribute priority failed')
    if x.private != True:
        raise ValueError('test_Attribute private failed')
    if x.inherit != False:
        raise ValueError('test_Attribute inherit failed')

# Generated at 2022-06-13 07:52:16.245222
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Basic tests for fields.
    a = FieldAttribute(isa='dict', class_type='dummyclass')
    assert a.isa == 'dict', 'FA: got %s' % a.isa
    assert a.class_type == 'dummyclass', 'FA: got %s' % a.class_type
    assert a.default is None, 'FA: got %s' % a.default
    assert a.required is False, 'FA: got %s' % a.required
    assert a.listof is None, 'FA: got %s' % a.listof
    assert a.priority == 0, 'FA: got %d' % a.priority
    assert a.inherit is True, 'FA: got %s' % a.inherit

# Generated at 2022-06-13 07:52:21.993195
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FieldAttribute(
        isa=bool,
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
        prepend=False
    )



# Generated at 2022-06-13 07:52:30.627758
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # obj = FieldAttribute(isa="str", default="Lloyd")
    obj = FieldAttribute(isa="str", default="Lloyd")
    assert obj.isa == "str"
    assert obj.private == False
    assert obj.default == "Lloyd"
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

if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:52:35.685021
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_values = {
        "true_value": (True, True),
        "false_value": (False, False),
        "int_value": (1, 1),
        "float_value": (1.0, 1.0),
        "string_value": ("pwd_attribute", "pwd_attribute"),
    }
    for (key, value) in test_values.items():
        check = FieldAttribute(default=value[0])
        assert value[1] == check.default


# Generated at 2022-06-13 07:52:36.674441
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='list')
    assert fa.isa == 'list'

# Generated at 2022-06-13 07:52:52.599344
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test private
    attr = Attribute(private=True)
    assert attr.private, "Private attribute should be set to True"

    # Test class_type
    attr = Attribute(class_type=int)
    assert attr.class_type == int, "class_type should be set to 'int'"

    # Test always_post_validate
    attr = Attribute(always_post_validate=True)
    assert attr.always_post_validate, "always_post_validate should be set to True"

    # Test inherit
    attr = Attribute(inherit=True)
    assert attr.inherit, "inherit should be set to True"

    # Test alias
    attr = Attribute(alias='testalias')

# Generated at 2022-06-13 07:53:02.626596
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(isa='dict') == FieldAttribute(isa='dict')
    assert FieldAttribute(isa='dict') is not FieldAttribute(isa='dict')
    assert FieldAttribute(isa='dict') != FieldAttribute(isa='int')
    assert FieldAttribute(isa='dict') < FieldAttribute(isa='int')
    assert FieldAttribute(isa='dict') <= FieldAttribute(isa='int')
    assert FieldAttribute(isa='dict') <= FieldAttribute(isa='dict')
    assert FieldAttribute(isa='list') > FieldAttribute(isa='int')
    assert FieldAttribute(isa='list') >= FieldAttribute(isa='int')
    assert FieldAttribute(isa='list') >= FieldAttribute(isa='list')



# Generated at 2022-06-13 07:53:10.298010
# Unit test for constructor of class Attribute
def test_Attribute():
    # Default constructor
    o1 = Attribute()
    assert o1.isa == None
    assert o1.default == None
    assert o1.required == False
    assert o1.listof == None
    assert o1.priority == 0

    # Constructor with a few assigned attributes
    o2 = Attribute(
        isa='some_type',
        default="some_default",
        required=True,
        listof="some_list"
    )
    assert o2.isa == 'some_type'
    assert o2.default == "some_default"
    assert o2.required == True
    assert o2.listof == "some_list"
    assert o2.priority == 0

# Generated at 2022-06-13 07:53:11.432257
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # TODO: needs unit test
    pass

# Generated at 2022-06-13 07:53:14.323787
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='str', default='default')
    assert attr.isa == 'str'
    assert attr.default == 'default'

# Generated at 2022-06-13 07:53:16.791395
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    if not attr:
        raise ValueError("Attribute constructor failed")



# Generated at 2022-06-13 07:53:31.086476
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test defaults
    fa = FieldAttribute()
    assert not fa.private
    assert fa.isa is None
    assert fa.default is None
    assert not fa.required
    assert fa.listof is None
    assert fa.class_type is None
    assert not fa.always_post_validate
    assert fa.inherit
    assert fa.alias is None
    assert not fa.extend
    assert not fa.prepend

    # test that we can specify values for each argument
    fa = FieldAttribute(private=True, isa='string', default='abc',
                        required=True, listof='string', class_type=dict,
                        always_post_validate=True, inherit=False,
                        alias='foo', extend=True, prepend=True)
    assert fa.private
    assert fa.isa == 'string'

# Generated at 2022-06-13 07:53:40.334908
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attributes = FieldAttribute()

    assert field_attributes.isa is None
    assert field_attributes.private is False
    assert field_attributes.default is None
    assert field_attributes.required is False
    assert field_attributes.listof is None
    assert field_attributes.priority == 0
    assert field_attributes.class_type is None
    assert field_attributes.always_post_validate is False
    assert field_attributes.inherit is True
    assert field_attributes.alias is None
    assert field_attributes.extend is False
    assert field_attributes.prepend is False
    assert field_attributes.static is False



# Generated at 2022-06-13 07:53:47.632200
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='dict')
    assert a.isa == 'dict'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.alias is None



# Generated at 2022-06-13 07:53:55.638258
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    isa = 'int'
    private = True
    default = 5
    required = True
    listof = True
    priority = 5
    class_type = None
    always_post_validate = False
    inherit = True
    alias = 'field_alias'

    attr = FieldAttribute(isa=isa,
                          private=private,
                          default=default,
                          required=required,
                          listof=listof,
                          priority=priority,
                          class_type=class_type,
                          always_post_validate=always_post_validate,
                          inherit=inherit,
                          alias=alias)

    assert attr.isa == isa
    assert attr.private == private
    assert attr.default == default
    assert attr.required == required
    assert attr

# Generated at 2022-06-13 07:54:19.125419
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(
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
        extend=False,
        prepend=False,
        static=False,
    )

    assert attribute.isa == 'list'
    assert attribute.private == False
    assert attribute.default == None
    assert attribute.required == False
    assert attribute.listof == None
    assert attribute.priority == 0
    assert attribute.class_type == None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias == None
    assert attribute.extend == False


# Generated at 2022-06-13 07:54:27.311259
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa="list", default="value", required=True, listof=1, inherit=True,
                     always_post_validate=True)
    assert attr.isa == "list"
    assert attr.default == "value"
    assert attr.required
    assert attr.listof == 1
    assert attr.inherit
    assert attr.always_post_validate
    assert attr.private is False
    assert attr.class_type is None
    assert attr.alias is None
    assert attr.is_set() is False



# Generated at 2022-06-13 07:54:35.065376
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'string'
    private = False
    default = None
    required = True
    listof = None
    priority = 10
    class_type = None
    always_post_validate = False
    inherit = True
    alias = None
    extend = True
    prepend = False
    static = False

    at = Attribute(isa, private, default, required, listof, priority,
                   class_type, always_post_validate, inherit, alias, extend,
                   prepend, static)

    assert isa == at.isa
    assert private == at.private
    assert default == at.default
    assert required == at.required
    assert listof == at.listof
    assert priority == at.priority
    assert class_type == at.class_type
    assert always_post_validate == at.always_

# Generated at 2022-06-13 07:54:36.070349
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().__dict__


# Generated at 2022-06-13 07:54:47.001741
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=1)
    assert a.isa == 1
    assert a.private == False
    assert a.default is None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate == False
    assert a.inherit == True
    a = Attribute(isa=None, private=False, default=None, required=False, listof=None, priority=0, class_type=None,
                  always_post_validate=False, inherit=True)
    assert a.isa is None
    assert a.private == False
    assert a.default is None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0

# Generated at 2022-06-13 07:54:50.677013
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa='foo', private=True)
    assert(a.isa == 'foo')
    assert(a.private == True)

    b = Attribute(isa='bar')
    assert(b.isa == 'bar')

# Generated at 2022-06-13 07:54:58.087106
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = FieldAttribute()
    assert attr.isa == None
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.prepend == False
    assert attr.extend == False
    assert attr.static == False


# Generated at 2022-06-13 07:55:08.353544
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='int', default=10)
    a.isa == 'int'
    a.default == 10

    a = Attribute(isa='dict', default=dict(a=1, b=2))
    a.isa == 'dict'
    a.default == dict(a=1, b=2)

    # not a callable
    try:
        a = Attribute(isa='dict', default=dict)
        raise TypeError('defaults for FieldAttribute may not be mutable, please provide a callable instead')
    except:
        return True

    # a callable
    a = Attribute(isa='dict', default=lambda: dict(a=1, b=2))
    a.isa == 'dict'
    a.default() == dict(a=1, b=2)



# Generated at 2022-06-13 07:55:14.519400
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(isa='dict')
    assert attribute.isa == 'dict'
    assert attribute.private == False
    assert attribute.default == None
    #assert attribute.required == "isa"
    assert attribute.listof == None
    assert attribute.priority == 0
    assert attribute.class_type == None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.extend == False
    assert attribute.prepend == False
    assert attribute.static == False

# Generated at 2022-06-13 07:55:18.964739
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(private=True, class_type=str, listof=str, inherit=True,
        always_post_validate=False)
    assert a.default is None
    assert a.required is False
    assert a.alias is None
    assert a.extend is False
    assert a.prepend is False
    assert a.static is False

# Generated at 2022-06-13 07:55:52.778064
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert a.isa is None
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



# Generated at 2022-06-13 07:55:55.751514
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        a = FieldAttribute(default={}, inherit=False)
        assert a.default is not None
    except TypeError as e:
        assert False, e
    return True



# Generated at 2022-06-13 07:56:04.662834
# Unit test for constructor of class Attribute
def test_Attribute():

    attr_obj = Attribute(isa='str')
    assert attr_obj.isa == 'str'
    assert attr_obj.private is False
    assert attr_obj.default is None
    assert attr_obj.required is False
    assert attr_obj.listof is None
    assert attr_obj.priority == 0
    assert attr_obj.class_type is None
    assert attr_obj.always_post_validate is False
    assert attr_obj.inherit is True
    assert attr_obj.alias is None

    attr_obj = Attribute(isa='list', default=[])
    assert attr_obj.isa == 'list'
    assert attr_obj.default == []

    # a default value may not be mutable, please provide a callable instead


# Generated at 2022-06-13 07:56:06.864815
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fieldattribute_test = FieldAttribute(isa='dict', default=dict)
    assert fieldattribute_test.isa == 'dict'



# Generated at 2022-06-13 07:56:12.439191
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test __init__ method
    # Test that a private attribute isn't set
    attr = Attribute(private = True)
    assert attr.private == True
    # Test that an attribute with a custom type is set
    attr = Attribute(isa = str)
    assert attr.isa == str
    # Test that an attribute with a custom type and an alias is set
    attr = Attribute(isa = str, alias='custom_alias')
    assert attr.isa == str
    assert attr.alias == 'custom_alias'

# Generated at 2022-06-13 07:56:21.976084
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='bool', private=False, default=False, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert attr.isa == 'bool'
    assert attr.private == False
    assert attr.default == False
    assert attr.required == False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias is None



# Generated at 2022-06-13 07:56:32.478604
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute(isa='str')
    assert FA.isa == 'str'
    assert FA.private == False
    assert FA.default == None
    assert FA.required == False
    assert FA.listof == None
    assert FA.priority == 0
    assert FA.class_type == None
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.alias == None
    assert FA.extend == False
    assert FA.prepend == False
    assert FA.static == False
    FA = FieldAttribute(isa='str', private=True, default='test', required=True, listof='list', priority=10, class_type='int', always_post_validate=True, inherit=False, alias='test', extend=True, prepend=True, static=True )

# Generated at 2022-06-13 07:56:35.159820
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='foo',class_type='Foo').isa == 'foo'
    assert Attribute(isa='foo',class_type='Foo').class_type == 'Foo'



# Generated at 2022-06-13 07:56:41.906452
# Unit test for constructor of class Attribute
def test_Attribute():
    # isa must be one of basic YAML datatype, python class, or percent
    try:
        Attribute(isa='invalid')
        assert False
    except TypeError:
        assert True
    # default must be immutable
    try:
        Attribute(default={})
        assert False
    except TypeError:
        assert True
    # default must be callable if isa is one of container type
    try:
        Attribute(isa='list', default=[])
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-13 07:56:44.373949
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute("test")
    assert attr.isa == "test"


# Generated at 2022-06-13 07:57:46.694575
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(
        isa='list',
        listof='string',
        private=False,
        default=None,
        required=False,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    assert foo.isa == 'list'
    assert foo.private == False
    assert foo.default == None
    assert foo.required == False
    assert foo.priority == 0
    assert foo.class_type == None
    assert foo.always_post_validate == False
    assert foo.inherit == True
    assert foo.alias == None
    assert foo.extend == False
    assert foo.prepend == False


# Generated at 2022-06-13 07:57:47.588423
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute()



# Generated at 2022-06-13 07:57:54.930624
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.module_utils.six import iteritems
    # test direct instantiation
    x = Attribute(
        isa='str',
        default='foobar',
        required=True,
        listof='int',
        private=True,
        priority=10,
        extend=True,
        prepend=True,
    )
    # test that the arguments are preserved
    assert x.isa == 'str'
    assert x.default == 'foobar'
    assert x.required == True
    assert x.listof == 'int'
    assert x.private == True
    assert x.extend == True
    assert x.prepend == True
    # test deprecated subclass

# Generated at 2022-06-13 07:58:02.649988
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import pytest
    fa = FieldAttribute()
    fa.__name__ = 'test'
    with pytest.raises(TypeError):
        _ = fa.default

    fa.listof = 'list'
    with pytest.raises(TypeError):
        _ = fa.listof

    fa.listof = 'other'
    assert fa.listof == 'other'

    fa.listof = Attribute()
    assert isinstance(fa.listof, Attribute)


# Generated at 2022-06-13 07:58:04.388026
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(
    isa='list of strings'
    )
    assert field.isa == 'list of strings'

# Generated at 2022-06-13 07:58:14.631973
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test for empty constructor
    f = FieldAttribute()
    assert f.isa is None
    assert f.private is False
    assert f.default is None
    assert f.required is False
    assert f.listof is None
    assert f.priority == 0
    assert f.class_type is None
    assert f.always_post_validate is False
    assert f.inherit is True
    assert f.alias is None
    assert f.extend is False
    assert f.prepend is False
    assert f.static is False

    # Test for keyword arguments
    # isa
    f = FieldAttribute(isa='list')
    assert f.isa is 'list'
    f = FieldAttribute(isa='dict')
    assert f.isa is 'dict'
    f = FieldAttribute(isa='str')

# Generated at 2022-06-13 07:58:21.568081
# Unit test for constructor of class Attribute

# Generated at 2022-06-13 07:58:28.320270
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test initialization of the Attribute Class
    attr = Attribute(
        isa='test')
    assert attr.__class__.__name__ == 'Attribute'
    assert attr.isa == 'test'
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == None
    assert attr.prepend == None
    assert attr.static == False

    # Test initialization of the Attribute Class

# Generated at 2022-06-13 07:58:30.325208
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='string')
    assert attr.isa == 'string'
    attr = Attribute(isa='list', listof='string')
    assert attr.listof == 'string'



# Generated at 2022-06-13 07:58:42.268371
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(
        isa='test',
        private='test',
        default='test',
        required='test',
        listof='test',
        priority='test',
        class_type='test',
        always_post_validate='test',
        inherit='test',
        alias='test',
        extend = 'test',
        prepend = 'test'
    )
    assert foo.isa == 'test'
    assert foo.private == 'test'
    assert foo.default == 'test'
    assert foo.required == 'test'
    assert foo.listof == 'test'
    assert foo.priority == 'test'
    assert foo.class_type == 'test'
    assert foo.always_post_validate == 'test'
    assert foo.inherit == 'test'
    assert foo.alias