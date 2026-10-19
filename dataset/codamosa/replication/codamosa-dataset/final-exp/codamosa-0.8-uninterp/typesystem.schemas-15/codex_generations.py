

# Generated at 2022-06-14 14:34:53.896089
# Unit test for function set_definitions
def test_set_definitions():
    class Course(Schema):
        slug = Reference(to="name")
        name = Field()
        category = Field()

    definitions = SchemaDefinitions()
    set_definitions(Course.fields["slug"], definitions)
    assert Course.fields["slug"].definitions is definitions
    assert Course.fields["slug"].target_string == "name"
    assert Course.fields["slug"]._target is None
    assert Course.fields["name"].definitions is None

    Course.fields["name"].definitions = definitions
    Course.fields["category"].definitions = definitions
    assert Course.fields["name"].definitions is definitions
    assert Course.fields["category"].definitions is definitions

    definitions[Course.__name__] = Course
    assert Course.fields["name"].definitions is definitions
   

# Generated at 2022-06-14 14:35:05.210057
# Unit test for function set_definitions
def test_set_definitions():
    class TestReference(Reference):
        pass

    class TestSchema(Schema):
        test = Field()
        ref = TestReference("TestObject")

    class TestObject(Schema):
        foo = Field()

    definitions = SchemaDefinitions()
    definitions["TestObject"] = TestObject

    assert TestReference(to="TestObject", definitions=definitions).definitions is None
    assert TestSchema.ref.definitions is None
    set_definitions(TestSchema, definitions)
    assert TestSchema.ref.definitions is definitions
    assert TestReference(to="TestObject", definitions=definitions).definitions is None

    test = TestSchema(test="test", ref={"foo": "bar"})
    assert test.ref.foo == "bar"
    assert test.ref.is_sparse is False
    assert Test

# Generated at 2022-06-14 14:35:07.673777
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field = Reference("Person")
    set_definitions(field, definitions)
    assert field.target == Person



# Generated at 2022-06-14 14:35:09.803037
# Unit test for constructor of class Schema
def test_Schema():
    class Test(Schema):
        a = Field(type='string')
    test = Test({'a': 'test'})


# Generated at 2022-06-14 14:35:15.999374
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Check class SimpleSchema
    class SimpleSchema(Schema):
        name = Field(str)
        age = Field(int)
        email = Field(str, nullable=True)
    # Assert return type
    assert isinstance(iter(SimpleSchema(name='Bob', age=34)), typing.Iterator)
    # Assert return value
    values = set(iter(SimpleSchema(name='Bob', age=34)))
    assert values == {'name', 'age'}

# Generated at 2022-06-14 14:35:20.358291
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        one = Field(str)
        two = Field(int)
        three = Field(str)
    s = TestSchema(one='one',three='three')
    assert len(s) == 2
    assert list(s) == ['one', 'three']

test_Schema___iter__()


# Generated at 2022-06-14 14:35:24.635782
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from timesystem.schema import Person
    # Create the person
    person = Person(name="Hellen", age=27)
    # Test for equality
    assert [i for i in person] == ['name', 'age']
    # Print 
    print("[i for i in person] == ['name', 'age']")
    # Print 
    print('print("[i for i in person] == [\'name\', \'age\']")')


# Generated at 2022-06-14 14:35:30.899259
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Sample(Schema):
        name = Field(str)
        age = Field(int)
        weight = Field(int)

    a = Sample(name="david", age=27, weight=85)
    b = Sample(name="david", age=27, weight=85)
    assert a == b
    b = Sample(name="david", weight=85)
    assert a != b


# Generated at 2022-06-14 14:35:31.508461
# Unit test for function set_definitions
def test_set_definitions():
    pass

# Generated at 2022-06-14 14:35:36.884581
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        name: Field
        age: Field
    
    schema1 = TestSchema(name='Fred', age=37)
    schema2 = TestSchema(name='Fred', age=37)
    schema3 = TestSchema(name='Fred', age=38)
    
    assert schema1 == schema2
    assert schema1 != schema3


