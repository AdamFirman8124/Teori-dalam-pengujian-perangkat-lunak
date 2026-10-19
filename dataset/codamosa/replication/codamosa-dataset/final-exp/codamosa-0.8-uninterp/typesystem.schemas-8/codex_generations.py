

# Generated at 2022-06-14 14:34:48.543485
# Unit test for function set_definitions
def test_set_definitions():
    class TestSchema(Schema):
        prop_1 = Reference("TestChildSchema", description="Prop 1")

    TestSchema.__metaclass__("Test", (), {"fields": TestSchema.fields}, SchemaDefinitions())

# Generated at 2022-06-14 14:34:55.480767
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    '''
    Unit test for method __iter__ of class Schema
    '''
    from typesystem.primitives import String
    class Person(Schema):
        name = String()
        age = String()
        city = String()

    p = Person(age = "16", name = "Sophie")
    l = list(p)
    assert len(l) == 2
    assert 'name' in l
    assert 'age' in l
    assert 'city' not in l



# Generated at 2022-06-14 14:34:57.200355
# Unit test for constructor of class Schema
def test_Schema():
    class Model(Schema):
        test = Field(1)

    test = Model({"test": 2})
    assert test.test == 2

# Generated at 2022-06-14 14:35:03.606579
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import typesystem
    class User(typesystem.Schema):
        name = typesystem.String(max_length=100)
        email = typesystem.String(max_length=100)
    obj = User(name="John Doe", email="jd@example.com")
    assert obj == User(name="John Doe", email="jd@example.com")


# Generated at 2022-06-14 14:35:09.285072
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    class BookSchema(Schema):
        title = Field()
        author = Reference("AuthorSchema")

    class AuthorSchema(Schema):
        name = Field()

    assert definitions == {}
    set_definitions(BookSchema.author, definitions)
    assert definitions == {
        "BookSchema": BookSchema,
        "AuthorSchema": AuthorSchema,
    }

# Generated at 2022-06-14 14:35:12.854563
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Book(Schema):
        title = Field(type="string")
        author = Field(type="string")
        publish_year = Field(type="integer")
    
    book = Book(title="Hello, world!")
    assert len(book) == 1


# Generated at 2022-06-14 14:35:15.693542
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    data = {
        'a': 1,
        'b': 2
    }
    schema = Schema(**data)
    schema1 = Schema(**data)

    assert schema == schema1



# Generated at 2022-06-14 14:35:16.713112
# Unit test for constructor of class Schema
def test_Schema():
    s = Schema()


# Generated at 2022-06-14 14:35:19.245620
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Person(Schema):
        name = Field(type="string", min_length=2)
        age = Field(type="integer", minimum=0)

    # Unit test for method __new__ of class Reference

# Generated at 2022-06-14 14:35:21.566657
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
  def Schema___iter__(self):
    for key in self.fields:
      if hasattr(self, key):
        yield key
  return Schema___iter__

# Generated at 2022-06-14 14:35:37.537846
# Unit test for method validate of class Reference
def test_Reference_validate():
    class Primitives(Schema):
        a = Reference(int)
        b = Reference(float)
        c = Reference(str)

    class MyError(Exception):
        pass

    class SomeSchema(Schema):
        x = Reference(Primitives, required=True)

        def mutate(self, data):
            if "x" not in data:
                raise MyError(data)

    def test_Reference_validate_1():
        try:
            assert SomeSchema.validate_or_error({"x": {"a": 1, "b": 2.22, "c": "hello"}}).error is None
        except:
            pass

# Generated at 2022-06-14 14:35:43.127135
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    @add_docstring_from_file("./test_Schema_docstring.txt")
    class TestSchema(Schema):
        field1 = Field(type="string")
        field2 = Field(type="string")
        field3 = Field(type="string")
    expected_result = ["field1", "field2", "field3"]
    result = list(TestSchema(field1 = "field1", field2 = "field2", field3 = "field3"))
    assert result == expected_result


# Generated at 2022-06-14 14:35:49.232230
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    Field.counter = 0
    o1 = Schema(argument_1=String(max_length=8, min_length=2), argument_2=Integer(min_value=5, max_value=10))
    o2 = Schema(argument_1=String(max_length=8, min_length=2), argument_2=Integer(min_value=5, max_value=10))
    assert o1.__repr__() == "Schema(argument_1='', argument_2=None)"
    assert o2.__repr__() == "Schema(argument_1='', argument_2=None)"
    assert o1 == o2


