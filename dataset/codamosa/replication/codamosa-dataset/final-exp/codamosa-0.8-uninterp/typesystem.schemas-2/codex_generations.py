

# Generated at 2022-06-14 14:34:51.247463
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    @add_method(Schema, '__repr__')
    def __repr__(self):
        class_name = self.__class__.__name__
        arguments = {key: getattr(self, key) for key in self.fields.keys() if hasattr(self, key)}
        argument_str = ", ".join([f'{key}={value!r}' for key, value in arguments.items()])
        sparse_indicator = ' [sparse]' if self.is_sparse else ''
        return f'{class_name}({argument_str}){sparse_indicator}'

# Generated at 2022-06-14 14:34:54.908371
# Unit test for function set_definitions
def test_set_definitions():
    from . import User
    def_ = SchemaDefinitions()
    assert len(def_) == 0
    set_definitions(User.make_validator(), def_)
    assert len(def_) == 1
    assert def_['User'] == User


# Generated at 2022-06-14 14:34:59.864147
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        id = Field()
        name = Field()
        age = Field()

    class Address(Schema):
        id = Field()
        name = Field()
        postcode = Field()

    class House(Schema):
        address = Reference(to=Address)
        tenant = Reference(to=Person)

    definitions = SchemaDefinitions()
    set_definitions(House.address, definitions)
    assert definitions

    definitions = SchemaDefinitions()
    set_definitions(House.tenant, definitions)
    assert definitions

# Generated at 2022-06-14 14:35:05.344778
# Unit test for function set_definitions
def test_set_definitions():
    class Definitions(SchemaDefinitions):
        pass
    definitions = Definitions()
    reference = Reference("MyType")
    assert reference.definitions is None
    set_definitions(reference, definitions)
    assert reference.definitions is definitions # pylint: disable=comparison-with-callable

# Generated at 2022-06-14 14:35:10.506370
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer

    class Person(Schema):
        id = Integer(minimum=0, maximum=100)

    assert Person(id=100) == Person(id=100)
    assert Person(id=100) != Person(id=200)
    assert Person(id=100) != Person()
    assert Person(id=100) != {}


# Generated at 2022-06-14 14:35:14.100453
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestSchema(Schema):
        test = Field(type="string")

    s = TestSchema.validate({"test": "s"}, strict=True)
    assert s.fields.__getitem__("test") == "s"


# Generated at 2022-06-14 14:35:20.626343
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class ThreeD(Schema):
        x = Field(type="number")
        y = Field(type="number")
        z = Field(type="number")

    three_d = ThreeD(x=5, y=6, z=7)
    assert three_d["x"] == 5
    assert three_d["y"] == 6
    assert three_d["z"] == 7

    with pytest.raises(KeyError):
        three_d["w"]

    with pytest.raises(KeyError):
        three_d["__dict__"]



# Generated at 2022-06-14 14:35:22.712296
# Unit test for constructor of class Schema
def test_Schema():
    schema = Schema(x = 5, y = 6)
    assert(schema.x == 5)
    assert(schema.y == 6)


# Generated at 2022-06-14 14:35:30.994418
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import String

    class Person(Schema):
        name = String(max_length=100)
        age = String(max_length=100, required=False)

    person = Person(name="Bob")
    assert len(person) == 1

    assert person == Person(name="Bob")

    assert len(Person()) == 0

    assert Person() != person

    assert len(Person(name="Bob", age="35")) == 2

    assert Person(name="Bob") == Person(name="Bob")

    assert Person() != Person(name="Bob")



# Generated at 2022-06-14 14:35:37.097068
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import typesystem
    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()
    p1=Person(name="U", age=18)
    p2=Person(name="U", age=18)
    p3=Person(name="U", age=19)
    assert p1==p2 and p2==p1
    assert p1!=p3 and p3!=p1


# Generated at 2022-06-14 14:35:50.002947
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    obj = Schema()
    length = len(obj)
    assert length == 0, f"expect length == 0: got {length}"
    print(f"length: {length}")


