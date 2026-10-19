

# Generated at 2022-06-14 14:34:35.081498
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Person(Schema):
        name = Field()

    class Car(Schema):
        make = Field()
        model = Field()



# Generated at 2022-06-14 14:34:39.103464
# Unit test for function set_definitions
def test_set_definitions():
    class Test(Object):
        foo = String()
        bar = String()

    Aschema = Object(properties={"a": String(), "b": Test()})

    definitions = SchemaDefinitions()
    set_definitions(Aschema, definitions)
    assert definitions
    assert definitions["Test"] == Test
    assert definitions["Aschema"] == Aschema


# Generated at 2022-06-14 14:34:43.401359
# Unit test for function set_definitions
def test_set_definitions():
    class Item(Schema):
        name = String()
    class ItemList(Schema):
        items = Array(items=Reference(to=Item))
    definitions = SchemaDefinitions({"Item": Item})
    set_definitions(ItemList.fields["items"], definitions)
    assert ItemList.fields["items"].items.target == Item
    assert ItemList.fields["items"].items.definitions == definitions

# Generated at 2022-06-14 14:34:45.933028
# Unit test for constructor of class Schema
def test_Schema():
    a = Schema({}, a = 1, b = 2)
    assert a.a ==1
    assert a.b ==2


# Generated at 2022-06-14 14:34:50.314823
# Unit test for function set_definitions
def test_set_definitions():
    class Thing(Schema):
        foo = Integer()
        bar = Reference("Thing")

    definitions = SchemaDefinitions()
    set_definitions(Thing.fields["bar"], definitions)
    assert Thing.fields["bar"].definitions is definitions



# Generated at 2022-06-14 14:34:54.743407
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Schema(Schema):
        fields = {"r": String()}

    assert repr(Schema()) == "Schema(r=None) [sparse]"

    assert repr(Schema(r="hello")) == "Schema(r='hello')"

    assert repr(Schema({"r": "hello"})) == "Schema(r='hello')"

# Generated at 2022-06-14 14:35:01.111633
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    class Schema1(Schema, metaclass=SchemaMetaclass, definitions=definitions):
        a = Reference(to="Schema2")
    class Schema2(Schema, metaclass=SchemaMetaclass, definitions=definitions):
        a = Integer()
    assert definitions == {'Schema1': Schema1, 'Schema2': Schema2}
    assert Schema1.fields == {'a': Reference(to="Schema2", definitions=definitions)}
    assert Schema2.fields == {'a': Integer()}
    assert Schema1.make_validator().properties == {
        'a': Reference(to="Schema2", definitions=definitions)
    }
    s = Schema1(a=dict(a=1))

# Generated at 2022-06-14 14:35:12.602638
# Unit test for function set_definitions
def test_set_definitions():
    class Schema1(Schema):
        str_field = Field(str)
        int_field = Field(int)
        array_field = Array((str, int))
        reference_field = Reference("Schema2")

    class Schema2(Schema):
        pass

    definitions = SchemaDefinitions()
    Schema1.validate(dict(str_field="str1", int_field=1, array_field=(1, 2)))
    set_definitions(Schema1.reference_field, definitions)
    assert Schema1.reference_field._target_string == 'Schema2'
    assert Schema1.fields['reference_field']._target_string == 'Schema2'
    definitions['Schema2'] = Schema2
    # If a string reference does not exist, then it should not be added
   

# Generated at 2022-06-14 14:35:16.165385
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int, default=30)

    person = Person(name='John Doe')
    assert person['name'] == 'John Doe'
    assert person['age'] == 30


# Generated at 2022-06-14 14:35:18.944081
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    schema = Schema(**{
        "name": "Max",
        "email": "Example@example.com"
    })
    assert list(schema) == ["name", "email"]



# Generated at 2022-06-14 14:35:42.126908
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem import Schema  # type: ignore
    from typesystem import fields  # type: ignore
    
    
    class UserSchema(Schema):
        id = fields.Integer()
        name = fields.String()
        age = fields.Integer()
    
    
    class BeerSchema(Schema):
        id = fields.Integer()
        name = fields.String()
        drinker = Reference(UserSchema)
    
    
    class BrewerySchema(Schema):
        name = fields.String()
        beers = Array(Reference(BeerSchema))
    