# Generated at 2022-06-14 14:35:54.398299
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Object1(Schema):
        a = Field()
        b = Field()
        c = Field()

    obj1 = Object1(a=1, b=2)
    assert len(obj1) == 2
    assert ['a', 'b'] == sorted(obj1)


# Generated at 2022-06-14 14:36:00.765660
# Unit test for function set_definitions
def test_set_definitions():
    class Def(Object):
        pass

    class Ref(Reference):
        pass

    class Nested(Array):
        items = [String, Ref]

    class A(Schema):
        field = Nested
        definitions = None
    
    set_definitions(field=A.field, definitions=SchemaDefinitions())
    assert isinstance(A.field.items[1].definitions, SchemaDefinitions)

# Generated at 2022-06-14 14:36:04.379963
# Unit test for function set_definitions
def test_set_definitions():
    schema_definitions = SchemaDefinitions()
    schema_definitions["bar"] = "baz"

    class Foo(Schema):
        hello = Reference("bar")

    set_definitions(Foo.fields["hello"], schema_definitions)
    assert Foo.fields["hello"].definitions is schema_definitions

# Generated at 2022-06-14 14:36:10.256922
# Unit test for function set_definitions
def test_set_definitions():
    """
    Given a schema without definitions, we should be able to set them,
    and the nested references should all be updated.
    """
    class Address(Schema):
        street = String(required=True)
        city = String(required=True)
        country = String(required=True)

    class Person(Schema):
        name = String(required=True)
        age = Integer(required=True)
        address = Reference(to=Address, required=True)

    class World(Schema):
        age = Integer(required=True)
        people = Array(items=Reference(Person), required=True)

    definitions = SchemaDefinitions()
    set_definitions(World, definitions)
    assert definitions["Address"] == Address
    assert definitions["Person"] == Person
    assert definitions["World"] == World

# Generated at 2022-06-14 14:36:19.283684
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from .models import TestSchema
    from .models import TestSchema2
    from typesystem.fields import String
    data = TestSchema()
    assert list(data) == ['str_field']
    data = TestSchema(str_field = 'test')
    assert list(data) == ['str_field']
    data = TestSchema(str_field = 'test', int_field = 1)
    assert list(data) == ['str_field', 'int_field']

    data = TestSchema2()
    assert list(data) == ['str_field2']
    data = TestSchema2(str_field2 = 'test')
    assert list(data) == ['str_field2']
    data = TestSchema2(str_field2 = 'test', int_field2 = 1)

# Generated at 2022-06-14 14:36:31.191366
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from random import choice, randrange
    import sys
    import types
    import pytest
    from typesystem import error_code, types

    class Person(types.Schema):
        name = types.String(max_length=10)
        age = types.Integer(minimum=10, maximum=20)
        gender = types.String()

    def __repr__(self):
        class_name = self.__class__.__name__
        arguments = {
            key: getattr(self, key) for key in self.fields.keys() if hasattr(self, key)
        }
        argument_str = ", ".join(
            [f"{key}={value!r}" for key, value in arguments.items()]
        )
        sparse_indicator = " [sparse]" if self.is_sparse else ""


# Generated at 2022-06-14 14:36:39.577795
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class TestSchema(Schema):
        a = Array(of=String())
        b = Integer(minimum=1)
        d = String()
        g = Integer(minimum=1)

    test_schema = TestSchema(a=['a'], b=3, d='c', g=3)
    assert test_schema == TestSchema({'a': ['a'], 'b': 3, 'd': 'c', 'g': 3})
    assert test_schema.a == ['a']
    assert test_schema.b == 3
    assert test_schema.d == 'c'
    assert test_schema.g == 3
    assert test_schema.is_sparse == False
    assert not hasattr(test_schema, 'f')

# Generated at 2022-06-14 14:37:01.788013
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        foo = String(max_length=4)
        bar = Integer(minimum=1, maximum=2)

    obj = {"foo": "abc", "bar": 1}
    schema = MySchema(**obj)

    keys = []

    for key in schema:
        keys.append(key)

    assert keys == ["foo", "bar"]



