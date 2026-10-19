

# Generated at 2022-06-13 07:49:17.148920
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa=list,
        default=list(),
        class_type=list,
        listof=list,
        static=True
    )

    assert a.isa == list
    assert a.private == False
    assert a.default == list()
    assert a.required == False
    assert a.listof == list
    assert a.priority == 0
    assert a.class_type == list
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False
    assert a.static == True



# Generated at 2022-06-13 07:49:22.730854
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test that the constructor will throw an exception if a default value is provided
    # and it is not a callable type
    # This test should pass
    Attribute(default=None)

    # This test should fail
    try:
        Attribute(default=123456)
    except TypeError as e:
        pass
    else:
        raise AssertionError('Failed to throw an exception when a non-callable default is provided')

# Generated at 2022-06-13 07:49:27.351166
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.playbook.base import Base

    class Foo(Base):
        _foo = FieldAttribute(isa='dict', default=[])
        _bar = FieldAttribute(isa='dict', default=lambda: [])

    foo = Foo()

    try:
        foo._foo
    except AnsibleError:
        pass

    try:
        foo._bar
    except AnsibleError:
        pass

# Generated at 2022-06-13 07:49:32.915701
# Unit test for constructor of class Attribute
def test_Attribute():
    # test with required fields
    a = Attribute(isa='list', default=list())
    assert(a.isa == 'list')
    assert(a.default == list())
    try:
        a = Attribute(isa='list', default='hello')
    except TypeError:
        pass
    else:
        raise AssertionError('Constructor with list isa and non-list default did not raise TypeError')



# Generated at 2022-06-13 07:49:38.284328
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.dataloader import DataLoader

    #
    # Test __init__ method
    #
    # test_object_name = Attribute()
    # test_object_name = Attribute(isa='str')
    # test_object_name = Attribute(isa='str', private=True)
    # test_object_name = Attribute(isa='str', private=True, default='test')
    # test_object_name = Attribute(isa='str', private=True, default='test', required=True)
    # test_object_name = Attribute(isa='str', private=True, default='test', required=True, listof='is_a_string')
    # test_object_name = Att

# Generated at 2022-06-13 07:49:39.375204
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert isinstance(attr, FieldAttribute)



# Generated at 2022-06-13 07:49:40.633555
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    attr.private = True
    assert attr.private == True



# Generated at 2022-06-13 07:49:52.068708
# Unit test for constructor of class Attribute
def test_Attribute():

    attr = Attribute(
        isa='dict',
        private=True,
        default='test',
        required=True,
        listof='str',
        priority=10,
        class_type=None,
        always_post_validate=True,
        inherit=False,
        alias='name'
    )

    assert attr.isa == 'dict'
    assert attr.private == True
    assert attr.default == 'test'
    assert attr.required == True
    assert attr.listof == 'str'
    assert attr.priority == 10
    assert attr.class_type == None
    assert attr.always_post_validate == True
    assert attr.inherit == False
    assert attr.alias == 'name'



# Generated at 2022-06-13 07:50:02.205973
# Unit test for constructor of class Attribute
def test_Attribute():
    # If a container type is given for default, and not callable,
    # raise a TypeError.
    _TEST_DATA = (
        (dict(), 'dict'),
        ([], 'list'),
    )
    for default, isa in _TEST_DATA:
        try:
            Attribute(isa, default=default)
        except TypeError as e:
            assert 'defaults for FieldAttribute may not be mutable' in to_text(e)
        else:
            assert False, 'TypeError was not raised'



# Generated at 2022-06-13 07:50:10.522795
# Unit test for constructor of class Attribute
def test_Attribute():
    from collections import deque
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Create a new instance
    attr = Attribute(isa=int)

    # Test basic member variables
    assert attr.isa == int
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

    # Test optional parameters

# Generated at 2022-06-13 07:50:18.574220
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
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
    assert isinstance(attr, Attribute)


# Generated at 2022-06-13 07:50:20.425739
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a is not None

if __name__=="__main__":
    test_Attribute()

