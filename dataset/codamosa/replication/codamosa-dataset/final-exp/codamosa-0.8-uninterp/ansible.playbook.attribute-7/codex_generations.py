

# Generated at 2022-06-13 07:49:08.510848
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    def test_default():
        pass

    attr = FieldAttribute(
        isa='list',
        private=False,
        default=test_default,
        required=False,
        listof='str',
        priority=0,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
    )
    assert attr.isa == 'list'
    assert attr.private == False
    assert attr.required == False
    assert attr.listof == 'str'
    assert attr.priority == 0
    assert attr.inherit == True
    assert attr.alias is None
    assert attr.extend == False
    assert attr.prepend == False
    assert callable(attr.default)

    # default cannot be mutable

# Generated at 2022-06-13 07:49:09.819579
# Unit test for constructor of class Attribute
def test_Attribute():

    attribute = Attribute()


# Generated at 2022-06-13 07:49:17.154404
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(isa='list',
                               private=False,
                               default=None,
                               required=True,
                               listof='str',
                               priority=0,
                               class_type=None,
                               always_post_validate=False,
                               inherit=True,
                               alias=None)

    if not isinstance(attribute, FieldAttribute):
        raise AssertionError




# Generated at 2022-06-13 07:49:26.940667
# Unit test for constructor of class Attribute
def test_Attribute():

    # test the basic structure
    test_field = Attribute()
    assert test_field.private == False
    assert test_field.default == None
    assert test_field.required == False
    assert test_field.listof == None
    assert test_field.priority == 0
    assert test_field.class_type == None
    assert test_field.always_post_validate == False
    assert test_field.inherit == True

    test_field = Attribute(private=False, default="a", required=False, listof="b", priority=10, class_type="c", always_post_validate=False, inherit=True)

    assert test_field.private == False
    assert test_field.default == "a"
    assert test_field.required == False
    assert test_field.listof == "b"

# Generated at 2022-06-13 07:49:36.462102
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    FA_Default = FieldAttribute()
    assert(FA_Default.isa == None)
    assert(FA_Default.private == False)
    assert(FA_Default.default == None)
    assert(FA_Default.required == False)
    assert(FA_Default.listof == None)
    assert(FA_Default.priority == 0)
    assert(FA_Default.class_type == None)
    assert(FA_Default.always_post_validate == False)
    assert(FA_Default.inherit == True)
    assert(FA_Default.alias == None)
    assert(FA_Default.extend == False)
    assert(FA_Default.prepend == False)
    assert(FA_Default.static == False)


# Generated at 2022-06-13 07:49:39.378677
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='str', private=False, default=None, required=False, listof=None,
                           priority=0, class_type=None, always_post_validate=False)

    assert isinstance(field, FieldAttribute)



# Generated at 2022-06-13 07:49:50.973783
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(
        isa='str',
        private=True,
        default='spam',
        required=True,
        listof=Attribute(
            isa='str',
            private=False,
            default='eggs',
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
        ),
        priority=0,
        class_type=None,
        always_post_validate=True,
        inherit=False,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )


# Generated at 2022-06-13 07:50:03.762166
# Unit test for constructor of class Attribute
def test_Attribute():
    import types
    import pytest

    # Positional args
    with pytest.raises(TypeError):
        Attribute(isa=types.StringType, default='foo')

    # Named args, w/defaults
    Attribute(isa=types.StringType)
    Attribute(isa=types.StringType, default='foo', required=True)

    # Always set required to False on instantiation
    a = Attribute(isa=types.StringType)
    assert a.required == False

    # Wrong isa type
    with pytest.raises(TypeError):
        Attribute(isa=1)

    with pytest.raises(TypeError):
        Attribute(isa=[1, 2, 3])

# Generated at 2022-06-13 07:50:07.038718
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        a = Attribute(default=['a', 'b'])
    except:
        a = None
    assert a is None

    a = Attribute(default=lambda: ['a', 'b'])
    assert a is not None

# Generated at 2022-06-13 07:50:08.046951
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute()


# Generated at 2022-06-13 07:50:12.024713
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='test_isa')
    assert a.isa == 'test_isa'



