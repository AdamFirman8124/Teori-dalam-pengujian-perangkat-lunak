

# Generated at 2022-06-14 14:34:46.939757
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import Integer

    class Fruit(Schema):
        id = Integer()

    fruit = Fruit(id=5)
    assert fruit.id == 5
    assert fruit["id"] == 5



# Generated at 2022-06-14 14:34:54.369984
# Unit test for function set_definitions
def test_set_definitions():
    class SubSchema(Schema):
        field = String()

    class Schema1(Schema):
        schema = SubSchema()

    class Schema2(Schema):
        reference = Reference("Schema1")

    definitions = SchemaDefinitions()
    definitions["Schema1"] = Schema1
    definitions["Schema2"] = Schema2
    assert definitions["Schema1"].fields["schema"].fields["field"].definitions == definitions

if __name__ == "__main__":
    test_set_definitions()

# Generated at 2022-06-14 14:35:03.377984
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from datetime import datetime

    from typesystem.fields import DateTime

    class Event(Schema):
        start = DateTime()
        end = DateTime()
        dt = DateTime()

    event = Event(
        start=datetime(2020, 7, 10, 16, 30, 0),
        end=datetime(2020, 7, 10, 17, 15, 0),
    )
    assert repr(event) == "Event(start=datetime.datetime(2020, 7, 10, 16, 30), end=datetime.datetime(2020, 7, 10, 17, 15), dt=None) [sparse]"

# Generated at 2022-06-14 14:35:08.923211
# Unit test for method validate of class Reference
def test_Reference_validate():
    definitions = SchemaDefinitions()
    # idx = 0
    class Product(Schema, metaclass=SchemaMetaclass, definitions=definitions):
        id = Field(type="string", title="ID", description="Product ID")
        name = Field(
            type="string", title="Name", description="Product Name",default="Samsung"
        )

    class Category(Schema, metaclass=SchemaMetaclass, definitions=definitions):
        id = Field(type="string", title="ID", description="Category ID")
        name = Field(
            type="string", title="Name", description="Category Name",default="Mobile"
        )
        category_product = Field(
            type="array",
            title="Products",
            description="Products in Category",
            items=Reference("Product", definitions=definitions),
        )

# Generated at 2022-06-14 14:35:13.313863
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        first_name = String()
        last_name = String()

        def __repr__(self):
            return "{} {}".format(self.first_name, self.last_name)
    assert repr(Person(first_name="Joe", last_name="Blow")) == "Joe Blow"


# Generated at 2022-06-14 14:35:16.649594
# Unit test for function set_definitions
def test_set_definitions():
    ref_field = Reference("to")
    arr_field = Array(items=ref_field)

    sch_def_dict = SchemaDefinitions()
    set_definitions(arr_field, sch_def_dict)
    assert sch_def_dict["to"] is Reference("to")

# Generated at 2022-06-14 14:35:24.392983
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # 1.
    class Foo(Schema):
        id = Integer(primary_key=True)
        bar = String(required=False)

    foo = Foo(id=5, bar="x")
    assert foo["id"] == 5
    assert foo["bar"] == "x"

    # 2.
    class Foo(Schema):
        id = Integer(primary_key=True)
        bar = String(required=False)

    foo = Foo(id=5)
    assert foo["id"] == 5
    assert foo["bar"] is None
    try:
        print(foo["x"])
    except KeyError as e:
        print("except:", e.args[0])

    # 3.
    class Foo(Schema):
        id = Integer(primary_key=True)

# Generated at 2022-06-14 14:35:29.682648
# Unit test for method validate of class Reference
def test_Reference_validate():
    class Person(Schema):
        name = String()
        age = Integer()

    class PersonReference(Schema):
        person = Reference(Person)

    person = Person(name="John Doe", age=42)
    person_reference = PersonReference(person=person)
    assert person_reference.validate()

# Generated at 2022-06-14 14:35:32.779904
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        foo = 'bar'
        name = 'some name'
    assert len(TestSchema({'foo': 'baz'})) == 1


# Generated at 2022-06-14 14:35:37.977111
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        a = Field(type='string')
        b = Field(type='string')
        c = Field(type='string')
    assert len(TestSchema(a = 'aaa', b = 'bbb')) is 2
    assert len(TestSchema(a = 'aaa', b = 'bbb', c = 'ccc')) is 3



