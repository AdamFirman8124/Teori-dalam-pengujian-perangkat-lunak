

# Generated at 2022-06-13 07:49:03.250321
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FieldAttribute(isa=None, private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)

# Generated at 2022-06-13 07:49:13.916157
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    def default_fn():
        return {'foo':'bar'}
    fa = FieldAttribute(
        isa='str',
        private=False,
        default=default_fn,
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
    assert fa.isa == 'str'
    assert fa.default() == {'foo':'bar'}

# Generated at 2022-06-13 07:49:14.750898
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass

# Generated at 2022-06-13 07:49:23.219356
# Unit test for constructor of class Attribute
def test_Attribute():

    # ensure that the tests don't modify the class
    ba = deepcopy(Attribute)

    # test validation code
    def test_validation(name, ba, values):
        for value in values:
            v = copy(ba)
            setattr(v, name, value)
            if hasattr(v, '_validate_' + name):
                getattr(v, '_validate_' + name)()
            else:
                assert True

    # test syntax for isa
    test_validation('isa', ba, ('string', 'int', 'boolean', 'dict', 'list'))

    # test syntax for private
    test_validation('private', ba, (True, False))

    # test syntax for required
    test_validation('required', ba, (True, False))

    # test syntax for inherit
   

# Generated at 2022-06-13 07:49:29.973459
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str',
                     private=False,
                     default='default',
                     priority=10,
                     class_type=str,
                     always_post_validate=False)
    assert(attr.isa == 'str')
    assert(not attr.private)
    assert(attr.default == 'default')
    assert(attr.priority == 10)
    assert(attr.class_type == str)
    assert(not attr.always_post_validate)

# Generated at 2022-06-13 07:49:30.899511
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert Attribute()
    assert FieldAttribute()



# Generated at 2022-06-13 07:49:37.179478
# Unit test for constructor of class Attribute
def test_Attribute():
    myattr = Attribute(isa='dict')
    assert myattr.isa == 'dict'
    assert myattr.private == False
    assert myattr.default == None
    assert myattr.required == False
    assert myattr.listof == None
    assert myattr.priority == 0
    assert myattr.class_type == None
    assert myattr.always_post_validate == False
    assert myattr.inherit == True
    assert myattr.alias == None
    assert myattr.extend == False
    assert myattr.static == False
    assert myattr.prepend == False


# Generated at 2022-06-13 07:49:38.693632
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    a = Attribute(isa='str')


# Generated at 2022-06-13 07:49:39.487600
# Unit test for constructor of class Attribute
def test_Attribute():
    pass


# Generated at 2022-06-13 07:49:51.128217
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(
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
        extend=False,
        prepend=False,
        static=False,
    )
    assert field_attribute.isa == 'dict' and field_attribute.private == True \
        and field_attribute.default == None and field_attribute.required == False \
        and field_attribute.listof == None and field_attribute.priority == 0 \
        and field_attribute.class_type == None and field_attribute.always_post_validate == False \
        and field_attribute.inherit == True and field

# Generated at 2022-06-13 07:50:01.882835
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str',
                  private=False,
                  default='nothing',
                  required=False,
                  listof='str',
                  priority=0,
                  class_type='str',
                  always_post_validate=False,
                  inherit=True,
                  alias='str',
                  extend=False,
                  prepend=False,
                  static=False,
                  )
    assert isinstance(a, Attribute)


# Unit test to verify that 'data' is not a mutable default parameter

# Generated at 2022-06-13 07:50:10.416424
# Unit test for constructor of class Attribute
def test_Attribute():

    # No value for required
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
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False

    # All values set

# Generated at 2022-06-13 07:50:14.200938
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
    assert type(obj) == FieldAttribute
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


# Generated at 2022-06-13 07:50:18.749764
# Unit test for constructor of class Attribute
def test_Attribute():
    def d():
        return dict(a=1)
    # We used to have an error 'defaults for FieldAttribute may not be mutable'
    # This is no longer true and we are passing these tests.
    a = Attribute(isa=dict, default=d)
    assert a.isa is dict
    assert a.default() == dict(a=1)