# Generated at 2022-06-13 07:50:19.139172
# Unit test for constructor of class Attribute
def test_Attribute():
    at = Attribute(
        isa = "string",
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


# An attribute which is only used in the Options class, to automatically assign
# an option to the default connection if it does not belong to any plugin.

# Generated at 2022-06-13 07:50:21.027740
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    attr = FieldAttribute(isa='set', always_post_validate=True, inherit=False)


# Generated at 2022-06-13 07:50:21.952399
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:50:31.498537
# Unit test for constructor of class Attribute
def test_Attribute():

    attrib = Attribute(isa='string')

    assert attrib != None
    assert attrib.isa == 'string'
    assert attrib.private == False
    assert attrib.default == None
    assert attrib.required == False
    assert attrib.listof == None
    assert attrib.priority == 0
    assert attrib.class_type == None
    assert attrib.always_post_validate == False
    assert attrib.inherit == True
    assert attrib.alias == None
    assert attrib.extend == False
    assert attrib.prepend == False
    assert attrib.static == False

# Generated at 2022-06-13 07:50:33.333321
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='string', private=True, default='test', required=True)
    assert a.isa == 'string'
    assert a.private == True
    assert a.default == 'test'
    assert a.required == True
    assert callable(a.default)

# Generated at 2022-06-13 07:50:42.990236
# Unit test for constructor of class Attribute
def test_Attribute():
    class DummyAttribute(Attribute):
        pass

    # Test invalid parameters
    for args in [
            {},
            {'isa': 'dict'},
            {'isa': 'dict', 'listof': 'foo'},
            {'isa': 'dict', 'default': 1},
            {'isa': 'dict', 'default': {}},
            {'isa': 'dict', 'listof': 'list', 'default': {}},
            {'isa': 'list', 'listof': 'foo'},
            {'isa': 'list', 'default': 1},
            {'isa': 'list', 'default': {}},
            {'isa': 'list', 'listof': 'list', 'default': {}},
            ]:
        try:
            attr = DummyAttribute(**args)
        except TypeError:
            pass


# Generated at 2022-06-13 07:50:56.371712
# Unit test for constructor of class Attribute
def test_Attribute():
    # __init__()
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

    # __eq__()
    a1 = Attribute()
    a2 = Attribute()
    assert a1 == a2
    a2.priority = 1
    assert not a1 == a2

    # __ne__()
    assert a1 != a2

    # __lt__()
    assert a2 < a1

    # __gt__()
    assert a1 > a2

    #

# Generated at 2022-06-13 07:50:58.705017
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='string', required=True)
    assert field.isa == 'string'
    assert field.required == True



# Generated at 2022-06-13 07:51:08.310898
# Unit test for constructor of class Attribute

# Generated at 2022-06-13 07:51:16.745700
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='class',
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=1,
        class_type=None,
        always_post_validate=True,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    # Test all properties
    assert a.isa == "class"
    assert a.private == 'private'
    assert a.default is None
    assert a.required == 'required'
    assert a.listof is None
    assert a.priority == 1
    assert a.class_type is None
    assert a.always_post_validate == 'always_post_validate'

# Generated at 2022-06-13 07:51:17.320297
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()

# Generated at 2022-06-13 07:51:27.561058
# Unit test for constructor of class Attribute
def test_Attribute():
    class BigInt(int):
        def __new__(cls, value):
            return super(BigInt, cls).__new__(cls, value + 100)

    class BaseAttr(object):
        thing = FieldAttribute(isa='int')
        alias_thing = FieldAttribute(isa='int', alias='real_alias_thing')
        big_thing = FieldAttribute(isa='int', default=BigInt(12))
        required_thing = FieldAttribute(isa='int', required=True)
        also_required_thing = FieldAttribute(isa='int', required=True)
        not_required_thing = FieldAttribute(isa='int', required=False)
        list_thing = FieldAttribute(isa='list', listof='int')
        big_list_thing = FieldAttribute(isa='list', default=[BigInt(0)])


# Generated at 2022-06-13 07:51:39.295774
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute()
    assert attribute.isa is None
    assert not attribute.private
    assert attribute.default is None
    assert not attribute.required
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert not attribute.always_post_validate
    assert attribute.inherit
    assert attribute.alias is None
    assert not attribute.extend
    assert not attribute.prepend
    assert not attribute.static

    attribute = FieldAttribute(default=True)
    assert attribute.default

    attribute = FieldAttribute(default=[])
    assert attribute.default is not None
    assert attribute.default == []

    attribute = FieldAttribute(default={})
    assert attribute.default is not None
    assert attribute.default == {}

    attribute = FieldAttribute(default=set())