# Generated at 2022-06-14 14:35:57.376475
# Unit test for method validate of class Reference
def test_Reference_validate():
    assert Reference('test').validate(1) == 1
    assert Reference('test').validate('str') == 'str'
    assert Reference('test').validate(None) == None
    assert Reference('test').validate(0.0) == 0.0
    assert Reference('test').validate(['a', 'b', 'c']) == ['a', 'b', 'c']
    assert Reference('test').validate({'key':'value'}) == {'key':'value'}
    try:
        Reference('test').validate(None, strict=True) == None
    except ValidationError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 14:36:06.294908
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class User(Schema):
        id = Field(type=int)
        name = Field(type=str)

    u = User(id=1, name="xiao")
    assert next(iter(u)) == "id"
    assert next(iter(u)) == "name"

    u = User(id=1)
    assert next(iter(u)) == "id"

    u = User(name="xiao")
    assert next(iter(u)) == "name"

    u = User()
    with pytest.raises(StopIteration):
        next(iter(u))


# Generated at 2022-06-14 14:36:15.285481
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    ''' Unit test for method __repr__ of class Schema
     '''
    from typesystem.fields import String, Integer, Boolean
    # Test example in the docstring of class Schema
    class Post(Schema):
        id = Integer(description="Identifier for the post.")
        name = String(max_length=255)
        is_published = Boolean(default=True)
    print('Class Post:',repr(Post))

    post = Post(name="How to type check your Python", id=1234)
    print('Instance of Post:', repr(post))
    # Test example in the docstring of __repr__ of class Schema
    class Author(Schema):
        name = String(max_length=255)
        id = Integer(description="Identifier for the post.")

# Generated at 2022-06-14 14:36:23.856378
# Unit test for function set_definitions
def test_set_definitions():
    string_field = Reference("str", title="str")
    array_field = Array(items=string_field)
    inner_field = Object(properties={"array_field": array_field})
    outer_field = Object(properties={"inner_field": inner_field})
    definitions = SchemaDefinitions()

    set_definitions(outer_field, definitions)

    assert outer_field.definitions is definitions
    assert inner_field.properties["array_field"].definitions is definitions
    assert inner_field.properties["array_field"].items.definitions is definitions



# Generated at 2022-06-14 14:36:30.820312
# Unit test for constructor of class Schema
def test_Schema():
    testDocument = Schema({"id": 1234, "name": "Somchay"})
    assert testDocument.id == 1234
    assert testDocument.name == "Somchay"
    assert testDocument.__eq__(Schema({"id": 1234, "name": "Somchay"}))
    assert repr(testDocument) == "Schema(id=1234, name='Somchay')"
    assert testDocument.is_sparse == False
    assert testDocument.__len__() == 2

# Generated at 2022-06-14 14:36:35.132451
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
  try:
    class Foo(metaclass=SchemaMetaclass):
      fields: typing.Dict[str, Field] = {}
  except Exception as e:
    print(f'Expected::No exception\nActual::{e}')
    
test_SchemaMetaclass___new__()


# Generated at 2022-06-14 14:36:40.410888
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    SchemaMetaclass.__new__.__annotations__["cls"]
    SchemaMetaclass.__new__.__annotations__["name"]
    SchemaMetaclass.__new__.__annotations__["bases"]
    SchemaMetaclass.__new__.__annotations__["attrs"]
    SchemaMetaclass.__new__.__annotations__["definitions"]
    SchemaMetaclass.__new__.__annotations__[""]
    SchemaMetaclass.__new__.__annotations__[None]


# Generated at 2022-06-14 14:36:45.046722
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.types import Integer

    class Test(Schema):
        i = Integer()

    assert Test(i=2) == Test(i=2)
    assert not Test(2) == Test(i=2)
    assert not Test(i=2) == Test(i=3)


# Generated at 2022-06-14 14:36:48.004661
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String()
        age = Integer()
        title = String(required=False)

    assert list(Person()) == ['name', 'age']


# Generated at 2022-06-14 14:36:50.482123
# Unit test for constructor of class Reference
def test_Reference():
    _test_Reference = Reference('test')
    assert _test_Reference.to == 'test'
    assert _test_Reference.definitions == None