# Generated at 2022-06-13 07:50:22.812447
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from collections import namedtuple
    f = FieldAttribute(isa="str")
    assert type(f) is FieldAttribute

# Unit tests for __eq__ operator on class FieldAttribute

# Generated at 2022-06-13 07:50:34.614441
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict')
    assert a.isa == 'dict'

    a = Attribute(isa='str', default='load_balance')
    assert a.default == 'load_balance'
    assert a.isa == 'str'

    a = Attribute(isa='float', default=0.9)
    assert a.default == 0.9
    assert a.isa == 'float'

    a = Attribute(isa='bool', required=True)
    assert a.required

    a = Attribute(isa='bool', required=False)
    assert not a.required

    a = Attribute(isa='list', listof='str')
    assert a.listof == 'str'
    assert a.isa == 'list'

    a = Attribute(isa='list', listof='int')
    assert a.listof

# Generated at 2022-06-13 07:50:39.806093
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attr = FieldAttribute(isa=str, private=False, default='test', required=False,
            listof=None, priority=0, class_type=None, always_post_validate=False,
            inherit=True, alias=None, extend=False, prepend=False, static=False)
    assert type(field_attr) is FieldAttribute



# Generated at 2022-06-13 07:50:50.478355
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='string', required=True)
    assert attr.isa == 'string'
    assert attr.required == True
    assert attr.default == None
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False



# Generated at 2022-06-13 07:51:02.458255
# Unit test for constructor of class Attribute
def test_Attribute():
    data = {
        'class_type': "TestClass",
        'inherit': False,
        'extend': False,
        'alias': 'TestAlias',
        'private': True,
        'static': False,
        'isa': 'TestIsa',
        'default': None,
        'required': False,
        'listof': 'TestListof',
        'priority': 0,
        'always_post_validate': False,
        'prepend': False,
    }

    a = Attribute(**data)
    assert a.class_type == data['class_type']
    assert a.inherit == data['inherit']
    assert a.extend == data['extend']
    assert a.alias == data['alias']
    assert a.private == data['private']

# Generated at 2022-06-13 07:51:07.546036
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        # Invalid default
        default = []
        field = FieldAttribute(isa='list', default=default)
        assert False, "Expected exception but didn't get one"
    except Exception as e:
        # We should have been here
        pass

    # Valid default as callable
    default = lambda: []
    field = FieldAttribute(isa='list', default=default)
    assert field.default() == []


# Generated at 2022-06-13 07:51:15.618450
# Unit test for constructor of class Attribute
def test_Attribute():
    # Attribute constructor
    test_attribute = Attribute(isa='boolean', private=False, default=None,
                               required=False, listof=None, priority=0,
                               class_type=None, always_post_validate=False,
                               inherit=True, alias=None)
    # Check if type is boolean
    if test_attribute.isa != 'boolean':
        print('Attribute constructor test failed')
        exit()
    # Check if private is False
    if test_attribute.private != False:
        print('Attribute constructor test failed')
        exit()
    # Check if default is None
    if test_attribute.default != None:
        print('Attribute constructor test failed')
        exit()
    # Check if required is False
    if test_attribute.required != False:
        print('Attribute constructor test failed')


# Generated at 2022-06-13 07:51:17.052268
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute()


# Generated at 2022-06-13 07:51:23.713968
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.playbook.attribute import FieldAttribute
    attr = FieldAttribute()
    print(attr.isa)
    print(attr.private)
    print(attr.default)

# call the test function
#test_FieldAttribute()

# Generated at 2022-06-13 07:51:32.753151
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int')
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None

    attr = Attribute(isa='int', default='123', listof='string')
    assert attr.private is False
    assert attr.default == '123'
    assert attr.required is False
    assert attr.listof == 'string'
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False


# Generated at 2022-06-13 07:51:41.073127
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
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False


# Generated at 2022-06-13 07:51:42.219837
# Unit test for constructor of class Attribute
def test_Attribute():
    Attribute(alias='foo')


