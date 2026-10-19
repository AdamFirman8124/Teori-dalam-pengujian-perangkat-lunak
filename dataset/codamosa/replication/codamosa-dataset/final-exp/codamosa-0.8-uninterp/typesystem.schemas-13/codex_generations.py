

# Generated at 2022-06-14 14:34:41.226077
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Type1(Schema, strict = True):
        field1 = Field()
        field2 = Field()

    Type1.field1.is_required = True
    Type1.field2.is_required = True

    class Type2(Type1):
        field3 = Field()

    Type2.field3.is_required = True
    
    print(Type2.fields)

# Generated at 2022-06-14 14:34:50.128674
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    print('start test_Schema___getitem__')
    from typesystem.fields import Integer, String
    from typesystem.exceptions import ValidationError
    class Person(Schema):
        name = String()
        age = Integer(default=21)

    person = Person({"name": "Jekyll"})
    assert person["name"] == "Jekyll"
    assert person["age"] == 21
    try:
        person["address"]
    except KeyError as error:
        print(error)

    try:
        Person({"age": "twenty-one"})
    except ValidationError as error:
        print(error)



# Generated at 2022-06-14 14:34:58.885352
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class DummyField(Field):
        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            super().__init__(*args, **kwargs)

    class DummySchema(
        Schema, metaclass=SchemaMetaclass, definitions=SchemaDefinitions()
    ):
        fields = {"foo": DummyField()}

    class DummySchema2(
        DummySchema, metaclass=SchemaMetaclass, definitions=SchemaDefinitions()
    ):
        fields = {"bar": DummyField()}

    class DummySchema3(
        DummySchema2,
        metaclass=SchemaMetaclass,
        definitions=SchemaDefinitions(),
    ):
        fields = {"baz": DummyField()}


# Generated at 2022-06-14 14:35:04.839450
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Demo(Schema):
        first_name = String(required=True)
        last_name = String(required=True)
    assert repr(Demo(first_name='John', last_name='Doe')) == "Demo(first_name='John', last_name='Doe')"


# Generated at 2022-06-14 14:35:08.131811
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    assert Reference("to").serialize("obj") == "obj"
    obj = Reference("to")
    assert obj.serialize("obj") == "obj"
    assert obj.serialize("obj") != obj


# Generated at 2022-06-14 14:35:09.109643
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    pass


# Generated at 2022-06-14 14:35:18.526487
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert Schema()['name'] == "Hello World"
    assert Schema(name="John Doe").name == "John Doe"
    assert Schema({'name': "John Doe"}).name == "John Doe"
    assert Schema(name="John Doe").__repr__() == "Schema(name='John Doe')"
    assert Schema(name="John Doe").__str__() == "{'name': 'John Doe'}"
    assert Schema(name="John Doe").__len__() == 1
    assert Schema(name="John Doe").__eq__(Schema(name="John Doe"))
    assert Schema(name="John Doe").__eq__(Schema(name="John Doe")) == True
    assert Schema(name="John Doe").__getitem__("name") == "John Doe"

# Generated at 2022-06-14 14:35:21.414485
# Unit test for constructor of class Reference
def test_Reference():
    class Foo(Schema):
        bar = Array(items=str)
        baz = Object(properties={"a": str, "b": int})
    ref = Reference(to=Foo)
    assert ref.target is Foo


# Generated at 2022-06-14 14:35:26.628528
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Bank1Account(Schema):
        account_number = String()
        name = String()
        balance = Number()
    
    s = Bank1Account(account_number="1234567890",
                     name="Sri Ram",
                     balance=10000)
    assert list(s) == ['account_number', 'name', 'balance']


# Generated at 2022-06-14 14:35:36.705500
# Unit test for constructor of class Reference
def test_Reference():
    from .fields import Any
    from .objects import Object
    from .schemas import Schema
    from .fields import Object as ObjectField
    from .fields import Reference as ReferenceField
    from .fields import String as StringField
    from .types import String
    from .fields import ValidationError
    from .utils import ValidationError as ValidationError2
    from .schemas import SchemaMetaclass
    from .schemas import SchemaDefinitions
    from .schemas import set_definitions


    class Property(Schema):
        title = StringField(required=True)
        size = StringField(choices=["small", "medium", "large"])


    class Person(Schema):
        name = StringField(required=True)
        prop = ReferenceField(Property)



