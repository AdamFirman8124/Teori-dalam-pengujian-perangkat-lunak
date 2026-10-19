

# Generated at 2022-06-13 07:49:15.457852
# Unit test for constructor of class Attribute
def test_Attribute():
    a1 = Attribute(
        isa = "string",
        private = False,
        default = "dehaan",
        required = False,
        listof = None,
        priority = 0,
        class_type = None,
        always_post_validate = False,
        inherit = True,
        alias = "foo",
    )

    # test constructor defaults
    a2 = Attribute()

    assert a1.isa == "string"
    assert a1.private == False
    assert a1.default == "dehaan"
    assert a1.required == False
    assert a1.listof == None
    assert a1.priority == 0
    assert a1.class_type == None
    assert a1.always_post_validate == False
    assert a1.inherit == True
    assert a

# Generated at 2022-06-13 07:49:16.242869
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass

# Generated at 2022-06-13 07:49:20.358212
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='list', default=lambda: ['test', 'default'], inherit=False)
    assert attr.inherit is False
    assert attr.default() == ['test', 'default']



# Generated at 2022-06-13 07:49:25.388362
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='option', required=True, default='default value',
                     always_post_validate=True, inherit=False)

    assert attr.isa == 'option'
    assert attr.required
    assert attr.default == 'default value'
    assert attr.always_post_validate
    assert not attr.inherit


# Generated at 2022-06-13 07:49:26.863553
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='foo', default='bar', required=True)
    a.default



# Generated at 2022-06-13 07:49:31.360027
# Unit test for constructor of class Attribute
def test_Attribute():
    with Attribute(isa='str', required=False, default='foo') as a:
        assert a.isa == 'str'
        assert a.private == False
        assert a.required == False
        assert a.inherit == True
        assert a.default == 'foo'

# Generated at 2022-06-13 07:49:39.413668
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import unittest
    from datetime import datetime
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    class Test(AnsibleBaseYAMLObject):
        _fields = dict(
            a=FieldAttribute(isa='float', listof='datetime'),
            b=FieldAttribute(isa='datetime', listof='float'),
            c=FieldAttribute(isa='datetime')
        )

    test_dict = dict(
        a=[datetime(1970, 1, 1), datetime(1970, 1, 1)],
        b=[1.0, 2.0],
        c=datetime(1970, 1, 1)
    )

    t = Test.from_yaml(test_dict)


# Generated at 2022-06-13 07:49:47.099355
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="Integer", private=False, default=None, required=False, listof=None, priority=0, always_post_validate=True, inherit=True, alias=None)
    assert a.isa == "Integer"
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.listof == None
    assert a.priority == 0
    assert a.always_post_validate == True
    assert a.inherit == True
    assert a.alias == None


# Generated at 2022-06-13 07:49:55.436207
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_a = FieldAttribute()
    assert field_a.isa is None
    assert field_a.private is False
    assert field_a.default is None
    assert field_a.required is False
    assert field_a.listof is None
    assert field_a.priority is 0
    assert field_a.class_type is None
    assert field_a.always_post_validate is False
    assert field_a.inherit is True
    assert field_a.alias is None
    assert field_a.extend is False
    assert field_a.prepend is False
    assert field_a.static is False



# Generated at 2022-06-13 07:49:57.326839
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(default='foo')
    assert attr

# Generated at 2022-06-13 07:50:00.386038
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass

FieldAttribute.__test__ = False



# Generated at 2022-06-13 07:50:06.538980
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f1 = FieldAttribute()
    f2 = FieldAttribute(isa="test", private=True, default="test", required=True, listof="test", priority=1, class_type="test", always_post_validate=True, inherit=False, alias="test", extend=False, prepend=True, static=True)
    assert f1 != f2


# Generated at 2022-06-13 07:50:16.816126
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from collections import namedtuple
    from ansible.playbook.task import Task

    # Two tasks with identical attributes (and no default) should be equal.
    task1 = Task()
    task2 = Task()
    assert task1 == task2

    # Change the value of the `name` attribute and the tasks should not be equal.
    task1.name = "test"
    assert task1 != task2

    # Make `task2` a clone of `task1` and they should be equal again.
    task2 = copy(task1)
    assert task1 == task2

    # Make `task2` a deep copy of `task1` and they should still be equal.
    task2 = deepcopy(task1)
    assert task1 == task2

# Generated at 2022-06-13 07:50:24.288338
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    my_kwarg = 'kwarg'
    _test_kwarg = FieldAttribute(my_kwarg)
    assert _test_kwarg.__dict__['isa'] == my_kwarg
    assert _test_kwarg.__dict__['private'] is False
    assert _test_kwarg.__dict__['default'] is None
    assert _test_kwarg.__dict__['required'] is False
    assert _test_kwarg.__dict__['listof'] is None
    assert _test_kwarg.__dict__['priority'] == 0
    assert _test_kwarg.__dict__['class_type'] is None
    assert _test_kwarg.__dict__['always_post_validate'] is False
    assert _test_kwarg.__dict__['inherit'] is True
    assert _test_kw