# Generated at 2022-06-14 14:35:45.292373
# Unit test for function set_definitions
def test_set_definitions():
    class TestSchema(Schema):
        ref = Reference("TestReference")

    class TestReference(Schema):
        foo = Field(str)

    definitions = SchemaDefinitions()
    definitions["TestReference"] = TestReference
    set_definitions(TestSchema.fields["ref"], definitions)

# Generated at 2022-06-14 14:35:52.959597
# Unit test for function set_definitions
def test_set_definitions():
    a = Reference("a")
    assert not hasattr(a, "definitions")
    class D(dict):
        pass
    definitions = D(a=True)
    set_definitions(a, definitions)
    assert hasattr(a, "definitions")
    assert a.definitions is definitions
    assert a.definitions["a"] is True  # pylint: disable=unsubscriptable-object
    b = Reference("a")
    c = Reference("a")
    d = [a, b, c]
    set_definitions(d, definitions)
    assert id(d[0].definitions) == id(d[1].definitions)
    assert id(d[1].definitions) == id(d[2].definitions)
    f = Array(items=d)

# Generated at 2022-06-14 14:35:55.283675
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    s = Schema()
    assert isinstance(s.__iter__(), collections.abc.Iterator)



# Generated at 2022-06-14 14:36:01.438073
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String()
        age = Integer(minimum=0)
    
    person = Person(name='Jason', age=20)
    lst = list(person)
    assert(lst == ['name', 'age']) == True
    person = Person(name='Jason')
    lst = list(person)
    assert(lst == ['name']) == True


# Generated at 2022-06-14 14:36:11.702411
# Unit test for constructor of class Schema
def test_Schema():
    import pytest
    from typesystem import Integer, String


    class Person(Schema):
        first_name = String(default="Eric")
        age = Integer(minimum=0, maximum=150)
        description = String()

    # Test that data is required for all fields
    with pytest.raises(
        TypeError, match=r"Invalid argument 'description' for Person\(\)"
    ):
        Person(
            first_name="Eric", age=33,
        )

    # Test that no unexpected parameters can be passed
    with pytest.raises(
        TypeError, match=r"extra is an invalid keyword argument for Person\(\)"
    ):
        Person(first_name="Eric", age=33, description="Hello!", extra=True)

    # Test that all parameters get set

# Generated at 2022-06-14 14:36:16.289591
# Unit test for constructor of class Reference
def test_Reference():
    import typesystem
    class SchemaExample(typesystem.Schema):
        string1 = typesystem.String()
        string2 = typesystem.String()
    class ExampleReference(typesystem.Reference):
        to: typesystem.SchemaExample = SchemaExample
    assert isinstance(ExampleReference(), typesystem.Reference)
test_Reference()

# Generated at 2022-06-14 14:36:24.313589
# Unit test for constructor of class Schema
def test_Schema():
    assert (Schema.validate(1) is None)
    schema = Schema.validate([{'title': 'Titanic', 'rating': 7.8}])
    assert schema == {'title': 'Titanic', 'rating': 7.8}
    assert Schema.validate(None) is None
    schema = Schema.validate({"title": "Titanic", "rating": 10})
    assert schema == {"title": "Titanic", "rating": 10}



# Generated at 2022-06-14 14:36:28.014342
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        first = String(required=True)
        last = String(required=True)

    person = Person(first="Ernest", last="Hemingway")
    test = len(person)
    assert test == 2


# Generated at 2022-06-14 14:36:31.367521
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    a = C(a=1)
    b = C(a=2)

    assert(a == a)
    assert(a != b)
    assert(b == b)


# Generated at 2022-06-14 14:36:45.134337
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Setup
    class A(Schema):
        a = Field()
        b = Field()

    # Exercise
    o = A(a=0, b=1)

    # Verify
    assert o['a'] == 0
    assert o['b'] == 1
    assert o.a == 0
    assert o.b == 1


# Generated at 2022-06-14 14:36:45.785400
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    pass


# Generated at 2022-06-14 14:36:47.248312
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.fields import String

    class TestSchema(Schema):
        to = Reference("to_string", definitions=None)
        test_string = String(max_length=10)

    assert TestSchema.__name__ == 'TestSchema'

# Generated at 2022-06-14 14:36:56.468595
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    my_schema = Schema(
        properties={
            "key1": String(max_length=2),
            "key2": String(max_length=2),
            "key3": String(max_length=2),
        },
        required=["key1", "key2", "key3"],
        additional_properties=False,
    )
    print("初期値: ", my_schema)
    assert len(my_schema) == 0