# Generated at 2022-06-13 07:51:51.663877
# Unit test for constructor of class Attribute
def test_Attribute():
    import warnings
    warnings.filterwarnings("ignore")

    a = Attribute(isa='int', private=True, default=0, required=True, listof='int')
    assert a.isa == 'int'
    assert a.private is True
    assert a.default == 0
    assert a.required is True
    assert a.listof == 'int'
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.extend is False
    assert a.prepend is False
    assert a.static is False



# Generated at 2022-06-13 07:51:53.146968
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute()
    assert x.isa is None
    x = Attribute('bool')
    assert x.isa is 'bool'



# Generated at 2022-06-13 07:51:53.670201
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass


# Generated at 2022-06-13 07:52:04.252853
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', class_type='str', prepend=True, extend=False)
    assert a.isa == 'str'
    assert a.class_type == 'str'
    assert a.prepend
    assert not a.extend

    b = FieldAttribute(isa='str', class_type='str', prepend=False, extend=True)
    assert b.isa == 'str'
    assert b.class_type == 'str'
    assert not b.prepend
    assert b.extend

    try:
        c = Attribute(isa='list', default=[])
    except TypeError:
        pass
    else:
        raise Error

# Generated at 2022-06-13 07:52:08.959359
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa = 'dict')
    assert a is not None
    assert isinstance(a, Attribute)

    # Verify that the constructor handled a passed keyword argument
    assert a.isa == 'dict'
    assert a.isa is not None


# Generated at 2022-06-13 07:52:18.452498
# Unit test for constructor of class Attribute
def test_Attribute():

    # check all inputs
    a = Attribute(isa='string', private=True, default='foo', required=True, listof=None,
        priority=0, class_type=None, always_post_validate=True, inherit=True, alias='attr')
    a = Attribute(isa='foo', private='bar', default=None, required=False, listof='foo',
        priority='bar', class_type=None, always_post_validate='bar', inherit='bar', alias=None)
    a = Attribute()

    # check isa
    a = Attribute(isa='boolean', default='foobar')
    assert a.isa == 'boolean', "isa value is not 'boolean'"

    # check default
    a = Attribute(default='foobar')

# Generated at 2022-06-13 07:52:33.219922
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa1 = FieldAttribute(required=True)
    assert fa1.private==False
    assert fa1.default == None
    assert fa1.required == True
    assert fa1.listof == None
    assert fa1.priority == 0
    assert fa1.class_type == None
    assert fa1.always_post_validate == False
    assert fa1.inherit == True
    assert fa1.alias == None
    assert fa1.extend == False
    assert fa1.prepend == False
    assert fa1.static == False

    fa2 = FieldAttribute(default = True)
    assert fa2.default == True

    fa3 = FieldAttribute(private = True)
    assert fa3.private == True

    fa4 = FieldAttribute(listof = True)
    assert fa4.listof == True
    fa

# Generated at 2022-06-13 07:52:37.897652
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().isa == None
    assert FieldAttribute().private == False
    assert FieldAttribute().default == None
    assert FieldAttribute().required == False
    assert FieldAttribute().listof == None
    assert FieldAttribute().priority == 0
    assert FieldAttribute().class_type == None
    assert FieldAttribute().always_post_validate == False
    assert FieldAttribute().inherit == True
    assert FieldAttribute().alias == None
    assert FieldAttribute().extend == False
    assert FieldAttribute().prepend == False
    assert FieldAttribute().static == False



# Generated at 2022-06-13 07:52:43.088316
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

    a = Attribute(isa='int', private=True, default=3, required=True, listof='string', priority=1, class_type='String',
                  always_post_validate=True, inherit=False, prepend=True, static=True, alias='foo')

    a_copy = copy(a)
    a_deepcopy = deepcopy(a)

    assert a_copy.isa == 'int'
    assert a_copy.private == True


# Generated at 2022-06-13 07:52:45.788917
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    # TODO - Write a proper unit test for this constructor


