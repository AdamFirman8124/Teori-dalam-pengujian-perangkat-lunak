

# Generated at 2022-06-13 07:49:12.514039
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute(isa='int')
    assert f1.isa == 'int'
    f1 = FieldAttribute(isa='int',default=0)
    assert f1.isa == 'int'
    assert f1.default == 0
    f2 = FieldAttribute(isa='int',default=0)
    assert f1 == f2
    f3 = FieldAttribute(isa='str',default='str')
    assert f2 != f3
    f4 = FieldAttribute(isa='str',default='str')
    assert f3 == f4



# Generated at 2022-06-13 07:49:16.150421
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', private=False, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False)



# Generated at 2022-06-13 07:49:26.320562
# Unit test for constructor of class Attribute
def test_Attribute():
    # Automatically generated: Wed, 08 Mar 2017 15:16:20 GMT
    # DO NOT EDIT or your changes may be overwritten

    import pytest

# Generated at 2022-06-13 07:49:28.477188
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute.__init__(isa='list') == (Attribute.isa == 'list')



# Generated at 2022-06-13 07:49:35.157632
# Unit test for constructor of class Attribute
def test_Attribute():
    expected_attrib = {
        'isa': 'str',
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

    attribute = Attribute()

    for k, v in expected_attrib.items():
        # assert v == getattr(attribute, k)
        assert v == attribute.__dict__[k]

# Generated at 2022-06-13 07:49:41.832420
# Unit test for constructor of class Attribute
def test_Attribute():

    test_object = Attribute(
        isa = 'str',
        private = False,
        required = False,
        listof = None,
        priority = 0,
        class_type = None,
        always_post_validate = True,
        alias = None,
        inherit = True,
    )

    assert test_object.isa == 'str'
    assert test_object.private == False
    assert test_object.required == False
    assert test_object.listof == None
    assert test_object.priority == 0
    assert test_object.class_type == None
    assert test_object.always_post_validate == True
    assert test_object.alias == None
    assert test_object.inherit == True


# Generated at 2022-06-13 07:49:43.328239
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(isa='int')
    assert attribute.isa == 'int', 'FieldAttribute.__init__() failed'



# Generated at 2022-06-13 07:49:45.131402
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    class Test(object):
        def __init__(s):
            s.foo = FieldAttribute(isa='str', default='bar')

    t = Test()
    assert t.foo == 'bar'


# Generated at 2022-06-13 07:49:50.131560
# Unit test for constructor of class Attribute
def test_Attribute():
    test_isa_attribute = Attribute(isa='dict')
    print(test_isa_attribute)
    assert test_isa_attribute.isa == 'dict'
    assert test_isa_attribute.private == False
    assert test_isa_attribute.default is None
    assert test_isa_attribute.required == False
    assert test_isa_attribute.listof is None
    assert test_isa_attribute.priority == 0
    assert test_isa_attribute.class_type is None
    assert test_isa_attribute.always_post_validate == False
    assert test_isa_attribute.inherit == True
    assert test_isa_attribute.alias is None

    test_alias_attribute = Attribute(isa='dict', alias='mydict')
    print(test_alias_attribute)

# Generated at 2022-06-13 07:50:03.569694
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.module_utils.basic import AnsibleModule
    assert Attribute().isa == None
    assert Attribute().private == False
    assert Attribute().default == None
    assert Attribute().required == False
    assert Attribute().listof == None
    assert Attribute().priority == 0
    assert Attribute().class_type == None
    assert Attribute().always_post_validate == False
    assert Attribute().inherit == True
    assert Attribute().alias == None
    assert Attribute(isa=True, private=True, default=True, required=True,
                     listof=True, priority=10, class_type=AnsibleModule,
                     always_post_validate=True, inherit=False, alias=True).isa == True

# Generated at 2022-06-13 07:50:09.266882
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    if 1 == 1:
        field = FieldAttribute (isa='string', private=False, default=None, required=False, listof=None,
                                priority=0, class_type=None, always_post_validate=False, inherit=True,
                                alias=None, extend=False, prepend=False)

# Generated at 2022-06-13 07:50:14.576031
# Unit test for constructor of class Attribute
def test_Attribute():
    import types
    import ansible.module_utils.six as six
    import ansible.utils.boolean as boolean

    def _test_bool(x):
        return boolean.boolean(x)

    attr1 = Attribute(isa='foo')
    # Default values
    assert not attr1.private
    assert attr1.default is None
    assert not attr1.required
    assert attr1.listof is None
    assert attr1.priority == 0
    assert attr1.class_type is None
    assert not attr1.always_post_validate
    assert attr1.inherit
    assert attr1.alias is None


# Generated at 2022-06-13 07:50:19.307767
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    '''
    Unit test for constructor of class FieldAttribute
    '''
    fields = []
    fields.append(FieldAttribute(isa=str))
    fields.append(FieldAttribute(isa=str, private=True))
    fields.append(FieldAttribute(isa=str, private=True, default='test', required=True))
    fields.append(FieldAttribute(isa=str, private=True, default='test', required=True, listof=str))
    fields.append(FieldAttribute(isa=str, private=True, default='test', required=True, listof=str, priority=0))
    fields.append(FieldAttribute(isa=str, private=True, default='test', required=True, listof=str, priority=0, class_type=str))

# Generated at 2022-06-13 07:50:21.574960
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='test', private=True, default='test')

    assert(a.isa == 'test')
    assert(a.private == True)
    assert(a.default == 'test')

