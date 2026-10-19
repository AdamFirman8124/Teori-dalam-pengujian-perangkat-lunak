

# Generated at 2022-06-14 14:34:42.619357
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert issubclass(SchemaMetaclass, ABCMeta)
    class Album(Schema):
        title = Field(str)
    assert dir(Album) == ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fields', 'make_validator', 'validate', 'validate_or_error']


# Generated at 2022-06-14 14:34:43.834420
# Unit test for function set_definitions
def test_set_definitions():
    set_definitions(Reference("Schema"), SchemaDefinitions())

# Generated at 2022-06-14 14:34:50.123358
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from typesystem import Integer, String

    class TestSchema(Schema):
        name = String()
        age = Integer()

    test = TestSchema(name="Bob", age=20)
    assert "name" in test
    assert "age" in test
    assert "age" in test.__dict__
    assert test["name"] == "Bob"
    assert test["age"] == 20


# Generated at 2022-06-14 14:34:57.693725
# Unit test for constructor of class Schema
def test_Schema():
    import unittest
    class TestSchema(Schema):
        test_fields = {}

        def __init__(self, *args, **kwargs):
            self.test_fields = TestSchema.test_fields
            super(Schema, self).__init__(*args, **kwargs)
            self.test_fields = TestSchema.test_fields

    # Test for the correct initialization of the class' constructor
    TestSchema({"TestSchema": TestSchema})
    TestSchema(test_fields=TestSchema.test_fields)

    class TestSchema2(TestSchema):
        def __init__(self, *args, **kwargs):
            super(Schema, self).__init__(*args, **kwargs)

    # Test for the correct initialization of the class' constructor
    TestSchema2

# Generated at 2022-06-14 14:35:09.666643
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from datetime import datetime
    from typesystem.fields import Boolean, Date, DateTime, Float, Integer, String
    from typesystem.types import Schema

    class Point(Schema):
        x = Float()
        y = Float()

    class Person(Schema):
        name = String()
        age = Integer()
        best_friend = Reference(to="Point")  # type: ignore
        is_cool = Boolean(default=False)

    person = Person(
        name="James",
        age=30,
        best_friend=Point(x=1, y=2),
    )
    serialized = person.serialize()

# Generated at 2022-06-14 14:35:13.311928
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import typesystem
    class Person(typesystem.Schema):
        first_name: str
        last_name: str
    person = Person(first_name='Mark')
    
    for key in person:        
        print(key, person[key])


# Generated at 2022-06-14 14:35:22.012667
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
   # Test Schema with lots of fields
   class SchemaNew(Schema):
      field1 = String(pattern="abc")
      field2 = Boolean()
      field3 = Date()
      field4 = DateTime()
      field5 = Array(items=String())
      field6 = Array(items=Date())
      field7 = Array(items=String())
      field8 = Array(items=Date())
      field9 = Array(items=String())
      field10 = Array(items=Date())
      field11 = Array(items=String())
      field12 = Array(items=Date())
      field13 = Array(items=String())
      field14 = Array(items=Date())
      field15 = Array(items=String())
      field16 = Array(items=Date())
      field17 = Array(items=String())
      field18

# Generated at 2022-06-14 14:35:23.892671
# Unit test for function set_definitions
def test_set_definitions():
    class TempSchema(Schema): # type: ignore
        pass

    definitions = SchemaDefinitions()
    set_definitions(TempSchema, definitions)

# Generated at 2022-06-14 14:35:28.289548
# Unit test for function set_definitions
def test_set_definitions():
    class User(Schema):
        pass

    definitions = SchemaDefinitions()
    field = Reference(User, definitions=definitions)
    assert field.definitions is definitions
    assert str(field.to) == "User"


# Generated at 2022-06-14 14:35:34.654139
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        a = 1
        b = 2
        c = 3
    schema = TestSchema(a=1, b=2, c=3)
    assert repr(schema) == "TestSchema(a=1, b=2, c=3)"
    schema = TestSchema(a=1, b=2)
    assert repr(schema) == "TestSchema(a=1, b=2) [sparse]"


