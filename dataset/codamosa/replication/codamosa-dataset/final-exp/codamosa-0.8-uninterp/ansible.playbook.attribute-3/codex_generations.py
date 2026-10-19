

# Generated at 2022-06-13 07:49:02.231498
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='string')
    assert a.isa == 'string'



# Generated at 2022-06-13 07:49:15.720333
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(isa='dict',
                          private=False,
                          default=None,
                          required=False,
                          listof=None,
                          priority=0,
                          always_post_validate=False,
                          inherit=True,
                          alias=None,
                          extend=False,
                          prepend=False,
                          static=False,)
    attribute.isa = 'dict'
    assert attribute.isa == 'dict'
    attribute.private = False
    assert attribute.private == False
    attribute.default = None
    assert attribute.default == None
    attribute.required = False
    assert attribute.required == False
    attribute.listof = None
    assert attribute.listof == None
    attribute.priority = 0
    assert attribute.priority == 0
    attribute.always_post_valid

# Generated at 2022-06-13 07:49:23.152449
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    am = FieldAttribute(isa='str')
    assert am.isa is not None
    # assert am.private is not None
    assert am.default is not None
    assert am.required is not None
    assert am.listof is not None
    assert am.priority is not None
    assert am.class_type is not None
    assert am.always_post_validate is not None
    assert am.inherit is not None
    assert am.alias is not None
    assert am.extend is not None
    assert am.prepend is not None
    assert am.static is not None

# Generated at 2022-06-13 07:49:30.380114
# Unit test for constructor of class Attribute
def test_Attribute():
    # A real attribute, with appropriate defaults
    with pytest.raises(TypeError) as excinfo:
        Attribute(isa='dict', default=dict())
    assert 'defaults for FieldAttribute may not be mutable' in str(excinfo.value)
    assert Attribute(isa='dict', default=lambda: dict())

    # Invalid attributes and appropriate errors
    with pytest.raises(ValueError) as excinfo:
        Attribute(isa='foo')
    assert 'Unrecognized isa foo' in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        Attribute(isa='dict', default='foo')
    assert 'isa dict but default is ' in str(excinfo.value)


# Generated at 2022-06-13 07:49:38.553714
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = Attribute(
        isa='list',
        private=True,
        default=[],
        required=False
    )
    assert attribute == attribute
    assert attribute.isa == 'list'
    assert attribute.private == True
    assert attribute.default == []
    assert attribute.required == False
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias is None
    assert attribute.extend == False
    assert attribute.prepend == False
    assert attribute.static == False
    assert attribute != attribute.basic(
        default=False,
        required=True
    )
    assert attribute < attribute.basic(listof=str)
    assert attribute <= attribute

# Generated at 2022-06-13 07:49:42.047772
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='list', always_post_validate=True)
    assert hasattr(field, 'always_post_validate')
    assert field.isa == 'list'
    assert field.always_post_validate == True



# Generated at 2022-06-13 07:49:47.765695
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    global_defaults = { 'name': 'foo', 'owner': 'bob', 'mode': '777' }
    item_defaults = { 'size': '100M', 'mode': '666' }

    global_attributes = dict(
        (key, FieldAttribute(default=value, inherit=True))
        for key, value in global_defaults.items())
    item_attributes = dict(
        (key, FieldAttribute(default=value, inherit=False))
        for key, value in item_defaults.items())

    class Item:
        ATTRIBUTES = item_attributes

    class Global:
        ATTRIBUTES = global_attributes
        def __init__(self, **kwargs):
            self._load_attributes(self, **kwargs)


# Generated at 2022-06-13 07:49:56.323705
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='string', default='hello')
    assert attr.isa == 'string'
    assert attr.default == 'hello'
    # test with a dict which is muttable
    try:
        attr = FieldAttribute(isa='dict', default=dict(a=1,b=2))
        assert False
    except TypeError:
        assert True

    # test with a dict which is muttable
    attr = FieldAttribute(isa='dict', default=lambda: dict(a=1,b=2))
    assert attr.isa == 'dict'
    assert attr.default == {'a': 1, 'b': 2}