# Generated at 2022-06-13 07:50:28.543944
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa="dict",
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

    assert(isinstance(a, FieldAttribute))



# Generated at 2022-06-13 07:50:39.215001
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.playbook.attribute import Attribute, FieldAttribute
    # test Attribute class constructor
    default_attribute_value = {
        'isa': None,
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
    test_attribute = Attribute()
    assert test_attribute.__dict__ == default_attribute_value
    test_attribute = FieldAttribute()
    assert test_attribute.__dict__ == default_attribute_value

# Generated at 2022-06-13 07:50:53.169933
# Unit test for constructor of class Attribute

# Generated at 2022-06-13 07:51:03.177564
# Unit test for constructor of class Attribute
def test_Attribute():
    field_attribute = FieldAttribute(isa='dict', default='default_value', required=True)
    assert field_attribute.isa == 'dict'
    assert field_attribute.private == False
    assert field_attribute.default == 'default_value'
    assert field_attribute.required == True
    assert field_attribute.listof == None
    assert field_attribute.priority == 0
    assert field_attribute.class_type == None
    assert field_attribute.always_post_validate == False
    assert field_attribute.inherit == True
    assert field_attribute.alias == None
    assert field_attribute.extend == False
    assert field_attribute.prepend == False
    print("test_Attribute PASS")


# Generated at 2022-06-13 07:51:11.364384
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    def a_default():
        return "default"
    # Check valid choices for isa
    for isa in ("str", "string", "int", "float", "bool", "bool", "boolean", "dict", "list", "set", "dict", "AnsibleBaseYAMLObject", "percent"):
        a = Attribute(isa=isa)
        assert isa == a.isa, "isa has the value %s but should have had the value %s" % (a.isa, isa)
    # Check inalid choices for isa

# Generated at 2022-06-13 07:51:20.352514
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Default values
    fa = FieldAttribute()
    assert fa.__class__.__name__ == 'FieldAttribute'
    assert fa.private is False
    assert fa.default is None
    assert fa.required is False
    assert fa.listof is None
    assert fa.priority == 0
    assert fa.class_type is None
    assert fa.always_post_validate is False
    assert fa.inherit is True
    assert fa.alias is None

    # Set custom values

# Generated at 2022-06-13 07:51:21.904376
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass



# Generated at 2022-06-13 07:51:22.988275
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()


# Generated at 2022-06-13 07:51:27.693637
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='int')
    assert attr.isa == 'int'
    attr = FieldAttribute(isa='int', required=True)
    assert attr.required == True
    attr = FieldAttribute(isa='bool', required=True, default=True)
    assert attr.default is True


