

# Generated at 2022-06-14 14:34:46.982253
# Unit test for constructor of class Schema

# Generated at 2022-06-14 14:34:50.498306
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = String()

    class People(Schema):
        people = Array(Reference("Person"))

    set_definitions(People.fields["people"], {Person.__name__: Person})

# Generated at 2022-06-14 14:34:54.244046
# Unit test for method validate of class Reference
def test_Reference_validate():
    # Create instance of array class
    array_field = Array(String())

    assert array_field.validate(None) == None

    assert array_field.validate('') == ['']

    assert array_field.validate(['']) == ['']


# Generated at 2022-06-14 14:34:59.067243
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        my_field = Field()

    instance = MySchema()
    assert instance.my_field is None
    instance = MySchema(my_field=True)
    assert isinstance(instance.my_field, bool)
    assert instance.my_field is True
    instance = MySchema({"my_field": True})
    assert isinstance(instance.my_field, bool)
    assert instance.my_field is True



# Generated at 2022-06-14 14:35:11.148788
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import pytest
    from sphinx.errors import SphinxError


# Generated at 2022-06-14 14:35:11.675219
# Unit test for constructor of class Schema
def test_Schema():
    assert callable(Schema)


# Generated at 2022-06-14 14:35:14.733435
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class MySchema(Schema):
        foo = String()
        bar = Integer()
        qux = String()
    assert MySchema({"foo": "hello", "bar": 42, "qux": "world"}) == MySchema(foo="hello", bar=42, qux="world")
    assert MySchema({"foo": "hello", "bar": 42}) == MySchema(foo="hello", bar=42)
    assert MySchema({"foo": "hello", "bar": 42}) != MySchema(foo="hello", bar=43)

# Generated at 2022-06-14 14:35:22.882960
# Unit test for function set_definitions
def test_set_definitions():
    # 1. Construct a Schema class that has a field defined with a Reference
    #    object.
    class FooSchema(Schema):
        a = Reference("Bar")
    
    # 2. Construct a SchemaClass that has a field that can be referenced to
    class BarSchema(Schema):
        b = Integer()

    # 3. Construct a SchemaDefinitions object containing the two schemas
    schema_definitions = SchemaDefinitions()
    schema_definitions["Bar"] = BarSchema
    
    # 4. Call set_definitions on the definitions and FooSchema
    set_definitions(FooSchema, schema_definitions)

    # 5. Assert that FooSchema.a has the correct target
    assert FooSchema.a.target is BarSchema

# Generated at 2022-06-14 14:35:25.727896
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    snippet = Schema.make_validator()
    set_definitions(snippet, definitions)


# Generated at 2022-06-14 14:35:29.282889
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class MySchema(Schema):
        id = Field()
        name = Field()
    schema = MySchema(id=42, name='Dev.to')

    # We should see the number of fields
    assert len(schema) == 2

# Generated at 2022-06-14 14:35:42.621120
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class test_Schema(Schema):
        pass
    
    S=test_Schema()
    assert S.__len__ == 0

# Generated at 2022-06-14 14:35:43.649056
# Unit test for function set_definitions
def test_set_definitions():
    class Settings(Schema):
        class User(Schema):
            id = Field()
            name = Field()

        user = Reference("User")

# Generated at 2022-06-14 14:35:47.254663
# Unit test for function set_definitions
def test_set_definitions():
    class ObjectObj(Object):
        x = Field()
        y = Field()

    class ObjectArray(Object):
        x = Field()
        y = Field()

    class Arrays(Object):
        objectobj = Array(items=ObjectObj)
        objectarray = Array(items=[ObjectArray])

    definitions = SchemaDefinitions()
    set_definitions(Arrays, definitions)

    assert definitions["ObjectArray"] == ObjectArray
    assert definitions["ObjectObj"] == ObjectObj

# Generated at 2022-06-14 14:35:49.416562
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    schema = Schema()
    assert repr(schema) == "Schema()"


# Generated at 2022-06-14 14:36:01.534507
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        pass

    assert len(MySchema.__dict__) == 1
    assert MySchema.__dict__.keys() == dict_keys(['__module__'])
    assert MySchema.__dict__.values() == dict_values(['main'])
    assert MySchema.__dict__.items() == dict_items([('__module__', 'main')])
    assert len(MySchema.__dict__['__module__']) == 4
    assert MySchema.__dict__['__module__'] == 'main'

    my_obj = MySchema()
    assert len(my_obj.__class__.__dict__) == 1
    assert my_obj.__class__.__dict__.keys() == dict_keys(['__module__'])

