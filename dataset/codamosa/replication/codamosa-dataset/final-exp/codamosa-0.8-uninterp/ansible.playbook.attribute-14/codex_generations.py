

# Generated at 2022-06-13 07:49:04.775488
# Unit test for constructor of class Attribute
def test_Attribute():
    # Declaration/definition of a class attribute
    attribute = Attribute(isa='list')

# Generated at 2022-06-13 07:49:18.480893
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # test constructor
    attr = FieldAttribute()
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

    # test defaults
    attr = FieldAttribute(isa='list', listof='int')
    assert attr.isa == 'list'
    assert attr.listof == 'int'

    # test callable default

# Generated at 2022-06-13 07:49:20.974099
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(isa='class', default='value')
    assert attr.isa == 'class'
    assert attr.default == 'value'



# Generated at 2022-06-13 07:49:24.256856
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        a = Attribute(isa='dict', default={})
        assert False, "Attribute constructor failed to raise exception"
    except TypeError:
        pass
    a = Attribute(isa='dict', default=lambda: {})

# Generated at 2022-06-13 07:49:31.033870
# Unit test for constructor of class Attribute
def test_Attribute():
    aa = Attribute()
    assert aa.private is False
    assert aa.default is None
    assert aa.required is False
    assert aa.listof is None
    assert aa.priority == 0
    assert aa.class_type is None
    assert aa.always_post_validate is False
    assert aa.inherit is True
    assert aa.alias is None

    # test default values and copy
    aa = Attribute(default='hello')
    assert aa.private is False
    assert aa.default == 'hello'
    assert aa.required is False
    assert aa.listof is None
    assert aa.priority == 0
    assert aa.class_type is None
    assert aa.always_post_validate is False
    assert aa.inher

# Generated at 2022-06-13 07:49:39.130584
# Unit test for constructor of class Attribute
def test_Attribute():
    from collections import Counter
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # initialize an Attribute with a string value
    attr = Attribute(isa='string', default='my attr')
    assert attr.isa == 'string', "Error: test_Attribute():  isa incorrect"
    assert attr.default == 'my attr', "Error: test_Attribute():  default incorrect"
    assert attr.required is False, "Error: test_Attribute():  required incorrect"
    assert attr.priority == 0, "Error:  test_Attribute():  priority incorrect"

    # initialize an Attribute with a listof value
    attr = Attribute(isa='listof', listof='string', default=[])
    assert attr.isa == 'listof', "Error: test_Attribute():  isa incorrect"

# Generated at 2022-06-13 07:49:48.361632
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='list', private=True, default='whatever',
                       required=False, listof=None, priority=5, class_type=None,
                       inherit=True, alias=None, extend=False, prepend=False)
    assert a.isa == 'list'
    assert a.private == True
    assert a.default == 'whatever'
    assert a.required == False
    assert a.listof == None
    assert a.priority == 5
    assert a.class_type == None
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False
    return True  # tested



# Generated at 2022-06-13 07:49:57.087210
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    a = FieldAttribute(
        isa         = 'str',
        default     = 'default',
        required    = True,
        listof      = 'list',
        priority    = 1000,
        class_type  = 'class',
        inherit     = False,
        alias       = 'alias',
        extend      = True
    )

    assert a.isa == 'str'
    assert a.default == 'default'
    assert a.required == True
    assert a.listof == 'list'
    assert a.priority == 1000
    assert a.class_type == 'class'
    assert a.inherit == False
    assert a.alias == 'alias'
    assert a.extend == True


# Generated at 2022-06-13 07:49:59.908428
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attr = FieldAttribute(alias='test_field_attr')
    assert field_attr.alias == 'test_field_attr'

# Generated at 2022-06-13 07:50:05.399862
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='str', private=False, default=None, required=True, listof=None, priority=0,
                  class_type=None, always_post_validate=False, inherit=True, alias=None, extend=False)
    assert a.isa == 'str'



# Generated at 2022-06-13 07:50:07.485373
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass



# Generated at 2022-06-13 07:50:18.486665
# Unit test for constructor of class Attribute
def test_Attribute():
    import six

    # Basic test, passing only isa
    test_attr1 = Attribute('dict')
    # Test that isa is set
    assert test_attr1.isa == 'dict'
    # Private should have default (False)
    assert test_attr1.private == False
    # Default should have default (None)
    assert test_attr1.default is None
    # Required should have default (False)
    assert test_attr1.required == False
    # Listof should have default (None)
    assert test_attr1.listof is None
    # Priority should have default (0)
    assert test_attr1.priority == 0

    # Test that we get an error if the default is mutable
    try:
        test_fail_attr1 = Attribute('dict', default={})
    except TypeError:
        has

