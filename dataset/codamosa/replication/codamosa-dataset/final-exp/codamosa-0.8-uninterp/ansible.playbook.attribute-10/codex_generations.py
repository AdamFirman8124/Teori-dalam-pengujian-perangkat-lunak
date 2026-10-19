

# Generated at 2022-06-13 07:49:15.395073
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        x = FieldAttribute(default={})
    except TypeError:
        pass
    else:
        raise AssertionError('FieldAttribute was instantiated with a mutable default')

    x = FieldAttribute(default=())
    assert x
    x = FieldAttribute(default=[])
    assert x
    x = FieldAttribute(default=set())
    assert x
    x = FieldAttribute(default=lambda: {})
    assert x
    x = FieldAttribute(default=lambda: [])
    assert x
    x = FieldAttribute(default=lambda: set())
    assert x
    x = FieldAttribute(default=lambda: ())
    assert x
test_FieldAttribute()



# Generated at 2022-06-13 07:49:25.677985
# Unit test for constructor of class Attribute
def test_Attribute():
    isa=None
    private=False
    default=None
    required=False
    listof=None
    priority=0
    class_type=None
    always_post_validate=False
    inherit=True

    attr = Attribute(isa, private, default, required, listof, priority, class_type, always_post_validate, inherit)
    assert attr.isa == isa
    assert attr.private == private
    assert attr.default == default
    assert attr.required == required
    assert attr.listof == listof
    assert attr.priority == priority
    assert attr.class_type == class_type
    assert attr.always_post_validate == always_post_validate
    assert attr.inherit == inherit


# Generated at 2022-06-13 07:49:35.312215
# Unit test for constructor of class Attribute
def test_Attribute():
    simple = Attribute(isa='int', required=True, default=2)
    assert simple.isa is int
    assert simple.private is False
    assert simple.required is True
    assert simple.default == 2
    assert simple.priority == 0

    assert not hasattr(simple, 'inherit')
    assert not hasattr(simple, 'alias')
    assert not hasattr(simple, 'extend')
    assert not hasattr(simple, 'prepend')
    assert not hasattr(simple, 'static')

    complexe = Attribute(
        isa='list',
        private=True,
        required=True,
        default='complexe.txt',
        priority=2,
        inherit=False,
        alias='complex',
        extend=True,
        prepend=False,
        static=False
    )

   

# Generated at 2022-06-13 07:49:37.060645
# Unit test for constructor of class Attribute
def test_Attribute():
    fl = Attribute(isa='list')
    fl1 = Attribute(isa='list', default=lambda: [])



# Generated at 2022-06-13 07:49:43.808181
# Unit test for constructor of class Attribute
def test_Attribute():

    obj = Attribute()

    # Default values
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


# Generated at 2022-06-13 07:49:46.473780
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()
    f2 = FieldAttribute('dict')
    f3 = FieldAttribute('dict', listof='list')
    f4 = FieldAttribute('list', class_type='int')
    f5 = FieldAttribute('list', default=lambda: [1,2,3])
    f6 = FieldAttribute('list', default=list())


# Generated at 2022-06-13 07:49:47.948253
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert type(field) == FieldAttribute



# Generated at 2022-06-13 07:49:50.402086
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()
    assert(field_attribute != None)


# Generated at 2022-06-13 07:49:52.200684
# Unit test for constructor of class Attribute
def test_Attribute():
    attributes = Attribute()
    assert isinstance(attributes, Attribute)


# Generated at 2022-06-13 07:50:04.119151
# Unit test for constructor of class Attribute
def test_Attribute():
    obj = Attribute(
        isa=dict,
        private=True,
        default=dict(key=3),
        required=True,
        listof=str,
        priority=3,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias='obj'
    )
    assert obj.isa == dict
    assert obj.private
    assert obj.default == dict(key=3)
    assert obj.required
    assert obj.listof == str
    assert obj.priority == 3
    assert obj.class_type == None
    assert not obj.always_post_validate
    assert obj.inherit
    assert obj.alias == 'obj'



