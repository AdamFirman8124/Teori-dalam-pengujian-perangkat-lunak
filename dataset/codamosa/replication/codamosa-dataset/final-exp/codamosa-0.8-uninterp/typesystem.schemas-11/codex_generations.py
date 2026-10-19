

# Generated at 2022-06-14 14:34:30.725898
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    student = {
        "name": "Jaap",
        "email": "jaap@example.com",
        "favorite_color": "blue"
    }
    class StudentSchema(Schema):
        name = Field(String())
        email = Field(String())
        favorite_color = Field(String())
    student_schema = StudentSchema(student)
    assert list(student_schema) == ['name', 'email', 'favorite_color']


# Generated at 2022-06-14 14:34:33.068647
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    d = SchemaDefinitions()
    class A: pass
    assert d._definitions == {}
    d[0] = A
    assert d._definitions == {0: A}


# Generated at 2022-06-14 14:34:38.971221
# Unit test for function set_definitions
def test_set_definitions():
    class TestSchema(Schema):
        definitions = SchemaDefinitions()
        thing = Object(properties={
            "a": Object(properties={
                "ref": Reference("RefClass"),
            }),
            "b": Array(items=Reference("RefClass")),
        })

    class RefClass(Schema):
        pass

    assert TestSchema.thing.properties["a"].properties["ref"].definitions \
           == TestSchema.definitions
    assert TestSchema.thing.properties["b"].items.definitions \
           == TestSchema.definitions



# Generated at 2022-06-14 14:34:42.371013
# Unit test for function set_definitions
def test_set_definitions():
    class A(Schema):
        a = Field(type="integer")
    assert A.fields["a"].definitions is None
    definitions = SchemaDefinitions()
    definitions["A"] = A
    A(definitions=definitions)
    assert A.fields["a"].definitions is not None

# Generated at 2022-06-14 14:34:44.175772
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    """
    test __setitem__ of class SchemaDefinitions
    """
    # TODO
    pass


# Generated at 2022-06-14 14:34:50.924839
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    schema_definitions = SchemaDefinitions(
        test1=1,
        test2=2,
    )
    with pytest.raises(AssertionError) as e:
        schema_definitions.__setitem__('test1', 3)
    assert str(e.value) == r"Definition for 'test1' has already been set."
    assert schema_definitions == {'test1':1,'test2':2}


# Generated at 2022-06-14 14:34:56.942434
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # Test the edge case when the schema has no value
    S = SchemaMetaclass("Test", (object,), {}, None)
    s = S()
    assert repr(s) == 'Test()'
    
    # Test the normal case when the schema has some values
    S = SchemaMetaclass("Test", (object,), {'a': 1, 'b': 2}, None)
    s = S()
    assert repr(s) == 'Test(a=1, b=2)'

# Generated at 2022-06-14 14:35:00.259302
# Unit test for constructor of class Schema
def test_Schema():
    class MySchema(Schema):
        name = Field()
        foo = Field()

    s = MySchema(name="foo")
    assert s.name == "foo"
    assert s.foo is None


# Generated at 2022-06-14 14:35:08.041707
# Unit test for constructor of class Schema
def test_Schema():
    class PersonSchema(Schema):
        first_name = Field(str, required=True)
        last_name = Field(str, required=True)
        dob = Field(str, required=False)

    person = PersonSchema({"first_name": "John", "last_name": "Doe"})
    assert person.first_name == "John"
    assert person.last_name == "Doe"
    assert person.dob is None


# Generated at 2022-06-14 14:35:17.599574
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    key = "a"
    value = "b"
    definitions[key] = value
    definitions["c"] = "d"
    definitions["e"] = "f"

    assert definitions.get("a") == "b"
    assert definitions.get("b") is None
    assert definitions.get("c") == "d"
    assert definitions.get("d") is None
    assert definitions.get("e") == "f"
    assert definitions.get("f") is None

    assert list(definitions.keys()) == ["a", "c", "e"]
    assert list(definitions.values()) == ["b", "d", "f"]
    assert list(definitions.items()) == [("a", "b"), ("c", "d"), ("e", "f")]