# Generated at 2022-06-13 07:51:32.616998
# Unit test for constructor of class Attribute
def test_Attribute():
    lib = Attribute()
    assert lib.required == False
    assert lib.private == False
    assert lib.default == None
    assert lib.isa == None
    assert lib.inherit == True
    assert lib.static == False
    assert lib.extend == False
    assert lib.prepend == False



# Generated at 2022-06-13 07:51:41.561944
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    isa=None
    private=False
    default=None
    required=False
    listof=None
    priority=0
    class_type=None
    always_post_validate=False
    inherit=True
    alias=None
    extend=False
    prepend=False
    static=False
    test_attr = FieldAttribute(
        isa,
        private,
        default,
        required,
        listof,
        priority,
        class_type,
        always_post_validate,
        inherit,
        alias,
        extend,
        prepend,
        static,
    )



# Generated at 2022-06-13 07:51:52.905641
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    import ansible.parsing.yaml.objects

    # Test keyword args are set correctly
    field_attribute = FieldAttribute(
    isa = 'test',
    private = True,
    default = 'test2',
    required = True,
    listof = 'test3',
    priority = -1,
    class_type = 'test4',
    always_post_validate = True,
    inherit = False,
    alias = 'test5',
    extend = True,
    prepend = True,
    )
    assert field_attribute.isa == "test"
    assert field_attribute.private == True
    assert field_attribute.default == "test2"
    assert field_attribute.required == True
    assert field_attribute.listof == "test3"
    assert field_attribute.priority == -1

# Generated at 2022-06-13 07:51:57.114243
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', listof='int')
    assert a.isa == 'dict'
    assert a.listof == 'int'
    assert a.default == None
    assert a.required == False

    a = Attribute(isa='dict', listof='int', default=True)
    assert a.isa == 'dict'
    assert a.listof == 'int'
    assert a.default == True
    assert a.required == False

# Generated at 2022-06-13 07:52:09.412665
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict')
    assert a.isa == 'dict'
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

    # confirm that exception is raised if user tries to provide a mutable
    # object as the default
    try:
        a = Attribute(isa='dict', default=dict())
        assert False, 'should have raised exception'
    except TypeError:
        pass



# Generated at 2022-06-13 07:52:18.693616
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.parsing.yaml.objects import AnsibleMapping
    import ansible.parsing.yaml.objects as objects
    import ansible.parsing.yaml.dumper as dumper
    import ansible.playbook.attribute as attribute

    attr_default = "attr_default_value"
    required = True
    isa = 'str'
    default = attr_default
    private = False
    listof = None
    priority = 0
    class_type = objects.AnsibleMapping
    always_post_validate = False
    inherit = True
    alias = None
    extend = False
    prepend = False
    static = False


# Generated at 2022-06-13 07:52:20.250994
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='foo', required=True, extend=True)
    assert attr.isa == 'foo'
    assert attr.required == True
    assert attr.extend == True



# Generated at 2022-06-13 07:52:21.946864
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Empty constructor
    assert FieldAttribute() is not None



# Generated at 2022-06-13 07:52:29.000441
# Unit test for constructor of class Attribute
def test_Attribute():
    class_type = (1,2,3)
    attribute = Attribute(isa='foo', private=True, default=False, required=True,
                          listof='foo', priority=0, class_type=class_type,
                          always_post_validate=True, inherit=False, alias='bar',
                          extend=True, prepend=True, static=True)

    assert attribute.isa == 'foo'
    assert attribute.private == True
    assert attribute.default == False
    assert attribute.required == True
    assert attribute.listof == 'foo'
    assert attribute.priority == 0
    assert attribute.class_type == class_type
    assert attribute.always_post_validate == True
    assert attribute.inherit == False
    assert attribute.alias == 'bar'
    assert attribute.extend == True


# Generated at 2022-06-13 07:52:33.293307
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='str', private=True, default=None, required=True, listof=None, priority=2)
    assert fa.isa == 'str'
    assert fa.private
    assert fa.default == None
    assert fa.required
    assert fa.listof == None
    assert fa.priority == 2

if __name__ == '__main__':
    test_FieldAttribute()

