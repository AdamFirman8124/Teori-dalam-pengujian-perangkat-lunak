

# Generated at 2022-06-14 14:34:46.464404
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        first_name = String(max_length=20, blank=False)
        last_name = String(max_length=20, blank=False)
        age = Integer()
        height_in_cm = Number()
        is_male = Boolean()

    person_1 = Person(
        first_name="John", last_name="Doe", age=25, height_in_cm=175, is_male=True
    )
    person_2 = Person(first_name="John", last_name="Doe", age=25, height_in_cm=175)
    person_3 = Person(
        first_name="John", last_name="Doe", age=25, is_male=True
    )  # missing height_in_cm


# Generated at 2022-06-14 14:34:56.629542
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Schema, String

    # Check that a schema prints its fields and their values
    class Example(Schema):
        foo = String()
        bar = String()
    value = Example(foo="foo_value", bar="bar_value")
    assert repr(value) == "Example(foo='foo_value', bar='bar_value')"

    # Check that a schema only prints fields that are set
    class Example(Schema):
        foo = String()
        bar = String()
    value = Example(foo="foo_value")
    assert repr(value) == "Example(foo='foo_value') [sparse]"

    # Check that a schema only prints fields that are set
    class Example(Schema):
        foo = String()
        bar = String()
    value = Example()

# Generated at 2022-06-14 14:35:08.838158
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Response(Schema):
        id = Integer()
        name = String()
    x = Response({'id': 0, 'name': 'mango'})
    y = Response({'id': 0, 'name': 'mango'})
    # test case 1
    assert x == y
    # test case 2
    y.id = 100
    assert x != y
    # test case 3
    x.id = 100
    y.id = 100
    y.name = 'apple'
    assert x != y
    # test case 4
    x.name = 'apple'
    assert x == y
    # test case 5
    x = Response(None)
    y = Response(None)
    assert x == y
    # test case 6
    x = Response({'id': 0})

# Generated at 2022-06-14 14:35:16.126520
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field = Reference("A")
    assert field.definitions is None
    set_definitions(field, definitions)
    assert field.definitions == definitions

    field = Array(items=Reference("A"))
    assert field.items.definitions is None
    set_definitions(field, definitions)
    assert field.items.definitions == definitions

    field = Object(properties={"a": Reference("A")})
    assert field.properties["a"].definitions is None
    set_definitions(field, definitions)
    assert field.properties["a"].definitions == definitions



# Generated at 2022-06-14 14:35:24.132877
# Unit test for function set_definitions
def test_set_definitions():
    class SimpleSchema(Schema):
        class UserSchema(Schema):
            username = Reference("username")
            email = Reference("email")

        user = Reference(UserSchema)
        username = Field(str)
        email = Field(str)

    definitions = SchemaDefinitions()

    for key, field in SimpleSchema.fields.items():
        set_definitions(field, definitions)

    assert definitions["username"] == SimpleSchema.username
    assert definitions["email"] == SimpleSchema.email
    assert definitions["UserSchema"].username == SimpleSchema.UserSchema.username
    assert definitions["UserSchema"].email == SimpleSchema.UserSchema.email
    assert definitions["user"].username == SimpleSchema.UserSchema.username
    assert definitions["user"].email == SimpleSchema.UserSche

# Generated at 2022-06-14 14:35:35.422330
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import String

    class Person(Schema):
        first_name = String()
        last_name = String()
        age = String(default=None)

    p = Person(first_name="Bob", last_name="Doe")
    assert repr(p) == "Person(first_name='Bob', last_name='Doe') [sparse]"
    assert p.to_primitive() == {"first_name": "Bob", "last_name": "Doe"}

    p = Person(first_name="Bob", last_name="Doe", age="35")
    assert repr(p) == "Person(first_name='Bob', last_name='Doe', age='35')"

# Generated at 2022-06-14 14:35:41.441115
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Sample(Schema):
        a = Field(int)
        b = Field(str)
        c = Field(int, default=10)
        d = Field(str, default='sample')
        
    assert list(Sample(a=1, b='a', c=11, d='instance')) == ['a', 'b', 'c', 'd']
    assert list(Sample(a=1, b='a')) == ['a', 'b']
    assert list(Sample()) == ['c', 'd']