# Generated at 2022-06-14 14:36:06.850571
# Unit test for function set_definitions
def test_set_definitions():
    class Child(Schema):
        child_field = Field()

    class Parent(Schema):
        parent_field = Field()
        child_field = Reference(Child, required=True)

    definitions = SchemaDefinitions()
    set_definitions(Parent.child_field, definitions)

    assert definitions["Child"] == Child


# Generated at 2022-06-14 14:36:14.172907
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Test Schema__len__
    schema = schema_cls(fields={})
    assert len(schema) == 0

    schema = schema_cls(fields={'a': 1, 'b': 2})
    assert len(schema) == 2

    schema = schema_cls(fields={'a': 1, 'b': 2}, a=1, b=2)
    assert len(schema) == 2

    schema = schema_cls(fields={'a': 1, 'b': 2}, a=1, b=2)
    schema.c = 3
    assert len(schema) == 3


# Generated at 2022-06-14 14:36:20.776033
# Unit test for constructor of class Schema
def test_Schema():
    class Y(Schema):
        a = Field(String)
        b = Field(Integer)
        c = Field(String, required = True, default = "abcde")
        d = Field(Integer, required = False, default = 123)
    class X(Schema):
        x = Field(String)
        y = Field(Y)
    x = X(x = String("hello world"), y = Y(a = "hello"))
    assert isinstance(x, X)
    assert isinstance(x.y, Y)
    assert x.y.a == "hello"
    assert x.y.b == None
    assert x.y.c == "abcde"
    assert x.y.d == 123

# Generated at 2022-06-14 14:36:30.022543
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import types

    # Define a schema class
    class ExampleSchema(Schema):
        a = Field(type_="integer")
        b = Field(type_="string")

    # Initialize an instance of the schema class
    e = ExampleSchema()

    # Verify the return type
    assert isinstance(iter(e), types.GeneratorType)

    # Verify the behavior
    assert list(e) == []
    e.a = 0
    assert list(e) == ['a']
    e.b = "hello world"
    assert list(e) == ['a', 'b']



# Generated at 2022-06-14 14:36:33.396780
# Unit test for constructor of class Schema
def test_Schema():
    class User(Schema):
        email = String()

    with pytest.raises(TypeError, match="Invalid argument 'email' for User()."):
        User(email="INVALID_EMAIL")


# Generated at 2022-06-14 14:36:53.147195
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import tempfile
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    with open('Schema.py') as oldfile, f:
        for line in oldfile:
            f.write(line.replace('test_Schema___iter__()', 'pass'))
    f.close()
    try:
        from importlib import reload
        from Schema import Schema
        reload(Schema)
        from Schema import test_Schema___iter__
        test_Schema___iter__()
    finally:
        import os
        os.remove(f.name)

# Generated at 2022-06-14 14:36:59.051944
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class TestSchema1(Schema):
        id = Field(type="string")
        name = Field(type="string")

    # Test that __iter__ method will return all fields for which there is an attribute set
    schema = TestSchema1(id='123', name='Name1')
    assert list(schema) == ['id', 'name']


# Generated at 2022-06-14 14:37:02.510752
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    import typesystem

    class Person(Schema):
        name = typesystem.String()
        age = typesystem.Integer(minimum=0, maximum=150)

    person = Person(name="Albert", age=42)
    assert person.name == "Albert"
    assert person.age == 42
    assert isinstance(person, Person)


# Generated at 2022-06-14 14:37:13.414941
# Unit test for function set_definitions
def test_set_definitions():
  """Unit test for function set_definitions"""
  class MySchema1(Schema):
      pass

  class MySchema2(Schema):
      pass

  class MySchema3(Schema):
      myref = Reference("MySchema1")

  class MySchema4(Schema):
      myref = Reference(MySchema2)

  # Generate non-string reference
  definitions = SchemaDefinitions()
  set_definitions(MySchema3.fields['myref'], definitions)
  assert MySchema3.fields['myref']._target_string == 'MySchema1'

  # Generate string reference
  definitions = SchemaDefinitions()
  definitions['MySchema2'] = MySchema2
  set_definitions(MySchema4.fields['myref'], definitions)


