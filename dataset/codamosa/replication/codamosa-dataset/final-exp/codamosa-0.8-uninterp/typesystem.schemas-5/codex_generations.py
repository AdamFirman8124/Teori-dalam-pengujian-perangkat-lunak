

# Generated at 2022-06-14 14:34:55.115128
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typing import Any, Callable, Dict, List, Optional, Tuple, Union, overload
    from typesystem import Schema, String, Reference
    definitions = SchemaDefinitions()
    class ChildSchema(Schema, metaclass=SchemaMetaclass):
        fields = {
            # Keyword arguments
            "name": String(),
            # Default argument
            "url": String(default=lambda: "http://example.com"),
            # String reference
            "ref": Reference("ChildSchema", definitions=definitions),
        }
    definitions.setdefault("ChildSchema", ChildSchema)
    obj = ChildSchema(
        name="Bob",
        url="http://thorgate.eu",
        ref=ChildSchema(name="Bob"),
    )
    assert obj.name == "Bob"

# Generated at 2022-06-14 14:35:03.208285
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class A(Schema):
        a = Field()

    class B(A):
        b = Field()

    class C(Schema):
        x = Field()
        a = Reference(to=A)

    a = A(a=1)
    b = B(b=2)
    c = C(a=a, x=3)
    assert len(list(c.__iter__())) == 2
    assert len(list(a.__iter__())) == 1
    assert len(list(b.__iter__())) == 2


# Generated at 2022-06-14 14:35:09.760710
# Unit test for constructor of class Reference
def test_Reference():
    target = Schema.make_validator()
    reference = Reference(to=target)
    assert reference.to == target
    assert reference.target_string == target.__name__

    definitions = SchemaDefinitions()
    assert definitions.setdefault(target.__name__, target) == target

    reference = Reference(to=target.__name__, definitions=definitions)
    assert reference.target == target

    reference.validate(target.validate({}))

# Generated at 2022-06-14 14:35:19.092827
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from .data_objects import Animal, City, Planets, Planet

    definitions = SchemaDefinitions()
    animal_schema = Animal(definitions=definitions)
    city_schema = City(definitions=definitions)
    planets_schema = Planets(definitions=definitions)
    planet_schema = Planet(definitions=definitions)

    assert "Animal" in definitions
    assert "City" in definitions
    assert "Planets" in definitions
    assert "Planet" in definitions

    assert "Animal" == animal_schema.__name__
    assert "City" == city_schema.__name__
    assert "Planets" == planets_schema.__name__
    assert "Planet" == planet_schema.__name__

# Generated at 2022-06-14 14:35:21.445795
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():

    class Schema1(Schema):
        name = String()
    assert Schema1(name='a') == Schema1(name='a')


# Generated at 2022-06-14 14:35:26.110839
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Point(Schema):
        x = Field(type="number")
        y = Field(type="number")
    p = Point(x=1,y=2)
    p_iter = iter(p)
    assert dict(p_iter) == {"x": 1, "y": 2}


# Generated at 2022-06-14 14:35:34.049907
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    print("\nTesting __len__()")
    class UserSchema(Schema):
        id = String()
        username = String()
        email = String()

    user = UserSchema(id="123", username="Alex", email="alex@foobar.com")
    assert len(user) == 3

    user = UserSchema(id="123", username="Alex")
    assert len(user) == 2

    user = UserSchema(id="123")
    assert len(user) == 1
    print("len() checks successful for method __len__ of class Schema")


# Generated at 2022-06-14 14:35:36.530497
# Unit test for method validate of class Reference
def test_Reference_validate():
    class MySchema(Schema):
        field = Reference(to=String)
    value = {"field": "test"}
    assert MySchema.validate(value)

# Generated at 2022-06-14 14:35:38.931306
# Unit test for constructor of class Schema
def test_Schema():
    new_Schema = Schema()
    assert (new_Schema != None)
    assert (isinstance(new_Schema, Schema))


