

# Generated at 2022-06-13 07:49:13.184190
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='str')
    assert a.isa == 'str'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.always_post_validate is False

    a = FieldAttribute(isa='str', private=True, default='foo', required=True, always_post_validate=True)
    assert a.isa == 'str'
    assert a.private is True
    assert a.default == 'foo'
    assert a.required is True
    assert a.listof is None
    assert a.priority == 0
    assert a.always_post_validate is True


# like the list() function, constructs a copy

# Generated at 2022-06-13 07:49:23.792049
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test default constructor
    test_attr = Attribute()
    assert test_attr.isa == None
    assert test_attr.private == False
    assert test_attr.default == None
    assert test_attr.required == False
    assert test_attr.listof == None
    assert test_attr.priority == 0
    assert test_attr.class_type == None
    assert test_attr.always_post_validate == False
    assert test_attr.inherit == True

    # Test all arguments constructor

# Generated at 2022-06-13 07:49:25.723406
# Unit test for constructor of class Attribute
def test_Attribute():
    with pytest.raises(TypeError):
        Attribute(default=dict(), isa='list')

# Generated at 2022-06-13 07:49:27.363380
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='dict', inherit=False)
    assert isinstance(a, FieldAttribute)



# Generated at 2022-06-13 07:49:29.922776
# Unit test for constructor of class Attribute
def test_Attribute():
    my_attr = Attribute(isa='int')
    assert my_attr.isa == 'int'


# Generated at 2022-06-13 07:49:38.181396
# Unit test for constructor of class Attribute
def test_Attribute():

    def try_init(isa, private, default, required, listof, priority, class_type, always_post_validate,
                 inherit, alias, extend, prepend, static):
        try:
            Attribute(isa=isa, private=private, default=default, required=required, listof=listof, priority=priority,
                      class_type=class_type, always_post_validate=always_post_validate, inherit=inherit,
                      alias=alias, extend=extend, prepend=prepend, static=static)
        except TypeError:
            print("Attribute initializer failed")


# Generated at 2022-06-13 07:49:43.825075
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    if not isinstance(FieldAttribute(
        default='value',
        isa='str',
        private=True,
        required=True,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=None,
    ), FieldAttribute):
        raise Exception()

# Generated at 2022-06-13 07:49:51.323006
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from collections import OrderedDict
    fa = FieldAttribute(
        isa = "test",
        private = False,
        default = None,
        required = False,
        listof = None,
        class_type = None,
        always_post_validate = False,
        inherit = True,
        alias = None,
    )
    # __init__ sets OrderedDict() as data structure
    assert isinstance(fa.__dict__, OrderedDict)



# Generated at 2022-06-13 07:50:04.516812
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(
        isa='str',
        private=False,
        default='localhost',
        required=True,
        listof=None,
        priority=0,
        always_post_validate=True,
        alias=None,
    )
    assert attr.isa == 'str'
    assert attr.default == 'localhost'
    # Note: attr.required can be True or False, since it's a function.
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.always_post_validate is True
    assert attr.alias is None
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False

# Generated at 2022-06-13 07:50:15.411207
# Unit test for constructor of class Attribute
def test_Attribute():
    # test default attributes
    a = Attribute()
    assert a.isa is None
    assert a.private is None
    assert a.default is None
    assert a.required is None
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is None
    assert a.inherit is None
    assert a.alias is None
    assert a.static is None

    # test override attributes
    b = Attribute(isa='string', private=True, default='abc', required=True, listof='list',
        priority=9, class_type='class', always_post_validate=True, inherit=True, alias='xxx',
        extend=True, prepend=False, static=False)
    assert b.isa == 'string'


# Generated at 2022-06-13 07:50:19.565462
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='list',
        private=True,
        default=None,
        required=True,
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



# Generated at 2022-06-13 07:50:22.167471
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    _f = FieldAttribute(isa='int', default=0, required=True)
    assert _f.isa == 'int'
    assert _f.default == 0
    assert _f.required == True



