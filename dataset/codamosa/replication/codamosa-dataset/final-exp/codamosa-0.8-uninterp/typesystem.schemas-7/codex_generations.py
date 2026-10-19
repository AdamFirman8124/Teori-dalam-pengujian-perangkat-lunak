

# Generated at 2022-06-14 14:34:31.341320
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    """
    Simple test for method __eq__ of class Schema.
    """
    class MySchema(Schema):
        x: int = 0
        y: int = 0
    s1 = MySchema(x=1, y=2)
    s2 = MySchema(y=2, x=1)
    assert s1 == s2
    s2 = MySchema(y=3, x=1)
    assert not (s1 == s2)

# Generated at 2022-06-14 14:34:39.135081
# Unit test for constructor of class Reference
def test_Reference():
    from json import loads
    # Define a class with a field that's defined as a Reference
    class Person(Schema):
        name = String()
        dob = String()
        # A person may be referenced by a string
        def __str__(self) -> str:
            return self.name
    # Define an object of class Person to serve as a reference
    jane_doe = Person(name="Jane Doe", dob="12-03-2001")
    # Define a schema with a reference to Person
    class Author(Schema):
        name = String()
        dob = String()
        best_friend = Reference(to=jane_doe)
    # Define an object of class Author
    joe_doe = Author(name="Joe Doe")
    # Retrieve the reference to jane_doe
   

# Generated at 2022-06-14 14:34:42.229440
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class Person(Schema):
        name = String()
        age = Integer()
    ref = Reference(to=Person)
    person = Person(name="John Doe", age=42)
    assert ref.serialize(person) == {"name": "John Doe", "age": 42}

# Generated at 2022-06-14 14:34:48.628392
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        """This class is used to test the method __iter__ of class Schema."""

        field_one = Field()
        field_two = Field()
        field_three = Field()

    schema = MySchema(field_one=1, field_two=2, field_three=3)
    assert "field_one" in schema
    assert "field_two" in schema
    assert "field_three" in schema
    assert "field_four" not in schema



# Generated at 2022-06-14 14:34:57.522961
# Unit test for function set_definitions
def test_set_definitions():
    field = Array(Reference("A"))
    assert hasattr(field, '_target_string'), 'Should have target string'
    assert '_target' not in field.__dict__, 'Should not have target'
    defs = SchemaDefinitions()
    set_definitions(field, defs)
    assert hasattr(field, '_target_string'), 'Should still have target string'
    assert '_target' not in field.__dict__, 'Should not have target'
    class A(Schema):
        pass
    defs["A"] = A
    assert hasattr(field, '_target_string'), 'Should have target string'
    assert '_target' in field.__dict__, 'Should have target'

# Generated at 2022-06-14 14:35:01.203784
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
	a = Schema(name='hong', age=10)	
	b = Schema(name='hong', age=10)	
	c = Schema(name='hong', age=13)
	assert a == b
	assert a != c

# Generated at 2022-06-14 14:35:06.445088
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class Dog(Schema):
        name = String()
        age = Integer()

    dog = Dog(name='Cyril', age=1)
    assert dog.serialize() == {'age': 1, 'name': 'Cyril'}


# Generated at 2022-06-14 14:35:10.660324
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    s = Schema(field_1="value_1", field_2="value_2", field_3="value_3")
    fields = list(s)

    assert "field_1" in fields
    assert "field_2" in fields
    assert "field_3" in fields


# Generated at 2022-06-14 14:35:18.274442
# Unit test for method validate of class Reference
def test_Reference_validate():
    #Tests if the validate method returns an instance of the target class
    #Builds a single field schema with a Reference field
    class Person(Schema):
        name = String(max_length=10)

    class PersonSchema(Schema):
        person = Reference(to=Person)
    #Creates a dictionary with input to the validate method
    value = {"person": {"name": "Paulo"}}
    #Creates a person schema
    schema = PersonSchema.validate(value)
    #First test
    assert isinstance(schema.person, Person)
    #Second test
    assert schema.person.name == "Paulo"


