

# Generated at 2022-06-14 14:34:54.160606
# Unit test for constructor of class Schema
def test_Schema():
    data = dict(a = 1)
    schema = Schema(data)
    assert schema.a == 1

test_Schema()

# Generated at 2022-06-14 14:34:59.993515
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class SimpleSchema(Schema):
        foo = "string"

    class SubSchema(SimpleSchema):
        bar = "string"

    class SubSubSchema(SubSchema):
        baz = "string"

    s = SubSubSchema(foo="foo", bar="bar", baz="baz")
    fields_list = [f for f in s]
    fields_set = set(fields_list)
    assert len(fields_list) == len(fields_set)
    assert 'foo' in fields_set
    assert 'bar' in fields_set
    assert 'baz' in fields_set



# Generated at 2022-06-14 14:35:09.666514
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    key_list = []
    def t1(key):
        key_list.append(key)
    class TestSchema(Schema):
        attr1 = Field()
        attr2 = Field()
        attr3 = Field()
    obj = TestSchema({
        'attr1': 1,
        'attr2': 2,
        'attr4': 4,
    })
    for key in obj:
        t1(key)
    assert len(key_list) == 2
    assert key_list[0] == 'attr1'
    assert key_list[1] == 'attr2'
    
test_Schema___iter__()

# Generated at 2022-06-14 14:35:10.727742
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class DummySchema(Schema):
        pass
    d = DummySchema()
    assert len(d) == 0

# Generated at 2022-06-14 14:35:17.640537
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        class_field = "class_field"
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__(**kwargs)
            self.instance_field = "instance_field"

    # An instance of Schema has two fields - class_field and instance_field
    schema = TestSchema()
    assert len(schema) == 2

    # A Schema with an empty constructor has zero fields
    schema = TestSchema()
    assert len(schema) == 0



# Generated at 2022-06-14 14:35:20.480295
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    schema_class = type("Schema", (Schema,), {})
    set_definitions(schema_class, definitions)
    assert definitions["Schema"] is schema_class


# Generated at 2022-06-14 14:35:26.899688
# Unit test for function set_definitions
def test_set_definitions():
    # A flat field structure
    class A(Schema):
        a1 = String()
        a2 = String()
    assert len(A.fields) == 2
    assert all(type(field) == String for field in A.fields.values())

    # Now a nested structure
    class B(Schema):
        b1 = A()
    assert len(B.fields) == 1
    assert type(B.fields["b1"]) == Object
    assert len(B.fields["b1"].properties) == 2
    assert all(type(field) == String for field in B.fields["b1"].properties.values())
    # The nested fields should be aware of their parent
    assert B.fields["b1"] in [field.parent for field in A.fields.values()]

    class C(Schema):
        c1

# Generated at 2022-06-14 14:35:35.550593
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(DateTime):
        fields = {
            'name': String(max_length=50, min_length=1),
            'age': Integer(multiple_of=2),
            'birth_date': Date,
            'address': String(max_length=50, min_length=1),
        }
        def __init__(self, *args, **kwargs):
            super(Person, self).__init__(*args, **kwargs)
            self.name()
            self.age()
            self.birth_date()
            self.address()
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

# Generated at 2022-06-14 14:35:40.876024
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem.base import TypeSystem
    from typesystem.fields import Reference, String

    names = ["James Bond", "Sherlock Holmes", "Bugs Bunny", "Daffy Duck"]
    class Character(TypeSystem):
        name=String()

    class Story(TypeSystem):
        characters = Reference(to=Character)

    dct = {"characters": [{"name": name} for name in names]}
    story = Story.validate(dct)
    assert len(story.characters) == len(names)
    for character, name in zip(story.characters, names):
        assert character.name == name


# Generated at 2022-06-14 14:35:45.549764
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Foobar(Schema):
        foo = Field(type="integer", min_value=0, max_value=10)
        bar = Field(type="string")

    f = Foobar(foo=3, bar="abc")
    assert all([i in f for i in ["foo", "bar"]])
    f1 = Foobar(foo=3)
    assert f1.is_sparse
    assert all([i in f1 for i in ["foo"]])