# Generated at 2022-06-14 14:35:46.088393
# Unit test for function set_definitions
def test_set_definitions():
    # Test Reference
    foo = Reference("Foo")
    assert not hasattr(foo, '_target')
    foo.definitions = SchemaDefinitions({'Foo': Field()})
    set_definitions(foo, foo.definitions)
    assert hasattr(foo, '_target')

    # Test Array
    foo = Reference("Foo")
    bar = Array(items=foo)
    assert not hasattr(foo, '_target')
    assert bar.items is foo
    foo.definitions = SchemaDefinitions({'Foo': Field()})
    set_definitions(bar, foo.definitions)
    assert hasattr(foo, '_target')

    # Test Nested Array
    foo = Reference("Foo")
    foo.definitions = SchemaDefinitions({'Foo': Field()})
    bar

# Generated at 2022-06-14 14:36:08.907437
# Unit test for method validate of class Reference
def test_Reference_validate():
    definitions = SchemaDefinitions()
    class User(Schema, definitions=definitions):
        uid = String()
        first_name = String(required=False)
        last_name = String(required=False)

    class Task(Schema, definitions=definitions):
        uid = String()
        user = Reference(to=User)
        title = String()

    task = Task.validate(
        {
            "uid": "123",
            "user": {
                "uid": "876",
                "first_name": "John",
                "last_name": "Doe"
            },
            "title": "Do this"
        },
        strict=True
    )

# Generated at 2022-06-14 14:36:12.092941
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        id = Field(type="integer")
        name = Field(type="string")
    mySchema = MySchema(id=1, name="alice")
    assert isinstance(mySchema,Schema)


# Generated at 2022-06-14 14:36:19.038328
# Unit test for function set_definitions
def test_set_definitions():
    class Definition(Schema):
        a = Field(String)
        b = Field(String)
        c = Field(String)

    class ReferenceObject(Schema):
        a = Reference("Definition")
        b = Field(Reference("Definition"))
        c = Array(Reference("Definition"))
        d = Array(String)

    definitions = SchemaDefinitions()
    set_definitions(ReferenceObject, definitions)

    assert ReferenceObject.a.target is Definition
    assert ReferenceObject.b.target is Definition
    assert ReferenceObject.c.items.target is Definition
    assert ReferenceObject.d.items.target is String

# Generated at 2022-06-14 14:36:28.762184
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    class Pet(Schema):
        name = Field(str)
    class Person(Schema):
        name = Field(str)
        age = Field(int, default=100)
        pets = Array(Reference("Pet"), default=())
    class Root(Schema):
        person = Reference("Person", definitions=definitions)
    set_definitions(Root.fields["person"], definitions)
    assert Root.fields["person"].definitions is definitions
    assert isinstance(Root.fields["person"], Reference)
    assert isinstance(Root.fields["person"].items, Reference)

# Unit tests for class Reference

# Generated at 2022-06-14 14:36:33.299603
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Integer, String
    from typesystem.schema.schema import Schema

    class TestSchema(Schema):
        name = String(required=True)
        age = Integer(required=False)

    t = TestSchema(name="Justin", age=5)
    assert repr(t) == "TestSchema(name='Justin', age=5)"

    t = TestSchema(name="Justin")
    assert repr(t) == "TestSchema(name='Justin') [sparse]"

    t = TestSchema(name="Justin")
    assert repr(t) == "TestSchema(name='Justin') [sparse]"

# Generated at 2022-06-14 14:36:42.640424
# Unit test for constructor of class Schema
def test_Schema():
    # Schema(*args, **kwargs)
    class User(Schema):
        name = Field(str)
        age = Field(int, default=0)

    user = User(name="George", age=24)
    assert user == User(name="George", age=24)

    user = User({"name": "George", "age": 24})
    assert user == User(name="George", age=24)

    user = User(object())
    assert user == User()

    user = User({"name": "George", "age": 24}, age=23)
    assert user == User(name="George", age=24)

    user = User(age=23, name="George")
    assert user == User(name="George", age=23)

    # Error cases