# Generated at 2022-06-13 07:50:25.326547
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():

    f = FieldAttribute(isa='list')
    assert f.isa == 'list', f.isa

    f = FieldAttribute(isa='list', private=True)
    assert f.private is True, f.private

    f = FieldAttribute(isa='list', private=1)
    assert f.private is True, f.private

    f = FieldAttribute(isa='list', default=['default'])
    assert f.default == ['default'], f.default

    f = FieldAttribute(isa='list', default=[])
    assert f.default == [], f.default

    f = FieldAttribute(isa='list', default=[1, 2, 3])
    assert f.default == [1, 2, 3], f.default

    f = FieldAttribute(isa='list', default=['default'])
    assert f.default == ['default'], f

# Generated at 2022-06-13 07:50:25.957676
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute()


# Generated at 2022-06-13 07:50:32.374014
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
    assert field.static == False


# Generated at 2022-06-13 07:50:41.389271
# Unit test for constructor of class Attribute
def test_Attribute():
    #Test the constructor
    default = object()
    isa = object()
    class_type = object()
    attribute = Attribute(isa=isa, class_type=class_type, default=default)
    assert attribute.isa is isa
    assert attribute.private == False
    assert attribute.default is default
    assert attribute.required == False
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is class_type
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias is None
    assert attribute.extend == False
    assert attribute.prepend == False
    assert attribute.static == False



# Generated at 2022-06-13 07:50:47.458201
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    global test_value
    test_value = None

    a = FieldAttribute(isa='dict', default='test', private=True)

    if (a.isa == 'dict') and (a.default == 'test') and a.private:
        test_value = True
    else:
        test_value = False

    if test_value is not True:
        raise AssertionError()

# Generated at 2022-06-13 07:50:50.158520
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='int', required=True)
    assert a.isa == 'int'
    assert a.required == True


# Generated at 2022-06-13 07:51:01.897801
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(alias='test_a')
    b = Attribute(alias='test_b')

    assert a == b
    assert not a != b
    assert not a < b
    assert not a > b
    assert a <= b
    assert a >= b

    assert b == a
    assert not b != a
    assert not b < a
    assert not b > a
    assert b <= a
    assert b >= a

    c = Attribute(alias='test_c', priority=1)
    assert c > a
    assert c >= a
    assert c != a
    assert c != b
    assert a != c
    assert b != c

    assert a < c
    assert a <= c

    assert b < c
    assert b <= c



# Generated at 2022-06-13 07:51:10.473257
# Unit test for constructor of class Attribute
def test_Attribute():
    inst = Attribute(isa=int)
    assert inst.isa == int
    assert inst.private == False
    assert inst.default == None
    assert inst.required == False
    assert inst.listof == None
    assert inst.priority == 0
    assert inst.class_type == None
    assert inst.always_post_validate == False
    assert inst.inherit == True

    inst = Attribute(isa=int, private=True, default='a string', required=True, listof=str, priority=1, class_type=str, 
                     always_post_validate=True, inherit=False)
    assert inst.isa == int
    assert inst.private == True
    assert inst.default == 'a string'
    assert inst.required == True
    assert inst.listof == str
    assert inst.priority == 1

# Generated at 2022-06-13 07:51:15.672722
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert(isinstance(attr, Attribute))
    assert(isinstance(attr, FieldAttribute))

# Generated at 2022-06-13 07:51:17.051682
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()