# Generated at 2022-06-14 14:37:03.841760
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    """Test for method __len__ of class Schema"""
    # Test
    assert(Schema({'data': 12}).__len__() == 1)


# Generated at 2022-06-14 14:37:08.038119
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    """
    Test for method Schema.__getitem__
    """
    # class definition for testing
    class Person(Schema):
        name = String()
    # test cases
    # case 1
    person = Person(name = "Jane Doe")
    assert person['name'] == "Jane Doe"



# Generated at 2022-06-14 14:37:19.438439
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Test if the method __getitem__ of class Schema work correctly
    
    sample_data = {"id": "bca27d",
                    "author": "joseportela",
                    "source_url_html": "https://github.com/toddmotto/public-apis",
                    "total_upvotes": 633,
                    "total_comments": 2}

    schema_data = {
            "id": typesystem.String(required=True),
            "author": typesystem.String(required=True),
            "source_url_html": typesystem.String(required=True),
            "total_upvotes": typesystem.Integer(required=True),
            "total_comments": typesystem.Integer(required=True)
        }
    
    # Create sample

# Generated at 2022-06-14 14:37:26.304333
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchemaLen(Schema):
        name = String()
    assert len(TestSchemaLen({'name': 'a'})) == 1
    assert len(TestSchemaLen({})) == 0
    assert len(TestSchemaLen()) == 0
    assert len(TestSchemaLen({'name': "a", 'age': 1})) == 1


# Generated at 2022-06-14 14:37:32.502418
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        a = Reference("Bar")

    class Bar(Schema):
        b = Reference("Foo")

    definitions = SchemaDefinitions({"Foo": Foo, "Bar": Bar})

    assert Foo.fields["a"].definitions is None
    assert Bar.fields["b"].definitions is None

    set_definitions(Foo, definitions)

    assert Foo.fields["a"].definitions is definitions
    assert Bar.fields["b"].definitions is definitions
    assert Foo.fields["a"].target is Bar

# Generated at 2022-06-14 14:37:45.126728
# Unit test for function set_definitions
def test_set_definitions():
    def assert_definitions(field: Field, definitions: SchemaDefinitions):
        if isinstance(field, Reference):
            assert field.definitions is definitions
        elif isinstance(field, Array):
            if field.items is not None and not isinstance(field.items, (list, tuple)):
                assert_definitions(field.items, definitions)
        elif isinstance(field, Object):
            for child in field.properties.values():
                assert_definitions(child, definitions)
    schema_definitions = SchemaDefinitions()
    schema_class = SchemaMetaclass(
        "SomeSchema", (Schema,), {}, schema_definitions
    )
    field = Reference("SomeReference")
    set_definitions(field, schema_definitions)

# Generated at 2022-06-14 14:37:53.993762
# Unit test for function set_definitions
def test_set_definitions():
    class InnerSchema(Schema):
        inner_attribute = Reference("OuterSchema")

    class OuterSchema(Schema):
        outer_attribute = Reference("InnerSchema")
        inner_attribute = InnerSchema

    definitions = SchemaDefinitions()
    definitions["InnerSchema"] = InnerSchema
    definitions["OuterSchema"] = OuterSchema
    set_definitions(InnerSchema.inner_attribute, definitions)
    set_definitions(OuterSchema.outer_attribute, definitions)

# Generated at 2022-06-14 14:38:02.571437
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        a = Field(type="string")
        b = Field(type="string")
        c = Field(type="string", default="foo")
    assert TestSchema(a="a", b="b") == TestSchema(a="a", b="b", c="foo")
    assert TestSchema(a="a", b="b", c="bar") == TestSchema(a="a", b="b", c="bar")
    assert TestSchema(a="a", b="b").is_sparse == False
    assert TestSchema(a="a").is_sparse == True
    assert TestSchema(a="a")["a"] == "a"
    assert TestSchema(a="a", b="b")["c"] == "foo"

# Generated at 2022-06-14 14:38:08.148447
# Unit test for function set_definitions
def test_set_definitions():
    class Definitions(SchemaDefinitions):
        pass
    definitions = Definitions()

    class A(Schema):
        a = String()
    class B(Schema):
        b = Reference("A")

    set_definitions(B.fields["b"], definitions)
    assert B.fields["b"].definitions is definitions
    assert B.fields["b"].target_string == "A"
    assert B.fields["b"].target is A