# Generated at 2022-06-13 07:52:51.267085
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        required=False,
        isa='list',
        default=[],
        listof='dict',
        always_post_validate=True,
        inherit=False,
        static=True
    )
    assert a.isa == 'list'
    assert a.default == []
    assert a.listof == 'dict'
    assert a.always_post_validate == True
    assert a.inherit == False
    assert a.static == True

# Generated at 2022-06-13 07:53:02.683529
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    def compare_field(field_attr, attr_name, attr_value):
        if getattr(field_attr, attr_name, None) != attr_value:
            raise Exception('%s %s should be %s' % (field_attr, attr_name, attr_value))

    # Test ClassNameFieldAttribute constructor with known good inputs
    field_attr1 = FieldAttribute(isa='int', private=True, default=1, required=True, listof='int', priority=0, class_type='int', always_post_validate=True, inherit=False, alias='field_name')
    compare_field(field_attr1, 'isa', 'int')
    compare_field(field_attr1, 'private', True)
    compare_field(field_attr1, 'default', 1)
    compare_

# Generated at 2022-06-13 07:53:03.801575
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()



# Generated at 2022-06-13 07:53:06.842677
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    Attribute = FieldAttribute(isa=str, class_type=str)
    assert Attribute.isa == str
    assert Attribute.class_type == str


# Generated at 2022-06-13 07:53:12.049381
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute('test', False, 'hello', True, 0, 'test1')
    assert field.isa == 'test'
    assert not field.private
    assert field.default == 'hello'
    assert field.required
    assert field.priority == 0
    assert field.class_type == 'test1'


# Generated at 2022-06-13 07:53:21.083478
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(isa="Foo")
    assert attribute.isa == "Foo"
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
    assert attribute.isa == "Foo"
    assert attribute.isa == "Foo"
    



# Generated at 2022-06-13 07:53:43.589923
# Unit test for constructor of class Attribute
def test_Attribute():
    defaults = {'isa': None, 'default': None, 'required': False, 'listof': None,
                'priority': 0, 'class_type': None, 'always_post_validate': False,
                'inherit': True, 'alias': None, 'extend': False, 'prepend': False, 'static': False}

    # Test attributes of an empty instance
    field = FieldAttribute()
    for k,v in defaults.items():
        assert getattr(field, k) == v

    # Test attributes of a fully instantiated instance

# Generated at 2022-06-13 07:53:53.678352
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str')
    assert a.isa == 'str'
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate is False
    assert a.inherit is True
    assert a.alias is None

    b = Attribute(isa='list', listof='int')
    assert b.listof == 'int'

    c = Attribute(isa='int', required=True)
    assert c.required is True

    d = Attribute(isa='dict', default={'x': 1})
    assert d.default == {'x': 1}


# Generated at 2022-06-13 07:53:57.215130
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.default == None
    a = Attribute(default='test')
    assert a.default == 'test'

# Generated at 2022-06-13 07:54:02.742809
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(
        isa='str',
        private=True,
        default='random',
        class_type=str,
        always_post_validate=True
        )
    assert attr.isa == 'str'
    assert attr.private == True
    assert attr.default == 'random'
    assert attr.class_type == str
    assert attr.always_post_validate == True