# Generated at 2022-06-14 14:36:52.891276
# Unit test for method __len__ of class Schema

# Generated at 2022-06-14 14:37:01.419294
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem import Integer, String


    class Person(Schema):
        name = String()
        age = Integer()

    class Employee(Schema):
        person = Reference(Person)
        salary = Integer()


    class Manager(Schema):
        employee = Reference(Employee)
        emplyees = Reference(Employee, many=True)

    target = Person(name="Peter", age=22)
    employee = Employee(person=target, salary=3000)
    manager = Manager(employee=employee, emplyees=[employee])

    assert manager.employee == employee
    assert manager.emplyees == [employee]

# Generated at 2022-06-14 14:37:07.965074
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Foo(Schema):
        a = Field()
        b = Field()
        c = Field()

    instance = Foo()
    assert list(instance) == []

    instance = Foo({"a": 1})
    assert list(instance) == ["a"]

    instance = Foo({"a": 1, "b": 2})
    assert list(instance) == ["a", "b"]

    instance = Foo({"a": 1, "b": 2, "c": 3})
    assert list(instance) == ["a", "b", "c"]


# Generated at 2022-06-14 14:37:18.372862
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from unittest.mock import patch
    from dataclasses import dataclass
    from typesystem.types import String
    @dataclass
    class MySchema(Schema):
        field1: String = "A"
        field2: String = "B"
        def __iter__(self):
            with patch("typesystem.schema.Schema.__iter__") as _M_Schema___iter__:
                ret_value = _M_Schema___iter__.return_value
                yield from ret_value
    schema = MySchema()
    ret_value = schema.__iter__()
    assert ret_value is schema.__iter__.return_value

# Generated at 2022-06-14 14:37:26.358273
# Unit test for constructor of class Schema
def test_Schema():
    class G(Schema):
        x = Field()

    g = G({"x": 42})
    assert g.x == 42


# Generated at 2022-06-14 14:37:33.588375
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    print ("test_Schema___eq__()")
    class MyClass(Schema):
        num_required = Integer(minimum=10)
        num_optional = Integer(minimum=10, default=0)

    obj1 = MyClass({"num_required":10, "num_optional":0})
    obj2 = MyClass({"num_required":10, "num_optional":0})
    assert (obj1 == obj2) == True
    obj3 = MyClass({"num_required":10, "num_optional":1})
    assert (obj1 == obj3) == False

if __name__ == "__main__":
    test_Schema___eq__()

# Generated at 2022-06-14 14:37:44.961956
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import unittest

    # self = Schema()
    class_name = self.__class__.__name__
    arguments = {
        key: getattr(self, key) for key in self.fields.keys() if hasattr(self, key)
    }
    argument_str = ", ".join(
        [f"{key}={value!r}" for key, value in arguments.items()]
    )
    sparse_indicator = " [sparse]" if self.is_sparse else ""
    # return f"{class_name}({argument_str}){sparse_indicator}"
    assert repr(self) == f"{class_name}({argument_str}){sparse_indicator}"

# Generated at 2022-06-14 14:37:49.561424
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Jane", age=25)
    assert repr(person) == "Person(name='Jane', age=25)"



# Generated at 2022-06-14 14:37:51.368663
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    pass
    # TODO: Document, test, and resolve issue #140


# Generated at 2022-06-14 14:37:56.082191
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class TestSchema(Schema):
        a = 1
        b = 2.0
        c = 3j
        d = "Test"

    assert list(TestSchema(a=1, d='Test')) == ['a', 'd']



# Generated at 2022-06-14 14:38:03.302774
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import Integer, String

    class User(Schema):
        name = String
        age = Integer

    user = User(name="Dave", age=25)
    assert list(user) == ["name", "age"]

    d = {"name": "Dave", "age": 25}
    user = User(d)
    assert list(user) == ["name", "age"]