# Generated at 2022-06-14 14:35:47.466939
# Unit test for function set_definitions
def test_set_definitions():
    new_defs = SchemaDefinitions()
    class Person(Schema):
        name = Reference('Name')
    class Name(Schema):
        first = Field()
        last = Field()

    set_definitions(Person.fields['name'], new_defs)
    assert Person.fields['name'].definitions == new_defs


# Generated at 2022-06-14 14:35:59.809422
# Unit test for constructor of class Reference
def test_Reference():
    # No definition.
    with pytest.raises(AssertionError, match=r"String reference missing 'definitions\.'."):
        Reference("user")

    schema_dict = {
        "user": Schema("user"),
    }
    class TestSchema(Schema):
        foo = Reference("user", definitions=schema_dict)

    s = TestSchema("foo")
    assert s.foo == "foo"
    assert s.fields["foo"].target == schema_dict["user"]
    assert s.fields["foo"].target_string == "user"

    class UserSchema(Schema):
        name = String()
        email = String()

    class TestSchema(Schema):
        foo = Reference(UserSchema)


# Generated at 2022-06-14 14:36:04.378063
# Unit test for function set_definitions
def test_set_definitions():

    class Definitions(SchemaDefinitions):
        pass
    definitions = Definitions()

    class MyObject(Schema):
        foo = Reference(to="AnotherObject", definitions=definitions)

    class AnotherObject(Schema):
        bar = Reference(to="YetAnotherObject", definitions=definitions)

    class YetAnotherObject(Schema):
        baz = Reference(to="YetAnotherObject", definitions=definitions)


# Generated at 2022-06-14 14:36:08.341913
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        foo = Field(int, required=False)
        bar = Field(str, required=False)
    schema = TestSchema(foo=123, bar=456)
    assert schema.foo == 123
    assert schema.bar == 456

# Generated at 2022-06-14 14:36:13.174175
# Unit test for function set_definitions
def test_set_definitions():
    class Thing(Schema):
        first = Field()
        second = Reference("OtherThing")

    class OtherThing(Schema):
        third = Field()
        fourth = Reference("Thing")

    definitions = SchemaDefinitions()
    set_definitions(Thing, definitions)
    assert definitions == {'Thing': Thing, 'OtherThing': OtherThing}


# Unit tests for classes Schema and Reference

# Generated at 2022-06-14 14:36:17.072695
# Unit test for function set_definitions
def test_set_definitions():
    assert Reference(int).allow_null is False
    assert Reference(int).allow_null is False
    assert Reference(int, allow_null=True).allow_null is True
    assert Reference(int, allow_null=False).allow_null is False
    assert Reference(int, allow_null=True).allow_null is True

# Generated at 2022-06-14 14:36:22.560489
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # Testing the following statement
    # len(Schema)

    # Real object: type 'Schema'
    assert len(Schema) == 0, 'Expected len(Schema) to be 0, but it is actually %d' % (len(Schema))
    # Expected output: 0


# Generated at 2022-06-14 14:36:28.564639
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Foo(Schema):
        one = Field()
        two = Field()
        three = Field()
    foo = Foo({'one': 1, 'two': 2, 'three': 3})
    assert sorted(foo.__iter__()) == ['one', 'two', 'three']
    foo = Foo(one = 1, two = 2)
    assert sorted(foo.__iter__()) == ['one', 'two']


# Generated at 2022-06-14 14:36:29.826544
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        a = Field()
    s = TestSchema({"a": 1})
    

# Generated at 2022-06-14 14:36:38.733594
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    schema = Schema()
    # Check that the display of an empty class is correct
    assert repr(schema) == "Schema()"
    assert isinstance(schema, Schema)
    assert issubclass(type(schema), Schema)
    schema = Schema({"value": 1})
    assert repr(schema) == "Schema(value=1)"
    assert isinstance(schema, Schema)
    assert issubclass(type(schema), Schema)
    schema = Schema(value=1)
    assert repr(schema) == "Schema(value=1)"
    assert isinstance(schema, Schema)
    assert issubclass(type(schema), Schema)
    schema = Schema({"value": 1, "other_value": 2})

# Generated at 2022-06-14 14:37:20.976227
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Schema, String, Integer

    class Person(Schema):
        name = String()
        age = Integer()


    person = Person(name='John', age=22)
    assert repr(person) == "Person(name='John', age=22)"

    person = Person({'name': 'John', 'age': 22})
    assert repr(person) == "Person(name='John', age=22)"