# Generated at 2022-06-13 07:50:27.508160
# Unit test for constructor of class Attribute
def test_Attribute():
    test = Attribute(required=True,default='hello')
    assert(test.required == True)
    assert(test.default == 'hello')
    try:
        Attribute(default={})
    except TypeError:
        pass
    else:
        assert False, 'defaults for FieldAttribute may not be mutable'


# Generated at 2022-06-13 07:50:38.757087
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test basic initialization
    assert Attribute().isa is None
    assert Attribute().private is False
    assert Attribute().default is None
    assert Attribute().required is False
    assert Attribute().listof is None
    assert Attribute().priority == 0
    assert Attribute().class_type is None
    assert Attribute().always_post_validate is False
    assert Attribute().inherit is True

    # Test that specifying isa, private, required and inherit sets the correct
    # attributes, and sets all other attributes to the defaults
    assert Attribute(
        isa='list',
        private=True,
        required=True,
        inherit=False,
    ).isa == 'list'

# Generated at 2022-06-13 07:50:52.632522
# Unit test for constructor of class Attribute
def test_Attribute():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Inventory
    from ansible.vars import VariableManager
    attr = Attribute(isa='list')
    assert attr.isa == 'list'
    assert attr.listof is None
    attr = Attribute(isa='list', listof='int')
    assert attr.isa == 'list'
    assert attr.listof == 'int'
    attr = Attribute(isa='list', default=[])
    assert attr.isa == 'list'
    assert attr.default == []
    attr = Attribute(isa='list', default=())
    assert attr.isa == 'list'
    assert attr.default == ()
    assert attr.default is not ()

# Generated at 2022-06-13 07:51:03.907779
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Pass valid values
    FieldAttribute('str', False, 'mytext', False, 'str')
    FieldAttribute('str', False, 'mytext', False, None)
    FieldAttribute('str', False, ('mytext'), True, 'list')
    FieldAttribute('str', False, ['mytext'], True, 'list')
    FieldAttribute('str', False, {'mytext': 'one'}, True, 'dict')
    FieldAttribute('str', False, set(['mytext']), True, 'set')
    # Pass invalid values
    # constructor raises exception if isa is None
    try:
        FieldAttribute(None, False, 'mytext', False, 'str')
        assert False
    except TypeError:
        pass

    # constructor raises exception if isa is not a String

# Generated at 2022-06-13 07:51:14.410192
# Unit test for constructor of class Attribute
def test_Attribute():
    import sys

    # Call constructor with empty arguments.
    attr_obj = Attribute()

    print(attr_obj.isa)
    print(attr_obj.private)
    print(attr_obj.default)
    print(attr_obj.required)
    print(attr_obj.listof)
    print(attr_obj.priority)
    print(attr_obj.class_type)
    print(attr_obj.always_post_validate)
    print(attr_obj.inherit)
    print(attr_obj.alias)
    print(attr_obj.extend)
    print(attr_obj.prepend)
    print(attr_obj.static)

    # Call constructor with arguments.
    # The argument 'isa' is a string.
    attr_obj = Attribute(isa = 'isa')

# Generated at 2022-06-13 07:51:21.084487
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()
    assert fa.isa is None
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


# Generated at 2022-06-13 07:51:30.825914
# Unit test for constructor of class Attribute
def test_Attribute():
    att = Attribute()
    assert att.isa is None
    assert att.private is False
    assert att.default is None
    assert att.required is False
    assert att.listof is None
    assert att.priority == 0
    assert att.class_type is None
    assert att.always_post_validate is False
    assert att.inherit is True

    att = Attribute(isa="str")
    assert att.isa == "str"
    assert att.private is False
    assert att.default is None
    assert att.required is False
    assert att.listof is None
    assert att.priority == 0
    assert att.class_type is None
    assert att.always_post_validate is False
    assert att.inherit is True