# Generated at 2022-06-13 07:50:29.309809
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Initializes an object of class FieldAttribute
    f = FieldAttribute(isa='dict', default=None, required=False, listof=None, priority=100, \
            class_type=None, inherit=True, alias=None, extend=False, prepend=False)
    # The attribute should be a dict
    assert f.isa == 'dict'
    # In the beginning, it should be NONE
    assert f.default is None
    # The attribute is not required
    assert not f.required
    # The attribute is not a list
    assert f.listof is None
    assert type(f.listof) is None
    assert f.listof is not list()
    # The priority should be 100
    assert f.priority == 100
    # The class type of the attribute should be None
    assert f.class_type is None
   

# Generated at 2022-06-13 07:50:34.509374
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute(isa=bool,
                    private=False,
                    default=True,
                    required=False,
                    listof=None,
                    priority=0)
    assert obj.isa == bool
    assert obj.private == False
    assert obj.default == True
    assert obj.required == False
    assert obj.priority == 0


# Generated at 2022-06-13 07:50:43.817952
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(isa="string", default='test')
    assert foo.default == 'test'
    assert foo.isa == 'string'

    foo = Attribute(isa="string", default=None)
    assert foo.default is None
    assert foo.isa == 'string'

    foo = Attribute(isa="string", default=[])
    assert foo.default == []
    assert foo.isa == 'string'

    foo = Attribute(isa="string", default={})
    assert foo.default == {}
    assert foo.isa == 'string'

    foo = Attribute(isa="string", default=set(['a', 'b']))
    assert foo.default == set(['a', 'b'])
    assert foo.isa == 'string'


# Generated at 2022-06-13 07:50:56.824184
# Unit test for constructor of class Attribute
def test_Attribute():

    import unittest

    class TestAttribute(unittest.TestCase):

        def runTest(self):
            pass

        def setUp(self):
            pass

        def test_init(self):

            a = Attribute(isa='list', private=False, default=[], required=True, listof='int', priority=0, class_type=None,
                          always_post_validate=False, inherit=False, alias='foobar', extend=False, prepend=False, static=False)
            assert a.isa == 'list'
            assert not a.private
            assert a.default == []
            assert a.required
            assert a.listof == 'int'
            assert a.priority == 0
            assert not a.class_type
            assert not a.always_post_validate
            assert not a.inher

# Generated at 2022-06-13 07:51:06.835891
# Unit test for constructor of class Attribute
def test_Attribute():
    old = dict(isa=None, private=False, default=None, required=False,
               listof=None, priority=0, class_type=None, always_post_validate=False,
               inherit=True, alias=None, extend=False, prepend=False, static=False)
    new = dict(isa='isa', private=True, default='default', required=True,
               listof='listof', priority=1, class_type='class_type', always_post_validate=True,
               inherit=False, alias='alias', extend=True, prepend=True, static=True)
    attr = Attribute(**new)
    for key in new:
        assert getattr(attr, key) == new[key], 'Attribute constructor failed: %s' % key
    attr = Attribute()

# Generated at 2022-06-13 07:51:15.279537
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='dict',
        private=True,
        default=None,
        required=True,
        listof='list',
        priority=0,
        class_type=dict,
        always_post_validate=False,
        inherit=True,
        alias='test_alias',
        extend=True,
        prepend=True,
        static=True,
    )
    assert fa.isa == 'dict'
    assert fa.private == True
    assert fa.default == None
    assert fa.required == True
    assert fa.listof == 'list'
    assert fa.priority == 0
    assert fa.class_type == dict
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias == 'test_alias'
   

# Generated at 2022-06-13 07:51:17.642101
# Unit test for constructor of class Attribute
def test_Attribute():
    # TODO
    pass


# Generated at 2022-06-13 07:51:25.861848
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='str', private=True, default=None, required=False, listof=None,
                        priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    assert fa.isa == 'str'
    assert fa.private == True
    assert fa.default == None
    assert fa.required == False
    assert fa.listof == None
    assert fa.priority == 0
    assert fa.class_type == None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias == None