# Generated at 2022-06-14 14:37:26.837697
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Test if the two values are equal
    # This is tested in class TestBasicSchema
    # Test if the two values are not equal
    # This is tested in class TestBasicSchema
    # Test if the two values are not equal, because they're of different type
    # This is tested in class TestBasicSchema
    return



# Generated at 2022-06-14 14:37:32.107958
# Unit test for function set_definitions
def test_set_definitions():
    class DogSchema(Schema):
        weight = Number()

    class CatSchema(Schema):
        breed = Text(max_length=50)

    class PersonSchema(Schema):
        animal = Reference(to=DogSchema)
    
    class PetSchema(Schema):
        animal = Reference(to=DogSchema)
        person = Reference(to=PersonSchema)

    class_list = [DogSchema, CatSchema, PersonSchema, PetSchema]
    definitions = SchemaDefinitions()
    for cls in class_list:
        set_definitions(cls, definitions)
    assert definitions[DogSchema.__name__] == DogSchema
    assert definitions[CatSchema.__name__] == CatSchema
    assert definitions[PersonSchema.__name__] == PersonSche

# Generated at 2022-06-14 14:37:43.724481
# Unit test for function set_definitions
def test_set_definitions():
    """
    Test that definitions get passed to nested references.
    """
    class A(Schema):
        b = Reference("B")

    class B(Schema):
        pass

    definitions = SchemaDefinitions()

    # Recursively set the definitions that string-referenced `Reference` fields
    # should use.
    set_definitions(A.fields["b"], definitions)

    # Check that the definitions have been added.
    assert definitions["B"] == B

    # Check that the definition has been added to the nested Reference.
    assert A.fields["b"].definitions == definitions

    # Check that the definition has been added for the nested Reference.
    assert A.fields["b"].target == B


# Generated at 2022-06-14 14:37:47.879291
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import typesystem

    class A(Schema):
        a = typesystem.String()
        b = typesystem.String()

    a = A(a='foo', b='bar')

    assert len(a) == 2


# Generated at 2022-06-14 14:37:59.135458
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class SimpleSchema(Schema):
        pass

    assert SimpleSchema.fields == {}

    class Person(Schema):
        id = Field()
        name = Field()
        age = Field()

    assert Person.fields == {
        "id": Field(),
        "name": Field(),
        "age": Field(),
    }

    assert Person.make_validator() == Object(
        properties={
            "id": Field(),
            "name": Field(),
            "age": Field(),
        },
        required=["id", "name", "age"],
        additional_properties=None,
    )


# Generated at 2022-06-14 14:38:05.407372
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    definitions = SchemaDefinitions()

    class ClassA(Schema):
        required = Field(description="description of this field")
        optional = Field(
            description="description of this field", has_default=True, default=1
        )

    class ClassB(Schema):
        reference = Reference(ClassA, definitions=definitions)

    obj = ClassB(reference={'required': 'abc'})
    assert obj.__iter__() == ['reference']

# Generated at 2022-06-14 14:38:09.503738
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    definitions["schema1"] = "schema1"
    definitions["schema2"] = "schema2"
    definitions["schema3"] = "schema3"
    definitions["schema4"] = "schema4"

    # Set references for schema1
    schema1_fields = {
        "field1": Reference("schema2", definitions=definitions),
        "field2": Reference("schema3", definitions=definitions),
        "field3": Reference("schema4", definitions=definitions)
    }
    schema1 = SchemaMetaclass("schema1", (), schema1_fields)

    # Set references for schema2

# Generated at 2022-06-14 14:38:21.401510
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        item = Field(type="string")
        value = Field(type="integer")
        flag = Field(type="boolean")
    instance = MySchema(item="foo", value=5)

    # Check that __iter__ works when Schema has all fields
    def test_check_iter_all():
        print("Testing __iter__ with all fields")
        # https://docs.python.org/3/tutorial/controlflow.html#comparing-sequences-and-other-types
        assert list(instance) == ['item', 'value', 'flag']

    test_check_iter_all()

    # Check that __iter__ works when Schema has some fields
    def test_check_iter_some():
        print("Testing __iter__ with some fields")
        # https://docs