# Generated at 2022-06-14 14:38:26.832437
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Author(Schema):
        id = Field(type="integer")
        author_name = Field(type="string")
        email = Field(type="string")

    author1 = Author(id = 1, author_name = "Sammi", email = "sammi@gryffindor.nl")
    assert list(author1) == ['id', 'author_name', 'email']


# Generated at 2022-06-14 14:38:37.685273
# Unit test for constructor of class Schema
def test_Schema():
    class HasDefaults(Schema):
        name = Field(str, allow_null=True)
        age = Field(int, default=None)
        is_active = Field(bool, default=True)

    has_defaults = HasDefaults()

    assert isinstance(has_defaults, Schema)
    assert has_defaults.is_sparse
    assert hasattr(has_defaults, "name")
    assert has_defaults.name is None
    assert hasattr(has_defaults, "age")
    assert has_defaults.age is None
    assert hasattr(has_defaults, "is_active")
    assert has_defaults.is_active is True

    has_defaults = HasDefaults(name="Alice")

    assert isinstance(has_defaults, Schema)
    assert has_

# Generated at 2022-06-14 14:38:45.095354
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        something = Field(required=True)
        something_else = Field(required=False)

    ts = TestSchema()
    # Construir un objeto Schema correctamente
    assert test_Schema.__name__ == "test_Schema"
    assert ts.__class__.__name__ == "TestSchema"
    assert isinstance(ts, Schema)
    assert ts.something is None
    assert ts.something_else is None
    assert ts.__repr__() == "TestSchema() [sparse]"
    assert ts == TestSchema()
    assert ts != TestSchema(something="a")

    ts2 = TestSchema({"something": "a"})
    # Construir un Objeto Schema desde un diccionario

# Generated at 2022-06-14 14:38:57.044728
# Unit test for constructor of class Schema
def test_Schema():
    d_schema = {'a': 123, 'b': 789}
    d_schema2 = {'c': 123, 'd': 789}
    t_schema = (1,2,3,4)
    d_schema3 = {'e': 123, 'f': 789}
    d_schema4 = {'g': 123, 'h': 789}
    # Test case 1
    case1 = Schema(d_schema)
    case1.__getitem__('a')
    assert case1 == case1
    assert len(case1) == 2
    assert 'a' in case1
    # Test case 2
    case2 = Schema(d_schema2)
    case2.__getitem__('e')
    # Test case 3

# Generated at 2022-06-14 14:39:07.219889
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    schema = Schema(
        structure = "TEST",
        id = "TEST",
        group = [
            {"id": "B", "type": [{"id": "B1", "type": "string"}]},
            {"id": "C", "type": [{"id": "C1", "type": "string"}]}
        ]
    )
    expected = ['structure', 'id', 'group']
    actual = []
    for key in schema:
        actual.append(key)
    assert len(expected) == len(actual)
    for i in range(len(expected)):
        assert expected[i] == actual[i]
        

# Generated at 2022-06-14 14:39:13.747426
# Unit test for constructor of class Reference
def test_Reference():
    from random import choice

    def add_item(item=None, *, allow_null=False, **kwargs):
        if isinstance(item, str):
            return Reference(item, allow_null, kwargs)
        else:
            assert issubclass(item, Schema)
            return Reference(item, allow_null, kwargs)

    if '__package__' not in globals() or __package__ is None or len(__package__)==0:
      from Reference_test import Schema_test, test_Schema
      __package__ = 'Reference_test'
    if __package__ is not None:
      from Reference_test import Schema_test, test_Schema
    enum_test = ["a", "b", "c"]

# Generated at 2022-06-14 14:39:25.314404
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import typesystem
    class XSchema(typesystem.Schema):
        x = typesystem.String()

    schema = typesystem.Schema({'x':'x-value'})
    x_schema = XSchema(schema)
    assert len(x_schema) == 1
    assert list(x_schema) == ['x']
    assert list(x_schema.keys()) == ['x']
    assert list(x_schema.values()) == ['x-value']
    assert list(x_schema.items()) == [('x','x-value')]

    # assert list(x_schema.__iter__()) == ['x']
    assert 'x' in x_schema
    assert 'y' not in x_schema