# Generated at 2022-06-13 07:51:41.796950
# Unit test for constructor of class Attribute
def test_Attribute():
    data = dict(isa='isa')
    _ = Attribute(**data)
    data = dict(isa='isa', private=True)
    _ = Attribute(**data)
    data = dict(isa='isa', private=True, default='default')
    _ = Attribute(**data)
    data = dict(isa='isa', private=True, default='default', required=True)
    _ = Attribute(**data)
    data = dict(isa='isa', private=True, default='default', required=True, listof=1)
    _ = Attribute(**data)
    data = dict(isa='isa', private=True, default='default', required=True, listof=1,
                priority=0)
    _ = Attribute(**data)

# Generated at 2022-06-13 07:51:51.507611
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute(isa="int")
    obj2 = Attribute(isa="int", default=1)
    assert (obj.default is None)
    assert obj.always_post_validate is False
    assert obj.inherit
    assert obj.extend is False
    assert obj.prepend is False
    assert obj.static is False
    assert obj2.default == 1
    assert obj2.always_post_validate is False
    assert obj2.inherit
    assert obj2.extend is False
    assert obj2.prepend is False



# Generated at 2022-06-13 07:51:55.272606
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_attr = FieldAttribute('str', default='foo', always_post_validate=True, inherit=False)
    assert test_attr.isa == 'str'
    assert test_attr.default == 'foo'
    assert test_attr.always_post_validate is True
    assert test_attr.inherit is False



# Generated at 2022-06-13 07:51:58.700648
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa="str", required=True, inherit=False, alias="name")
    assert attr.isa == "str"
    assert attr.private == False
    assert attr.default is None
    assert attr.required == True
    assert attr.priority == 0
    assert attr.inherit == False
    assert attr.alias == "name"



# Generated at 2022-06-13 07:52:11.515782
# Unit test for constructor of class Attribute
def test_Attribute():
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

    attr = Attribute(isa, private, default, required, listof, priority, class_type, always_post_validate, inherit, alias,
                     extend, prepend, static)

    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False

# Generated at 2022-06-13 07:52:16.187888
# Unit test for constructor of class Attribute
def test_Attribute():
    # Default constructor
    attr = Attribute()
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert not attr.always_post_validate
    assert attr.inherit is True

    # Invalid default value
    try:
        Attribute(default=dict())
        assert False, 'Expected TypeError'
    except TypeError:
        pass

    # Valid default value
    try:
        Attribute(default=lambda: dict())
    except TypeError:
        assert False, 'Unexpected TypeError'

    # Not subclassing Attribute

# Generated at 2022-06-13 07:52:19.187425
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(isa='class')
    assert attribute.isa == 'class'



# Generated at 2022-06-13 07:52:24.435138
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int')
    assert attr.isa == 'int'
    assert isinstance(attr, Attribute)

    # Python 3 compatibility test:
    attr2 = Attribute(isa='int')
    assert attr == attr2
    assert attr != attr2
    assert attr < attr2
    assert attr > attr2
    assert attr <= attr2
    assert attr >= attr2


# Generated at 2022-06-13 07:52:33.181966
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """Function to test the FieldAttribute class.

    Checks that default values are correctly set and that all
    parameters are correctly set.
    """
    # test defaults
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
    assert attribute.alias == None
    assert attribute.extend == False
    assert attribute.prepend == False
    assert attribute.static == False
    # test setting values

# Generated at 2022-06-13 07:52:38.738780
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.private == False
    assert attr.required == False
    assert attr.inherit == True
    attr = Attribute(private=True)
    assert attr.private == True
    attr = Attribute(required=True)
    assert attr.required == True
    attr = Attribute(inherit=False)
    assert attr.inherit == False
    attr = Attribute(private=True, required=True, inherit=False)
    assert attr.private == True
    assert attr.required == True
    assert attr.inherit == False


# Generated at 2022-06-13 07:52:39.959796
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='list', listof='dict')



# Generated at 2022-06-13 07:52:45.815143
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute()
    assert foo
    assert foo.isa == None
    assert foo.required == False
    assert foo.class_type == None
    return True
# Unit test class Attribute  END