# Generated at 2022-06-14 14:36:01.088309
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        a = Field()
        b = Field()
        c = Field()
        d = Field()

    example = ExampleSchema(a=1, b=2, c=3, d=4)
    result = len(example)
    expected = 4
    assert result == expected


# Generated at 2022-06-14 14:36:01.682119
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    pass

# Generated at 2022-06-14 14:36:05.130643
# Unit test for function set_definitions
def test_set_definitions():
    class RelatedSchema(Schema):
        name = Field()

    class MySchema(Schema):
        definitions = SchemaDefinitions()
        items = Array(Reference("RelatedSchema"))

    assert MySchema.items.items.definitions == MySchema.definitions

# Generated at 2022-06-14 14:36:11.217262
# Unit test for function set_definitions
def test_set_definitions():

    class X(Schema):
        x = Field(str)

    class Y(Schema):
        y = Field(int)

    class Z(Schema):
        z = Reference(Y)

    definitions = SchemaDefinitions()
    set_definitions(X.make_validator(), definitions)

    assert 'X' in definitions
    assert X in definitions.values()

    set_definitions(Z.make_validator(), definitions)

    assert 'Y' in definitions
    assert Y in definitions.values()

# Generated at 2022-06-14 14:36:16.456151
# Unit test for constructor of class Reference
def test_Reference():
    to = 'some'
    definitions = {'some': 1}
    field = Reference(to=to, definitions=definitions, required=True)
    assert field.to == to
    assert field.definitions == definitions
    assert field.target == 1
    assert field.target_string == to
    assert field.required == True
    assert field.errors == {'null': 'May not be null.'}



# Generated at 2022-06-14 14:36:24.872798
# Unit test for constructor of class Schema
def test_Schema():
    from ..types import String, Integer
    class Person(Schema):
        name = String(description="A person's name.")
        age = Integer(description="A person's age.")
    p = Person(name='hello', age=123)
    assert p['name'] == 'hello'
    assert p['age'] == 123
    assert list(p.keys()) == ['name', 'age']
    assert len(p) == 2
    #print(repr(p))
    assert repr(p) == "Person(age=123, name='hello')"

# Generated at 2022-06-14 14:36:28.738876
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

  class FooSchema(Schema):
    bar = Field()
    baz = Field()
    boz = Field()
    xyz = Field()
    xxx = Field()
    ttt = Field()
    
    
  foo = FooSchema(bar=True, baz=None, boz=None, xyz=None, xxx=None, ttt=None)
  # test
  result = iter(foo)
  assert result == iter(['bar'])
  assert next(result) == 'bar'
  # clean up
  del foo


# Generated at 2022-06-14 14:36:34.212402
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem.types import String

    class Person(Schema):
        name = String()
        age = Reference(to='Integer')

    person = Person(name='John', age=18)
    assert person.validate(None) is None
    assert person.validate(person) is person
    assert person.validate(dict(name='John', age=18)) == dict(name='John', age=18)

# Generated at 2022-06-14 14:36:42.965917
# Unit test for constructor of class Schema
def test_Schema():
    import json

# Generated at 2022-06-14 14:36:46.545700
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Test(Schema):
        name = 'Test'
        x = 123
        fields = {'y': '123'}

    s = Test()
    result = iter(s)
    assert isinstance(result, typing.Iterator)


# Generated at 2022-06-14 14:36:59.325097
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    schema_fields = {'foo': Field()}
    proto = Schema(schema_fields)
    proto.foo = 1
    assert list(proto.__iter__()) == ['foo']
test_Schema___iter__()


# Generated at 2022-06-14 14:37:04.167476
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        foo = Reference("Bar")
    class Bar(Schema):
        bar = Reference("Foo")

    foo = Foo()
    bar = Bar()

    definitions = SchemaDefinitions()
    definitions["Bar"] = Bar
    definitions["Foo"] = Foo
    set_definitions(foo, definitions)
    set_definitions(bar, definitions)
    assert foo.fields["foo"].target is Bar
    assert bar.fields["bar"].target is Foo

