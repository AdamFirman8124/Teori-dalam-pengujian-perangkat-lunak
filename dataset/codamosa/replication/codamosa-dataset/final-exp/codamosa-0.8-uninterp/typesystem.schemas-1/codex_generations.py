

# Generated at 2022-06-14 14:34:59.157832
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    """
    Test the __eq__ method of class Schema.
    """
    class Person(Schema):
        name = String("name")
        age = Integer("age")

    class Book(Schema):
        name = String("name")
        owner = Object("owner", properties={"name": String("name")})

    person = Person(name="Jack", age=12)
    person2 = Person(name="Jack", age=12)
    person3 = Person(name="Jack", age=13)
    book = Book(name="The Lord of the Rings", owner={"name": "Jack"})
    book2 = Book(name="The Lord of the Rings", owner={"name": "Jack"})
    book3 = Book(name="The Lord of the Rings", owner={"name": "Mary"})
    assert person == person2


# Generated at 2022-06-14 14:35:04.654112
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class SomeSchema(Schema):
        foo = Field(type=int)
        bar = Field(type=int)
        baz = Field(type=int)

    x = SomeSchema(bar=42)

    assert {'bar'} == x



# Generated at 2022-06-14 14:35:07.464564
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    s = Student(name=True, age=11)
    assert isinstance(s, Schema)
    assert s.name is True
    assert s.age == 11


# Generated at 2022-06-14 14:35:09.493687
# Unit test for method __len__ of class Schema
def test_Schema___len__():

    class Person(Schema):
        first_name = Field(type=str)
        last_name = Field(type=str)
        age = Field(type=int)
    
    person = Person(first_name="Jane", last_name="Doe")
    assert len(person) == 2


# Generated at 2022-06-14 14:35:15.694620
# Unit test for function set_definitions
def test_set_definitions():
    class AbcSchema(Schema):
        abc = Array[Reference("XyzSchema")]

    class XyzSchema(Schema):
        xyz = Object({"xyz": Field()})

    definitions = SchemaDefinitions()
    AbcSchema.__init_subclass__(definitions=definitions)
    assert AbcSchema.fields["abc"].items.definitions is definitions
    assert AbcSchema.fields["abc"].items.items.definitions is definitions

# Generated at 2022-06-14 14:35:24.306411
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # Setup
    schema = Schema(
        {
            "name": "Alice",
            "age": 26,
            "children": [{"name": "Charlie", "age": 3}, {"name": "Beatrice", "age": 1}],
        }
    )
    # Exercise
    schema_repr = schema.__repr__()
    # Verify
    assert (
        schema_repr
        == "Schema(name='Alice', age=26, children=[{'name': 'Charlie', 'age': 3}, {'name': 'Beatrice', 'age': 1}])"
    )

    # Setup

# Generated at 2022-06-14 14:35:26.814872
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    definitions["a"] = 1


# Generated at 2022-06-14 14:35:33.467166
# Unit test for method validate of class Reference
def test_Reference_validate():
    import pytest
    from typesystem import Integer, String
    from typesystem.object import Object

    class InlineSubSchema(Object):
        a = Integer()
        b = Integer()

    class InlineSchema(Object):
        c = Integer()
        d = InlineSubSchema()

    class ReferenceSubSchema(Object):
        a = Integer()
        b = Integer()
    class ReferenceSchema(Object):
        c = Integer()
        d = Reference(ReferenceSubSchema)

    def test_validate_Inline():
        schema = InlineSchema()
        schema.validate({
            "c": 4,
            "d": {
                "a": 1,
                "b": 2
            }
        })

    def test_validate_Reference():
        schema = ReferenceSchema()
        schema

# Generated at 2022-06-14 14:35:42.346451
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = Field(str)

    class Dog(Schema):
        name = Field(str)

    class DefinitionSchema(Schema, definitions=SchemaDefinitions()):
        person = Reference(Person)
        dog = Reference(Dog)

    # Make sure that the reference has been initialized with the correct
    # definitions.
    assert DefinitionSchema.fields["person"].definitions == DefinitionSchema.definitions
    assert DefinitionSchema.fields["dog"].definitions == DefinitionSchema.definitions

    # Ensure that if a Reference's `.to` is a string, it's only set to a
    # schema after the Reference has been embedded in a Schema instance.
    class DefinitionSchemaWithStringRef(Schema, definitions=SchemaDefinitions()):
        person2 = Reference("Person")
        dog2