# Generated at 2022-06-13 07:51:51.226573
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    field_py = {
        'isa': 'py',
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
        'static': False
    }


# Generated at 2022-06-13 07:51:58.594230
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # isa
    field_attribute_1 = FieldAttribute(isa='str')
    assert field_attribute_1.isa is str
    # private
    field_attribute_2 = FieldAttribute(private=True)
    assert field_attribute_2.private is True
    # default
    field_attribute_3 = FieldAttribute(default='test')
    assert field_attribute_3.default == 'test'
    # required
    field_attribute_4 = FieldAttribute(required=True)
    assert field_attribute_4.required is True
    # listof
    field_attribute_5 = FieldAttribute(listof='test')
    assert field_attribute_5.listof == 'test'
    # class_type
    class_type = type('', (object,), {})

# Generated at 2022-06-13 07:52:11.415816
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six import string_types

    def _check_object(f, isa=None):
        assert hasattr(f, 'isa')
        assert hasattr(f, 'private')
        assert hasattr(f, 'default')
        assert hasattr(f, 'required')
        assert hasattr(f, 'listof')
        assert hasattr(f, 'priority')
        assert hasattr(f, 'class_type')
        assert hasattr(f, 'always_post_validate')
        assert hasattr(f, 'inherit')
        assert hasattr(f, 'alias')
        assert hasattr(f, 'extend')
        assert hasattr(f, 'prepend')
        assert hasattr(f, 'static')

# Generated at 2022-06-13 07:52:17.715610
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='list', static=False)
    assert a.isa == 'list'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias is None
    assert a.extend == False
    assert a.prepend == False
    assert a.static == False

# Generated at 2022-06-13 07:52:25.197057
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    try:
        b = Attribute(default={'val': 'dict'})
    except:
        b = None
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

    assert b != None

# Generated at 2022-06-13 07:52:26.119214
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()


# Generated at 2022-06-13 07:52:36.392152
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    default_attr = FieldAttribute()
    assert default_attr.isa is None
    assert default_attr.private is False
    assert default_attr.default is None
    assert default_attr.required is False
    assert default_attr.listof is None
    assert default_attr.priority == 0
    assert default_attr.class_type is None
    assert default_attr.always_post_validate is False
    assert default_attr.inherit is True
    assert default_attr.alias is None
    assert default_attr.extend is False
    assert default_attr.prepend is False
    assert default_attr.static is False


# Generated at 2022-06-13 07:52:46.717871
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        isa='bool',
        private=True,
        default=True,
        required=False,
        listof='bool',
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert attr.isa == "bool"
    assert attr.private == True
    assert attr.default == True
    assert attr.required == False
    assert attr.listof == "bool"
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True