# Generated at 2022-06-14 14:38:30.321084
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String
    from unittest.mock import MagicMock
    from unittest.mock import Mock
    from unittest.mock import patch
    from unittest.mock import sentinel

    class MockSchema(Schema):
        field1 = String(max_length=10)
        field2 = String(max_length=20)
        field3 = String(max_length=30)

        def __init__(self, *args, **kwargs):
            # mock part of constructor
            for key, value in kwargs.items():
                setattr(self, key, value)

    def mocked_validate(value, *, strict=False):
        return value


# Generated at 2022-06-14 14:39:05.090864
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.types import String

    class Person(Schema):
        first_name = String(max_length=100)
        last_name = String(max_length=100)
        age = String(max_length=100)

    data = Person.validate({'first_name': 'John', 'last_name': 'Doe', 'age': '26'})
    for key in data:
        print(key)



if __name__ == '__main__':
    test_Schema___iter__()

# Generated at 2022-06-14 14:39:10.590383
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        pass
    assert Schema.__eq__(TestSchema, None) == False
    assert Schema.__eq__(TestSchema, Schema()) == True
    assert Schema.__eq__(TestSchema, 5) == False
    assert Schema.__eq__(TestSchema, TestSchema()) == True


# Generated at 2022-06-14 14:39:17.947514
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        field1: int = 1
        field2: int = 2

    schema = TestSchema(field1=2)
    assert(len(schema) == 1)

    class TestSchema(Schema):
        field1: int = 1
        field2: int = 2

    schema = TestSchema(field2=2)
    assert(len(schema) == 1)


# Generated at 2022-06-14 14:39:25.446470
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Foo(Schema):
        foo = String(min_length=1)
        bar = String(max_length=10)

    objA = Foo(foo='A', bar='B')
    objB = Foo(foo='A')
    objC = Foo(foo='A', bar='B', **{'baz': 'C'})
    assert objA == objA
    assert objA != objB
    assert objA != objC
    assert objA != 42
    assert objA != 'A'



# Generated at 2022-06-14 14:39:36.409120
# Unit test for function set_definitions
def test_set_definitions():
    class Empty(object):
        ...

    class Foo(Schema):
        a = Field()

    class Bar(Schema):
        b = Reference("baz", foo=Empty())

    class Baz(Schema):
        c = Reference("foo")

    definitions = SchemaDefinitions()

    set_definitions(Foo.fields["a"], definitions)
    set_definitions(Bar.fields["b"], definitions)
    set_definitions(Baz.fields["c"], definitions)

    assert Baz.fields["c"].definitions == definitions
    assert Baz.fields["c"].target_string == "foo"
    assert Baz.fields["c"].target == Foo

    assert Bar.fields["b"].definitions == definitions
    assert Bar.fields["b"].target_string == "baz"

# Generated at 2022-06-14 14:39:37.323572
# Unit test for constructor of class Reference
def test_Reference():
    _ = Reference(to='',definitions='')

# Generated at 2022-06-14 14:39:48.768959
# Unit test for function set_definitions
def test_set_definitions():
    fields = {
        "str_field": Field(type="string"),
        "obj_field": Object(properties={"string_field": Field(type="string")}),
        "arr_field": Array(items=Field(type="string")),
        "ref_field": Reference("StringReferencingSchema"),
    }
    class StringReferencingSchema(Schema):
        fields = fields

    definitions = SchemaDefinitions()
    set_definitions(fields["ref_field"], definitions)
    assert fields["ref_field"].definitions == definitions
    assert fields["obj_field"].properties["string_field"].definitions == definitions
    assert fields["arr_field"].items.definitions == definitions

# Generated at 2022-06-14 14:39:51.137599
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Class(Schema):
        prop = "value"
    assert list(Class()) == ["prop"]

# Generated at 2022-06-14 14:39:57.914955
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class User(Schema):
        id = typesystem.Integer()
        name = typesystem.String()
        active = typesystem.Boolean(default=True)
        age = typesystem.Integer(required=False)

    user = User(id=1, name="Bob")
    assert len(user) == 3
    assert sorted(list(user)) == ["active", "id", "name"]