# Generated at 2022-06-13 07:52:38.390394
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute()
    assert field.isa == None
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
    assert field.static   == False

#Unit test for all comparison operators for class FieldAttribute

# Generated at 2022-06-13 07:52:46.001434
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


# Generated at 2022-06-13 07:52:53.983603
# Unit test for constructor of class Attribute
def test_Attribute():

    with pytest.raises(TypeError):
        Attribute(default=_CONTAINERS)

    with pytest.raises(TypeError):
        Attribute(default={})

    with pytest.raises(TypeError):
        Attribute(default=[])

    with pytest.raises(TypeError):
        Attribute(default=set())

    Attribute(default=None)

    Attribute(default=())

    Attribute(default=0)

    Attribute(default=[0])

    Attribute(default={})

    Attribute(default=set())

    Attribute(default=1.0)

    Attribute(default="")

    Attribute(default=deepcopy)

    Attribute(default=Attribute)

    Attribute(default=FieldAttribute)

    Attribute(default=FieldAttribute())


# Generated at 2022-06-13 07:53:05.644584
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    """
    Unit test for constructor of class FieldAttribute
    """
    # attribute = FieldAttribute(isa='bool', private=True, default=None,
    #                        required=True, listof=None, class_type=None,
    #                        always_post_validate=False, inherit=True, alias=None)
    # print(attribute)

    # attribute = FieldAttribute(isa='bool', private=True, default=None,
    #                            required=True, listof=None, class_type=None,
    #                            always_post_validate=False, inherit=True, alias=None)
    # print(attribute)

    # attribute = FieldAttribute(isa='str', private=False, default=None,
    #                            required=False, listof=None, class_type=None,
    #                            always_post

# Generated at 2022-06-13 07:53:16.084833
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa1 = FieldAttribute(
        isa='dict',
        private=True,
        default=dict(),
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
    )

    assert fa1.isa == 'dict'
    assert fa1.private == True
    assert fa1.default == dict()
    assert fa1.required == False
    assert fa1.listof == None
    assert fa1.priority == 0
    assert fa1.class_type == None
    assert fa1.always_post_validate == False
    assert fa1.inherit == True
    assert fa1.alias == None
    assert fa1.extend == False



# Generated at 2022-06-13 07:53:26.986749
# Unit test for constructor of class Attribute
def test_Attribute():
    # test case for isa validation
    attr = Attribute(isa='dict')
    assert type(attr) == Attribute
    assert attr.isa == 'dict'

    # test case for isa validation None type
    attr = Attribute(isa=None)
    assert type(attr) == Attribute
    assert attr.isa == None

    # test case for isa validation % type
    attr = Attribute(isa='%')
    assert type(attr) == Attribute
    assert attr.isa == '%'

    # test case for not valid class type
    try:
        attr = Attribute(isa='MyAttr')
        raise AssertionError('Test case failed')
    except:
        assert True

    # test case for isa validation boolean type
    attr = Attribute(isa='bool')


# Generated at 2022-06-13 07:53:37.574217
# Unit test for constructor of class Attribute
def test_Attribute():
    bogus = Attribute()
    assert bogus.isa is None
    assert bogus.default is None
    assert not bogus.required
    assert bogus.listof is None
    assert bogus.priority == 0

    assert bogus.class_type is None
    assert not bogus.always_post_validate
    assert bogus.inherit
    assert bogus.alias is None

    bogus = Attribute(isa='percent',
                      default=lambda: {},
                      required=True,
                      listof='ipaddr',
                      priority=25,
                      class_type=object,
                      always_post_validate=True,
                      inherit=False,
                      alias='foo')

    assert bogus.isa == 'percent'
    assert callable(bogus.default)
    assert bogus.required
    assert bogus.listof == 'ipaddr'

# Generated at 2022-06-13 07:53:47.469926
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa='test_isa', private=False, default=None,
                                     required=False, listof=None, priority=0,
                                     class_type=None, always_post_validate=False,
                                     inherit=True, alias=None, extend=False,
                                     prepend=False, static=False)

    assert field_attribute.__class__.__name__ == 'FieldAttribute'
    assert field_attribute.default == None
    assert field_attribute.alias == None