# Generated at 2022-06-13 07:51:22.743044
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    expected_dict = {
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

    attribute = FieldAttribute()

    for key in expected_dict:
        assert attri

# Generated at 2022-06-13 07:51:24.601220
# Unit test for constructor of class Attribute
def test_Attribute():
    # test if the constructor works
    # TODO: add more tests
    a = Attribute()

# Generated at 2022-06-13 07:51:33.461137
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    doc = FieldAttribute(
        isa='boolean',
        private=False,
        default=True,
        required=True,
        listof=None,
        priority=0,
        class_type=None,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
    )
    assert doc.isa == "boolean"
    assert doc.private is False
    assert doc.default is True
    assert doc.required is True
    assert doc.listof is None
    assert doc.priority == 0
    assert doc.class_type is None
    assert doc.always_post_validate is False
    assert doc.inherit is True
    assert doc.alias is None
    # Make sure error is raised when mutable container is provided

# Generated at 2022-06-13 07:51:39.636670
# Unit test for constructor of class Attribute
def test_Attribute():

    preferred_attr = Attribute(isa='class', priority=50)
    another_attr = Attribute(isa='class', priority=100)

    assert preferred_attr != another_attr
    assert preferred_attr < another_attr
    assert not preferred_attr > another_attr
    assert preferred_attr >= another_attr
    assert preferred_attr <= another_attr



# Generated at 2022-06-13 07:51:50.812090
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(isa='int',
                        private=True,
                        required=True,
                        inherit=False,
                        default=8,
                        priority=4,
                        extend=True,
                        prepend=True,
                        static=True,
                        alias='alias_for_int',
                        listof='dict')

    assert fa.isa == 'int'
    assert fa.private == True
    assert fa.required == True
    assert fa.inherit == False
    assert fa.default == 8
    assert fa.priority == 4
    assert fa.extend == True
    assert fa.prepend == True
    assert fa.static == True
    assert fa.alias == 'alias_for_int'
    assert fa.listof == 'dict'



# Generated at 2022-06-13 07:51:56.878369
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Check if an exception is raised when no arguments are provided in constructor call
    try:
        from_field = FieldAttribute()
    except TypeError as e:
        assert '__init__() takes at least 1 argument (0 given)' in str(e)
    else:
        raise Exception('Test Failed')

    # Check if the correct arguments are passed along to the constructor of class Attribute
    default_field = FieldAttribute(isa='str', private=False, required=False,
                                   listof=None, priority=0, class_type=None,
                                   always_post_validate=False, inherit=True, alias=None,
                                   extend=False, prepend=False, static=False)
    assert default_field.isa == 'str'
    assert default_field.private == False
    assert default_field.required == False

# Generated at 2022-06-13 07:52:09.694250
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    def test_function():
        pass

    obj = FieldAttribute(isa=None, default=None, required=False, listof=None, priority=0, class_type=None, always_post_validate=False, extend=False, prepend=False)
    assert obj.isa is None
    assert obj.private is False
    assert obj.default is None
    assert obj.required is False
    assert obj.listof is None
    assert obj.priority == 0
    assert obj.class_type is None
    assert obj.always_post_validate is False
    assert obj.extend is False
    assert obj.prepend is False


# Generated at 2022-06-13 07:52:12.505318
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    try:
        FieldAttribute(default=set())
    except TypeError:
        pass
    else:
        assert False, "failed to raise exception"

# Generated at 2022-06-13 07:52:23.177243
# Unit test for constructor of class Attribute
def test_Attribute():
    # for now, this is a very simple test
    # later the test is expanded to verify
    # the Attribute class works as expected
    attribute = Attribute(isa='string', required=True)
    assert attribute.isa == 'string'
    assert attribute.private == False
    assert attribute.default is None
    assert attribute.required == True
    assert attribute.listof is None
    assert attribute.priority == 0
    assert attribute.class_type is None
    assert attribute.always_post_validate == False
    assert attribute.inherit == True
    assert attribute.alias is None
    assert attribute.extend == False

# Generated at 2022-06-13 07:52:25.301507
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    a = FieldAttribute(isa='list', static=True)
    assert a.isa == 'list'
    assert a.static == True


# Generated at 2022-06-13 07:52:33.669233
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.playbook import PlayBook, Play

    #
    # Test "basic" isa types
    #

    # Test a simple attribute
    attr = FieldAttribute(isa='str')
    assert attr.isa == 'str'

    # Test an attribute which is a list of other attributes
    attr = FieldAttribute(isa='list')
    assert attr.isa == 'list'
    attr = FieldAttribute(isa='list', listof='int')
    assert attr.isa == 'list'
    assert attr.listof == 'int'

    # Test an attribute which is a dict containing other attributes
    attr = FieldAttribute(isa='dict')
    assert attr.isa == 'dict'
    attr = FieldAttribute(isa='dict', listof='int')
    assert attr.isa == 'dict'


# Generated at 2022-06-13 07:52:36.800155
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(private=True,
                          default='',
                          required=True,
                          listof=True,
                          priority=1,
                          extend=False,
                          prepend=False,
                          static=False)
    assert(attr.private == True)
# End unit test for constructor of class FieldAttribute



# Generated at 2022-06-13 07:52:38.168240
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    field_attribute = FieldAttribute(isa = 'str')
    assert field_attribute.isa == 'str'


# Generated at 2022-06-13 07:52:48.278678
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from collections import Mapping

    field = FieldAttribute(listof='string')
    assert field.listof == 'string'

    field = FieldAttribute(listof='string', default=list)
    assert field.listof == 'string'
    assert not isinstance(field.default, type)

    field = FieldAttribute(listof='string', default=lambda: [])
    assert field.listof == 'string'
    assert isinstance(field.default, type(lambda: None))

    field = FieldAttribute(default=Mapping)
    assert field.default is Mapping
    
    field = FieldAttribute(default=dict)
    assert field.default is dict
    
    field = FieldAttribute(default=dict)
    assert field.default is dict

# Generated at 2022-06-13 07:52:54.166644
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



# Generated at 2022-06-13 07:53:05.808238
# Unit test for constructor of class Attribute
def test_Attribute():
    # __init__(self,
    #         isa='str',
    #         private=False,
    #         default=None,
    #         required=True,
    #         listof=None,
    #         priority=0,
    #         class_type=None,
    #         always_post_validate=False,
    #         inherit=True,
    #         alias=None,
    #         extend=False,
    #         prepend=False):

    attr1 = Attribute()
    assert attr1.isa == 'str'
    assert attr1.private == False
    assert attr1.default == None
    assert attr1.required == True
    assert attr1.listof == None
    assert attr1.priority == 0
    assert attr1.class_type == None


# Generated at 2022-06-13 07:53:13.393374
# Unit test for constructor of class Attribute
def test_Attribute():
    x = Attribute()
    assert x.isa is None
    assert x.private == False
    assert x.default is None
    assert x.required == False
    assert x.listof is None
    assert x.priority == 0
    assert x.class_type is None
    assert x.always_post_validate == False
    assert x.inherit == True
    assert x.alias is None
    assert x.extend == False
    assert x.prepend == False
    assert x.static == False

# Generated at 2022-06-13 07:53:16.859495
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().inherit
    assert FieldAttribute(inherit=True).inherit
    assert not FieldAttribute(inherit=False).inherit


# Generated at 2022-06-13 07:53:37.806796
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        test_attr = Attribute(default=[1,2,3])
        assert False
    except TypeError:
        pass
    try:
        test_attr = Attribute(default={1:1})
        assert False
    except TypeError:
        pass
    try:
        test_attr = Attribute(default={'a':1})
        assert False
    except TypeError:
        pass
    try:
        test_attr = Attribute(default=set(['a','a']))
        assert False
    except TypeError:
        pass

# Generated at 2022-06-13 07:53:43.730203
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    att = FieldAttribute(isa='str', required=True)
    assert att.isa == 'str'
    assert att.required == True
    assert att.private == False
    assert att.default is None
    assert att.listof is None
    assert att.priority == 0
    assert att.class_type is None
    assert att.always_post_validate == False
    assert att.inherit == True
    assert att.alias is None
    assert att.extend == False
    assert att.prepend == False
    assert att.static == False



# Generated at 2022-06-13 07:53:53.772208
# Unit test for constructor of class Attribute
def test_Attribute():
    # no args/kwargs
    test = Attribute()
    assert test is not None

    # with isa, private
    test = Attribute(isa="list", private=False)
    assert test.isa == "list"
    assert test.private == False

    # with default, required
    test = Attribute(default="hello", required=True)
    assert test.default == "hello"
    assert test.required is True

    test = Attribute(default="world", required=False)
    assert test.default == "world"
    assert test.required is False

    # with listof
    test = Attribute(listof="boolean")
    assert test.listof == "boolean"

    # with priority
    test = Attribute(priority=1)
    assert test.priority == 1

    # with class_type
   

# Generated at 2022-06-13 07:54:04.838907
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa="CONTAINER")
    assert a.isa == "CONTAINER"
    assert a.private == False
    assert a.default == None
    assert a.required == False
    assert a.priority == 0
    assert a.class_type == None
    assert a.always_post_validate == False
    assert a.inherit == True
    assert a.alias == None
    assert a.extend == False
    assert a.prepend == False

    a.private = True
    assert a.private == True
    a.default = "some value"
    assert a.default == "some value"
    a.required = True
    assert a.required == True
    a.listof = "STRING"
    assert a.listof == "STRING"
    a.priority = 1000