# Generated at 2022-06-13 07:54:15.066474
# Unit test for constructor of class Attribute
def test_Attribute():

    # Default constructor
    a = FieldAttribute()

    # Named constructor
    b = FieldAttribute(
        isa='string',
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

    # Named constructor with argument named 'name'

# Generated at 2022-06-13 07:54:20.033010
# Unit test for constructor of class Attribute
def test_Attribute():
    Field = FieldAttribute()
    assert Field.private == False
    assert Field.default == None
    assert Field.required == False
    assert Field.listof == None
    assert Field.priority == 0
    assert Field.class_type == None
    assert Field.always_post_validate == False
    assert Field.inherit == True
    assert Field.alias == None


# Generated at 2022-06-13 07:54:21.725281
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().isa == None
    assert FieldAttribute().private == False



# Generated at 2022-06-13 07:54:30.676463
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a1 = FieldAttribute(isa='dict')
    a1.isa == 'dict'
    a2 = FieldAttribute(isa='dict', required=True)
    a2.isa == 'dict'
    a2.required == True
    a3 = FieldAttribute(isa='dict', listof=dict)
    try:
        a3.isa == 'dict'
        a3.listof == dict
    except TypeError as e:
        print(e)
    else:
        raise AssertionError()
    a4 = FieldAttribute(isa='dict', class_type=dict)
    a4.isa == 'dict'
    a4.class_type == dict
    
    

# used for action plugins

# Generated at 2022-06-13 07:54:33.189433
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        Attribute(default={})
    except TypeError as e:
        print(e)
    else:
        assert False, "Attribute constructor did not raise TypeError for mutable default"

# Generated at 2022-06-13 07:54:35.143219
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="a")
    assert a is not None


# TODO: move mock_obj to a general testing utilities file

# Generated at 2022-06-13 07:55:10.849857
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='str').isa == 'str'

    # Test that a default value is allowed if it is a callable
    # (since the theory is that it only gets called once)
    assert Attribute().default is None
    def test_default():
        return []
    assert Attribute(default=test_default).default == []

    # Test that a default value is not allowed if it is not
    # a callable (since it would be called for each new Attribute instance)
    try:
        Attribute(default='string')
    except TypeError:
        pass
    else:
        raise Exception('should have raised TypeError')

# Generated at 2022-06-13 07:55:16.053764
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(priority=42)
    assert fa.priority == 42

    # assert Attribute.__init__ doesn't throw exception
    fa = FieldAttribute(default='foo')
    fa = FieldAttribute(default=['foo', 'bar'])

    # assert Attribute.__init__ does throw exception
    try:
        fa = FieldAttribute(default={'foo': 'bar'})
        assert 'Attribute initialized'
    except TypeError:
        pass



# Generated at 2022-06-13 07:55:18.781184
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='boolean', default=True, private=True)
    assert a.isa == 'boolean'
    assert a.default is True
    assert a.private is True

# Generated at 2022-06-13 07:55:30.256582
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='bool',
                     private=True,
                     default=None,
                     required=False,
                     listof='int',
                     priority=0,
                     class_type=None,
                     always_post_validate=False,
                     inherit=False,
                     alias='my_bool',
                     extend=False,
                     prepend=False,
                     static=False
                     )

    assert attr.isa == 'bool', \
        'Attribute(): test for constructor failed: isa field is %r, expecting %r' % (
        attr.isa, 'bool')
    assert attr.private is True, \
        'Attribute(): test for constructor failed: private field is %r, expecting %r' % (
        attr.private, True)

# Generated at 2022-06-13 07:55:42.299852
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa = 'list', private=True, default='hello', required=True,
                    listof='int', priority=10, class_type='class', always_post_validate=True,
                    inherit=False)

    assert attr.isa == 'list'
    assert attr.private is True
    assert attr.default == 'hello'
    assert attr.required is True
    assert attr.listof == 'int'
    assert attr.priority == 10
    assert attr.class_type == 'class'
    assert attr.always_post_validate is True
    assert attr.inherit is False
    print('test_Attribute() passed')


# Generated at 2022-06-13 07:55:53.224281
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(
        isa='string',
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=10,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False
    )
    assert attribute.isa == 'string'
    assert attribute.private == False
    assert attribute.default == None
    assert attribute.required == False
    assert attribute.listof == None
    assert attribute.priority == 10
    assert attribute.class_type == None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias == None
    assert attribute.extend == False
   

# Generated at 2022-06-13 07:56:02.807193
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa="test", private=True, default="test", required=True,
                listof="test", priority=1, class_type="test", always_post_validate=True,
                inherit=False, alias="test", extend=False, prepend=True)
    assert field_attribute.isa == "test"
    assert field_attribute.private == True
    assert field_attribute.default == "test"
    assert field_attribute.required == True
    assert field_attribute.listof == "test"
    assert field_attribute.priority == 1
    assert field_attribute.class_type == "test"
    assert field_attribute.always_post_validate == True
    assert field_attribute.inherit == False
    assert field_attribute.alias == "test"