# Generated at 2022-06-13 07:52:53.650073
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    # if the method do not throw exceptions, they works
    attr = FieldAttribute(isa='list')
    attr = FieldAttribute(isa='list', listof='int')
    attr = FieldAttribute(isa='list', default=[])
    attr = FieldAttribute(isa='list', default=lambda: [])
    attr = FieldAttribute(isa='list', alias='fuz')
    attr = FieldAttribute(isa='list', inherit=False)
    attr = FieldAttribute(isa='list', class_type='str')
    attr = FieldAttribute(isa='list', extend=True)
    attr = FieldAttribute(isa='list', prepend=True)
    attr = FieldAttribute(isa='list', static=True)



# Generated at 2022-06-13 07:52:57.433319
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='str', private=True, default='test_default')

    assert attr.isa == 'str'
    assert attr.private == True
    assert attr.default == 'test_default'



# Generated at 2022-06-13 07:53:07.293312
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # Variable to hold the instance of object FieldAttribute
    obj_atr = []

    # create an object of class FieldAttribute and pass the following parameters
    obj_atr.append( FieldAttribute(isa='str', class_type=str, private=False, default=None, listof=None,
                    priority=0, always_post_validate=False, inherit=True, alias=None, static=False))

    # Test the isa variable of class FieldAttribute
    assert obj_atr[0].isa == 'str'

    # Test the class_type variable of class FieldAttribute
    assert obj_atr[0].class_type == str

    # Test the isa variable of class FieldAttribute
    assert obj_atr[0].private == False

    # Test the default variable of class FieldAttribute

# Generated at 2022-06-13 07:53:17.013970
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='dict')
    assert attr.isa == 'dict'
    attr = Attribute(isa='list', listof='bool')
    assert attr.isa == 'list'
    assert attr.listof == 'bool'
    attr = Attribute(isa='list', listof='basestring')
    assert attr.isa == 'list'
    assert attr.listof == 'basestring'
    attr = Attribute(isa='list', listof='complex')
    assert attr.isa == 'list'
    assert attr.listof == 'complex'
    attr = Attribute(isa='list', listof='dict')
    assert attr.isa == 'list'
    assert attr.listof == 'dict'

# Generated at 2022-06-13 07:53:30.353242
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # constructor of FieldAttribute
    field_attribute = FieldAttribute()

    # attributes of FieldAttribute
    assert field_attribute.isa is None
    assert isinstance(field_attribute.private, bool)
    assert field_attribute.default is None
    assert isinstance(field_attribute.required, bool)
    assert field_attribute.listof is None
    assert field_attribute.priority == 0
    assert field_attribute.class_type is None
    assert isinstance(field_attribute.always_post_validate, bool)
    assert field_attribute.inherit is True
    assert field_attribute.alias is None
    assert field_attribute.extend is False
    assert field_attribute.prepend is False
    assert field_attribute.static is False



# Generated at 2022-06-13 07:53:40.386680
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.module_utils.six import string_types
    a = FieldAttribute(
        isa = 'str',
        private = True,
        default = 'default',
        required = False,
        listof = 'str',
        priority = 0,
        class_type = 'str',
        always_post_validate = True,
        alias = 'test_alias'
    )

    assert a.isa == 'str'
    assert a.private == True
    assert a.default == 'default'
    assert a.required == False
    assert a.listof == 'str'
    assert a.priority == 0
    assert a.class_type == 'str'
    assert a.always_post_validate == True
    assert a.alias == 'test_alias'

# Generated at 2022-06-13 07:53:51.826568
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa='str',
    )
    a = FieldAttribute(
        isa='str',
        default='default',
    )
    a = FieldAttribute(
        isa='str',
        default=[],
    )
    a = FieldAttribute(
        isa='list',
        default=[],
    )
    a = FieldAttribute(
        isa='list',
        default=copy,
    )


# TODO: To be removed post 2.2.  This is deprecated as of 2.2, replaced with specific field attributes
# class BaseAttributes(object):
#     """
#     Contains common attributes and functions.
#     """
#     _name         = FieldAttribute(isa='string')
#     _parent       = FieldAttribute(isa='string')
#     _role         = FieldAttribute(isa