# Generated at 2022-06-14 14:35:48.486040
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = Field()

    class PersonSchema(Schema):
        person = Reference(to=Person)

    def test_set_definitions_field(field, definitions):
        set_definitions(field, definitions)
        assert field.definitions == definitions

    definitions = SchemaDefinitions()
    person_schema = PersonSchema.make_validator()
    test_set_definitions_field(person_schema, definitions)
    test_set_definitions_field(person_schema.properties["person"], definitions)
    test_set_definitions_field(person_schema.properties["person"].target, definitions)
    test_set_definitions_field(person_schema.properties["person"].target.properties["name"], definitions)

# Generated at 2022-06-14 14:36:09.516846
# Unit test for function set_definitions
def test_set_definitions():
    class Parent(Schema):
        child = Reference("Child")

    class Child(Schema):
        pass

    class GrandChild(Schema):
        pass

    definitions = SchemaDefinitions(Child=Child)
    set_definitions(Parent.fields["child"], definitions)

# Generated at 2022-06-14 14:36:18.645136
# Unit test for constructor of class Schema
def test_Schema():
    class Test(Schema):
        a = Field(required=True)
        b = Field(required=False)

    class Test2(Test):
        c = Field(required=True)
        d = Field(required=False)

    test = Test(a = 3)
    test2 = Test2(a = 2, c = 5)

    assert test.a == 3
    assert test.b is None
    assert test2.a == 2
    assert test2.b is None
    assert test2.c == 5
    assert test2.d is None
    try:
        test2.validate({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}, strict = True)
    except:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:36:27.148850
# Unit test for method validate of class Reference
def test_Reference_validate():
    class UserSchema(Schema):
        name = String()
    class Settings:
        pass
    class SettingsSchema(Schema):
        user = Reference(UserSchema)
    settings = Settings()
    settings.user = UserSchema(name='david')
    # Test for valid input
    result = Reference(UserSchema).validate(settings.user)
    assert result.name == 'david'
    # Test for invalid input
    with pytest.raises(TypeError):
        Reference(UserSchema).validate(settings)

# Generated at 2022-06-14 14:36:37.115165
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from . import SubJsonSchema
    from . import SubJsonSchemaWithDefault
    from . import SubNonJsonSchema
    from . import SubNonJsonSchemaWithDefault
    obj = SubNonJsonSchemaOpt(a=1, b=2, c=3)
    real_result = obj.__repr__()
    expected_result = "SubNonJsonSchemaOpt(a=1, b=2, c=3)"
    assert real_result == expected_result
    obj = SubJsonSchema(a=1, b=2, c=3)
    real_result = obj.__repr__()
    expected_result = "SubJsonSchema(a=1, b=2, c=3)"
    assert real_result == expected_result
    obj = SubJsonSchemaWith

# Generated at 2022-06-14 14:36:42.976873
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        title = String()
    class Bar(Schema):
        ref = Reference(Foo)

    Bar.fields['ref'].definitions = SchemaDefinitions()
    assert 'Foo' in Bar.fields['ref'].definitions
    assert Bar.fields['ref'].definitions['Foo'] == Foo

# Generated at 2022-06-14 14:36:53.247067
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import jsonschema
    data = {'id': 'this is a test', 'name': 'sand'}
    expected = 'sand'
    with pytest.raises(jsonschema.ValidationError):
        schema = TypeSystem(
            schema_type='object',
            additional_properties=False,
            properties={
                'name': {
                    'type': 'string',
                    'title': 'Name',
                    'description': 'The name of the thing',
                    'maxLength': 10
                }
            },
            required=['name', 'id']
        )
        val = schema.validate(data)
        assert val['name'] == expected
    data = {'id': 'this is a test', 'name': 'sand', 'color': 'brown'}