# Generated at 2022-06-14 14:35:50.655825
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class mySchema(Schema):
        fields = {'id': Field(type=str)}
    s1 = mySchema(id="1")
    s2 = mySchema(id="1")
    assert(s1 == s2)



# Generated at 2022-06-14 14:36:02.908313
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    assert Schema(a=1, b=0) == Schema(a=1, b=0)
    assert Schema(a=1, b=0) != Schema(a=0, b=1)
    assert Schema(a=1, b=0) != Schema(a=1)
    assert Schema(a=1, b=0) != Schema(a=1, b=0, c=0)
    assert Schema(a=1, b=0) != 1
    assert Schema(a=1, b=0) != {}
    assert Schema(a=1, b=0) != {"a": 1, "b": 0}

if __name__ == "__main__":
    import json
    import doctest
    doctest.testmod()

    print("Testing __eq__:")

# Generated at 2022-06-14 14:36:12.612442
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from decimal import Decimal
    from typesystem.fields import Integer, Float, Decimal as DecimalField, Date

    class ProductSchema(Schema):
        id = Integer()
        name = Integer()
        price = DecimalField(places=2)
        released_on = Date()

    values = {
        'id': 1,
        'name': 'candy',
        'price': Decimal('0.50'),
        'released_on': datetime.date(2017, 7, 15)
    }

    obj = ProductSchema(values)
    expected = {'id': 1, 'name': 'candy', 'price': Decimal('0.50'), 'released_on': datetime.date(2017, 7, 15)}

    result = {}

    for key,value in obj.__iter__():
        result[key]

# Generated at 2022-06-14 14:36:15.032160
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class A(Schema):
        a = Field()

    a = A()
    assert(a['a'] == None)


# Generated at 2022-06-14 14:36:20.449535
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Author(Schema):
        name = String(max_length=100)
        age = Integer()
    d_aut,d_aut_repr, d_aut_stored = {'name': 'John', 'age': 44}, Author(name='John', age=44), Author(name='John', age=44)
    if isinstance(d_aut, Mapping):
        assert d_aut == eval(d_aut_repr.__repr__())
    else:
        print('Error: isinstance(d_aut, Mapping) --> False')


# Generated at 2022-06-14 14:36:31.367857
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from datetime import datetime, timezone
    from typesystem import DateTime

    class FooSchema(Schema):
        x = DateTime()
        y = DateTime()

    foo = FooSchema(x=datetime(2010, 10, 1, 12, 30, 0, tzinfo=timezone.utc),
                    y=datetime(2010, 10, 1, 12, 30, 0, tzinfo=timezone.utc))
    assert foo['x'] == '2010-10-01T12:30:00+00:00'
    assert foo['y'] == '2010-10-01T12:30:00+00:00'

test_Schema___getitem__()
# End unit test


# Generated at 2022-06-14 14:36:35.316086
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class BugSchema(Schema):
        first_seen = String()
        reproducible = Boolean()
    obj = BugSchema(
        first_seen="Tuesday",
        reproducible=True,
    )
    assert obj.__iter__() == ['first_seen', 'reproducible']


# Generated at 2022-06-14 14:36:41.932457
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class A(Schema):
        a = int
    class B(Schema):
        b = int
    assert A() == A()
    assert B() == B()
    assert A({"a": 1}) == A(a=1)
    assert A({"a": 1}) == A({})
    assert A({"a": 1}) == A({}, a=1)
    assert A({"a": 1}) == B({"a": 1})
    assert A({"a": 1}) != B({"b": 1})
    assert A({"a": 1}) != B()


# Generated at 2022-06-14 14:36:43.329355
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    s = Schema
    assert len(s)==0


# Generated at 2022-06-14 14:36:46.544966
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    d = SchemaDefinitions()
    class A(Schema, metaclass=SchemaMetaclass, definitions=d):
        a = Integer()
    assertTrue(d['A'])