# Generated at 2022-06-14 14:37:02.965365
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem import String

    class MySchema(Schema):
        field_1 = String()
        field_2 = String()

    assert set(MySchema()) == set()
    assert set(MySchema({"field_1": "value_1", "field_2": "value_2"})) == {"field_1", "field_2"}


# Generated at 2022-06-14 14:37:06.905562
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import typesystem
    class Person(typesystem.Schema):
        first_name = typesystem.String()
        last_name = typesystem.String()

    person = Person(first_name='Bob', last_name='Smith')

    x = str(person)
    assert x



# Generated at 2022-06-14 14:37:17.175679
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Example(Schema):
        m = Field()
    class Example2(Schema):
        m2 = Field()
    examples = [
        Example({'m': 1}),
        Example({'m': 1}),
        Example({'m': 1, 'extra': 2}),
        Example({'m': 1, 'extra': 2}),
        Example2({'m2': 1}),
        Example2({'m2': 1}),
    ]
    for i in range(100):
        examples.append({'m': 1})
    for i in range(100):
        examples.append({'m': 1, 'extra': 2})
    assert all(len(x) == 1 for x in examples)

# Generated at 2022-06-14 14:37:22.146143
# Unit test for function set_definitions
def test_set_definitions():
    class Foo(Reference):
        pass

    class Bar(Reference):
        pass

    class Base(Schema):
        foo: Foo
        bar: Bar

    definitions = SchemaDefinitions()
    set_definitions(Base.fields["foo"], definitions)
    definitions["Foo"] = Foo

    assert Base.fields["foo"].definitions is definitions
    assert Base.fields["bar"].definitions is None
    assert Base.fields["foo"].target is Foo

# Generated at 2022-06-14 14:37:25.571890
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        field = Field(type="number")

    obj = MySchema(field=10)
    assert list(iter(obj)) == ["field"]


# Generated at 2022-06-14 14:37:32.704864
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class XField(Field):
        pass

    class B(Schema):
        b1 = XField()
        b2 = XField()

    class A(Schema):
        a1 = XField()
        a2 = B()
        a3 = XField()

    a = A(a1 = 1, a2 = {'b1': 1, 'b2': 2})
    assert len(a) == 3
    a = A(a1 = 1, a2 = {'b1': 1, 'b2': 2}, a3 = 3)
    assert len(a) == 3
    a = A(a1 = 1, a2 = {'b1': 1, 'b2': 2, 'b3': 3})
    assert len(a) == 3



# Generated at 2022-06-14 14:37:38.286592
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class A(Schema):
        a = Field(String)
        b = Field(Boolean)

    a = A(a="a", b=True)

    assert set(iter(a)) == {"a", "b"}


# Generated at 2022-06-14 14:37:47.568794
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Schema, String

    class PersonSchema(Schema):
        first_name = String(title="First Name")

    class AddressSchema(Schema):
        street_address = String(title="Street Address")
        postcode = String(title="Postcode")

    class PersonAddressSchema(Schema):
        person = Reference(PersonSchema)
        address = Reference(AddressSchema)


# Generated at 2022-06-14 14:37:59.062370
# Unit test for constructor of class Schema
def test_Schema():
    new_Schema = Schema()
    new_Schema.test_dict = {"key1":"value1", "key2":"value2"}
    new_Schema.test_list = ["value1", "value2"]
    new_Schema.test_str = "This is a Schema test string."
    assert isinstance(new_Schema, Schema)
    assert new_Schema == new_Schema
    assert isinstance(new_Schema.test_dict, dict)
    assert new_Schema.test_dict == {"key1":"value1", "key2":"value2"}
    assert isinstance(new_Schema.test_list, list)
    assert new_Schema.test_list == ["value1", "value2"]
    assert isinstance(new_Schema.test_str, str)

# Generated at 2022-06-14 14:38:06.137214
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class EmployeeSchema(Schema):
        name = Field(type=str)
        department = Field(type=str)

    employee = EmployeeSchema(name="Alice")
    assert len(employee) == 1
    assert list(employee.items()) == [("name", "Alice")]

    employee.department = "Test"
    assert len(employee) == 2
    assert list(employee.items()) == [("name", "Alice"), ("department", "Test")]