# Generated at 2022-06-14 14:35:44.930868
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import json

    class Person(Schema):
        name = String()
        age = Integer()

    person = Person(name="Guido", age=64)

    result = json.dumps(person, indent=2)
    assert result == """{
  "name": "Guido",
  "age": 64
}"""


# Generated at 2022-06-14 14:35:46.966472
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():

    class A(Schema):
        x = Field(name="x")
        y = Field(name="y")

    assert A(x=1, y=2) == A(x=1, y=2)


# Generated at 2022-06-14 14:35:50.883455
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Schema(object):
        _fields = {"a": "a"}

        def __getitem__(self, key):
            return self._fields[key]
    obj = Schema()
    assert obj["a"] == "a"


# Generated at 2022-06-14 14:36:12.258485
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String(max_length=10)
        employer = String()
        phone = String(pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}")

    john = Person(name="John Doe", employer="Acme Corp", phone="123-456-7890")
    assert john.name == "John Doe"
    assert john.employer == "Acme Corp"
    assert john.phone == "123-456-7890"


# Generated at 2022-06-14 14:36:14.398504
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    result = Schema.__eq__(self,other)
    assert result == False
    

# Generated at 2022-06-14 14:36:19.067075
# Unit test for function set_definitions
def test_set_definitions():
    """
    Test the set_definitions function.
    """
    definitions = SchemaDefinitions({"test": Object(properties={"test": String()})})
    schema = Object(properties={"test": Reference("test")})
    set_definitions(schema, definitions)
    assert isinstance(schema.properties["test"], Reference)
    assert isinstance(schema.properties["test"].target, Object)
    print(schema)

# Generated at 2022-06-14 14:36:25.547636
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Simple(object):
        pass
        
    class SimpleSchema(Schema):
        name = String()
        age = Integer()
        is_active = Boolean()
        
    assert SimpleSchema.fields == {'name': String(), 'age': Integer(), 'is_active': Boolean()}
    assert SimpleSchema.__module__ == __name__


# Generated at 2022-06-14 14:36:35.692675
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    
    # -- test 1
    from jsonclasses import jsonclass, JSONObject, types
    from jsonclasses.compat import str
    from jsonclasses.exceptions import ValidationError
    from typesystem.fields import Array, Field, Integer, Object, String
    from typesystem.validators import Between, Length
    from typing import Any, Dict, List, Optional, Tuple, Union
    from unittest.mock import MagicMock, patch

    
    
    
    
    
    
    
    
    
    
    # -- test 2
    from jsonclasses import jsonclass, JSONObject, types
    from jsonclasses.compat import str
    from jsonclasses.exceptions import ValidationError
    from typesystem.fields import Array, Field, Integer, Object, String
    from typesystem.validators import Between, Length

# Generated at 2022-06-14 14:36:44.270473
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import copy
    import io
    import sys
    
    capturedOutput = io.StringIO()          # Create StringIO object
    sys.stdout = capturedOutput             #  and redirect stdout.
    
    # Call the method to be tested
    testClass_1 = Schema()
    testClass_1.__iter__()
    
    sys.stdout = sys.__stdout__             # Reset redirect.
    assert capturedOutput.getvalue() == "{}\n" + "Iterable object created successfully\n"
    
    capturedOutput = io.StringIO()          # Create StringIO object
    sys.stdout = capturedOutput             #  and redirect stdout.
    
    # Call the method to be tested
    testClass_2 = Schema()
    for i in testClass_1:
        print(i)
    
    sys

# Generated at 2022-06-14 14:36:53.703698
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():

    from typesystem.base import Schema
    from typesystem import fields

    class Person(Schema):
        name = fields.String(required=True)
        age = fields.Integer(default=0)

    person = Person()
    assert repr(person) == "Person(name=None, age=0)"

    person = Person(name="Will")
    assert repr(person) == "Person(name='Will', age=0)"

    person = Person(name="Will", age=40)
    assert repr(person) == "Person(name='Will', age=40)"

    person = Person(name="Will", age=40, invalid=True)
    assert repr(person) == "Person(name='Will', age=40 [sparse])"

# Generated at 2022-06-14 14:36:58.726842
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Test input parameters
    parm_cls = Schema
    parm_other =  object()

    # Expected results
    exp_output = False

    # Execute function
    assert(parm_cls.__eq__(parm_other) == exp_output)