# Generated at 2022-06-14 14:37:05.686148
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(metaclass=SchemaMetaclass):
        pass


# Generated at 2022-06-14 14:37:15.869669
# Unit test for function set_definitions
def test_set_definitions():
    # Make a fake set of definitions.
    definitions = SchemaDefinitions()
    # Make an empty Schema class with a Reference field.
    class TestSchema(Schema, metaclass=SchemaMetaclass):
        id = Reference("Integer")
        # Define the Integer type and add it to the definitions.
        class Integer(Field):
            pass
    set_definitions(TestSchema, definitions)
    # Test that the Reference field has a copy of the definitions
    assert TestSchema.fields["id"].definitions == definitions
    # Test that the Reference field also has a copy of the target field (Integer)
    assert TestSchema.fields["id"].target == TestSchema.Integer



# Generated at 2022-06-14 14:37:18.853898
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    assert repr(Schema()) == "Schema()"
    assert repr(Schema(data={"age":20})) == "Schema(data={'age': 20})"


# Generated at 2022-06-14 14:37:29.303362
# Unit test for constructor of class Reference
def test_Reference():
    assert Reference(Reference).to == Reference
    assert Reference(to="foo").to == "foo"
    assert Reference(to="foo").definitions is None
    assert Reference(to="foo", definitions={}).to == "foo"
    assert Reference(to="foo", definitions={}).definitions == {}
    try:
        Reference(to="foo", definitions=None)
    except AssertionError:
        assert True
    else:
        assert False
    assert Reference(to="foo", definitions={}).target_string == "foo"
    assert Reference(to=Reference).target_string == "Reference"
    assert Reference(to=Reference).target == Reference


# Generated at 2022-06-14 14:37:31.412592
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Test(Schema):
        name = Field()
        age = Field()
    obj = Test(name="Bob", age=12)
    assert len(obj) == 2


# Generated at 2022-06-14 14:37:36.605202
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        a = String()
        b = String()
        c = String()

    instance = ExampleSchema(a="a", b="b", c="c")
    repr_ = repr(instance)



# Generated at 2022-06-14 14:37:46.924617
# Unit test for method validate of class Reference
def test_Reference_validate():
    class ExampleSchema(Schema):
        uuid = String()
        firstname = String()
    class ProfileSchema(Schema):
        address = String()
        register_id = Reference(ExampleSchema)
    # case 1:
    # test case for validate return None
    profile_obj = ProfileSchema.validate(dict(address = "Beijing", register_id = {"uuid": "1", "firstname": "wang"}))
    assert profile_obj.register_id == ExampleSchema.validate(dict(uuid = "1", firstname = "wang"))

    # case 2:
    # test case for if value is None and self.allow_null:
    # return None
    example_obj = ExampleSchema.validate(dict(uuid = "1", firstname = None))

# Generated at 2022-06-14 14:37:52.757933
# Unit test for function set_definitions
def test_set_definitions():
    class Child(Schema):
        test = String()
    class Parent(Schema):
        child = Reference(Child)
    definitions = SchemaDefinitions({"Child": Child})
    set_definitions(Parent.fields["child"], definitions)

test_set_definitions()

# Generated at 2022-06-14 14:38:06.921083
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert len(Schema()) == 0
    assert len(Schema({"a": 1})) == 1
    class Test(Schema):
        a = Field(type_hint=int)
    assert len(Test({})) == 0
    assert len(Test({"a": 1})) == 1


# Generated at 2022-06-14 14:38:09.840754
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")
        print(Person.fields)

if __name__ == '__main__':
    test_SchemaMetaclass___new__()

# Generated at 2022-06-14 14:38:18.432230
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # class A(Schema):
    #    a1 = String()
    #    a2 = Number()
    from .literals import Number, String

    class A(Schema):
        a1 = String()
        a2 = Number()
    A()
    a = A(a1="f1", a2=100)
    result = a.__iter__()
    assert iter(result) == iter(['a1', 'a2'])
    assert result == list(['a1', 'a2'])