# Generated at 2022-06-14 14:35:50.496524
# Unit test for constructor of class Schema
def test_Schema():
    assert issubclass(Schema, Mapping)
    assert issubclass(Schema, typing.Mapping)
    assert not issubclass(Schema, type)



# Generated at 2022-06-14 14:35:55.796159
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem import String, Number

    ref = Reference(
        "Person", definitions={"Person": Schema(name=String(), age=Number())}
    )

    assert ref.validate({"name": "Me", "age": 42}) == {"name": "Me", "age": 42.0}



# Generated at 2022-06-14 14:36:00.602952
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class MySchema(Schema):
        name = Field(str)
        age = Field(int, default=None)

    myObj = MySchema(name="Lara", age=18)
    print(repr(myObj))


test_Schema___repr__()



# Generated at 2022-06-14 14:36:03.112190
# Unit test for method validate of class Reference
def test_Reference_validate():
    test_data = {"name": "Somkiat"}
    result = Reference.validate(test_data, strict=False)
    assert result is None

# Generated at 2022-06-14 14:36:06.895704
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class S(Schema):
        a = Field()
        b = Field()

    s = S(a = 1, b = 2)
    assert len(s) == 2
    del s.a
    assert len(s) == 1



# Generated at 2022-06-14 14:36:11.050834
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
  if (not (1)):
    raise AssertionError
  if (not (1)):
    raise AssertionError
  if (not (1)):
    raise AssertionError
  if (not (1)):
    raise AssertionError
  if (not (1)):
    raise AssertionError

# Generated at 2022-06-14 14:36:18.716087
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import String
    from typesystem.schema import Schema
    s = Schema(other='b', name='a')
    assert str(repr(s)) == "Schema(name='a', other='b')"
    class MySchema(Schema):
        name = String()
        other = String()
    s = MySchema(other='b', name='a')
    assert str(repr(s)) == "MySchema(name='a', other='b')"
    s = MySchema(other='b')
    assert str(repr(s)) == "MySchema(other='b') [sparse]"


# Generated at 2022-06-14 14:36:26.819246
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem import String

    class Review(Schema):
        comment = String()

    reference = Reference(to="Review")
    assert reference.definitions is None
    assert reference.target_string == "Review"
    assert reference.target is None

    reference = Reference(to="Review", definitions={"Review": Review})
    assert reference.target_string == "Review"
    assert reference.target == Review

    reference = Reference(to=Review)
    assert reference.definitions is None
    assert reference.target == Review

# Generated at 2022-06-14 14:36:34.041367
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class TestSchemaMetaclass___new__(metaclass=SchemaMetaclass):
        foo = String()
        bar = String()
    assert TestSchemaMetaclass___new__.fields == {
        'foo': TestSchemaMetaclass___new__.foo,
        'bar': TestSchemaMetaclass___new__.bar
    }
    assert TestSchemaMetaclass___new__.__name__ == 'TestSchemaMetaclass___new__'

test_SchemaMetaclass___new__()


# Generated at 2022-06-14 14:36:42.800680
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class User(Schema):
        name = Field(str)
        age = Field(int)
    class Name(Schema):
        first_name = Field(str)
        last_name = Field(str)
    class Person(Schema):
        name = Field(Name)
        age = Field(int)
    u1 = User(name=u"Jim", age=33)
    u2 = User(name=u"Jim", age=33)
    u3 = User(name=u"James", age=33)
    u4 = User(name=u"Jim", age=34)
    u5 = User(name=u"Jim", age=33, address=u"100 Main St.")

# Generated at 2022-06-14 14:36:57.815598
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    class A(Schema):
        foo = String()

    assert A.fields.keys() == {"foo"}
    assert A().foo == ""