# Generated at 2022-06-14 14:37:07.201155
# Unit test for method validate of class Reference
def test_Reference_validate():
    class User(Schema):
        name = String()
        email = String()

    class Post(Schema):
        author = Reference(to=User)
        content = String()

    definitions = SchemaDefinitions()
    Post(author=User(name="George", email="foo@example.com"), content="hello", definitions=definitions)
    Post(author=User(name="George", email="foo@example.com"), content="hello") == Post(author=User(name="George", email="foo@example.com"), content="hello") == True
    Post(author=User(name="George", email="foo@example.com"), content="hello") == Post(author=User(name="George", email="foo@example.com"), content="hello", definitions=definitions) == True

# Generated at 2022-06-14 14:37:18.772501
# Unit test for constructor of class Schema
def test_Schema():
    class C(Schema):
        a = Field()
        b = Field()
        c = Field(required=True)
        d = Reference("D")

    assert C.fields == dict(
        a=Field(), b=Field(), c=Field(required=True), d=Reference("D")
    )
    assert C().a is None
    assert C().b is None
    assert C().c is None
    assert C().d is None
    assert C().is_sparse
    assert isinstance(C().a, Field) is False
    assert isinstance(C().b, Field) is False
    assert C(dict(a="a", b="b")).a == "a"
    assert C(dict(a="a", b="b")).b == "b"

# Generated at 2022-06-14 14:37:34.152572
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import String
    from unittest import TestCase
    from ddt import ddt, data

    @ddt
    class SchemaTests(TestCase):
        def test_constructor_with_no_args(self):
            class Person(Schema):
                name = String(default="Anonymous")
            person = Person()
            self.assertEqual(person.name, "Anonymous")
            self.assertRaises(AttributeError, lambda: person.age)


# Generated at 2022-06-14 14:37:43.394581
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer()
        height = fields.Integer()

    schema1 = TestSchema(name="Tom", age=15, height=170)
    assert repr(schema1) == "TestSchema(name='Tom', age=15, height=170)"

    schema2 = TestSchema(name="Tom", age=15)
    assert repr(schema2) == "TestSchema(name='Tom', age=15) [sparse]"

# Generated at 2022-06-14 14:37:55.932535
# Unit test for method validate of class Reference
def test_Reference_validate():
    class SchemaA(Schema):
        a = Field(type="string")
        b = Field(type="string")

    class SchemaB(Schema):
        a = Reference(to="SchemaA")
        b = Field(type="number")
        c = Field(type="string")
    schema_b = SchemaB.validate({"a": {"a": "2", "b": "2"}, "b": 2, "c": "a"})
    assert(schema_b.a.a == "2")
    assert(schema_b.a.b == "2")
    assert(schema_b.b == 2)
    assert(schema_b.c == "a")

    class SchemaC(Schema):
        a = Reference(to="SchemaA")

# Generated at 2022-06-14 14:38:07.788798
# Unit test for constructor of class Reference
def test_Reference():
    """
    Unit tests for constructor of class Reference
    """
    Schema = Reference('schema')
    assert Schema.target_string == 'schema'
    assert Schema.target is None
    # Assert TypeError
    try:
        Reference(None)
    except TypeError:
        assert True
    # Assert KeyError
    try:
        Reference('schema', definitions={})
    except KeyError:
        assert True
    def custom_validate(self, value):
        return value
    # Assert AttributeError
    try:
        Reference('schema', validate=custom_validate)
    except AttributeError:
        assert True
    # Assert AttributeError
    try:
        Reference('schema', validate_always=custom_validate)
    except AttributeError:
        assert True
   

# Generated at 2022-06-14 14:38:15.738338
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class DummyIfClass( Schema ):
        ID = Field(type="string", name="ID", required=True)
        CMD = Field(type="string", name="CMD", required=True)
        def __init__(self, ID, CMD,  *args, **kwargs):
            super().__init__(ID, CMD, *args, **kwargs)
    instance = DummyIfClass('1','2')
    assert repr(instance) == "DummyIfClass(CMD='2', ID='1')"

