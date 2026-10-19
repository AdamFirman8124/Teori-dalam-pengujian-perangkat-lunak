

# Generated at 2022-06-13 07:49:19.122499
# Unit test for constructor of class Attribute
def test_Attribute():
    test_attr = Attribute(isa="string", private=False)
    assert test_attr.isa == "string"
    assert test_attr.private == False
    test_attr = Attribute(isa="string", private=True)
    assert test_attr.isa == "string"
    assert test_attr.private == True
    test_attr = Attribute(isa="string", default="default")
    assert test_attr.isa == "string"
    assert test_attr.default == "default"
    test_attr = Attribute(isa="string", required=True)
    assert test_attr.isa == "string"
    assert test_attr.required == True
    test_attr = Attribute(isa="list", listof="string")
    assert test_attr.isa == "list"

# Generated at 2022-06-13 07:49:20.806923
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='str')
    assert isinstance(attr, FieldAttribute)


# Generated at 2022-06-13 07:49:26.439505
# Unit test for constructor of class Attribute
def test_Attribute():
    # if 'default' is not callable, then following error is raised
    #   TypeError: defaults for FieldAttribute may not be mutable, please provide a callable instead
    c = Attribute(private=True, default={1:True}, always_post_validate=True)
    # the default value of 'default' is None.
    c = Attribute(private=True)
    print("c.default = ", c.default)
    assert c.default == None

# Generated at 2022-06-13 07:49:31.875577
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list', inherit=True, listof='dict', required=False, private=False)
    assert attr is not None
    assert attr.isa == 'list'
    assert attr.listof == 'dict'
    assert attr.required is False
    assert attr.private is False
    assert attr.inherit is True



# Generated at 2022-06-13 07:49:39.841550
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test with required=False and no isa
    a = Attribute(required=False)
    assert a.required == False
    assert a.isa == None

    # Test with required=False and isa
    a = Attribute(required=False, isa='boolean')
    assert a.required == False

    # Testing with required=True and no isa
    a = Attribute(required=True)
    assert a.required == True

    # Testing with required=True and isa='string'
    a = Attribute(required=True, isa='string')
    assert a.required == True
    assert a.isa == 'string'

    # Testing with required=True and isa='list'
    a = Attribute(required=True, isa='list')
    assert a.required == True

# Generated at 2022-06-13 07:49:47.319562
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='test')
    assert fa.isa == 'test'
    assert fa.private is False
    assert fa.default is None
    assert fa.required is False
    assert fa.listof is None
    assert fa.priority == 0
    assert fa.class_type is None
    assert fa.always_post_validate is False
    assert fa.inherit is True
    assert fa.alias is None
    assert fa.extend is False
    assert fa.prepend is False
    assert fa.static is False


# Generated at 2022-06-13 07:49:57.231559
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'test_isa'
    private = False
    default = 'test_default'
    required = False
    listof = 'test_listof'
    priority = 1
    class_type = 'test_class_type'
    always_post_validate = False
    inherit = True
    alias = 'test_alias'
    attr = Attribute(isa=isa, private=private, default=default, required=required, listof=listof,
                     priority=priority, class_type=class_type, always_post_validate=always_post_validate,
                     inherit=inherit, alias=alias)
    assert attr.isa == isa
    assert attr.private == private
    assert attr.default == default
    assert attr.required == required
    assert attr.listof == listof

# Generated at 2022-06-13 07:50:08.975284
# Unit test for constructor of class Attribute
def test_Attribute():
    from units.mock.loader import DictDataLoader

    isa = 1
    private = True
    default = 'A'
    required = True
    listof = 2
    priority = 3
    class_type = DictDataLoader
    always_post_validate = False
    inherit = True
    alias = 'test'
    extend = False
    prepend = False
    static = False


# Generated at 2022-06-13 07:50:19.949236
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list', static=True)
    assert attr.isa == 'list'
    assert attr.static == True
    attr = FieldAttribute(default=['1','2','3'])
    assert attr.default() == ['1','2','3']
    attr = FieldAttribute(required=['1','2','3'])
    assert attr.required(['1','2','3']) == ['1','2','3']
    attr = FieldAttribute(listof='list', extend=True)
    assert attr.listof == 'list'
    assert attr.extend == True
    attr = FieldAttribute(class_type=['1','2','3'])
    assert attr.class_type(['1','2','3']) == ['1','2','3']
    att