# Generated at 2022-06-13 07:50:17.053041
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list', private=False, default=None, required=False, listof=None,
            priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None,
            extend=False, prepend=False, static=False)

    assert attr.isa == 'list', 'Wrong isa attribute'
    assert attr.private == False, 'Wrong private attribute'
    assert attr.default == None, 'Wrong default attribute'
    assert attr.required == False, 'Wrong required attribute'
    assert attr.listof == None, 'Wrong listof attribute'
    assert attr.priority == 0, 'Wrong priority attribute'
    assert attr.class_type == None, 'Wrong class_type attribute'
    assert attr.always

# Generated at 2022-06-13 07:50:26.925905
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

    a = Attribute(isa='int', private=False, default=42)
    assert a.isa == 'int'
    assert a.private == False
    assert a.default == 42
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a

# Generated at 2022-06-13 07:50:36.840426
# Unit test for constructor of class Attribute
def test_Attribute():
    class AttributeTest(object):
        a = FieldAttribute(isa='str', default='a', required=True, listof='str', priority=0, class_type='str', always_post_validate=False, inherit=True, alias='a_alias')
        b = FieldAttribute(isa='str', default='b', required=True, listof='str', priority=0, class_type='str', always_post_validate=False, inherit=True, alias='a_alias')

    obj_1 = AttributeTest()
    obj_2 = AttributeTest()

    assert obj_1 == obj_2
    assert obj_1 <= obj_2
    assert obj_1 >= obj_2


# Generated at 2022-06-13 07:50:45.280660
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    '''
    Constructor of class FieldAttribute
    '''
    isa = str
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
    f = FieldAttribute(isa=isa, private=private, default=default, required=required, listof=listof, priority=priority, class_type=class_type,
                        always_post_validate=always_post_validate, inherit=inherit, alias=alias, extend=extend, prepend=prepend, static=static)

    assert f.isa == isa
    assert f.private == private
    assert f.default == default
   

# Generated at 2022-06-13 07:50:46.617121
# Unit test for constructor of class Attribute
def test_Attribute():
    pass


# Generated at 2022-06-13 07:50:59.261164
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', private=True, default=False, required=True, listof='string',
                  priority=0, class_type=True, always_post_validate=True,
                  inherit=True, alias='alias', extend=True, prepend=False,
                  static=True)

    assert a.isa == 'list'
    assert a.private is True
    assert a.default is False
    assert a.required is True
    assert a.listof == 'string'
    assert a.priority == 0
    assert a.class_type is True
    assert a.always_post_validate is True
    assert a.inherit is True
    assert a.alias == 'alias'
    assert a.extend is True
    assert a.prepend is False
    assert a.static is True


# Unit

# Generated at 2022-06-13 07:51:08.629495
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import yaml
    from collections import namedtuple
    from ansible.playbook.play import Play
    FA = FieldAttribute
    # Test all the different types of constructors for FieldAttribute
    fa = FA(isa='list')
    assert isinstance(fa, FA)
    fa = FA(isa='dict')
    assert isinstance(fa, FA)
    fa = FA(isa='str')
    assert isinstance(fa, FA)
    fa = FA(isa='list', default=[])
    assert isinstance(fa, FA)
    fa = FA(isa='int', default=0)
    assert isinstance(fa, FA)
    fa = FA(isa='bool', default=False)
    assert isinstance(fa, FA)
    fa = FA(isa='list', default=[], inherit=True)

# Generated at 2022-06-13 07:51:16.219367
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        # Test that mutable defaults fail
        FieldAttribute(isa='test', default={})
    except TypeError:
        pass
    else:
        raise TypeError('Default immutable containers must not be accepted')

    # Test that immutable defaults are accepted
    FieldAttribute(isa='test', default=set)
    FieldAttribute(isa='test', default=lambda: {'default': 'value'})

    # Test that callable defaults with side effects are not allowed
    def sideeffect():
        sideeffect.called = True
        return True
    sideeffect.called = False

    try:
        FieldAttribute(isa='test', default=sideeffect)
    except TypeError:
        pass
    else:
        raise TypeError('Default callables with side-effects must not be accepted')

    # Test that callable defaults without side effects are allowed
    Field