# Generated at 2022-06-14 14:35:56.716117
# Unit test for function set_definitions
def test_set_definitions():
    from typesystem.definition import Definition

    class TestDefinition(Definition):
        name = Field(str)

    definitions = SchemaDefinitions({1: TestDefinition})

    class TestSchema(Schema):
        foo = Field(str)
        bar = Array(items=Reference(1))

    set_definitions(TestSchema, definitions)
    assert TestSchema.bar.items == definitions[1]

# Generated at 2022-06-14 14:35:59.808638
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Test(Schema):
        name = 'name'
        age = 42
    instance = Test(name='Paul')
    assert list(instance) == ['name']



# Generated at 2022-06-14 14:36:03.600800
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        age = Field(int)
    assert Person(name="Alice", age=24) == Person({"name": "Alice", "age": 24})


# Generated at 2022-06-14 14:36:05.370463
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert not hasattr(Schema, "__iter__")

# Generated at 2022-06-14 14:36:08.578826
# Unit test for constructor of class Schema
def test_Schema():
    # Create a schema class for testing
    class MySchema(Schema):
        test = Field()

    want = MySchema({"test": 1})
    got = MySchema(test=1)

    assert want == got


# Generated at 2022-06-14 14:36:17.600779
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class A(Schema):
        id = str
        name = str
        age = int
        weight = float
    assert len(A(id='id', name='name', age=1, weight=80.7)) == 4
    assert len(A(id='id', name='name', weight=80.7)) == 3 # when missing field 'age'
    assert len(A(name='name', age=1, weight=80.7)) == 3 # when missing field 'id'
    assert len(A(id='id', age=1, weight=80.7)) == 3 # when missing field 'name'
    assert len(A(id='id', name='name', age=1)) == 3 # when missing field 'weight'
    assert len(A(id='id', name='name', age=1, weight=80.7)) == 4

# Generated at 2022-06-14 14:36:26.576533
# Unit test for constructor of class Schema
def test_Schema():
    # Initialize attributes of class Schema with default values.
    fields_dict = {}
    attrs_dict = {
        'fields': fields_dict
    }
    args_list = []
    kwargs_dict = {}

    # Use class.
    obj = Schema.__new__(Schema, 'Schema', (), attrs_dict)

    # Instantiate object from constructor of class Schema.
    object = Schema(*args_list, **kwargs_dict)
    assert object != None
    assert type(object) ==  Schema



# Generated at 2022-06-14 14:36:27.924992
# Unit test for constructor of class Reference
def test_Reference():
    def_dict = SchemaDefinitions()


# Generated at 2022-06-14 14:36:29.170602
# Unit test for constructor of class Schema
def test_Schema():
    pass


# Generated at 2022-06-14 14:36:43.324902
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        age = Field(int, default=18)
        height = Field(float, default=0.0)

    p = Person(name="abc", height=1.77)
    assert p["name"] == "abc"
    assert p["age"] == 18
    assert p["height"] == 1.77
    assert len(p) == 3
    assert ("name" in p) and ("age" in p) and ("height" in p)


# Generated at 2022-06-14 14:36:44.283112
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    pass


# Generated at 2022-06-14 14:36:47.846107
# Unit test for method __len__ of class Schema
def test_Schema___len__():
  schema = Schema(a = int)
  assert len(schema) == 1
  #Check that len is 0 when there are no fields
  schema = Schema()
  assert len(schema) == 0


# Generated at 2022-06-14 14:36:54.472231
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    class Foo(Schema):
        bar = Reference("Bar")
    class Bar(Schema):
        baz = Reference("Baz")
    class Baz(Schema):
        pass

    set_definitions(Foo.fields["bar"], definitions)
    assert Foo.fields["bar"].definitions is definitions
    assert Foo.fields["bar"].target is Bar
    assert Bar.fields["baz"].definitions is definitions
    assert Bar.fields["baz"].target is Baz
    assert Baz.fields == {}