# Generated at 2022-06-13 07:53:58.056307
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # call FieldAttribute with valid parameters
    result = FieldAttribute(isa='string', private=False, default=None, required=False,
                    listof='string', priority=0, class_type=None, always_post_validate=False,
                    inherit=True, alias=None, extend=False, prepend=False, static=False)

    assert isinstance(result, FieldAttribute)

    # call FieldAttribute with invalid parameters
    try:
        result = FieldAttribute(isa='list', private=True, default={}, required=False,
                    listof='string', priority=0, class_type=None, always_post_validate=False,
                    inherit=True, alias=None, extend=False, prepend=False, static=False)
    except TypeError:
        pass
    except Exception as e:
        raise e

# Generated at 2022-06-13 07:53:59.049823
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()


# Generated at 2022-06-13 07:54:14.037740
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import unittest
    import tempfile
    import os

    class TestFieldAttribute(unittest.TestCase):

        def test_init(self):
            attr_init = Attribute()

            self.assertEqual(attr_init.isa, None)
            self.assertEqual(attr_init.private, False)
            self.assertEqual(attr_init.default, None)
            self.assertEqual(attr_init.required, False)
            self.assertEqual(attr_init.listof, None)
            self.assertEqual(attr_init.priority, 0)
            self.assertEqual(attr_init.always_post_validate, False)
            self.assertEqual(attr_init.inherit, True)
            self.assertEqual(attr_init.alias, None)

# Generated at 2022-06-13 07:54:22.672130
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(isa='int', default=0)
    assert attribute.isa == 'int'
    assert attribute.private == False
    assert attribute.default == 0
    assert attribute.required == False
    assert attribute.listof == None
    assert attribute.priority == 0
    assert attribute.class_type == None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True

    # Check Attribute.__eq__ is correct
    assert (attribute == Attribute(isa='int', default=0))
    assert (not attribute == Attribute(isa='int', default=1))

    # Check Attribute.__ne__ is correct
    assert (attribute != Attribute(isa='int', default=1))
    assert (not attribute != Attribute(isa='int', default=0))

    # Check Attribute.

# Generated at 2022-06-13 07:54:32.701726
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # One of the fields (isa) not specified so should be None
    assert FieldAttribute().isa is None
    # One of the fields (isa) specified, should be set to the value
    assert FieldAttribute(isa='str').isa == 'str'
    # One of the fields (private) specified, should be set to the value
    assert FieldAttribute(private=True).private == True
    # All fields specified, should be exactly equal
    fa = FieldAttribute(isa='str', private=True, default='test', required=True, listof=True, priority=10, class_type=True,
                        always_post_validate=True, inherit=True, alias='test', extend=True, prepend=True, static=True)
    assert fa.isa == 'str'
    assert fa.private == True
    assert fa.default == 'test'
   

# Generated at 2022-06-13 07:54:46.169385
# Unit test for constructor of class Attribute
def test_Attribute():

    test_kwargs = {
        'isa': 'class',
        'private': False,
        'default': 'abc',
        'required': False,
        'listof': 'abc',
        'priority': 0,
        'class_type': 'abc',
        'always_post_validate': False,
        'inherit': True,
        'alias': 'abc',
        'extend': True,
        'prepend': True,
    }

    # test required kwargs
    Attribute()

    # test all kwargs
    Attribute(**test_kwargs)

    # test duplicate kwarg
    try:
        Attribute(**copy(test_kwargs), isa='dict', listof='dict')
    except TypeError as e:
        assert 'got multiple values for keyword argument' in str

# Generated at 2022-06-13 07:54:56.401446
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute_1 = FieldAttribute()
    assert field_attribute_1
    assert field_attribute_1.isa == None
    assert field_attribute_1.private == False
    assert field_attribute_1.default == None
    assert field_attribute_1.required == False
    assert field_attribute_1.listof == None
    assert field_attribute_1.priority == 0
    assert field_attribute_1.class_type == None
    assert field_attribute_1.always_post_validate == False
    assert field_attribute_1.inherit == True
    assert field_attribute_1.alias == None
    assert field_attribute_1.extend == False
    assert field_attribute_1.prepend == False
    assert field_attribute_1.static == False