# Generated at 2022-06-13 07:50:24.120506
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    attr = Attribute('list', private=True, default=None, required=True, listof='list', priority=10, class_type='list', always_post_validate=True, inherit=False)
    attr = Attribute(default=dict)
    attr = Attribute(default=[])


# Generated at 2022-06-13 07:50:30.088727
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.isa == None
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None


# Generated at 2022-06-13 07:50:40.739134
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa = 'dict',
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

    assert isinstance(a, Attribute)

    assert a.isa == 'dict'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias

# Generated at 2022-06-13 07:50:53.692680
# Unit test for constructor of class Attribute
def test_Attribute():
    my_attr = Attribute(isa='list', default=[])
    assert my_attr.isa == 'list'
    assert my_attr.default == []
    try:
        my_attr2 = Attribute(isa='list', default=[1,2,3])
        res = False
    except TypeError:
        res = True
    assert res
    my_attr3 = Attribute(isa='list', default=lambda: [])
    try:
        my_attr3 = Attribute(isa='list', default=lambda: {'foo':'bar'})
        assert False
    except TypeError:
        assert True
    assert my_attr3.isa == 'list'
    assert callable(my_attr3.default)
    assert my_attr3.default() == []



# Generated at 2022-06-13 07:50:55.897839
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    x = FieldAttribute(required=False, isa='float', default=5.0, listof='str')
    assert x.required == False
    assert x.isa == 'float'
    assert x.default == 5.0
    assert x.listof == 'str'



# Generated at 2022-06-13 07:51:02.275344
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
        isa='list',
        private=False,
        default=None,
        required=False,
        listof='list',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert f.isa == 'list'


# Generated at 2022-06-13 07:51:10.747108
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert isinstance(a, Attribute)
    b = Attribute(isa='foo')
    assert isinstance(b, Attribute)
    assert b.isa == 'foo'
    c = Attribute(isa='foo', private=True)
    assert isinstance(c, Attribute)
    assert c.isa == 'foo'
    assert c.private == True
    d = Attribute(isa='foo', private=True, default='bar')
    assert isinstance(d, Attribute)
    assert d.isa == 'foo'
    assert d.private == True
    assert d.default == 'bar'
    assert d.required == False
    assert d.listof == None
    assert d.priority == 0
    assert d.class_type == None
    assert d.always_post_validate == False

# Generated at 2022-06-13 07:51:13.787139
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import pytest
    with pytest.raises(TypeError):
        FieldAttribute(default=dict(test=True))
    field = FieldAttribute(default=lambda: dict(test=True))
    assert field.default() == dict(test=True)


# Generated at 2022-06-13 07:51:20.037815
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
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
        static=False
    )
    assert field_attribute.isa == 'dict'



# Generated at 2022-06-13 07:51:29.660012
# Unit test for constructor of class Attribute
def test_Attribute():
    test_attr = Attribute(isa='bool',
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
                static=False)
    print("Type test_attr: %s" % test_attr)
    print("Type test_attr.isa: %s" % test_attr.isa)
    test_attr.isa = 'bool'
    print("Change isa to boolean, Type test_attr.isa: %s" % test_attr.isa)


if __name__ == '__main__':
    test_Attribute()