# Generated at 2022-06-13 07:52:54.160876
# Unit test for constructor of class Attribute
def test_Attribute():

    # test whether the constructor works fine when set with the
    # given keyword arguments
    attr = Attribute(
        isa='int',
        private=False,
        default=1,
        required=True,
        listof = 'int',
        priority=2,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    assert attr.isa == 'int'
    assert attr.private == False
    assert attr.default == 1
    assert attr.required == True
    assert attr.listof == 'int'
    assert attr.priority == 2
    assert attr.class_type == None
    assert attr.always_post_valid

# Generated at 2022-06-13 07:53:02.845838
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
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
    assert obj.static is False
    assert obj.prepend is False

    obj = FieldAttribute(prepend=True)
    assert obj.prepend is True



# Generated at 2022-06-13 07:53:10.849538
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute().default is None
    assert Attribute().private is False
    assert Attribute().required is False
    assert Attribute().listof is None
    assert Attribute().priority is 0
    assert Attribute().class_type is None
    assert Attribute().always_post_validate is False
    assert Attribute().inherit is True
    assert Attribute().alias is None
    assert Attribute().extend is False
    assert Attribute().prepend is False
    assert Attribute().static is False

# Generated at 2022-06-13 07:53:14.206897
# Unit test for constructor of class Attribute
def test_Attribute():
    contain_default = Attribute(default=())

    if contain_default.default is () or contain_default.default is None:
        pass
    # print('Attribute constructor passed')

if __name__ == '__main__':
    test_Attribute()

# Generated at 2022-06-13 07:53:16.101162
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    x=FieldAttribute()
    print(x.__dict__)


# Generated at 2022-06-13 07:53:20.418642
# Unit test for constructor of class Attribute
def test_Attribute():
    print("Testing constructor for Attribute...", end="")
    try:
        Attribute(default={})
    except TypeError as err:
        print("Passed")
        return True
    print("Failed")
    return False

# Generated at 2022-06-13 07:53:32.466998
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    The following test serves as a sanity check that the constructor of the class
    FieldAttribute works as expected.
    """
    isa = 'string'
    private = True
    default = 'required'
    required = True
    listof = 'str'
    priority = 10
    class_type = str
    always_post_validate = False
    inherit = True
    alias = 'attr_name'
    extend = False
    prepend = False
    static = False

# Generated at 2022-06-13 07:53:42.227875
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = FieldAttribute()
    assert a1.isa == None
    assert a1.private == False
    assert a1.default == None
    assert a1.required == False
    assert a1.listof == None
    assert a1.priority == 0
    assert a1.class_type == None
    assert a1.always_post_validate == False
    assert a1.inherit == True
    assert a1.alias == None
    assert a1.extend == False
    assert a1.prepend == False
    assert a1.static == False


# Generated at 2022-06-13 07:53:54.443715
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='test', private=True, default='test_default', required=True, listof='test_listof',
                                                                                 priority=1, class_type='test_type',
                                                                                 always_post_validate=True,
                                                                                 inherit=False, alias='test_alias')
    assert(fa.isa == 'test')
    assert(fa.private is True)
    assert(fa.default == 'test_default')
    assert(fa.required is True)
    assert(fa.listof == 'test_listof')
    assert(fa.priority == 1)
    assert(fa.class_type == 'test_type')
    assert(fa.always_post_validate is True)
    assert(fa.inherit is False)

# Generated at 2022-06-13 07:53:59.436434
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    tf1 = FieldAttribute("string", True, "hello", True, "string", 0, None, True, True, None)
    attr1 = FieldAttribute("string", True, "hello", True, "string", 0, None, True, True, None)
    assert tf1 == attr1

# Generated at 2022-06-13 07:54:04.589326
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()
    f2 = FieldAttribute(required=True)
    f3 = FieldAttribute(required=True, priority=10)
    f4 = FieldAttribute(required=True, priority=15)
    f5 = FieldAttribute(required=True, priority=10)
    f6 = FieldAttribute(required=True, priority=20)

    assert f1 is not None
    assert f2 is not None
    assert f3 is not None
    assert f4 is not None
    assert f5 is not None
    assert f6 is not None

    assert f1.required is False
    assert f2.required is True
    assert f3.required is True
    assert f4.required is True
    assert f5.required is True
    assert f6.required is True

    assert f1.priority == 0
    assert f2

# Generated at 2022-06-13 07:54:17.206195
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute(False, 'test', True, None, 1, 2, 3, 4, 5, 6, 7, 8)

    # test if isa is set correctly
    assert FA.isa == 'test'

    # test if private is set correctly
    assert FA.private == False

    # test if default is set correctly
    assert FA.default == True

    # test if required is set correctly
    assert FA.required == None

    # test if listof is set correctly
    assert FA.listof == 1

    # test if priority is set correctly
    assert FA.priority == 2

    # test if class_type is set correctly
    assert FA.class_type == 3

    # test if always_post_validate is set correctly
    assert FA.always_post_validate == 4

    # test if inherit is set correctly
    assert FA

# Generated at 2022-06-13 07:54:19.086025
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='foo')
    assert attr.isa == 'foo'



# Generated at 2022-06-13 07:54:29.775457
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute(isa='string', private=False, default='default', required=False, 
                        listof='string', priority=0, class_type=None,
                        always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    assert FA.isa == 'string'
    assert FA.private == False
    assert FA.default == 'default'
    assert FA.required == False
    assert FA.listof == 'string'
    assert FA.priority == 0
    assert FA.class_type == None
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.alias == None
    assert FA.extend == False
    assert FA.prepend == False
    assert FA.static == False

# Generated at 2022-06-13 07:54:31.432695
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = Attribute(isa='dict')
    assert obj.isa == 'dict'



# Generated at 2022-06-13 07:54:45.069044
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    The following unit tests that the FieldAttribute constructor works properly
    """
    # Test defaults for FieldAttribute constructor
    attr = FieldAttribute()
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

    # Test the required parameter for FieldAttribute constructor
    attr = FieldAttribute(required=True)
    assert attr.required

    # Test the isa parameter for FieldAttribute constructor
    attr = FieldAttribute(isa='foo')
    assert attr.isa == 'foo'

    # Test

# Generated at 2022-06-13 07:54:54.029945
# Unit test for constructor of class Attribute
def test_Attribute():
    # test that we raise an error because the default is not a callable but is a container type
    try:
        a = Attribute(default=[])
        raise AssertionError('Should have raised an exception.')
    except TypeError:
        pass

    # test that we can pass in a lambda for a default for a container type
    a = Attribute(default=lambda: [])
    assert a.default == []

    # test that we can pass in a lambda for a default for a non-container type
    a = Attribute(default=lambda: 1)
    assert a.default == 1

    # test that we can pass in a defined function as the default
    def foo():
        return 'foo'
    a = Attribute(default=foo)
    assert a.default == 'foo'

    # test that we can pass in a default that is

# Generated at 2022-06-13 07:55:01.089986
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='freeform')
    assert attr.isa == 'freeform'
    assert attr.private == False
    assert attr.default is None
    assert attr.required == False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias is None
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False


