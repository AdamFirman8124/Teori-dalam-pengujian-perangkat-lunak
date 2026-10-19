

# Generated at 2022-06-13 07:49:17.897888
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test for require and default
    def test_require_default(require, default, should_raise):
        try:
            attr = Attribute(require=require, default=default)
        except TypeError:
            if should_raise:
                return
            else:
                raise

        if should_raise:
            raise

    test_require_default(require=True, default=None, should_raise=True)
    test_require_default(require=True, default=True, should_raise=False)
    test_require_default(require=False, default=None, should_raise=False)
    test_require_default(require=False, default=True, should_raise=False)

    # Test for default is not mutable when isa is in _CONTAINERS

# Generated at 2022-06-13 07:49:24.171383
# Unit test for constructor of class Attribute
def test_Attribute():

    # This should raise an exception. Requires a callable for default.
    try:
        my_attr = Attribute(default={})
    except Exception as e:
        assert (isinstance(e,TypeError))

    my_attr = Attribute(default=lambda: {})
    assert (isinstance(my_attr.default, Attribute))

    # This should not raise an exception
    my_attr = Attribute(default=lambda: {})
    assert (isinstance(my_attr.default, Attribute))

# Generated at 2022-06-13 07:49:30.900140
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert f.class_type is None
    assert f.default is None
    assert f.extend is False
    assert f.inherit is True
    assert f.listof is None
    assert f.private is False
    assert f.priority is 0
    assert f.required is False
    assert f.alias is None
    assert f.static is False
    assert f.prepend is False
    assert f.always_post_validate is False

# Generated at 2022-06-13 07:49:36.633113
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(
        isa='str',
        default='default-value',
        private=False,
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
    assert a.isa == 'str'
    assert a.default == 'default-value'
    assert a.private == False
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a

# Generated at 2022-06-13 07:49:40.602708
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='bar',
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

    return a

# Generated at 2022-06-13 07:49:45.103278
# Unit test for constructor of class Attribute
def test_Attribute():

    attr = Attribute()
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
    assert attr.extend == False
    assert attr.prepend == False
    assert attr.static == False



# Generated at 2022-06-13 07:49:49.237131
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', prepend=True, extend=True)
    assert a.prepend == True
    assert a.extend == True

    a = Attribute(isa='dict', prepend=False, extend=True)
    assert a.prepend == False
    assert a.extend == True

    a = Attribute(isa='dict', prepend=False, extend=False)
    assert a.prepend == False
    assert a.extend == False

    a = Attribute(isa='dict', prepend=True, extend=False)
    assert a.prepend == True
    assert a.extend == False

# Generated at 2022-06-13 07:49:50.108570
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='list')

    assert f.isa == 'list'



# Generated at 2022-06-13 07:49:59.338039
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', default=42)
    assert attr.isa == 'str'
    assert attr.default == 42
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    assert attr.extend == False
    assert attr.prepend == False


# Generated at 2022-06-13 07:50:02.758235
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa="int", default=1, required=True)
    assert f.isa == "int"
    assert f.default == 1
    assert f.required == True

# Generated at 2022-06-13 07:50:08.933658
# Unit test for constructor of class Attribute
def test_Attribute():
    # No error raised if default is None
    Attribute(
        default=None,
        required=False,
        isa='dict',
    )

    # Error raised if default is not None and isa is 'dict'
    try:
        Attribute(
            default={},
            required=False,
            isa='dict',
        )
    except TypeError as e:
        pass

# Generated at 2022-06-13 07:50:15.411019
# Unit test for constructor of class Attribute
def test_Attribute():
    f = FieldAttribute(
        isa='bool',
        default=False
    )
    assert f.isa == 'bool'
    assert f.default == False
    assert f.required == False
    assert f.listof == None
    assert f.priority == 0
    assert f.class_type == None
    assert f.always_post_validate == False
    assert f.inherit == True


# Generated at 2022-06-13 07:50:16.863595
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int', default=10)


# Generated at 2022-06-13 07:50:18.808038
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert isinstance(a, FieldAttribute)
    assert isinstance(a, Attribute)



# Generated at 2022-06-13 07:50:22.082320
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='int', default=7, required=False, private=False)
    assert (attr.isa == 'int')
    assert (attr.private == False)
    assert (attr.default == 7)
    assert (attr.required == False)