# Generated at 2022-06-13 07:51:17.313547
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()



# Generated at 2022-06-13 07:51:23.565523
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', static=False, alias=None)
    assert a.isa == 'str'
    assert a.static == False
    assert a.alias == None
    b = Attribute(isa='str', static=False, alias=None)
    assert a == b
    c = Attribute(isa='str', static=True, alias=None)
    assert a != c
    assert a < c
    assert c > a
    assert a <= c
    assert c >= a

# Generated at 2022-06-13 07:51:34.141745
# Unit test for constructor of class Attribute
def test_Attribute():
    test_dict = dict(
        isa=str,
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        alias=None,
    )
    test_attribute = Attribute(**test_dict)
    assert test_attribute.isa == test_dict['isa']
    assert test_attribute.private == test_dict['private']
    assert test_attribute.default == test_dict['default']
    assert test_attribute.required == test_dict['required']
    assert test_attribute.listof == test_dict['listof']
    assert test_attribute.priority == test_dict['priority']
    assert test_attribute.class_type == test_dict['class_type']


# Generated at 2022-06-13 07:51:41.223951
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', default='bar', required=True, priority=10)

    assert attr.isa == 'str'
    assert attr.private is False
    assert attr.default == 'bar'
    assert attr.required is True
    assert attr.priority == 10
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True



# Generated at 2022-06-13 07:51:52.750197
# Unit test for constructor of class Attribute
def test_Attribute():
    # init takes a valid argument
    a = Attribute(isa='list')

    # init takes no arguments
    a = Attribute()

    # init takes a valid keyword argument
    a = Attribute(listof='dict')

    # init takes no positional arguments
    try:
        a = Attribute('list', 'list')
    except TypeError:
        pass

    # init takes the named argument isa
    a = Attribute(isa='list')

    # init takes the named argument default
    a = Attribute(default=None)

    # init takes the named argument required
    a = Attribute(required=False)

    # init takes the named argument listof
    a = Attribute(listof='list')

    # init takes the named argument priority
    a = Attribute(priority=0)

    # init takes the named argument class_

# Generated at 2022-06-13 07:52:02.456705
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='test')

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
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False



# Generated at 2022-06-13 07:52:14.360269
# Unit test for constructor of class Attribute
def test_Attribute():
    # All parameters
    attr = Attribute(
        'class',
        always_post_validate=True,
        private=True,
        default='test_default',
        required=True,
        listof='integer',
        priority=99,
        class_type=Attribute,
        inherit=False,
        alias='test_alias',
        extend=True,
        prepend=True,
        static=True,
    )
    assert attr.isa == 'class'
    assert attr.always_post_validate
    assert attr.private
    assert attr.default == 'test_default'
    assert attr.required
    assert attr.listof == 'integer'
    assert attr.priority == 99
    assert attr.class_type == Attribute
    assert not attr.inherit


# Generated at 2022-06-13 07:52:18.700960
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='string')
    assert a.isa == 'string'
    try:
        a = Attribute(isa='list', default=['foo'])
        assert False, "constructor should have failed"
    except TypeError:
        pass

# Generated at 2022-06-13 07:52:20.058788
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='list')
    assert fa.isa ==  'list'

# Generated at 2022-06-13 07:52:27.794688
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test basic initialization of class FieldAttribute()
    myfield = FieldAttribute(isa='bool', default=False)
    assert myfield.isa == 'bool', 'isa is not properly set to \'bool\''

    # Test that providing an invalid isa type raises a TypeError
    try:
        FieldAttribute(isa='foo')
    except TypeError:
        pass
    except:
        assert False, 'isa was set to \'foo\' but an invalid TypeError was thrown'
    else:
        assert False, 'isa was set to \'foo\' but no TypeError was thrown'

    # Test that the default value is properly returned
    assert myfield.default == False, 'default not properly set to False'

    # Test that Mutable objects for default values raise TypeError