# Generated at 2022-06-14 14:37:05.082773
# Unit test for function set_definitions
def test_set_definitions():

    class M1(Schema):
        x = Reference("")
    class M2(Schema):
        y = Reference("")
    class M3(Schema):
        m1 = Object(properties={'x': Reference("")})

    definitions = SchemaDefinitions()

    set_definitions(M1, definitions)
    assert M1.fields['x'].definitions == definitions

    set_definitions(M2, definitions)
    assert M2.fields['y'].definitions == definitions

    set_definitions(M3, definitions)
    assert M3.fields['m1'].properties['x'].definitions == definitions
    assert M3.fields['m1'].definitions == definitions

# Generated at 2022-06-14 14:37:10.389865
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    s = Shema()
    class person(s):
        last_name = Field()
        first_name = Field()
        age = Field()
        p = person(last_name = 'last_name', first_name = 'first_name', age = 'age')
        assert len(p) == 3
    print("Schema.__len__ test successful")

# Generated at 2022-06-14 14:37:17.080994
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    # TODO: Create and set real values for all parameters
    first_value = ""
    second_value = ""
    third_value = ""
    # Invoke method
    try:
        return_value = Schema.__iter__(first_value, second_value, third_value)
    except Exception as e:
        # Test failure
        print(e)
    else:
        # Test success
        pass


# Generated at 2022-06-14 14:37:19.924644
# Unit test for constructor of class Schema
def test_Schema():
    class UserSchema(Schema):
        username=String()
    u=UserSchema(username='hong')
    print('test_Schema:',u.username)


# Generated at 2022-06-14 14:37:24.752600
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Book(Schema):
        title = 'title' 
        author = 'author'
    my_book = Book({'title':'Python','author':'SJ'})
    assert my_book['title'] == 'Python'

# Generated at 2022-06-14 14:37:32.320935
# Unit test for function set_definitions
def test_set_definitions():
    class ExampleSchema(Schema):
        a = Reference("B")
        b = Reference("C")
        c = Reference("D")
        d = Reference("E")

        class Meta:
            definitions = SchemaDefinitions()

    exampleschema = ExampleSchema()
    assert exampleschema.a.definitions == exampleschema.Meta.definitions
    assert exampleschema.b.definitions == exampleschema.Meta.definitions
    assert exampleschema.c.definitions == exampleschema.Meta.definitions
    assert exampleschema.d.definitions == exampleschema.Meta.definitions

test_set_definitions()

# Generated at 2022-06-14 14:37:45.002854
# Unit test for constructor of class Schema
def test_Schema():
    # TODO: mock the Expr, b/c it's a bit messy to get a valid expr for tests
    schem = Schema()
    assert not schem.is_sparse
    # try:
    #     schem.validate(1)
    #     assert 0
    # except:
    #     assert 1
    # try:
    #     schem.validate(None)
    #     assert 0
    # except:
    #     assert 1
    # try:
    #     schem.validate(1.0)
    #     assert 0
    # except:
    #     assert 1
    # try:
    #     schem.validate(True)
    #     assert 0
    # except:
    #     assert 1
    # try:
    #     schem.validate(False)

# Generated at 2022-06-14 14:37:52.266655
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        name = String(max_length=100)
        age = Integer(maximum=150)
        email = String(pattern=r"^.+@.+\..+$")

    p = Person(name='novo', age=10, email='a@b.com')
    l = list(p)
    assert l == ['name', 'age', 'email']

# Generated at 2022-06-14 14:38:01.690183
# Unit test for method validate of class Reference
def test_Reference_validate():
    definitions = SchemaDefinitions()
    class Event(Schema, metaclass=SchemaMetaclass, definitions=definitions):
        type = Reference("EventType")
        class EventType(Schema, metaclass=SchemaMetaclass, definitions=definitions):
            event_id = Reference("EventId")
            detail = Reference("EventDetail")
            class EventId(Schema, metaclass=SchemaMetaclass, definitions=definitions):
                creation_time = "2020-08-12T11:26:16.486099Z"
                event_type = "some_random_type"
            class EventDetail(Schema, metaclass=SchemaMetaclass, definitions=definitions):
                requestParameters = Reference("requestParameters")
                responseElements = Reference("responseElements")