# Generated at 2022-06-14 14:38:11.478120
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Create a mock class object as the return value of __iter__
    class mock_iter():
        def __init__(self):
            self.value = iter(["value1", "value2"])
        
        def __iter__(self):
            return self
        
        def __next__(self):
            return next(self.value)
            
    # Create a mock class object
    class mock_Schema():
        def __init__(self):
            self.fields = mock_iter()
    
    # Test the return of __iter__()
    mock_obj = mock_Schema()
    out=Schema.__iter__(mock_obj)
    assert isinstance(out, mock_iter)



# Generated at 2022-06-14 14:38:13.921283
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    schema = Schema()
    assert schema == schema
    assert not (schema != schema)


# Generated at 2022-06-14 14:38:24.623419
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import Boolean, Integer, String, Float

    class MovieSchema(Schema):
        name = String(min_length=1)
        year = Integer(minimum=1900)
        rating = Float(minimum=0, maximum=10)
        oscar_win = Boolean()

    assert MovieSchema.fields == {"name": String(min_length=1),
                                  "year": Integer(minimum=1900),
                                  "rating": Float(minimum=0, maximum=10),
                                  "oscar_win": Boolean()}

    class TreatedMovieSchema(MovieSchema):
        treated = Boolean()


# Generated at 2022-06-14 14:38:35.741597
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import pytest
    from .utils import is_equal

    class A(Schema):
        a = Field()

    with pytest.raises(TypeError) as error_a:
        A()
    is_equal(error_a, "Argument a is required.")

    assert len(A(a=1)) == 1



# Generated at 2022-06-14 14:38:37.977604
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert isinstance(Schema().__getitem__, collections.abc.Callable)
    # TODO
    assert False # TODO: implement your test here


# Generated at 2022-06-14 14:38:42.159049
# Unit test for constructor of class Schema
def test_Schema():
    assert Schema()
    assert Schema({"a": 1, "b": "string"})
    assert Schema(Schema())
    try:
        Schema("a")
    except Exception:
        assert True
    try:
        Schema(1)
    except Exception:
        assert True
    try:
        Schema(1.1)
    except Exception:
        assert True


# Generated at 2022-06-14 14:38:48.386827
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():

    import typesystem

    def validate_test_SchemaMetaclass___new__(value):
        try:
            return value
        except Exception as e:
            return (
                'Error: test_SchemaMetaclass___new__("{0}") threw "{1}"'.format(
                    value, e
                )
            )


# Generated at 2022-06-14 14:38:50.892872
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        age = Field()

    person = Person({"age": 10})
    assert person.age == 10



# Generated at 2022-06-14 14:38:55.729874
# Unit test for constructor of class Schema
def test_Schema():
    class ArrayOf(Schema):
        items = Array(String())

    try:
        ArrayOf(['a', 'b'])
    except Exception as e:
        assert type(e) == TypeError
        assert str(e) == "ArrayOf() takes no arguments"


# Generated at 2022-06-14 14:39:00.381093
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Schema, String
    class Person(Schema):
        name = String(max_length=50)
    assert len(Person(name="John")) == 1
    assert len(Person(name="John", height=175)) == 2
    assert len(Person()) == 0



# Generated at 2022-06-14 14:39:07.566266
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Setup
    name = "TestSchema"
    attrs = {"fields": {}}
    class_ = SchemaMetaclass.__new__(SchemaMetaclass, name, (), attrs)
    schema = SchemaMetaclass.__call__(class_)
    # Exercise
    iter_ = schema.__iter__()
    # Verify
    assert iter_ is not None
    assert list(iter_) == []



# Generated at 2022-06-14 14:39:10.655629
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Integer, String

    class User(Schema):
        id = Integer()
        username = String()

    user = User(id=1, username="leela")
    s = repr(user)
    assert s == "User(id=1, username='leela')"