# Generated at 2022-06-14 14:35:21.041027
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    schema = Schema({'id': {'type': 'integer'}})
    class User(schema):
        pass
    u = User({'id': 1})
    assert u.serialize() == {'id': 1}


# Generated at 2022-06-14 14:35:58.758212
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import Integer
    from typesystem.schemas import Schema
    from typesystem.errors import ValidationError


    class TestSchema(Schema):
        foo = Integer()


    s = TestSchema(foo=1)
    assert s.foo == 1


    try:
        TestSchema(1)
    except ValidationError:
        pass
    else:
        assert False


    try:
        TestSchema(foo=1, bar=2)
    except TypeError:
        pass
    else:
        assert False


    class TestSchema2(Schema):
        foo = Integer()
        bar = Integer()


    TestSchema2(foo=1)


    s = TestSchema2(foo=1, bar=2)
    assert s.foo == 1


# Generated at 2022-06-14 14:36:07.233689
# Unit test for method validate of class Reference
def test_Reference_validate():
    class_name = 'Person'
    fields = {
        'name': str,
        'age': int
    }
    person_schema = type(class_name, (Schema,), fields)
    a_person = person_schema(name='Max')
    assert(a_person.name == 'Max')
    assert('.name' in '.'.join(str(v) for v in a_person.validate_or_error(a_person).error.messages()))
    a_person = person_schema(name='Max', age=10)
    assert(a_person.name == 'Max' and a_person.age == 10)
    
    
    class_name = 'Car'

# Generated at 2022-06-14 14:36:16.248790
# Unit test for method __len__ of class Schema
def test_Schema___len__():
	dummy_fields = {}
	dummy_args = ()
	dummy_kwargs = {}
	obj_0 = Schema(dummy_args, dummy_kwargs)
	dummy_key = __DUMMY__0
	dummy_value = __DUMMY__1
	dummy_fields[dummy_key] = dummy_value
	dummy_args = ()
	dummy_kwargs = {}
	obj_1 = Schema(dummy_args, dummy_kwargs)
	dummy_key = __DUMMY__2
	dummy_value = __DUMMY__3
	dummy_fields[dummy_key] = dummy_value
	dummy_args = ()
	dummy_kwargs = {}
	obj_2 = Schema(dummy_args, dummy_kwargs)

# Generated at 2022-06-14 14:36:27.748098
# Unit test for method validate of class Reference
def test_Reference_validate():
    # Create a new class
    class Dog(Schema):
        age = int
        breed = str
        list_of_pets = Array(str)
        owner = Reference("Person", nullable=True)
    
    # Create a new class
    class Person(Schema):
        name = str
        age = int
        dogs = Array(Reference(Dog), nullable=True)
    
    # Create a new class
    class Pet(Schema):
        name = str
        age = int
        type = str
        owner = Reference("Person")
    
    # Create a set of definitions
    arrayOfPet = Array(Reference("Pet"))
    person = Reference("Person")
    personClass = Person
    pet = Reference("Pet")
    petClass = Pet
    dog = Reference("Dog")
    dogClass = Dog
    definitions

# Generated at 2022-06-14 14:36:28.965739
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    assert True


# Generated at 2022-06-14 14:36:38.309842
# Unit test for constructor of class Schema
def test_Schema():
    class FooSchema(Schema):
        foo = Integer()
    # test init with proper args
    foo = FooSchema({"foo": 1})
    assert isinstance(foo, FooSchema)
    assert foo.foo == 1
    # test init with invalid args
    try:
        foo = FooSchema({"not_exist": 1})
        raise Exception("Schema init with invalid args should raise error")
    except TypeError as e:
        assert "is an invalid keyword argument for FooSchema()" in str(e)
    try:
        foo = FooSchema({"foo": "1"})
        raise Exception("Schema init with invalid args should raise error")
    except TypeError as e:
        assert "Invalid argument 'foo' for FooSchema()" in str(e)
    # test init with no kwargs