# Generated at 2022-06-14 14:38:20.426027
# Unit test for function set_definitions
def test_set_definitions():

    class User(Schema):
        id = Field(type="integer")

    class SchemaWithRef(Schema):
        reference = Reference(to=User)

    definitions = SchemaDefinitions()
    set_definitions(SchemaWithRef.fields["reference"], definitions)
    assert definitions["User"] is User

# Generated at 2022-06-14 14:38:21.772372
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    assert Schema(name = 'A sample', num = 5, str = 'A string')

# Generated at 2022-06-14 14:38:23.518190
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    s = Schema({"id": 1})
    l = len(s)
    assert l == 1

# Generated at 2022-06-14 14:38:29.310171
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from inspect import signature
    from typesystem.schema import Schema
    from typesystem.typing import *

    from inspect import signature
    from typesystem.schema import Schema
    from typesystem.typing import *

    schema = Schema(
        a=Integer(),
        b=Integer(),
        c=Integer(),
        d=Integer(),
    )
    assert len(signature(schema.__len__).parameters) == 0
    assert len(schema) == 4


# Generated at 2022-06-14 14:38:34.942775
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():

    class Album(Schema):
        name = String()
        year = Integer()
        songs = Array(
            items=String()
        )

    assert repr(Album(name="High Violet", year=2010, songs=["Terrible love"])) == "Album(name='High Violet', year=2010, songs=['Terrible love'])"


# Generated at 2022-06-14 14:38:58.245196
# Unit test for method validate of class Reference
def test_Reference_validate():

    class Person(Schema):
        name = String(max_length=255, required=True)
        age = Integer(min_value=0)

    class PersonReference(Reference):
        to = Person
    person = Person(name='Rafael Borges', age=36)
    print(person)

    person_reference = PersonReference(person)
    print(person_reference.validate(person))
    person_reference = PersonReference()
    print(person_reference.validate(person))
    person_reference.to = 'Person'
    print(person_reference.validate(person))
    person_reference = PersonReference(to='Person')
    print(person_reference.validate(person))
    #person_reference = PersonReference(to='Person2')
    #print(person_reference.validate(person))

   

# Generated at 2022-06-14 14:39:09.324921
# Unit test for function set_definitions
def test_set_definitions():
    class Author(Schema):
        name = Field()

    class Article(Schema):
        author = Reference("Author")

    # Make sure that we've correctly set `_target` on the `Reference` field.
    assert isinstance(Article.fields["author"].target, Field)
    # Make sure that this works with nested objects.
    definitions = SchemaDefinitions()
    class Article(Schema):
        author = Reference("Author")
        comments = Array(Reference("Comment"))

    class Comment(Schema):
        author = Reference("Author")

    set_definitions(Article, definitions)
    assert isinstance(Article.fields["comments"].items.target, Field)
    assert isinstance(Comment.fields["author"].target, Field)

# Generated at 2022-06-14 14:39:13.944948
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Coord(Schema):
        lat = Field(format="float")
        lng = Field(format="float")
    coord = Coord(lat = 1, lng = 2)
    assert repr(coord) == "Coord(lat=1, lng=2)"

# Generated at 2022-06-14 14:39:25.414518
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert True
    #from datetime import date
    #from pytz import timezone
    #from app.models.schema import Schema, Model, List, String, Integer, DateTime, Date, Time, Array, Object, Reference, ValidationError, ValidationResult
    #from typing import List
    #from app.models.schema import Schema, Model, List, String, Integer, DateTime, Date, Time, Array, Object, Reference, ValidationError, ValidationResult
    #from typing import List
    #from app.models.schema import Schema, Model, List, String, Integer, DateTime, Date, Time, Array, Object, Reference, ValidationError, ValidationResult
    #from typing import List
    #from app.models.schema import Schema, Model, List, String, Integer, DateTime, Date, Time, Array, Object

# Generated at 2022-06-14 14:39:29.981960
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Integer, String

    class Person(Schema):
        name = String(format="name_first", max_length=20)
        age = Integer()

    person1 = Person(name="John", age=20)
    assert person1 == Person({"name": "John", "age": 20})
    assert person1 == Person(name="John", age=20)
    assert person1 == Person(Person(name="John", age=20))

    with pytest.raises(TypeError, match="Unknown arguments"):
        Person(name="John", age=20, foo=42)

    with pytest.raises(TypeError, match="Invalid argument 'foo'. Is not defined"):
        Person({"name": "John", "age": 20, "foo": 42})