# Generated at 2022-06-14 14:37:03.841364
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import Integer, String

    class User(Schema):
        id = Integer()
        name = String()

    assert User.fields == {'id': Integer(), 'name': String()}
    user = User(id=1, name='Frank')
    assert user.id == 1
    assert user.name == 'Frank'
    assert user.fields == {'id': Integer(), 'name': String()}
    assert user == User(id=1, name='Frank')
    assert not (user == User(id=1, name='Frances'))

    try:
        User(unknown='unknown')
    except TypeError as error:
        assert str(error) == "unknown is an invalid keyword argument for User()."
    else:
        assert False, r"User(unknown='unknown') should have raised a TypeError."


# Generated at 2022-06-14 14:37:15.301657
# Unit test for constructor of class Schema
def test_Schema():
    x = Schema()
    validator_1 = Schema.make_validator(strict = False)
    validator_2 = Schema.make_validator(strict = True)
    result = Schema.validate(x)
    validator_1.validate(result)
    validator_2.validate(result)
    # Running the line below should raise an exception
    # validator_2.validate(result, strict = True)
    assert Schema.validate_or_error(x) == ValidationResult(value = result, error = None)
    assert Schema.validate_or_error(x, strict = True) == ValidationResult(value = result, error = None)
    assert not(x.is_sparse)
    assert len(x) == 0

# Generated at 2022-06-14 14:37:25.526041
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Schema, String, Integer
    from typesystem.fields import Boolean

    class User(Schema):
        id = Integer()
        name = String()
        active = Boolean(default=False)

    assert repr(User(id=1, name="Alice")) == "User(id=1, name='Alice', active=False)"
    assert repr(User(id=1, name="Alice", active=True)) == "User(id=1, name='Alice', active=True)"
    assert repr(User(name="Alice")) == "User([sparse], active=False)"
    assert repr(User(id=1, active=True)) == "User(id=1, [sparse], active=True)"

# Generated at 2022-06-14 14:37:26.593620
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert False


# Generated at 2022-06-14 14:37:30.501933
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        bar = Reference('baz')

    class Baz(Schema):
        pass
    definitions = SchemaDefinitions()
    set_definitions(Foo.fields['bar'], definitions)
    Foo(baz=Baz())
# test_set_definitions

# Generated at 2022-06-14 14:37:34.806554
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class B(Schema):
        x = Integer(default=42)

    class A(B):
        y = String()

    assert A.fields['x'] == Integer(default=42)
    assert A.fields['y'] == String()


# Generated at 2022-06-14 14:37:46.389963
# Unit test for constructor of class Schema
def test_Schema():
    import unittest
    from unittest import TestCase

    from typesystem.fields import String
    from typesystem import Schema, error_handler

    class Foo(Schema):
        name = String()

    def validate_with_error_handler(schema: Schema, value: object) -> None:
        error = error_handler(lambda: schema(value))
        if error is not None:
            raise error

    class SchemaTestCase(TestCase):
        def test_schema(self) -> None:
            foo = Foo(name="Foo")
            self.assertEqual(foo.name, "Foo")

            _, error = Foo.validate_or_error({})
            self.assertIn("name", error.messages()[0].path)


# Generated at 2022-06-14 14:37:53.494090
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    list_of_dict = [{'name':'a'}, {'name':'b'}, {'name':'c'}]
    for dict_item in list_of_dict:
        for dict_key in dict_item:
            assert dict_key in dict_item
            assert dict_item[dict_key] == dict_key


# Generated at 2022-06-14 14:38:02.287328
# Unit test for function set_definitions
def test_set_definitions():
    def test_field(field: Field, expected_definitions: SchemaDefinitions) -> None:
        definitions = SchemaDefinitions()
        set_definitions(field, definitions)
        assert definitions == expected_definitions

    test_field(Reference("Person"), SchemaDefinitions(Person={}))

# Generated at 2022-06-14 14:38:05.706390
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    schema = Schema()
    assert len(schema) == 0
    schema = Schema({"field1": "value1", "field2": "value2"})
    assert len(schema) == 2