# Generated at 2022-06-14 14:37:20.890499
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class SubSchema(Schema):
        prop1 = Field()
    class SubSchema2(Schema):
        prop2 = Field()
    class TestSchema(Schema):
        sub1 = SubSchema()
        sub2 = SubSchema2()
    s = TestSchema(sub1=SubSchema(prop1=1))
    assert repr(s) == 'TestSchema(sub1=SubSchema(prop1=1), sub2=SubSchema2())'

    s = TestSchema()
    assert repr(s) == 'TestSchema()'


# Generated at 2022-06-14 14:37:23.239914
# Unit test for constructor of class Schema
def test_Schema():
    schema = Schema()
    assert schema.fields == {}


# Generated at 2022-06-14 14:37:28.091469
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import Array
    from typesystem import Schema, SchemaMetaclass

    class Message(Schema, metaclass=SchemaMetaclass):
        foo = Array()

    assert isinstance(Message.fields.get('foo'), Array)
    assert Message.__name__ == 'Message'


# Generated at 2022-06-14 14:37:38.847921
# Unit test for function set_definitions
def test_set_definitions():
    def check_definitions(field: Field, definitions: SchemaDefinitions) -> None:
        assert field.definitions == definitions
        if isinstance(field, Array):
            if field.items is not None:
                if isinstance(field.items, (tuple, list)):
                    for child in field.items:
                        check_definitions(child, definitions)
                else:
                    check_definitions(field.items, definitions)
        elif isinstance(field, Object):
            for child in field.properties.values():
                check_definitions(child, definitions)

    definitions = SchemaDefinitions()
    field = Object(properties={"test": Reference("test")})
    set_definitions(field, definitions)
    check_definitions(field, definitions)

# Generated at 2022-06-14 14:37:47.842514
# Unit test for function set_definitions
def test_set_definitions():
    class First:
        pass

    class Second:
        pass

    field1 = Reference(to="First")
    field2 = Reference(to=First)
    field3 = Reference(to="Second")

    definitions = SchemaDefinitions()
    set_definitions(field1, definitions)
    set_definitions(field2, definitions)
    set_definitions(field3, definitions)

    definitions["First"] = First
    definitions["Second"] = Second

    assert field1.target is First
    assert field2.target is First
    assert field3.target is Second

    assert field1.target_string == "First"
    assert field2.target_string == "First"
    assert field3.target_string == "Second"

    assert field1.to == "First"
    assert field2.to == First
    assert field

# Generated at 2022-06-14 14:37:54.274844
# Unit test for constructor of class Schema
def test_Schema():
    class Test(Schema):
        name = Field(type="string")
        age= Field(type="integer")

    a = Test(name="Tyler",age="25")
    assert a.is_sparse is False
    assert a.name == "Tyler"
    assert a.age == 25
    print('Pass the test of "[__init__]" of class Schema')


# Generated at 2022-06-14 14:38:07.507717
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = String(max_length=100)

    Person.validate({"name": "Ada"}, strict=True)

    p = Person(name="Johann Wolfgang von Goethe")
    assert repr(p) == "Person(name='Johann Wolfgang von Goethe')"


# Generated at 2022-06-14 14:38:15.292961
# Unit test for function set_definitions
def test_set_definitions():
    class Book(Schema):
        title = Field(type_=str)

    class Library(Schema):
        books = Reference(Book, type_=Array)

    def1 = SchemaDefinitions()
    def2 = SchemaDefinitions()
    set_definitions(Library, def1)
    set_definitions(Library, def2)
    assert len(def1) == 1
    assert len(def2) == 1
    assert def1["Book"] == def2["Book"]



# Generated at 2022-06-14 14:38:18.217553
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String
    p = Person(name='Tom')
    assert iter(p) == iter(['name'])

test_Schema___iter__()

# Generated at 2022-06-14 14:38:25.986768
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Integer, String
    from collections import OrderedDict

    class BasicSchema(Schema):
        title = String(max_length=255)
        price = Integer(minimum=0)
        stock = Integer(minimum=0)

    item_dict = {
        'title': 'item',
        'price': 10,
        'stock': 1
    }
    try:
        item = BasicSchema(item_dict)
        assert item.title == 'item'
        assert item.price == 10
        assert item.stock == 1
        # Note: The fields of input dictionary are arranged in order of creation.
        assert item.fields == OrderedDict([('title', String(max_length=255)), ('price', Integer(minimum=0)), ('stock', Integer(minimum=0))])
    except:
        assert False

# Generated at 2022-06-14 14:38:28.230761
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert (
        len(Schema({"a": 100, "b": "abcd"})) == 2
    ), "Length of the object should be same as the number of attributes"