# Generated at 2022-06-13 07:50:08.025415
# Unit test for constructor of class Attribute
def test_Attribute():
    attr_1 = Attribute(isa='int')
    assert (attr_1.isa == 'int' and attr_1.private == False and attr_1.default == None and
            attr_1.required == False and attr_1.listof == None and attr_1.priority == 0)

    attr_2 = Attribute(isa='int', required=True)
    assert (attr_2.isa == 'int' and attr_2.private == False and attr_2.default == None and
            attr_2.required == True and attr_2.listof == None and attr_2.priority == 0)

    # Testing for the default mutable restriction
    attr_3 = Attribute(isa='list', default=[])


# Generated at 2022-06-13 07:50:12.629025
# Unit test for constructor of class Attribute
def test_Attribute():
    import unittest

    class ConstructorTest(unittest.TestCase):

        def test_default_no_list(self):
            with self.assertRaises(TypeError):
                Attribute(default=['some_list'])

    unittest.main(verbosity=2)

# Generated at 2022-06-13 07:50:14.937997
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()



# Generated at 2022-06-13 07:50:20.630526
# Unit test for constructor of class Attribute
def test_Attribute():
    # These are not exceptions
    attr = Attribute()
    attr = Attribute(isa='str')
    attr = Attribute(isa='str', listof='str')
    attr = Attribute(isa='str', listof='str', required=True)

    # These are exceptions
    # Attribute(isa='str', default=[1, 2, 3])  # default mutable
    # Attribute(isa='list', listof='str')  # listof is not a str

# Generated at 2022-06-13 07:50:32.025368
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fieldattribute1 = FieldAttribute(
        isa='dict',
        default={},
        inherit=True,
        always_post_validate=True,
        class_type=None,
        required=False,
        listof=None,
        priority=2,
        private=False,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert fieldattribute1.isa == 'dict'
    assert fieldattribute1.default == {}
    assert fieldattribute1.inherit == True
    assert fieldattribute1.always_post_validate == True
    assert fieldattribute1.class_type == None
    assert fieldattribute1.required == False
    assert fieldattribute1.listof == None
    assert fieldattribute1.priority == 2

# Generated at 2022-06-13 07:50:33.057789
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert attr.isa is None, "FieldAttribute.isa is None"

test_FieldAttribute()



# Generated at 2022-06-13 07:50:36.633567
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa = 'str', required = False)
    assert fa.isa == 'str'
    assert fa.private == False
    assert fa.default == None
    assert fa.listof == None
    assert fa.priority == 0



# Generated at 2022-06-13 07:50:44.192866
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(None)

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

    assert attr == Attribute()
    assert attr != Attribute(priority=1)



# Generated at 2022-06-13 07:50:50.228204
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FieldAttribute(default = {})
    except Exception as e:
        if 'defaults for FieldAttribute may not be mutable' in str(e):
            pass
        else:
            raise
    else:
        raise AssertionError("Expected exception, did not get one.")

# Unit tests for operator overloads of class FieldAttribute

# Generated at 2022-06-13 07:50:56.731845
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # the class for constructor of FieldAttribute
    class TestAttribute(Attribute):
        has_default = FieldAttribute(default=True)
        listof_int = FieldAttribute(listof=int)

    # create an instance of class TestAttribute
    test_attr = TestAttribute()

    assert test_attr.has_default == True
    assert test_attr.listof_int == []

# Generated at 2022-06-13 07:51:03.679869
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    expected = {
        'default': None,
        'required': False,
        'listof': None,
        'priority': 0,
        'alias': None,
        'private': False,
        'extend': False,
        'prepend': False,
        'static': False,
        'class_type': None,
        'inherit': True,
        'always_post_validate': False,
        'isa': None
    }
    assert expected == FieldAttribute().__dict__

# Generated at 2022-06-13 07:51:11.719927
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa='dict')
    assert type(a.isa) is str
    assert isinstance(a.isa, str)
    assert a.isa == 'dict'
    assert a.isa == u'dict'

    a = Attribute(isa='dict', private=False, default=True, required=True, listof=None, priority=0, class_type='self')
    assert type(a.isa) is str
    assert type(a.private) is bool
    assert type(a.default) is bool
    assert type(a.required) is bool
    assert type(a.listof) is NoneType
    assert type(a.priority) is int
    assert type(a.class_type) is str

    # Ensure that the constructor ensures that the default value is not mutable

# Generated at 2022-06-13 07:51:19.575103
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f=FieldAttribute()
    assert f.isa==None
    assert f.private==False
    assert f.default==None
    assert f.required==False
    assert f.listof==None
    assert f.priority==0
    assert f.class_type==None
    assert f.always_post_validate==False
    assert f.inherit==True
    assert f.alias==None



