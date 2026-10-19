

# Generated at 2022-06-14 14:34:50.924517
# Unit test for function set_definitions
def test_set_definitions():
    class Category(Schema):
        name = Field(type="string")

    class Product(Schema):
        category = Reference(to=Category)
        # TODO: test `Reference(to="Category")`

    definitions = SchemaDefinitions()
    set_definitions(Product.make_validator(), definitions)
    assert definitions["Category"] == Category

# Generated at 2022-06-14 14:34:58.386687
# Unit test for constructor of class Reference
def test_Reference():
    assert Reference(to='a', definitions=None, label='b').to == 'a'
    assert Reference(to='a', definitions=None, label='b').definitions == None
    assert Reference(to='a', definitions=None, label='b').label == 'b'
    assert Reference(to='a', definitions=None, label='b').errors == {'null': 'May not be null.'}
    assert Reference(to='a', definitions=None, label='b').allow_null == False
    assert Reference(to='a', definitions=None, label='b').context == {}
    assert Reference(to='a', definitions=None, label='b').description == ''
    assert Reference(to='a', definitions=None, label='b').example == None
    assert Reference(to='a', definitions=None, label='b').to == 'a'


# Generated at 2022-06-14 14:35:03.377837
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        field1 = Field()
        field2 = Field()
    t = TestSchema(field1=1, field2=2)
    assert len(t) == 2


# Generated at 2022-06-14 14:35:13.605263
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Animal(Schema):
        name = String(max_length=100)  # type: ignore
        species = String()  # type: ignore
        age = Number()  # type: ignore

    assert Animal.name.validate("Fido") == "Fido"
    assert Animal.name.validate("Fido the WonderPup") == "Fido the WonderPup"
    try:
        Animal.name.validate("Fido the WonderPup and a really really really long name.")
        assert False
    except ValidationError:
        pass

    assert Animal.species.validate("dog") == "dog"
    assert Animal.age.validate("3") == 3.0



# Generated at 2022-06-14 14:35:16.493155
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem import Schema, Boolean

    class Person(Schema):
        name = Boolean()

    person = Person(name=True)
    assert list(person) == ["name"]


# Generated at 2022-06-14 14:35:21.624431
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Assert that the number fields in version of a Schema
    # is equal to 9
    class Version(Schema):

        major = Integer()
        minor = Integer()
        patch = Integer()
        pre_release = String()
        post_release = String()
        build = String()
        epoch = Integer()
        pre_release_metadata = String()
        post_release_metadata = String()

    assert len(Version()) == 9


# Generated at 2022-06-14 14:35:28.383443
# Unit test for function set_definitions
def test_set_definitions():

    class One(Schema):
        name = Field(type="string")

    class Two(Schema):
        one = Reference(to="One")
        name = Field(type="string")

    class Three(Schema):
        two = Reference(to="Two")
        name = Field(type="string")

    definitions = SchemaDefinitions()
    set_definitions(Three(), definitions)
    assert isinstance(Three.fields["two"].target, type(Two))

# Generated at 2022-06-14 14:35:36.926598
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    print('\n\nUnit test for method __len__ of class Schema')
    #Test 1
    print('Test 1')
    schema = Schema(
        title=Field(type="string"),
        user=Field(type="string"),
        tags=Array(items=Field(type="string")),
    )
    data = {"title": "A Title", "user": "user", "tags": ["foo"]}
    result = schema.validate(data)
    assert len(result) == 3
    data = {"title": "A Title", "user": "user"}
    result = schema.validate(data)
    assert len(result) == 2



# Generated at 2022-06-14 14:35:42.997389
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import unittest

    class TestSchema(Schema):
        field1 = Field(type="string")

    class TestSchema2(Schema):
        field2 = Field(type="string")

    item1 = TestSchema(field1=None)
    item2 = TestSchema(field1=None)
    item3 = TestSchema2(field2=None)
    assert item1 == item2
    assert item1 != item3
    assert item1 != 1
    assert item1 != object()
    assert item1 != object
    assert item1 != None



# Generated at 2022-06-14 14:35:46.825810
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        a = Integer()
        b = Float()

    instance = MySchema(a=5, b=5.0)
    assert list(instance) == ['a', 'b']
    instance = MySchema({'a': 5, 'b':5.0})
    assert list(instance) == ['a', 'b']
    instance = MySchema(a=5)
    assert list(instance) == ['a']