# Generated at 2022-06-13 07:53:54.378979
# Unit test for constructor of class Attribute
def test_Attribute():
    # Constructor with no parameters
    a1 = Attribute()
    assert a1.private == False
    assert a1.required == False
    assert a1.priority == 0
    assert a1.alias == None
    assert a1.inherit == True

    # Construct with parameters
    a2 = Attribute(private=True, required=True, priority=-1, alias="A2", inherit=False)
    assert a2.private == True
    assert a2.required == True
    assert a2.priority == -1
    assert a2.alias == "A2"
    assert a2.inherit == False

# Generated at 2022-06-13 07:54:05.191927
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test constructor
    a = Attribute(isa='list', class_type='list')
    assert a.isa == 'list'
    assert a.class_type == 'list'

    # Test constructor with default
    a = Attribute(isa='list', class_type='list', default=lambda: [])
    assert a.isa == 'list'
    assert a.class_type == 'list'
    assert isinstance(a.default, (copy, deepcopy))
    assert callable(a.default)

    # Test that defaults may not be mutable
    try:
        a = Attribute(isa='list', default=[])
    except TypeError as e:
        assert str(e) == 'defaults for FieldAttribute may not be mutable, please provide a callable instead'

# Generated at 2022-06-13 07:54:07.202557
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()
    assert field_attribute is not None


# Generated at 2022-06-13 07:54:08.540164
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    Attribute()
    FieldAttribute()


# Generated at 2022-06-13 07:54:12.939487
# Unit test for constructor of class Attribute
def test_Attribute():
    att = Attribute(isa='int', default='test', required=True)
    assert att.isa == 'int'
    assert att.default == 'test'
    assert att.required == True


# Generated at 2022-06-13 07:54:15.020520
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str')
    assert attr.isa == 'str', "isa should be 'str'"

# Generated at 2022-06-13 07:54:17.982679
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FieldAttribute(isinstance,None,False)
    except Exception as e:
        print(e)
        print("Attribute Error. Wrong type of Attribute.")


# Generated at 2022-06-13 07:54:18.912228
# Unit test for constructor of class Attribute
def test_Attribute():
    pass


# Generated at 2022-06-13 07:54:24.624043
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


# Generated at 2022-06-13 07:54:33.444521
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().isa is None
    assert FieldAttribute().default is None
    assert not FieldAttribute().required
    assert FieldAttribute().priority == 0
    assert FieldAttribute().isa is None
    assert not FieldAttribute().private
    assert FieldAttribute().class_type is None
    assert not FieldAttribute().always_post_validate
    assert FieldAttribute().inherit
    assert FieldAttribute().alias is None
    assert not FieldAttribute().extend
    assert not FieldAttribute().prepend
    assert not FieldAttribute().static

# Generated at 2022-06-13 07:54:36.962081
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='dict', default=dict)
    assert a.isa == 'dict'
    assert a.default == dict
    try:
        a = FieldAttribute(isa='dict', default={})
        raise Exception("didn't catch the non-callable default")
    except TypeError:
        pass



# Generated at 2022-06-13 07:54:48.745341
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    _ = FieldAttribute()
    _ = FieldAttribute(isa='thing')
    _ = FieldAttribute(alias='bob')
    _ = FieldAttribute(private=True)
    _ = FieldAttribute(default=None)
    _ = FieldAttribute(required=False)
    _ = FieldAttribute(listof=['a', 'b', 'c'])
    _ = FieldAttribute(priority=42)
    _ = FieldAttribute(class_type=type)
    _ = FieldAttribute(always_post_validate=False)
    _ = FieldAttribute(inherit=True)
    _ = FieldAttribute(extend=False)
    _ = FieldAttribute(prepend=False)



# Generated at 2022-06-13 07:54:53.632928
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=str, private=False, default=None, required=False,
                  listof=None, priority=0, class_type=None,
                  always_post_validate=False, inherit=True, alias=None, extend=False,
                  prepend=False, static=False)
    ansible_module_test(a)
    a.default = "hello"
    ansible_module_test(a)
    a.required=True
    ansible_module_test(a)