# Generated at 2022-06-14 14:37:01.453257
# Unit test for function set_definitions
def test_set_definitions():
    class A(Schema):
        name = Field()

        class Meta:
            definitions = SchemaDefinitions()

    class B(Schema):
        foo = Field()
        bar = Field(items=Reference("A"))

        class Meta:
            definitions = SchemaDefinitions()

    field = B.fields["bar"]
    assert isinstance(field, Array)
    assert isinstance(field.items, Reference)
    assert field.items.definitions is not None



# Generated at 2022-06-14 14:37:08.034198
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import String, Integer, Float, Boolean, Enum, Reference

    # String fields
    class StringFields(Schema):
        # String fields
        f1 = String()
        f2 = String(format="url", max_length=10)
        f3 = String(default="default value")
        f4 = String(default="default value", required=True)

    # Integer fields
    class IntegerFields(Schema):
        # Integer fields
        f5 = Integer(minimum=0, exclusive_minimum=True)
        f6 = Integer(maximum=10, exclusive_maximum=True)
        f7 = Integer(multiple_of=2, default=42)
        f8 = Integer(default=42, required=True)

    # Float fields
    class FloatFields(Schema):
        # Float fields
        f9

# Generated at 2022-06-14 14:37:19.145526
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Contact(Schema):
        name = String()
        phone = String()
        email = String()

    contact = Contact(name="John")  # type: ignore
    print(contact.__repr__())
    if contact.__repr__()!="Contact(name='John') [sparse]":
        return False

    contact.phone = "555-111-2222"
    contact.email = "test@test.test"
    print(contact)
    if contact.__repr__()!="Contact(name='John', phone='555-111-2222', email='test@test.test')":
        return False
    return True


if __name__ == "__main__":
    if not test_Schema___repr__():
        exit(-1)

# Generated at 2022-06-14 14:37:27.767796
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TaskSchema(Schema):
        title = String()
        completed = Boolean(default=False)

    task_schema = TaskSchema(title="write tests", completed=False)
    assert task_schema.__repr__() == "TaskSchema(title='write tests', completed=False)"

    task_schema = TaskSchema(completed=False)
    assert task_schema.__repr__() == "TaskSchema(completed=False) [sparse]"



# Generated at 2022-06-14 14:37:32.164777
# Unit test for method validate of class Reference
def test_Reference_validate():
    class BeforeAfter(Schema):
        before = Reference("After")
        # before = Reference(After)
        after = Field()

    result = BeforeAfter.validate({"before": "test", "after": "test2"})
    assert result.before == "test"
    assert result.after == "test2"
    assert result.is_sparse is False


# Generated at 2022-06-14 14:37:37.333692
# Unit test for constructor of class Schema
def test_Schema():
    assert issubclass(Schema, Mapping)
    assert Schema.__name__ == 'Schema'
    assert Schema.__module__ == __name__
    assert Schema.__metaclass__ == SchemaMetaclass


# Generated at 2022-06-14 14:37:58.758660
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Test for valid value types
    def test_valid():
        class Student(Schema):
            name = String()
            age = Integer()

        student1 = {
            "name": "John",
            "age": 20
        }
        student2 = Student(**student1)
        assert student1["name"] == student2["name"]
        assert student1["age"] == student2["age"]

    # Test for invalid value type
    def test_invalid():
        class Student(Schema):
            name = String()
            age = Integer()

        student1 = {
            "name": "John",
            "age": 20
        }
        student2 = Student(**student1)
        with pytest.raises(KeyError):
            student1["invalid_key"]


# Generated at 2022-06-14 14:38:08.231386
# Unit test for function set_definitions
def test_set_definitions():
    class SuperSchema(Schema):
        prop1 = Reference("SubSchema")
        prop2 = Array(
            items=Reference("SuperArraySchema"),
        )

    class SubSchema(Schema):
        pass

    definitions = SchemaDefinitions()
    set_definitions(SuperSchema.fields["prop1"], definitions)
    set_definitions(SuperSchema.fields["prop2"].items, definitions)
    assert (
        SuperSchema.fields["prop1"].definitions is definitions
    ), "Expected reference.definitions to be set."
    assert (
        SuperSchema.fields["prop2"].items.definitions is definitions
    ), "Expected reference.definitions to be set."