# Generated at 2022-06-14 14:36:06.199327
# Unit test for function set_definitions
def test_set_definitions():
    parent = Object(
        properties={
            'ref': Reference('child'),
            'nested_ref': Array(Reference('child')),
            'nested_nested_ref': Array(Array(Reference('child')))
        }
    )

    class Child(Schema):
        name = String()

    definitions = SchemaDefinitions()
    set_definitions(parent, definitions)

    assert isinstance(parent.properties['ref'], Reference)
    assert isinstance(parent.properties['nested_ref'].items, Reference)
    assert isinstance(parent.properties['nested_nested_ref'].items.items, Reference)

    assert parent.properties['ref'].definitions == definitions
    assert parent.properties['nested_ref'].items.definitions == definitions

# Generated at 2022-06-14 14:36:09.739959
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    person = Person(name="john", age=25)
    assert person.name == "john"
    assert person.age == 25
    return 0


# Generated at 2022-06-14 14:36:18.872904
# Unit test for constructor of class Reference
def test_Reference():
    class Foo(Schema):
        value = String(max_length=10)

    class Bar(Schema):
        foo = Reference(to=Foo)

    b = Bar({"foo": {"value": "hello"}})

    # Unit test for private attribute _target_string
    assert b.foo._target_string == "Foo"

    # Unit test for private attribute _target
    assert b.foo._target == Foo

    # Unit test for private attribute definitions
    assert b.foo.definitions == {Foo.__name__: Foo}

    # Unit test for property target_string
    assert b.foo.target_string == "Foo"

    # Unit test for property target
    assert b.foo.target == Foo

if __name__ == "__main__":
    test_Reference()

# Generated at 2022-06-14 14:36:24.519927
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class A(Schema):
        field1 = Field()
        field2 = Field()

    class B(Schema):
        field1 = Field()
        field2 = Field()

    assert A(field1=1, field2=2) == B(field1=1, field2=2)



# Generated at 2022-06-14 14:36:34.797487
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
  class S(Schema):
      a = Field(default=0)
      b = Field(default=0)
      c = Field(default=0)
  assert S(a=1) == S(a=1)
  assert S(a=1, b=2) == S(a=1, b=2)
  assert S(a=1, b=2, c=3) == S(a=1, b=2, c=3)

  assert S(a=1) != S(a=1, b=2)
  assert S(a=1, b=2) != S(a=1, b=2, c=3)
  assert S(a=1, b=2, c=3) != S(a=1, b=2, c=4)


# Generated at 2022-06-14 14:36:41.266265
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        pass

    class Bar(Schema):
        foo = Reference("Foo")
        foos = Array(Reference("Foo"))
        baz = Object(properties={"foo": Reference("Foo")})

    definitions = SchemaDefinitions()
    assert "Foo" not in definitions
    foo = Foo()
    bar = Bar()
    definitions["Bar"] = bar
    assert "Bar" in definitions
    assert "Foo" not in definitions
    set_definitions(bar, definitions)
    assert "Foo" in definitions
    assert "Bar" in definitions

# Generated at 2022-06-14 14:36:42.932236
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert len(Schema1(a=1)) == 1


# Generated at 2022-06-14 14:36:47.510349
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class FooSchema(Schema):
        id = Integer()
        name = String()
        status = Boolean()

    foo_schema = FooSchema(id=1, name='foo')
    res = dict(foo_schema)
    expected = {'id': 1, 'name': 'foo'}
    assert res == expected
    

# Generated at 2022-06-14 14:36:50.537137
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class SomeSchema(Schema):
        """
        A schema class with a couple of positions.
        """

        field_a = String()
        field_b = String()
        field_c = String()

    instance = SomeSchema(field_b="hello")
    assert list(instance) == ["field_b"]

# Generated at 2022-06-14 14:36:55.995417
# Unit test for method validate of class Reference
def test_Reference_validate():
    print('\n\nTest Reference')
    schema = SchemaDefinitions()
    class Person(Schema):
        name = Field(type=str)
    class PersonRef(Reference):
        to = "Person"
    test_person = Person(name='Test')
    person_ref = PersonRef()
    person_ref.definitions = schema
    person_ref.validate(test_person)
    print("Test passed")
test_Reference_validate()