# Generated at 2022-06-14 14:40:02.150935
# Unit test for constructor of class Schema
def test_Schema():
    print('Function: test_Schema')
    class Person(Schema):
        name = Array(items=str)
        age = int

    person = Person(name=["John", "Doe"], age=24)
    print(person)


# Generated at 2022-06-14 14:40:55.578316
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert False


# Generated at 2022-06-14 14:41:03.105990
# Unit test for constructor of class Reference
def test_Reference():
    import json

    class TestSchema1(Schema):
        pass

    class TestSchema2(Schema):
        ref = Reference("TestSchema1")

    my_schema = TestSchema2()
    schema_json = json.dumps(my_schema)
    obj_json = json.loads(schema_json)
    # Do not raise any exceptions


# Generated at 2022-06-14 14:41:05.745051
# Unit test for constructor of class Schema
def test_Schema():
    # Create an instance of class Schema
    schema = Schema()
    schema.__init__("String")
    # Check whether the instance is correctly instantiated
    assert isinstance(schema, Schema)
    # No return, unit test passed
    return

# Generated at 2022-06-14 14:41:16.595174
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class User(Schema):
        name = String()

    class Comment(Schema):
        name = String()

    class BlogPost(Schema):
        author = String()
        title = String()
        content = String()
        comments = Array(items=Reference(Comment))

    assert User.fields['name'] == String()
    assert Comment.fields['name'] == String()
    assert BlogPost.fields['author'] == String()
    assert BlogPost.fields['title'] == String()
    assert BlogPost.fields['content'] == String()
    assert BlogPost.fields['comments'] == Array(items=Reference(Comment))
    assert BlogPost.fields['comments'].items.target == Comment


# Generated at 2022-06-14 14:41:22.017186
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        b = Field()
        a = Field()

    o = TestSchema(a=1, b=2)
    assert len(o) == 2
    assert len(o) == 2
    assert len(o) == 2


# Generated at 2022-06-14 14:41:30.963714
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        id = String()
        name = String()
        age = Integer()
        # sex = String()
        # test = String()
        # tes = String()
        # te = String()
        # t = String()
    a = TestSchema()
    a.id = "1"
    a.name = "2"
    a.age = 1
    # a.sex = "1"
    # a.test = "1"
    # a.tes = "1"
    # a.te = "1"
    # a.t = "1"
    # print(a)
    print([key for key in a])

# Generated at 2022-06-14 14:41:43.377123
# Unit test for constructor of class Reference
def test_Reference():
    class NoDefinitions(Reference):
        def __init__(self):
            super().__init__("Test")
    try:
        NoDefinitions()
    except AssertionError as e:
        assert e.args[0] == "String reference missing 'definitions'."
    else:
        assert False

    class WithDefinitions(Reference):
        def __init__(self, definitions):
            super().__init__("Test", definitions=definitions)

    class Test(Schema):
        field = Field()
    definitions = SchemaDefinitions(Test=Test)
    WithDefinitions(definitions)

    class WithTarget(Reference):
        def __init__(self):
            super().__init__(Test)
    WithTarget()

if __name__ == "__main__":
    test_Reference()

# Generated at 2022-06-14 14:41:52.622911
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert len(Schema()) == 0
    assert len(Schema({})) == 0
    assert len(Schema({"x": "a"})) == 1
    assert len(Schema(x="a")) == 1
    assert len(Schema({"x": "a", "y": "b"})) == 2
    assert len(Schema({"x": "a", "y": "b", "z": "c"}, z="z")) == 3
    assert len(Schema({"x": "a", "y": "b"}, z="z")) == 3


# Generated at 2022-06-14 14:41:57.526627
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Example(Schema):
        a = Field(type="integer")
        b = Field(type="string")

    ex_instance = Example(a=1, b="b")
    ex_instance_1 = Example(a=1)

    assert list(ex_instance) == ['a', 'b']
    assert list(ex_instance_1) == ['a']



# Generated at 2022-06-14 14:42:01.580828
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MyTestSchema(Schema):
        field_one = String()
        field_two = String()
    
    my_test_schema = MyTestSchema(
        field_one="foo",
        field_two="bar",
    )
    assert all(iter(my_test_schema) == ["field_one", "field_two"])
    