# Generated at 2022-06-14 14:38:17.001280
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Integer, String
    from typesystem.fields import Object

    class Example(Schema):
        foo = String()
        bar = Integer()

    # Test the get the len of a Schema
    example = Example(foo='foo', bar=1)
    assert len(example) == 2

    # Test when the Object has a sub-object
    class Example2(Schema):
        foo = String()
        bar = Object(properties={'baz': String()})

    example = Example2(foo='foo', bar={'baz': 'baz'})
    assert len(example) == 2


# Generated at 2022-06-14 14:38:20.251557
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        test_value = Field(type="string")

    schema = MySchema(test_value="Another value")
    assert schema.test_value == "Another value"

# Generated at 2022-06-14 14:38:27.918552
# Unit test for constructor of class Schema
def test_Schema():
    o = Schema({"a": "apa", "b": "banan"})
    assert o.a == "apa"
    assert o.b == "banan"

    try:
        o = Schema({"a": "apa", "c": "citron"})
    except TypeError as e:
        assert "citron is" in str(e)
        pass

    try:
        o = Schema({"a": "apa", "b": "banan"}, z="zebra")
    except TypeError:
        pass

    assert o.a == "apa"
    assert o.b == "banan"



# Generated at 2022-06-14 14:38:38.581603
# Unit test for method validate of class Reference
def test_Reference_validate():
    # test for boolean value
    boolean_field = Reference('boolean')
    assert boolean_field.validate(True) == True
    assert boolean_field.validate(False) == False
    with pytest.raises(ValidationError):
        boolean_field.validate(None)
    # test for integer value
    integer_field = Reference('integer')
    assert integer_field.validate(0) == 0
    assert integer_field.validate(1) == 1
    with pytest.raises(ValidationError):
        integer_field.validate(None)
    with pytest.raises(ValidationError):
        integer_field.validate('1')
    # test for float value
    float_field = Reference('float')
    assert float_field.validate(0.0) == 0.0
   

# Generated at 2022-06-14 14:38:45.739364
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        bar = Reference("Bar")  # type: ignore
        baz = Reference("Bar")  # type: ignore

    class Bar(Schema):
        bing = Reference("Baz")  # type: ignore
        bong = Reference("Baz")  # type: ignore

    class Baz(Schema):
        pass

    class Qux(Schema):
        pass

    # Set definitions property on all Reference fields
    definitions = SchemaDefinitions()
    definitions["Foo"] = Foo
    definitions["Bar"] = Bar
    definitions["Baz"] = Baz
    definitions["Qux"] = Qux
    set_definitions(Foo, definitions)
    set_definitions(Bar, definitions)
    set_definitions(Baz, definitions)


# Generated at 2022-06-14 14:38:51.242334
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class_ = type("class_", (SchemaMetaclass, ), {"__new__": SchemaMetaclass.__new__})
    name = str()
    bases = list()
    attrs = dict()
    definitions = dict()
    assert isinstance(class_.__new__(class_, name, bases, attrs, definitions), type)

# Generated at 2022-06-14 14:38:52.930661
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass

# Generated at 2022-06-14 14:39:00.495119
# Unit test for function set_definitions
def test_set_definitions():
    class Schema_A(Schema):
        foo = Array(items=Reference("Schema_B"))

    class Schema_B(Schema):
        bar = Reference("Schema_A")

    class Schema_C(Schema):
        baz = Reference("Schema_A")

    class Schema_D(Schema):
        foobar = Reference("Schema_B")

    definitions = SchemaDefinitions()

    set_definitions(Schema_A.fields["foo"], definitions)
    set_definitions(Schema_B.fields["bar"], definitions)
    set_definitions(Schema_C.fields["baz"], definitions)
    set_definitions(Schema_D.fields["foobar"], definitions)

# Generated at 2022-06-14 14:39:24.248995
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Create some test data
    item = {'name': 'bob', 'age': 42}

    # Create a Schema class
    class Foo(Schema):
        name = String()
        age = Integer()

    # Create a Schema instance
    foo = Foo(item)

    # Assert that the length of the Schema instance is 2
    assert len(foo) == 2



# Generated at 2022-06-14 14:39:36.205747
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    s = Schema()
    assert isinstance(s, Schema)

    class A(Schema):
        a = String()

        def __init__(self, x):
            self.x = x
            super(A, self).__init__()

    assert isinstance(A, SchemaMetaclass)
    a = A("test")
    assert isinstance(a, Schema)
    assert a.x == "test"
    assert a.a == ""

    def test_metadata():
        class A(Schema):
            a = String()

        assert A.a.label is None
        assert A.a.description is None

    test_metadata()

    def test_label():
        class A(Schema):
            a = String(label="A")

        assert A.a.label == "A"