# Generated at 2022-06-14 14:39:22.921029
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from serializable import Serializable
    from serializable import fields
    from serializable.exceptions import SerializationError

    class Post(Serializable):
        slug = fields.String()
        title = fields.String(default="No title")
        text = fields.String(default="No text")
        tags = fields.Array(fields.String)

    post = Post(slug="hello", title="Hello world")
    assert repr(post) == "Post(slug='hello', title='Hello world', text='No text')"
    assert post.is_sparse
    assert dict(post) == dict(
        slug="hello", title="Hello world", text="No text", tags=[]
    )

    post.tags = ["spam", "eggs"]

# Generated at 2022-06-14 14:39:39.153488
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # test 'person'
    person = Schema(name = 'John Doe', age = 27, gender = 'M')
    assert person['name'] == 'John Doe'
    assert person['age'] == 27
    assert person['gender'] == 'M'
    assert person['nonexistent-key'] == None
    assert person['nonexistent-key'] == None


# Generated at 2022-06-14 14:39:51.103429
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from .fields import String, Number
    from .utils import as_dict

    class TestSchema(Schema):
        foo = String(min_length=2)
        bar = Number(max_value=42)

    schema = TestSchema(foo="hello", bar=21)
    assert as_dict(schema) == {"foo": "hello", "bar": 21}
    assert as_dict(schema, include=["foo"]) == {"foo": "hello"}
    assert as_dict(schema, exclude=["foo"]) == {"bar": 21}
    assert as_dict(schema, include=["foo"], exclude=["bar"]) == {"foo": "hello"}
    assert as_dict(schema, include=["bar", "foo"]) == {"foo": "hello", "bar": 21}

# Generated at 2022-06-14 14:39:54.689258
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Integer, String

    class Person(Schema):
        age = Integer()
        name = String()

    person = Person(age=10, name="John")
    assert len(person) == 2

# Generated at 2022-06-14 14:40:02.043407
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class SimpleSchema(Schema):
        id = Field(type='integer')
        name = Field(type='string')
    ss = SimpleSchema({'id': 102, 'name': 'test'})
    assert ss.__getitem__('id') == 102
    assert ss.__getitem__('name') == 'test'
    try:
        ss.__getitem__('id2')
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:40:06.956069
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from . import TestSchema1
    data = TestSchema1.validate({"name": "foo", "age": 12})
    assert len(data) == 2
    data = TestSchema1.validate({"name": "foo"})
    assert len(data) == 1


# Generated at 2022-06-14 14:40:08.534062
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
  schema = Schema()
  assert list(schema) == []


# Generated at 2022-06-14 14:40:14.731661
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import typing
    import dataclasses

    from typesystem.base.meta import PRIVATE
    from typesystem.exceptions import ValidationError
    from typesystem.fields import Array, Boolean, Integer, Object
    from typesystem.schema import Schema, SchemaDefinitions

    @dataclasses.dataclass
    class Person(Schema):
        name: str
        age: int

    @dataclasses.dataclass
    class PersonSchema(Schema):
        _private: typing.Tuple[str] = PRIVATE
        people: Array[Person]

    definitions = SchemaDefinitions()
    PersonSchema(people=[Person(name="Paul", age=29)], definitions=definitions)

# Generated at 2022-06-14 14:40:16.080944
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():  # regression test for bug #183
    class Data(Schema):
        pass

    assert Data() == Data()

# Generated at 2022-06-14 14:40:28.498391
# Unit test for constructor of class Schema
def test_Schema():
    A = Schema
    B = Schema

    # A < B
    assert A.__bases__ == (B,)
    assert isinstance(A(), B)
    assert issubclass(A, B)

    # A > B
    assert B.__bases__ == (A,)
    assert isinstance(B(), A)
    assert issubclass(B, A)

    # A == B
    assert A.__bases__ == B.__bases__ == ()
    assert isinstance(A(), A)
    assert isinstance(B(), B)
    assert issubclass(A, A)
    assert issubclass(B, B)

    # A is B
    assert A() is B()
    assert type(A()) is type(B())

    # A is not B
    assert A() is not B()