# Generated at 2022-06-14 14:35:44.418668
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    if (Schema(test_typesystem_base_Person(**{'age': 5, 'name': 'hello'}) ) == Schema(test_typesystem_base_Person(**{'age': 5, 'name': 'hello'}))):
        return 1
    else:
        return 0



# Generated at 2022-06-14 14:35:48.170574
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Schema1(Schema):
        name: str = "Brent"
        age: int = 28

    class Schema2(Schema):
        address: str
        phone: int

    s1 = Schema1()
    s2 = Schema2(address="shanghai", phone=12345678)

    assert len(s1) == 2
    assert len(s2) == 2

    s2.address = ""
    assert len(s2) == 1



# Generated at 2022-06-14 14:36:00.479384
# Unit test for constructor of class Reference
def test_Reference():
    # Test 1
    def assert_error(to, definitions=None, **kwargs):
        try:
            Reference(to, definitions, **kwargs)
        except AssertionError:
            pass
        except Exception as e:
            raise AssertionError(
                "AssertionError was expected but {e!r} ({e.__class__.__name__}) was returned".format(e=e))
        else:
            raise AssertionError(
                "AssertionError was expected but nothing was raised"
            )

    assert_error(None)
    assert_error(1)
    assert_error(1, definitions=False)
    # Test 2
    class DummySchema(Schema):
        pass
    t = Reference(DummySchema)
    assert (t._target == DummySchema)


# Generated at 2022-06-14 14:36:10.926113
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import typesystem
    class LazyDescriptor:
        def __get__(self, instance: 'typesystem.Schema', owner: type) -> typing.Any:
            return 'LazyDescriptor'
        def __set__(self, instance: 'typesystem.Schema', value: typing.Any) -> None:
            pass
        def __delete__(self, instance: 'typesystem.Schema') -> None:
            pass
    class TestSchema(typesystem.Schema):
        lazy: 'LazyDescriptor' = LazyDescriptor()
        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            self.lazy = '__init__'
    schema = TestSchema()
    assert schema['lazy'] == '__init__'

#

# Generated at 2022-06-14 14:36:18.335171
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from hypothesis import strategies as st

    from .schemas import PluginSchema

    empty_schema = PluginSchema()
    non_empty_schema = PluginSchema(
        name="name",
        canonical_name="canonical_name",
        module="module",
        author="author",
        version="version",
        description="description",
    )

    schema = st.builds(PluginSchema, name=st.text())
    val = st.one_of(schema, empty_schema, non_empty_schema)

    assert len(val) > 0 if val is not empty_schema else True



# Generated at 2022-06-14 14:36:23.182801
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = String()
        age = Integer()

    class PersonReference(Reference):
        to = Person

    d = SchemaDefinitions()
    set_definitions(PersonReference(), d)
    assert d["Person"] == Person

# Generated at 2022-06-14 14:36:24.718726
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # tested in test_Schema_init
    pass


# Generated at 2022-06-14 14:36:28.564598
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class FooSchema(Schema):
        x = Field(String)

    assert len(FooSchema({})) == 0
    assert len(FooSchema({"x": "foo"})) == 1
# Test calling method __getitem__ of class Schema

# Generated at 2022-06-14 14:36:36.588406
# Unit test for method validate of class Reference
def test_Reference_validate():
    from td_maternal_validators.form_validators import MaternalHivInterimHxFormValidator, ProtocolDeviationsViolationsFormValidator
    """This function tests that Reference.validate behaves correctly"""

    maternal_hiv_interim_hx_form_validator = MaternalHivInterimHxFormValidator(
        raise_exception=True)
    sd = SchemaDefinitions()
    maternal_hiv_interim_hx_form_validator.set_schema_definitions(sd)
    sd["MaternalHivInterimHxFormValidator"].validate({})


# Generated at 2022-06-14 14:36:40.440235
# Unit test for function set_definitions
def test_set_definitions():

    class OldSchema(Schema):
        name = Field()
        age = Field()

    class NewSchema(OldSchema):
        address = Reference("OldAddressSchema")

    definitions = SchemaDefinitions()

    # Check references in `Schema`
    fields = dict(NewSchema.fields)

    for field in fields.values():
        set_definitions(field, definitions)

    assert fields["address"].definitions is definitions