# Generated at 2022-06-13 07:51:34.290709
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    def check_attr(attr, isa=None, private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False):

        assert (attr.isa == isa)
        assert (attr.private == private)
        assert (attr.default == default)
        assert (attr.required == required)
        assert (attr.listof == listof)
        assert (attr.priority == priority)
        assert (attr.class_type == class_type)
        assert (attr.always_post_validate == always_post_validate)
        assert (attr.inherit == inherit)
        assert (attr.alias == alias)

# Generated at 2022-06-13 07:51:43.310872
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str',
                  private=False,
                  default='test',
                  required=False,
                  listof=False,
                  priority=0,
                  class_type=None,
                  always_post_validate=False,
                  inherit=True,
                  alias=None)
    assert a.isa == 'str'
    assert a.private == False
    assert a.default == 'test'
    assert a.required == False
    assert a.listof == False
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None



# Generated at 2022-06-13 07:51:49.028573
# Unit test for constructor of class Attribute
def test_Attribute():

    attr = Attribute()

    assert isinstance(attr,Attribute)
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


# Generated at 2022-06-13 07:51:55.657410
# Unit test for constructor of class Attribute
def test_Attribute():
    attributes = Attribute(
        isa='test1',
        private=True,
        default='test2',
        required=True,
        listof='test3',
        class_type='test4',
        always_post_validate=True,
        inherit=True,
        alias='test5',
        extend=True,
        prepend=True,
    )
    assert attributes.isa == 'test1'
    assert attributes.private == True
    assert attributes.default == 'test2'
    assert attributes.required == True
    assert attributes.listof == 'test3'
    assert attributes.priority == 0
    assert attributes.class_type == 'test4'
    assert attributes.always_post_validate == True
    assert attributes.inherit == True
    assert attributes.alias == 'test5'
    assert attributes

# Generated at 2022-06-13 07:52:05.653852
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Instantiate a FieldAttribute object
    attr = FieldAttribute()

    # Check fields
    assert isinstance(attr, Attribute)
    assert attr.isa == None
    assert not attr.private
    assert attr.default == None
    assert not attr.required
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert not attr.always_post_validate
    assert attr.inherit
    assert attr.alias == None
    assert not attr.extend
    assert not attr.prepend
    assert not attr.static


# Generated at 2022-06-13 07:52:16.699867
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute()
    assert attribute.isa is None
    assert attribute.private is False
    assert attribute.default is None
    assert attribute.required is False
    assert attribute.listof is None
    assert attribute.priority is 0
    assert attribute.class_type is None
    assert attribute.always_post_validate is False
    assert attribute.inherit is True
    assert attribute.alias is None
    assert attribute.extend is False
    assert attribute.prepend is False
    assert attribute.static is False

    attribute = Attribute("Test Attribute")
    assert attribute.isa is not None
    assert attribute.private is False
    assert attribute.default is None
    assert attribute.required is False
    assert attribute.listof is None
    assert attribute.priority is 0
    assert attribute.class_type is None
    assert attribute.always

# Generated at 2022-06-13 07:52:19.682943
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=str)
    assert a.isa == str

    try:
        a = Attribute(isa='str', default={})
        raise AssertionError
    except TypeError:
        pass

    a = Attribute(isa='str', default=lambda: {})
    assert a.isa == str



# Generated at 2022-06-13 07:52:24.212009
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

# Generated at 2022-06-13 07:52:28.652332
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert isinstance(Attribute(isa='int'), FieldAttribute)
    assert isinstance(Attribute(isa='int', alias='myAlias'), FieldAttribute)


# Generated at 2022-06-13 07:52:32.409453
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field=FieldAttribute(
        isa='int',
        private=False,
        default=0,
        required=False,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=False,
        alias=None,
        static=False,
    )
    return True

# Generated at 2022-06-13 07:52:39.764356
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_attribute = FieldAttribute(
        isa='string',
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
    assert test_attribute.isa == 'string'
    assert test_attribute.private == True
    assert test_attribute.default == None
    assert test_attribute.required == False
    assert test_attribute.listof == None
    assert test_attribute.priority == 0
    assert test_attribute.class_type == None
    assert test_attribute.always_post_validate == False
    assert test_attribute.inherit

# Generated at 2022-06-13 07:52:41.619546
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a is not None

# Tests to make sure that Attribute is callable and makes a copy of itself

# Generated at 2022-06-13 07:52:48.280214
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='list', private=True, default=[], listof='dict')
    assert f.isa == 'list'
    assert f.private
    assert f.default == []
    assert f.listof == 'dict'
    def val(): return []
    f = FieldAttribute(isa='list', default=val)
    assert f.default == val()