# Generated at 2022-06-13 07:54:10.628715
# Unit test for constructor of class Attribute
def test_Attribute():
    # bad datatype for default
    attr = Attribute(default=list())
    assert attr.default() == []

    # good datatype for default
    attr = Attribute(default=lambda: list())
    assert attr.default() == []

# Generated at 2022-06-13 07:54:15.110045
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa=dict, default=lambda: {"a": 1}, listof=int)
    assert a.isa == dict
    # Used a lambda call to test defaults since mutable objects cannot be used
    assert a.default() == {"a": 1}
    assert a.listof == int

# Generated at 2022-06-13 07:54:20.915967
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute(
        isa='integer',
        private=True,
        default=lambda: 5,
        required=True,
        listof='string',
        priority=3,
        class_type='foo',
        always_post_validate=True,
        inherit=True,
        alias='bar',
        extend=False,
        prepend=True,
    )
    assert f.priority == 3
    assert f.__lt__(Attribute(priority=2))

# Generated at 2022-06-13 07:54:31.663676
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    from units.mock.loader import DictDataLoader
    from ansible.parsing.vault import VaultLib

    is_required = True
    is_not_required = False
    isa_str = 'str'
    isa_bool = 'bool'
    isa_int = 'int'
    isa_float = 'float'
    isa_dict = 'dict'
    isa_unicode = 'unicode'
    isa_list = 'list'
    isa_set = 'set'
    isa_path = 'path'
    isa_complex = 'complex'
    isa_password = 'password'
    isa_list_str = 'list of str'
    isa_list_bool = 'list of bool'
    isa_list_int = 'list of int'