# Generated at 2022-06-14 14:36:51.571633
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Foo(Schema):
        bar = Integer()

    foo = Foo(bar=10)
    assert repr(foo) == "Foo(bar=10)"


# Generated at 2022-06-14 14:36:59.825879
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema1(Schema):
        field1 = Field(type="integer")

    class TestSchema2(Schema):
        field1 = Field(type="integer", default=4)

    obj1 = TestSchema1(field1=3)
    assert len(obj1) == 1

    obj2 = TestSchema2()
    assert len(obj2) == 0

    obj3 = TestSchema2(field1=4)
    assert len(obj3) == 0


# Generated at 2022-06-14 14:37:08.817824
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from hypothesis import given, assume, settings
    from hypothesis.strategies import integers, dictionaries, frozensets, tuples, sampled_from
    from mimesis import Generic
    from typesystem.base import ValidationResult
    from typesystem.types import Integer
    from typesystem.types import array
    from typesystem.types import object_
    from typesystem.types import string
    import typesystem
    import typing
    import mimesis
    import hypothesis
    import hypothesis.internal.reflection
    import hypothesis.internal.conjecture.utils


    class Test_Schema___repr__(object):
        def __init__(self, a: typing.Any, b: typing.Any, c: typing.Any) -> None:
            self.a = a
            self.b = b
            self.c = c


# Generated at 2022-06-14 14:37:10.507345
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 14:37:15.194577
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    class A(Schema):
        a = Reference("B")
    class B(Schema):
        b = Reference("C")

    set_definitions(A, definitions)
    set_definitions(B, definitions)
    return definitions

# Generated at 2022-06-14 14:37:22.977188
# Unit test for constructor of class Schema
def test_Schema():
    class A(Schema):
        a = Field()
        b = Field()
        c = Field(default=1)

    assert isinstance(A(), A)
    assert isinstance(A(a=1,b=2,c=3), A)
    assert isinstance(A(dict(a=1,b=2,c=3)), A)

    try:
        A(a=1,b=2,c=3,d=4)
    except TypeError:
        pass
    else:
        raise AssertionError


# Generated at 2022-06-14 14:37:26.404903
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():

    class SchemaMetaclassTest(metaclass=SchemaMetaclass):
        def __init__(self):
            pass

    test = SchemaMetaclassTest()
    assert test is not None

# Generated at 2022-06-14 14:37:31.005922
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class TestSchema(Schema):
        name = Field(type="string")
        age = Field(type="integer")
        ref = Reference("Person")  # type: ignore

    assert not definitions
    set_definitions(TestSchema.fields["ref"], definitions)
    assert TestSchema.fields["ref"].definitions == definitions



# Generated at 2022-06-14 14:37:36.939282
# Unit test for constructor of class Schema
def test_Schema():
    class C(Schema):
        number = Field(type="integer")
        name = Field(type="string")
    try:
        c = C(dict(number=1))
    except Exception as error:
        print(error)
    else:
        print(c)


# Generated at 2022-06-14 14:37:47.045668
# Unit test for constructor of class Schema
def test_Schema():
    assert issubclass(Schema, Mapping)
    assert not hasattr(Schema, "abstract")
    assert Schema.__name__ == "Schema"
    assert Schema.__module__ == __name__
    assert not hasattr(Schema, "make_validator")
    assert not hasattr(Schema, "validate")
    assert not hasattr(Schema, "validate_or_error")
    assert not hasattr(Schema, "is_sparse")
    assert not hasattr(Schema, "__init__")
    assert not hasattr(Schema, "__eq__")
    assert not hasattr(Schema, "__getitem__")
    assert not hasattr(Schema, "__iter__")
    assert not hasattr(Schema, "__len__")
    assert not hasattr

# Generated at 2022-06-14 14:38:07.619978
# Unit test for function set_definitions
def test_set_definitions():
    class Book(Schema):
        author = String(max_length=20)

    class Author(Schema):
        name = String(max_length=20)
        bio = String(max_length=20)
        book = Reference(to='Book')

    class AuthorList(Schema):
        authors = Array(items=Reference(to='Author'))

    definitions = SchemaDefinitions()

    first_author = Author.validate({"name": "G. R. R. Martin", "bio": "Cool bio"})
    
    second_author = Author(
        name="J. K. Rowling",
        bio="Another cool bio",
    )

    book = Book(
        author="J. K. Rowling"
    )
    second_author.book = book