# Generated at 2022-06-14 14:38:28.193923
# Unit test for constructor of class Schema
def test_Schema():
    assert Schema()
    assert Schema.__name__ == 'Schema'

# Generated at 2022-06-14 14:38:38.834510
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Create a test schema
    class Person(Schema):
        name = String()

    # Check that accessing invalid keys raises a KeyError
    invalid_key = "invalid"
    try:
        # Access the invalid key
        person = Person()
        value = person[invalid_key]
    except KeyError as e:
        # Check that the error message matches
        assert e.args[0] == invalid_key
    else:
        raise AssertionError(
            f"Accessing an invalid key {invalid_key!r} should raise KeyError"
        )

    # Check normal access
    valid_key = "name"
    # Access the valid key
    person = Person()
    value = person[valid_key]
    # Check the value is None
    assert value is None


# Generated at 2022-06-14 14:38:44.307902
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class VeryBasicSchema(Schema):
        name = String()
        age = Integer(minimum=0)

    assert VeryBasicSchema(name="John", age=22) == VeryBasicSchema(name="John", age=22)
    assert VeryBasicSchema(name="John", age=22) != VeryBasicSchema(name="Bobby", age=22)
    assert VeryBasicSchema(name="John", age=22) != VeryBasicSchema(name="John", age=23)


# Generated at 2022-06-14 14:38:56.164980
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import copy
    import json
    import random

    test_iter_count = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100])
    test_iter_list = []
    for _ in range(0, test_iter_count):
        test_iter_list.append(random.choice([True, False]))
    # 
    test_Schema_obj = Schema()
    for temp_iter in test_iter_list:
        setattr(test_Schema_obj, str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100])), temp_iter)
    # 
    test_ret = test_Schema_obj.__iter__()

# Generated at 2022-06-14 14:39:01.761257
# Unit test for function set_definitions
def test_set_definitions():
    class Child(Schema):
        pass

    class Parent(Schema):
        child = Reference("Child")

    definitions = SchemaDefinitions()

    assert not hasattr(Parent.child, "definitions")
    set_definitions(Parent.child, definitions)
    assert hasattr(Parent.child, "definitions")
    assert Parent.child.definitions == definitions

# Generated at 2022-06-14 14:39:08.006632
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        arg1 = Field()
        arg2 = Field(default=1)
        arg3 = Field(default=2)

    schema_obj = TestSchema(arg1="first")
    actual = schema_obj.__repr__()
    expected = "TestSchema(arg1='first')"
    assert actual == expected

# Generated at 2022-06-14 14:39:13.903175
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class User(Schema):
        username = String(max_length=100)
        email = String(max_length=100)

    user = User(username="bob", email="bob@example.com")
    assert repr(user) == "User(username='bob', email='bob@example.com')"
    user = User(username="bob", email="bob@example.com", foo="bar")
    assert repr(user) == "User(username='bob', email='bob@example.com')"
    user = User(username="bob")
    assert repr(user) == "User(username='bob') [sparse]"
    assert str(user) == "{'username': 'bob'}"
    assert user["username"] == "bob"

# Generated at 2022-06-14 14:39:37.472433
# Unit test for constructor of class Schema
def test_Schema():
	fields = {"name" : "abc", "gender" : "male"}
	schema = Schema(fields)
	assert type(schema) == Schema, "schema is not of the type Schema"


# Generated at 2022-06-14 14:39:40.558642
# Unit test for constructor of class Schema
def test_Schema():
  class Person(Schema):
      name = String()

  actual = Person()
  assert actual == {"name": None}


# Generated at 2022-06-14 14:39:45.597193
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Setup
    class User(Schema):
        id = Field(int)
        name = Field(str)

    # Exercise
    assert User(id=1, name="foo") == User(id=1, name="foo")

    # Teardown
    pass


# Generated at 2022-06-14 14:39:51.912328
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class A(Schema):
        a = String()
        b = String(default='b')
        c = String(default='c')

    a = A({"a": "1"})
    assert repr(a) == "A(a='1')"
    assert a.is_sparse == False