# Generated at 2022-06-14 14:37:01.031316
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # Setup
    class Person(Schema):
        id = Field(type="string")
        name = Field(type="string")
        age = Field(type="number")
    person = Person(
        id="1234567",
        name="John Smith",
        age=42,
    )
    expected = "Person(age=42, id='1234567', name='John Smith')"

    # Exercise
    actual = repr(person)

    # Verify
    assert actual == expected


# Generated at 2022-06-14 14:37:06.959314
# Unit test for constructor of class Schema
def test_Schema():
    # Test with no args
    try:
        Schema()
        assert False
    except TypeError:
        pass

    # Test args not dict
    try:
        Schema(1)
        assert False
    except TypeError:
        pass

    # Test kwargs
    try:
        Schema(a=1)
        assert False
    except TypeError:
        pass
    try:
        Schema(1, a=1)
        assert False
    except TypeError:
        pass

    # Test correct args
    assert Schema({})
    assert Schema({}, a=1)
    assert Schema({}, a=1)


# Generated at 2022-06-14 14:37:10.337235
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    try:
        Schema({"a": 1})
    except TypeError as error_:
        # Expected TypeError
        assert error and True
    else:
        # Unexpected success
        assert False



# Generated at 2022-06-14 14:37:14.113375
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = String()
        age = Integer()

    p = Person(name='john', age=10)
    assert repr(p) == "Person(name='john', age=10)"

# Generated at 2022-06-14 14:37:22.730529
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Set up a Schema class with all Field types
    class S(Schema):
        s = String()
        b = Boolean()
        f = Float(default=1.0)
        i = Integer(default=2)
        t = Time(default="12:34:56")

    # Check that __getitem__ returns the correct values
    s = S(s="foo")
    assert s["s"] == "foo"
    assert s["b"] is False
    assert s["f"] == 1.0
    assert s["i"] == 2
    assert s["t"] == "12:34:56"

    # Check that keys not found raise a KeyError
    with pytest.raises(KeyError):
        s["missing"]

    # Check that keys not set in the Schema instance return None

# Generated at 2022-06-14 14:37:27.674929
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0, maximum=100)
        occupation = String(max_length=100)

    fields = list(Person())
    assert fields == ['age', 'name', 'occupation']
    # TODO: add other tests


# Generated at 2022-06-14 14:37:42.675576
# Unit test for function set_definitions
def test_set_definitions():
    class Defined(Schema):
        field = Field(required=False)
    
    class Collection(Schema):
        foo = Reference(to="Defined")
        definitions = SchemaDefinitions({"Defined":Defined})

    assert Collection.fields["foo"].definitions == {"Defined":Defined}

# Generated at 2022-06-14 14:37:45.534287
# Unit test for constructor of class Reference
def test_Reference():
    class A(Schema):
        a = Field()

    A.validate({'a': 12})
    A.validate({'a': 12})
    A.validate({'a': 12})

# Generated at 2022-06-14 14:37:58.038750
# Unit test for constructor of class Schema
def test_Schema():
    import typesystem
    class Pet(typesystem.Schema):
        id = typesystem.Integer(description="The unique identifier for a pet", format="int64")
        name = typesystem.String(description="The name of the pet", max_length=100)
        photoUrls = typesystem.Array(description="The list of photo URLs, must be publicly accessible",
            items=typesystem.String())
        tags = typesystem.Array(items=typesystem.Reference(to="Tag"))
        status = typesystem.Enumeration(description="pet status in the store", enum=["available", "pending", "sold"], default="available")

    pet = Pet({"id": 1, "name": "Polly", "photoUrls": [], "status": "available"})
    assert pet.id == 1