# Generated at 2022-06-13 07:51:27.163995
# Unit test for constructor of class Attribute
def test_Attribute():
    # define a attribute instance
    attribute = Attribute()

    # check result
    assert attribute.isa is None
    assert attribute.private == False
    assert attribute.default is None
    assert attribute.required == False
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias is None
    assert attribute.extend == False
    assert attribute.prepend == False
    assert attribute.static == False


# Generated at 2022-06-13 07:51:39.077179
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test that an error is raised if a default value is provided and it is a
    # mutable (not a callable)
    try:
        FieldAttribute(isa=None,
                       private=False,
                       default=[],
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
        raise Exception('An error should have been raised')
    except TypeError:
        pass
    # Test that an error is not raised if a callable is provided as the default

# Generated at 2022-06-13 07:51:51.186554
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()
    # No attributes
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

    # Attributes

# Generated at 2022-06-13 07:51:58.567451
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=True, default=None, required=False,
                  listof=None, priority=0, inherit=True, always_post_validate=False, alias=None)
    assert a.isa == 'str'
    a = Attribute(isa='dict', private=True, default=None, required=False,
                  listof=None, priority=0, inherit=True, always_post_validate=False, alias=None)
    # defaults to 'dict'
    assert a.isa == Attribute.isa
    a = Attribute(isa='list', private=True, default=None, required=False,
                  listof=None, priority=0, inherit=True, always_post_validate=False, alias=None)
    # defaults to 'list'
    assert a.isa == 'list'

# Generated at 2022-06-13 07:52:11.415420
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:52:19.655476
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa1 = FieldAttribute()
    assert fa1.isa is None
    assert fa1.private is False
    assert fa1.default is None
    assert fa1.required is False
    assert fa1.listof is None
    assert fa1.priority == 0
    assert fa1.class_type is None
    assert fa1.always_post_validate is False
    assert fa1.inherit is True
    assert fa1.alias is None
    assert fa1.extend is False
    assert fa1.prepend is False
    assert fa1.static is False


# Generated at 2022-06-13 07:52:25.198100
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test for valid case
    try:
        FieldAttribute(isa="boolean", required=True, private=False, listof="dict")
    except Exception:
        raise Exception("Test for valid case failed")

    # Test for invalid case
    # One option is invalid: isa = "dict"
    try:
        FieldAttribute(isa="dict", required=True, private=False, listof="dict")
    except TypeError:
        pass
    else:
        raise Exception("Test for invalid case failed")



# Generated at 2022-06-13 07:52:27.936851
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute(default=True, always_post_validate=True)
    assert x.default == True
    assert x.always_post_validate == True
    x = Attribute(default=True)
    assert x.default == True
    assert x.always_post_validate == False


# Generated at 2022-06-13 07:52:35.880310
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

    attr = Attribute(
        isa='str',
        private=True,
        default=False,
        required=True,
        listof="dict",
        priority=1,
        class_type="test_class",
        always_post_validate=True,
        inherit=False,
        alias='alias',
    )

# Generated at 2022-06-13 07:52:47.680259
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # FIXME: Should be passing in a callable as a default value to verify
    # the behavior of passing in non-callables.
    test_field = FieldAttribute(isa='list', default=[], listof='str')
    assert test_field.isa == 'list'
    assert test_field.default == []
    assert test_field.listof == 'str'



# Generated at 2022-06-13 07:52:51.583973
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa='test', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, static=False)
    assert isinstance(a, Attribute)