a = A({"a": "1"})
assert len(a) == 1
assert a.a == "1"
assert a.b == "b"
assert a.c == "c"


# Generated at 2022-06-14 14:39:53.623927
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    d = {"description": "hello world"}
    assert list(d) == ["description"]

# Generated at 2022-06-14 14:40:03.113911
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    """Test whether the __iter__ method of Schema behaves as expected"""
    class TestSchema(Schema):
        field1 = Field(required=True)
        field2 = Field()

    # Add values to fields that are required
    instance = TestSchema(field1=1)
    result = list(iter(instance))
    expected = ['field1']
    assert result == expected

    # Assign a value to a field that is not required
    instance = TestSchema(field1=1, field2=2)
    result = list(iter(instance))
    expected = ['field1', 'field2']
    assert result == expected

# Generated at 2022-06-14 14:40:11.082891
# Unit test for constructor of class Schema
def test_Schema():
    from schemalite.schema import Article, Person
    article = Article(
        id="123",
        title="Foo",
        author=Person(id="567", name="Lauren Ipsum"),
        date_published="2018-01-10",
    )
    assert article.id == "123"
    assert article.title == "Foo"
    assert article.author.id == "567"
    assert article.author.name == "Lauren Ipsum"
    assert article.date_published == "2018-01-10"


# Generated at 2022-06-14 14:40:15.049290
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    # Setup
    definitions = SchemaDefinitions()
    # Exercise and Verify
    assert isinstance(SchemaMetaclass.__new__(SchemaMetaclass, "FakeSchemaClass", (), {}, definitions), type)
    assert definitions["FakeSchemaClass"] is not None


# Generated at 2022-06-14 14:40:20.805834
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        field_1 = String
        field_2 = String

    s = TestSchema(field_1='test')
    assert len(s) == 1
    s = TestSchema(field_1='test', field_2='test')
    assert len(s) == 2


# Generated at 2022-06-14 14:40:27.439851
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import String

    class Foo(Schema):
        first_name = String()
        last_name = String()

    foo_dict = {
        "first_name": "Thiago",
        "last_name": "Dantas",
    }

    foo_inst = Foo(first_name="Thiago", last_name="Dantas")

    assert foo_dict == foo_inst



# Generated at 2022-06-14 14:41:14.890390
# Unit test for constructor of class Schema
def test_Schema():
    pass
    # print('\n===Unit test for constructor of class Schema===')
    # a = Schema(a=3)
    # print(a)
    # a = Schema(a=3, b=6)
    # print(a)
    # try:
    #     a = Schema(a=3, b=6, c=7)
    # except Exception as e:
    #     print(e)
    # try:
    #     a = Schema(a=3, b='c')
    # except Exception as e:
    #     print(e)



# Generated at 2022-06-14 14:41:20.396430
# Unit test for function set_definitions
def test_set_definitions():
    def_definitions = SchemaDefinitions(
        {
            "test": {
                "test_name": "test_field"
            }
        }
    )

    test = Reference("test")
    test_name = Reference("test_name")

    set_definitions(test, def_definitions)
    set_definitions(test_name, def_definitions)

    assert test is not None
    assert test_name is not None

# Generated at 2022-06-14 14:41:25.134015
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class FooSchema(Schema):
        a = 1
        b = 2

    assert repr(FooSchema(a=5)) == "FooSchema(a=5)"
    assert repr(FooSchema(a=5, b=6)) == "FooSchema(a=5, b=6)"


# Generated at 2022-06-14 14:41:30.553051
# Unit test for constructor of class Schema
def test_Schema():
    class User(Schema):
        name: str
        is_active: bool = False
    user = User(name='programmer')
    assert user.name == 'programmer'
    assert user.is_active == False
    user = User(name='programmer', is_active=True)
    assert user.name == 'programmer'
    assert user.is_active == True