# Generated at 2022-06-14 14:37:08.667628
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # Testing with a class with defined length
    class TestClass1(Schema):
        field1 = Field()
        field2 = Field()
    a = TestClass1(field1=1, field2=1)
    assert a.__repr__() == "TestClass1(field1=1, field2=1)"



# Generated at 2022-06-14 14:37:16.446303
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
  try:
    from typesystem import schema
  except:
    import schema
  from datetime import datetime

  class PostSchema(schema.Schema):
    title = schema.String(max_length=100)
    created = schema.DateTime()

  post = PostSchema(title="Hello", created=datetime.now())
  assert repr(post) == "PostSchema(title='Hello', created=datetime.datetime(2019, 1, 8, 21, 29, 41, 573273))"

# Generated at 2022-06-14 14:37:20.364840
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import String
    from typesystem.schema import SchemaMetaclass

    class Person(object):
        class __metaclass__(SchemaMetaclass):
            pass

        name = String(max_length=10)

    assert isinstance(Person.fields["name"], String)



# Generated at 2022-06-14 14:37:29.393475
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class C(Schema):
        a = Field()
        b = Field()
        c = Field()

    x = C(a=1, b=2, c=3)
    assert x == {'a': 1, 'b': 2, 'c': 3}
    assert x == {'a': 1, 'c': 3, 'b': 2}
    assert x == {'a': 1, 'b': 2}
    assert x == {'b': 2, 'c': 3}
    assert x == {'b': 2}
    assert x == {'c': 3}


# Generated at 2022-06-14 14:37:30.084635
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Test case 1:
    pass

# Generated at 2022-06-14 14:37:41.390734
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import typesystem

    # Create a class with a 'foo' field
    class FooClass(typing.NamedTuple):
        foo: int

    # Create a schema for that class
    class FooSchema(typing.NamedTuple):
        foo = typesystem.Integer()

    # Create an instance of the class with a value for 'foo'
    foo_tuple = FooClass(foo=5)

    # Create an equivalent schema instance
    foo_schema = FooSchema(foo=5)

    # The class instance and the schema instance should have the same length (1)
    len(foo_tuple) == len(foo_schema)
    

# Generated at 2022-06-14 14:37:48.917976
# Unit test for constructor of class Schema
def test_Schema():
	def fields():
		return dict(
			name = String(max_length=20),
			age = Integer(min_value=0, max_value=150),
			address = String(max_length=30),
			courses = Array(Integer(min_value=1, max_value=9999)),
		)
	def test_init_with_empty_dict():
		schema = Schema(fields=fields())
		for field_name in schema.fields.keys():
			assert not hasattr(schema, field_name)

# Generated at 2022-06-14 14:37:52.987663
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class ExampleSchema(Schema):
        value = Field(type="string")
    es = ExampleSchema(value="example value")
    assert es.__iter__() == ('value',)



# Generated at 2022-06-14 14:37:57.402652
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        age = Integer(minimum=0, maximum=200)

    assert len(Person()) == 0              # type: ignore
    assert len(Person(age=49)) == 1        # type: ignore
    assert len(Person(age=49, name="foo")) == 1  # type: ignore

# Generated at 2022-06-14 14:38:03.412964
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
     class User(Schema):
        name = String()
        age = Integer()

     user = User(name="Bob", age=42)
     assert list(user) == ["name", "age"]

     user = User(name="Bob")
     assert list(user) == ["name"]

     user = User()
     assert list(user) == []



# Generated at 2022-06-14 14:38:17.958648
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from schema import Integer, Schema, String


    class BaseSchema(Schema):
        name = String()


    class ExtendedSchema(BaseSchema):
        age = Integer()


    validator = ExtendedSchema.make_validator()
    valid, error = validator.validate_or_error({'name': 'foo', 'age': 42})
    if error:
        raise error

# Generated at 2022-06-14 14:38:21.359801
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class SomeSchemaWithProp(Schema):
        prop = Field()

    instance = SomeSchemaWithProp({"prop": "value"})
    assert len(instance) == 1
    assert "prop" in instance



# Generated at 2022-06-14 14:38:28.230371
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestSchema(Schema):
        name = String(max_length=100, required=True)
        age = Integer(min_value=0, max_value=150, required=True)
        gender = String(enum=["m", "f"])
    obj = TestSchema(name="Bob", age=10, gender="m")
    assert obj.name == "Bob"
    assert obj.age == 10
    assert obj.gender == "m"
    assert obj["name"] == "Bob"
    assert obj["age"] == 10
    assert obj["gender"] == "m"