# Generated at 2022-06-13 07:54:56.772650
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    FA = FieldAttribute(isa='str', default='str', required=True, priority=1)
    FA2 = FieldAttribute(isa='str', default='str')
    assert(FA != FA2)

# Generated at 2022-06-13 07:54:59.845914
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='int')
    assert isinstance(a.isa, str)

    a = Attribute(isa=int)
    assert isinstance(a.isa, type)



# Generated at 2022-06-13 07:55:02.075331
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    class Y(object):
        x = FieldAttribute(isa='dict')

    y = Y()

    assert y.x is None

# Generated at 2022-06-13 07:55:12.141806
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute().isa is None
    assert Attribute(isa='list').isa == 'list'
    assert Attribute(listof='int').listof == 'int'
    assert Attribute(default=[1,2]).default == [1,2]
    assert Attribute(required=True).required is True
    assert Attribute(priority=3).priority == 3
    assert Attribute(class_type=(dict,)).class_type == (dict,)
    assert Attribute(always_post_validate=True).always_post_validate is True
    assert Attribute(private=True).private is True
    assert Attribute(alias='foo').alias == 'foo'
    assert Attribute(extend=True).extend is True
    assert Attribute(prepend=True).prepend is True
    assert Attribute(static=True).static is True

# Generated at 2022-06-13 07:55:19.623027
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute1 = Attribute(isa='str', alias='bob')
    assert set(attribute1.__dict__.keys()) == set(['isa', 'private', 'default', 'required', 'listof', 'priority', 'class_type', 'always_post_validate', 'inherit', 'alias', 'extend', 'prepend'])
    assert attribute1.isa == 'str'
    assert attribute1.private is False
    assert attribute1.default is None
    assert attribute1.required is False
    assert attribute1.listof is None
    assert attribute1.priority == 0
    assert attribute1.class_type is None
    assert attribute1.always_post_validate is False
    assert attribute1.inherit
    assert attribute1.alias == 'bob'
    assert attribute1.extend is False
    assert attribute

# Generated at 2022-06-13 07:55:22.719982
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='list', priority=1)
    assert field.isa == 'list'
    assert field.priority == 1


# Generated at 2022-06-13 07:55:32.278567
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()

# Generated at 2022-06-13 07:55:43.198577
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute(isa='str', private=False, default='foo', required=True, listof='str', priority=0, class_type='myclass',
              always_post_validate=False, inherit=True, alias='my_alias')
    assert x.isa == 'str'
    assert x.private is False
    assert x.default == 'foo'
    assert x.required is True
    assert x.listof == 'str'
    assert x.priority == 0
    assert x.class_type == 'myclass'
    assert x.always_post_validate is False
    assert x.inherit is True
    assert x.alias == 'my_alias'


# Generated at 2022-06-13 07:55:50.312378
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    '''
    Unit test for FieldAttribute constructor
    '''
    constr = Attribute(isa='string', private=False, default='foo', required=False, listof=None, priority=0, class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False, prepend=False, static=False)
    print(constr)

# Generated at 2022-06-13 07:55:52.303697
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='dict')
    assert attr.isa == 'dict'

# Generated at 2022-06-13 07:55:59.791985
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=True, required=True, listof='str', priority=1, class_type='str',
                  always_post_validate=True, inherit=False)
    assert a.isa == 'str'
    assert a.private == True
    assert a.required == True
    assert a.listof == 'str'
    assert a.priority == 1
    assert a.class_type == 'str'
    assert a.always_post_validate == True
    assert a.inherit == False

# Call the unit test.
test_Attribute()

# Generated at 2022-06-13 07:56:11.966061
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='string', private=False, default='default', required=False, listof='str', priority=0, class_type=None, always_post_validate=False, inherit=True)
    assert f.isa == 'string'
    assert f.private == False
    assert f.default == 'default'
    assert f.required == False
    assert f.listof == 'str'
    assert f.priority == 0
    assert f.class_type == None
    assert f.always_post_validate == False
    assert f.inherit == True

    # check if error is thrown when a mutable object is assigned to a default
    try:
        f = FieldAttribute(isa='dict', default={'this': 'is', 'a': 'dict'})
    except Exception:
        pass