# Generated at 2022-06-14 14:36:44.199880
# Unit test for constructor of class Schema
def test_Schema():
    s = Schema(S1=[S2(a=1, b=2), S2(b=3)])
    assert s == Schema(S1=[S2(a=1, b=2), S2(a=None, b=3)])
    assert s.S1[-1].b == 3
    s.S1[-1] = S2(a=4, b=5)
    assert s == Schema(S1=[S2(a=1, b=2), S2(a=4, b=5)])


# Generated at 2022-06-14 14:36:49.172387
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Initialise of Schema
    schema = Schema()
    # Unit test
    try:
        result = schema.__iter__()
        assert (
            result == []
        ), f"Expected: {[]}, Actual: {result}"
    except TypeError:
        assert False, "Expected: No TypeError"
    # Return of test
    return None


# Generated at 2022-06-14 14:36:58.246843
# Unit test for constructor of class Reference
def test_Reference():
    assert Reference.__init__.__doc__ == None
    assert Reference.__init__.__annotations__ == {'to': typing.Union['str', typing.Type['Schema']], 'definitions': typing.Mapping, 'kwargs': typing.Any, 'return': None}
    assert Reference.__new__.__defaults__ == (None,)
    assert Reference.__dict__['__init__'].__defaults__ == (None,)
    assert Reference.__dict__['__init__'].__annotations__ == {'self': None, 'to': typing.Union['str', typing.Type['Schema']], 'definitions': typing.Mapping, 'kwargs': typing.Any, 'return': None}

# Generated at 2022-06-14 14:37:06.736838
# Unit test for constructor of class Schema
def test_Schema():
    from typing import Sequence
    schema = Schema()
    assert schema == {}
    schema = Schema([])
    assert schema == {}
    schema = Schema({1: 2})
    assert schema == {1: 2}
    schema = Schema(fields=[])
    assert schema == {}
    schema = Schema(fields=[])
    assert schema == {}
    schema = Schema([1, 2, 3])
    assert schema == [1, 2, 3]
    schema = Schema(1, 2, 3)
    assert schema == (1, 2, 3)
    schema = Schema(1, 2, 3, **{})
    assert schema == (1, 2, 3)
    schema = Schema(1, 2, 3, **{4: 5})
    assert schema == (1, 2, 3)
    schema = Sche

# Generated at 2022-06-14 14:37:23.153568
# Unit test for method validate of class Reference
def test_Reference_validate():
    class A(Schema):
        a = String(max_length=1)

    class B(Schema):
        b = String(max_length=2)

    class C(Schema):
        c = String(max_length=3)

    class D(Schema):
        d = String(max_length=4)

    class E(Schema):
        e = Reference('F')

    class F(Schema):
        f = Integer(minimum=0, maximum=1)

    # Case 1:
    # Case 1.1: value is None
    # Case 1.2: value is not None
    # Case 1.2.1: value is str
    # Case 1.2.2: value is not str
    # Case 1.2.2.1: value is in definitions
    # Case 1.2.2.

# Generated at 2022-06-14 14:37:24.362887
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass


# Generated at 2022-06-14 14:37:33.447681
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem import SchemaDefinitions, Object, Integer, String
    from typesystem import Schema, Reference

    class TeamPerson(Schema):
        first_name = String()
        last_name = String()

    class Team(Schema):
        team_name = String()
        members = Array(items=Reference(to="TeamPerson"))

    class Game(Schema):
        game_name = String()
        score = Integer()
        team = Reference(to="Team")

    definitions = SchemaDefinitions()
    Game.make_validator(definitions=definitions)


# Generated at 2022-06-14 14:37:41.814858
# Unit test for constructor of class Reference
def test_Reference():
    assert hasattr(Reference, "__init__"), "Reference class requires a __init__ method"
    reference = Reference('refer_to', definitions = {'refer_to': 'String'}, to = 'refer_to', allow_null = False)
    assert reference.to == 'refer_to'
    assert reference.definitions == {'refer_to': 'String'}
    assert reference.allow_null == False


# Generated at 2022-06-14 14:37:44.456609
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Test1(Schema):
        name = String()
    s = Test1(name="Test")
    assert len(s) == 1