# Generated at 2022-06-14 14:39:30.279604
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    obj = Object(properties={"a": Reference("User"), "b": Reference("User")})
    set_definitions(obj, definitions)
    assert obj.properties["a"].definitions is definitions
    assert obj.properties["b"].definitions is definitions

# Generated at 2022-06-14 14:39:35.504134
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # This test is intended to ensure that the __len__ method works correctly
    correct_output = 2
    class ExampleSchema(Schema):
        field1 = String()
        field2 = Integer()

    test_schema = ExampleSchema(field1='abc', field2=123)

    assert len(test_schema) == correct_output, "The __len__ method does not return the correct output"


# Generated at 2022-06-14 14:39:38.729311
# Unit test for constructor of class Reference
def test_Reference():
    # Setup
    definitions = SchemaDefinitions()
    Reference('Pet', definitions=definitions)
    # Verify
    assert(Reference('Cat', definitions=definitions).target_string == "Pet")

# Generated at 2022-06-14 14:39:56.566277
# Unit test for constructor of class Schema
def test_Schema():
    chelem = Schema(**{'a': 4, 'b': 5})
    assert chelem.a == 4
    assert chelem.b == 5
    print('Schema constructor passed!')


# Generated at 2022-06-14 14:39:59.871997
# Unit test for function set_definitions
def test_set_definitions():
    class TestSchema(Schema):
        test_field = Reference("TestClass")

    definitions = SchemaDefinitions()
    set_definitions(TestSchema.test_field, definitions)



# Generated at 2022-06-14 14:40:05.300216
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import Field, get_validator

    class Dog(Schema):
        name = Field.string()
        age = Field.number()

    dog = Dog(name="Scooby", age=4)
    assert dog.name == "Scooby"
    assert dog.age == 4

    # Unknown keyword arguments should raise error.
    with pytest.raises(TypeError):
        Dog(height=175)



# Generated at 2022-06-14 14:40:15.647429
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem import String
    assert issubclass(SchemaMetaclass, ABCMeta)
    class TestSchemaMetaclass___new__1(Mapping, metaclass=SchemaMetaclass):
        fields: typing.Dict[str, Field] = {}
    class TestSchemaMetaclass___new__2(Schema):
        name = String(description="Name of account", max_length=42)
    assert 'TestSchemaMetaclass___new__1' == TestSchemaMetaclass___new__1.__name__
    assert 'fields' == TestSchemaMetaclass___new__1.fields
    assert 'TestSchemaMetaclass___new__2' == TestSchemaMetaclass___new__2.__name__
    assert 'name' in TestSchemaMetaclass___new__2.fields
   

# Generated at 2022-06-14 14:40:20.745801
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        field1 = Field()
        field2 = Field()

    def schema_from_dict():
        schema = TestSchema({'field1': 'val1'})
        return bool(schema.field1 == 'val1' and schema.field2 == None)

    def schema_from_obj():
        class TestObj:
            field1 = 'val1'
        schema = TestSchema(TestObj())
        return bool(schema.field1 == 'val1' and schema.field2 == None)

    def schema_from_args():
        schema = TestSchema(field1='val1')
        return bool(schema.field1 == 'val1' and schema.field2 == None)

# Generated at 2022-06-14 14:40:31.750737
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from collections import UserDict

    class Info(Schema):
        id = Integer(minimum=1)
        value = String()

    class MyDict(UserDict):
        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            super().__init__(*args, **kwargs)
            self.data["y"] = 1

        def __eq__(self, other: typing.Any) -> bool:
            return self.data == other.data

    info = Info(id=1, value="value")
    assert info == Info(Info(id=1, value="value"))
    assert info == Info(id=1, value="value")
    assert info == MyDict(id=1, value="value")


# Generated at 2022-06-14 14:40:34.902395
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class PersonSchema(Schema):
        pass
    assert 'PersonSchema' == PersonSchema.__name__

    class PersonSchema(Schema):
        Reference('a')
    assert 'PersonSchema' == PersonSchema.__name__


# Generated at 2022-06-14 14:40:37.798670
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field = Reference(to="foo")
    set_definitions(field, definitions)
    assert definitions["foo"] is field._target