# Generated at 2022-06-14 14:40:34.395549
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Integer
    class Point(Schema):
        x = Integer()
        y = Integer()
        z = Integer()

    point1 = Point(x=1, y=2)
    assert str(point1) == "Point(x=1, y=2) [sparse]"
    point2 = Point(x=1, y=2, z=3)
    assert str(point2) == "Point(x=1, y=2, z=3)"

# Generated at 2022-06-14 14:40:52.821270
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import typesystem
    class User(typesystem.Schema):
        username = typesystem.String(max_length=255)
        password = typesystem.String(max_length=255)

    user = User(username='John', password='pass123')
    assert repr(user) == "User(username='John', password='pass123')"

# Generated at 2022-06-14 14:41:05.101626
# Unit test for constructor of class Schema
def test_Schema():
    class SubSchema(Schema):
        foo = Field()

    SubSchema.validate({"foo": "bar"}, strict=True)
    try:
        SubSchema.validate({"bar": "foo"}, strict=True)
        assert False, "should have raised an error for unexpected key in the object"
    except ValidationError:
        pass

    try:
        SubSchema.validate(["foo", "bar"], strict=True)
        assert False, "should have raised an error for an array"
    except TypeError:
        pass

    SubSchema2 = type("SubSchema2", (Schema,), {"foo": Field()})
    SubSchema2.validate({"foo": "bar"})


# Generated at 2022-06-14 14:41:06.368892
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    introspect(SchemaMetaclass)


# Generated at 2022-06-14 14:41:11.497975
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    person = Person(name="Foo", age=20)
    person_foo = Person(name="Foo", age=20)
    
    assert person == person_foo

# Generated at 2022-06-14 14:41:21.136518
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    #Test Schema
    class MySchema(Schema):
        a = str
        b = int
        c = str
    a = MySchema.validate({"a": "a", "b": 1, "c": "c"})
    assert list(a) == ['a', 'b', 'c']
    b = MySchema.validate({"a": "a"})
    assert list(b) == ['a']
    c = MySchema.validate({"a": "a", "b": 1})
    assert list(c) == ['a', 'b']
    d = MySchema.validate({"a": "a", "b": 1, "c": "c"})
    assert list(d) == ['a', 'b', 'c']

# Generated at 2022-06-14 14:41:23.867899
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert (
        "name" in Person()  and "name" in Person(name="Doe") and "id" in Person(id=10) 
    )
    

# Generated at 2022-06-14 14:41:32.735473
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from datetime import date

    class Account(Schema):
        username = String(max_length=30)
        email = String()
        website = String(required=False)
        joined = Date()
        balance = Float()
        is_staff = Boolean(default=False)

    account = Account(
        username="Testing",
        email="testing@example.com",
        joined=date(2002, 12, 25),
        balance=100.00,
    )

    assert repr(account) == (
        "Account(username='Testing', email='testing@example.com', "
        "joined=datetime.date(2002, 12, 25), balance=100.0, is_staff=False)"
    )


# Generated at 2022-06-14 14:41:44.393442
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        age = Int(minimum=0)
        name = String()

    # Test that the constructor works without any arguments.
    person = Person()
    assert isinstance(person, Person)
    assert isinstance(person, Mapping)

    # Test that the constructor works with a dictionary argument.
    person = Person({"age": 1, "name": "David"})
    assert isinstance(person, Person)
    assert isinstance(person, Mapping)
    assert person == {"age": 1, "name": "David"}

    # Test that the constructor works with a class argument.
    person = Person(Person({"age": 1, "name": "David"}))
    assert isinstance(person, Person)
    assert isinstance(person, Mapping)

# Generated at 2022-06-14 14:41:56.461151
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class TestSchema(Schema):
        age = Integer(description="age")
        name = String(description="name")

    schema1 = TestSchema(age=10, name="test")
    assert schema1 == TestSchema({"age": 10, "name": "test"})
    assert schema1 == TestSchema({"age": 10, "name": "test", "test": True}, test=False)