# Generated at 2022-06-14 14:37:55.981274
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.main import Schema
    from typesystem.fields import String, Integer
    class TestSchema(Schema):
        name = String()
        age = Integer()
    class_field = TestSchema()
    assert len(class_field) == 0
    # __init__(self, *args: typing.Any, **kwargs: typing.Any):
    t = TestSchema(name="felipe", age=24)
    assert len(t) == 2
    t = TestSchema(name="felipe", age=24, other="argument")
    assert t.name == "felipe"
    assert t.age == 24
    assert len(t) == 2


# Generated at 2022-06-14 14:37:59.600660
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    test_schema = Schema({'a':1})
    assert len(test_schema) == 1


# Generated at 2022-06-14 14:38:02.164201
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Foo(Schema):
        foo = String()
    assert Foo.fields.keys() == {'foo'}


# Generated at 2022-06-14 14:38:07.493481
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Test(Schema):
        a = Field()

    assert Test() == Test({})
    assert Test({}) == Test()
    assert Test() == Test()

    assert Test(a=1) == Test(a=1)
    assert Test() != Test(a=1)
    assert Test(a=1) != Test()

    assert Test() != "test"
    assert Test() != object()


# Generated at 2022-06-14 14:38:15.782831
# Unit test for constructor of class Schema
def test_Schema():
    # Should not create Schema instance if args is not empty
    try:
        Schema("x")
        assert False
    except AssertionError:
        pass
    try:
        Schema("x", "y")
        assert False
    except AssertionError:
        pass
    try:
        Schema("x", "y", "z")
        assert False
    except AssertionError:
        pass
    try:
        Schema("x", "y", "z", "a")
        assert False
    except AssertionError:
        pass
    try:
        Schema("x", "y", "z", "a", "b")
        assert False
    except AssertionError:
        pass

# Generated at 2022-06-14 14:38:28.582279
# Unit test for function set_definitions
def test_set_definitions():
    class SubSchema(Schema):
        field = Reference("SubSchema")
    class Schema(Schema):
        test_field = Reference("SubSchema")
    definitions = SchemaDefinitions()
    set_definitions(Schema.fields["test_field"], definitions)

# Generated at 2022-06-14 14:38:39.157983
# Unit test for constructor of class Schema
def test_Schema():
    class User(Schema):
        name = String()
        age = Integer()

    user = User(name="Bruce", age=25)
    assert user==User(name="Bruce", age=25)
    assert user.name == "Bruce"
    assert user.age == 25
    assert len(user) == 2
    assert list(user.keys()) == ["name", "age"]
    assert list(user.values()) == ["Bruce", 25]
    assert len(user.items()) == 2
    assert list(user.items()) == [("name", "Bruce"), ("age", 25)]
    # User only takes one argument which must be a dict.
    try:
        User()
        assert False
    except TypeError as e:
        assert str(e)=="__init__() missing 1 required positional argument: 'args'"

# Generated at 2022-06-14 14:38:39.581726
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    pass

# Generated at 2022-06-14 14:38:44.720986
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    try:
        import __main__
    except ImportError:
        import sys
        __main__ = sys.modules["__main__"]

    __main__ = sys.modules["__main__"]
    # Test empty schema
    schema = Schema()
    assert list(schema) == []

    # Test non-empty schema
    schema = Schema(bar=1)
    assert list(schema) == ['bar']


# Generated at 2022-06-14 14:38:56.633419
# Unit test for constructor of class Reference
def test_Reference():
    test1 = Reference(to = None)
    assert type(test1.to) == str
    assert test1.definitions == None
    assert test1._target == None
    assert test1._target_string == None
    assert test1.errors == {"null": "May not be null."}
    assert test1.allow_null == False
    assert test1.child == None
    assert test1.name == None
    assert test1.label == None
    assert test1.description == None
    assert test1.example == None
    assert test1.read_only == False
    assert test1.write_only == False
    assert test1.missing_value == None
    assert test1.default_value == None
    assert test1.null_value == None
    assert test1.enum_values == None
    assert test1._creation