# Generated at 2022-06-14 14:38:04.818242
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class_name = 'Schema'
    arguments = {'a': 1, 'b': 2}
    sparse_indicator = ' [sparse]'
    
    if arguments:
        argument_str = ', '.join([f'{key}={value!r}' for key, value in arguments.items()])
    
    print(f'{class_name}({argument_str}){sparse_indicator}')
    print()




# Generated at 2022-06-14 14:38:07.662351
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    Schema = type("Schema", (object,), {"fields": {"a": 1}})
    s = Schema(a=1)
    assert repr(s) == "Schema(a=1)"


# Generated at 2022-06-14 14:38:09.641404
# Unit test for constructor of class Schema
def test_Schema():
    assert issubclass(Schema, Mapping)
    assert issubclass(Schema, SchemaMetaclass)


# Generated at 2022-06-14 14:38:21.528852
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import typesystem
    from typesystem import Schema, fields
    from typesystem.structures import OrderedDict

    class Movie(Schema):
        budget = fields.Integer()
        genre = fields.String()

    movie = Movie({'budget': 100000})

    assert movie.is_sparse == True

    # dict
    movie_dict = dict(movie)
    assert movie_dict == {'budget': 100000}

    # ordered dict
    movie_ordered_dict = OrderedDict(movie)
    assert isinstance(movie_ordered_dict, OrderedDict)
    assert movie_ordered_dict.keys() == ['budget']
    assert movie_ordered_dict.values() == [100000]

    # using **
    movie_dict = dict(**movie)

# Generated at 2022-06-14 14:38:26.043091
# Unit test for constructor of class Reference
def test_Reference():
    # test_scalar_args_only
    target = Reference(to='foo')
    assert target.to == 'foo'

    # test_with_kwargs
    target = Reference(to='foo', name='foo_name')
    assert target.to == 'foo'
    assert target.name == 'foo_name'


# Generated at 2022-06-14 14:38:32.698729
# Unit test for function set_definitions
def test_set_definitions():
    from typesystem import String

    class Person(Schema):
        name = String()
        age = String()

    class MySchema(Schema):
        person = Reference("Person")

    definitions = SchemaDefinitions()
    set_definitions(MySchema.person, definitions)
    assert "Person" in definitions
    assert definitions["Person"] is Person
    assert MySchema.person.definitions is definitions

# Generated at 2022-06-14 14:38:38.667125
# Unit test for constructor of class Schema
def test_Schema():
    # Test without arguments
    class Test(Schema):
        name = Field(type="string")
    t = Test()
    assert isinstance(t, Schema)

    # Test with keyword arguments
    t = Test(name="Joe")
    assert isinstance(t, Schema)

    # Test with positional arguments
    t = Test({"name": "Joe"})
    assert isinstance(t, Schema)


if __name__ == "__main__":
    test_Schema()
    print("Done.")

# Generated at 2022-06-14 14:39:17.198753
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String()

    assert Person(dict(name="John")) == Person(name="John")
    assert Person(dict(name="John")) != Person(name="Johna")
    assert Person(dict(name="John")) != {"name": "John"}

    # The validation is done by the constructor
    try:
        Person(dict(name=2))
        assert False, "ValidationError not raised"
    except ValidationError as e:
        assert str(e) == r"'2' is not a string"

    try:
        Person(name=2)
        assert False, "ValidationError not raised"
    except TypeError as e:
        assert str(e) == "2 is an invalid keyword argument for Person()"


# Generated at 2022-06-14 14:39:24.531552
# Unit test for constructor of class Schema
def test_Schema():
    from components.object_formats import User
    # this is a validator and not a schema object
    validator = User.make_validator()
    assert validator.properties['name'].required == True
    assert validator.properties['lastname'].required == False
    assert validator.additional_properties == False
    assert validator.properties['name'].data_type == str

    # this is a schema object
    user = User(name = 'John', lastname = 'Doe')
    assert user.name == 'John'
    assert user.lastname == 'Doe'
    assert user.is_sparse() == False

    # check it's working in strict mode
    user = User(name = 'John', lastname = 'Doe', age = 12)
    # this will throw a ValidationError since we're in strict