# Generated at 2022-06-14 14:41:36.030266
# Unit test for method validate of class Reference
def test_Reference_validate():
    '''
        This test validates if the method works correctly when argument null or not null.
    '''
    ref = Reference('name')
    assert ref.validate(None) is None
    assert ref.validate('name') == 'name'

# Generated at 2022-06-14 14:41:45.640492
# Unit test for function set_definitions
def test_set_definitions():
    class FooSchema(Schema):
        pass

    class BarSchema(Schema):
        pass

    class BazSchema(Schema):
        foo = Reference(FooSchema)
        bar = Reference(BarSchema)
        baz = Reference(to="BazSchema")

    definitions = SchemaDefinitions()
    definitions[FooSchema.__name__] = FooSchema
    definitions[BarSchema.__name__] = BarSchema

    assert not hasattr(BazSchema.foo, "definitions")
    assert not hasattr(BazSchema.bar, "definitions")
    assert not hasattr(BazSchema.baz, "definitions")

    set_definitions(BazSchema, definitions)

    assert BazSchema.foo.definitions == definitions
    assert BazSche

# Generated at 2022-06-14 14:41:46.972811
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass


# Generated at 2022-06-14 14:41:55.726338
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Address(Schema):
        city = String(max_length=1)
        country = String(max_length=2)
    
    assert Address.fields == {'city': String(max_length=1), 'country': String(max_length=2)}
    
    class Person(Schema):
        name = String(max_length=5)
        address = Reference(Address)
        
    assert Person.fields == {'name': String(max_length=5), 'address': Reference(to=Address, allow_null=True)}
    
    
    

# Generated at 2022-06-14 14:41:58.997687
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Book(Schema):
        title = String(required=True)
        author = String(required=True)

    b1 = Book(title="The Stand", author="Stephen King")
    b2 = Book(title="The Stand", author="Stephen King")
    assert b1 == b2



# Generated at 2022-06-14 14:42:03.182022
# Unit test for function set_definitions
def test_set_definitions():
    class Example(Schema):
        field1 = Reference("other-target")
        field2 = Array(Reference("third-target"))

    definitions = SchemaDefinitions()

    set_definitions(Example.fields["field1"], definitions)
    assert Example.fields["field1"].definitions is definitions

    set_definitions(Example.fields["field2"], definitions)
    assert Example.fields["field2"].items[0].definitions is definitions

# Generated at 2022-06-14 14:42:27.467483
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Schema, Integer, String

    class Person(Schema):
        name = String()
        age = Integer(minimum=0, maximum=150)

    person = Person(name="Paul", age=35)
    assert len(person) == 2



# Generated at 2022-06-14 14:42:30.767267
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    properties = {'a':1,'b':2,'c':3}
    obj = Schema(properties)
    assert iter(obj) == iter(properties)


# Generated at 2022-06-14 14:42:34.350912
# Unit test for method __len__ of class Schema
def test_Schema___len__():
  	assert len(Schema(dict(name='bob', age=20))) == 2
  	assert len(Schema(dict(name='bob'))) == 1

# Generated at 2022-06-14 14:42:37.953754
# Unit test for function set_definitions
def test_set_definitions():
    class Pet(Schema):
        name = Field()

    class Owner(Schema):
        pet = Reference(to="Pet", definitions={"Pet": Pet})

    assert isinstance(Owner.fields["pet"].target, Field)

# Generated at 2022-06-14 14:42:40.068755
# Unit test for constructor of class Schema
def test_Schema():
    obj = Schema()
    assert repr(obj) == "Schema()"
    return obj

# Generated at 2022-06-14 14:42:41.567318
# Unit test for constructor of class Schema
def test_Schema():
    x = Schema(strict=True)


# Generated at 2022-06-14 14:42:45.674688
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class BandSchema(Schema):
        name = String()

    band = BandSchema({"name": "The Beatles"})
    assert band["name"] == "The Beatles"