# Generated at 2022-06-13 07:54:35.732519
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute(isa='bool')
    assert isinstance(attr, FieldAttribute)
    assert attr.isa == 'bool'
    assert attr.listof is None


# Generated at 2022-06-13 07:54:36.549646
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().private == False


# Generated at 2022-06-13 07:55:04.888244
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    Attribute()
    assert True


# Generated at 2022-06-13 07:55:14.517133
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Test FieldAttribute constructor with empty parameters
    a = FieldAttribute()
    # Check default values of attributes of a
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

    # Test FieldAttribute constructor with non-default parameters

# Generated at 2022-06-13 07:55:15.321008
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    f.isa



# Generated at 2022-06-13 07:55:21.771700
# Unit test for constructor of class Attribute
def test_Attribute():
    from ansible.playbook.play_context import PlayContext
    import yaml
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.defaults import DefaultVars
    from ansible.playbook.helpers import load_list_of_tasks

    #import ansible.playbook.block
    #from ansible.playbook.handler import Handler

    #import ansible.utils
    #import ansible.inventory
    #import ansible.callbacks
    #import ansible.constants
    #from ansible.executor.task_queue_manager import TaskQueueManager
    #import ansible.executor.process.worker
    #import ansible.plugins
    #from ansible.exec

# Generated at 2022-06-13 07:55:36.788530
# Unit test for constructor of class Attribute
def test_Attribute():

    # Test construction
    a = Attribute(isa='foo')
    assert a.isa == 'foo'
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

    # Test equality and comparison operators
    b = Attribute(isa='bar', priority=1)
    c = Attribute(isa='baz', priority=2)

    assert a == a
    assert b == b
    assert c == c

    assert a != b

# Generated at 2022-06-13 07:55:40.178212
# Unit test for constructor of class Attribute
def test_Attribute():
    try:
        a = Attribute(default={})
        assert False, 'Attribute constructor should not allow a mutable default'
    except TypeError:
        print('Attribute constructor should not allow a mutable default')
    except Exception:
        assert False, 'Attribute constructor raised bad exception'

# Generated at 2022-06-13 07:55:52.091047
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Defaults for all parameters for constructor
    # of class FieldAttribute
    fieldAttribute = FieldAttribute()
    assert fieldAttribute.isa == None
    assert fieldAttribute.private == False
    assert fieldAttribute.default == None
    assert fieldAttribute.required == False
    assert fieldAttribute.listof == None
    assert fieldAttribute.priority == 0
    assert fieldAttribute.class_type == None
    assert fieldAttribute.always_post_validate == False
    assert fieldAttribute.inherit == True
    assert fieldAttribute.alias == None
    assert fieldAttribute.extend == False
    assert fieldAttribute.prepend == False
    assert fieldAttribute.static == False