# Generated at 2022-06-13 07:52:29.717982
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='string', default='whatever')
    assert a.isa == 'string'
    assert a.default == 'whatever'

# Generated at 2022-06-13 07:52:37.184674
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing import vault
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var as u

    assert Attribute(isa='list') == Attribute(isa='list')

    a = Attribute(isa='bool', default=True)
    assert a == Attribute(isa='bool', default=True)
    assert a != Attribute(isa='bool', default=False)
    assert a == Attribute(isa='bool', default=True)
    assert a != Attribute(isa='bool', default=False)

    assert a.default is True
    a.default = False
    assert a.default is False

    # is same as a.default == False
    assert not a.default


# Generated at 2022-06-13 07:52:48.370813
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='list', private=False, default=None, required=False, listof='str', priority=0, class_type=None)
    assert attr.isa == 'list'
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof == 'str'
    assert attr.priority == 0
    assert attr.class_type is None

# Generated at 2022-06-13 07:52:51.536085
# Unit test for constructor of class Attribute
def test_Attribute():
    class TestClass:
        test_attribute = Attribute(isa='string')

    tc = TestClass()

    assert tc.test_attribute == 'string'

# Legacy class name
Field = FieldAttribute

# Generated at 2022-06-13 07:52:56.580868
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    s = FieldAttribute("dict")
    assert s.isa == "dict"

    s = FieldAttribute("dict", True)
    assert s.isa == "dict"
    assert s.private == True

    s = FieldAttribute("dict", private=True)
    assert s.isa == "dict"
    assert s.private == True


# Generated at 2022-06-13 07:52:58.270500
# Unit test for constructor of class Attribute
def test_Attribute():
    att = Attribute(isa='dict')
    assert att.isa == 'dict'

# Generated at 2022-06-13 07:53:06.197216
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    attr = Attribute(isa='bool', private=True)
    attr = Attribute(isa='bool', private=True, default=True)
    attr = Attribute(isa='bool', required=True, default=False)
    attr = Attribute(isa='bool', listof='bool')
    attr = Attribute(isa='bool', priority=10, class_type=True)
    attr = Attribute(isa='bool', always_post_validate=True)
    attr = Attribute(isa='bool', inherit=False)
    attr = Attribute(isa='bool', alias='foo')

# Generated at 2022-06-13 07:53:12.988367
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    expected_result = {
        'isa': None,
        'private': False,
        'default': None,
        'required': False,
        'listof': None,
        'priority': 0,
        'class_type': None,
        'always_post_validate': False,
        'inherit': True,
        'alias': None
    }
    assert FieldAttribute().__dict__ == expected_result


# Generated at 2022-06-13 07:53:27.539871
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='int', private=True)
    assert(field.isa == 'int')
    assert(field.private)
    assert(not field.required)
    assert(field.listof is None)
    assert(field.priority == 0)
    assert(field.class_type is None)
    assert(not field.always_post_validate)
    assert(field.inherit)
    assert(field.alias is None)
    assert(not field.extend)
    assert(not field.prepend)
    assert(not field.static)

    # Test immutable defaults
    # if not callable
    try:
        field = FieldAttribute(isa='list', default={'foo': 'bar'})
    except TypeError:
        pass

# Generated at 2022-06-13 07:53:34.367878
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()

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



# Generated at 2022-06-13 07:53:43.410765
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.parsing import vault
    from ansible.inventory import Group
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    isa = False
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


# Generated at 2022-06-13 07:53:48.980337
# Unit test for constructor of class Attribute
def test_Attribute():
    attr_test = Attribute(isa='list', private=False, default=None, required=False, listof=None, \
                          priority=0, class_type=None, always_post_validate=False, inherit=True, \
                          alias=None, extend=False, prepend=False, static=False)


# Generated at 2022-06-13 07:54:06.316507
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.isa == None
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False


# Generated at 2022-06-13 07:54:19.046810
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int', default=0, listof='dict')
    def default_for_dict():
        return {"x":1, "y": 2}