# Generated at 2022-06-13 07:56:05.933794
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='bool', default=False)

# W0212: Access to a protected member %r of a client class



# Generated at 2022-06-13 07:56:11.327253
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='dict', listof='string', required=True, class_type=dict, priority=1)
    assert attr.isa is 'dict'
    assert attr.listof is 'string'
    assert attr.class_type is dict
    assert attr.required
    assert attr.priority == 1



# Generated at 2022-06-13 07:56:17.696954
# Unit test for constructor of class Attribute
def test_Attribute():
    my_attr = FieldAttribute(isa='dict')
    assert my_attr.isa == 'dict'
    assert my_attr.default is None
    assert my_attr.required is False
    assert my_attr.listof is None
    assert my_attr.priority == 0
    assert my_attr.class_type is None
    assert my_attr.always_post_validate is False
    assert my_attr.inherit is True
    assert my_attr.alias is None
    assert my_attr.extend is False
    assert my_attr.prepend is False
    assert my_attr.static is False

    # Test the Class methods for isa
    # fail_isa is when the type is not allowed for the class
    fail_isa = FieldAttribute(isa='badValue')
    assert fail_isa.isa == 'badValue'

# Generated at 2022-06-13 07:57:17.859795
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list')
    assert a.isa == 'list'

# Generated at 2022-06-13 07:57:31.764680
# Unit test for constructor of class Attribute
def test_Attribute():

    # Default constructor.
    obj = Attribute()

    # Overwrite default values by "parameterised" constructor.
    # Note that in Python, a function parameter may be assigned
    # a value only once. If a parameter is given multiple
    # values, the last given one will be used.
    obj = Attribute(isa="string", private=True, default=False, required=False, listof="string", priority=0)

    # Invalid constructions:
    #   Attribute(invalid=1) # invalid keyword argument not supported
    #   Attribute(isa) # missing keyword argument
    #   Attribute(isa="string", isa="integer") # duplicate keyword argument

    # Check that an immutable datastructure is forbidden as a default.

# Generated at 2022-06-13 07:57:36.379703
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    t = FieldAttribute(isa='list', listof='str')
    if t.isa != 'list' or t.listof != 'str':
        raise AssertionError('TypeError: expected isa=list, listof=str.')
    t.default = list
    if t.default != list:
        raise AssertionError('TypeError: expected t.default=list')

# Generated at 2022-06-13 07:57:42.043499
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
            isa=int,
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
    assert(isinstance(f, Attribute))


# Generated at 2022-06-13 07:57:49.273605
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:57:54.490588
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import pytest
    x = FieldAttribute()
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
    x = FieldAttribute(isa="str", private=False, default="default", required=False, listof=False, priority=1, class_type=None,
                       always_post_validate=False, inherit=True, alias="alias", extend=False, prepend=False, static=False)
   

# Generated at 2022-06-13 07:57:57.053503
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    val = FieldAttribute(
        isa='str'
    )

    assert val.isa == 'str'
    assert val.default == None


# Generated at 2022-06-13 07:58:06.591565
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test only the constructor
    attr = FieldAttribute(isa='str', default='foo')
    assert attr.isa == 'str'
    assert attr.private == False
    assert attr.default == 'foo'
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



# Generated at 2022-06-13 07:58:10.473947
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    x = FieldAttribute(isa='int')
    assert x.isa == 'int'

    x = FieldAttribute(isa='str')
    assert x.isa == 'str'

    x = FieldAttribute(isa='class')
    assert x.isa == 'class'


# Generated at 2022-06-13 07:58:13.505437
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FieldAttribute(isa="list", default = [])
    except TypeError:
        assert True
    else:
        assert False

    assert FieldAttribute(isa="list", default = lambda: [])