# Generated at 2022-06-14 14:38:36.543782
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Error(Exception):
        pass
    class SubSchema1(Schema):
        param01 = Int(tags = ["request"], maximum = 20, required = True)
        param02 = String(tags = ["response"], max_length = 30)
    class SubSchema2(Schema):
        param03 = String(tags = ["request"], max_length = 30, required = True)
        param04 = Int(tags = ["response"], maximum = 20)
    class SubSchema3(Schema):
        param05 = String(tags = ["request"], max_length = 30, required = True)
        param06 = String(tags = ["response"], max_length = 30)
    class SubSchema4(Schema):
        param07 = String(tags = ["request"], max_length = 30, required = True)

# Generated at 2022-06-14 14:38:44.156868
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # A test for method __repr__ of class Schema
    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer()

    # Scenario 1
    # A test for method __repr__ of class Schema
    # Given
    person = Person(first_name='John', last_name='Doe', age=42)

    # When
    actual = repr(person)

    # Then
    assert actual == "Person(age=42, first_name='John', last_name='Doe')"

    # Scenario 2
    # A test for method __repr__ of class Schema
    # Given
    person = Person(first_name='John', last_name='Doe')

    # When
    actual = repr(person)

    # Then

# Generated at 2022-06-14 14:38:53.759549
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # This function will test the equality of two objects.
    class TestSchema(Schema):
        a = Field(primitive=str, default='def')
        b = Field(primitive=int)


    d1 = {'a':'abc','b': 1}
    d2 = TestSchema(d1)
    d3 = {'a':'abc'}
    d4 = TestSchema(d3)
    d5 = TestSchema(d1)
    assert d2 == d5
    assert not (d2 == d4)
    assert not (d2 == d1)


# Generated at 2022-06-14 14:38:58.104299
# Unit test for function set_definitions
def test_set_definitions():
    class Address(Schema):
        street = Field(str)
        city = Field(str)

    class Person(Schema):
        name = Field(str)
        address = Reference(Address)

    definitions = SchemaDefinitions()
    set_definitions(Person.fields["address"], definitions)

    assert definitions == {
        "Address": Address,
        "Person": Person
    }

# Generated at 2022-06-14 14:39:04.429982
# Unit test for function set_definitions
def test_set_definitions():
    ref = Reference(to="TestClass", default=None)
    definitions = {
        "TestClass": Schema({"name": Field(str, default="")}),
    }
    set_definitions(ref, definitions)
    assert ref.definitions == definitions
    assert ref.to == "TestClass"
    assert ref.target == Schema({"name": Field(str, default="")})

# Generated at 2022-06-14 14:39:09.708796
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class A(Schema):
        a = Array[str]
        b = Array[str]

    class B(Schema):
        a = Array[str]
        b = Array[str]
        c = Array[str]

    a = A(a=["a", "b"])
    assert len(a) == 1


# Generated at 2022-06-14 14:39:21.982597
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
  
    # Initialization
    schemascenario1fields = {}
    schemascenario1 = Schema(**schemascenario1fields)

    try:
        schemascenario1.__iter__()
        myoutput1 = "Pass"
    except:
        myoutput1 = "Fail"
    testoutput1 = ("test1test")
    assert myoutput1 == testoutput1

    # Initialization
    schemascenario2fields = {"fieldA": Array(items=String())}
    schemascenario2 = Schema(**schemascenario2fields)
    schemascenario2.fieldA = ["a", "b"]

    try:
        schemascenario2.__iter__()
        myoutput2 = "Pass"
    except:
        myoutput2 = "Fail"

# Generated at 2022-06-14 14:39:24.083346
# Unit test for constructor of class Schema
def test_Schema():
    assert not hasattr(Schema, "foo")
    assert Schema({"foo": 123})


# Generated at 2022-06-14 14:39:36.204760
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class A(Schema):
        a = Field(type="string")
        b = Field(type="string")
        c = Field(type="string")
        d = Field(type="string")

    class B(A):
        e = Field(type="string")
        f = Field(type="string")
        g = Field(type="string")
        h = Field(type="string")

    class C(B):
        i = Field(type="string")
        j = Field(type="string")
        k = Field(type="string")
        l = Field(type="string")

    assert len(A(a="1", b="2")) == 2
    assert len(B(a="1", b="2")) == 2
    assert len(C(a="1", b="2")) == 2