# Generated at 2022-06-13 07:50:33.756307
# Unit test for constructor of class Attribute
def test_Attribute():
    print("\n Unit Testing Attribute")
    at = Attribute(isa="str")
    print("Type of class is: " + str(type(at)))
    print("Type of object is: " + str(at.isa))
    print("Value of private is: " + str(at.private))
    print("Value of default is: " + str(at.default))
    print("Value of required is: " + str(at.required))
    print("Value of listof is: " + str(at.listof))
    print("Value of priority is: " + str(at.priority))
    print("Value of class_type is: " + str(at.class_type))
    print("Value of always_post_validate is: " + str(at.always_post_validate))

# Generated at 2022-06-13 07:50:39.429608
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(required=True) != Attribute()
    assert Attribute() < Attribute(priority=1)
    assert Attribute(priority=1) > Attribute()
    assert Attribute() <= Attribute(priority=1)
    assert Attribute(priority=1) >= Attribute()
    assert Attribute() == Attribute()
    assert Attribute(priority=1) == Attribute(priority=1)


# Generated at 2022-06-13 07:50:49.471338
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='dict')
    fa.priority = 1
    FA = FieldAttribute(isa='list')
    FA.priority = 2
    assert fa < FA
    fa.priority = 3
    assert fa > FA
    assert fa == FA
    FA.priority = 3
    assert fa == FA
    assert fa <= FA
    assert fa >= FA
    assert fa != FA
    FA.priority = 2
    assert fa != FA
    assert fa >= FA
    assert fa <= FA
    assert fa > FA
    assert fa < FA


# Generated at 2022-06-13 07:51:01.800439
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute()
    assert a is not None
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

    a = FieldAttribute(isa = int)
    assert a is not None
    assert a.isa == int
    assert a.private is False
    assert a.default is None
    assert a.required is False
    assert a.listof is None
    assert a.priority == 0

# Generated at 2022-06-13 07:51:07.995812
# Unit test for constructor of class Attribute
def test_Attribute():
    attrib = Attribute(isa='dict', required=True, listof='str')
    assert attrib.isa == 'dict'
    assert attrib.required is True
    assert attrib.listof == 'str'
    assert attrib.private is False
    assert attrib.default is None
    assert attrib.priority == 0
    assert attrib.class_type is None
    assert attrib.always_post_validate is False
    assert attrib.inherit is True
    assert attrib.alias is None



# Generated at 2022-06-13 07:51:12.284865
# Unit test for constructor of class Attribute
def test_Attribute():
    required_true = Attribute(required=True)
    required_false = Attribute(required=False)
    assert(required_true.prioritiy > required_false.prioritiy)

# Generated at 2022-06-13 07:51:13.408179
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='dict')
    assert fa.isa == 'dict'



# Generated at 2022-06-13 07:51:15.329007
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict')
    assert a.isa == 'dict'



# Generated at 2022-06-13 07:51:25.818824
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='some_type',
        private=False,
        default='some_default',
        required=False,
        listof='some_listof',
        priority=0,
        class_type='some_class_type',
        always_post_validate=False,
        inherit=True,
        alias='some_alias',
        extend=False,
        prepend=False,
        static=False,
    )
    assert a.isa == 'some_type'
    assert a.private == False
    assert a.default == 'some_default'
    assert a.required == False
    assert a.listof == 'some_listof'
    assert a.priority == 0
    assert a.class_type == 'some_class_type'
    assert a.always_post_validate

# Generated at 2022-06-13 07:51:34.256618
# Unit test for constructor of class Attribute
def test_Attribute():
    # Verify constructor fails when default is specified and is mutable
    try:
        FieldAttribute(isa='dict', default={'foo': 'bar'})
        assert False, "Expected TypeError"
    except TypeError:
        pass

    # Verify constructor succeeds when default is specified and is callable
    f = FieldAttribute(isa='dict', default=lambda: {'foo': 'bar'})
    assert callable(f.default)
    assert f.default() == {'foo': 'bar'}

    # Verify constructor succeeds when default is not specified
    f = FieldAttribute(isa='dict')
    assert f.default is None

    # Verify constructor sets default based on isa
    f = FieldAttribute(isa='list')
    assert f.default == []
    f = FieldAttribute(isa='dict')
    assert f.default == {}
   