# Generated at 2022-06-14 14:38:16.891085
# Unit test for function set_definitions
def test_set_definitions():
    foo_schema = Schema(
        definitions=SchemaDefinitions(),      
    )
    for i in range(1,5):
        set_definitions(foo_schema.fields['foo'+str(i)], foo_schema)

# Generated at 2022-06-14 14:38:22.312756
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = Field(type=str)

    class Employee(Schema):
        employee_id = Field(type=str)
        person = Reference(to="Person")

    employee_definition = Employee.make_validator()
    assert employee_definition.properties["person"].definitions is not None
    assert employee_definition.properties["person"].definitions["Person"] is Person

# Generated at 2022-06-14 14:38:28.704134
# Unit test for constructor of class Schema
def test_Schema():
    class Point(Schema):
        x = Field(type=int, required=True)
        y = Field(type=int, required=True)

    point = Point(x=2, y=3)
    print(point)
    point = Point({"x":2, "y":3})
    print(point)
    # TypeError: 'z' is an invalid keyword argument for Point()
    #point = Point(z=2)
    #print(point)
    point = Point(x=2)
    print(point)


# Generated at 2022-06-14 14:38:31.998465
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class FooSchema(Schema):
        x = Field(type="integer", required=True)
        y = Field(type="integer", required=True)
    data = {'x': 2, 'y': 3}
    s = FooSchema(data)

    assert sorted(list(s.__iter__())) == ['x', 'y']


# Generated at 2022-06-14 14:38:34.116962
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        a = 'b'
    assert len(TestSchema()) == 0
    assert len(TestSchema(a='b')) == 1


# Generated at 2022-06-14 14:38:37.848421
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class TestSchema(Schema, metaclass=SchemaMetaclass):
        field = Reference("TestReference")

    class TestReference(Schema, metaclass=SchemaMetaclass):
        test_field = str

    set_definitions(TestSchema.field, definitions)

# Generated at 2022-06-14 14:38:40.847108
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Example(Schema):
        field1 = int
        field2 = float
        field3 = float

    instance = Example(field1=1, field2=1.0, field3=1.0)
    assert len(instance) == 3


# Generated at 2022-06-14 14:38:42.730104
# Unit test for constructor of class Schema
def test_Schema():
    class TestSchema(Schema):
        x = Field()

    data = TestSchema({"x": 42})
    assert data.x == 42


# Generated at 2022-06-14 14:38:48.628192
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class User(Schema):
        id = Field()
        name = Field()
        age = Field()

    class Tweet(Schema):
        id = Field()
        text = Field()
        user = Reference(User)

    assert User(id=1, name="Adam", age=32) == User(id=1, name="Adam", age=32)
    assert not User(id=1, name="Adam", age=32) == User(id=1, name="Adam", age=44)
    assert Tweet(id=1, text="Hello world!", user=User(id=1, name="Adam", age=32)) == Tweet(
        id=1, text="Hello world!", user=User(id=1, name="Adam", age=32)
    )



# Generated at 2022-06-14 14:38:53.069240
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class User(Schema):
        full_name = String(max_length=255)

    admin = User(full_name="Test-Name")
    assert admin["full_name"] == "Test-Name"

# Generated at 2022-06-14 14:39:12.985380
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class FooSchema(Schema):
        bar = Field(String())
        baz = Field(Int())

    foo = FooSchema({'bar': 'bar'})
    assert list(foo) == ['bar']



# Generated at 2022-06-14 14:39:15.014730
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    schema = Schema({'a':1,'b':2})
    assert len(schema) == 2


# Generated at 2022-06-14 14:39:16.157512
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    pass


# Generated at 2022-06-14 14:39:24.436018
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name: str
        age: int

    person = Person(name='John', age=21)
    assert(person.name == 'John')
    assert(person.age == 21)

    person = Person({'name': 'John', 'age': 21})
    assert(person.name == 'John')
    assert(person.age == 21)

    person = Person(Person(name='John', age=21))
    assert(person.name == 'John')
    assert(person.age == 21)


# Generated at 2022-06-14 14:39:31.685563
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class S1(Schema):
        a = Field(str)
        b = Field(str)

    s1 = S1(a='1', b='2')
    s2 = S1(a='3', b='2')
    s3 = S1(a='3', b='2')

    assert s1 != s2
    assert s1 != s3
    assert s2 == s3