if __name__ == "__main__":
    # Unit test for class Schema
    test_SchemaMetaclass___new__()
    # Unit test for method make_validator of class Schema
    validator = TestSchema.make_validator()
    value1 = validator.validate({"age": 10, "name": "test"})

# Generated at 2022-06-14 14:42:06.311511
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class User(Schema):
        id = Field(type="string", required=True)
        email = Field(type="string", required=True)
        first_name = Field(type="string", required=True)
        last_name = Field(type="string", required=True)
        active = Field(type="boolean")
        admin = Field(type="boolean")

    value = {
        "id": "123",
        "email": "test@test.test",
        "first_name": "test",
        "last_name": "test",
        "active": True,
        "admin": False,
    }
    user = User(value)


# Generated at 2022-06-14 14:42:37.546961
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import Integer, String
    class A(Schema):
        # fieldname: Integer
        a = Integer(minimum = 1, maximum = 100)
        # fieldname: String
        b = String(min_length = 2, max_length = 10)
    assert 'a' in A.fields
    assert 'b' in A.fields


# Generated at 2022-06-14 14:42:44.223432
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String, Integer


    class Point(Schema):
        x = Integer(minimum=0)
        y = Integer(minimum=0)


    point = Point(x=1, y=2)
    assert 'x' in point
    assert 'y' in point
    assert 'z' not in point
    assert len(point) == 2
    assert list(point) == ['x', 'y']


# Generated at 2022-06-14 14:42:49.503665
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class A(Schema):
        field1 = Field(default="default1")
        field2 = Field()

    assert repr(A()) == "A(field1='default1') [sparse]"
    assert repr(A(field2="value2")) == "A(field1='default1', field2='value2')"

# Generated at 2022-06-14 14:42:55.203513
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import Text
    from typesystem.types import SchemaMetaclass

    class Schema(Mapping, metaclass=SchemaMetaclass):
        field0 = Text()
        field1 = Text()

    x = Schema()
    x.field1 = 'bar'
    assert [key for key in x.keys()] == ['field1']
    assert [key for key in x.__iter__()] == ['field1']


# Generated at 2022-06-14 14:42:59.231926
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    expected_repr = '<class \'tests.test_schema.TestSchema\'>(field_1=1)'
    assert TestSchema(field_1=1).__repr__() == expected_repr


# Generated at 2022-06-14 14:43:02.564256
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        name = String(max_length=10)
        age = Integer(minimum=0, maximum=150)
    p = Person(name="Joe", age=28)
    assert len(p) == 2


# Generated at 2022-06-14 14:43:07.764434
# Unit test for method validate of class Reference
def test_Reference_validate():
    class mySchema(Schema):
        name = Field(type=str)
        age = Field(type=int)

    m = mySchema(name="Wilfred", age=36)
    assert m.target == mySchema
    assert m.target_string == 'mySchema'
    assert m.validate(m) == m

# Generated at 2022-06-14 14:43:12.407566
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert list(S1()) == ['a'] 
    assert list(S3()) == ['a', 'b', 'c']
    assert list(S5()) == ['a', 'b', 'c', 'd', 'e']
    assert list(S6()) == ['a', 'b', 'c', 'd']


# Generated at 2022-06-14 14:43:16.577843
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    field = Field()
    class TestSchema(Schema):
        field = field
    obj = TestSchema(field="value")
    assert len(obj) == 1


# Generated at 2022-06-14 14:43:24.979891
# Unit test for method validate of class Reference
def test_Reference_validate():
    from . import user
    class Age(Field):
        pass
    class User(Schema):
        name = Field(str)
        age = Age(int)
    definitions = SchemaDefinitions()
    definitions['User'] = User
    user_json = {
        "name": "Alice",
        "age": 20
    }
    # Valid user
    user_valid = User(user_json)
    user_reference = Reference(to = "User", definitions = definitions)
    assert user_valid == user_reference.validate(user_json)
    # Invalid user
    user_valid = User(user_json)
    user_json_invalid = {
        "name": 20,
        "age": "20"
    }