# Generated at 2022-06-14 14:39:08.645110
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    import types
    import unittest
    from unittest.mock import patch

    class _SchemaMetaclass(SchemaMetaclass):
        def __new__(  # type: ignore
            cls: type,
            name: str,
            bases: typing.Sequence[type],
            attrs: dict,
            definitions: SchemaDefinitions = None,
        ) -> type:
            return super(_SchemaMetaclass, cls).__new__(  # type: ignore
                cls, name, bases, attrs, definitions
            )

    class _Schema(Schema, metaclass=_SchemaMetaclass):
        pass

    class A(_Schema):
        pass

    class B(_Schema):
        pass

    class C(_Schema):
        pass


# Generated at 2022-06-14 14:39:14.160901
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class ExampleSchema(Schema):
        name = String()
        age = Integer()
        weight = Float()
        is_active = Boolean(default=True)

    schema = ExampleSchema(name="Joe", age=20, weight=180.2)
    assert list(schema) == ["name", "age", "weight"]



# Generated at 2022-06-14 14:39:25.544003
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    #define class A
    class A(Schema):
        #define fields
        a = String(max_length=10)
        b = Integer(minimum=1, maximum=10)
        c = Object(
            properties={
                "d": Boolean(),
                "e": Integer(maximum=1, exclusive_maximum=True),
            }
        )

    assert isinstance(A.fields, dict)
    assert len(A.fields) == 3

    x = A(a="1", b=2)
    assert x.a == "1"
    assert x.b == 2

    y = A(x)
    assert y.a == "1"
    assert y.b == 2

    z = A(a="1", d=True, e=1)
    assert z.a == "1"
    assert z.b

# Generated at 2022-06-14 14:39:28.452700
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class A(Schema):
        a = Integer()

    class B(Schema):
        b = Field()

    class Parent(Schema):
        a = Reference(A)
        b = Reference(B, definitions=definitions)

    set_definitions(Parent, definitions)

    assert Parent.fields["a"].definitions is None
    assert Parent.fields["b"].definitions is definitions

# Generated at 2022-06-14 14:39:37.966698
# Unit test for method validate of class Reference
def test_Reference_validate():
    schema_defs = {}
    class A(Schema, metaclass=SchemaMetaclass, definitions=schema_defs):
        a_prop = Reference("B")

    class B(Schema, metaclass=SchemaMetaclass, definitions=schema_defs):
        b_prop = String()
        # Eventhough we don't use this properties in the validation
        # we need to aks for them for it to work
        a_prop = String()

    res, _ = A.validate_or_error({
        "a_prop": { 
            "b_prop": "b_prop"
        }
    })
    assert isinstance(res, A)
    assert isinstance(res.a_prop, B)
    assert res.a_prop.b_prop == "b_prop"

# Generated at 2022-06-14 14:39:54.021356
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class A(Schema):
        pass
    assert A() == A()
    class B(Schema):
        a = String()
    assert B() == B()
    assert B(a="b") == B(a="b")
    assert B(a="b") != B(a="c")
    class C(Schema):
        a = String()
        b = String()
    assert C(a="b", b="c") == C(a="b", b="c")
    assert C(a="b", b="c") != C(a="b", b="d")
    assert C(a="b", b="c") != C(a="d", b="c")


# Generated at 2022-06-14 14:40:04.786751
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Initialize a Schema instance with iterable of fields and field properties
    schema_instance = Schema(
        {
            "id": "1",
            "order_item_id": "2",
            "quantity": 2,
            "variation": {
                "id": "3",
                "product_id": "4",
                "name": "Large",
                "sku": "5",
            },
        }
    )
    # Set the expected value for __iter__
    expected_value = ["id", "order_item_id", "quantity", "variation"]
    # Get the actual value from __iter__
    actual_value = [key for key in schema_instance]
    # Assert the result
    assert actual_value == expected_value


# Generated at 2022-06-14 14:40:07.784635
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from core.models import Account
    a = Account()
    assert a.__repr__() == 'Account(label=None, type=None, is_primary=False)'