# Generated at 2022-06-14 14:39:48.771719
# Unit test for constructor of class Schema
def test_Schema():
    class PersonSchema(Schema):
        name = String()
        age = Integer()
        height = Float()
        alive = Boolean()
        fave_color = String(default='blue', max_length=10)

    # Test constructor of Schema class
    p = PersonSchema(name='John', age=35)
    assert p.name == 'John'
    assert p.age == 35
    # p.height is None
    assert p.alive is False
    assert p.fave_color == 'blue'

    # Test constructor - Errors
    with pytest.raises(TypeError):
        PersonSchema(name='John', age=35, height='5 feet 7 inches')


# Generated at 2022-06-14 14:40:13.443779
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Request(Schema):
        id = Field(format="integer")
        title = Field(format="string")

    req = Request(id=1, title="foo")
    assert req["id"] == 1
    assert req["title"] == "foo"
    assert req["id"] == req["id"]
    assert req["id"] != req["title"]
    assert req["id"] not in req


# Generated at 2022-06-14 14:40:24.384450
# Unit test for constructor of class Schema
def test_Schema():
    # Test for constructor with no arguments
    class TestSchema(Schema):
        test_field = Field()

    test_instance = TestSchema()
    assert hasattr(test_instance, "test_field")
    assert test_instance.test_field is None

    # Test for constructor with one argument
    test_dict = {"test_field": None}
    test_instance = TestSchema(test_dict)
    assert hasattr(test_instance, "test_field")
    assert test_instance.test_field is None

    test_dict = {"test_field": "test"}
    test_instance = TestSchema(test_dict)
    assert hasattr(test_instance, "test_field")
    assert test_instance.test_field == "test"

    # Test for constructor with multiple arguments
    test_instance = Test

# Generated at 2022-06-14 14:40:28.716722
# Unit test for function set_definitions
def test_set_definitions():

    class Author(Schema):
        name = String()

    class Book(Schema):
        author = Reference(Author)
        title = String()

    defn = SchemaDefinitions()

    set_definitions(Book.fields["author"], defn)

    assert defn == {'Author': Author}

# Generated at 2022-06-14 14:40:31.082570
# Unit test for function set_definitions
def test_set_definitions():

    class NewSchema(Schema):
        field = Reference("AnotherSchema", definitions=SchemaDefinitions())

    set_definitions(NewSchema.field, NewSchema.field.definitions)
    assert isinstance(NewSchema.field.definitions, SchemaDefinitions)

# Generated at 2022-06-14 14:40:35.246239
# Unit test for function set_definitions
def test_set_definitions():
    class Address(Schema):
        street = String()
        city = String()
    class Person(Schema):
        name = String()
        address = Reference(Address)
    definitions = SchemaDefinitions()
    set_definitions(Person.fields['address'], definitions)
    assert Person.fields['address'].definitions == definitions

# Generated at 2022-06-14 14:40:39.791775
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = String()
        age = Integer()

    p1 = Person(name='Pablo',age=23)
    p2 = Person(name='Pablo',age=23)
    assert p1 == p2


# Generated at 2022-06-14 14:40:49.748136
# Unit test for function set_definitions
def test_set_definitions():
    class DummyField(Field):
        pass
    class DummySchema(Schema):
        field = DummyField()
    
    dummy_field = DummyField()
    dummy_schema = DummySchema()
    definitions = SchemaDefinitions()
    
    set_definitions(dummy_field, definitions)
    set_definitions(dummy_schema, definitions)
    assert dummy_field.definitions == definitions
    assert dummy_schema.definitions == definitions
    assert dummy_schema.field.definitions == definitions
    with pytest.raises(AssertionError):
        set_definitions(dummy_schema, definitions)
    with pytest.raises(AssertionError):
        set_definitions(dummy_field, definitions)