# Generated at 2022-06-13 07:50:31.498198
# Unit test for constructor of class Attribute
def test_Attribute():
    status = 0

    obj = Attribute()
    if obj.required == True:
        print('Attribute constructor test FAILED')
        status += 1

    obj = Attribute(required=True)
    if obj.required == False:
        print('Attribute constructor test FAILED')
        status += 1

    if status > 0:
        exit(1)


if __name__ == '__main__':
    test_Attribute()

# Generated at 2022-06-13 07:50:35.468110
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    import unittest
    from collections import Mapping
    class TestFieldAttribute(unittest.TestCase):
        def test_all_args(self):
            field = FieldAttribute(
                isa='int',
                private=True,
                default=1,
                required=True,
                listof='int',
                priority=0,
                always_post_validate=False,
                inherit=True,
                alias='a_field_name',
                extend=False,
                prepend=False,
                static=False
            )

        def test_no_args(self):
            field = FieldAttribute()

        def test_default_must_be_immutable(self):
            self.assertRaises(TypeError, FieldAttribute, default={})
            self.assertRaises(TypeError, FieldAttribute, default=[])



# Generated at 2022-06-13 07:50:44.217564
# Unit test for constructor of class Attribute
def test_Attribute():
    test_data = dict(
        isa = ['bool', 'string', 'int'],
        private = True,
        default = 'hello',
        required = False,
        listof = ['bool', 'string', 'int'],
        priority = 1,
        class_type = "",
        always_post_validate = True,
        inherit = False,
        alias = '',
        extend = True,
        prepend = False,
        static = False,
    )
    attr = Attribute(**test_data)
    for k, v in test_data.items():
        assert getattr(attr, k) == v
    try:
        attr = Attribute(default=[1, 2, 3])
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 07:50:57.113146
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='string')
    assert attr.default is None, "default should be None"
    assert attr.isa == 'string', "isa should be 'string'"
    assert attr.private is False, "private should be False"
    assert attr.required is False, "required should be False"
    assert attr.listof is None, "listof should be None"
    assert attr.priority == 0, "priority should be 0"
    assert attr.class_type is None, "class_type should be None"
    assert attr.always_post_validate is False, "always_post_validate should be False"
    assert attr.inherit is True, "inherit should be True"
    assert attr.alias is None, "alias should be None"

    attr = Att

# Generated at 2022-06-13 07:51:07.128108
# Unit test for constructor of class Attribute
def test_Attribute():
    assert Attribute(isa='string').isa == 'string'
    assert Attribute(isa='list').isa == 'list'
    assert Attribute(isa='boolean').isa == 'boolean'
    assert Attribute(isa='float').isa == 'float'
    assert Attribute(isa='int').isa == 'int'
    assert Attribute(isa='dict').isa == 'dict'
    assert Attribute(isa='foo').isa == 'foo'
    assert Attribute(isa='set').isa == 'set'
    #assert Attribute(isa='class').isa == 'class'
    assert Attribute(isa='dict', default=dict).isa == 'dict'
    assert Attribute(isa='dict', static=True).isa == 'dict'

    # Test for failure with mutable default

# Generated at 2022-06-13 07:51:11.505665
# Unit test for constructor of class Attribute
def test_Attribute():
    class _AttributeTest(object):
        _argspec = dict(isa=Attribute(isa='dict', listof=Attribute(isa='int')))

    attr = _AttributeTest()

    assert attr._argspec.get('isa').isa == 'dict'
    assert attr._argspec.get('isa').listof.isa == 'int'

# Generated at 2022-06-13 07:51:24.370393
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        isa='string',
        private=False,
        default="",
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
    attr1 = Attribute(
        isa='string',
        private=True,
        default="",
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
    att

# Generated at 2022-06-13 07:51:33.290682
# Unit test for constructor of class Attribute
def test_Attribute():
    default = 'default'
    required = False
    listof = 'listof'
    priority = 0
    class_type = 'class_type'
    always_post_validate = False
    inherit = True
    alias = 'alias'
    extend = False
    prepend = False
    static=False
    attr = Attribute(is_a=1,
                     private=2,
                     default=default,
                     required=required,
                     listof=listof,
                     priority=priority,
                     class_type=class_type,
                     always_post_validate=always_post_validate,
                     inherit=inherit,
                     alias=alias,
                     extend=extend,
                     prepend=prepend,
                     static=static)
    assert attr.priority == priority
    assert attr.class_type

# Generated at 2022-06-13 07:51:41.111529
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='test')
    assert a.isa == 'test'
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

# Generated at 2022-06-13 07:51:46.269572
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(isa='boolean')
    assert f.isa == 'boolean'
    assert f.private == False
    assert f.default == None
    assert f.listof == None
    assert f.priority == 0
    assert f.class_type == None

# Generated at 2022-06-13 07:51:52.829237
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        always_post_validate=True,
        inherit=False,
    )
    assert attr.private == False
    assert attr.default == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == True
    assert attr.inherit == False
    assert attr.alias == None