# Generated at 2022-06-14 14:39:44.100853
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class A(Schema):
        a = Field(int)
        b = Field(int)

    a = A(a=1)
    assert len(a) == 1
    assert list(a) == ['a']
    assert list(a.fields) == ['a', 'b']

    a = A(a=1, b=2)
    assert len(a) == 2
    assert set(a.fields) == set(a)



# Generated at 2022-06-14 14:39:53.590354
# Unit test for function set_definitions
def test_set_definitions():
    class MyReference(Reference):
        pass

    class MySchema(Schema):
        x = MyReference("MySchema")

    def assertDefinition(field: Field, definition: type) -> None:
        assert isinstance(field, Reference)
        assert field.to == definition.__name__
        assert field.target == definition

    definitions = SchemaDefinitions()
    set_definitions(MySchema.x, definitions)
    assertDefinition(MySchema.x, MySchema)

    class LevelOne(Schema):
        x = MyReference("LevelTwo")

    class LevelTwo(Schema):
        x = MyReference("LevelThree")

    class LevelThree(Schema):
        x = MyReference("MySchema")

    set_definitions(LevelOne.x, definitions)

# Generated at 2022-06-14 14:40:04.788054
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
  from collections.abc import Mapping, MutableMapping
  from typesystem.fields import Array, Field, Object
  from typesystem.types import Boolean, Integer, String
  from typesystem.validators import Choice, MaxLength

  class Person(Schema):
      name = String(validators=[MaxLength(max_length=10)])
      age = Integer()

  person = Person({"name": "Alex", "age": 30})

  assert isinstance(person, Mapping)
  assert person == {"name": "Alex", "age": 30}
  assert person["name"] == "Alex"
  assert person["age"] == 30
  try:
      person["invalid"]
  except KeyError:
      assert True
  else:
      assert False


# Generated at 2022-06-14 14:40:12.719868
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class EmptySchema(Schema):
        pass
    s = EmptySchema()
    assert repr(s) == f"EmptySchema()"

    class NonEmptySchema(Schema):
        foo = Field(str)
        bar = Field(str)
    s = NonEmptySchema()
    assert repr(s) == f"NonEmptySchema() [sparse]"
    s = NonEmptySchema(foo="hello", bar="world")
    assert repr(s) == f"NonEmptySchema(foo='hello', bar='world')"



# Generated at 2022-06-14 14:40:16.743226
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        pass

    class TestSchema2(TestSchema):
        pass

    assert TestSchema() == TestSchema()
    assert TestSchema2() == TestSchema2()
    assert TestSchema2() != TestSchema()
    assert TestSchema() != TestSchema2()



# Generated at 2022-06-14 14:40:24.432359
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name: str
        age: int
        address: 'Address'
    person = Person({
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'California',
            'code': 94107,
            'country': 'USA'
        }
    })

# Generated at 2022-06-14 14:40:31.302651
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TempSchema(Schema):
       a = Field()
       b = Field()

    class TempSchema2(Schema):
       a = Field()
       b = Field()
    
    s = TempSchema(a = "aaa", b = "bbb")
    s2 = TempSchema(a = "aaa", b = "bbb")
    s3 = TempSchema2(a = "aaa", b = "bbb")
    assert s == s2
    assert s != s3



# Generated at 2022-06-14 14:40:38.320283
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from copy import copy

    class Person(Schema):
        name = String()
        age = Integer()

        def __init__(self, name: str, age: int) -> None:
            super(Person, self).__init__()
            self.name = name
            self.age = age

    class Team(Schema):
        name = String()
        members = Array(items=Reference(to="Person"))

    definitions = SchemaDefinitions()
    definitions["Person"] = Person
    definitions["Team"] = Team

    team = Team(name="Members", members=[Person(name="Alice", age=25)])
    assert len(team) == 1

    team = Team(name="Members", members=[Person(name="Alice", age=25), Person(name="Bob", age=32)])
    assert len(team) == 2



# Generated at 2022-06-14 14:41:41.168518
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Integer

    class User(Schema):
        age = Integer()

    assert len(User()) == 0
    assert len(User(age=10)) == 1