# Generated at 2022-06-14 14:38:17.208377
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    """
    Test if __iter__ method returns all attributes in a Schema object
    """
    # Set up test class
    class TestSchema(Schema):
        test_attr = Field(type="integer")
    # Try to make a Schema object with a value for test_attr
    test_schema = TestSchema(test_attr=2)
    # Test if __iter()__ returns a list with just one attribute name
    assert isinstance(iter(test_schema), list)
    assert len(iter(test_schema)) == 1
    assert 'test_attr' in iter(test_schema)


# Generated at 2022-06-14 14:38:21.870384
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class C(Schema):
        a = Field()
        b = Field()

    obj = C()
    assert len(obj) == 0

    obj = C({"a": 1})
    assert len(obj) == 1

    obj = C({"a": 1, "b": 2})
    assert len(obj) == 2



# Generated at 2022-06-14 14:38:24.846748
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    from typesystem.fields import String

    class User(Schema):
        name = String()

    user = User(
        name="John",
    )

    assert user["name"] == "John"


# Generated at 2022-06-14 14:38:25.427537
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    pass

# Generated at 2022-06-14 14:38:30.193321
# Unit test for constructor of class Schema
def test_Schema():
    class Example(Schema):
        myfield = Field(type=int)
    example = Example(myfield=3)
    assert example.myfield == 3
    with pytest.raises(TypeError):
        Example(myfield='3')
    with pytest.raises(TypeError):
        Example(myfield2=2)
    with pytest.raises(TypeError):
        Example(myfield=3, myfield2=2)

# Generated at 2022-06-14 14:38:32.746229
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class MySchema(Schema):
        pass
    a = MySchema()
    assert repr(a) == "MySchema()"

# Generated at 2022-06-14 14:38:38.709049
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        name = Field(type=str)

    person = Person(name="joe")
    assert dict(person)["name"] == "joe"

    class Person(Schema):
        name = Field(type=str)

    person = Person(name="joe")
    invalid_key = "age"
    __tracebackhide__ = True
    with pytest.raises((KeyError, AttributeError)):
        dict(person)[invalid_key]


# Generated at 2022-06-14 14:38:45.501335
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    animal_schema = Schema.make_validator()
    animal_schema.properties["name"] = Field(str)
    animal_schema.properties["number"] = Field(int)

    class Animal(Schema):
        name = Field(str)
        number = Field(int)

    assert(Animal({'name': 'Nasreddine', 'number': 1}) == Animal({'name': 'Nasreddine', 'number': 1}))
    assert(Animal({'name': 'Nasreddine', 'number': 1}) != Animal({'name': 'Nasreddine', 'number': 10}))

    v1 = Schema({'name': 'Nasreddine', 'number': 1})
    v2 = Schema({'name': 'Nasreddine', 'number': 10})

# Generated at 2022-06-14 14:38:57.402817
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class A(Schema):
        a = String(default="a")
        b = String(default="b")
        c = String(default="c")
    a = A()
    assert a == A(a="a", b="b", c="c")
    assert a != A()
    assert a != A(a="a", b="b", c="a")
    assert a == A(a="a", b="b")
    assert a != A(a="a", b="b", c="c")

    class B(Schema):
        a = String(default="a")
        b = String(default="b")
        c = String(default="c")
    b = B()
    assert b == B(a="a", b="b", c="c")
    assert b != B()

# Generated at 2022-06-14 14:39:25.239207
# Unit test for function set_definitions
def test_set_definitions():
    def assert_set_definitions(
        field: "t.Any", expected_definitions: "t.Any"
    ) -> None:
        field = copy.deepcopy(field)
        definitions_to_set = copy.deepcopy(expected_definitions)
        set_definitions(field, definitions_to_set)
        assert definitions_to_set == expected_definitions
        assert field.definitions is expected_definitions

    assert_set_definitions(
        Reference("Item"), SchemaDefinitions(Item=None)
    )
    assert_set_definitions(
        Object(Item),
        SchemaDefinitions(
            Item=Object(properties={"name": String(max_length=100)})
        ),
    )