# Generated at 2022-06-14 14:39:33.425687
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        one = Field()
        two = Field()
        three = Field()
    assert len(TestSchema()) == 3
    assert len(TestSchema(one=1, three=3)) == 2

# Generated at 2022-06-14 14:39:37.124172
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
  class Person(Schema):
      name = String(max_length=100)
      age = Integer(min_value=0, max_value=150)


  person = Person({'name': 'John', 'age': 34})
  assert ['name', 'age'] == [key for key in person]



# Generated at 2022-06-14 14:39:49.630015
# Unit test for constructor of class Reference
def test_Reference():
    class RequiredFields(Schema):
        field1 = String(required=True)
        field2 = String(default="aaa")
        ref = Reference(
            to=RequiredFields,
            definitions={RequiredFields.__name__: RequiredFields},
            default=RequiredFields(field1="a", field2="b"),
        )
    assert RequiredFields.validate_or_error(
        {"ref": {"field1": "myf1", "field2": "myf2"}},
    )
    assert RequiredFields().ref.target is RequiredFields

    class OptionalFields(Schema):
        field1 = String(required=True)
        field2 = String(required=False)
        field3 = String()


# Generated at 2022-06-14 14:39:57.585363
# Unit test for constructor of class Reference
def test_Reference():
    class Child(Schema):
        pass
    class Parent(Schema):
        child = Reference('Child')
    assert Parent.child._target_string == 'Child'
    assert Parent.child.errors == {'null': 'May not be null.'}
    assert Parent.child.target == Child
    assert Parent.child.to == 'Child'
    assert Parent.child.validation_error('null') == ValidationError({'child': 'May not be null.'})
test_Reference()

# Generated at 2022-06-14 14:40:05.544166
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    test_field1 = Field()
    test_field2 = Field()
    test_schema = Schema(test_field1, test_field2)
    test_field1_value = 'test_field1_value'
    test_field2_value = 'test_field2_value'
    setattr(test_schema, 'field1', test_field1_value)
    setattr(test_schema, 'field2', test_field2_value)
    expected = {'field1', 'field2'}
    actual = set(test_schema.__iter__())
    assert actual == expected


# Generated at 2022-06-14 14:40:31.121988
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import String

    class Task(Schema):
        title = String
        price = String

    assert Task.fields == {"title": String, "price": String}
    assert isinstance(Task.fields["title"], String)
    assert isinstance(Task.fields["price"], String)
    assert Task.validate({"title": "test", "price": "test"}) == {"title": "test", "price": "test"}
    assert Task.validate({"title": "test", "price": "test"}, strict=True) == {"title": "test", "price": "test"}
    assert Task({"title": "test", "price": "test"}) == {"title": "test", "price": "test"}



# Generated at 2022-06-14 14:40:34.358091
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        field_1 = Field()
        field_2 = Field()
        field_3 = Field()

    schema = ExampleSchema(field_1=1, field_2=2)

    assert len(schema) == 2


# Generated at 2022-06-14 14:40:41.499046
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Point(Schema):
        x = Float()
        y = Float()
    point1 = Point({"x": 1.1, "y": 1.2})
    point2 = Point({"x": 1.1, "y": 1.2})
    assert point1 == point2
    point3 = Point({"x": 1.1, "y": 1.0})
    assert point1 != point3


# Generated at 2022-06-14 14:40:51.711193
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    # Test case data
    schemas_cls_name = 'schemas'
    schemas_bases_list = [object]
    schemas_attrs_dict = {
        'name_1': 'value_1',
        'name_2': 'value_2',
        'name_3': 'value_3',
    }

    # Perform the test
    result = SchemaMetaclass.__new__(
        SchemaMetaclass,
        schemas_cls_name,
        schemas_bases_list,
        schemas_attrs_dict,
    )

    # Check the result
    assert isinstance(result, type)
    assert issubclass(result, Mapping)
    assert result.__name__ == schemas_cls_name

# Generated at 2022-06-14 14:40:59.482820
# Unit test for constructor of class Schema
def test_Schema():
    class A(Schema):
        row1: Field(required=True)
        row2: Field(required=True)

    _ = A(row1=1, row2=2)
    _ = A({'row1': 1, 'row2': 2})
    _ = A(A(row1=1, row2=2))
    _ = A(A({'row1': 1, 'row2': 2}))