# Generated at 2022-06-14 14:42:53.189584
# Unit test for constructor of class Schema
def test_Schema():
    assert isinstance(Schema(), Schema)
    assert isinstance(Schema({}), Schema)
    assert isinstance(Schema(dict()), Schema)
    assert isinstance(Schema([]), Schema)
    assert isinstance(Schema(list()), Schema)
    assert isinstance(Schema((1, 2, 3)), Schema)
    assert isinstance(Schema(tuple()), Schema)
    assert isinstance(Schema(1), Schema)
    assert isinstance(Schema(int()), Schema)

# Generated at 2022-06-14 14:42:57.241907
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions({
        "Point": Object(
            properties={
                "x": {"type": "integer"},
                "y": {"type": "integer"},
            },
            additional_properties=False
        )
    })

    class Point(Schema):
        x = {"type": "integer"}
        y = {"type": "integer"}

    assert definitions["Point"] == Point



# Generated at 2022-06-14 14:43:04.276724
# Unit test for constructor of class Reference
def test_Reference():
    assert Reference('to', definitions=None, **kwargs).to == 'to'
    assert Reference('to', definitions=None, **kwargs).definitions == None
    assert Reference('to', definitions=None, **kwargs)._target_string == 'to'
    assert Reference('to', definitions=None, **kwargs)._target == None
    assert Reference('to', definitions=None, **kwargs).target_string == 'to'
    assert Reference('to', definitions=None, **kwargs).target == None


# Generated at 2022-06-14 14:43:31.543483
# Unit test for function set_definitions
def test_set_definitions():
    class A(Schema):
        a = String(max_length=10)
        b = String(max_length=10)

    class B(Schema):
        a = String(max_length=10)
        b = String(max_length=10)
        c = Reference("A", required=False)


if __name__ == "main":
    test_set_definitions()

# Generated at 2022-06-14 14:43:36.101558
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import Number
    class Circle(Schema):
        radius = Number(minimum=0)
        circumference = Number()
        area = Number()
    circle = Circle(radius=1)
    assert len(list(circle.__iter__())) == 1

# Generated at 2022-06-14 14:43:45.751552
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.base import ValidationError

    class Location(Schema):
        latitude = Field(type="number")
        longitude = Field(type="number")

    field_with_default = Field(default='john')
    schema_with_optional_field = type("SchemaWithOptionalField", (Schema,), {"field_with_default": field_with_default})

    location_with_default_fields = Location(latitude=1.2,longitude=0.0)
    location_with_custom_fields = Location(latitude=1.2,longitude=3.2)
    location_with_null_fields = Location(latitude=None, longitude=None)
    schema_with_optional_field_with_default_fields = schema_with_optional_field(field_with_default='john')
    schema_

# Generated at 2022-06-14 14:43:50.904855
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class M(Schema):
        string1 = String(field_name="string1")
        string2 = String(field_name="string2")
    i = M()
    assert list(i.__iter__()) == []
    i = M(MappingProxyType({'string1': '', 'string2': ''}))
    assert list(i.__iter__()) == ['string1', 'string2']


# Generated at 2022-06-14 14:44:00.998052
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.schema import Schema
    from typesystem.fields import String
    from typesystem.exceptions import InvalidType
    from typesystem.utils import get_full_type
    from pytest import raises
    class User(Schema):
        first_name = String()
        last_name = String()
        email = String(required=True)
        age = String(required=False)
    _mock_0_ = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'age': '23',
    }

# Generated at 2022-06-14 14:44:03.314894
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class SchemaTest(Schema):
        field1 = String()
    schema_test = SchemaTest(field1='a')
    assert schema_test['field1'] == 'a'


# Generated at 2022-06-14 14:44:11.216403
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import String
    class A(Schema):
        name = String()
    # 
    class B(Schema):
        name = String()
    # 
    class C(Schema):
        a = Reference(A)
        b = Reference(B)
        c = Reference(B)
    # 
    # 
    c = C(a=A(name="Ivan"),c=B(name="Elena"))
    assert repr(c) == "C(a=A(name='Ivan'), c=B(name='Elena'))"
    assert repr(c) == "C(a=A(name='Ivan'), c=B(name='Elena'))"