# Generated at 2022-06-14 14:39:34.520788
# Unit test for method validate of class Reference
def test_Reference_validate():
    class ExampleSchema(Schema):
        integer = Integer()

    # class ExampleSchema2 is an instance of ExampleSchema, thus in the dict definitions
    class ExampleSchema2(ExampleSchema, Schema):
        pass

    reference = Reference("ExampleSchema")
    reference.definitions = SchemaDefinitions()
    reference.definitions["ExampleSchema"] = ExampleSchema
    # value is an instance of the class ExampleSchema2
    value = ExampleSchema2(integer=11111)
    value = reference.validate(value, strict=False)
    assert isinstance(value, ExampleSchema)


# Generated at 2022-06-14 14:39:37.433751
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        a = Field()
        b = Field()
        c = Field()
    obj = TestSchema(a=5, b=5)
    assert list(obj.__iter__()) == ['a', 'b']

# Generated at 2022-06-14 14:39:47.623469
# Unit test for constructor of class Schema
def test_Schema():
    class Child(Schema):
        name = Field(type=str)

    class Parent(Schema):
        children = Array(items=Child)

    data = {
        "children": [
            {"name": "john"},
            {"name": "jane"},
            {"name": "jim"},
        ]
    }

    parent = Parent(data)
    assert parent.children[0].name == "john"
    assert parent.children[1].name == "jane"
    assert parent.children[2].name == "jim"
    assert parent.is_sparse is False

# Generated at 2022-06-14 14:39:48.711676
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert False, "Test not implemented."


# Generated at 2022-06-14 14:39:53.806534
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem import String
    from .schema import Schema
    class Book(Schema):
        title = String()
    book = Book.validate({"title": "The Stand"})
    assert isinstance(book, Book)
    assert book.title == "The Stand"
    assert book == Book({"title": "The Stand"})
    try:
        Reference.validate({"title": "The Stand"})
    except:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:40:04.934776
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        pass

    class Bar(Schema):
        pass

    class Baz(Schema):
        foo = Reference(to="Foo", allow_null=True)
        bar = Reference(to=Bar)
        baz = Array(
            items=[
                Reference(to="Foo"),
                Reference(to="Bar"),
            ]
        )
        baz2 = Array(
            items=Reference(to="Bar"),
        )

    definitions = SchemaDefinitions()
    set_definitions(Baz.fields["foo"], definitions)
    assert Baz.fields["foo"].to == "Foo"
    assert Baz.fields["foo"].definitions == definitions
    assert Baz.fields["bar"].to == Bar
    assert Baz.fields["bar"].definitions == definitions
    assert Baz.fields

# Generated at 2022-06-14 14:40:15.385371
# Unit test for constructor of class Schema
def test_Schema():

    import typesystem

    class TestSchema(typesystem.Schema):
        # initializing TestSchema fields
        name = typesystem.String()
        age = typesystem.Int()

    # function Schema.__init__
    # semantics:
    # if args:
    # NO_TEST
    # elif kwargs:
    #   # case True:
    #   case (1, 1): keyword arguments provided
    #   case (1, 0): no keyword arguments
    # else:
    # NO_TEST
    #   case True:
    #   case (1, 0): no arguments

    # initialize TestSchema
    init_test = TestSchema(name="test", age=99)
    # no args
    # NO_TEST
    # elif kwargs
    # case True: keyword args

# Generated at 2022-06-14 14:40:16.134263
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    pass


# Generated at 2022-06-14 14:40:28.542648
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    ref_1 = Reference("Target")
    set_definitions(ref_1, definitions)
    assert ref_1.definitions is definitions
    obj_1 = Object(properties={"field_1": ref_1})
    set_definitions(obj_1, definitions)
    assert ref_1.definitions is definitions
    arr_1 = Array(items=ref_1)
    set_definitions(arr_1, definitions)
    assert ref_1.definitions is definitions
    ref_2 = Reference("Target")
    set_definitions(ref_2, definitions)
    assert ref_2.definitions is definitions
    obj_2 = Object(properties={"field_1": ref_2, "field_2": obj_1})
    set_definitions(obj_2, definitions)