# Generated at 2022-06-14 14:41:03.455379
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    new_Schema = Schema()
    new_Schema.fields['key'] = 'object'
    assert list(new_Schema.__iter__()) == ['key']



# Generated at 2022-06-14 14:41:08.325882
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import pytest
    from typesystem import Schema, String

    class MySchema(Schema):
        foo = String()
        bar = String()

    schema = MySchema({"foo": "hello", "bar": "world"})
    assert schema["foo"] == "hello"
    with pytest.raises(KeyError):
        schema["baz"]


# Generated at 2022-06-14 14:41:11.119092
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    Z = Schema(dict(x=1, y=2))
    W = Schema(dict(y=2, x=1))
    assert(Z == W)

#Unit test for method __eq__ of class Schema

# Generated at 2022-06-14 14:41:13.494363
# Unit test for constructor of class Schema
def test_Schema():
    s = Schema(a=1, b=2)
    assert s.a == 1
    assert s.b == 2


# Generated at 2022-06-14 14:41:22.260613
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
	#
	#
	#
	#
	#
	#
	print('Test for method __eq__ of class Schema')
	#
	if test_Schema___eq__.__name__ == '__main__':
		print('Function "test_Schema___eq__" is being run by itself')
	else:
		print('Function "test_Schema___eq__" is being imported from another module')
	print('Function "test_Schema___eq__" called on object <typesystem.schemas.Schema object at 0x7f9b5a5c1fd0>')
	#
	#
	#
	#
	#
	#
	print('Test for method __eq__ of class Schema')
	#

# Generated at 2022-06-14 14:41:48.982710
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem import Boolean, Integer, String, Array
    from .schema import Schema, Reference
    from .schema import test_Schema_validate
    from .author import Author
    from .book import Book
    from .book_status import BookStatus

    # Test for a sub-class of Schema
    def create_author_validator():
        # Create a Reference sub-class
        author_field = Reference(Author)

        # Add the sub-class to a schema
        schema = Schema(title=String(max_length=100), author=author_field)
        return schema

    # Test create_author_validator
    author_schema = create_author_validator()
    test_Schema_validate(author_schema)

    # Test for string argument

# Generated at 2022-06-14 14:41:54.414999
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class SchemaTest(Schema):
        test_str = String(max_length=4)
        test_int = Integer()

    obj = SchemaTest(test_str="abc", test_int=5)
    assert len(obj) == 2
    assert obj.is_sparse == False


# Generated at 2022-06-14 14:41:55.448465
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    Schema(name= "hoang")

# Generated at 2022-06-14 14:41:57.135632
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert Schema({"name": "John"})["name"] == "John"



# Generated at 2022-06-14 14:42:01.252363
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        age = Field(type="integer")
        name = Field(type="string")

    Person(age=10, name="Ravi") == Person(age=10, name="Ravi")
    Person(age=10, name="Ravi") == Person(age=10, name="Ravi")

test_Schema___eq__()

# Generated at 2022-06-14 14:42:11.574950
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import pytest
    from typesystem import Schema
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)


    class Pet(Schema):
        name = String(max_length=100)
        owner = Reference(to=Person)


    pet = Pet(name='fido', owner=Person(name='bob', age=42))
    pet_repr = pet.__repr__()

    pet_repr_expected = """Pet(name='fido', owner={'name': 'bob', 'age': 42})"""
    assert pet_repr_expected == pet_repr

# Generated at 2022-06-14 14:42:19.047959
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import doctest
    from .test_types import test_fields, test_schemas
    failure_count, test_count = doctest.testmod(
        test_fields, optionflags=doctest.ELLIPSIS, raise_on_error=False, verbose=False
    )
    failure_count, test_count = doctest.testmod(
        test_schemas, optionflags=doctest.ELLIPSIS, raise_on_error=False, verbose=False
    )
    assert failure_count == 0

# Generated at 2022-06-14 14:42:25.858844
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    s = Schema()
    assert repr(s) == 'Schema()' # check return value has the expected value
    s = Schema(a=1)
    assert repr(s) == "Schema(a=1)"  # check return value has the expected value
    s = Schema(a=1, b=2)
    assert repr(s) == "Schema(a=1, b=2)"  # check return value has the expected value
    s = Schema(a=1, b=2, c=3)
    assert repr(s) == "Schema(a=1, b=2, c=3)"  # check return value has the expected value