# Generated at 2022-06-13 07:52:59.377584
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=False, default='test', required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=False, alias=None, extend=False, prepend=False, static=False)
    assert a.isa == 'str'
    assert a.private == False
    assert a.default == 'test'
    assert a.required == True
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == False
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False
    assert a.static == False



# Generated at 2022-06-13 07:53:08.279969
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test the creation of an Attribute instance
    attribute = Attribute(isa='int', required=True, default=0, inherit=True)

    # Check the values of the arguments
    assert attribute.isa == 'int'
    assert attribute.required == True
    assert attribute.default == 0
    assert attribute.inherit == True

    # Test the creation of an Attribute instance with an invalid default value
    try:
        attribute = Attribute(isa='str', default=[])
        assert False
    except AssertionError:
        assert True
    except Exception:
        assert False


# Generated at 2022-06-13 07:53:15.644100
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    user_name = FieldAttribute(
        isa='dict',
        required=True,
        listof=FieldAttribute(
            isa='dict',
            required=True,
            listof=FieldAttribute(
                isa='string',
                required=True,
            ),
        ),
    )
    assert user_name.isa == 'dict'
    assert user_name.required
    assert user_name.listof.isa == 'dict'
    assert user_name.listof.listof.isa == 'string'
    assert user_name.listof.listof.required



# Generated at 2022-06-13 07:53:21.485053
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.private == False
    assert attr.required == False
    assert attr.inherit == True
    attr = Attribute(private=True, required=True, inherit=False)
    assert attr.private == True
    assert attr.required == True
    assert attr.inherit == False