# Generated at 2022-06-14 14:39:27.882076
# Unit test for constructor of class Reference
def test_Reference():
    print( Reference(to='a',definitions=None,required=True) )


# Generated at 2022-06-14 14:39:37.357609
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestSchema(Schema):
        foo = Field()
        _bar = Field()
        fizz = Field()

    s = TestSchema(foo=1, _bar=2, fizz=3)
    assert s["foo"] == 1
    assert s["fizz"] == 3
    assert s.is_sparse == False
    foo, fizz = s["foo"], s["fizz"]
    assert foo == 1
    assert fizz == 3
    _bar = s["_bar"]
    assert _bar == 2
    with pytest.raises(KeyError):
        s["nope"]
    s = TestSchema()
    assert s.is_sparse == True
    with pytest.raises(KeyError):
        s["foo"]


# Generated at 2022-06-14 14:39:46.624872
# Unit test for constructor of class Reference
def test_Reference():
    class MySchema(Schema):
        name = String()
    to_str = 'MySchema'
    to_obj = MySchema
    # This next line is needed for the Type Checker to be happy
    assert isinstance(to_obj, type)
    rs = Reference(to_str)
    ro = Reference(to_obj)
    s = MySchema(name="Bob")
    assert rs.validate(s) == ro.validate(s)
    assert rs.serialize(s) == ro.serialize(s)

# Generated at 2022-06-14 14:39:50.807045
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    def reference_test():
        class User(Schema):
            username = Field(types.string)
            email = Field(types.string)
            password = Field(types.string)
        class ProjectMember(Schema):
            user = Reference(User)
            role = Field(types.string)

        user = {
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': '$2a$10$X9egIeM2EvWf1c0hCZoJmeZoD05i0pf8.MAX0BX9k.Fv6KWU6O4Oa'
        }

        project_member = {
            'user': user,
            'role': 'owner'
        }


# Generated at 2022-06-14 14:40:02.305514
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Schema):
        pass

    class Definitions(SchemaDefinitions):
        pass

    definitions = Definitions()

    class Bar(Schema):
        reference = Reference("Foo", definitions=definitions)

    set_definitions(Bar.reference, definitions)
    assert Bar.reference.definitions is definitions

    class Bar(Schema):
        reference = Reference("Foo", definitions=definitions)
        array = Array(Reference("Foo", definitions=definitions))

    set_definitions(Bar.reference, definitions)
    set_definitions(Bar.array, definitions)
    assert Bar.reference.definitions is definitions
    assert Bar.array.items.definitions is definitions


if __name__ == "__main__":
    test_set_definitions()

# Generated at 2022-06-14 14:40:13.489793
# Unit test for constructor of class Schema
def test_Schema():
    class Nested(Schema):
        one = Field()
        two = Field()
    class Schema2(Schema):
        one = Field()
        two = Field()
        nested = Reference(to=Nested)
    class Schema1(Schema):
        one = Field()
        two = Field(default=lambda: {'a': 1})
        nested = Reference(to=Nested)
        schema2 = Reference(to=Schema2)
    definitions = SchemaDefinitions()
    s1 = Schema1(nested=Nested(one=1, two=2), schema2=Schema2(one=1, two=2), one=1)

# Generated at 2022-06-14 14:40:16.735171
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        email = Field(str)

    person = Person(name="Joe", email="joe@joe.com")
    assert isinstance(person, Person)
    assert person.name == "Joe"
    assert person.email == "joe@joe.com"


# Generated at 2022-06-14 14:40:23.973352
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from pprint import pprint
    import pytest

    # Arrange
    class M(Schema):
        a = Array(String, default=None)
        b = Boolean(default=False)

    m = M(a=['a', 'b', 'c'])

    # Act
    actual = len(m)

    # Assert
    assert actual == 1