# Generated at 2022-06-13 07:55:18.185170
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # create object field_attribute
    field_attribute = FieldAttribute()
    assert field_attribute
    assert field_attribute.isa == None
    assert field_attribute.private == False
    assert field_attribute.default == None
    assert field_attribute.required == False
    assert field_attribute.listof == None
    assert field_attribute.priority == 0
    assert field_attribute.class_type == None
    assert field_attribute.always_post_validate == False
    assert field_attribute.inherit == True
    assert field_attribute.alias == None
    assert field_attribute.extend == False
    assert field_attribute.prepend == False
    assert field_attribute.static == False


# Generated at 2022-06-13 07:55:28.879023
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr1 = FieldAttribute()
    attr2 = FieldAttribute(isa='str')
    attr3 = FieldAttribute(isa='str', listof=str)
    attr4 = FieldAttribute(isa='str', listof='str')
    attr5 = FieldAttribute(isa='str', listof='str', inherit=False, required=True)
    assert attr1.isa is None
    assert attr2.isa == 'str'
    assert attr3.isa == 'str'
    assert attr3.listof == str
    assert attr4.isa == 'str'
    assert attr4.listof == str
    assert attr5.inherit is False
    assert attr5.required is True


# Generated at 2022-06-13 07:55:42.544343
# Unit test for constructor of class Attribute
def test_Attribute():
    # isa
    a = Attribute(isa='list')
    assert a.isa == list
    a = Attribute(isa='dict')
    assert a.isa == dict
    a = Attribute(isa='set')
    assert a.isa == set
    a = Attribute(isa='str')
    assert a.isa == str
    a = Attribute(isa='int')
    assert a.isa == int
    a = Attribute(isa='float')
    assert a.isa == float
    a = Attribute(isa='bool')
    assert a.isa == bool
    # private
    a = Attribute(private=True)
    assert a.private
    a = Attribute(private=False)
    assert not a.private
    # default
    a = Attribute(default=1)
    assert a.default == 1

# Generated at 2022-06-13 07:55:52.724913
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', private=False, default=None, required=False, listof=None, priority=1, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False)
    assert a.isa == 'dict'
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 1
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False


# Generated at 2022-06-13 07:56:02.384066
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # FieldAttribute(isa=None, private=False, default=None, required=False,
    # listof=None, priority=0, class_type=None, always_post_validate=False,
    # inherit=True, alias=None)
    import pytest

    # defaults
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

    # isa=None
    fa = FieldAttribute(isa="foo")
    assert fa.isa == "foo"

    # private=False

# Generated at 2022-06-13 07:56:09.649464
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    v = FieldAttribute(
        isa='str',
        default='value'
    )
    assert v.isa == 'str'
    assert v.private is False
    assert v.default == 'value'
    assert v.required is False
    assert v.priority == 0
    assert v.class_type is None
    assert v.always_post_validate is False
    assert v.inherit is True
    assert v.alias is None


# Generated at 2022-06-13 07:56:13.214015
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', required=True, listof='dict')
    assert a.isa == 'list'
    assert a.required
    assert a.listof == 'dict'

    a = Attribute()
    assert a.isa is None
    assert not a.required
    assert a.listof is None