# Generated at 2022-06-14 14:38:20.791124
# Unit test for constructor of class Schema
def test_Schema():
    class Movie(Schema):
        title = Field(str)
        director = Field(str)
        language = Field(str)
        year = Field(int)

    print(Movie(title = "The Shawshank Redemption", director = "Frank Darabont", language = "English", year = 1994))
    print(Movie({"title": "The Shawshank Redemption", "director": "Frank Darabont", "language": "English", "year": 1994}))



# Generated at 2022-06-14 14:38:24.532408
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Test(Schema):
        a = Field()
        b = Field()
        c = Field(default=3)
        
    obj = Test(a=1,b=2)
    res = len(obj)
    exp = 2
    assert res == exp

# Generated at 2022-06-14 14:38:29.756660
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class test1(Schema):
        a=String(default='a',max_length=3)
        b=String(default='b', max_length=3)
    assert len(list(test1())) == 2
    assert len(list(test1(a='c',b='d'))) == 2
    assert list(test1()) == ['a','b']
    assert list(test1(a='c',b='d')) == ['a','b']


# Generated at 2022-06-14 14:38:32.943534
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class ExampleSchema(Schema):
        pass
    assert ExampleSchema.fields == {}
    assert ExampleSchema.__name__ == 'ExampleSchema'
    return

# Generated at 2022-06-14 14:38:34.328985
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    pass
# Unit tests for method __getitem__ of class Schema

# Generated at 2022-06-14 14:38:38.312918
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class User(Schema):
        id = String()
        name = String()
        email = String()
    user = User({'id': '123', 'name': 'John Doe', 'email': 'j@d.com'})
    assert len(user) == 3

# Unit Test for method __iter__ of class Schema

# Generated at 2022-06-14 14:38:41.027170
# Unit test for constructor of class Reference
def test_Reference():
    schema = {"name" : "testSchema", "type" : "string"}
    assert(Reference(to="schema") == Reference(to="schema", definitions=schema))

if __name__ == "__main__":
    test_Reference()

# Generated at 2022-06-14 14:38:41.814913
# Unit test for method validate of class Reference
def test_Reference_validate():
    pass



# Generated at 2022-06-14 14:38:47.961517
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestSchema(Schema):
        fields = {
            "name": String(max_length=12),
            "age": Integer()
        }
    schema = TestSchema(name="a", age=30)
    assert schema["name"] == "a"
    assert schema["age"] == 30
    # Exception: KeyError
    with pytest.raises(KeyError):
        schema["missing"]



# Generated at 2022-06-14 14:38:54.883789
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem import Object, String
    from typesystem.validators import min_length

    class Person(Schema):
        name = String(validators=[min_length(2)])
        description = String()

    person = Person(name="Jeff", description="Jeff is fat.")

    iter(person)
    testresult = ["name", "description"]
    assert list(person.__iter__()) == testresult


# Generated at 2022-06-14 14:39:06.760466
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        example = Field()
    schema = ExampleSchema({"example": 'value'})
    len(schema) == 1

# Generated at 2022-06-14 14:39:10.926498
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class E(Schema):
        id = Integer()
        name = String()
    obj = E(id=1, name="a")
    assert len(obj) == 2
    assert 'id' in obj
    assert 'name' in obj


# Generated at 2022-06-14 14:39:23.394348
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import unittest
    import uuid
    from datetime import datetime
    
    class Author(Schema):
        name = String()
        email = String()
    
    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer()
    
    class Post(Schema):
        title = String()
        content = String()
        published = DateTime()
        author = Reference(Author)
        comments = Array(String())
        editors = Array(Reference(Person))
    

# Generated at 2022-06-14 14:39:34.610886
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Movie(Schema):
        name = Field(str)
        release_date = Field(str)
        director = Reference("Person")

    class Person(Schema):
        name = Field(str)
        date_of_birth = Field(str)

    movie = Movie(name = "Blade Runner", release_date = "06/25/1982", director = Person(name = "Ridley Scott", date_of_birth = "11/30/1937"))
    movie_dict = movie.__getitem__("director")
    assert(movie_dict == {"name": "Ridley Scott", "date_of_birth": "11/30/1937"})