# Generated at 2022-06-13 07:54:57.532561
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()
    assert isinstance(fa, FieldAttribute)

# Generated at 2022-06-13 07:55:07.707048
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """ ensure the constructor of FieldAttribute throws TypeError if the default is mutable but not a callable """
    class MyAttr():
        def __init__(self):
            self.default_list = []
            self.default_dict = {}
            self.default_callable = lambda: 'default'
            self.default_string = 'default'

        def __str__(self):
            return self.name

    class MyAttr2():
        def __init__(self):
            self.default_list = []
            self.default_dict = {}
            self.default_callable = lambda: 'default'
            self.default_string = 'default'

        def __str__(self):
            return self.name

    a = FieldAttribute(isa='list', default=MyAttr().default_list)
    b = FieldAttribute

# Generated at 2022-06-13 07:55:16.821649
# Unit test for constructor of class Attribute
def test_Attribute():

    # Valid isa
    _Attribute = Attribute(isa='dict')
    assert not _Attribute.private
    assert _Attribute.default is None
    assert not _Attribute.required
    assert _Attribute.listof == None
    assert _Attribute.priority == 0
    assert _Attribute.class_type == None
    assert not _Attribute.always_post_validate
    assert _Attribute.inherit
    assert _Attribute.alias is None
    assert not _Attribute.extend
    assert not _Attribute.prepend
    assert not _Attribute.static

    try:
        _Attribute = Attribute(isa='mutable')
    except Exception:
        pass
    else:
        assert False, "constructor should raise an exception"

    # Private parameter
    _Attribute = Attribute(private=True)
    assert _Attribute.private

    # Default

# Generated at 2022-06-13 07:55:28.827916
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'list'
    private = False
    default = None
    required = False
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False
    inherit = True
    alias = ''
    extend = False
    prepend = False
    static = False
    a = Attribute(isa, private, default, required, listof, priority, class_type, always_post_validate, inherit, alias, extend, prepend, static)
    assert a.isa == isa
    assert a.private == private
    assert a.default == default
    assert a.required == required
    assert a.listof == listof
    assert a.priority == priority
    assert a.class_type == class_type
    assert a.always_post_validate == always_post_validate

# Generated at 2022-06-13 07:55:31.477596
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    attr = FieldAttribute(isa='str', private=True)
    assert attr is not None



# Generated at 2022-06-13 07:55:45.170817
# Unit test for constructor of class Attribute
def test_Attribute():
    # constructor
    assert(Attribute(isa='dict', private=False, required=False, default=None, inherit=True, priority=0,
                     always_post_validate=False, alias=None).isa=='dict')
    # test priority
    assert(Attribute(isa='list', priority=1)==Attribute(isa='list', priority=1))
    assert(Attribute(isa='list', priority=1)!=Attribute(isa='list', priority=2))
    assert(Attribute(isa='list', priority=10)<Attribute(isa='list', priority=20))
    assert(Attribute(isa='list', priority=10)<=Attribute(isa='list', priority=20))
    assert(Attribute(isa='list', priority=10)>Attribute(isa='list', priority=1))

# Generated at 2022-06-13 07:55:53.311095
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test with default constructor
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



# Generated at 2022-06-13 07:56:02.904028
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test: boolean, no default but require
    attr_boolean_nodefault = Attribute(isa='boolean', required=True)
    assert attr_boolean_nodefault is not None
    assert attr_boolean_nodefault.isa == 'boolean'
    assert attr_boolean_nodefault.default is None
    assert attr_boolean_nodefault.required is True

    # Test: string, defaulted, not required
    attr_string_default = Attribute(isa='string', default='Happy Valley')
    assert attr_string_default is not None
    assert attr_string_default.isa == 'string'
    assert attr_string_default.default == 'Happy Valley'
    assert attr_string_default.required is False
    assert attr

# Generated at 2022-06-13 07:56:14.505775
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr is not None