# Generated at 2022-06-14 14:42:38.179775
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from json import loads
    from typesystem import Schema, String
    definitions = SchemaDefinitions()
    class Person(Schema,metaclass=SchemaMetaclass,definitions=definitions):
        first_name = String()
        last_name = String()
        age = String()
    Person.validate({"first_name": "Jane", "last_name": "Doe", "age": "32"})

# Generated at 2022-06-14 14:42:50.529678
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    assert len(definitions) == 0

    class Foo(Schema):
        bar = Reference("Bar")

    assert len(definitions) == 1
    assert "foo" in definitions
    assert "bar" not in definitions
    assert isinstance(definitions["foo"], type)

    class Bar(Schema):
        baz = Reference("Baz")

    assert len(definitions) == 2
    assert "bar" in definitions
    assert "baz" not in definitions
    assert isinstance(definitions["foo"], type)
    assert isinstance(definitions["bar"], type)

    class Baz(Schema):
        pass

    assert len(definitions) == 3
    assert "baz" in definitions
    assert isinstance(definitions["foo"], type)

# Generated at 2022-06-14 14:43:31.692683
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        hoge = Field()
        fuga = Field()
        piyo = Field()
    class TestSchema2(Schema):
        hoge = Field()
        fuga = Field()
        piyo = Field()

    # test equal
    instance1 = TestSchema(hoge=0, fuga=1, piyo=2)
    instance2 = TestSchema(hoge=0, fuga=1, piyo=2)
    assert instance1 == instance2

    # test not equal
    instance3 = TestSchema2(hoge=0, fuga=1, piyo=2)
    assert instance1 != instance3
    

# Generated at 2022-06-14 14:43:36.948488
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Base(Schema):
        foo = Field()
    
    class Subclass(Base):
        bar = Field()

    assert Subclass.fields['foo'] is Base.fields['foo']
    assert Subclass.fields['bar'] is Subclass.bar
    assert Base.fields['bar'] not in Subclass.fields


# Generated at 2022-06-14 14:43:40.807712
# Unit test for constructor of class Schema
def test_Schema():
    class Human(Schema):
        id = Field(type="string")
        name = Field(type="string")

    obj = Human(id="0", name="chris")
    assert obj["id"] == "0"
    assert obj["name"] == "chris"

# Generated at 2022-06-14 14:43:44.406836
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")
    p = Person(name="Joe", age=10)
    assert p.name == "Joe"
    assert p.age == 10


# Generated at 2022-06-14 14:43:50.445698
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem import Schema


    class ColorSchema(Schema):
        name = "Color"
        r = Reference("Hex4", required=True)
        g = Reference("Hex4", required=True)
        b = Reference("Hex4", required=True)

    class Hex4(Schema):
        length = 4
        pattern = "0-9A-Fa-f"

    class Color(Schema):
        definitions = SchemaDefinitions({"Hex4": Hex4})
        schema = ColorSchema()

# Generated at 2022-06-14 14:43:58.339408
# Unit test for constructor of class Reference
def test_Reference():
    class Actor(Schema):
        name = String()

    class Movie(Schema):
        title = String()
        director = Reference(Actor)

    # Initialize a instance of class Movie
    movie = Movie.validate({"title": "Avengers: Endgame", "director": {"name": "Joe Russo"}})
    # Test if the initialization is correct
    print(movie.director.name == "Joe Russo")
    # Test if the class is validator
    print(movie.validate({"title": "Avengers: Endgame", "director": {"name": "Joe Russo"}}))



# Generated at 2022-06-14 14:44:02.506345
# Unit test for constructor of class Reference
def test_Reference():
    r = Reference("a")
    assert r.to == "a" and not hasattr(r, "_target_string") and not hasattr(r, "_target")
    r = Reference("a", definitions={"a": 1})
    assert r.to == "a" and not hasattr(r, "_target_string") and r._target == 1


# Generated at 2022-06-14 14:44:06.255483
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    p = Person(name="John Smith", age=20)
    assert p.name == "John Smith"
    assert p.age == 20