# Generated at 2022-06-14 14:38:34.711528
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Foo(object):
        pass
    class_name = 'Foo'
    bases = (object,)
    attrs = {'Foo': Foo, '__module__': 'typesystem.schemas'}
    new_type = SchemaMetaclass.__new__(SchemaMetaclass, class_name, bases, attrs)
    assert new_type == Foo

# Generated at 2022-06-14 14:38:42.730758
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        a = Field(required=True)
        b = Field(required=True)
    s = TestSchema({'a': 10, 'b': 20})
    assert s.a == 10
    assert s.b == 20
    try:
        s = TestSchema({'a': 10})
    except TypeError as e:
        pass
    s = TestSchema(a=10, b=20)
    assert s.a == 10
    assert s.b == 20
    try:
        s = TestSchema(a=10)
    except TypeError as e:
        pass
    s = {'a': 10, 'b': 20}
    assert s['a'] == 10
    assert s['b'] == 20

# Generated at 2022-06-14 14:38:44.457406
# Unit test for constructor of class Schema
def test_Schema():
    schema = Schema({"a": 1})
    assert(schema == {"a":1})


# Generated at 2022-06-14 14:38:56.294971
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import json
    d1 = {
        "name": "Country1",
        "areas": [{
            "name": "Area1",
            "lat": 0,
            "long": 0
        }, {
            "name": "Area2",
            "lat": 0,
            "long": 0
        }]
    }
    d2 = {
        "name": "Country1",
        "areas": [{
            "name": "Area1",
            "lat": 0,
            "long": 0
        }, {
            "name": "Area2",
            "lat": 0,
            "long": 0
        }]
    }

# Generated at 2022-06-14 14:39:00.760964
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from .fields import String
    from .exceptions import ValidationError
    from .utils import ValidationStrict

    class Foo(Schema):
        bar = String()

    foo = Foo(bar='baz')
    result = foo['bar']
    assert result == 'baz'


# Generated at 2022-06-14 14:39:13.207940
# Unit test for method validate of class Reference
def test_Reference_validate():
    class A(Schema):
        a = Int()
    definitions = SchemaDefinitions({"A": A})
    a = Reference("A", definitions=definitions)
    assert a.validate({"a": 1}) == A(a=1)
    a.allow_null = True
    assert a.validate(None, strict=False) is None
    a.allow_null = False
    with pytest.raises(ValidationError) as exc_info:
        a.validate(None)
    assert exc_info.value.as_json() == {
        "code": "null",
        "validator": "reference",
        "path": "",
        "message": "May not be null.",
    }

# Generated at 2022-06-14 14:39:21.189178
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        field1 = Field(int)
        field2 = Field(str)

    assert repr(TestSchema()) == "TestSchema(field1=None, field2=None) [sparse]"
    assert repr(TestSchema(field1=1)) == "TestSchema(field1=1, field2=None)"
    assert repr(TestSchema(field1=1, field2="hello")) == "TestSchema(field1=1, field2='hello')"





# Generated at 2022-06-14 14:39:29.832787
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert 0

# Generated at 2022-06-14 14:39:38.712674
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from .models import Person, Address

    # Test that two schemas with the same attributes are equal.
    person1 = Person(first_name="John", last_name="Smith")
    person2 = Person(first_name="John", last_name="Smith")
    assert person1 == person2

    # Test that two schemas with different attributes are not equal.
    person1 = Person(first_name="John", last_name="Smith")
    person2 = Person(first_name="Jane", last_name="Smith")
    assert not person1 == person2

    # Test that two schemas of a different type are not equal.
    person = Person(first_name="John", last_name="Smith")
    address = Address(street="10 Downing Street", city="London")
    assert not person == address

    # Test that a schema is not equal to

# Generated at 2022-06-14 14:39:46.064437
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String
    from typesystem.schema import Schema

    class Person(Schema):
        first_name = String()
        middle_name = String(required=False)
        last_name = String()

    person = Person(first_name="Joe", last_name="Bloggs")
    lst = sorted(iter(person))
    assert lst == ["first_name", "last_name"]