# Generated at 2022-06-13 07:56:01.952127
# Unit test for constructor of class Attribute
def test_Attribute():
    attr = Attribute(
        listof='str',
        default=[],
        required=True,
        always_post_validate=True,
    )
    assert attr.private == False
    assert attr.required == True
    assert attr.listof == 'str'
    assert attr.default == []
    assert attr.priority == 0
    assert attr.always_post_validate == True

    attr = Attribute(
        isa='str',
        private=True,
        default='foobar',
        required=False,
        always_post_validate=True,
    )
    assert attr.private == True
    assert attr.required == False
    assert attr.listof == None
    assert attr.default == 'foobar'
    assert attr.priority == 0


# Generated at 2022-06-13 07:56:04.244700
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    assert FieldAttribute().__class__ == FieldAttribute
    assert FieldAttribute().priority == 0


# Generated at 2022-06-13 07:56:07.789221
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute(
        isa='dict',
        default={}
    )

    assert fa.isa == 'dict'
    assert fa.default == {}



# Generated at 2022-06-13 07:57:13.563867
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



# Generated at 2022-06-13 07:57:15.799502
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    attr = FieldAttribute()
    assert type(attr) == FieldAttribute

    attr = FieldAttribute(isa='list')
    assert attr.isa == 'list'



# Generated at 2022-06-13 07:57:16.457685
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    pass


# Generated at 2022-06-13 07:57:30.219950
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    f = FieldAttribute()
    assert f.isa == None
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


# Generated at 2022-06-13 07:57:33.681857
# Unit test for constructor of class Attribute
def test_Attribute():
    a = Attribute(isa='dict', required=True, default='foo', always_post_validate=True, inherit=True, alias='foozle')
    assert a



# Generated at 2022-06-13 07:57:43.923910
# Unit test for constructor of class Attribute
def test_Attribute():

    # let's try to create an instance of `Attribute`
    # and check its attributes
    # FIXME: do we really need  `isinstance` methods to return `True` for this test?
    #        the goal of this test is to prove that all attributes are set properly

    fields = [('isa', 'str'),
              ('private', False),
              ('default', None),
              ('required', False),
              ('listof', None),
              ('priority', 1),
              ('class_type', None),
              ('inherit', True),
              ('alias', None)]

    attr = Attribute(**dict(fields))


# Generated at 2022-06-13 07:57:52.476194
# Unit test for constructor of class Attribute
def test_Attribute():
    from collections import Counter
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.compat.six import text_type, binary_type

    a = Attribute()

    # None is always acceptable
    assert a._isa(None)

    # Unfortunately, for non-collection types, we don't know
    # how to create a valid Type object, so we just check that
    # the correct isinstance checks are done in the _isa call
    assert a._isa(Exception())
    assert a._isa(AnsibleUnsafeText(u"foo", warn_only=True))
    assert a._isa(binary_type("foo"))
    assert a._isa(0)
    assert a._isa(0.1)
    assert a._isa(True)

    # Other types we will make a best-effort attempt

# Generated at 2022-06-13 07:58:03.434398
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    # Testing defaults.
    attr = FieldAttribute()
    assert attr.isa == None
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.static == False

    # Testing string constructor
    attr = FieldAttribute('foo')
    assert attr.isa == 'foo'
    assert attr.required == False
    assert attr.listof == None
    assert attr.priority == 0
    assert attr.class_type == None
    assert attr.always_post_validate == False
    assert attr.inherit == True
    assert attr.static == False

    # Testing

# Generated at 2022-06-13 07:58:13.797364
# Unit test for constructor of class Attribute
def test_Attribute():
    foo = Attribute(
        isa='int',
        private=False,
        default=None,
        required=False,
        listof=None,
        priority=0,
        class_type=type,
        always_post_validate=False,
        inherit=True,
        alias=None,
        extend=False,
        prepend=False,
        static=False,
    )
    assert foo.isa == 'int'
    assert foo.private == False
    assert foo.default == None
    assert foo.required == False
    assert foo.listof == None
    assert foo.priority == 0
    assert foo.class_type == type
    assert foo.always_post_validate == False
    assert foo.inherit == True
    assert foo.alias == None
    assert foo.extend == False


# Generated at 2022-06-13 07:58:14.715670
# Unit test for constructor of class FieldAttribute
def test_FieldAttribute():
    fa = FieldAttribute()