# Generated at 2022-06-14 14:40:42.626876
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class StrSchema(Schema):
        field = String()
    obj = StrSchema({"field": "value"})
    assert obj['field'] == "value"
    with pytest.raises(KeyError):
        obj['missing']


# Generated at 2022-06-14 14:40:52.686867
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    # test 'returns the new type'
    class Base(metaclass=SchemaMetaclass):
        pass

    assert Base() is not None
    assert isinstance(Base(), Base)
    assert Base().fields == {}

    # test 'adds members of base classes, in reverse MRO order'
    class BaseOne(metaclass=SchemaMetaclass):
        field_one = Field()

    class BaseTwo(metaclass=SchemaMetaclass):
        field_two = Field()

    class DerivedThree(BaseOne, BaseTwo, metaclass=SchemaMetaclass):
        pass

    assert DerivedThree().fields == {'field_one': BaseOne.field_one, 'field_two': BaseTwo.field_two}

    # test 'adds own members'

# Generated at 2022-06-14 14:41:13.354455
# Unit test for constructor of class Schema
def test_Schema():
    S = Schema
    S(dict(a = 1, b = 2))
    S(a = 1, b = 2)
    class A(S):
        fields = dict(a = 1, b = 2)
    A(dict(a = 1, b = 2))
    A(a = 1, b = 2)
    S(dict(a = 1)) # This should work

# Generated at 2022-06-14 14:41:15.924375
# Unit test for function set_definitions
def test_set_definitions():
    class MySchema(Schema):
        foo = Reference("Foo")

    definitions = SchemaDefinitions()
    set_definitions(MySchema.foo, definitions)

# Generated at 2022-06-14 14:41:21.574602
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    s = Schema()
    iter_ = s.__iter__()
    assert iter_ == iter([])
    s.a = 1
    s.b = 2
    iter_ = s.__iter__()
    assert iter_ == iter(['a', 'b'])
    return


# Generated at 2022-06-14 14:41:22.230460
# Unit test for constructor of class Schema
def test_Schema():
    assert (False)

# Generated at 2022-06-14 14:41:27.221289
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.base import String
    from typesystem import Schema
    from typesystem import fields

    class ResponseSchema(Schema):
        status = String()
        message = String()

    class RequestSchema(Schema):
        method = String()
        response = fields.Reference(to=ResponseSchema)



# Generated at 2022-06-14 14:41:35.322876
# Unit test for method validate of class Reference
def test_Reference_validate():
    class Movie(Schema):
        title = Field(str)
        genre = Field(str)

    class Person(Schema):
        name = Field(str)
        age = Field(int)

    class User(Schema):
        username = Field(str)
        password = Field(str)

    definitions = SchemaDefinitions()
    schema = Schema(
        definitions=definitions,
        movies=Array(Reference(Movie)),
        person=Reference(Person, definitions=definitions),
        users=Array(Reference(User))
    )


# Generated at 2022-06-14 14:41:45.617602
# Unit test for function set_definitions
def test_set_definitions():
    def check_set_definitions(schema, definitions):
        set_definitions(schema, definitions)
        assert schema.definitions == definitions
    schema = Object()
    definitions = {}
    check_set_definitions(schema, definitions)
    schema = Object()
    definitions = {"foo": "bar"}
    check_set_definitions(schema, definitions)
    schema = Array(items=String)
    definitions = {}
    check_set_definitions(schema, definitions)
    schema = Array(items=String)
    definitions = {"foo": "bar"}
    check_set_definitions(schema, definitions)
    schema = Reference(to="foo")
    schema.definitions = {"foo": "bar"}
    definitions = {}
    check_set_definitions(schema, definitions)

# Generated at 2022-06-14 14:41:53.633769
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    p1 = Person(name="John", age=20)
    p2 = Person(name="John", age=20)
    p3 = Person(name="Jane", age=20)
    p4 = Person(name="Jane", age=21)

    assert p1 == p2
    assert p1 != p3
    assert p3 != p4



# Generated at 2022-06-14 14:41:54.677781
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert False