# Generated at 2022-06-13 07:51:36.630569
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    Tests the constructor of class FieldAttribute.

    :return: None
    """

    # Tests
    # Test constructor FieldAttribute
    test_attr = FieldAttribute(isa="int", private=True, default=1, required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=False, alias=None)
    assert(test_attr.isa == "int")
    assert(test_attr.private == True)
    assert(test_attr.default == 1)
    assert(test_attr.required == True)
    assert(test_attr.listof == None)
    assert(test_attr.priority == 0)
    assert(test_attr.class_type == None)
    assert(test_attr.always_post_validate == False)

# Generated at 2022-06-13 07:51:45.333131
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='str', private=True, default=None, required=True, listof='str')
    attr1 = FieldAttribute(isa='str', private=True, default=None, required=True, listof='str')
    assert attr == attr1



# Generated at 2022-06-13 07:51:52.697748
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test the __init__ method of class FieldAttribute
    test_fa = FieldAttribute(
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
    assert type(test_fa) == FieldAttribute
    assert test_fa.isa == 'list'
    assert test_fa.private == False
    assert test_fa.default == None
    assert test_fa.required == False
    assert test_fa.listof == None
    assert test_fa.priority == 0
    assert test_fa.class_type == None

# Generated at 2022-06-13 07:51:53.586990
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute('str')


# Generated at 2022-06-13 07:51:54.952157
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test init
    test_obj = FieldAttribute()
    assert test_obj is not None


# Generated at 2022-06-13 07:52:00.814885
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fatt = FieldAttribute()
    assert fatt.isa is None
    assert fatt.private is False
    assert fatt.default is None
    assert fatt.required is False
    assert fatt.listof is None
    assert fatt.priority == 0
    assert fatt.class_type is None
    assert fatt.always_post_validate is False
    assert fatt.inherit is True
    assert fatt.alias is None
    assert fatt.extend is False
    assert fatt.prepend is False
    assert fatt.static is False

    fatt = FieldAttribute(isa='string')
    assert fatt.isa == 'string'
    assert fatt.private is False
    assert fatt.default is None
    assert fatt.required is False
    assert fatt.listof is None

# Generated at 2022-06-13 07:52:03.259233
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FieldAttribute(isa='list', private=False, required=False, default=None)



# Generated at 2022-06-13 07:52:07.285773
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='dict', default='{"a": ["b", "c", "d"]}')
    assert field.isa == 'dict'
    assert field.default() == {'a': ['b', 'c', 'd']}



# Generated at 2022-06-13 07:52:16.773841
# Unit test for constructor of class Attribute
def test_Attribute():
    import pytest

    with pytest.raises(TypeError) as e:
        Attribute(default=['foo', 'bar'])
    assert 'defaults for FieldAttribute may not be mutable' in str(e)

    a = Attribute()
    assert a.isa is None
    assert not a.private
    assert a.default is None
    assert not a.required
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert not a.always_post_validate
    assert a.inherit
    assert a.alias is None
    assert not a.extend
    assert not a.prepend
    assert not a.static


# Generated at 2022-06-13 07:52:20.884682
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='boolean', required=True)
    assert attr.isa == 'boolean'
    assert attr.required == True
    assert attr.private == False
    assert attr.default == None
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None

    # Test handling of constructor's 'default' parameter.
    attr = FieldAttribute(isa='list', default=['one', 'two', 'three'])
    assert attr.default == ['one', 'two', 'three']

# Generated at 2022-06-13 07:52:26.889449
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


# Generated at 2022-06-13 07:52:39.757625
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', listof='str', always_post_validate=True)
    assert a.isa == 'str'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == 'str'
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == True
    assert a.inherit == True
    assert a.alias == None

    b = Attribute(isa='list', listof='str', always_post_validate=True)
    assert a.isa == b.isa


# Test if the inherited Attribute is correctly sorted

# Generated at 2022-06-13 07:52:50.487840
# Unit test for constructor of class Attribute
def test_Attribute():
    # Check that the initialization is OK with no argument
    attribute = Attribute()
    assert attribute.isa is None
    assert attribute.private is False
    assert attribute.default is None
    assert attribute.required is False
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert attribute.always_post_validate is False
    assert attribute.alias is None

    # Check that the initialization is OK with all arguments
    attribute = Attribute(isa="integer",
                          private=True,
                          default=100,
                          required=True,
                          listof="string",
                          priority=50,
                          class_type='',
                          always_post_validate=True,
                          inherit=False,
                          alias="unit_test_alias")
    assert attribute

# Generated at 2022-06-13 07:53:01.851073
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # isa
    f = FieldAttribute(isa=dict)
    assert f.isa is dict
    f = FieldAttribute(isa=3)
    assert f.isa is int
    f = FieldAttribute(isa=2.5)
    assert f.isa is float
    f = FieldAttribute(isa="str string")
    assert f.isa is str
    f = FieldAttribute(isa=r'rstring')
    assert f.isa is str
    f = FieldAttribute(isa=[])
    assert f.isa is list
    f = FieldAttribute(isa=(1, 2, 3))
    assert f.isa is tuple
    f = FieldAttribute(isa=set())
    assert f.isa is set

    # default
    f = FieldAttribute(default=[])
    assert f.default == []

# Generated at 2022-06-13 07:53:08.939388
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(listof='string', priority=10)
    assert field.isa is None
    assert field.listof == 'string'
    assert field.priority == 10
    assert field.required is False
    assert type(field)

    field = FieldAttribute()
    assert field.isa is None
    assert field.listof is None
    assert field.priority == 0
    assert field.required is False
    assert type(field)



# Generated at 2022-06-13 07:53:17.730219
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA=FieldAttribute
    assert type(FA()) is FieldAttribute
    assert type(FA(None)) is FieldAttribute
    assert type(FA(False)) is FieldAttribute
    assert type(FA(0)) is FieldAttribute
    assert type(FA('')) is FieldAttribute
    assert type(FA(None, False)) is FieldAttribute
    assert type(FA(True, False)) is FieldAttribute
    assert type(FA(0, False)) is FieldAttribute
    assert type(FA('', False)) is FieldAttribute
    assert type(FA(None, True)) is FieldAttribute
    assert type(FA(True, True)) is FieldAttribute
    assert type(FA(0, True)) is FieldAttribute
    assert type(FA('', True)) is FieldAttribute
    default = {'foo': 'bar'}
    assert type(FA(default=default)) is FieldAttribute

# Generated at 2022-06-13 07:53:27.720176
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute(isa='dict', class_type=dict)
    obj = Attribute(isa='list', class_type=list)
    obj = Attribute(isa='str', class_type=str)
    obj = Attribute(isa='int', class_type=int)
    obj = Attribute(isa='bool', class_type=bool)
    obj = Attribute(isa='float', class_type=float)
    obj = Attribute(isa='percent', class_type=int)
    obj = Attribute(isa='complex', class_type=complex)
    obj = Attribute(isa='unicode', class_type=unicode)
    obj = Attribute(isa='class', default=dict)
    obj = Attribute(isa='class', default=list)
    obj = Attribute(isa='class', default=str)

# Generated at 2022-06-13 07:53:34.575529
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_attrs = dict(
        isa='list',
        private=False,
        default=None,
        required=False,
        listof='dict',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True
    )
    field_attr = FieldAttribute(**test_attrs)

    for k, v in test_attrs.items():
        assert getattr(field_attr, k) == v



# Generated at 2022-06-13 07:53:43.532247
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test if default value is None
    attr_1 = FieldAttribute(default=None)
    assert attr_1.default == None
    # test if default value is a number
    attr_2 = FieldAttribute(default=1)
    assert attr_2.default == 1
    # test if default value is a list
    attr_3 = FieldAttribute(default=[1])
    assert attr_3.default[0] == 1
    # test if default value is a string
    attr_4 = FieldAttribute(default="1")
    assert attr_4.default == "1"
    # test if default value is a dictionary
    attr_5 = FieldAttribute(default={"a":"b"})
    assert attr_5.default["a"] == "b"
    # test if default value is a callable


# Generated at 2022-06-13 07:53:49.771603
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='dict',
        private=False,
        default=dict(),
        required=True,
        listof='list',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias='test',
        extend=False,
        prepend=False,
        static=False,
    )

# Generated at 2022-06-13 07:53:56.825837
# Unit test for constructor of class Attribute
def test_Attribute():

    print("Testing class Attribute...")
    test_isa = "class"
    test_private = True
    test_default = None
    test_required = True
    test_listof = None
    test_priority = 9
    test_class_type = None
    test_always_post_validate = False
    test_inherit = True
    test_alias = None


# Generated at 2022-06-13 07:54:17.770123
# Unit test for constructor of class Attribute
def test_Attribute():
    class TestObject:
        a = Attribute(isa='int', default=1, required=False)
        b = Attribute(isa='int', default=1, required=False)

    assert TestObject.a > TestObject.b
    assert TestObject.a == TestObject.a
    assert TestObject.a != TestObject.b
    assert TestObject.a >= TestObject.a
    assert TestObject.a >= TestObject.b
    assert TestObject.a <= TestObject.a
    assert TestObject.a <= TestObject.b

# Generated at 2022-06-13 07:54:24.376690
# Unit test for constructor of class Attribute
def test_Attribute():
    import types
    from ansible.module_utils.six import string_types


# Generated at 2022-06-13 07:54:26.230991
# Unit test for constructor of class Attribute
def test_Attribute():
    test_attr = Attribute(isa='class')
    assert (test_attr.isa == 'class')

# Generated at 2022-06-13 07:54:29.773026
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        a = Attribute(default=['some', 'list'])
    except TypeError:
        assert True
    else:
        assert False, 'defaults for FieldAttribute may not be mutable, please provide a callable instead'

# Generated at 2022-06-13 07:54:34.307123
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list', listof='str')
    assert attr.isa == 'list'
    assert attr.listof == 'str'
    assert attr.default == None
    assert attr.required == False
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True


# Generated at 2022-06-13 07:54:41.669493
# Unit test for constructor of class Attribute

# Generated at 2022-06-13 07:54:51.738217
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int')
    assert attr.isa == 'int'
    attr = Attribute(isa='int', default=10)
    assert attr.default == 10
    attr = Attribute(isa='int', default=lambda: 10)
    assert attr.default() == 10
    attr = Attribute(isa='int', default=None)
    assert attr.default is None


#
# portability of namedtuples.
#
# On some systems, namedtuple isn't available in the collections module in python2.4,
# while it is in python2.6, which makes name collisions with constants on 2.6 and 2.4, even
# though 2.6 doesn't have the constants module.
#

# Generated at 2022-06-13 07:54:58.239322
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
    assert fa.extend == False
    assert fa.prepend == False
    assert fa.static == False



# Generated at 2022-06-13 07:55:04.239636
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute
    test = f(default="test")
    assert test.default == "test"
    assert test.isa == None
    assert test.private == False
    assert test.required == False
    assert test.listof == None
    assert test.priority == 0
    assert test.class_type == None
    assert test.always_post_validate == False
    assert test.inherit == True
    assert test.alias == None



# Generated at 2022-06-13 07:55:13.998830
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test no options
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

    # Test all options

# Generated at 2022-06-13 07:55:48.324101
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
        isa='dict',
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
        static=False
    )

    assert field_attribute.isa == 'dict'
    assert field_attribute.private == False
    assert field_attribute.default == None
    assert field_attribute.required == False
    assert field_attribute.listof == 'dict'
    assert field_attribute.priority == 0
    assert field_attribute.class_type == None
    assert field_attribute.always_post_validate == False
    assert field_attribute.inher

# Generated at 2022-06-13 07:55:59.443891
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=False, default=None, required=False, listof=None,
                  priority=0, class_type=None)
    assert a.isa == 'str'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None

    try:
        a = Attribute(isa='list', default=[])
        assert False, "Attribute constructor should fail with mutable default"
    except TypeError as e:
        assert True
    #assert e.message == 'Attribute constructor should fail with mutable default'

    a = Attribute(isa='str', default=str())
    assert a.isa == 'str'
    assert a.default == str()

   

# Generated at 2022-06-13 07:56:08.497740
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    class Container(object):
        x = FieldAttribute(isa='list')
        y = FieldAttribute(isa='str', default='foo')
        z = FieldAttribute(isa='str', default='foo', static=True)
        w = FieldAttribute(isa='int', default=lambda: 5)

    test_object = Container()

    assert isinstance(test_object.x, dict)
    assert isinstance(test_object.y, str)
    assert isinstance(test_object.z, str)
    assert isinstance(test_object.w, int)



# Generated at 2022-06-13 07:56:14.214358
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
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



# Generated at 2022-06-13 07:56:25.101960
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.utils.listify import listify_lookup_plugin_terms
    assert FieldAttribute(always_post_validate=True) is not None
    assert FieldAttribute(always_post_validate=True).__doc__ is not None
    assert FieldAttribute(always_post_validate=True).isa is None
    assert FieldAttribute(always_post_validate=True, isa="list").isa == "list"
    assert FieldAttribute(always_post_validate=True, isa=["list", "str"]).isa == ["list", "str"]
    assert FieldAttribute(always_post_validate=True, isa=listify_lookup_plugin_terms(["foo"], templar=None, loader=None)).isa == "foo"

# Generated at 2022-06-13 07:56:31.960273
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
    assert a.extend is False
    assert a.prepend is False
    assert a.class_type is None
    assert a.static is False



# Generated at 2022-06-13 07:56:39.266374
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:56:50.822770
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attrib = FieldAttribute(isa='list', private=False, default=None, required=False, listof=None,
                                  priority=0, class_type=None, always_post_validate=False, inherit=True,
                                  alias=None, extend=False, prepend=False, static=False)

    assert (field_attrib.isa == 'list')
    assert (field_attrib.private == False)
    assert (field_attrib.default == None)
    assert (field_attrib.required == False)
    assert (field_attrib.listof == None)
    assert (field_attrib.priority == 0)
    assert (field_attrib.class_type == None)
    assert (field_attrib.always_post_validate == False)

# Generated at 2022-06-13 07:56:53.692631
# Unit test for constructor of class Attribute
def test_Attribute():
    dict1 = dict(isa='dict', static=True, class_type='test')
    attribute = Attribute(**dict1)

    assert(attribute.isa == 'dict')
    assert(attribute.static == True)
    assert(attribute.class_type == 'test')


# Generated at 2022-06-13 07:56:55.080896
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_instance = FieldAttribute()
    assert test_instance is not None
    return True



# Generated at 2022-06-13 07:57:55.960541
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa = "list")
    assert attr.isa == "list"
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


# Generated at 2022-06-13 07:58:07.357181
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    atr = FieldAttribute()
    assert atr.isa == None
    assert atr.private == False
    assert atr.default == None
    assert atr.required == False
    assert atr.listof == None
    assert atr.priority == 0
    assert atr.class_type == None
    assert atr.always_post_validate == False
    assert atr.inherit == True
    assert atr.alias == None
    atr = FieldAttribute(isa='token')
    assert atr.isa == 'token'
    atr = FieldAttribute(isa='token', inherit=False)
    assert atr.inherit == False
    atr = FieldAttribute(isa='token', alias='alias')
    assert atr.isa == 'token'
    assert atr.alias == 'alias'
    atr

# Generated at 2022-06-13 07:58:16.240570
# Unit test for constructor of class Attribute
def test_Attribute():
    immutables = (str, int, float, bool)
    myattr = Attribute(isa=immutables)
    assert myattr.isa == immutables

    myattr2 = Attribute(isa=immutables)
    assert myattr == myattr2

    class Base1(object):
        pass
    class Base2(object):
        pass
    class Derived(Base1, Base2):
        pass
    myattr = Attribute(isa=Base1)
    myattr2 = Attribute(isa=Base2)
    assert myattr != myattr2

    myattr = Attribute(isa=Derived)
    myattr2 = Attribute(isa=Base2)
    assert myattr != myattr2



# Generated at 2022-06-13 07:58:25.186745
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test simple use
    attr = Attribute()

    # Test isa
    attr = Attribute(isa='bool')
    assert attr.isa == 'bool'

    # Test default
    attr = Attribute(default='foo')
    assert attr.default == 'foo'

    # Test required
    attr = Attribute(required=True)
    assert attr.required

    # Test listof
    attr = Attribute(isa='list', listof=True)
    assert attr.isa == 'list'
    assert attr.listof == True

    # Test priority
    attr = Attribute(priority=1)
    assert attr.priority == 1

    attr = Attribute(always_post_validate=True)
    assert attr.always_post_validate

    # Test class_

# Generated at 2022-06-13 07:58:30.771279
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute('isa',True,None,False,'listof',1,'class_type',True,True,'alias')
    assert attribute.isa == 'isa'
    assert attribute.private == True
    assert attribute.default == None
    assert attribute.required == False
    assert attribute.listof == 'listof'
    assert attribute.priority == 1
    assert attribute.class_type == 'class_type'
    assert attribute.always_post_validate == True
    assert attribute.inherit == True
    assert attribute.alias == 'alias'

test_Attribute()

# Generated at 2022-06-13 07:58:33.409910
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # Ensure function returns an object of class FieldAttribute
    assert isinstance(FieldAttribute(), FieldAttribute)

    # Ensure function fails if an attribute is of a mutable data-type
    try:
        # Try to instantiate FieldAttribute with a mutable default
        FieldAttribute(default={})
    except TypeError:
        assert True
    else:
        assert False

# Generated at 2022-06-13 07:58:35.205742
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # Passing no args should work
    FieldAttribute()



# Generated at 2022-06-13 07:58:47.059461
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int', private=False, default=None, required=False, listof=None, priority=0)
    assert attr.isa == 'int'

    attr = Attribute(isa='list', default='my_list', required=False, listof=None, priority=0)
    assert attr.isa == 'list'
    assert attr.default == 'my_list'

    attr = Attribute(isa='list', default=list, required=False, listof=None, priority=0)
    assert attr.isa == 'list'
    assert attr.default == list

    attr = Attribute(isa='set', default=set, required=False, listof=None, priority=0)
    assert attr.isa == 'set'
    assert attr.default == set

    att

# Generated at 2022-06-13 07:58:51.830036
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list', listof='string', default=[])
    assert isinstance(attr.default, list)
    assert isinstance(attr.default[0], str)
    attr = Attribute(isa='list', default=[])
    assert isinstance(attr.default, list)

# Generated at 2022-06-13 07:58:55.015141
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

if __name__ == '__main__':
    test_FieldAttribute()