# Generated at 2022-06-14 14:37:01.911799
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # Positivo

    # Creamos una instancia de Schema
    class Document(Schema):
        title = String()
        author = String()

    # Creamos una instancia de Document con los valores
    # 'El Quijote', 'Cervantes'
    document = Document(
        title='El Quijote', author='Cervantes'
    )

    # Usamos la función __iter__
    it = document.__iter__()

    # El iterador it contiene los mismos elementos que la lista
    # ['title', 'author']
    assert [item for item in it] == ['title', 'author']


# Generated at 2022-06-14 14:37:07.874891
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import copy

    class Person(Schema):
        name = String()
        age = Integer()

    p1 = Person(name="John Smith", age=30)
    p2 = Person(name="Paul Allen", age=30)
    assert not p1 == p2

    p2.age = 31  # p2 becomes a sparsely populated schema
    assert not p1 == p2

    p2.age = 30
    p3 = copy.copy(p1)
    assert p1 == p3

# Generated at 2022-06-14 14:37:13.196927
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class MySchema(Schema):
        field_one = Field(type="string")
        field_two = Field(type="string")
        field_three = Field(type="string")
    schema = MySchema()
    result = len(schema)
    expected = 0
    assert result == expected

# Generated at 2022-06-14 14:37:18.526081
# Unit test for function set_definitions
def test_set_definitions():
    class A(Schema):
        a = Reference("B")
        b = Reference("C")

    class B(Schema):
        b = Reference("C")
        c = Reference("D")

    class C(Schema):
        c = Reference("D")
        d = Reference("E")

    class D(Schema):
        d = Reference("E")
        f = Reference("F")

    class F(Schema):
        pass

    definitions = SchemaDefinitions()
    set_definitions(A, definitions)
    assert "B" in definitions
    assert "C" in definitions
    assert "D" in definitions
    assert "E" in definitions
    assert "F" in definitions

# Generated at 2022-06-14 14:37:33.137904
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class T(Schema):
        f = Field()

    assert T(f=1) == T(f=1)
    assert T(f=1) != T(f=2)
    assert T(f=1) != T(f=1, g=2)
    assert T(f=1) != T(f=1, g=2)



# Generated at 2022-06-14 14:37:36.043342
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    instance = Schema()
    assert list(instance) == []



# Generated at 2022-06-14 14:37:38.509384
# Unit test for method validate of class Reference
def test_Reference_validate():
    ref = Reference("Person")
    assert ref.validate({"name": "John"}) == {"name": "John"}

# Generated at 2022-06-14 14:37:40.626356
# Unit test for constructor of class Reference
def test_Reference():
    r = Reference(str,default=None)
    assert r._target_string == str(r.to)



# Generated at 2022-06-14 14:37:44.543078
# Unit test for function set_definitions
def test_set_definitions():
    class MySchema(Schema):
        target = Object(properties={"x": Reference('Y')})

    defs = SchemaDefinitions()
    set_definitions(MySchema.fields['target'], defs)
    assert defs['Y'] == MySchema.fields['target'].properties['x'].target

# Generated at 2022-06-14 14:37:50.149050
# Unit test for function set_definitions
def test_set_definitions():
    from typesystem.fields import Number
    class Num(Schema):
        i = Number()
    class Group(Schema):
        nums = Array(items=Reference(Num))
    definitions = SchemaDefinitions()
    set_definitions(Group.fields['nums'], definitions)
    
    


# Generated at 2022-06-14 14:37:53.601804
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class A(Schema):
        field_0 = Field(type=int)
    a = A()
    assert len(a) == 0



# Generated at 2022-06-14 14:37:56.818267
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    schema = Schema({'name': 'John', 'surname': 'Smith'})
    other = Schema({'surname': 'Smith', 'name': 'John'})
    assert schema == other


# Generated at 2022-06-14 14:38:08.149492
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem import Integer, String
    from typesystem_extensions import SchemaMetaclass

    class MySchema(Schema, metaclass=SchemaMetaclass):
        a = Integer()
        b = Integer()
        c = String()
        d = Reference(to=MySchema)

    print(MySchema.fields)
    print(MySchema.validate({"a": 1, "b": 2}))
    print(MySchema.validate({"a": 1, "c": "33"}))
    print(MySchema.validate({"a": 1, "b": 2, "d": {"a": 4, "b": 4, "c": "44"}}))