# Generated at 2022-06-13 07:52:05.242341
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.utils.vars import combine_vars

    field = FieldAttribute(
        isa='dict',
        private=True,
        default={},
        required=True,
        listof='str',
        priority=1,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )

    assert field.isa == 'dict'
    assert field.private == True
    assert field.default == {}
    assert field.required == True
    assert field.listof == 'str'
    assert field.priority == 1
    assert field.class_type == None
    assert field.always_post_validate == False
    assert field.inherit == True
   

# Generated at 2022-06-13 07:52:13.686757
# Unit test for constructor of class Attribute
def test_Attribute():
    # pylint: disable=attribute-defined-outside-init
    # this is on purpose, to test that the constructor
    # is working correctly
    class TestClass:
        def __init__(self):
            self.foo = FieldAttribute(isa='dict', listof='string', alias='bar')

    tc = TestClass()
    assert tc.foo.isa == 'dict'
    assert tc.foo.listof == 'string'
    assert tc.foo.alias == 'bar'
    # pylint: enable=attribute-defined-outside-init



# Generated at 2022-06-13 07:52:24.021153
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

    assert Attribute(isa='str').isa == 'str'
    assert Attribute(private=True).private is True
    assert Attribute(default=123).default == 123
    assert Attribute(required=True).required is True
    assert Attribute(listof=123).listof == 123
   

# Generated at 2022-06-13 07:52:31.820737
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from ansible.playbook.attribute import FieldAttribute
    a = FieldAttribute(
        isa='list',
        private=False,
        default=None,
        required=False,
        listof='set',
        priority=0,
        class_type='class',
        always_post_validate=True,
        inherit=True,
        alias='alias'
    )
    assert a.default is None
    assert a.required is False
    assert a.listof == 'set'
    assert a.priority == 0
    assert a.class_type == 'class'
    assert a.always_post_validate is True
    assert a.inherit is True
    assert a.alias == 'alias'



# Generated at 2022-06-13 07:52:38.641576
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
        isa='dict',
        private=True,
        default=dict,
        required=False,
        listof='dict',
        priority=1,
        class_type=dict,
        always_post_validate=True,
        inherit=False,
        alias='dict_alias',
        extend=True,
        prepend=True,
        static=False,
    )

    assert f.isa == 'dict'
    assert f.private == True
    assert f.default == dict
    assert f.required == False
    assert f.listof == 'dict'
    assert f.priority == 1
    assert f.class_type == dict
    assert f.always_post_validate == True
    assert f.inherit == False
    assert f.alias == 'dict_alias'
   

# Generated at 2022-06-13 07:52:44.889380
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()
    assert(a)

# Generated at 2022-06-13 07:52:53.329445
# Unit test for constructor of class Attribute
def test_Attribute():
    isa = 'dict'
    private = False
    default = None
    required = False
    listof = None
    priority = 0
    class_type = None
    always_post_validate = False

    a = Attribute(isa=isa, private=private, default=default, required=required,
                  listof=listof, priority=priority, class_type=class_type,
                  always_post_validate=always_post_validate)

    assert a.isa is isa
    assert a.private == private
    assert a.default is default
    assert a.required == required
    assert a.listof is listof
    assert a.priority == priority
    assert a.class_type is class_type
    assert a.always_post_validate == always_post_validate

    a.isa = None
   

# Generated at 2022-06-13 07:52:54.056122
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute()

# Generated at 2022-06-13 07:52:57.852070
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='list', extends=False, prepend=False, static=False, listof='str', inherit=True, alias=None)
    b = Attribute()
    assert a==b
    assert a >= b
    assert a <= b

# Generated at 2022-06-13 07:53:00.422405
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa = 'complex'
    )
    assert fa.isa == 'complex'
test_FieldAttribute.unittest = True


# Generated at 2022-06-13 07:53:02.467984
# Unit test for constructor of class Attribute
def test_Attribute():
    def test():
        ansible_module_test('test_Attribute')
    test()


# Generated at 2022-06-13 07:53:07.397069
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    isa = "dict"
    alias = "foo"
    class_type = FieldAttribute

    field_attribute = FieldAttribute(isa, alias, class_type)
    assert field_attribute.isa == isa
    assert field_attribute.alias == alias
    assert field_attribute.class_type == class_type


# Generated at 2022-06-13 07:53:09.231360
# Unit test for constructor of class Attribute
def test_Attribute():
    attribute = Attribute()
    assert attribute


# Generated at 2022-06-13 07:53:17.868967
# Unit test for constructor of class Attribute
def test_Attribute():
    # Basic tests
    a = Attribute()
    assert isinstance(a, Attribute)
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

    # Test constructor with all args set to non-default value

# Generated at 2022-06-13 07:53:21.585615
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute(isa='list')

    # defaults for FieldAttribute may not be mutable
    try:
        FieldAttribute(isa='list', default={})
        assert False
    except TypeError:
        assert True