# Generated at 2022-06-14 14:38:29.918792
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    assert False, "Unimplemented"

# Generated at 2022-06-14 14:38:36.964708
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
	class MySchema(Schema):
		field_1 = String(max_length=12, description="A description of field 1")
		field_2 = String(max_length=12, description="A description of field 2")
		field_3 = String(max_length=12, description="A description of field 3")

	s = MySchema(field_1="a valid string", field_2="a valid string2")
	x = list(s)
	assert(x == ['field_1', 'field_2'])


# Generated at 2022-06-14 14:38:44.372582
# Unit test for function set_definitions
def test_set_definitions():
    # Create a few test field objects.
    object_field = Object(properties={}, additional_properties=False)
    object_field_2 = Object(properties={}, additional_properties=True)
    array_field = Array(items=[object_field, object_field_2])
    array_field_2 = Array(items=[array_field, object_field_2])
    reference_field = Reference("foo")
    reference_field_2 = Reference("foo", required=True)
    reference_field_3 = Reference("foo", definitions={"foo": object_field})

    # Create a test definitions map.
    definitions = SchemaDefinitions()

    # Test setting a simple object field.
    set_definitions(object_field, definitions)
    assert object_field.definitions == definitions

    # Test setting a simple array field.
    set

# Generated at 2022-06-14 14:38:48.123565
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Foo(Schema):
        a = Field()
        b = Field()
    foo = Foo(a='hello')
    assert len(foo) == 1
    assert list(iter(foo)) == ['a']


# Generated at 2022-06-14 14:38:53.114668
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # given
    class MySchema(Schema):
        pass
    schema = MySchema()
    # when
    result = schema.__repr__()
    # then
    assert result == "MySchema()"



# Generated at 2022-06-14 14:39:24.531816
# Unit test for method __len__ of class Schema
def test_Schema___len__():
        from typesystem import Integer
        from typesystem.exceptions import TypeError
        class OneFieldSchema(Schema):
            a = Integer(default = 5)
        
        schema = OneFieldSchema()
        assert len(schema) == 1
        
        
        class TwoFieldsSchema(Schema):
            a = Integer(default = 5)
            b = Integer()
            
        schema = TwoFieldsSchema()
        assert len(schema) == 1
        
        
        class TwoFieldsSchema(Schema):
            a = Integer(default = 5)
            b = Integer(default = 7)
            
        schema = TwoFieldsSchema()
        assert len(schema) == 2
        
        
        

# Generated at 2022-06-14 14:39:31.360775
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Create schema
    schema = Schema()

    # Create string property
    string_property = 'string_property'

    # Add property to schema
    schema.string_property = string_property

    # Iterate schema
    for property in schema:
        # Log message
        print('Property = ' + property)
        print('type = ' + str(type(property)))


# Generated at 2022-06-14 14:39:35.415307
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    Schema1 = Schema
    Schema2 = Schema
    assert Schema1 is not Schema2
    # TODO: Introduce a class to be used as superclass of Schema1 and Schema2
    # to fix the next assertion.
    # assert not Schema1.__eq__(Schema2)

# Generated at 2022-06-14 14:39:41.667074
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Obj1(Schema):
        a = String(request=True)
        b = String()
    class Obj2(Schema):
        a = String(request=True)
        b = String()

    obj1 = Obj1(a="ok", b="ok")
    obj2 = Obj2(a="ok", b="ok")

    assert obj1 == obj2

    class Obj3(Schema):
        a = String(request=True)
        b = String()
    class Obj4(Schema):
        a = String(request=True)

    obj3 = Obj3(a="ok", b="ok")
    obj4 = Obj4(a="ok")

    assert not (obj3 == obj4)


# Generated at 2022-06-14 14:39:46.895596
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    person = Person(
        {
            "name": "John",
            "age": 30,
        }
    )
    assert person["name"] == "John"
    assert person["age"] == 30

# Generated at 2022-06-14 14:39:50.891985
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(Schema):
        a = Field()

    class B(A):
        b = Field()

    class Tests(B):
        c = Field()

    assert Tests.fields == {'a': A.fields['a'], 'b': B.fields['b'], 'c': Field()}


# Generated at 2022-06-14 14:39:58.012616
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Foo(Schema):
        bar = String()
        baz = String()

    foo = Foo(bar="x", baz="y")
    assert foo["bar"] == "x"
    assert foo["baz"] == "y"

    try:
        foo["does_not_exist"]
    except KeyError:
        pass
    else:
        assert False, "KeyError should have been raised."