# Generated at 2022-06-13 07:51:44.333609
# Unit test for constructor of class Attribute
def test_Attribute():
    import unittest
    import sys

    class test_constructor(unittest.TestCase):

        def test_attribute_default(self):

            class test_obj():
                attr = Attribute(default='Test')

            self.assertEqual(test_obj().attr, 'Test')

        def test_attribute_default_callable(self):

            class test_obj():
                attr = Attribute(default=dict)

            self.assertEqual(test_obj().attr, {})

        def test_attribute_required(self):

            class test_obj():
                attr = Attribute(required=True)

            self.assertEqual(test_obj().attr, None)

        def test_attribute_listof(self):

            class test_obj():
                attr = Attribute(listof="foo")



# Generated at 2022-06-13 07:51:54.436363
# Unit test for constructor of class Attribute
def test_Attribute():
    # _CONTAINERS is a frozenset!
    try:
        _CONTAINERS.add('tuple')
    except TypeError:
        pass
    else:
        # Should never happen
        raise AssertionError("_CONTAINERS is not immutable")

    # .default may not be mutable if .isa is a container type
    for container in _CONTAINERS:
        try:
            Attribute(container, default=[])
        except TypeError:
            pass
        else:
            raise AssertionError("default of type {} may not be a mutable container".format(container))

    # .default may be mutable if .isa is not a container type
    for non_container in set(Attribute.TYPES) - _CONTAINERS:
        Attribute(non_container, default=[])


# Generated at 2022-06-13 07:51:56.900431
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(prepend=True, priority=1)
    assert a.prepend == True
    assert a.priority == 1


# Generated at 2022-06-13 07:51:59.989848
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='list', default=[], required=True, listof='str')
    assert isinstance(f.default, list) and len(f.default) == 0


# Generated at 2022-06-13 07:52:12.910017
# Unit test for constructor of class Attribute
def test_Attribute():
    # isa
    Attribute(isa='int')
    Attribute(isa='float')
    Attribute(isa='bool')
    Attribute(isa='complex')
    Attribute(isa='dict')
    Attribute(isa='list')
    Attribute(isa='set')
    Attribute(isa='str')
    Attribute(isa='dict', listof='str')
    Attribute(isa='dict', listof='dict')
    Attribute(isa='dict', listof='int')
    Attribute(isa='dict', listof='float')
    Attribute(isa='dict', listof='bool')
    Attribute(isa='dict', listof='complex')
    Attribute(isa='dict', listof='dict')
    Attribute(isa='dict', listof='list')

# Generated at 2022-06-13 07:52:25.782304
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa='number', private=False, default=0,
    required=False, listof=None, priority=0, class_type=None,
    always_post_validate=False, inherit=True, alias=None, extend=False,
    prepend=False, static=False)

    assert field_attribute.isa == 'number'
    assert field_attribute.private == False
    assert field_attribute.default == 0
    assert field_attribute.required == False
    assert field_attribute.priority == 0
    assert field_attribute.class_type == None
    assert field_attribute.always_post_validate == False
    assert field_attribute.inherit == True
    assert field_attribute.alias == None
    assert field_attribute.extend == False
    assert field_attribute.prepend == False


# Generated at 2022-06-13 07:52:30.669648
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    a = Attribute(isa=str, private=False, default=None, required=False, listof=None, priority=0, class_type=None)
    assert a.isa in (str, unicode)
    assert not a.private
    assert a.default is None
    assert not a.required
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None

# Generated at 2022-06-13 07:52:34.670280
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    # basic test
    attribute_object = FieldAttribute()
    assert isinstance(attribute_object, FieldAttribute)

    # test default values
    assert attribute_object.isa is None
    assert attribute_object.private is False
    assert attribute_object.default is None
    assert attribute_object.required is False
    assert attribute_object.listof is None
    assert attribute_object.priority == 0
    assert attribute_object.class_type is None
    assert attribute_object.always_post_validate is False
    assert attribute_object.inherit is True
    assert attribute_object.alias is None
    assert attribute_object.extend is False
    assert attribute_object.prepend is False
    assert attribute_object.static is False

    # test class attributes
    assert FieldAttribute(isa='list').isa == 'list'
    assert Field