# Generated at 2022-06-14 14:41:00.844815
# Unit test for constructor of class Reference
def test_Reference():
    from typing import Union
    from typesystem.fields import String
    from typesystem.schema import Schema

    class AddressSchema(Schema):
        street = String()
        city = String()
        zip = String()

    class PersonSchema(Schema):
        name = String()
        address = Reference(AddressSchema)

    a = AddressSchema(street='first', city='second', zip='third')
    p = PersonSchema(name='name', address=a)
    assert p.name == 'name'
    assert p.address == a
    assert p.address.street == 'first'
    assert p.address.city == 'second'
    assert p.address.zip == 'third'

# Generated at 2022-06-14 14:41:03.874341
# Unit test for constructor of class Reference
def test_Reference():
    assert isinstance(Reference('test'), Reference)
    assert Reference('test')._target_string == 'test'


# Generated at 2022-06-14 14:41:06.806294
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    def schema_iter():
        class ExampleSchema(Schema):
            foo = String()

        schema = ExampleSchema()
        return list(schema)
    assert schema_iter() == []

# Generated at 2022-06-14 14:41:48.283503
# Unit test for constructor of class Schema
def test_Schema():
	class Person(Schema):
		name = String()
	Person({"name":"sam"})



# Generated at 2022-06-14 14:41:50.588478
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Test if two objects of class Schema are equal
    pass


# Generated at 2022-06-14 14:41:56.605091
# Unit test for constructor of class Reference
def test_Reference():
    error = Reference("test", "definitions")
    assert error.target == "test"
    assert Reference("test", "definitions").to == "test"
    assert error.errors == {"null": "May not be null."}
    assert error.definitions == "definitions"
    assert error.to == "test"
    assert error.target_string == "test"
    assert error.target == "definitions"


# Generated at 2022-06-14 14:42:01.963471
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    assert Schema({"a": 1}).__repr__() == "Schema(a=1)"
    assert Schema({"a": 1, "b": 2}).__repr__() == "Schema(a=1, b=2)"
    assert Schema({"a": 1}).__repr__() == "Schema(a=1)"
    assert Schema({"a": 1, "b": 2}).__repr__() == "Schema(a=1, b=2)"


# Generated at 2022-06-14 14:42:09.054867
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class SubSchema(Schema):
        pass

    class TestSchemaMetaclass(Schema):
        sub = SubSchema

        sub_with_default = SubSchema(default={})

    fields = TestSchemaMetaclass.fields
    assert fields.keys() == {"sub", "sub_with_default"}
    assert isinstance(fields["sub"], Reference)
    assert isinstance(fields["sub_with_default"], Reference)


# Generated at 2022-06-14 14:42:18.495776
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field1 = Reference(name="person", to="Person")
    field2 = Array(name="people", items=Reference(name="children", to="Child"))
    object_field = Object(name="object", properties={"person": Reference(name="person", to="Person")})
    field3 = Array(name="nested", items=object_field)
    set_definitions(field1, definitions)
    set_definitions(field2, definitions)
    set_definitions(field3, definitions)
    assert field1.definitions == definitions
    assert field2.items.definitions == definitions
    assert field3.items.properties["person"].definitions == definitions


# Generated at 2022-06-14 14:42:26.497990
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    object_fields = dict(
        a=Field(),
        b=Field(),
        c_ref=Reference('C', definitions),
        d_ref=Reference('D', definitions),
        e_ref=Reference('E', definitions),
        f=Field(default='f'),
    )
    set_definitions(Object(properties=object_fields), definitions)
    assert definitions['C'] == Field()
    assert definitions['D'] == Field()
    assert definitions['E'] == Field()
    assert set(definitions.keys()) == set('CDE')
    assert object_fields['c_ref'].definitions is not None
    assert object_fields['c_ref'].definitions is definitions
    assert object_fields['d_ref'].definitions is not None