# Generated at 2022-06-14 14:40:46.249973
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    schema = Schema()
    # __iter__()
    assert list(schema.__iter__()) == []


# Generated at 2022-06-14 14:40:51.446104
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        field1 = Field()
    schema = TestSchema(field1="field1")
    assert repr(schema) == "TestSchema(field1='field1')"
    schema = TestSchema(field1="field1", field2="field2")
    assert repr(schema) == "TestSchema(field1='field1', field2='field2') [sparse]"

# Generated at 2022-06-14 14:40:52.548780
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
	pass
	

# Generated at 2022-06-14 14:40:55.793886
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    print("Schema - __eq__")
    schema1 = Schema()
    schema2 = Schema()

    assert(schema1 == schema2)


# Generated at 2022-06-14 14:41:08.037932
# Unit test for function set_definitions
def test_set_definitions():
    class F1(Field):
        pass

    class F2(Field):
        pass

    class F3(Field):
        pass

    class F4(Field):
        pass

    class F5(Field):
        pass

    class A1(Array):
        items: Field = F1()

    class O1(Object):
        properties: typing.Dict[str, Field] = {
            "f2": F2(),
            "f3": F3(),
        }

    class R1(Reference):
        to: str = "O2"

    class O2(Object):
        properties: typing.Dict[str, Field] = {
            "f4": F4(),
            "f5": F5(),
            "r1": R1(),
        }

    definitions = SchemaDefinitions()

# Generated at 2022-06-14 14:41:12.094789
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
  from typesystem.fields import String, Integer

  class User(Schema):
    id = Integer(maximum=255)
    name = String(max_length=255)
    email = String(format="email")

  user = User(id=1, name="John Doe", email="john.doe@example.com")
  assert list(iter(user)) == ['id', 'name', 'email']


# Generated at 2022-06-14 14:41:18.954242
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    if __name__ != "typesystem.schema":
        pytest.skip()
    class A(Schema):
        a=String()
        b=String()
    a = A(a="a", b="b")
    assert set(a) == set(["a", "b"])
    assert set(A(a="a")) == set(["a"])
    assert set(A(b="b")) == set(["b"])
    assert set(A()) == set([])


# Generated at 2022-06-14 14:41:23.467820
# Unit test for function set_definitions
def test_set_definitions():
    class Address(Schema):
        city = Field()

    class Person(Schema):
        name = Field()
        address = Reference(Address)

    d = SchemaDefinitions()

    set_definitions(Person.make_validator(), d)
    assert 'Address' in d

# Generated at 2022-06-14 14:41:33.298622
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.base import SimpleType
    from typesystem.exceptions import ValidationError
    from typesystem.fields import Integer, String

    # test 1
    class A(Schema):
        name = String()

    a1 = A(name='a1')
    a2 = A(name='a2')
    a3 = A(name='a1')

    assert a1 != a2
    assert a1 != a3
    assert a2 != a3

    # test 2
    class B(SimpleType):
        def __init__(self, name: str) -> None:
            self.name = name

        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            if isinstance(value, B):
                return value
            raise ValidationError("")


# Generated at 2022-06-14 14:41:44.436723
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class Post(Schema):
        title = Field(str)

    class Comment(Schema):
        text = Field(str)

    class CommentReference(Reference):
        def __init__(self, **kwargs: typing.Any) -> None:
            super().__init__("Comment", definitions=definitions, **kwargs)

    class PostWithComments(Schema):
        comments = Array(items=CommentReference())

    for reference_field in PostWithComments.fields.values():
        assert reference_field.definitions is definitions

    # Make sure that set_definitions doesn't duplicate/overwrite
    set_definitions(PostWithComments, definitions)
    for reference_field in PostWithComments.fields.values():
        assert reference_field.definitions is definitions

# Generated at 2022-06-14 14:42:02.098520
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class Example(Schema):
        foo = Integer()
        bar = String()
    example = Example(foo=1, bar='hello')
    list_ex = [key for key in example]
    assert list_ex == ['foo', 'bar']