# Generated at 2022-06-13 07:52:38.912112
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    >>> a = Attribute()
    >>> a.isa
    None
    >>> a.default
    None
    >>> a.private
    False
    >>> a.required
    False
    >>> a.listof
    None
    >>> a.priority
    0
    >>> a.class_type
    None
    >>> a.always_post_validate
    False
    >>> a.inherit
    True
    >>> a.alias
    None
    """


# Generated at 2022-06-13 07:52:49.786090
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(
        isa='dict',
        private=True,
        default=dict,
        required=True,
        listof=dict,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
    )
    assert a.isa == 'dict'
    assert a.private == True
    assert a.default == dict
    assert a.required == True
    assert a.listof == dict
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend

# Generated at 2022-06-13 07:52:50.395568
# Unit test for constructor of class Attribute
def test_Attribute():
    pass



# Generated at 2022-06-13 07:52:51.030341
# Unit test for constructor of class Attribute
def test_Attribute():
    pass

# Generated at 2022-06-13 07:53:02.574002
# Unit test for constructor of class Attribute
def test_Attribute():
    # Just instantiating an instance of Attribute with no keyword arguments
    # should not raise any exceptions
    attr = Attribute()

    # To make the tests more readable
    isa = 'dict'
    private = False
    default = None
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False
    inherit = True
    alias = None
    extend = False
    prepend = False
    static = False

    # Instantiate an instance with keyword arguments
    attr = Attribute(isa=isa, private=private, default=default, listof=listof, priority=priority, class_type=class_type, always_post_validate=always_post_validate, inherit=inherit, alias=alias, extend=extend, prepend=prepend, static=static)



# Generated at 2022-06-13 07:53:14.166512
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

    b = Attribute(isa='dict', private=True, default=3, required=False, listof='dict', priority=1, class_type='dict',
                   always_post_validate=True, inherit=False, alias='test')

    assert b.isa == 'dict'
    assert b.private == True
    assert b.default == 3
    assert b.required == False
    assert b.listof == 'dict'


# Generated at 2022-06-13 07:53:23.429597
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    args = dict(
        isa='test',
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

    field = FieldAttribute(**args)
    assert field.isa == "test"


# Generated at 2022-06-13 07:53:37.301834
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute(isa='int', private=False, default=None, required=False,
                         listof=None, priority=0, class_type=None,
                         always_post_validate=False, inherit=True, alias=None)
    assert obj.isa == 'int'
    assert obj.private == False
    assert obj.default is None
    assert obj.required == False
    assert obj.listof is None
    assert obj.priority == 0
    assert obj.class_type is None
    assert obj.always_post_validate == False
    assert obj.inherit == True
    assert obj.alias is None

# Generated at 2022-06-13 07:53:43.865683
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='str', private=True, default='foo', required=True,
            listof=None, priority=0, always_post_validate=False,
            inherit=False, alias='bar')

    assert attr.isa == 'str'
    assert attr.private == True
    assert attr.default == 'foo'
    assert attr.required == True
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.always_post_validate == False
    assert attr.inherit == False
    assert attr.alias == 'bar'



# Generated at 2022-06-13 07:53:53.305396
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    assert attr
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None

    attr = Attribute(default=dict())
    assert attr.default == {}

    attr = Attribute(default=dict, required=True, priority=1, class_type=dict)
    assert attr.default == {}
    assert attr.required is True
    assert attr.priority == 1
    assert attr.class_type == dict
    try:
        attr = Attribute(default=object)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 07:53:57.032046
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attribute = FieldAttribute(
        isa='list',
        private=True,
        default=None,
        required=True,
        listof='int',
        priority=1,
        class_type=int,
        always_post_validate=False,
        inherit=True,
        alias='new_name',
    )
    assert attribute.get_name() == 'new_name', "FieldAttribute is initialized correctly. check attribute.get_name()"

# Generated at 2022-06-13 07:54:01.160565
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.required == False
    assert a.inherit == True
    assert a.extend == False
    assert a.prepend == False
    assert a.isa == None
    assert a.listof == None
    assert a.static == False


# Generated at 2022-06-13 07:54:13.442321
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test default values
    assert FieldAttribute().isa is None
    assert FieldAttribute().private is False
    assert FieldAttribute().default is None
    assert FieldAttribute().required is False
    assert FieldAttribute().listof is None
    assert FieldAttribute().priority == 0
    assert FieldAttribute().class_type is None
    assert FieldAttribute().always_post_validate is False
    assert FieldAttribute().inherit is True
    assert FieldAttribute().alias is None
    assert FieldAttribute().extend is False
    assert FieldAttribute().prepend is False

    # test values set by kwargs
    assert FieldAttribute(isa='str').isa == 'str'
    assert FieldAttribute(private=True).private is True
    assert FieldAttribute(default='').default == ''
    assert FieldAttribute(required=True).required is True

# Generated at 2022-06-13 07:54:20.809381
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute().private is False
    attr = Attribute(True, required=True)
    assert attr.private is True
    assert attr.required is True
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False
    attr = Attribute(True, required=True, extend=True, prepend=True, static=True)
    assert attr.private is True
    assert attr.required is True
    assert attr.extend is True
    assert attr.prepend is True
    assert attr.static is True


# Generated at 2022-06-13 07:54:25.481436
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='dict', default={}, required=True, priority=10, static=True)
    assert attr.isa == 'dict'
    assert attr.default == {}
    assert attr.required == True
    assert attr.priority == 10
    assert attr.static == True



# Generated at 2022-06-13 07:54:26.993546
# Unit test for constructor of class Attribute
def test_Attribute():
    with pytest.raises(TypeError):
        Attribute(default=[])



# Generated at 2022-06-13 07:54:33.503457
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa=int, default=0)
    assert attr.isa == int
    assert attr.default == 0
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.alias == None
    attr = Attribute(isa=int, default={})
    assert attr.default == {}

# Generated at 2022-06-13 07:54:52.916694
# Unit test for constructor of class Attribute
def test_Attribute():
    field1 = FieldAttribute(isa='foo', default='bar')
    field2 = FieldAttribute(isa='foo', default='baz')
    field3 = FieldAttribute(isa='foo', default='bax')
    field4 = FieldAttribute(isa='foo', default='bar')

    assert field1 != field2
    assert field1 != field3
    assert field1 != field4
    assert field2 != field3
    assert field2 != field4
    assert field3 != field4

    assert field1 == field4

    assert field1 != field3
    assert field3 != field1
    assert not field1 == field3
    assert not field3 == field1



# Generated at 2022-06-13 07:55:00.560478
# Unit test for constructor of class Attribute
def test_Attribute():

    # test isa
    try:
        Attribute(isa='yo')
        assert (Attriute(isa=3))
        assert (Attribute(isa=[]))
        assert (Attribute(isa=5.5))
        assert (Attribute(isa=None))
        assert (Attribute(isa=False))
    except TypeError:
        pass
    except Exception:
        raise AttributeError('Test for isa failed!')

    # test private
    try:
        Attribute(private='yo')
        assert (Attribute(private=3))
        assert (Attribute(private=[]))
        assert (Attribute(private=5.5))
        assert (Attribute(private=None))
        assert (Attribute(private=False))
    except TypeError:
        pass
    except Exception:
        raise AttributeError('Test for private failed!')

   

# Generated at 2022-06-13 07:55:10.706154
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        isa='list',
        private=True,
        default=[],
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
    assert attr.isa == 'list'
    assert attr.private == True
    assert attr.default == []
    assert attr.required == False
    assert attr.listof == 'dict'
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate == False
    assert attr.inherit == True

# Generated at 2022-06-13 07:55:18.729607
# Unit test for constructor of class Attribute
def test_Attribute():
    import sys
    if sys.version_info < (2, 7):
        return

    # isa: The type of the attribute.  Allowable values are a string
    # representation of any yaml basic datatype, python class, or percent.
    # (Enforced at post-validation time).
    with pytest.raises(TypeError):
        Attribute(isa='integer')
    with pytest.raises(TypeError):
        Attribute(isa='float')
    with pytest.raises(TypeError):
        Attribute(isa='list')
    with pytest.raises(TypeError):
        Attribute(isa='dict')
    with pytest.raises(TypeError):
        Attribute(isa='set')
    with pytest.raises(TypeError):
        Attribute(isa='boolean')


# Generated at 2022-06-13 07:55:25.071227
# Unit test for constructor of class Attribute
def test_Attribute():
    """
    test code for class Attribute
    """
    attr = Attribute(isa='dict')
    assert attr.isa == 'dict'
    attr.default = {}
    try:
        attr.default = [1, 2, 3]
    except TypeError:
        pass
    else:
        raise AssertionError('attribute.default expects a callable for mutable defaults')

# Generated at 2022-06-13 07:55:38.922759
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='string', private=True, default=None, required=True)
    assert attr.isa == 'string'
    assert attr.private == True
    assert attr.default == None
    assert attr.required == True
    attr = Attribute(isa='string', private=True, default='somevalue', required=True)
    assert attr.isa == 'string'
    assert attr.private == True
    assert attr.default == 'somevalue'
    assert attr.required == True
    attr = Attribute(isa='string', private=True, required=True)
    assert attr.isa == 'string'
    assert attr.private == True
    assert attr.default == None
    assert attr.required == True



# Generated at 2022-06-13 07:55:53.809535
# Unit test for constructor of class Attribute
def test_Attribute():
    import unittest

    # scenario 1: isa, default and listof takes valid values
    class ScenarioA(unittest.TestCase):
        def setUp(self):
            self.isa = [int, str, 'dict', 'list', 'bool']
            self.default = ['string', 'default', 100, True]
            self.listof = [str, 'list', 'tuple', 'dict', 'int']
            self.result = []
            for i in self.isa:
                for d in self.default:
                    for l in self.listof:
                        try:
                            attribute = Attribute(isa=i, default=d, listof=l)
                            self.result.append(True)
                        except:
                            self.result.append(False)


# Generated at 2022-06-13 07:56:03.509887
# Unit test for constructor of class Attribute
def test_Attribute():

    a = Attribute(isa='string')
    assert a.isa == 'string'
    assert a.private == False
    assert a.default is None
    assert a.required == False
    assert a.listof is None
    assert a.priority == 0
    assert a.class_type is None
    assert a.always_post_validate == False
    assert a.inherit == True

    # test setting of values
    a = Attribute(isa='string',
                  private = False,
                  default = 'test',
                  required = True,
                  listof = 'dict',
                  priority = 1,
                  class_type = 'TestClass',
                  always_post_validate = True,
                  inherit = False,
                  extend = True)
    assert a.isa == 'string'
    assert a.private == False

# Generated at 2022-06-13 07:56:14.754442
# Unit test for constructor of class Attribute
def test_Attribute():

    # Create instance of class Attribute with argument isa
    attribute_isa_obj = Attribute(isa='list')
    assert attribute_isa_obj.isa == 'list'
    assert attribute_isa_obj.private == False
    assert attribute_isa_obj.default == None
    assert attribute_isa_obj.required == False
    assert attribute_isa_obj.listof == None
    assert attribute_isa_obj.priority == 0
    assert attribute_isa_obj.class_type == None
    assert attribute_isa_obj.always_post_validate == False
    assert attribute_isa_obj.inherit == True
    assert attribute_isa_obj.alias == None
    assert attribute_isa_obj.extend == False
    assert attribute_isa_obj.prepend == False
    assert attribute_isa_obj.static == False

   

# Generated at 2022-06-13 07:56:19.198634
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    sample_obj = FieldAttribute(isa='str', default='test_str')

    assert sample_obj.isa == 'str'
    assert sample_obj.private == False
    assert sample_obj.default == 'test_str'
    assert sample_obj.listof == None


# Generated at 2022-06-13 07:56:53.375305
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.playbook.base import AnsibleObject
    from ansible.playbook.attribute import FieldAttribute

    class TestTask(AnsibleObject):
        _common_field_names = frozenset((
            'name',
            'delegate_to',
            'notify',
            'local_action'))

        name = FieldAttribute(isa='string', required=True, priority=50)
        delegate_to = FieldAttribute(isa='string', default=None, inherit=True, priority=100)
        notify = FieldAttribute(isa='list', default=[], priority=300)
        local_action = FieldAttribute(isa='string', default=None, priority=10)

    # Basic constructor tests from the AnsibleObject base class
    t = TestTask()
    assert t.name is None
    assert t.delegate_to is None

# Generated at 2022-06-13 07:57:02.623599
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(isa='int', private=True, default=5,
                           required=True, listof='string', priority=0,
                           class_type='class',
                           always_post_validate=False,
                           alias='int_a', extend=False, prepend=False, static=False)

    assert field.isa == 'int'
    assert field.private == True
    assert field.default == 5
    assert field.required == True
    assert field.listof == 'string'
    assert field.priority == 0
    assert field.class_type == 'class'
    assert field.always_post_validate == False
    assert field.alias == 'int_a'
    assert field.extend == False
    assert field.prepend == False
    assert field.static == False

# Generated at 2022-06-13 07:57:05.496888
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    obj = FieldAttribute()
    assert "FieldAttribute" in str(obj)


# Generated at 2022-06-13 07:57:07.112238
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field = FieldAttribute(required=True)
    field.validate()



# Generated at 2022-06-13 07:57:10.941443
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert a.listof == None
    assert a.default == None
    assert a.required == False
    assert a.priority == 0
    assert a.class_type == None


# Generated at 2022-06-13 07:57:19.084670
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    isa = 'list'
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

    fa = FieldAttribute(isa, private, default, required, listof, priority, class_type,
                        always_post_validate, inherit, alias, extend, prepend, static)
    assert fa.isa == isa
    assert fa.private == private
    assert fa.default == default
    assert fa.required == required
    assert fa.listof == listof
    assert fa.priority == priority
    assert fa.class_type == class_type
    assert fa.always_post_validate == always_post_

# Generated at 2022-06-13 07:57:32.066725
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import pytest
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    f = FieldAttribute(isa="string", default="hello world")
    assert f.isa == "string"
    assert f.default == "hello world"

    f = FieldAttribute(isa=("string", "int"), default=("hello world", 10))
    assert f.isa == ("string", "int")
    assert f.default == ("hello world", 10)

    f = FieldAttribute(isa=("string", "int"), default=("hello world", 10))
    assert f.isa == ("string", "int")
    assert f.default == ("hello world", 10)

    f = FieldAttribute(isa=("string", "int"), default=("hello world", 10))
    assert f

# Generated at 2022-06-13 07:57:43.049597
# Unit test for constructor of class Attribute
def test_Attribute():

    # Standard creation
    attr = Attribute(isa='name')
    assert isinstance(attr, Attribute)

    # With additional arguments
    attr = Attribute(isa='name', class_type=tuple, always_post_validate=True)
    assert isinstance(attr, Attribute)

    # With default value specified
    attr = Attribute(isa='name', default='foo')
    assert isinstance(attr, Attribute)

    # default value may be callable, mutable types are not allowed
    attr = Attribute(isa='name', default=lambda: ['foo'])
    assert isinstance(attr, Attribute)

    # mutable types are not allowed

# Generated at 2022-06-13 07:57:51.785389
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute()
    attr = Attribute(5)
    assert attr.isa == 5

    attr = Attribute(isa='foo')
    assert attr.isa == 'foo'

    attr = Attribute(default='bar')
    assert attr.default == 'bar'

    attr = Attribute(required=True)
    assert attr.required is True

    attr = Attribute(listof='baz')
    assert attr.listof == 'baz'

    attr = Attribute(priority=1)
    assert attr.priority == 1

    attr = Attribute(private=True)
    assert attr.private is True

    attr = Attribute(always_post_validate=True)
    assert attr.always_post_validate is True

    attr = Att

# Generated at 2022-06-13 07:58:02.753034
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='list', default=[])
    try:
        b = FieldAttribute(isa='list', default=[], extend=True)
        raise Exception('fail')
    except TypeError:
        pass
    try:
        b = FieldAttribute(isa='list', default=[], prepend=True)
        raise Exception('fail')
    except TypeError:
        pass
    try:
        b = FieldAttribute(isa='list', default=[], static=True)
        raise Exception('fail')
    except TypeError:
        pass
    try:
        b = FieldAttribute(isa='list', default=[], inherit=True, extend=True)
        raise Exception('fail')
    except TypeError:
        pass

# Generated at 2022-06-13 07:59:04.237079
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute('string',
                          private=False,
                          default=None,
                          required=False,
                          listof='string',
                          priority=0,
                          class_type='object',
                          always_post_validate=False,
                          inherit=True,
                          alias=None,
                          extend=False,
                          prepend=False,
                          static=False)

# For unit test
if __name__ == '__main__':
    test_Attribute()