# Generated at 2022-06-13 07:56:14.121687
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa=FieldAttribute()
    if fa is None:
        print("Test fail")
    else:
        print("Test pass")



# Generated at 2022-06-13 07:56:22.789037
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='str', private=True)
    assert(a.isa=='str')
    assert(a.private==True)
    assert(a.default==None)
    assert(a.required==False)
    assert(a.listof==None)
    assert(a.priority==0)
    assert(a.class_type==None)
    assert(a.always_post_validate==False)
    assert(a.inherit==True)
    assert(a.alias==None)
    assert(a.extend==False)
    assert(a.prepend==False)



# Generated at 2022-06-13 07:56:25.959443
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='list',
        listof='string',
        required=True,
        default=['test'],
    )
    assert fa.isa == 'list'
    assert fa.listof == 'string'
    assert fa.required == True
    assert fa.default == ['test']



# Generated at 2022-06-13 07:56:30.947951
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='bool')

    for i in ('isa', 'private', 'default', 'required', 'listof', 'priority', 'class_type', 'always_post_validate', 'inherit', 'alias'):
        assert hasattr(a, i)

    assert not a.private

    # default not used by non-list fields.
    b = Attribute(isa='list', default='bar')
    assert b.default == 'bar'

    # Default for list fields should be a callable returning a new container.
    c = Attribute(isa='list')
    assert callable(c.default)
    assert c.default() == []
    c = Attribute(isa='dict')
    assert callable(c.default)
    assert c.default() == {}

# Generated at 2022-06-13 07:56:50.561272
# Unit test for constructor of class Attribute
def test_Attribute():
    import os
    from ansible.errors import AnsibleAssertionError
    if os.environ.get('ANSIBLE_FORCE_COLOR') and os.environ.get('ANSIBLE_FORCE_COLOR') == "False":
        raise AnsibleAssertionError('os.environ["ANSIBLE_FORCE_COLOR"] should not be set to "False"')



# Generated at 2022-06-13 07:56:54.361581
# Unit test for constructor of class Attribute
def test_Attribute():
    fixture = dict(
        isa=None,
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
    )
    compare_obj = Attribute(**fixture)
    assert compare_obj.__dict__ == fixture

# Generated at 2022-06-13 07:57:05.038791
# Unit test for constructor of class Attribute
def test_Attribute():
    # Test the constructor of class Attribute
    def __init__(
        self,
        isa=None,
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
    ):
        assert isa is None
        assert private is False
        assert default is None
        assert required is False
        assert listof is None
        assert priority == 0
        assert class_type is None
        assert always_post_validate is False
        assert inherit is True
        assert alias is None
        assert extend is False
        assert prepend is False

    attribute = Attribute()

# Generated at 2022-06-13 07:57:15.959333
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

# Generated at 2022-06-13 07:57:27.216796
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(isa = 'str', static=True)
    assert(attribute.isa == 'str')
    assert(attribute.static == True)
    assert(attribute.default == None)
    assert(attribute.required == False)
    assert(attribute.listof == None)
    assert(attribute.priority == 0)
    assert(attribute.class_type == None)
    assert(attribute.always_post_validate == False)
    assert(attribute.inherit == True)
    assert(attribute.alias == None)
    assert(attribute.extend == False)
    assert(attribute.prepend == False)



# Generated at 2022-06-13 07:57:28.494144
# Unit test for constructor of class Attribute
def test_Attribute():
    test = Attribute()
    return test

# Generated at 2022-06-13 07:57:31.392914
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(default=dict())
    assert isinstance(f.default, dict)
    f = FieldAttribute(default=list())
    assert isinstance(f.default, list)


# Generated at 2022-06-13 07:57:37.862794
# Unit test for constructor of class Attribute
def test_Attribute():
    def f():
        pass

    def g():
        pass

    # Ensure that Attribute objects are hashable
    # (this is used in the _ATTRIBUTE_CLASSES dict)
    attr = Attribute()
    attr2 = Attribute()
    result = {attr: f, attr2: g}
    assert len(result) == 2