# Generated at 2022-06-14 14:38:15.517917
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from collections import OrderedDict
    from typesystem.types import Integer
    class Person(Schema):
        age = Integer(description='Age of the person', format='int32')
        surname = Integer(description='Surname of the person', format='int32')

    person = Person()
    person.age = 23
    person._order_dict = OrderedDict({'age':person.age, 'surname':person.surname})
    assert person['age'] == 23


# Generated at 2022-06-14 14:38:39.945647
# Unit test for function set_definitions
def test_set_definitions():
    class MyObject(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class UserSchema(Schema):
        id = Field(type="string")
        name = Field(type="string")

    class CommentSchema(Schema):
        body = Field(type="string")

        def validate(self, value, strict=False):
            value = super().validate(value, strict)
            value = MyObject(**value)
            return value

    class PostSchema(Schema):
        text = Field(type="string")
        author = Reference(UserSchema)
        comments = Array(items=Reference(CommentSchema))

        def validate(self, value, strict=False):
            value = super().validate(value, strict)
            value = MyObject

# Generated at 2022-06-14 14:38:45.345556
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class_name = "Schema"
    fields = {
        "foo": Field(),
        "bar": Field(),
        "baz": Field(),
        "qux": Field(),
    }
    bases = ()
    attrs = {}
    for key, value in fields.items():
        attrs[key] = value
    definitions = SchemaDefinitions()
    cls = SchemaMetaclass(class_name, bases, attrs, definitions)
    assert cls.__name__ == class_name
    assert cls.fields == fields
    assert definitions[class_name] == cls
    return cls

# Generated at 2022-06-14 14:38:49.966719
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        field_a = Field()
        field_b = Field()
    schema = TestSchema(field_a=42, field_b=43)
    assert list(schema) == ['field_a', 'field_b']

# Generated at 2022-06-14 14:38:51.332663
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert False



# Generated at 2022-06-14 14:38:52.893701
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    # list
    my_list = [1, 2, 3]
    my_list_len = len(my_list)
    assert my_list_len == 3


# Generated at 2022-06-14 14:39:02.408290
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Book(Schema):
        title = String()
        author = String()
        publication_date = Date()
    class_name = 'Book'
    assert Book().__repr__() == str(class_name+'(title=None, author=None, publication_date=None) [sparse]')
    book = Book(title = 'The Book of Awesomeness', author = 'Sujie Qiu', publication_date = '2020-06-23')
    assert book.__repr__() == str(class_name+"(title='The Book of Awesomeness', author='Sujie Qiu', publication_date=datetime.date(2020, 6, 23))")

test_Schema___repr__()

# Generated at 2022-06-14 14:39:14.795614
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    # Tests the case when args and kwargs are not empty.
    class PersonSchema(Schema):
        name = Field(description="A person's name.")
        age = Field(description="A person's age.")
    try:
        PersonSchema(None)
        assert False
    except TypeError as e:
        assert str(e) == "__init__() takes 1 positional argument but 2 were given"
    try:
        PersonSchema()
        assert False
    except TypeError as e:
        assert str(e) == "__init__() takes at least 2 positional arguments " + \
                         "(1 given)"

# Generated at 2022-06-14 14:39:20.978483
# Unit test for method validate of class Reference
def test_Reference_validate():
    # test happy path
    to_dic = {'a': 'happy', 'b': 'path'}
    try:
        Reference("a_reference_string").validate(to_dic)
    except TypeError:
        print('happy path tested')
    else:
        print('happy path test failed')
# test_Reference_validate()


# Generated at 2022-06-14 14:39:32.086112
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import unittest

    class Person(Schema):
        name = Field()
        age = Field(default=0)

    person1 = Person(name="Gilberto")
    person2 = Person(name="Gilberto", age=2)
    person3 = Person(name="gilberto")

    class Test1(unittest.TestCase):
        def test_person_equals_person(self):
            self.assertTrue(person1 == Person(name="Gilberto"))
            self.assertFalse(person1 == Person(name="gilberto"))

    class Test2(unittest.TestCase):
        def test_sparse_person_equals_sparse_person(self):
            self.assertTrue(person1 == person2)


# Generated at 2022-06-14 14:39:35.014432
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    fields = {}
    obj = Schema(fields)
    expected = "Schema({}) [sparse]"
    actual = obj.__repr__()
    assert actual == expected


# Generated at 2022-06-14 14:39:48.988251
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    schema = Schema()
    set_definitions(schema, definitions)
    assert definitions == {}



# Generated at 2022-06-14 14:39:52.209484
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class MySchema(Schema):
        a = Field(required=True)
        b = Field(required=True)

    s = MySchema(a=1, b=2)
    assert repr(s) == "MySchema(a=1, b=2)"

# Generated at 2022-06-14 14:40:03.863218
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    assert Person.fields == {"name": Field(type=str), "age": Field(type=int)}
    try:
        class Person(Schema):
            name = Field(type=str)
            name = Field(type=str)
    except AssertionError as e:
        assert str(e) == r"Definition for 'name' has already been set."
    class Person(Schema):
        name = Field(type=str, default="John Doe")
        age = Field(type=int)
    assert Person.fields == {
        "name": Field(type=str, default="John Doe"),
        "age": Field(type=int)
    }




# Generated at 2022-06-14 14:40:05.072114
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass


# Generated at 2022-06-14 14:40:13.398276
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String, Integer

    class TestCase(Schema):
        name = String(max_length=3)
        age = Integer()

    test_case = TestCase(age=34, name='abc')
    print('\n')
    print(test_case)
    key_list = list(test_case)
    print(key_list)
    print(type(key_list[0]))
    print(type(key_list[1]))
    assert(type(key_list[0]) is str)
    assert(type(key_list[1]) is str)


# Generated at 2022-06-14 14:40:17.493753
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import ipdb
    ipdb.set_trace()
    from typesystem.fields import String
    from typesystem.schema import Schema

    class PersonSchema(Schema):
        name = String()

    person = PersonSchema(name='Jack')
    iter1 = person.__iter__()
    assert next(iter1) == 'name'


# Generated at 2022-06-14 14:40:27.394967
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Book(Schema):
        """
        A book that features in a library
        """
        title = Field()
        isbn = Field()
        year = Field()
        authors = Array(String())


    definitions = SchemaDefinitions()
    book_validator = Book.make_validator(strict=True)
    assert book_validator.properties == {
        'title': Field(),
        'isbn': Field(),
        'year': Field(),
        'authors': Array(String()),
    }
    assert book_validator.required == ['title', 'isbn', 'year', 'authors']

# Generated at 2022-06-14 14:40:30.945758
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class PersonSchema(Schema):
        name = String()
        # ...
    assert PersonSchema.__name__ == "PersonSchema"
    assert bool(PersonSchema.fields) == True
    
    

# Generated at 2022-06-14 14:40:38.140981
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    text = """from typing import Any

    from typesystem import Schema, String, Integer

    class TestSchema(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)
    """
    from typesystem import Schema, String, Integer
    from typesystem.utils import class_from_source

    class TestSchema(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)
        def __init__(self, *args, **kwargs):
            if args:
                assert len(args) == 1
                assert not kwargs
                item = args[0]
                if isinstance(item, dict):
                    for key in self.fields.keys():
                        if key in item:
                            setattr(self, key, item[key])

# Generated at 2022-06-14 14:40:45.340601
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from bson import ObjectId
    from typesystem.schema import Schema
    from typesystem.fields import String
    from typesystem.integer.integer import Integer

    class Book(Schema):
        _id = Integer(allow_null=True)
        title = String(max_length=100)

    book = Book(_id=None, title="Don Quixote")
    assert book["title"] == "Don Quixote"
    assert book["_id"] is None


# Generated at 2022-06-14 14:41:08.326452
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Book(Schema):
        title = String()
        isbn = String(title="ISBN")
        # abstract = Boolean() - to mark whether the book is a draft or published
        id = String(format="uuid")
        created_at = DateTime()
        publication_date = DateTime()
        author = Reference(to="Author")

    class Author(Schema):
        name = String()
        email = String(format="email")
        phone = String(format="phone")

    author = Author(name="John Doe", email="john@doe.com", phone="555-0123")

# Generated at 2022-06-14 14:41:10.961039
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        a = Field(type=int)
        b = Field(type=int)

    # test
    obj = TestSchema(a=1, b=2)
    assert len(obj) == 2
    # test
    obj = TestSchema(a=1)
    assert len(obj) == 1
    # test
    # ValueError: Invalid argument 'a' for TestSchema().
    obj = TestSchema(a=1.0, b=2)


# Generated at 2022-06-14 14:41:11.550227
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass

# Generated at 2022-06-14 14:41:21.168243
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import typesystem
    import datetime
    import abc
    import typing
    import dataclasses


    class User(Schema):
        id = typesystem.Integer()
        first_name = typesystem.String(max_length=255, default="")
        last_name = typesystem.String(max_length=255, default="")
        is_active = typesystem.Boolean(default=False)
        email = typesystem.String()
        created_at = typesystem.DateTime()
        updated_at = typesystem.DateTime()



# Generated at 2022-06-14 14:41:25.774761
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    person1 = Person({"name": "John", "age": 20})
    person2 = Person({"name": "John", "age": 20})

    assert person1 == person2

# Generated at 2022-06-14 14:41:34.566858
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    test1 = Schema(a=1)
    assert test1.__repr__() == 'Schema(a=1)'
    test2 = Schema(a=1, b=2, c=3)
    assert test2.__repr__() == 'Schema(a=1, b=2, c=3)'
    test3 = Schema(a=1, b=2)
    assert test3.__repr__() == 'Schema(a=1, b=2)'
    test4 = Schema(a=1, b=2, c=3, d=4)
    assert test4.__repr__() == 'Schema(a=1, b=2, c=3, d=4)'

# Generated at 2022-06-14 14:41:39.432532
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class TestSchema(Schema, metaclass=SchemaMetaclass):
        name = String(name="name", required=True)
        age = Integer(name="age", required=True, max=120)
        ice_cream = String(name="ice_cream", default='vanilla')

    field_names = {field.name for field in TestSchema.fields.values()}

    assert field_names == {"name", "age", "ice_cream"}
    assert TestSchema.fields["name"].required is True
    assert TestSchema.fields["age"].required is True
    assert TestSchema.fields["ice_cream"].required is False
    assert TestSchema.fields["ice_cream"].default == 'vanilla'


if __name__ == "__main__":
    import pytest, sys
    py

# Generated at 2022-06-14 14:41:51.988189
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import random
    import string
    random_letters = (random.choice(string.ascii_uppercase) for _ in range(10))
    class TestSchema(Schema):
        str_0=Field(type_=str, default="")
        str_1=Field(type_=str, default="")
        str_2=Field(type_=str, default="")
        str_3=Field(type_=str, default="")
        str_4=Field(type_=str, default="")
        str_5=Field(type_=str, default="")
        str_6=Field(type_=str, default="")
        str_7=Field(type_=str, default="")
        str_8=Field(type_=str, default="")

# Generated at 2022-06-14 14:41:57.357677
# Unit test for function set_definitions
def test_set_definitions():
    class Simple(Schema):
        a = Integer()
        b = Reference("Simple", allow_null=True)
    definitions = SchemaDefinitions()
    class_name = "Simple"
    field = Simple.make_validator()
    set_definitions(field, definitions)
    assert field.properties["b"].definitions == definitions
    assert definitions[class_name] == Simple


# Generated at 2022-06-14 14:42:07.522606
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema1(Schema):
        field1 = Field()
        field2 = Field()
        field3 = Field()
        field4 = Field()
        field5 = Field()

        def __init__(self, value1, value2, value3, value4, value5, **kwargs: typing.Any) -> None:
            self.field1 = value1
            self.field2 = value2
            self.field3 = value3
            self.field4 = value4
            self.field5 = value5
            super(TestSchema1, self).__init__(**kwargs)
    
    schema1 = TestSchema1(1, 2, 3, 4, 5)
    # all values are assigned

# Generated at 2022-06-14 14:42:35.798763
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Integer, String

    class RaceCar(Schema):
        name = String()
        hp = Integer()

    car = RaceCar({"name": "stig", "hp": 2000})
    # print(car)
    assert car.name == "stig"
    assert car.hp == 2000


# Generated at 2022-06-14 14:42:38.044006
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        field = 'Example'
    assert ExampleSchema() == ExampleSchema()


# Generated at 2022-06-14 14:42:47.227730
# Unit test for function set_definitions
def test_set_definitions():

    from typesystem.fields import String, DateTime

    string_field = String()
    time_field = DateTime()
    array_field = Array(items=string_field)
    object_field = Object(properties={"test": string_field})

    definitions = SchemaDefinitions()

    assert set_definitions(string_field, definitions) is None
    assert set_definitions(time_field, definitions) is None
    assert set_definitions(array_field, definitions) is None
    assert set_definitions(object_field, definitions) is None



# Generated at 2022-06-14 14:42:50.577346
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    s = Schema(first_name="John", last_name="Smith", age=36)
    for key, value in s.items():
        assert key in s
        assert s[key] == value



# Generated at 2022-06-14 14:42:58.420625
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():

    # Default implementation
    try:
        from typesystem import types
    except ImportError:
        pass
    else:
        reference_to = types.Reference("name")

    # Implementation from typesystem 3.2.0
    class String(Field):
        def __init__(self, **kwargs: typing.Any) -> None:
            kwargs.setdefault("error_messages", {"null": "May not be null."})
            super().__init__(**kwargs)

        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if value is None and self.allow_null:
                return None
            elif value is None:
                raise self.validation_error("null")
            return str(value)

    class Person(Schema):
        name = String()

# Generated at 2022-06-14 14:43:02.275172
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Test_Schema_iter(Schema):
        a = Field()
        b = Field()
    obj = Test_Schema_iter(a=1, b=2)
    assert set(iter(obj)) == {'a', 'b'}

# Generated at 2022-06-14 14:43:07.484257
# Unit test for constructor of class Schema
def test_Schema():
    temp_args = [{"name": "toto", "age": 21}]
    s = Schema(*temp_args)

    assert s.__len__() == 2
    for key in s.fields.keys():
        if key in s:
            assert getattr(s, key) == temp_args[0][key]


# Generated at 2022-06-14 14:43:14.392161
# Unit test for function set_definitions
def test_set_definitions():
    class Foo:
        a = Field()
        b = Field()

    class Bar(Schema):
        a = Field()
        b = Field()

    class FooBar(Schema):
        foo = Bar()
        bar = Reference(Bar)

    class Definitions(SchemaDefinitions):
        pass

    definitions = Definitions()
    definitions["Foo"] = Foo
    definitions["Bar"] = Bar
    definitions["FooBar"] = FooBar
    FooBar.validate({
        "foo": {},
        "bar": {},
    })

# Generated at 2022-06-14 14:43:23.769497
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        name = String()
        age = Integer()
    person = Person(name="James", age=42)
    assert person == Person({"name": "James", "age": 42})
    assert person.name == "James"
    assert person["name"] == "James"
    try :
        person[2]
    except KeyError as err:
        assert str(err) == "2"
    try :
        Person()["name"]
    except KeyError as err:
        assert str(err) == "name"
    try :
        Person(2)["name"]
    except TypeError as err:
        assert str(err) == "Expected a valid value for schema `Person()`."

# Generated at 2022-06-14 14:43:31.264185
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Schema1(Schema):
        field = Field()

    x = Schema1()
    Schema1.fields = {'field': 1}
    object1 = Schema1.__iter__(x)
    assert object1 == iter([])

    class Schema2(Schema):
        field = Field()

    x = Schema2({'field': 1})
    Schema2.fields = {'field': 1}
    object2 = Schema2.__iter__(x)
    assert object2 == iter(['field'])