# Generated at 2022-06-14 14:39:49.961792
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    schema = Schema(dict(a=1, b=2, c=3, d=4, e=5, f=6))
    assert [key for key in ['a', 'b', 'c', 'd', 'e', 'f']] == [key for key in schema]

# Generated at 2022-06-14 14:39:56.424126
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    assert repr(Schema()) == "Schema()"
    assert repr(Schema(1)) == "Schema(1)"
    assert repr(Schema(1,2)) == "Schema(1,2)"
    assert repr(Schema(1,2,3)) == "Schema(1,2,3)"
    assert repr(Schema(1,2,3,4)) == "Schema(1,2,3,4)"
    assert repr(Schema(1,2,3,4,5)) == "Schema(1,2,3,4,5)"
    assert repr(Schema(1,2,3,4,5,6)) == "Schema(1,2,3,4,5,6)"

# Generated at 2022-06-14 14:39:59.388875
# Unit test for method validate of class Reference
def test_Reference_validate():
    obj = Reference(to='string', definitions={'string': str})
    result = obj.validate('hello world', strict=False)
    assert result == 'hello world'


# Generated at 2022-06-14 14:40:06.322847
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import os.path
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from definitions import User, Address
    class UserSchema(Schema):
        address = Reference(to=Address)
    u = User(name='test', address=Address(city='test'))
    s = UserSchema(u)
    assert ('name' in s.keys())
    assert ('address' in s.keys())

# Generated at 2022-06-14 14:40:11.408571
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from pydantic import BaseModel as model
    class User(model):
        id: int
        name = 'John Doe'
        signup_ts: datetime = None
    user = User(id=1)
    for key in ['id', 'name']:
        assert key in user                                                                                                        # +1


# Generated at 2022-06-14 14:40:13.905249
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        name = Field()
        age = Field(required=False)
    schema = TestSchema(name="Olivia")