# Generated at 2022-06-14 14:39:46.907584
# Unit test for constructor of class Schema
def test_Schema():
    assert Schema.__init__ is not object.__init__
    assert issubclass(Schema, dict)
    assert not issubclass(Schema, (list, tuple))
    Schema()
    assert Schema() == {}

    class Person(Schema):
        name = Field(str)
        age = Field(int)

    person = Person(name="Fred", age=21)
    assert person["name"] == "Fred"
    assert person["age"] == 21
    assert person == {"name": "Fred", "age": 21}
    assert "name" in person
    assert "age" in person
    assert len(person) == 2

    # Test equality
    assert Person(name="Fred", age=21) == Person(name="Fred", age=21)
    assert Person(name="Fred", age=21) != Person

# Generated at 2022-06-14 14:39:51.596017
# Unit test for method validate of class Reference
def test_Reference_validate():
    class User(Schema):
        name = String()
    class ReferenceReference(Schema):
        user = Reference(to=User)
    user = User(name='demo')
    assert ReferenceReference(user=user).validate({"user": {"name": 'demo'}}) == {'user': {'name': 'demo'}}


# Generated at 2022-06-14 14:39:55.763848
# Unit test for constructor of class Schema
def test_Schema():
    class A(Schema):
        b = Field()
        c = Field()
    a = A(b = 3, c = 4)
    assert a.b == 3
    assert a.c == 4


# Generated at 2022-06-14 14:39:56.876283
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    pass



# Generated at 2022-06-14 14:39:57.957113
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass


# Generated at 2022-06-14 14:40:04.533241
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    definitions = SchemaDefinitions()
    class Test(Schema, metaclass=SchemaMetaclass):
        name = String(max_length=100)

    class_name = Test.__name__

    assert len(Test.fields) == 1
    assert list(Test.fields.keys()) == ["name"]
    assert definitions[class_name] is Test
    assert definitions[class_name] is not None


# Generated at 2022-06-14 14:40:59.584314
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Foo(Schema):
        a = 1  
    foo = Foo()
    r = foo.__repr__() 
    assert r == "Foo(a=1)"
    class Foo(Schema):
        a = 1  
        b = 2
    foo = Foo()
    r = foo.__repr__() 
    assert r == "Foo(a=1, b=2)"
    class Foo(Schema):
        a = 1  
        c = 3
    foo = Foo()
    r = foo.__repr__() 
    assert r == "Foo(a=1) [sparse]"


# Generated at 2022-06-14 14:41:05.930165
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name=String()
        age=Integer()

    try:
        assert Person(name="David", age=7) == Person(name="David", age=7)
    except:
        print("Unit test for Schema's eq method have failed")
        return False
    else:
        print("Unit test for Schema's eq method have passed")
        return True


# Generated at 2022-06-14 14:41:17.889533
# Unit test for function set_definitions
def test_set_definitions():
    class_schema = {
        'properties': {
            'level1': {
                '$ref': '#/definitions/level1'
            }
        },
        'definitions': {
            'level2': {
                'properties': {
                    'level3': {
                        '$ref': '#/definitions/level3'
                    }
                }
            },
            'level1': {
                'properties': {
                    'level2': {
                        '$ref': '#/definitions/level2'
                    }
                }
            },
            'level3': {
                'properties': {
                    'level1': {
                        '$ref': '#/definitions/level1'
                    }
                }
            }
        }
    }

# Generated at 2022-06-14 14:41:19.005480
# Unit test for constructor of class Schema
def test_Schema():
    pass


# Generated at 2022-06-14 14:41:24.290483
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import typesystem
    
    class BookSchema(typesystem.Schema):
        author = typesystem.String()
        title = typesystem.String()
        year = typesystem.Integer()
    
    book = BookSchema({"author": "Dostoevsky", "title": "Crime and Punishment"})
    assert len(book) == 2

# Generated at 2022-06-14 14:41:33.840963
# Unit test for method validate of class Reference
def test_Reference_validate():
    import unittest
    import unittest.mock
    from typesystem.definitions import Definitions
    from typesystem.fields import Integer
    from typesystem.schema import Schema

    class MySchema(Schema):
        year = Integer(minimum=1900, maximum=2100)

    definitions = Definitions.of(MySchema)
    ref_field = Reference(to="MySchema")

    # Case 1, normal case:
    target = MySchema({'year':2019})
    value = ref_field.validate(target)

    # Case 2, normal case:
    target = MySchema(year=2019)
    value = ref_field.validate(target)

    # Case 3, normal case:
    value = ref_field.validate({'year':2019})
    # Case 4, normal case:


# Generated at 2022-06-14 14:41:36.790961
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import json

    class FooSchema(Schema):
        bar = Field()
        baz = Field()

        def __iter__(self):
            return iter(['bar', 'baz'])

    obj = FooSchema(bar=1, baz=2)
    assert json.dumps(obj) == '{"bar": 1, "baz": 2}'

test_Schema___iter__()


# Generated at 2022-06-14 14:41:39.686363
# Unit test for constructor of class Reference
def test_Reference():
    class Test(Schema):
        name = Field()

    reference = Reference('Test')
    assert reference.target_string == 'Test'
    assert type(reference.target) == type(Test)

# Generated at 2022-06-14 14:41:46.452036
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # Test for equality
    class A(Schema):
        a = String()
        b = String()

    class B(Schema):
        b = String()
        c = String()

    a1 = A(a = "a", b = "b")
    a2 = A(a = "a", b = "b")
    b1 = B(b = "b", c = "c")
    assert a1 == a2
    assert a1 != b1

    # Test for sparse class
    class C(Schema):
        c = String()
        d = String()

    c1 = C(c = "c")
    c2 = C(c = "c")
    assert c1.is_sparse
    assert c1 == c2

    # Test for non-sparse class

# Generated at 2022-06-14 14:41:57.871494
# Unit test for method validate of class Reference
def test_Reference_validate():
    from typesystem.fields import String
    from typesystem.definitions import definitions

    class C(Schema):
        x = String(name="x")
        y = String(name="y")

    class B(Schema):
        y = String(name="y")
        z = String(name="z")
        a = Reference("C", name="a")

    class A(Schema):
        a = Reference("B", name="a", definitions=definitions)

    c = C(x="1", y="2")
    b = B(y="2", z="3", a=c)
    a = A(a=b)

# Generated at 2022-06-14 14:42:23.216074
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
  # _ = importlib.reload(sys.modules['typesystem.schemas'])
  from typesystem.schemas import Schema
  # _ = importlib.reload(sys.modules['typesystem.fields'])
  from typesystem.fields import Boolean
  class MySchema(Schema):
    a = Boolean()
    b = Boolean()
  ms = MySchema(a=True,b=False)
  # expected: __getitem__(a) == True
  assert (ms['a'] == True)

test_Schema___getitem__()

# Generated at 2022-06-14 14:42:33.204059
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.base import String, Boolean

    class Person(Schema):
        name = String(required=True)
        age = String()
        alive = Boolean(required=True)

    person = Person(name='Cecilia', age='28', alive=True)

    for key, value in person.items():
        print(f"{key!r} -> {value!r}")

    # name -> 'Cecilia'
    # age -> '28'
    # alive -> True

    # validating empty string is valid
    print(Person().validate({
        'name': '',
        'alive': True
    }))


# Generated at 2022-06-14 14:42:37.817984
# Unit test for method validate of class Reference
def test_Reference_validate():
    test_value = {'id':'ciao', 'type':'hello'}
    test_schema = {'id':String(min_length=3), 'type':String()}
    test_Reference = Reference(test_schema)
    assert test_Reference.validate(test_value) == test_value

# Generated at 2022-06-14 14:42:50.090007
# Unit test for method validate of class Reference
def test_Reference_validate():
    class Person(Schema):
        name = String(max_length=10)

    class User(Schema):
        person = Reference(Person)

    user = User({"name": "xyz"}, strict=False)
    user_serialized = json.loads(json.dumps(user))
    print(user_serialized)
    assert user_serialized == {"person": {"name": "xyz"}}

    class Person(Schema):
        name = String(max_length=10)

    class User(Schema):
        person = Reference(Person)

    user = User({"name": "xyz"}, strict=False)
    user_serialized = json.loads(json.dumps(user))
    print(user_serialized)
    assert user_serialized == {"person": {"name": "xyz"}}




# Generated at 2022-06-14 14:42:51.183783
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert Schema.__len__(None) == 0