# Generated at 2022-06-13 07:56:24.315765
# Unit test for constructor of class Attribute
def test_Attribute():

    import ansible.utils.unsafe_proxy
    def f():
        return True

    a = Attribute()
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

    a = Attribute(isa='int')
    assert a.isa is int
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None

# Generated at 2022-06-13 07:56:27.373999
# Unit test for constructor of class Attribute
def test_Attribute():
    field = Attribute()

    field = Attribute(isa='int', default='test')
    assert(field.isa == 'int')
    assert(field.default == 'test')



# Generated at 2022-06-13 07:56:34.318538
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute()
    assert attribute.isa == None
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
    assert attribute.prepend == False
    assert attribute.static == False

# Generated at 2022-06-13 07:57:08.450777
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Test Attribute with default value,
    Test Attribute with and without default value,
    Test Attribute with mutable default value
    """

    # Test Attribute with default value
    def test_with_default():
        required_attr = Attribute(required=True)
        assert required_attr.required == True

    # Test Attribute with and without default value
    def test_without_default():
        required_attr = Attribute()
        required_attr.required = True
        assert required_attr.required == True

    # Test Attribute with mutable default value
    def test_with_mutable_default():
        import pytest
        with pytest.raises(TypeError):
            Attribute(default=[])

# Generated at 2022-06-13 07:57:14.162143
# Unit test for constructor of class Attribute
def test_Attribute():

    # These are the default values for Attribute
    default_attr = Attribute()
    assert default_attr.isa is None
    assert default_attr.private is False
    assert default_attr.required is False
    assert default_attr.listof is None
    assert default_attr.priority == 0

    # TODO(aisipos): test constructor with a lot of kwargs



# Generated at 2022-06-13 07:57:29.322755
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'integer'
    private = True
    default = None
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False
    extend = False
    prepend = False
    static = False

    attr = Attribute( isa = isa, private = private,
                      default = default, listof = listof,
                      priority = priority, class_type = class_type,
                      always_post_validate = always_post_validate,
                      extend = extend, prepend = prepend, static= static )

    assert attr.isa == isa, 'attr.isa does not match'
    assert attr.private == private, 'attr.private does not match'
    assert attr.default == default, 'attr.default does not match'
    assert attr.list

# Generated at 2022-06-13 07:57:41.007023
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    attr = FieldAttribute(
        private=False,
        default="default",
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        isa=str,
        static=False,
    )

    # isa=str should convert the string value to an AnsibleUnsafeText
    assert isinstance(attr.default, AnsibleUnsafeText)

    # isa=None should not convert the string value
    attr = FieldAttribute(default="default")
    assert isinstance(attr.default, str)

    # default value is not set if isa

# Generated at 2022-06-13 07:57:42.578132
# Unit test for constructor of class Attribute
def test_Attribute():
    t = Attribute()


# Generated at 2022-06-13 07:57:51.416849
# Unit test for constructor of class Attribute
def test_Attribute():
    test_object = Attribute()
    assert isinstance(test_object, Attribute)

    assert test_object.isa is None
    assert test_object.private is False
    assert test_object.default is None
    assert test_object.required is False
    assert test_object.listof is None
    assert test_object.priority == 0
    assert test_object.class_type is None
    assert test_object.always_post_validate is False
    assert test_object.inherit is True
    assert test_object.alias is None
    assert test_object.extend is False
    assert test_object.prepend is False
    assert test_object.static is False

    test_object = Attribute(always_post_validate=True, inherit=False, alias='test_alias')

    assert test_object.always

# Generated at 2022-06-13 07:57:57.774103
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = Attribute(isa='string', private=False, default='foo', required=False, extend=False, always_post_validate=False, inherit=True, alias='bar')
    assert attr.isa == 'string'
    assert attr.private == False
    assert attr.default == 'foo'
    assert attr.required == False
    assert attr.extend == False
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == 'bar'

# Generated at 2022-06-13 07:58:09.194734
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # testing empty object
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

    # testing non-empty object

# Generated at 2022-06-13 07:58:15.673088
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
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

# Generated at 2022-06-13 07:58:21.864731
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute()
    assert attribute.isa == None
    assert attribute.private == False
    assert attribute.default == None
    assert attribute.required == False
    assert attribute.listof == None
    assert attribute.priority == 0
    assert attribute.class_type == None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.extend == False
    assert attribute.extend == False
    assert attribute.prepend == False