# Generated at 2022-06-13 07:53:32.833853
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Test the Attribute class
    """
    field_1 = FieldAttribute(
        isa='int',
        default=0,
        required=False,
        priority=10,
        always_post_validate=False
    )
    assert field_1.isa == 'int'
    assert not field_1.private
    assert field_1.default == 0
    assert not field_1.required
    assert field_1.listof is None
    assert field_1.priority == 10
    assert field_1.class_type is None
    assert not field_1.always_post_validate
    assert field_1.inherit
    assert field_1.alias is None
    assert not field_1.extend
    assert not field_1.prepend
    assert not field_1.static

    field_

# Generated at 2022-06-13 07:53:45.022973
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    result = FieldAttribute()

    # default values
    assert result.isa is None
    assert result.private is False
    assert result.default is None
    assert result.required is False
    assert result.listof is None
    assert result.priority == 0
    assert result.class_type is None
    assert result.always_post_validate is False
    assert result.inherit is True
    assert result.alias is None
    assert result.extend is False
    assert result.prepend is False
    assert result.static is False

    result = FieldAttribute(alias="Testing")
    assert result.alias == 'Testing'

    result = FieldAttribute(isa="String")
    assert result.isa == "String"

    result = FieldAttribute(isa="String", private=True)
    assert result.isa == "String"

# Generated at 2022-06-13 07:53:47.579119
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from nose.plugins.skip import SkipTest
    raise SkipTest("TODO: tests for FieldAttribute")


# Generated at 2022-06-13 07:53:50.484183
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import unittest
    class testFieldAttribute(unittest.TestCase):
        def setUp(self):
            self.fieldAttribute = FieldAttribute(
            )
    unittest.main()


# Generated at 2022-06-13 07:53:56.097397
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute(isa='str', private=True, default=123, required=True, listof=None, priority=0, class_type='foo', always_post_validate=False, inherit=True, alias='string')

    assert FA.isa == 'str'
    assert FA.private == True
    assert FA.default == 123
    assert FA.required == True
    assert FA.listof == None
    assert FA.priority == 0
    assert FA.class_type == 'foo'
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.alias == 'string'



# Generated at 2022-06-13 07:53:58.173979
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    Attribute(isa=int, class_type=int)


# Generated at 2022-06-13 07:54:01.694301
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa=1, private=True, default=None,
                required=False, listof=None, priority=0, inherit=False,
                alias='my_alias', extend=False, prepend=False, static=False)
    assert attr.isa == 1
    assert attr.private is True
    assert attr.inherit is False
    assert attr.alias == 'my_alias'

# Unit test to check if attribute class is singleton or not

# Generated at 2022-06-13 07:54:13.907808
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.isa is None
    assert not a.private
    assert a.default is None
    assert not a.required
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert not a.always_post_validate
    assert not a.static

    default = dict(abcde=None)
    a = Attribute(
        isa='dict',
        static=True,
        private=True,
        required=True,
        listof='any',
        priority=10,
        class_type='dict',
        always_post_validate=True,
        default=default,
    )
    assert a.isa == 'dict'
    assert a.static
    assert a.private
    assert a.required

# Generated at 2022-06-13 07:54:17.424377
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    f = FieldAttribute(isa=AnsibleUnicode, default=lambda: "")
    assert(isinstance(f.default(), AnsibleUnicode))


# Generated at 2022-06-13 07:54:28.704483
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test for setting various parameters for class Attribute
    a = Attribute(isa=str)
    assert a.isa == str
    assert a.private == False
    assert a.default is None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias is None

    a = Attribute(isa='list', private=True, default=True, required=True, listof=True, priority=1, class_type=True, always_post_validate=True, inherit=False, alias=True)
    assert a.isa == 'list'
    assert a.private == True
    assert a.default is True
    assert a.required

# Generated at 2022-06-13 07:54:35.845808
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    new = FieldAttribute(isa='list', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    f = FieldAttribute()
    f.private = False
    f.default = None
    f.required = False
    f.listof = None
    f.priority = 0
    f.class_type = None
    f.always_post_validate = False
    f.inherit = True
    f.alias = None
    f.extend = False
    f.prepend = False
    f.static = False
    f.isa = 'list'
    assert f == new


# Generated at 2022-06-13 07:54:56.446406
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="test")
    assert a.isa == "test"
    assert a.private == False
    assert a.required == False
    assert a.default == None
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None

    # Test with a non-mutable default
    a = Attribute(isa="list", default='test')
    assert a.isa == "list"
    assert a.private == False
    assert a.required == False
    assert a.default == 'test'
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post

# Generated at 2022-06-13 07:55:06.397553
# Unit test for constructor of class Attribute
def test_Attribute():

    # Instantiate an object of class Attribute
    # See: ansible/playbook/__init__.py
    x = Attribute(isa='dict', default=dict)
    assert x.isa == 'dict'
    assert callable(x.default)

    try:
        # should be throwing an exception here
        # Instantiating the class with a 'dict' for default
        # value, and dict is not a callable
        x = Attribute(isa='dict', default=dict())
        raise Exception
    except TypeError:
        # test passed
        assert True

    # Instantiating the class with a 'dict' for default
    # value, and dict() is a callable
    x = Attribute(isa='dict', default=dict())
    assert x.isa == 'dict'
    assert callable(x.default) == False

# Generated at 2022-06-13 07:55:11.877736
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    def MyDefault():
        return 'my default'

    def MyDefault2():
        return 'my default'

    a1 = FieldAttribute(
        isa='dict',
        default=MyDefault,
        required=True
    )

    a2 = FieldAttribute(
        isa='dict',
        default=MyDefault2,
        required=True
    )

    assert a1 == a2



# Generated at 2022-06-13 07:55:16.562703
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # valid usages
    a = FieldAttribute()
    a = FieldAttribute(isa='str')
    a = FieldAttribute(isa=str, default='abc')

    # invalid usages
    try:
        a = FieldAttribute(isa=str(), default='abc')
        assert False
    except:
        pass

    try:
        a = FieldAttribute(isa=str, default=str())
        assert False
    except:
        pass



# Generated at 2022-06-13 07:55:17.358572
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()


# Generated at 2022-06-13 07:55:29.391639
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from collections import Iterable, Mapping
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    a = Attribute()

    # the isa=None value was causing issues with variables not being copied
    # and overwritten in the facts module. This should be fixed with this
    # commit, but we need to test to ensure that it is indeed fixed.
    #
    # The problem was that we were using setattr with None as the value
    # and thus it was not actually setting the value.
    data = { 'a': 1, 'b': 2 }
    cop = copy(data)
    setattr(a, 'str_ok', data)

# Generated at 2022-06-13 07:55:37.669287
# Unit test for constructor of class Attribute
def test_Attribute():
    class A:
        attr = Attribute()
    assert A.attr.isa is None and \
           A.attr.private is False and \
           A.attr.default is None and \
           A.attr.required is False and \
           A.attr.listof is None and \
           A.attr.priority == 0 and \
           A.attr.class_type is None and \
           A.attr.always_post_validate is False and \
           A.attr.inherit is True and \
           A.attr.alias is None



# Generated at 2022-06-13 07:55:45.505793
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True)
    a2 = Attribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True)
    a3 = Attribute(isa='str', private=False, default=None, required=False, listof=None, priority=100, class_type=None, always_post_validate=False, inherit=True)

    assert a1 == a2
    assert a1.__lt__(a3)
    assert a1.__lt__(a3)

# Generated at 2022-06-13 07:55:46.429327
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute is not None


# Generated at 2022-06-13 07:55:49.643263
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa == None
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False


# Generated at 2022-06-13 07:56:10.357825
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(required=True, isa='int', default=5)
    assert f is not None

# Generated at 2022-06-13 07:56:22.306122
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
  attr = FieldAttribute(isa = 'boolean', inherit = True, static = False, private = False, prepend = True,
                        extend = True, alias = 'test', required = True, listof = "list", priority = 5,
                        class_type = 'someclass', default = 'somedefault', always_post_validate = False)
  assert attr.isa == 'boolean'
  assert attr.inherit is True
  assert attr.static is False
  assert attr.private is False
  assert attr.prepend is True
  assert attr.extend is True
  assert attr.alias == 'test'
  assert attr.required is True
  assert attr.listof == "list"
  assert attr.priority == 5
  assert attr.class_type == 'someclass'


# Generated at 2022-06-13 07:56:27.809985
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from unittest import TestCase

    class Test(TestCase):
        def test_containers_require_callable_defaults(self):
            Attribute(isa='dict', default={'foo': 'bar'})
            Attribute(isa='set', default=set(['foo', 'bar']))
            Attribute(isa='list', default=[1, 2, 3])
            with self.assertRaises(TypeError):
                Attribute(isa='dict', default='foo')
            with self.assertRaises(TypeError):
                Attribute(isa='set', default='foo')
            with self.assertRaises(TypeError):
                Attribute(isa='list', default='foo')

# Generated at 2022-06-13 07:56:36.393410
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='string', required=True)
    assert a.isa == 'string'
    assert a.private == False
    assert a.default == None
    assert a.required == True
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    a = Attribute(default='Hi!')
    assert a.default == 'Hi!'
    a = Attribute(listof='dict')
    assert a.listof == 'dict'
    a = Attribute(required=True)
    assert a.required == True
    assert a.default == None



# Generated at 2022-06-13 07:56:36.908189
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass

# Generated at 2022-06-13 07:56:42.339321
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='list', listof='str')
    assert fa.isa == 'list'
    assert fa.default is None
    assert fa.listof == 'str'

FieldAttribute.register(dict)
FieldAttribute.register(list)
FieldAttribute.register(tuple)
FieldAttribute.register(bool)
FieldAttribute.register(str)
FieldAttribute.register(int)
FieldAttribute.register(float)

# Generated at 2022-06-13 07:56:52.936689
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='bool', private=True, default=False, required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)
    a = Attribute(isa='dict', private=False, default={}, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=False, alias=None)
    FieldAttribute(isa='bool', private=True, default=False, required=True, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None)

# Generated at 2022-06-13 07:56:54.969259
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field=FieldAttribute(isa='int',required=False,default=0)
    assert field.isa == 'int'
    assert field.required == False
    assert field.default == 0

# Generated at 2022-06-13 07:56:59.962120
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa="bool")
    assert attr.isa == "bool"
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


# Generated at 2022-06-13 07:57:12.540127
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute()
    assert FA.default is None
    assert FA.required is False
    assert FA.priority == 0
    assert FA.listof is None
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.extend == False
    assert FA.prepend == False
    FA = FieldAttribute(default=1)
    assert FA.default == 1
    assert FA.required is False
    assert FA.priority == 0
    assert FA.listof is None
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.extend == False
    assert FA.prepend == False
    FA = FieldAttribute(default='default')
    assert FA.default == 'default'
    assert FA.required is False

# Generated at 2022-06-13 07:58:04.119151
# Unit test for constructor of class Attribute
def test_Attribute():
    attr_obj = Attribute(isa='str', private=False, default='default', listof='something')
    assert attr_obj.isa == 'str'
    assert attr_obj.private == False
    assert attr_obj.default == 'default'
    assert attr_obj.listof == None
    assert attr_obj.priority == 0
    assert attr_obj.class_type == None
    assert attr_obj.always_post_validate == False
    assert attr_obj.inherit == True
    assert attr_obj.alias == None

    attr_obj = Attribute(isa='str', private=True, default='default', listof='something')
    assert attr_obj.isa == 'str'
    assert attr_obj.private == True
    assert attr_obj.default

# Generated at 2022-06-13 07:58:08.403110
# Unit test for constructor of class Attribute
def test_Attribute():
    sample_attr = Attribute(isa='boolean', default=True, required=True)
    assert isinstance(sample_attr, Attribute)
    assert sample_attr.isa == 'boolean'
    assert sample_attr.private is False
    assert sample_attr.default is True
    assert sample_attr.required is True

# Generated at 2022-06-13 07:58:17.732187
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='foo', private=True, default=None, required=False,
            listof='bar', priority=0, class_type='class',
            always_post_validate=False, inherit=True, alias='foo_alias',
            extend=False, prepend=False, static=False)
    assert a.isa == 'foo'
    assert a.private == True
    assert a.default == None
    assert a.required == False
    assert a.listof == 'bar'
    assert a.priority == 0
    assert a.class_type == 'class'
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == 'foo_alias'
    assert a.extend == False
    assert a.prepend == False
    assert a.static

# Generated at 2022-06-13 07:58:25.948525
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
        isa='bool',
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
    assert f.isa == 'bool'
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


# Generated at 2022-06-13 07:58:31.096716
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa="string",
        private=False,
        default=None,
        required=True,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias='foo',
        extend=False,
        prepend=False,
        static=False,
    )

    assert fa.isa == "string"
    assert fa.private == False
    assert fa.default == None
    assert fa.required == True
    assert fa.listof == None
    assert fa.priority == 0
    assert fa.class_type == None
    assert fa.always_post_validate == False
    assert fa.inherit == True
    assert fa.alias == 'foo'

# Generated at 2022-06-13 07:58:36.142981
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute(isa=None, private=False, default=None, required=False,
            listof=None, priority=0, class_type=None, always_post_validate=False,
            inherit=True, alias=None, extend=False, prepend=False, static=False)


# Generated at 2022-06-13 07:58:39.384300
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(private=True, inherit=False, required=True)
    assert fa.private
    assert not fa.inherit
    assert fa.required



# Generated at 2022-06-13 07:58:46.122398
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.utils import type_compat
    from ansible.validate import validator
    from ansible.parsing.yaml.objects import AnsibleUnicode

    x = Attribute(isa='string', default='a default string')
    assert x.isa == 'string'
    assert x.default == 'a default string'
    assert x.required is False



# Generated at 2022-06-13 07:58:53.784750
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=int, default=0, required=True)
    assert a.isa == int
    assert a.default == 0
    assert a.required == True

    # bad value for isa
    try:
        a = Attribute(isa='not_a_valid_isa_type')
    except TypeError:
        pass

    # bad value for default
    try:
        a = Attribute(isa=int, default='not_a_valid_default_type')
    except TypeError:
        pass

# Generated at 2022-06-13 07:58:55.144317
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict')
    assert a.isa == 'dict'