# Generated at 2022-06-14 14:42:06.518506
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class MySchema(Schema):
        a = Field(int)
        b = Field(int, default=42)

    s = MySchema(a=1)
    assert repr(s) == "MySchema(a=1)"

# Generated at 2022-06-14 14:42:10.358718
# Unit test for constructor of class Schema
def test_Schema():
    s = Schema(a=3, b=4)
    # assert(s.a == 3)
    # assert(s.b == 4)

    s = Schema(c=7, a=2)
    assert(s.a == 2)

# Generated at 2022-06-14 14:42:15.250520
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    person = Person(name="John", age=38)

    assert person["name"] == "John" == person.serialize()["name"]
    assert person["age"] == 38 == person.serialize()["age"]



# Generated at 2022-06-14 14:42:19.280048
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        field1 = Field()
        field2 = Field()

    schema = TestSchema(field1="a", field2="b")
    assert schema.field1 == "a"
    assert schema.field2 == "b"

# Generated at 2022-06-14 14:42:23.813728
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from .serialization import serialize
    class RenamedSchema(Schema):
        a = Field(name="a-renamed")
        b = Field()
        c = Field()
    r = RenamedSchema(a="foo", c="bar")
    assert serialize(r) == {"a-renamed": "foo", "c": "bar"}

# Generated at 2022-06-14 14:42:27.695215
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class User(Schema):
        name = Field(str)

    user1 = User({"name": "jing"})
    user2 = User({"name": "jing"})
    assert user1 == user2


# Generated at 2022-06-14 14:42:39.382566
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Declare fields in class
    class Schema:
        fields = {
            "name": None,
            "created_at": None,
            "updated_at": None,
        }

    # Instantiate a schema
    schema = Schema()
    # Set values for fields
    schema.name = "name"
    schema.created_at = "2020-02-18T00:00:00"
    schema.updated_at = "2020-02-18T00:00:00"
    # Get dict of a schema
    values = dict(schema)
    # Check if dict of fields are same

# Generated at 2022-06-14 14:42:41.879094
# Unit test for constructor of class Schema
def test_Schema():
    import typesystem
    schema = typesystem.Schema(name="test")
    assert schema.name == "test"


# Generated at 2022-06-14 14:42:53.587898
# Unit test for method validate of class Reference
def test_Reference_validate():
    class User(Schema):
        age = Field(type=int)
        name = Field(type=str)
    class Role(Schema):
        role_name = Field(type=str)
        user = Reference(User)
    
    user1 = User(name="Leo", age=18)
    role1 = Role(role_name="developer", user=user1)

    try:
        role_valid = Role.validate(role1)
    except ValidationError:
        role_valid = False
    except TypeError:
        role_valid = False
    assert(role_valid == True)
    
    user2 = User(name="Leo")
    role2 = Role(role_name="tester", user=user2)

# Generated at 2022-06-14 14:44:01.912926
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    """Test for method __repr__ of class Schema.
    """
    schema = Schema(foo = int, bar = str)
    schema = Schema(foo = int, bar = str, definitions = {'Schema': Schema})
    schema = Schema(foo = int, bar = str, definitions = {'schema': schema})
    schema = Schema(foo = int, bar = str, definitions = {'schema': schema}, baz = bool)
    assert repr(schema) == "Schema(foo=1, bar='2', baz=True)"
    schema = Schema(foo = int, bar = str)
    schema = Schema(foo = int, bar = str, definitions = {'Schema': Schema})

# Generated at 2022-06-14 14:44:11.183449
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from collections import OrderedDict
    from typesystem import Integer, String
    from typesystem.compat import quote_plus
    import httpx
    from fastapi import FastAPI
    from pydantic.error_wrappers import ValidationError
    app = FastAPI()


    class Model(Schema):
        foo = String(title="Foo", max_length=254, description="Foo description")
        bar = Integer(title="Bar", description="Bar description")


    client = httpx.Client(app=app)

    @app.get("/")
    def root():
        return dict()
    response = client.get("/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == {}

    @app.put("/")
    def root():
        model