# Generated at 2022-06-14 14:40:15.852647
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
  s = Schema("name")
  assert repr(s) == "Schema(name={'c': {'a': 1, 'b': 2}})"
  s = Schema("name", {"a": 1, "b": 2})
  assert repr(s) == "Schema(name={'c': {'a': 1, 'b': 2}})"
  s = Schema("name", {})
  assert repr(s) == "Schema(name={})"
  s = Schema("name", {'a': 1})
  assert repr(s) == "Schema(name={'a': 1})"

test_Schema___repr__()

# Generated at 2022-06-14 14:40:16.704523
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert Schema().__len__() == 0

# Generated at 2022-06-14 14:40:23.919254
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)
        height = Float(minimum=0.0)

    me = Person(name="John", age=30, height=1.75)
    assert repr(me) == "Person(age=30, height=1.75, name='John')"

# Generated at 2022-06-14 14:40:25.147176
# Unit test for function set_definitions
def test_set_definitions():
    class A:
        field: Reference

    assert hasattr(A(), 'field')
    assert A().field is None



# Generated at 2022-06-14 14:40:31.390250
# Unit test for method validate of class Reference
def test_Reference_validate():
    class FooSchema(Schema):
        foo = String()

    foo = FooSchema(foo='bar')
    schema = Reference(to=foo)
    result = schema.validate(foo)
    assert result.foo == 'bar'

    result = schema.validate({'foo':'bar'})
    assert result.foo == 'bar'

    result = schema.validate(FooSchema(foo='bar'))
    assert result.foo == 'bar'


# Generated at 2022-06-14 14:40:33.316780
# Unit test for constructor of class Schema
def test_Schema():
    assert Schema(MessageRequest(msg_id = '123')) == {'msg_id': 123}
    
    
    


# Generated at 2022-06-14 14:40:37.032607
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(Schema):
        a = 100
        b = 200
        fields = {'a':a,'b':b}
    assert repr(A) == 'A(a=100, b=200)'



# Generated at 2022-06-14 14:41:07.063692
# Unit test for method validate of class Reference
def test_Reference_validate():
    # create definitions
    def1 = {'Person': Person}
    def2 = {'Person': Person, 'Book': Book}
    # create data instance
    person = Person('Tom', 20)
    book = Book('Python', person, 88.8)
    person2 = Person('Jack', 30)
    book2 = Book('JavaScript', person2, 66.6)
    #test case 1
    expected1 = {'name': 'Tom', 'age': 20}
    t1 = Reference('Person', def1)
    r1 = t1.validate(person)
    assert r1 == expected1
    #test case 2
    expected2 = {'Person': {'name': 'Tom', 'age': 20}}
    t2 = Reference('Person', def1)

# Generated at 2022-06-14 14:41:13.099301
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        key1 = Field()
        key2 = Field()

    schema1 = TestSchema(key1="value1", key2="value2")
    schema2 = TestSchema(key1="value1", key2="value2")
    assert(schema1 == schema2)


# Generated at 2022-06-14 14:41:22.032051
# Unit test for function set_definitions
def test_set_definitions():
    class TestSchema1(Schema):
        field1 = Reference("TestSchema2")
        field2 = Array(Reference("TestSchema2"))
        field3 = Array(
            [
                Reference("TestSchema2"),
                Reference("TestSchema2"),
            ]
        )
        field4 = Object(
            properties={
                "field1": Reference("TestSchema2"),
                "field2": Array(Reference("TestSchema2")),
            }
        )

    class TestSchema2(Schema):
        field1 = Field()

    definitions = SchemaDefinitions()
    set_definitions(TestSchema1, definitions)
    assert TestSchema1.field1.definitions is definitions
    assert TestSchema1.field2.definitions is definitions