TASK_ATTRIBUTE = Attribute(priority=10)
DELEGATE_TO = FieldAttribute(priority=50, always_post_validate=True)
BLOCK = Attribute(priority=10)
BLOCKS = Attribute(priority=10)
RESCUE = Attribute(priority=10)
ALWAYS = Attribute(priority=10)
ANY_ERRORS_FATAL = Attribute(priority=10)
ANY_ERRORS_WARN = Attribute(priority=10)
FAILED_WHEN = Attribute(priority=10)
UNTIL = Attribute(priority=10)
WHEN = Attribute(priority=10)
RETRY = Attribute(priority=10)

# Generated at 2022-06-13 07:56:22.394904
# Unit test for constructor of class Attribute
def test_Attribute():
    attr1 = Attribute(3, 44, 56, 'elz')
    assert attr1.isa == 3
    assert attr1.private == 44
    assert attr1.default == 56
    assert attr1.required == 'elz'
    assert attr1.listof == None
    assert attr1.priority == 0
    assert attr1.class_type == None
    assert attr1.always_post_validate == False
    assert attr1.inherit == True
    assert attr1.alias == None

# Generated at 2022-06-13 07:56:28.631084
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()

    # Confirm that default values of instantiated class are correct
    assert(a.isa is None)
    assert(a.private == False)
    assert(a.default is None)
    assert(a.required == False)
    assert(a.listof is None)
    assert(a.priority == 0)
    assert(a.class_type is None)
    assert(a.always_post_validate == False)
    assert(a.inherit == True)
    assert(a.alias is None)

    # Test setting isa
    b = Attribute(isa='foo')
    assert(b.isa == 'foo')

    # Test setting private
    c = Attribute(private=True)
    assert(c.private is True)

    # Test setting default

# Generated at 2022-06-13 07:56:37.632765
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Constructor exception
    try:
        attr = FieldAttribute(default={}, isa='list')
    except TypeError:
        pass
    else:
        raise RuntimeError('FieldAttribute default must be immutable')

    # Constructor
    attr = FieldAttribute(isa='list')
    assert attr is not None
    assert attr.isa == 'list'

    # Initialize from dict
    dictattr = Attribute.from_dict(dict(isa='list'))
    assert dictattr is not None
    assert dictattr.isa == 'list'

    # Test comparison operators
    assert attr == dictattr
    assert attr != dictattr
    assert attr == dictattr
    assert attr <= dictattr
    assert attr >= dictattr
    assert attr < dictattr
    assert attr > dictattr

# Generated at 2022-06-13 07:56:46.684894
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # FieldAttribute shows: copy, deepcopy, pickle, cmp
    fa1 = FieldAttribute(is_a="list", listof=int)
    fa2 = FieldAttribute(is_a="list", listof=int)
    assert fa1 == fa2
    assert fa1 is not fa2
    fc1 = copy(fa1)
    fc2 = deepcopy(fa1)
    assert fa1 == fc1
    assert fa1 is not fc1
    assert fc1 is not fc2
    assert fa1 == fc2
    assert fa1 is not fc2

# Generated at 2022-06-13 07:56:55.548589
# Unit test for constructor of class Attribute
def test_Attribute():
    # TODO: not working yet
    def my_default_list():
        return []

    def my_default_dict():
        return {}

    attr = Attribute(isa='str', default='default')
    assert attr.isa == 'str'
    assert attr.default == 'default'
    assert attr.private == False
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


# Generated at 2022-06-13 07:56:58.295862
# Unit test for constructor of class Attribute
def test_Attribute():
    # base case
    with pytest.raises(TypeError):
        Attribute(default='hello')

    # should not raise exception
    Attribute(default=lambda: 'hello')

    # should raise exception
    with pytest.raises(TypeError):
        Attribute(default=['hello'])

# Generated at 2022-06-13 07:57:17.065493
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    '''
    Unit test for constructor of class FieldAttribute
    '''

    FA = FieldAttribute()

    FA.isa = 'test'
    FA.private = False
    FA.default = 1
    FA.required = True
    FA.listof = 2
    FA.priority = 0
    FA.class_type = 'class'
    FA.always_post_validate = False
    FA.inherit = True
    FA.alias = 'alias'
    FA.extend = False
    FA.prepend = False
    FA.static = False