# Generated at 2022-06-13 07:54:25.585113
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute(
        isa='list',
        private=True,
        default=[],
        listof='list',
        priority=1,
        class_type=None,
        always_post_validate=False,
        extend=False,
        prepend=False,
        static=False,
    )
    print(attribute.__dict__)

if __name__ == "__main__":
    # test_Attribute()
    print("hello Attribute")

# Generated at 2022-06-13 07:54:25.992689
# Unit test for constructor of class Attribute
def test_Attribute():
    pass

# Generated at 2022-06-13 07:54:35.497306
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import types

    attr = FieldAttribute()
    assert isinstance(attr.isa, types.NoneType)
    assert attr.private is False
    assert isinstance(attr.default, types.NoneType)
    assert attr.required is False
    assert isinstance(attr.listof, types.NoneType)
    assert attr.priority == 0
    assert isinstance(attr.class_type, types.NoneType)
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert isinstance(attr.alias, types.NoneType)
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False


# Generated at 2022-06-13 07:54:38.638546
# Unit test for constructor of class Attribute
def test_Attribute():
    test_attr = Attribute(alias="test_attr")
    if test_attr.alias != "test_attr":
        # This error is thrown because the constructor of class Attribute does not set the alias attribute
        raise TypeError('__init__() does not set the "alias" attribute')

test_Attribute()

# Generated at 2022-06-13 07:54:44.757612
# Unit test for constructor of class Attribute
def test_Attribute():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    #pylint: disable=unused-variable
    a = Attribute(isa='string')
    a = Attribute(isa='AnsibleVaultEncryptedUnicode')
    a = Attribute(isa='int')
    a = Attribute(isa='float')
    a = Attribute(isa='bool')
    a = Attribute(isa='complex')
    a = Attribute(isa='set')
    a = Attribute(isa='list')
    a = Attribute(isa='dict')
    a = Attribute(isa=list)
    a = Attribute(isa=dict)
    a = Attribute(isa=AnsibleVaultEncryptedUnicode)

# Generated at 2022-06-13 07:54:55.088295
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = FieldAttribute(isa='list',
                   private=True, 
                   default=['b', 'c'],
                   required=False,
                   listof='int',
                   priority=2,
                   class_type='xx',
                   always_post_validate=False,
                   inherit=True,
                   alias='aa',
                   extend=False,
                   prepend=False,
                   static=False
                   )
    assert attr.isa == 'list'
    assert attr.private == True
    assert attr.required == False
    assert attr.listof == 'int'
    assert attr.priority == 2
    assert attr.class_type == 'xx'
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == 'aa'

# Generated at 2022-06-13 07:55:02.561558
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    fa = FieldAttribute()

    # test that our constructor generates the expected
    # Attribute object, defaults are taken from the top
    # of the code.  The primary reason is to ensure the
    # defaults are properly documented.
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



# Generated at 2022-06-13 07:55:12.564952
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.vars import AnsibleVars
    var = AnsibleVars()
    test_obj = Attribute(isa=dict(a=0),
                         private=True,
                         default=dict(b=1),
                         required=False,
                         listof=dict(c=2),
                         priority=0,
                         class_type=type(var),
                         always_post_validate=False,
                         inherit=True,
                         alias='alias_name',
                         extend=False,
                         prepend=False,
                         static=False,
                        )
    assert test_obj.isa == dict(a=0)
    assert test_obj.private == True
    assert test_obj.default == dict(b=1)
    assert test_obj.required == False

# Generated at 2022-06-13 07:55:30.002953
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()


# Generated at 2022-06-13 07:55:43.288630
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    attr.isa = 'dict'
    attr.private = False
    attr.default = {'name': 'default'}
    attr.required = False
    attr.listof = None
    attr.priority = 1
    attr.class_type = None
    attr.always_post_validate = False
    attr.inherit = True
    attr.alias = None
    attr.extend = False
    attr.prepend = False
    attr.static = False

    assert attr.isa == 'dict'
    assert attr.private == False
    assert attr.default == {'name': 'default'}
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 1