# Generated at 2022-06-14 14:42:58.767931
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class BaseSchema(Schema):
        base_field = Field()

    class SubSchema(BaseSchema):
        sub_field = Field()

    # Test __eq__ with two instances of the same class, but with different values.
    instance1 = SubSchema(base_field="base value", sub_field="sub value")
    instance2 = SubSchema(base_field="base value", sub_field="different sub value")
    assert instance1 != instance2

    # Test __eq__ with an instance and a dict object, when they have the same data.
    instance3 = SubSchema(base_field="base value", sub_field="sub value")
    dict_instance1 = {"base_field": "base value", "sub_field": "sub value"}
    assert instance1 == dict_instance1
    assert instance1 == instance3

# Generated at 2022-06-14 14:43:01.943239
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import typesystem
    class Student(Schema):
        name=typesystem.String(description="name of the student")
        school=typesystem.String(description="school of the student")
    stu=Student({'name':"Tom",'school':"BJUT"})
    assert set(iter(stu))=={"name","school"}


# Generated at 2022-06-14 14:43:05.067982
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Person(Schema):
        id = String()
        name = String()

    person = Person(id="1", name="John Doe")
    assert len(person) == 2



# Generated at 2022-06-14 14:43:15.461727
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    import typesystem
    class UserSchema(Schema):
        id = typesystem.Integer()
        name = typesystem.String(max_length=100)
        email = typesystem.String(max_length=100)

    user_1 = UserSchema(id=1, name="John Doe", email="john@example.com")
    user_2 = UserSchema(id=1, name="John Doe", email="john@example.com")
    user_3 = UserSchema(id=1, name="John Doe")
    user_4 = UserSchema(id=1, name="John Doe", email="john@gmail.com")
    assert user_1 == user_2
    assert user_2 == user_1
    assert user_1 != user_3
    assert user_3 != user_1
    assert user_1

# Generated at 2022-06-14 14:43:20.300227
# Unit test for constructor of class Schema
def test_Schema():
  def validate(cls, value, *, strict=False) -> Schema:
    validator = cls.make_validator(strict=strict)
    value = validator.validate(value, strict=strict)
    return cls(value)

  assert validate(Schema, {'a':1})


# Generated at 2022-06-14 14:43:42.134775
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Book(Schema):
        title = Field(type="string")
        author = Field(type="string")

    book = Book(title="Moby-Dick", author="Herman Melville")
    assert len(book) == 2



# Generated at 2022-06-14 14:43:50.944205
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from mimesis import Person
    from mimesis.enums import Gender
    person = Person()
    person.gender(gender=Gender.FEMALE)

    class PersonSchema(Schema):
        name = Field(type_=str)
        surname = Field(type_=str)
        dob = Field(type_=str)
        age = Field(type_=int)
        gender = Field(type_=str)
        permissions = Field(type_=list)

    person_schema = PersonSchema(person)
    expected = ['name', 'surname', 'dob', 'age', 'gender', 'permissions']
    result = list(person_schema.__iter__())
    assert result == expected


# Generated at 2022-06-14 14:43:58.711477
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    test_obj = Schema(name='a', value=None)
    assert test_obj['name'] == 'a'
    assert test_obj['value'] == None
    test_obj = Schema(name='a', value=1)
    assert test_obj['name'] == 'a'
    assert test_obj['value'] == 1
    test_obj = Schema(name='a', value=1, T=1)
    assert test_obj['name'] == 'a'
    assert test_obj['value'] == 1
    assert test_obj['T'] == 1


# Generated at 2022-06-14 14:44:02.843405
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    if True:
        class ExampleSchema(Schema):
            boo = String()
            foo = String()
    expected_value = ['boo', 'foo']
    actual_value = list(Schema().__iter__())
    assert expected_value == actual_value


# Generated at 2022-06-14 14:44:07.495114
# Unit test for constructor of class Schema
def test_Schema():
    assert issubclass(Schema, Mapping)
    assert Schema.__name__ == 'Schema'
    assert isinstance(Schema.__doc__, str)
    assert Schema.__module__ == 'typesystem'
    assert Schema.__bases__ == (dict,)
    assert Schema.__dict__['fields'] == {}
    s = Schema()
    assert isinstance(s, Schema)
    assert isinstance(s, Mapping)
    assert isinstance(s, dict)
    assert s == {}
    assert len(s) == 0


# Generated at 2022-06-14 14:44:12.908236
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    d = Schema(a = 'a',b = 'b',c = 'c')
    assert len(d) == 3
    d = Schema(a = 'a',b = 'b')
    assert len(d) == 2
    d = Schema()
    assert len(d) == 0