# Generated at 2022-06-14 14:39:39.113528
# Unit test for constructor of class Schema
def test_Schema():
    class Dummy(Schema):
        foo = Field()
        bar = Field(default="baz")

    assert Dummy({"foo": "test"}) == Dummy(foo="test")
    assert Dummy(Dummy(foo="test")) == Dummy(foo="test")
    assert Dummy(foo="test", bar="qux") == Dummy(foo="test", bar="qux")
    assert Dummy(bar="qux", foo="test") == Dummy(bar="qux", foo="test")
    assert Dummy(foo="test") == Dummy(foo="test", bar="baz")
    assert Dummy(foo="test") != Dummy(foo="other")



# Generated at 2022-06-14 14:39:48.615142
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        name = "TestSchema"
        field1 = Field()
        field2 = Field()

    schema1 = TestSchema(field1=1, field2=2)
    schema2 = TestSchema(field1=1, field2=3)
    schema3 = TestSchema(field1=1, field2=2)
    schema4 = dict(field1=1, field2=2)
    
    assert schema1 == schema3
    assert not schema1 == schema2
    assert not schema1 == schema4


# Generated at 2022-06-14 14:39:52.209189
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class SimpleSchema(Schema):
        name = Field()
        email = Field()
        age = Field()
    simple_schema = SimpleSchema(name='Durdan', email='durdan@mailinator.com', age=20)
    assert len(simple_schema) == 3

# Generated at 2022-06-14 14:39:59.389503
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class Foo(Schema):
        bar = Reference("Bar")

    class Bar(Schema):
        pass
        
    assert Foo.bar.definitions == None
    set_definitions(Foo.bar, definitions)
    assert Foo.bar.definitions != None
    assert Foo.bar.definitions == definitions
    assert Foo.bar.target_string == "Bar"
    assert Foo.bar.to == "Bar"

# Generated at 2022-06-14 14:40:04.030421
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    definitions["Foo"] = Schema
    definitions["Bar"] = Schema

    class MySchema(Schema):
        foo = Reference("Foo")
        bar = Reference("Bar")

    assert MySchema.foo.definitions == definitions
    assert MySchema.bar.definitions == definitions

# Generated at 2022-06-14 14:40:35.752021
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Foo(Schema):
        bar = 1
    assert repr(Foo()) == 'Foo()'


# Generated at 2022-06-14 14:40:42.342876
# Unit test for function set_definitions
def test_set_definitions():
    class TestField(Field):
        pass

    class TestReference(Reference):
        pass

    class TestSchema(Schema):
        test1 = TestField()
        test2 = TestReference("TestSchema")

    definitions = SchemaDefinitions()

    set_definitions(TestSchema, definitions=definitions)
    assert TestSchema.test2.target is TestSchema


# Unit tests for Schema

# Generated at 2022-06-14 14:40:46.189325
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    t0 = Schema()
    assert list(t0.__iter__()) == []
    t1 = Person(first_name="Nicole")
    assert list(t1.__iter__()) == ['first_name', 'last_name']


# Generated at 2022-06-14 14:40:57.213476
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    import copy
    def test_func(value, result):
        data = copy.deepcopy(value)
        schema = Schema(**data)
        assert len(schema) == result

# Generated at 2022-06-14 14:41:05.655588
# Unit test for method validate of class Reference
def test_Reference_validate():
    def validate(self: Reference, value: typing.Any, *, strict: bool = False) -> typing.Any:
        if value is None and self.allow_null:
            return None
        elif value is None:
            raise self.validation_error("null")
        return self.target.validate(value, strict=strict)
    s = Reference(to='target')
    s.target = Array()
    result = validate(s, ['hello'], strict=True)
    print(result)

# Generated at 2022-06-14 14:41:11.189104
# Unit test for function set_definitions
def test_set_definitions():

    class SchemaWithReference(Schema, metaclass=SchemaMetaclass):
        definitions = SchemaDefinitions()
        # Make sure the test doesn't fail if the string reference field is called definition
        definition = Reference("Test") 

    assert isinstance(SchemaWithReference.definition.definitions, SchemaDefinitions)