# Generated at 2022-06-14 14:42:32.394823
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class MySchema(Schema):
        field1 = Field()
        field2 = Field()

    obj = MySchema(field1=5, field2=10)
    print('{!r}'.format(len(obj)))
    assert len(obj) == 2
    print('PASS')



# Generated at 2022-06-14 14:42:40.915785
# Unit test for constructor of class Reference
def test_Reference():
    from . import Reference
    a = Reference("asdf")
    assert a.target_string == "asdf"
    assert a.definitions is None
    assert a.allow_null is False
    assert a._target_string == "asdf"
    assert a._target is None
    assert a.to == "asdf"
    assert a.errors == {"null": "May not be null."}
    assert a.constraints == ()
    assert a.required is False
    assert a.has_default() is False
    assert a.default_value is None
    assert a.validate(None) is None
    assert a.serialize(None) is None
# END Unit test for constructor of class Reference

# Generated at 2022-06-14 14:42:45.854141
# Unit test for method __len__ of class Schema
def test_Schema___len__():
   # Test if the length of attributes is returned correctly

   # An object of the class
   obj = Schema()
   # Default nbr of attributes for objects of this class
   expected = 2

   got = len(obj)

   assert(got == expected)


# Generated at 2022-06-14 14:43:46.914786
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import numpy as np
    # Test when the class attribute self.fields of the two instances are
    # different
    class Schema0(Schema):
        a = Field(type_=float, default=1.1)
    class Schema1(Schema):
        b = Field(type_=float, default=1.1)
    a = Schema0()
    b = Schema1()
    assert a == b is False
    # Test when the class attribute self.fields of the two instances are
    # the same
    class Schema2(Schema):
        a = Field(type_=float, default=1.1)
    class Schema3(Schema):
        a = Field(type_=float, default=1.1)
    a = Schema2()
    b = Schema3()
    assert a

# Generated at 2022-06-14 14:43:52.378285
# Unit test for function set_definitions
def test_set_definitions():
    class Definition(Schema):
        pass

    def make_definition(name):
        class Definition_name(Schema):
            pass
    
        Definition_name.__name__ = name
        return Definition_name
    
    definition = make_definition('definition1')

    class definition2(Schema):
        definition = Reference(to='definition1')
        definition2 = Reference(to=definition)

    definition = make_definition('definition1')


# Generated at 2022-06-14 14:44:01.952824
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer

    class ExampleSchema(Schema):
        a = Integer(minimum=0)
        b = Integer(minimum=0)

    # First check if 2 instances of ExampleSchema class are equal.
    example = ExampleSchema(a=1, b=1)
    example2 = ExampleSchema(a=1, b=1)
    print(example == example2)

    # Check if the instance is equal to an instance of a different class
    # (which is not a subclass of ExampleSchema class).
    print(example == 123)

    # Check if the instance is equal to an instance of a different class
    # (which is a subclass of ExampleSchema class).
    print(example == ExampleSchema(a=1, b=0))

    # Check if the instance is equal to a dictionary.
    print

# Generated at 2022-06-14 14:44:03.603800
# Unit test for constructor of class Reference
def test_Reference():
    class Foo(Schema):
        bar = Reference(Object)
    foo = Foo(bar={})


# Generated at 2022-06-14 14:44:07.787522
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class T(Schema):
        field_0 = Field()
        field_1 = Field()

    schema = T({'field_0': 'hello', 'field_1': 'world'})

    assert schema['field_0'] == 'hello'
    assert schema['field_1'] == 'world'



# Generated at 2022-06-14 14:44:19.058092
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # 1. test whether __iter__ works as expected
    class Person(Schema):
        name = String()
        age = Int()
    p = Person(name="foo", age=20)
    assert iter(p) == iter(('name', 'age'))
    assert list(p) == list(('name', 'age'))
    assert set(p) == {'name', 'age'}
    assert len(p) == 2
    p = Person(name="foo", age=None)
    assert iter(p) == iter(('name', ))
    assert list(p) == list(('name', ))
    assert set(p) == {'name'}
    assert len(p) == 1
    
    # 2. test whether __getitem__ works as expected
    class Person(Schema):
        name = String()