# Generated at 2022-06-13 07:57:26.269675
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
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.alias is None
    assert a.extend is False
    assert a.prepend is False
    assert a.static is False


# Generated at 2022-06-13 07:57:34.180300
# Unit test for constructor of class Attribute
def test_Attribute():
    # test class Attribute
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

    b = Attribute(isa='list', private=True, required=True, listof='dict', priority=1)
    assert b.isa == 'list'
    assert b.private == True
    assert b.default == None
    assert b.required == True
    assert b.listof == 'dict'
    assert b.priority == 1

# Generated at 2022-06-13 07:57:40.413329
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='list',
        private=False,
        default=[],
        required=False,
        listof='str',
        priority=0,
        inherit=True,
    )
    assert fa.isa == 'list' and fa.private == False and fa.default == [] and fa.required == False and fa.listof == 'str' and fa.priority == 0 and fa.inherit == True


# Generated at 2022-06-13 07:57:43.061106
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(default=2)
    assert a.default == 2

############################################################################
#
# NOW, some more specialized Attributes for fields.  Some of these may
# be merged back into the class Attribute above at some point in the future
# or some syntax may be devised to allow them to exist at the same time.
#
############################################################################



# Generated at 2022-06-13 07:57:51.784869
# Unit test for constructor of class Attribute
def test_Attribute():

    class Foo(object): pass

    f = Attribute()
    assert f is not None
    assert f.isa is None
    assert f.default is None
    assert not f.required
    assert f.listof is None
    assert f.priority == 0
    assert f.class_type is None
    assert not f.always_post_validate
    assert f.inherit
    assert f.alias is None

    # test isa
    f = Attribute(isa=int)
    assert f is not None
    assert f.isa == int
    f = Attribute(isa='int')
    assert f.isa == int
    f = Attribute(isa=float)
    assert f.isa == float
    f = Attribute(isa='float')
    assert f.isa == float
    f = Attribute(isa=str)

# Generated at 2022-06-13 07:58:02.754218
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa=bool,
        default=False,
        private=False,
        required=True,
        listof=dict,
        priority=1000,
        always_post_validate=False,
        class_type=dict,
        inherit=False,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    print(a.isa)
    print(a.private)
    print(a.required)
    print(a.default)
    print(a.listof)
    print(a.priority)
    print(a.always_post_validate)
    print(a.inherit)
    print(a.alias)
    print(a.class_type)
    print(a.extend)
    print

# Generated at 2022-06-13 07:58:04.619434
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='int')
    assert(attr.isa == 'int')


# Generated at 2022-06-13 07:58:14.092304
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()

    assert (field_attribute.isa == None)
    assert (field_attribute.private == False)
    assert (field_attribute.default == None)
    assert (field_attribute.required == False)
    assert (field_attribute.listof == None)
    assert (field_attribute.priority == 0)
    assert (field_attribute.class_type == None)
    assert (field_attribute.always_post_validate == False)
    assert (field_attribute.inherit == True)
    assert (field_attribute.alias == None)
    assert (field_attribute.extend == False)
    assert (field_attribute.prepend == False)
    assert (field_attribute.static == False)


# Generated at 2022-06-13 07:58:19.550659
# Unit test for constructor of class Attribute
def test_Attribute():
    assert(Attribute(isa='list', required=True) == Attribute(isa='list', required=True))
    assert(Attribute(isa='list', required=True) != Attribute(isa='list', required=False))
    assert(Attribute(isa='list', required=True) < Attribute(isa='list', required=False))
    assert(Attribute(isa='list', required=True) <= Attribute(isa='list', required=True))

# Generated at 2022-06-13 07:58:49.460962
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', default=list)
    if a.isa != 'list' or a.default != list:
        raise Exception("Attribute constructor is broken")



# Generated at 2022-06-13 07:58:57.588844
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(
        isa='dict',
        private=True,
        default=None,
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
    )

    assert attr.isa == 'dict'
    assert attr.private == True
    assert attr.default is None
    assert attr.required == False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias is None