# Generated at 2022-06-14 14:41:20.915967
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem import Integer
    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer()

    p = Person(
        first_name="name1",
        last_name="name2",
        age=1,
    )

    assert p.first_name == "name1"
    assert p.last_name == "name2"
    assert p.age == 1

    p = Person(dict(
        first_name="name1",
        last_name="name2",
        age=1,
    ))

    assert p.first_name == "name1"
    assert p.last_name == "name2"
    assert p.age == 1

    class Person(Schema):
        first_name = String(default="default_fname")
        last_

# Generated at 2022-06-14 14:41:26.303039
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class User(Schema):
        first_name = String()
        last_name = String()
        age = Integer()

    user1 = User(first_name="Joe", last_name="Doe", age=10)
    user2 = User(first_name="Joe", last_name="Doe", age=10)
    assert user1 == user2


# Generated at 2022-06-14 14:41:31.669715
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # fixture ----
    class Example(Schema):
        field = int()
    # test case 1 ----
    example = Example(field=1)
    # verification 1 ----
    assert repr(example) == "Example(field=1)"
    # test case 2 ----
    example = Example()
    # verification 2 ----
    assert repr(example) == "Example([sparse])"


# Generated at 2022-06-14 14:41:43.744851
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ButtonType(Schema):
        label = String()
        work_item_name = String()
        color = String()
        icon = String(default=None)
        action = String()

    # without icon
    button_value = {
        'label': 'Add to support group',
        'work_item_name': 'Support Issue',
        'color': '#0078d4',
        'action': 'create_support_issue'
    }
    button = ButtonType(button_value)
    assert repr(button) == 'ButtonType(label=\'Add to support group\', work_item_name=\'Support Issue\', color=\'#0078d4\', action=\'create_support_issue\')'

    # with icon

# Generated at 2022-06-14 14:42:08.286863
# Unit test for method validate of class Reference
def test_Reference_validate():
    # Preparation
    field = Reference("Example")
    value = Example()
    strict = False
    # Action
    result = field.validate(value, strict=strict)
    # Assertion
    assert isinstance(result, Example)
    assert result == value


# Generated at 2022-06-14 14:42:11.131774
# Unit test for constructor of class Reference
def test_Reference():
    x = Reference('x', allow_null=True)
    assert x.to == 'x'
    assert x.definitions is None
    assert x.allow_null is True

# Generated at 2022-06-14 14:42:20.900501
# Unit test for function set_definitions
def test_set_definitions():
    class Person(Schema):
        name = Field(type=str)

    class Cat(Schema):
        name = Field(type=str)

    class People(Schema):
        people = Array(items=Reference(to=Person))

    class Peopled(Schema):
        people = Array(items=Reference(to="Person"))

    class Pets(Schema):
        cats = Array(items=Cat)
        people = Array(items=Reference(to=["Person", "Pet"]))
        pet_people = Array(items=Reference(to=Person))

    definitions = SchemaDefinitions()
    set_definitions(Pets, definitions)


if __name__ == "__main__":
    test_set_definitions()

# Generated at 2022-06-14 14:42:26.051578
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # Schema
    class TestSchema(Schema):
        a = Array(items=str)
        b = Array(items=str)

    testSchema = TestSchema({'a': ['a', 'b'], 'b': ['c', 'd']})
    print(testSchema)
    print(testSchema.is_sparse)
    print(testSchema.a)
    print(testSchema['a'])


if __name__ == '__main__':
    test_Schema___repr__()

# Generated at 2022-06-14 14:42:38.343771
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer(minimum=18)

    instances = [
        Person({"first_name": "Harry", "last_name": "Potter", "age": 17}),
        Person({"first_name": "Harry", "last_name": "Potter", "age": 23}),
        Person({"first_name": "Harry", "last_name": "Potter", "age": 23}),
        Person({"first_name": "Harry", "last_name": "Potter", "age": 23}),
    ]
    # Can not pass age to 17, age must be greater than or equal to 18
    assert instances[0] is None # This should be an AssertionError

    # Person object must have an age = 23
   