# Generated at 2022-06-14 14:40:03.385558
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    
    # Test type casting
    from typesystem import Integer

    class SomeClass(Schema):
        a = Integer()

    obj = SomeClass(a=1)
    assert len(obj) == 1

    class SomeClass(Schema):
        a = Integer(default=1)

    obj = SomeClass()
    assert len(obj) == 0


# Generated at 2022-06-14 14:40:07.511191
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from typesystem.objects import Schema

    class Person(Schema):
        name = String(max_length=100)
        age = Integer()

    person = Person(name="Conrad", age=5)
    serialized_person = person["name"]

# Generated at 2022-06-14 14:40:12.335207
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert list(Schema({"x": 1, "y": 2})) == ["x", "y"]
    assert list(Schema({"x": 1}, y=2)) == ["x", "y"]
    assert list(Schema({"x": 1}, y=2, z=None)) == ["x", "y"]

# Generated at 2022-06-14 14:40:56.898436
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.types import String

    class Hero(Schema):
        name = String(max_length=100)

    hero = Hero(name="Frodo")
    assert tuple(hero) == ('name',)


# Generated at 2022-06-14 14:41:06.108623
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Test simple cases
        class A(Schema):
            a = Field(type="string")
            b = Field(type="string")
            c = Field(type="string")
            d = Field(type="string")

        # Test complex cases
        class B(Schema):
            a = Field(type="string")

        class C(Schema):
            a = Field(type="string")
            b = Field(type="string")

        assert len(A()) == 4
        assert len(B()) == 1
        assert len(C()) == 2


# Generated at 2022-06-14 14:41:15.416786
# Unit test for constructor of class Reference
def test_Reference():
    class TestSchema(Schema):
        pass

    class TestSchema2(Schema):
        pass

    class TestSchema3(Schema):
        pass

    def test_Reference_string():
        Reference("TestSchema")
        Reference("TestSchema", to="TestSchema")

    def test_Reference_Schema():
        Reference(TestSchema)
        Reference(TestSchema, to=TestSchema)
        Reference(TestSchema, definitions={"TestSchema": TestSchema})

    test_Reference_string()
    test_Reference_Schema()


# Generated at 2022-06-14 14:41:20.501290
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Item(Schema):
        name = String()
        quantity = Integer()

    item1 = Item(name="apple", quantity=3)
    item2 = Item(name="apple", quantity=3)
    item3 = Item(name="apple", quantity=5)
    assert item1 == item2
    assert item1 != item3
    assert item2 != item3
    assert item1 != "foo"


# Generated at 2022-06-14 14:41:31.137426
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import sys
    import pytest
    import typesystem
    from typesystem.exceptions import ValidationError
    from typing import Any, List, Optional, Tuple, Union
    from typesystem.base import FIELD_VALIDATION_ERROR
    from typesystem import fields
    from typesystem.schemas import Schema, Reference
    typesystem.ValidationError = ValidationError
    def test_empty_schema():
        class TestSchema(Schema):
            pass
        assert len(TestSchema({})) == 0
    def test_empty_schema2():
        class TestSchema(Schema):
            field = fields.String()
        assert len(TestSchema({})) == 0
    def test_empty_schema3():
        class TestSchema(Schema):
            field = fields.String()
            field

# Generated at 2022-06-14 14:41:37.414136
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Address(Schema):
        street = String()
        city = String()

    class Person(Schema):
        first_name = String()
        last_name = String()
        address = Reference(to=Address)

    Person.validate({"first_name": "Joe", "last_name": "Smith", "address": {}})

# Generated at 2022-06-14 14:41:41.063776
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        b = Field(str)
        a = Field(str)
    s = MySchema(b="foo", a="bar")
    assert s.a == "bar"
    assert s.b == "foo"

# Generated at 2022-06-14 14:41:44.561549
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)

    assert len(Person({"name": "John", "age": 42})) == 2
    assert len(Person({"age": 42})) == 1
    assert len(Person()) == 0



# Generated at 2022-06-14 14:41:49.570234
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    # Given that:
    class Class1(Schema):
        field1 = String(max_length=10)
    # When we:
    # Then:
    assert Class1.fields == {"field1": String(max_length=10)}
#