# Generated at 2022-06-14 14:41:31.011134
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert any(Person.__iter__()) == any([key for key in Person.fields if hasattr(Person, key)])
    assert any(Person.__iter__()) == any(['name', 'age', 'address'])
    assert any(Person.__iter__()) == any(['name', 'age', 'address'])
    assert all(Person.__iter__()) == all(['name', 'age', 'address'])
    assert all(Person.__iter__()) == all([key for key in Person.fields if hasattr(Person, key)])
    assert all(Person.__iter__()) == all(['name', 'age', 'address'])


# Generated at 2022-06-14 14:41:43.423959
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Integer, String

    fields = {
        "first": Integer(),
        "last": String(default="Smith")
    }
    Person = Schema(first=Integer(), last=String(default="Smith"))
    assert Person.fields == fields
    assert Person.validate({"first": 1}) == Person(1, "Smith")
    assert Person(first=1) == Person(1, "Smith")
    assert Person(first=1, last="Jones") == Person(1, "Jones")
    try:
        Person(first=1, last="Jones", middle="Quincy")
    except TypeError:
        pass
    else:
        assert False, "Unexpected non-error"
    assert repr(Person(1, "Smith")) == "Person(first=1, last='Smith')"

# Generated at 2022-06-14 14:41:45.174657
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(Schema):
        pass

    assert "A" in Schema.__subclasses__()



# Generated at 2022-06-14 14:41:55.011216
# Unit test for constructor of class Schema
def test_Schema():
    data = {"name": "tester"}
    test = Schema(data)
    assert(test.name == "tester")
    assert(test.__class__.__name__ == "Schema")
    assert(test.is_sparse == True)
    assert(test == Schema(name="tester"))
    test = Schema(name="tester")
    assert(test.name == "tester")
    assert(test.__class__.__name__ == "Schema")
    assert(test.is_sparse == True)
    assert(test == Schema(name="tester"))


# Generated at 2022-06-14 14:42:03.100951
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Setup
    from .objects import Simple, NullableSimple
    simple1 = Simple(a="simple1")
    simple2 = Simple(a="simple2")
    nullable_simple1 = NullableSimple(a="nullable_simple1")
    nullable_simple2 = NullableSimple(a="nullable_simple2")

    # AssertionError: {'a': 'simple1'} != {'a': 'simple2'}
    assert simple1 == simple2
    # {'a': 'nullable_simple1'}
    print(nullable_simple1)
    # AssertionError: {'a': 'nullable_simple1'} != {'a': 'nullable_simple2'}
    assert nullable_simple1 == nullable_simple2
    # {'a': 'simple2'}
   

# Generated at 2022-06-14 14:42:07.473990
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        a = (1, 2)
        b = 2

    schema = TestSchema()
    assert list(schema.__iter__()) == ['a', 'b']



# Generated at 2022-06-14 14:42:10.411826
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Create instance
    schema = Schema()

    # Call method
    result = schema.__getitem__()

    assert result == 'expected result'


# Generated at 2022-06-14 14:42:37.954169
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Test when self: is sparsely populated
    obj = Schema()
    try:
        result = obj.__len__()
    except:
        assert False, "Unable to calculate length of sparsely populated Schema"
    else:
        assert result == 0, "Did not calculate length of sparsely populated Schema"
    
    # Test when self: is fully populated
    obj = Schema()
    try:
        result = obj.__len__()
    except:
        assert False, "Unable to calculate length of fully populated Schema"
    else:
        assert result == 0, "Did not calculate length of fully populated Schema"



# Generated at 2022-06-14 14:42:47.103512
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String

    class Person(Schema):
        name = String()
        age = String()

    p1 = Person({"name": "Alice"})
    assert len(p1) == 1
    assert list(p1) == ["name"]
    assert p1.is_sparse is True

    p2 = Person({"name": "Alice", "age": "21"})
    assert len(p2) == 2
    assert list(p2) == ["name", "age"]
    assert p2.is_sparse is False



# Generated at 2022-06-14 14:42:50.890729
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class SampleSchema(Schema):
        name = String()
        age = Integer()
    schema = SampleSchema(name="Chinh", age=18)
    assert schema.__iter__() == ['name', 'age']