# Generated at 2022-06-14 14:40:19.711065
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    """SchemaIterator
    :type Schema:
    """
    class Schema(object):
        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            print(args)
            print(kwargs)
        def set_fields(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            print(args)
            print(kwargs)
    one = Schema('a','b','c','d','e','f','g')
    one.set_fields('1','2','3','4','5','6','7')
    assert isinstance(one, Schema)

# Generated at 2022-06-14 14:40:43.189809
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(Schema):
        a = Integer()

    class B(A):
        b = String()

    assert A.fields == {'a': A.a}
    assert B.fields == {'a': A.a, 'b': B.b}


# Generated at 2022-06-14 14:40:45.829925
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        a = Field(value_type=int, default=1)
        b = Field(value_type=str)
    schema = TestSchema(a=1, b='1')
    assert list(schema.__iter__()) == ['a', 'b']

# Generated at 2022-06-14 14:40:51.029339
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    c = Car(car_name='Toyota', price=1234, color='red')
    assert c.__repr__() == "Car(car_name='Toyota', price=1234, color='red')"
    d = Car(car_name='Toyota')
    assert d.__repr__() == "Car(car_name='Toyota', price=None) [sparse]"


# Generated at 2022-06-14 14:41:00.846488
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        def_1 = Reference('def_1')
        def_2 = Reference('def_2')

    class Bar(Schema):
        def_1 = Reference('def_1')
        def_2 = Reference('def_2')

    class Baz(Schema):
        def_1 = Reference('def_1')

    definitions = SchemaDefinitions()
    definitions['def_1'] = Foo
    definitions['def_2'] = Bar

    set_definitions(Baz.fields['def_1'], definitions)
    assert Baz.fields['def_1'].definitions == definitions

# Generated at 2022-06-14 14:41:02.479494
# Unit test for constructor of class Schema
def test_Schema():
    class Foo(Schema):
        bar = String()
    foo = Foo(bar="baz")
    assert foo.bar == "baz"
    foo = Foo()
    assert foo.bar is None


test_Schema()

# Generated at 2022-06-14 14:41:08.036642
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Test Schema.__getitem__
    d = {'item_0': 'test_value_0', 'item_1': 'test_value_1', 'item_2': 'test_value_2', 'item_3': 'test_value_3'}
    p = Schema(d)
    for key, value in d.items():
        assert p[key] == value


# Generated at 2022-06-14 14:41:12.959831
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestSchema(Schema):
        field_1 = String()
        field_2 = String()

    # Test 1
    schema = TestSchema(field_1="field_1", field_2="field_2")
    assert schema["field_1"] == "field_1"


# Generated at 2022-06-14 14:41:18.542826
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class User(Schema):
        username = Field()
        city = Field()
        id = Field()

    user1 = User({"username": "derek", "city": "New York", "id": 123})

    assert list(user1) == ["username", "city", "id"]
    assert list(user1.__iter__()) == ["username", "city", "id"]



# Generated at 2022-06-14 14:41:27.316348
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field = Object(
        properties={
            "nested": Reference(to="Nested", definitions=definitions),
            "array": Array(items=Reference(to="Nested", definitions=definitions)),
        }
    )
    class Nested(Schema):
        name = Field()

    set_definitions(field, definitions)
    assert isinstance(field.properties["nested"].target, Nested)
    assert isinstance(field.properties["array"].items.target, Nested)
    assert len(definitions) == 1
    assert definitions["Nested"] == Nested

# Generated at 2022-06-14 14:41:32.404121
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        age = Field(int)
    p = Person(name="kiko", age=29)
    assert p.name == "kiko"
    assert p.age == 29
    p = Person(dict(name="kiko", age=29))
    assert p.name == "kiko"
    assert p.age == 29


# Generated at 2022-06-14 14:41:53.789856
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    assert(len(Person()) == 0)
    assert(len(Person(name='')) == 1)
    assert(len(Person(age=0)) == 1)
    assert(len(Person(name='',age=0)) == 2)


# Generated at 2022-06-14 14:41:57.740344
# Unit test for method validate of class Reference
def test_Reference_validate():
    class Test(metaclass=SchemaMetaclass):
        foo = Reference(to=str)
    success = Test.validate({'foo': 'bar'})
    assert type(success) == Test
    assert type(success.foo) == str

schemas = SchemaDefinitions()



# Generated at 2022-06-14 14:42:03.827272
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Case 1: An item is accessed
    class Schema_getitem_test_case_1(Schema):
        key = "value"

    my_obj = Schema_getitem_test_case_1()
    assert (my_obj["key"] == "value")
    # Case 2: A non-existing item is accessed (raises KeyError)
    class Schema_getitem_test_case_2(Schema):
        pass

    my_obj = Schema_getitem_test_case_2()
    try:
        my_obj["key"]
    except KeyError as ex:
        assert "key" in str(ex)


# Generated at 2022-06-14 14:42:05.642357
# Unit test for constructor of class Reference
def test_Reference():
    r = Reference(to='test', definitions='test')

test_Reference()

# Generated at 2022-06-14 14:42:12.260801
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Foo(Schema):
        bar = Field(str)
        baz = Field(str)
        qux = Field(str, default="qax")

    foo1 = Foo(bar="1", baz="2")
    foo2 = Foo(bar="1", baz="2")
    foo3 = Foo(bar="1", qux="3")

    assert(foo1 == foo2)
    assert(foo1 != foo3)


# Generated at 2022-06-14 14:42:14.761697
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class Person(Schema):
        name = Field()

    person = Person(name="John")

    assert list(iter(person)) == ['name']

# Generated at 2022-06-14 14:42:23.490472
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.fields import String
    a=Reference('obj1')
    b=Reference('obj1',String())
    try:
        assert a==b
    except AssertionError as err:
        print(err)
    else:
        print('Reference class constructor test Pass')
    definations = SchemaDefinitions()
    obj1 = Schema(definations)
    setattr(obj1, 'id', String())
    setattr(obj1, 'name', String())
    from typesystem.fields import Object
    setattr(obj1, 'address', Object({'street': String(), 'city': String()}))

if __name__=='__main__':
    test_Reference()

# Generated at 2022-06-14 14:42:35.961196
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from unittest import TestCase, main
    from itertools import chain

    class A(Schema):
        a = 1
        b = 2
        c = 3

    class B(A):
        d = 4

    class C(B):
        e = 5

    class Test(TestCase):
        def test_Schema_iterator(self):
            class A(Schema):
                a = 1
                b = 2
                c = 3

            class B(A):
                d = 4

            class C(B):
                e = 5

            self.assertEqual(list(A().__iter__()), ['a', 'b', 'c'])
            self.assertEqual(list(B().__iter__()), ['a', 'b', 'c', 'd'])

# Generated at 2022-06-14 14:42:46.515338
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    # Test that it creates a new type
    class Person(Schema):
        name = String()

    assert Person.__class__ == type(Schema)
    assert Person.fields["name"] == String()

    # Test that it inherits fields
    class Employee(Person):
        salary = String()

    assert Employee.fields["salary"] == String()

    # Test that it handles conflicting field names
    class Peer(Person):
        name = String()

    assert Peer.fields["name"] == String()

    # Test that it handles overriden fields
    class Employee(Person):
        name = String(required=False)

    assert Employee.fields["name"] == String(required=False)


# Generated at 2022-06-14 14:42:56.176964
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    assert Schema({"a": 1, "b": 2}) == Schema({"a": 1, "b": 2})
    assert Schema({"a": 1, "b": 2}) == Schema({"a": 1, "b": 2, "c": 3})
    assert Schema({"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert Schema({"a": 1, "b": 2}) != Schema({"a": 1})
    assert Schema({"a": 1, "b": 2}) != {"a": 1}
    assert Schema({"a": 1, "b": 2}) != Schema({"a": 1, "b": 2, "c": 3})

# Generated at 2022-06-14 14:43:30.413662
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
   obj = Schema()
   str = obj.__repr__()
   assert str == "Schema()"
   print("SUCCESS: test_Schema___repr__")



# Generated at 2022-06-14 14:43:31.826592
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    s = Schema({})
    assert len(s) == 0



# Generated at 2022-06-14 14:43:42.629285
# Unit test for constructor of class Schema
def test_Schema():
    class Foo(Schema):
        alpha = Field(type="number")

    assert Foo({"alpha": 1.23}) == Foo(alpha=1.23)

    # Use keyword arguments
    assert Foo(alpha=1.23) == Foo(alpha=1.23)

    # Use named arguments
    assert Foo(alpha=1.23) == Foo(alpha=1.23)

    # Test validation
    try:
        Foo({"alpha": "bar"})
        assert False
    except ValidationError:
        pass

    try:
        Foo({"alpha": "bar"}, strict=True)
        assert False
    except ValidationError:
        pass

    try:
        Foo({"alpha": "bar"}, strict=False)
        assert False
    except ValidationError:
        pass


# Generated at 2022-06-14 14:43:46.582895
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Boolean, Integer, String

    class Example(Schema):
        foo = String()
        bar = Integer()
        baz = Boolean()

    instance = Example(foo="foo", bar=1, baz=True)
    repr(instance) == "Example(foo='foo', bar=1, baz=True)"

# Generated at 2022-06-14 14:43:54.577834
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import String
    import copy
    import typesystem

    class AuthorSchema(Schema):
        name = String()

        @classmethod
        def validate(cls, value, **kwargs):
            return cls._validate_author_schema(value, **kwargs)

        @staticmethod
        def _validate_author_schema(value, **kwargs):
            validator = cls.make_validator(strict=strict)
            value = validator.validate(value, strict=strict)
            return cls(value, **kwargs)

    AuthorSchema()

    # If not in strict mode, we allow additional fields on the dictionary.
    # This isn't limited to just top-level fields on the schema.

# Generated at 2022-06-14 14:44:02.321306
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    some_fields = dict(key1=Field(), key2=Field())
    class SomeSchema(Schema, metaclass=SchemaMetaclass, fields=some_fields):
        pass

    # Create an object of the new class with one attribute
    schema1 = SomeSchema(key1=1)
    assert len(schema1) == 1
    assert list(schema1) == ['key1']

    # Create an object of the new class with two attributes
    schema2 = SomeSchema(key1=1, key2=2)
    assert len(schema2) == 2
    assert list(schema2) == ['key1', 'key2']


# Generated at 2022-06-14 14:44:11.374301
# Unit test for constructor of class Schema
def test_Schema():
    class A(Schema):
        pass
    assert A() == A()
    assert A() is not A()
    assert not A() != A()
    assert not (A() == 1)
    assert not (A() != 1)
    assert A() != 1
    assert A() is not 1
    assert [1, 2] != A()
    assert [1, 2] is not A()

    class B(Schema):
        field = Field(required=True)
    try:
        B()
    except TypeError as e:
        assert str(e) == "'field' is a required argument for B()."
    else:
        assert False

    class C(Schema):
        field = Field(required=True)
    assert C(field="value") == C(field="value")