# Generated at 2022-06-14 14:42:11.761004
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        a = 1
        b = 2

    s = ExampleSchema()
    assert len(s) == 0
    s.a = 3
    assert len(s) == 1
    s.b = 4
    assert len(s) == 2

# Generated at 2022-06-14 14:42:16.727592
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem import Integer, String

    class User(Schema):
        username = String(max_length=255)
        age = Integer(minimum=0, maximum=200)

    user1 = User(username="monty", age=42)
    user2 = User(username="monty", age=42)
    assert user1 == user2

# Generated at 2022-06-14 14:42:25.271103
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        first_name = String(required=True)
        last_name = String(required=True)
        age = Int()
        is_alive = Boolean(required=True)
        children = Array(String(), default=[])

    if __name__ == "__main__":
        import sys
        from typesystem import parse_schema
        from .functools import print_schema_details

        print_schema_details(parse_schema(sys.argv[1], format="yaml"))
        exit()

    s = MySchema(first_name="John", last_name="Doe", age=42)
    assert set(s) == {'first_name', 'last_name', 'age'}


# Generated at 2022-06-14 14:42:28.900311
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    kwargs = {
        'value': '123',
    }
    obj = Schema(**kwargs)
    # Test len(obj) == 0
    assert len(obj) == 0


# Generated at 2022-06-14 14:42:33.966564
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class MySchema(Schema):
        name = Field(type="text")
        age = Field(type="integer")
    schema = MySchema.validate({'name': 'ray', 'age': 18})
    assert len(schema) == 2


# Generated at 2022-06-14 14:42:41.945883
# Unit test for constructor of class Reference
def test_Reference():
    class Person(Schema):
        name = Reference("Identity")
        age = Reference(Identity)
    assert isinstance(Person.fields['name'],Reference)
    assert isinstance(Person.fields['age'],Reference)
    assert Person.fields['name'].to == 'Identity'
    assert Person.fields['age'].to == Identity
    assert Person.fields['name']._target_string == 'Identity'
    assert Person.fields['age'].target == Identity
    # test __init__
    assert Person.fields['name'].definitions is None
    assert Person.fields['age'].definitions is None
    assert Person.fields['name'].allow_null
    assert Person.fields['age'].allow_null



# Generated at 2022-06-14 14:42:48.965605
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class NewComplexType(Schema):
        name = String(min_length=1)
        expiry = Date()
    schema = NewComplexType({"name": "ABC", "expiry": datetime.date(2020, 2, 1)})
    assert schema["name"] == "ABC"
    assert schema["expiry"] == datetime.date(2020, 2, 1)


# Generated at 2022-06-14 14:42:53.847488
# Unit test for function set_definitions
def test_set_definitions():
    class Item(Schema):
        title = Field()
    class List(Schema):
        items = Array(Reference("Item"))

    definitions = SchemaDefinitions()
    List.make_validator(definitions=definitions)

    assert definitions['List'] == List
    assert definitions['Item'] == Item

if __name__ == "__main__":
    test_set_definitions()

# Generated at 2022-06-14 14:42:57.434493
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String()

    p = Person(name='name1')
    assert ['name'] == list(p.__iter__())

    p = Person(name=None)
    assert ['name'] == list(p.__iter__())

    p = Person()
    assert [] == list(p.__iter__())


# Generated at 2022-06-14 14:43:08.636528
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():

    class TestSchemaMetaclass___new__(Schema, metaclass=SchemaMetaclass):
        first_name = String(max_length=255)
        last_name = String(max_length=255)
        age = Integer()

    print(TestSchemaMetaclass___new__.fields)
    # {'first_name': String(max_length=255, min_length=None, pattern=None), 'last_name': String(max_length=255, min_length=None, pattern=None), 'age': Integer(minimum=None, maximum=None, exclusive_maximum=None, exclusive_minimum=None)}

    print(TestSchemaMetaclass___new__.__mro__)
    # (<class 'tests.fields.tests_schema.test_SchemaMetaclass___new__.TestSchemaMet