# Generated at 2022-06-13 07:53:03.006587
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Test Attribute constructor with various inputs.
    """
    # Test with input isa as None and default as None
    atr = Attribute(isa=None, default=None)
    assert atr.isa == None
    assert atr.default == None


    # Test with input isa as integer and default as None
    atr = Attribute(isa=int, default=None)
    assert atr.isa == int
    assert atr.default == None


    # Test with input isa as int and default as an integer
    default = 15
    atr = Attribute(isa=int, default=default)
    assert atr.isa == int
    assert atr.default == 15


    # Test with input isa as list, listof as integer,
    # default as list of integers and always_post_validate

# Generated at 2022-06-13 07:53:07.066590
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        fieldattr = FieldAttribute(default=['a'])
    except TypeError as e:
        assert "defaults for FieldAttribute may not be mutable, please provide a callable instead" in str(e)


# Generated at 2022-06-13 07:53:15.565951
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()
    assert field_attribute.isa is None
    assert field_attribute.private is False
    assert field_attribute.default is None
    assert field_attribute.required is False
    assert field_attribute.listof is None
    assert field_attribute.priority == 0
    assert field_attribute.class_type is None
    assert field_attribute.always_post_validate is False
    assert field_attribute.inherit is True
    assert field_attribute.alias is None
    assert field_attribute.extend is False
    assert field_attribute.prepend is False
    assert field_attribute.static is False



# Generated at 2022-06-13 07:53:17.887428
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    test_attribute = Attribute()
    print (test_attribute)

if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:53:25.538238
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute(isa='list')
    a2 = Attribute(isa='list')
    a3 = Attribute(isa='list', default='foo')
    a4 = Attribute(isa='list', default='foo')

    assert a1 == a2
    assert a3 == a4

    assert a1 < a3
    assert a3 > a1

    a1.priority = 10
    a2.priority = -10

    assert a1 > a2
    assert a1 < a2

# Generated at 2022-06-13 07:53:31.201504
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute(isa='bool', alias='boolean')
    print(a1)
    print(type(a1))
    assert a1.isa == 'bool'
    assert a1.alias == 'boolean'


if __name__ == "__main__": 
    test_Attribute()

# Generated at 2022-06-13 07:53:41.325617
# Unit test for constructor of class Attribute
def test_Attribute():
    arg = Attribute()
    assert arg.isa is None
    assert arg.required is False
    assert arg.listof is None
    assert arg.default is None
    assert arg.class_type is None
    assert arg.inherit is True
    assert arg.alias is None
    assert arg.priority == 0

    arg = Attribute(isa='boolean', required=True, default=True)
    assert arg.isa == 'boolean'
    assert arg.required is True
    assert arg.default is True
    assert arg.priority == 0

    arg = Attribute(isa='class', required=True, default=True, class_type=object)
    assert arg.isa == 'class'
    assert arg.required is True
    assert arg.default is True
    assert arg.class_type is object
    assert arg.priority == 0

# Generated at 2022-06-13 07:53:43.083413
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='string', default=dict())

# Generated at 2022-06-13 07:53:59.160330
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from .. import BASE_ATTRIBUTES
    yml = dict(
        FieldAttribute(isa='dc1', default='abc', listof='c', always_post_validate=True, inherit=False, alias='d', prepend=True) ==
        dict(isa='dc1', default='abc', listof='c', always_post_validate=True, inherit=False, alias='d', prepend=True, **BASE_ATTRIBUTES)
    )

# Generated at 2022-06-13 07:54:03.206009
# Unit test for constructor of class Attribute
def test_Attribute():
  assert isinstance(Attribute(), Attribute)
  assert isinstance(Attribute(), Attribute)

  Attribute(isa=int)
  Attribute(default=0)

  try:
    Attribute(default=int)
  except TypeError:
    pass

  Attribute(listof=int)
  Attribute(class_type=int)

  try:
    Attribute(class_type='int')
  except TypeError:
    pass

  Attribute(extend=True)
  Attribute(prepend=True)
  Attribute(static=True)

# Generated at 2022-06-13 07:54:07.217578
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.base_vars import BaseVars

    # test that the base_vars class has a base_vars attribute
    base_vars = BaseVars()
    assert 'base_vars' in base_vars.__dict__

    # test that the base_vars attribute is an instance of class Attribute
    assert isinstance(base_vars.base_vars, Attribute)

    # test that the base_vars => Attribute  __init__ is properly constructed
    assert base_vars.base_vars.isa == 'dict'
    assert base_vars.base_vars.private is False
    assert base_vars.base_vars.default is None
    assert base_vars.base_vars.required is False

# Generated at 2022-06-13 07:54:13.252946
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()
    print(f1)
    f2 = FieldAttribute(private=False, default=None, required=False, priority=0)
    print(f2)
    f3 = FieldAttribute(private=True, default=None, required=True, priority=1)
    print(f3)

# Generated at 2022-06-13 07:54:14.973879
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    myattribute = FieldAttribute(isa='list')
    assert myattribute.isa == 'list'


# Generated at 2022-06-13 07:54:18.999896
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # Create an object of class FieldAttribute
    attr = FieldAttribute(isa='int')

    # Check the type of attr
    if not isinstance(attr, FieldAttribute):
        raise AssertionError('attr is not an instance of class FieldAttribute')



# Generated at 2022-06-13 07:54:29.692419
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test case 1: isa, default and required
    test_case_1 = {'isa': str, 'default': 10, 'required': False }
    try:
        Attribute(**test_case_1)
    except TypeError:
        assert False, 'test case 1 failed'
    # Test case 2: isa, default and listof
    test_case_2 = {'isa': str, 'default': 10, 'listof': None }
    try:
        Attribute(**test_case_2)
    except TypeError:
        assert False, 'test case 2 failed'
    # Test case 3: isa, default and class_type
    test_case_3 = {'isa': str, 'default': 10, 'class_type': None }

# Generated at 2022-06-13 07:54:36.538954
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import yaml

    base_attr = dict(
        isa='list',
        listof='dict',
    )

    attr_inherit = copy(base_attr)
    attr_inherit['inherit'] = True
    attr_inherit_default = copy(attr_inherit)
    attr_inherit_default['default'] = dict()


# Generated at 2022-06-13 07:54:43.358867
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # init(self,
    #      isa=None,
    #      private=False,
    #      default=None,
    #      required=False,
    #      listof=None,
    #      priority=0,
    #      class_type=None,
    #      always_post_validate=False,
    #      inherit=True,
    #      alias=None,
    #      extend=False,
    #      prepend=False,
    #      static=False,
    #      ):

    x = FieldAttribute()
    y = FieldAttribute(isa='str')
    z = FieldAttribute(isa='str', private=True)
    q = FieldAttribute(isa='str', private=True, default='a')

# Generated at 2022-06-13 07:54:47.734330
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
    assert obj.isa is None and obj.private == False and obj.default is None and obj.required == False and obj.listof is None \
        and obj.priority == 0 and obj.class_type is None and obj.always_post_validate == False and obj.inherit == True and obj.alias is None

# Generated at 2022-06-13 07:55:08.396594
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute()

test_FieldAttribute()


# Generated at 2022-06-13 07:55:10.753740
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='test', required=True)
    assert attr.isa == 'test'
    assert attr.required



# Generated at 2022-06-13 07:55:18.762826
# Unit test for constructor of class Attribute
def test_Attribute():

    class TestClass(object):
        def __init__(self, one=None, two=None, three=None, four=None, five=None, six=None):
            self.one = one
            self.two = two
            self.three = three
            self.four = four
            self.five = five
            self.six = six

        @property
        def one(self):
            return self._one

        @one.setter
        def one(self, value):
            self._one = value

        @property
        def two(self):
            return self._two

        @two.setter
        def two(self, value):
            self._two = value

        @property
        def three(self):
            return self._three

        @three.setter
        def three(self, value):
            self._

# Generated at 2022-06-13 07:55:29.885154
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='String', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=None, prepend=None)
    assert attr.isa == 'String'
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


# Generated at 2022-06-13 07:55:34.859709
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', private=False, default='test')
    assert attr
    assert attr.isa == 'str'
    assert attr.private == False
    assert attr.default == 'test'



# Generated at 2022-06-13 07:55:41.960447
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    c = FieldAttribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    assert c.isa == 'str'
    # Validate that type of default is not mutable
    try:
        c = FieldAttribute(isa='str', default='foo')
    except TypeError:
        assert True
    else:
        assert False, 'TypeError not raised'



# Generated at 2022-06-13 07:55:48.953879
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='list')
    assert f.isa == 'list'
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


# Generated at 2022-06-13 07:56:00.966404
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = str
    private = True
    default = 'default'
    required = True
    listof = list
    priority = 17
    class_type = Attribute()
    always_post_validate= True
    inherit= True
    alias= 'my_alias'
    extend= True
    prepend= True
    static= True
    attr = Attribute(isa, private, default, required, listof, priority, class_type, always_post_validate, inherit, alias, extend, prepend, static)
    assert attr.isa == isa
    assert attr.private == private
    assert attr.default == default
    assert attr.required == required
    assert attr.listof == listof
    assert attr.priority == priority
    assert attr.class_type == class_type
    assert att

# Generated at 2022-06-13 07:56:07.390149
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert f.isa is None
    assert f.default is None
    assert f.required is False
    assert f.listof is None
    assert f.priority == 0
    assert f.class_type is None
    assert f.always_post_validate is False
    assert f.inherit is True
    assert f.alias is None



# Generated at 2022-06-13 07:56:11.283399
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list')
    assert attr.isa == 'list'
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None

# Test for equality of 2 Attribute objects

# Generated at 2022-06-13 07:56:53.697977
# Unit test for constructor of class Attribute
def test_Attribute():
    pass

# Generated at 2022-06-13 07:56:56.231629
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa="str", private=True, default='a', required=True,
                listof='str', priority=0, class_type=str,
                always_post_validate=False, inherit=True, alias="test")


# Generated at 2022-06-13 07:57:07.815197
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    data = {
        "isa": "str",
        "private" : True,
        "default": "ansible",
        "required": True,
        "listof": "str",
        "priority": 3,
        "class_type": None,
        "always_post_validate": False,
        "inherit": True,
        "alias": "TestAlias",
        "extend": False,
        "prepend": False,
        "static": False
    }
    ansible_obj = FieldAttribute(**data)

    assert ansible_obj.isa == "str"
    assert ansible_obj.private is True
    assert ansible_obj.default == "ansible"
    assert ansible_obj.required is True
    assert ansible_obj.listof == "str"
    assert ansible_obj

# Generated at 2022-06-13 07:57:17.811151
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(isa='int').isa == 'int'
    assert FieldAttribute(isa='int', private=True).private is True
    assert FieldAttribute(isa='int', default=42).default == 42
    assert FieldAttribute(isa='int', required=True).required is True
    assert FieldAttribute(isa='int', listof='int').listof == 'int'
    assert FieldAttribute(isa='list', default=list).default is list
    assert FieldAttribute(isa='int', priority=1).priority == 1
    assert FieldAttribute(isa='class', class_type=int).class_type is int
    assert FieldAttribute(isa='int', inherit=False).inherit is False
    assert FieldAttribute(isa='int', alias='foo').alias == 'foo'
    assert FieldAttribute(isa='int').alias is None



# Generated at 2022-06-13 07:57:31.474904
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    a = Attribute(isa='list')
    a = Attribute(isa='list', default=[])
    a = Attribute(isa='list', default=[], inherit=False)
    a = Attribute(isa='list', inherit=False)
    a = Attribute(isa='list', static=True)
    a = Attribute(isa='list', static=False)
    a = Attribute(isa='list', listof='str')
    a = Attribute(isa='list', listof='str', inherit=False)
    a = Attribute(isa='dict', default={})
    a = Attribute(isa='dict', default={}, inherit=False)
    a = Attribute(isa='dict', inherit=False)
    a = Attribute(isa='dict', static=True)

# Generated at 2022-06-13 07:57:40.543740
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()

    assert f1 is not None
    assert f1.isa is None
    assert f1.private is False
    assert f1.default is None
    assert f1.required is False
    assert f1.listof is None
    assert f1.priority == 0
    assert f1.class_type is None
    assert f1.always_post_validate is False
    assert f1.inherit is True
    assert f1.alias is None
    assert f1.extend is False
    assert f1.prepend is False
    assert f1.static is False

# Generated at 2022-06-13 07:57:44.102907
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = FieldAttribute()
    a2 = FieldAttribute(isa='int', default=42)
    assert a1 != a2
    assert a1.default is None
    assert a2.default == 42



# Generated at 2022-06-13 07:57:49.324999
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    Test if we can create an instance of FieldAttribute
    """
    mytest_instance = FieldAttribute(isa=None, private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)

    assert isinstance(mytest_instance, FieldAttribute)




# Generated at 2022-06-13 07:57:56.136116
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='string', private=False, default='foo', required=True)
    a1 = Attribute(isa='string', private=False, default='foo', required=True)
    a2 = Attribute(isa='string', private=False, default='foo', required=True, priority=50)
    a3 = Attribute(isa='string', private=False, default='foo', required=True, priority=10)
    assert a == a1
    assert a != a2
    assert a < a2
    assert a2 > a
    assert a2 <= a2
    assert a2 >= a2
    assert a <= a2
    assert a <= a1
    assert a2 >= a1
    assert a2 >= a
    assert a == a
    assert a <= a
    assert a >= a

# Generated at 2022-06-13 07:57:56.758636
# Unit test for constructor of class Attribute
def test_Attribute():
    pass