# Generated at 2022-06-14 14:42:54.055491
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import String

    class Person(Schema):
        name = String()
        age = Integer()

    assert "name" in Person.fields
    assert "age" in Person.fields
    assert len(Person.fields) == 2

# Generated at 2022-06-14 14:43:00.361024
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import json
    import typesystem

    class MySchema(typesystem.Schema):
        name = typesystem.String()

    # Serialize a Schema object as a dictionary.
    schema = MySchema(name='Alice')
    schema_dict = schema.__getitem__('name')
    schema_json = json.dumps(schema_dict)
    assert schema_json == '"Alice"'


# Generated at 2022-06-14 14:43:11.275235
# Unit test for method validate of class Reference
def test_Reference_validate():
    # test value not none and pass validation
    field = Reference(to='Name')
    field.definitions = {'Name': Schema}
    data = Schema({"name": "James"}, age=25)
    assert field.validate(data) == data
    
    # test value is none and allow null
    field = Reference(to='Name', allow_null=True)
    field.definitions = {'Name': Schema}
    assert field.validate(None) == None
    
    # test value is none and not allow null
    field = Reference(to='Name')
    field.definitions = {'Name': Schema}
    with pytest.raises(ValidationError) as e:
        assert field.validate(None) == None   
    assert e.value.messages[0].code == 'null'

# Generated at 2022-06-14 14:43:17.185613
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import typesystem
    class SomeSchema(Schema):
        a = typesystem.Integer(minimum=0)
        b = typesystem.String()
        c = typesystem.Integer(maximum=0)

    assert sorted(list(SomeSchema())) == []
    assert sorted(list(SomeSchema(a=5))) == ["a"]
    assert sorted(list(SomeSchema(b=5))) == ["b"]
    assert sorted(list(SomeSchema(b=5, c=-1))) == ["b", "c"]



# Generated at 2022-06-14 14:43:21.296109
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer()

    person = Person(first_name="Jane", last_name="Doe", age=33)
    assert person.first_name == "Jane"
    assert person.last_name == "Doe"
    assert person.age == 33

# Generated at 2022-06-14 14:43:31.694031
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from unittest import TestCase, main
    from typing import Dict, List


    class ExampleSchema(Schema):
        id = Field(type='integer')
        name = Field(type='string', max_length=100)
        tag = Field(type='string', max_length=100, default='cat')
        age = Field(type='integer')


    class TestSchema(TestCase):
        def test___eq__(self):
            example = ExampleSchema(id=1, name='john', age=31)
            case = {
                'delta': {
                    'id': 2,
                    'name': 'mary',
                    'tag': 'cat',
                    'age': 32
                },
                'expected': False
            }

# Generated at 2022-06-14 14:43:39.079213
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Question(Schema):
        foo = Field()
        bar = Field()
        baz = Field()

        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            super().__init__(*args, **kwargs)
            self.foo = "foo"
            self.baz = "baz"

    question = Question()

    result = set(question)
    expected = {"foo", "baz"}

    assert result == expected


# Generated at 2022-06-14 14:44:03.963037
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # test that the iter method iterates over all the
    # existing attributes of the class.

    class TestSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    schema = TestSchema(first=True, second=True, third=True)
    assert set(schema) == set(schema.fields)

    delattr(schema, "first")
    delattr(schema, "second")

    assert set(schema) == {"third"}
    delattr(schema, "third")
    assert set(schema) == set()


# Generated at 2022-06-14 14:44:12.328665
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String(default="Tom")
        age = Integer()

    p = Person()
    assert p.name == "Tom"
    assert p.age is None

    p = Person({"name": "Tom", "age": 18})
    assert p.name == "Tom"
    assert p.age == 18

    p = Person(name="Tom")
    assert p.name == "Tom"
    assert p.age is None

    from collections import namedtuple

    PersonN = namedtuple("Person", ["name", "age"])

    p = Person(PersonN(name="Tom", age=18))
    assert p.name == "Tom"
    assert p.age == 18

    p = Person(name="Tom", age=18)
    assert p.name == "Tom"
    assert p