# Generated at 2022-06-14 14:42:41.763198
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        pass
    item1 = TestSchema()
    item2 = TestSchema()
    assert item1 == item2
    assert not item1 != item2


# Generated at 2022-06-14 14:42:48.730596
# Unit test for function set_definitions
def test_set_definitions():
    class AddressSchema(Schema):
        zip = Reference("ZipSchema")

    class UserSchema(Schema):
        address = Reference("AddressSchema")

    definitions = SchemaDefinitions()
    set_definitions(UserSchema, definitions)
    assert issubclass(definitions["ZipSchema"], Schema)
    assert issubclass(definitions["AddressSchema"], Schema)



# Generated at 2022-06-14 14:42:51.508807
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    try:
        _Schema__iter__()
    except Exception:
        # pylint: disable=bare-except
        raise AssertionError



# Generated at 2022-06-14 14:42:54.860550
# Unit test for constructor of class Schema
def test_Schema():
    # Create typesystem.Schema instance
    inst = Schema()
    # Check type of __init__ return value (typesystem.Schema)
    assert isinstance(inst, Schema)
    # Check default values
    assert inst.fields is {}


# Generated at 2022-06-14 14:42:56.422978
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    assert False # TODO: implement your test here


# Generated at 2022-06-14 14:43:35.853083
# Unit test for constructor of class Schema
def test_Schema():
    assert hasattr(Schema, '__init__')
    Schema() # Should not throw


# Generated at 2022-06-14 14:43:45.533007
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class MySchemaDefinitions(SchemaDefinitions):
        def __init__(self) -> None:
            super(MySchemaDefinitions, self).__init__()
    class MySchemaMetaclass(SchemaMetaclass):
        def __new__(
            cls: type,
            name: str,
            bases: typing.Sequence[type],
            attrs: dict,
            definitions: typing.Optional[typing.Mapping] = None,
        ) -> type:
            return super(MySchemaMetaclass, cls).__new__(  # type: ignore
                cls,
                name,
                bases,
                attrs,
                definitions=definitions
            )
    class MyObject(metaclass=MySchemaMetaclass):
        pass

# Generated at 2022-06-14 14:43:53.704340
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.fields import Integer, Number, Object, String

    schemas = SchemaDefinitions()

    class Person(Schema):
        age = Integer()
        name = String()

    class Address(Schema):
        city = String()
        country = String()

    class Company(Schema):
        address = Reference(Address, definitions=schemas)

    class Employee(Schema):
        company = Reference(Company, definitions=schemas)

    class PersonReference(Schema):
        person = Reference(Person, definitions=schemas)

    class EmployeeReference(Schema):
        employee = Reference(Employee, definitions=schemas)

    class PersonAddress(Schema):
        person = Reference(Person, definitions=schemas)
        address = Reference(Address, definitions=schemas)


# Generated at 2022-06-14 14:44:02.864877
# Unit test for method validate of class Reference
def test_Reference_validate():
    class A(Schema):
        a = Reference('B')
        b = Reference('B')

        class Meta:
            additional = ['b']

    class B(Schema):
        c = Reference('C')
        d = Reference('C')

        class Meta:
            additional = True

    class C(Schema):
        e = int()
        g = Field()

    definitions = SchemaDefinitions()
    A(definitions=definitions)
    B(definitions=definitions)
    C(definitions=definitions)
    testA = A(a=B(c=C(e=3)), b=B(d=C(g=8)))
    assert testA.a.c.e == 3
    assert testA.b.d.g == 8

# Generated at 2022-06-14 14:44:11.705632
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():

    from typesystem.fields import String

    class Definition1(metaclass=SchemaMetaclass):
        pass

    class Definition2(metaclass=SchemaMetaclass):
        pass

    class Definition3(metaclass=SchemaMetaclass):
        pass

    class Definition4(metaclass=SchemaMetaclass):
        pass

    class ValidationSchema1(metaclass=SchemaMetaclass):
        age = String()

    class ValidationSchema2(ValidationSchema1):
        name = String()

    class ValidationSchema3(ValidationSchema2):
        name = String(max_length=20)

    class ValidationSchema4(ValidationSchema2):
        name = String(max_length=10)