# Generated at 2022-06-14 14:41:47.599565
# Unit test for constructor of class Schema
def test_Schema():
    class ExampleSchema(Schema):
        field1 = Field(required=True)
        field2 = Field(required=True)
        field3 = Field(required=True)
    # Test Schema.__init__()
    import util
    try:
        e_schema = ExampleSchema()
    except TypeError as e:
        if str(e) != "'field1' is a required field for ExampleSchema().":
            util.print_fail(
                f"Unexpected exception for ExampleSchema() '{str(e)}'")
    else:
        util.print_fail(f"Unexpected result for ExampleSchema() '{e_schema}'")

# Generated at 2022-06-14 14:41:53.982290
# Unit test for constructor of class Schema
def test_Schema():
    class UserSchema(Schema):
        name = Field(type="string", min_length=2)
        email = Field(type="string", min_length=5)
        age = Field(type="number", nullable=True)

    data = {"name": "My Name", "email": "my@email.com"}
    user = UserSchema(data)

# Generated at 2022-06-14 14:42:02.514754
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Verify that __eq__ is implemented.
    # If a class doesn't implement __eq__, the one in object is used, which just
    # checks the object's identity.

    class Author(Schema):
        id = Field(name="id")
        first_name = Field(name="first_name")
        last_name = Field(name="last_name")

    author1 = Author(id=1, first_name="George", last_name="Orwell")
    author2 = Author(id=1, first_name="George", last_name="Orwell")
    author3 = Author(id=2, first_name="George", last_name="Orwell")
    author4 = Author(id=1, first_name="George", last_name="Orwell", middle_name="Julian")

# Generated at 2022-06-14 14:42:12.718304
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Foo(Schema):
        foo = String
        bar = Integer
        baz = Boolean

    class Bar(Schema):
        foo = String
        bar = Integer
        baz = Boolean

    a = Foo(foo="hello")
    b = Foo(foo="world")
    c = Foo(foo="hello", bar=42)
    d = Foo(foo="hello", bar=42, baz=True)
    e = Bar(foo="hello", bar=42, baz=True)

    assert a == a
    assert a == Foo(foo="hello")

    assert a != b
    assert a != c
    assert c != d
    assert d != e

    assert a == Bar(foo="hello")

# Generated at 2022-06-14 14:42:17.348436
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class MySchema(Schema):
        field1 = Field(type="string")
        field2 = Field(type="string")
    s = MySchema(field1="a", field2="b")
    assert s == MySchema(field1="a", field2="b")


# Generated at 2022-06-14 14:42:22.934463
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            setattr(self, "id", 1)
            setattr(self, "name", "Test")

    test_schema = TestSchema(id=1, name="Test")
    assert list(test_schema.__iter__()) == ['id', 'name']


# Generated at 2022-06-14 14:42:29.601284
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class TestSchema(Schema):
        foo = String()
        bar = String()
    assert len(TestSchema.fields) == 2
    TestSchema.fields["foo"].add_error("null", "cannot be null")
    TestSchema.fields["bar"].add_error("null", "cannot be null")
    TestSchema.fields["foo"].allow_none()
    TestSchema.fields["bar"].allow_none()

# Generated at 2022-06-14 14:42:39.808949
# Unit test for constructor of class Schema
def test_Schema():
    class A(Schema):
        a = Field(type="number")
        b = Field(type="number", default=1)
        c = Field(type="number", required=True)

    try:
        A({"a": 1, "c": 3, "d": 4})
    except TypeError:
        print("Invalid argument d for A(). Does not match 'properties' schema.")
    a = A({"a": 1, "c": 3, "b": 4})
    print("a is", a)
    b = A({"a": 1, "c": 3, "b": 4})
    assert a == b
    assert a["a"] == 1 and a["b"] == 4 and a["c"] == 3


test_Schema()

# Generated at 2022-06-14 14:42:51.887773
# Unit test for constructor of class Schema
def test_Schema():
    class ExampleSchema(Schema):
        field_1 = Field(type='number', description='description 1')
        field_2 = Field(type='number', description='description 2')

    # One argument is a dict
    example_schema = ExampleSchema({'field_1': 1, 'field_2': 2})
    assert(example_schema['field_1'] == 1)
    assert(example_schema['field_2'] == 2)

    # One argument is an object
    class example_obj(object):
        field_1 = 1
        field_2 = 2

    example_schema = ExampleSchema(example_obj)
    assert(example_schema['field_1'] == 1)
    assert(example_schema['field_2'] == 2)

    # One argument is a dict containing definition

# Generated at 2022-06-14 14:44:06.124892
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    pass