# Generated at 2022-06-13 07:55:52.287949
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a is not None
    a = Attribute(1, True, 2, True, 3, 4, 5, True, True, None, True, True)
    assert a is not None
    a = Attribute(
        isa=1,
        private=True,
        default=2,
        required=True,
        listof=3,
        priority=4,
        class_type=5,
        always_post_validate=True,
        inherit=True,
        alias=None,
        extend=True,
        prepend=True,
    )
    assert a is not None



# Generated at 2022-06-13 07:56:02.075513
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute().isa is None
    assert Attribute().private is False
    assert Attribute().default is None
    assert Attribute().required is False
    assert Attribute().listof is None
    assert Attribute().priority == 0
    assert Attribute().class_type is None
    assert Attribute().always_post_validate is False
    assert Attribute().inherit is True
    assert Attribute().alias is None
    assert Attribute().extend is False
    assert Attribute().prepend is False
    assert Attribute().static is False

    def default_func(*args, **kwargs):
        pass

    # Test that an exception is raised for mutable defaults
    try:
        Attribute(default=['test'])
        assert False
    except TypeError as e:
        assert 'may not be mutable' in str(e)

# Generated at 2022-06-13 07:56:14.091298
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    Test that the correct values are set for all arguments in the Attribute constructor.
    """
    test_args = {
        'isa' : 'test_isa',
        'private' : 'test_private',
        'default' : 'test_default',
        'required' : 'test_required',
        'listof' : 'test_listof',
        'priority' : 'test_priority',
        'class_type' : 'test_class_type',
        'always_post_validate' : 'test_always_post_validate',
        'inherit' : 'test_inherit',
        'alias' : 'test_alias',
        'extend' : 'test_extend',
        'prepend' : 'test_prepend'
    }

# Generated at 2022-06-13 07:56:25.007152
# Unit test for constructor of class Attribute
def test_Attribute():
    field_attribute = Attribute(
            isa='str',
            private=False,
            default='test',
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
    assert field_attribute.isa == 'str'
    assert field_attribute.private == False
    assert field_attribute.default == 'test'
    assert field_attribute.required == False
    assert field_attribute.listof is None
    assert field_attribute.priority == 0
    assert field_attribute.class_type is None
    assert field_attribute.always_post_validate == False

# Generated at 2022-06-13 07:56:35.277735
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='str', private=False, default=None, required=False, listof=None, priority=0,
                       class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False,
                       static=False)
    assert(a.isa == 'str')
    assert(a.private == False)
    assert(a.default == None)
    assert(a.required == False)
    assert(a.listof == None)
    assert(a.priority == 0)
    assert(a.class_type == None)
    assert(a.always_post_validate == False)
    assert(a.inherit == True)
    assert(a.alias == None)
    assert(a.extend == False)

# Generated at 2022-06-13 07:56:36.178996
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute



# Generated at 2022-06-13 07:56:37.370303
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert type(a) == FieldAttribute



# Generated at 2022-06-13 07:56:48.806967
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Static field attribute
    obj = FieldAttribute()
    assert(isinstance(obj, FieldAttribute))
    assert(obj.isa == None)
    assert(obj.private == False)
    assert(obj.default == None)
    assert(obj.required == False)
    assert(obj.listof == None)
    assert(obj.priority == 0)
    assert(obj.class_type == None)
    assert(obj.always_post_validate == False)
    assert(obj.inherit == True)
    assert(obj.alias == None)
    assert(obj.extend == False)
    assert(obj.prepend == False)
    assert(obj.static == False)

    # Dynamic field attribute

# Generated at 2022-06-13 07:57:34.209389
# Unit test for constructor of class Attribute
def test_Attribute():
    def test_func():
        return 'test'

    FA = FieldAttribute(isa='str', private=True, default='test', listof='str', priority=1, class_type='str', always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    assert FA.isa == 'str'
    assert FA.private == True
    assert FA.default == 'test'
    assert FA.listof == 'str'
    assert FA.priority == 1
    assert FA.class_type == 'str'
    assert FA.always_post_validate == False
    assert FA.inherit == True
    assert FA.alias == None
    assert FA.extend == False
    assert FA.prepend == False
    assert FA.static == False


# Generated at 2022-06-13 07:57:42.936131
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert isinstance(a, FieldAttribute)
    assert isinstance(a, Attribute)
    assert a.isa == None
    assert a.priority == 0
    assert a.listof == None
    assert a.class_type == None
    assert a.always_post_validate == False

    b = FieldAttribute(isa='dict')
    assert isinstance(b, FieldAttribute)
    assert isinstance(b, Attribute)
    assert b.isa == 'dict'
    assert b.priority == 0
    assert b.listof == None
    assert b.class_type == None
    assert b.always_post_validate == False


    c = FieldAttribute(isa='dict', listof='int', priority=100, class_type=None, always_post_validate=False)

# Generated at 2022-06-13 07:57:45.805944
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='str')
    assert attr.isa == 'str'
    # test for exception
    #raise TypeError('defaults for FieldAttribute may not be mutable, please provide a callable instead')

# Generated at 2022-06-13 07:57:53.709853
# Unit test for constructor of class Attribute
def test_Attribute():
    print("test_Attribute")
    a = Attribute(
        isa="string",
        private=False,
        default=None,
        required=False,
        listof="string",
        priority=0,
        class_type="string",
        always_post_validate=False,
        inherit=True,
        alias="string"
    )

    assert isinstance(a, Attribute)
    assert a.__class__ == Attribute
    assert a.__eq__
    assert a.__ne__
    assert a.__lt__
    assert a.__gt__
    assert a.__le__
    assert a.__ge__
    assert a.__lt__
    assert a.__gt__
    assert a.__le__
    assert a.__ge__



# Generated at 2022-06-13 07:58:04.966977
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fail_attributes = [
        {
            'isa': 'list',
            'default': [],
        },
        {
            'isa': 'dict',
            'default': {},
        },
        {
            'isa': 'set',
            'default': set(),
        },
    ]

    success_attributes = [
        {
            'isa': 'list',
            'default': lambda: [],
        },
        {
            'isa': 'dict',
            'default': lambda: {},
        },
        {
            'isa': 'set',
            'default': lambda: set(),
        },
    ]

    for fail_attribute in fail_attributes:
        try:
            FieldAttribute(**fail_attribute)
        except TypeError:
            continue

# Generated at 2022-06-13 07:58:07.308699
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='bool', default=False)
    assert f.isa == 'bool'
    assert f.default == False

# Generated at 2022-06-13 07:58:13.593392
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # define a class
    class Foo(object):
        def __init__(self):
            self.bar = 0
            self.foo = "test"

    # create instance of class Foo
    f = Foo()

    # create an attr and assign it
    attr = FieldAttribute(isa="string", default="test", required=True, class_type=Foo)
    f.attr = attr

    assert f.attr.required == True
    assert f.attr.default == "test"

# Generated at 2022-06-13 07:58:17.766790
# Unit test for constructor of class FieldAttribute

# Generated at 2022-06-13 07:58:25.946510
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Input data
    isa = 'int'
    private = False
    default = 0
    required = False
    priority = 0

    # Call constructor
    attr = FieldAttribute(isa=isa, private=private, default=default,
        required=required, priority=priority)

    # Assertions
    # Assert that the values of the parameters are correctly retrieved
    assert(attr.isa == isa)
    assert(attr.private == private)
    assert(attr.default == default)
    assert(attr.required == required)
    assert(attr.priority == priority)
    # Assert that the default values of the parameters are correctly retrieved
    assert(attr.listof is None)
    assert(attr.class_type is None)
    assert(attr.always_post_validate is False)

# Generated at 2022-06-13 07:58:32.243408
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Simple constructor
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
    
    # Constructor with arguments
    a = FieldAttribute(
        isa="varchar",
        private=True,
        default="default_value",
        required=True,
        listof="integer",
        priority=99,
        class_type="class_type",
        always_post_validate=False,
        inherit=True,
        alias="alias_name",
    )
   