# Generated at 2022-06-14 14:42:02.910692
# Unit test for constructor of class Schema
def test_Schema():
    class Schema2(Schema):
        field1 = Field(required=True)
        field2 = Field(required=True)
        field3 = Field(required=True)
        field4 = Field(required=True)
        field5 = Field(required=True)

    assert isinstance(Schema2(), Mapping)
    a = Schema2(field1="field1", field2="field2", field3="field3", field4="field4", field5="field5")
    assert a.field1 == "field1"
    assert a.field2 == "field2"
    assert a.field3 == "field3"
    assert a.field4 == "field4"
    assert a.field5 == "field5"

# Generated at 2022-06-14 14:42:39.774183
# Unit test for constructor of class Schema
def test_Schema():
    employee = Employee(name='John Smith', annual_salary=65000, department='IT')
    assert employee.name == 'John Smith'
    assert employee.annual_salary == '65000'
    assert employee.department == 'IT'
    
    employee = Employee(name='John Smith', department='IT')
    assert employee.name == 'John Smith'
    assert employee.annual_salary == '50000'
    assert employee.department == 'IT'
    
    employee = Employee(name='John Smith')
    assert employee.name == 'John Smith'
    assert employee.annual_salary == '50000'
    assert employee.department == 'undefined'
    
    employee = Employee(name='John Smith', annual_salary=65000, department='IT', bonus=60000)

# Generated at 2022-06-14 14:42:40.532818
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass

# Generated at 2022-06-14 14:42:52.434726
# Unit test for constructor of class Schema
def test_Schema():
    class User(Schema):
        name = String(max_length=100)
        age = Int()
        created = Date()

    user = User(name="Joe", age=25, created=datetime.date(2019, 2, 21))
    assert user.name == "Joe"
    assert user.age == 25
    assert user.created == datetime.date(2019, 2, 21)

    user = User({"name": "Joe", "age": 25, "created": datetime.date(2019, 2, 21)})
    assert user.name == "Joe"
    assert user.age == 25
    assert user.created == datetime.date(2019, 2, 21)

    user = User(User(name="Joe", age=25, created=datetime.date(2019, 2, 21)))

# Generated at 2022-06-14 14:43:01.037133
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from copy import deepcopy
    from typesystem import Integer

    class Person(Schema):
        age = Integer()

    assert Person(age=36) == Person(age=36)
    assert Person(age=37) != Person(age=36)
    assert Person() == Person(age=None)
    assert Person() != Person(age=37)
    assert Person() != Person(name="Jared")

    bob = Person(age=36)
    assert bob == deepcopy(bob)
    bob.age = 37
    assert bob != Person(age=36)

# Generated at 2022-06-14 14:43:05.265002
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from . import Metadata
    assert Metadata(state="validated", status="ready").__repr__() == "Metadata(state='validated', status='ready')"
    assert Metadata().__repr__() == "Metadata()"
    assert Metadata(state="validated").__repr__() == "Metadata(state='validated')"
    assert Metadata(status="ready").__repr__() == "Metadata(status='ready')"
    assert Metadata().__repr__() == "Metadata()"


# Generated at 2022-06-14 14:43:08.425349
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import datetime
    class Date(Schema):
        date = datetime.date
    assert list(Date(date=datetime.date(2020,1,1)))==['date']

# Generated at 2022-06-14 14:43:12.274093
# Unit test for function set_definitions
def test_set_definitions():
    target = "test"
    definitions = SchemaDefinitions()
    class Test(Schema):
        test = Reference(target, definitions)

    set_definitions(Test.test, definitions)
    
    assert Test.test.target is Test
    
    

# Generated at 2022-06-14 14:43:16.927073
# Unit test for constructor of class Schema
def test_Schema():
    from .validators import String
    class User(Schema):
        name = String()
    user = User(name='Mat')
    assert user['name'] == 'Mat'


# Generated at 2022-06-14 14:43:18.551276
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    s = Schema()
    print(s.__repr__())


# Generated at 2022-06-14 14:43:23.290461
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        foo = Reference(to="Bar")
    class Bar(Schema):
        name = Reference(to="Foo")

    definitions = SchemaDefinitions()
    set_definitions(Foo.fields["foo"], definitions)
    set_definitions(Bar.fields["name"], definitions)
    assert Foo.fields["foo"].definitions == definitions
    assert Bar.fields["name"].definitions == definitions