# Generated at 2022-06-14 14:41:59.761206
# Unit test for constructor of class Reference
def test_Reference():
    # This function tests the various use cases for reference
    # The first unit test is to see if we can use a string.
    # This first test uses a string
    class Test(object):
        references = Reference("Test")
        def __init__(self, references):
            self.references = references
    # The second test is to see a subclass of Reference
    class Test2(Reference):
        pass
    class Test3(object):
        references = Test2(to="Test2")
        def __init__(self, references):
            self.references = references
    # The third test is an object subclass of Reference
    class Test4(object, Reference):
        def __init__(self, to, definitions):
            super(Test4, self).__init__(to, definitions)
    class Test5(object):
        references = Test

# Generated at 2022-06-14 14:43:30.862201
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        foo = Field()
        bar = Field()
        baz = Field(default="quux")

    assert MySchema.fields == {"foo": Field(), "bar": Field(), "baz": Field(default="quux")}

    schema = MySchema(foo=1, bar=2)
    assert schema.foo == 1
    assert schema.bar == 2
    assert schema.baz == "quux"

    schema = MySchema(dict(foo=1, bar=2))
    assert schema.foo == 1
    assert schema.bar == 2
    assert schema.baz == "quux"

    class MyOtherSchema(Schema):
        foo = Field()
        bar = Field()

    schema = MyOtherSchema(MySchema(foo=1, bar=2))


# Generated at 2022-06-14 14:43:36.001505
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem import Boolean, Integer, String


    class User(Schema):
        id = String(allow_null=False)
        is_active = Boolean(allow_null=False)
        age = Integer(allow_null=False)


    user1 = User(id="123", is_active=True, age=12)
    user2 = User(id="123", is_active=True, age=12)
    user3 = User(id="123", is_active=False, age=12)

    assert user1 == user2
    assert user1 != user3


# Generated at 2022-06-14 14:43:39.848900
# Unit test for function set_definitions
def test_set_definitions():
    class User(Schema):
        name = Field()

    class Page(Schema):
        user = Reference("User")

    definitions = SchemaDefinitions()
    set_definitions(Page(user={}).fields["user"], definitions)
    assert definitions["User"] == User

# Generated at 2022-06-14 14:43:45.867816
# Unit test for function set_definitions
def test_set_definitions():
    class User(Schema):
        name = String()
        is_admin = Boolean(default=False)

    class UserInfo(Schema):
        name = Reference("User")
        is_admin = Reference("User")

    assert UserInfo.fields["name"].definitions is None
    definitions = SchemaDefinitions()
    set_definitions(UserInfo, definitions)
    assert UserInfo.fields["name"].definitions is definitions
    assert UserInfo.fields["is_admin"].definitions is definitions

# Generated at 2022-06-14 14:43:47.737668
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        field = 'field'
    obj = TestSchema(field=1)
    assert str(obj) == "TestSchema(field=1)"

# Generated at 2022-06-14 14:43:52.578361
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class FooSchema(Schema):
        foo = Field(Integer)
        bar = Field(String)
        baz = Field(String)

    f1 = FooSchema({'foo': 1, 'bar': 'abc'})

    expected = ['foo', 'bar', 'baz']
    actual = []

    for k in f1:
        actual.append(k)

    assert actual == expected


# Generated at 2022-06-14 14:43:59.778001
# Unit test for function set_definitions
def test_set_definitions():
    class MySchema1(Schema):
        field = Reference('other_field')
        other_field = String()

    class MySchema2(Schema):
        my_schema1 = Reference('MySchema1')

    definitions = SchemaDefinitions()
    for field in [MySchema1.field, MySchema2.my_schema1]:
        set_definitions(field, definitions)

    assert MySchema1.field.target == MySchema1.other_field
    assert MySchema2.my_schema1.target == MySchema1

# Generated at 2022-06-14 14:44:04.860069
# Unit test for function set_definitions
def test_set_definitions():
    class Inner(Schema):
        a = Field()
        b = Field()

    definitions = SchemaDefinitions()
    class Outer(Schema):
        inner = Reference(Inner)

    set_definitions(Outer.fields["inner"], definitions)
    assert Outer.fields["inner"].definitions is definitions

# Generated at 2022-06-14 14:44:10.230537
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    # Test 1
    class TestSchema(Schema):
        field = Field()

    obj = TestSchema(field="test_field")

    if len(list(obj.__iter__())) == 1:
        pass

    # Test 2
    class TestSchema(Schema):
        field = Field()

    obj = TestSchema()

    if list(obj.__iter__()) == []:
        pass