# Generated at 2022-06-13 07:57:44.303950
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='str',
        default=None,
        required=False,
        listof='bool',
        priority=0,
        inherit=True
    )

    assert a.isa == 'str'
    assert a.default is None
    assert not a.required
    assert a.listof == 'bool'
    assert a.priority == 0
    assert a.inherit is True


# YAML/AnsibleObjectLoader class.  Basically just a wrapper around Kyu_Loader
# which handles a couple of special cases (for backwards compatibility)


# Generated at 2022-06-13 07:57:48.196198
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='dict')
    assert fa.isa == 'dict', "Got unexpected isa '%s' expecting 'dict'" % fa.isa

    fa = FieldAttribute(required=True)
    assert fa.required == True, "Got unexpected required '%s' expecting 'True'" % fa.required



# Generated at 2022-06-13 07:58:24.261231
# Unit test for constructor of class Attribute
def test_Attribute():
    # No args
    Attribute()

    # One arg
    Attribute(isa='list')

    # Args as kwargs, should not raise exceptions
    Attribute(isa='boolean', private=True, required=True)
    Attribute(isa='string', private=True, required=False)
    Attribute(isa='list', private=False, required=False)
    Attribute(isa='dict', private=False, required=True)

    # The Attribute constructor should raise an exception if the default value
    # is not None and the isa is something which is mutable.
    for isa in ('list', 'dict', 'set'):
        try:
            Attribute(isa=isa, default={})
            assert False
        except TypeError:
            assert True

    # The default value can be None, though.
    Att

# Generated at 2022-06-13 07:58:31.001207
# Unit test for constructor of class Attribute
def test_Attribute():
    class TestFieldAttribute(object):
        a = FieldAttribute(isa='list',
                           class_type=list,
                           inherit=True,
                           always_post_validate=True,
                           alias='a')
        b = FieldAttribute(isa='list',
                           default=[],
                           inherit=False,
                           alias='b')
        c = FieldAttribute(isa='list',
                           default=[],
                           inherit=True,
                           alias='c')
        d = FieldAttribute(isa='dict',
                           default={},
                           inherit=False,
                           alias='d')
        e = FieldAttribute(isa='dict',
                           default={},
                           inherit=True,
                           alias='e')

# Generated at 2022-06-13 07:58:43.066592
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # test every argument and kwarg
    assert FieldAttribute(isa="dict",
                          private=True,
                          default="a value",
                          required=True,
                          listof="a_type",
                          priority=10,
                          class_type=Attribute,
                          always_post_validate=True,
                          inherit=False,
                          alias="another_name",
                          extend=True,
                          prepend=True,
                          static=True).isa == "dict"

# Generated at 2022-06-13 07:58:54.774013
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute.__init__(isa='dict') == Attribute('dict')
    assert Attribute.__init__(isa='str') == Attribute('str')
    assert Attribute.__init__(isa=dict) == Attribute(dict)
    assert Attribute.__init__(isa='dict', private=True) == Attribute('dict', private=True)
    assert Attribute.__init__(isa='dict', alias='something') == Attribute('dict', alias='something')
    assert Attribute.__init__(isa='dict', default=dict()) == Attribute('dict', default=dict())
    assert Attribute.__init__(isa='dict', required=True) == Attribute('dict', required=True)

# Generated at 2022-06-13 07:58:56.610372
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert not f.private, "Default value of private is incorrect"
    f = FieldAttribute(private=True)
    assert f.private, "Private was not set"

# Generated at 2022-06-13 07:59:00.969846
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='str', private=False, default='hi', required=False, 
                 listof=None, priority=0, class_type=None, always_post_validate=False,
                 inherit=True, alias=None, extend=False, prepend=False, static=False)
    assert f.isa == 'str'
    assert not f.private
    assert f.default == 'hi'
    assert not f.required
    assert not f.always_post_validate
    assert f.inherit
    assert f.alias is None

