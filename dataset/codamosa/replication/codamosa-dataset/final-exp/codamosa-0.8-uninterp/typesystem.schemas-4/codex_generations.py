

# Generated at 2022-06-14 14:35:04.226739
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    to = Object(name = "to", properties = {
        "a": String(),
        "b": Integer(),
        "c": Float()
    })
    definitions = SchemaDefinitions(vars())
    ref = Reference(to = 'to', definitions = definitions)
    obj = {'a': 'a', 'b': 2, 'c': 3.14}
    result = ref.serialize(obj)
    assert result == obj

# Generated at 2022-06-14 14:35:10.551100
# Unit test for constructor of class Schema
def test_Schema():
    # Test inline string reference
    schema = Schema.validate({"foo": "bar"})
    assert isinstance(schema, Schema)

    # Test class reference
    class TestSchema(Schema):
        foo = Reference(to="bar")

    assert TestSchema({"foo": "bar"}) == TestSchema(foo="bar")

    # Test partial initialization
    assert TestSchema(foo="bar") != TestSchema(foo="bar", baz="foo")

# Generated at 2022-06-14 14:35:16.492607
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class A(Schema):
        name = String()

    a = A(name='abc')
    
    assert isinstance(a.__getitem__('name'), str) 
    assert a.__getitem__('name') == 'abc'
    
    try:
        assert a.__getitem__('key')
    except KeyError as e:
        assert isinstance(e, KeyError)
        assert e.__str__() == 'key'



# Generated at 2022-06-14 14:35:19.050711
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class MySchema(Schema):
        a = "a"
        b = "b"
    obj = MySchema()
    assert obj['a'] == obj['b'] == "a"


# Generated at 2022-06-14 14:35:24.233468
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int, default=0)

    person_1 = Person(name="Alice")
    assert person_1 == Person(name="Alice", age=0)

    person_2 = Person(name="Alice", age=18)
    assert person_2 == Person(name="Alice", age=18)

    assert person_1 != person_2
    assert person_1 != "someone else"
    assert person_1 != None


# Generated at 2022-06-14 14:35:35.138034
# Unit test for function set_definitions
def test_set_definitions():
    class ChildSchema(Schema):
        pass

    class ParentSchema(Schema):
        child1 = Reference(ChildSchema)
        child2 = Reference(ChildSchema)
        children = Array(Resource(ChildSchema))

    definitions = SchemaDefinitions()
    class_name = ParentSchema.__name__
    assert definitions[class_name] is ParentSchema

    assert ParentSchema.child1.definitions is None
    assert ParentSchema.child2.definitions is None
    assert ParentSchema.children.items.definitions is None

    set_definitions(ParentSchema, definitions)

    assert ParentSchema.child1.definitions is definitions
    assert ParentSchema.child2.definitions is definitions
    assert ParentSchema.children.items.definitions is definitions

# Generated at 2022-06-14 14:35:36.963550
# Unit test for constructor of class Schema
def test_Schema():
    class Foo(Schema):
        bar = Field(str)
    f=Foo(bar="str")
    assert f.bar=="str"


# Generated at 2022-06-14 14:35:38.013696
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    assert tuple(Schema()) == ()



# Generated at 2022-06-14 14:35:41.126254
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    target = '{target}'
    foo = '{foo}'
    expected = '(target={}, foo={})'.format(target, foo)
    schema = Schema(target=target, foo=foo)
    result = schema.__repr__()
    assert result == expected, '__repr__ does not match'


# Generated at 2022-06-14 14:35:47.249706
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class Foo(Schema):
        field = Reference("Bar")

    class Bar(Schema):
        field = Reference("Baz")

    class Baz(Schema):
        field = Field()

    set_definitions(Foo.field, definitions)
    assert Foo.field.definitions is definitions
    assert Bar.field.definitions is definitions
    assert Baz.field.definitions is definitions

    class Qux(Schema):
        field = Reference("Bar")

    set_definitions(Qux.field, definitions)
    assert Qux.field.definitions is definitions
    assert Bar.field.definitions is definitions
    assert Baz.field.definitions is definitions

# Generated at 2022-06-14 14:35:55.740619
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    assert (None == None)
    assert (not (None != None))


# Generated at 2022-06-14 14:35:59.276702
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import json
    schema = Schema(a=10, b=3, c="hi")
    assert repr(schema) == 'Schema(a=10, b=3, c="hi")'


# Generated at 2022-06-14 14:36:00.446016
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    # TODO: implement 
    pass


# Generated at 2022-06-14 14:36:10.883698
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        name = String(required=True)
        age = Integer(default=0)

    assert TestSchema(name='may',age=100) == TestSchema(name='may',age=100)
    assert TestSchema(name='may',age=100) != TestSchema(name='may',age=300)

    assert TestSchema(name='may') == TestSchema(name='may')
    assert TestSchema(age=100) == TestSchema(age=100)
    assert TestSchema(name='may') != TestSchema(age=100)
    assert TestSchema(name='may',age=100) != TestSchema(name='may')
    assert TestSchema(name='may',age=100) != TestSchema(age=100)


# Generated at 2022-06-14 14:36:11.768377
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    assert len(Schema()) == 0



# Generated at 2022-06-14 14:36:15.600128
# Unit test for constructor of class Schema
def test_Schema():
    assert Schema({}).is_sparse
    assert not Schema({"foo": "bar"}).is_sparse
    assert not Schema(foo="bar").is_sparse
    assert not Schema(foo="bar", sparse=True).is_sparse

# Generated at 2022-06-14 14:36:20.264365
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class mySchema(Schema):
        test = Field()
    instance = mySchema(test=1)
    assert repr(instance) == 'mySchema(test=1)'
    instance = mySchema(test=1, sparse=[])
    assert repr(instance) == 'mySchema(test=1, sparse=[])'


# Generated at 2022-06-14 14:36:27.334235
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        id = Field(type="integer")
        first_name = Field(type="string")
        last_name = Field(type="string")

    t1 = TestSchema(id=1, first_name="John", last_name="Doe")
    t2 = TestSchema(id=1, first_name="John", last_name="Doe")
    assert t1 == t2


# Generated at 2022-06-14 14:36:37.275725
# Unit test for function set_definitions
def test_set_definitions():
    class ChildSchema(Schema):
        field_from_child = String(default="")
        field_from_parent = String(default="")

    class ParentSchema(Schema):
        field_from_parent = Reference(ChildSchema)

    class MySchema(Schema):
        field_from_root = Reference(ParentSchema)

    definitions = SchemaDefinitions()
    definitions[ParentSchema.__name__] = ParentSchema

    assert MySchema.field_from_root.definitions == definitions
    assert MySchema.field_from_root.target.definitions == definitions
    assert (
        MySchema.field_from_root.target.field_from_parent.definitions == definitions
    )

# Generated at 2022-06-14 14:36:38.553780
# Unit test for method __len__ of class Schema
def test_Schema___len__():


    #
    # Test is incorrect
    #
    pass


# Generated at 2022-06-14 14:36:55.652212
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class TestSchema(Schema):
        field1 = Field()
        field2 = Field()
        field3 = Field(default="field3")

    schema1 = TestSchema(field1="field1", field2="field2")
    schema2 = TestSchema(field1="field1", field2="field2", field3="field3")
    schema3 = TestSchema()
    schema4 = TestSchema(field1="field1", field2="field2", field3="field4")
    schema5 = TestSchema(field1="field1", field2="field3")
    schema6 = TestSchema(field1="field1", field2="field2", field3="field3")

    assert schema1 == schema2
    assert not schema1 == schema3
    assert not schema1 == schema4
    assert not schema1

# Generated at 2022-06-14 14:36:56.346008
# Unit test for constructor of class Reference
def test_Reference():
    r=Reference('self')
    assert r.to == 'self'

# Generated at 2022-06-14 14:37:04.470330
# Unit test for function set_definitions
def test_set_definitions():
    class SubclassSchema(Schema):
        pass

    class SubSchema(Schema):
        field = Reference("SubclassSchema")

    class Schema(Schema):
        field = SubSchema

    assert isinstance(SubSchema.fields["field"].items, Reference)
    assert "SubclassSchema" == SubSchema.fields["field"].items.target_string
    assert isinstance(SubclassSchema(), Schema)
    assert isinstance(SubSchema.fields["field"].items, Reference)
    assert isinstance(SubSchema.fields["field"].items.target, type)
    assert isinstance(SubSchema.fields["field"].items.target, Schema)
    assert isinstance(SubSchema.fields["field"].items.target(), Schema)

# Generated at 2022-06-14 14:37:13.709411
# Unit test for function set_definitions
def test_set_definitions():
    class User(Schema):
        first_name = String()
        last_name = String()

    class Post(Schema):
        title = String()
        author = Reference(User)

    definitions = SchemaDefinitions()
    assert User.fields["first_name"].definitions is None
    assert Post.fields["title"].definitions is None
    assert Post.fields["author"].definitions is None
    set_definitions(Post, definitions)
    assert User.fields["first_name"].definitions is None
    assert Post.fields["title"].definitions is None
    assert Post.fields["author"].definitions is definitions



# Generated at 2022-06-14 14:37:18.505561
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class Test(Schema):
        field = Field()
    reference = Reference(Test)

    # Test this method with an object Test
    assert reference.serialize(Test(field="value")) == {
        "field": "value"
    }

    # Test this method with null
    assert reference.serialize(None) == None


# Generated at 2022-06-14 14:37:20.403911
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Foo(Schema):
        field = String()
    foo = Foo()
    assert isinstance(len(foo), int)

# Generated at 2022-06-14 14:37:28.647920
# Unit test for function set_definitions
def test_set_definitions():
    class TestDefinitions(Schema):
        class TestDefinitions_one(Schema):
            foo = Reference("two")
        class TestDefinitions_two(Schema):
            bar = Reference("one")
        definitions = SchemaDefinitions()
        set_definitions(TestDefinitions_one, definitions)
        set_definitions(TestDefinitions_two, definitions)
    assert TestDefinitions.TestDefinitions_one.fields["foo"].definitions != None
    assert TestDefinitions.TestDefinitions_two.fields["bar"].definitions != None

# Generated at 2022-06-14 14:37:33.384991
# Unit test for method validate of class Reference
def test_Reference_validate():
    # test case1 - Raise ValidationError when value is None
    definitions = SchemaDefinitions({"Test": object})
    ref = Reference("Test", definitions)
    with pytest.raises(ValidationError):
        ref.validate(None)
    # test case2 - return None when value is None
    ref2 = Reference("Test", definitions, allow_null=True)
    assert ref2.validate(None) is None


# Generated at 2022-06-14 14:37:45.751789
# Unit test for constructor of class Schema
def test_Schema():

    class ComplexSchema(Schema):
        a = Field()
        b = Field()
        c = Field()

    obj = ComplexSchema({"a": 1, "b": 2, "c": 3})
    assert obj == ComplexSchema(obj)
    assert obj == {
        "a": 1,
        "b": 2,
        "c": 3
    }
    assert obj == {"a": 1, "b": 2, "c": 3}
    assert obj.a == 1
    assert obj.b == 2
    assert obj.c == 3

    obj = ComplexSchema(a=1, b=2, c=3)
    assert obj == ComplexSchema(obj)
    assert obj == {
        "a": 1,
        "b": 2,
        "c": 3
    }

# Generated at 2022-06-14 14:37:58.204824
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field(str)
        age = Field(int)
        optional = Field(str, required=False)

    person = Person({"name": "john", "age": 42})
    assert person.name == "john"
    assert person.age == 42
    assert person.optional is None
    assert person == Person(name="john", age=42)

    with pytest.raises(TypeError) as exc_info:
        Person("not-a-dict")
    assert str(exc_info.value) == "Expected a mapping for Person() constructor."

    with pytest.raises(TypeError) as exc_info:
        Person(name="john", age="not-an-int")

# Generated at 2022-06-14 14:38:26.789025
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class Person(Schema):
        name = String()
        age = Integer(default=None)
        friends = Array(items=Reference(Person))
        family = Array(items=Reference(Person))
    # Unit test for method __init__ of class Schema
    class TestSchema:
        def test___init__(self):
            name = "Roger"
            age = 24
            friends = [
                {"name": "Paul", "age": 24},
                {"name": "Nick", "age": 23}
            ]
            p = Person(name=name, age=age, friends=friends)
            assert p.name == name
            assert p.age == age
            assert p.friends == [Person(friend) for friend in friends]
            assert p.family == []
            # Unit test for method fields of class Schema

# Generated at 2022-06-14 14:38:35.163733
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        first_name = Field(type="string")
        last_name = Field(type="string")
        age = Field(type="integer")

    p = Person(first_name="John", last_name="Doe")
    assert list(p) == ["first_name", "last_name"]
    chunks = [f"{name}={value!r}" for name, value in p.items()]
    assert "first_name='John'" in chunks
    assert "last_name='Doe'" in chunks
    assert "age=None" not in chunks

# Generated at 2022-06-14 14:38:36.059421
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    pass



# Generated at 2022-06-14 14:38:43.876205
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class TestSchema(Schema):
        a = Field()
        b = Field()
    from typesystem.base import String
    class TestSchema2(Schema):
        a = Field()
        b = String()
    
    # TestSchema(a={'a': 1, 'b': 2}, b={'a': 1, 'b': 2})
    obj = TestSchema(a={'a': 1, 'b': 2}, b={'a': 1, 'b': 2})
    assert repr(obj) == 'TestSchema(a={\'a\': 1, \'b\': 2}, b={\'a\': 1, \'b\': 2})'
    # TestSchema(b={'a': 1, 'b': 2})
    obj = TestSchema(b={'a': 1, 'b': 2})

# Generated at 2022-06-14 14:38:46.288912
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Foo(Schema):
        field1 = Field(required=True)
        field2 = Field()

    foo = Foo(field1="a", field2="b")

    assert list(iter(foo)) == ['field1', 'field2']


# Generated at 2022-06-14 14:38:54.432822
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    field = Array(items=Reference("TestReference"))
    set_definitions(field, definitions)
    assert field.items.definitions == definitions

    class TestReference(Schema):
        field = String()

    definitions = SchemaDefinitions()
    field = Array(items=Reference(TestReference))
    set_definitions(field, definitions)
    assert field.items._target == TestReference
    assert field.items.definitions is None

# Generated at 2022-06-14 14:39:01.925622
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class NestedSchema(Schema):
        age = Field(Integer, required=False)

    class TestSchema(Schema):
        name = Field(String)
        age = Field(Integer, default=10)
        nested = Field(Object(properties={"age": Field(Integer)}))
        nested_schema = Field(NestedSchema)
    test_schema = TestSchema(name="John", age=30)
    assert test_schema["name"] == "John"
    assert test_schema["age"] == 30
    assert test_schema["nested"] == {"age": None}
    assert test_schema["nested_schema"] == {"age": None}
    test_schema = TestSchema(name="John", age=30, nested={"age": 20})
    assert test_schema

# Generated at 2022-06-14 14:39:14.277059
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    # Test case data
    d1 = {'name':'amy', "age": 15}
    d2 = {"name": "bob", "age": 15}
    p1 = Person(name="amy", age=15)
    p2 = Person(name="bob", age=15)
    p3 = Person(name="amy", age=16)
    p4 = Person(name="bob", age=16)
    Person.validate(d1)
    Person.validate(d2)
    # Perform test
    # assert p1['name']=='amy', "P1 name error"
    # assert p1['age'] == 15, "P1 age error"
    # assert p2['name'] == 'bob', "P2 name error"
    # assert p2['age'] == 15, "P2 age

# Generated at 2022-06-14 14:39:14.962285
# Unit test for constructor of class Reference
def test_Reference():
    assert Reference("name")

# Generated at 2022-06-14 14:39:25.479831
# Unit test for method validate of class Reference
def test_Reference_validate():
    d = {
        "name_1": "test",
        "name_2": "test",
        "name_3": "test",
    }
    s = Schema(d)
    class TestReference(Schema):
        name_1 = String(min_length=2)
        name_2 = String(min_length=4)
    
    class TestObject(Schema):
        name_1 = Reference(TestReference)
        name_2 = Reference(TestReference)
        name_3 = Reference(TestReference)
    
    test = TestObject.validate(s)
    assert test.name_1 == s
    assert test.name_2 == s
    assert test.name_3 == s


# Generated at 2022-06-14 14:39:40.383332
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    # TODO: Implement test
    pass


# Generated at 2022-06-14 14:39:51.677007
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class MySchema(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0, maximum=100)

    s1 = MySchema({"name": "john", "age": 23})
    s2 = MySchema({"name": "john", "age": 23})
    s3 = MySchema({"name": "jane", "age": 23})
    s4 = MySchema({"name": "john", "age": 24})
    s5 = MySchema({"name": "john", "age": 23, "hair": "black"})
    s6 = MySchema({"name": "john"})
    s7 = MySchema({"age": 23})
    s8 = MySchema()


# Generated at 2022-06-14 14:39:57.524825
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class PersonSchema(Schema):
        name = String(max_length=200)
        age = Integer(minimum=0)

    assert isinstance(PersonSchema.fields, dict)
    assert isinstance(PersonSchema.fields.get("name"), Field)
    assert isinstance(PersonSchema.fields.get("age"), Field)



# Generated at 2022-06-14 14:40:02.547806
# Unit test for function set_definitions
def test_set_definitions():
    class A(Schema):
        b = Field()

    class B(Schema):
        a = Reference("A", definitions=SchemaDefinitions())
        c = Reference("C", definitions={"C": A})

    set_definitions(B.fields["a"], SchemaDefinitions())
    assert B.fields["a"].target is A

# Generated at 2022-06-14 14:40:06.744187
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Test(Schema):
        f1 = Field()
        f2 = Field(default=2)

    instance = Test(f1=1)
    assert instance['f1'] == 1
    assert instance['f2'] == 2



# Generated at 2022-06-14 14:40:16.667509
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():

    class User(Schema):
        id = String()
        age = Integer()

    u = User(id='1', age=18)
    keys = [key for key in u]
    assert isinstance(keys, list)
    assert keys == ['id', 'age']

    # Test empty object
    u = User()
    keys = [key for key in u]
    assert isinstance(keys, list)
    assert keys == []

    # Test None object
    u = None
    keys = [key for key in u]
    assert isinstance(keys, list)
    assert keys == []

    # Test faulty object
    u = User()
    delattr(u, 'id')
    keys = [key for key in u]
    assert isinstance(keys, list)
    assert keys == ['age']


# Generated at 2022-06-14 14:40:23.870064
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        field_1 = String()
        field_2 = String()
        field_3 = String()

    a = TestSchema(field_1="1", field_2="2", field_4="4")
    abs_ = ["field_1", "field_2"]
    assert list(iter(a)) == abs_


# Generated at 2022-06-14 14:40:33.979176
# Unit test for constructor of class Schema
def test_Schema():
    class ExtendedSchema(Schema):
        field1 = Field(type=str)
        field2 = Field(type=str, default="Default value")

    schema = ExtendedSchema(field1="Value 1", field2="Value 2")
    assert schema.field1 == "Value 1" and schema.field2 == "Value 2"

    schema = ExtendedSchema(dict(field1="Value 1"))
    assert schema.field1 == "Value 1" and schema.field2 == "Default value"

    # raises TypeError
    try:
        ExtendedSchema(field1="Value 1", field2="Value 2", field3="Value 3")
    except TypeError as e:
        assert str(e) == "field3 is an invalid keyword argument for ExtendedSchema()."
        assert True
    except:
        assert False

    # raises TypeError


# Generated at 2022-06-14 14:40:38.400886
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    import json
    class Member(Schema):
        name = String()
        age = Integer()

    member = Member(name='foo', age=20)

    assert member.__repr__() == "Member(name='foo', age=20)"


# Generated at 2022-06-14 14:40:43.394815
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class MySchema(Schema):
        a = Field()
        b = Field()
        c = Field()
    my_object = MySchema({"a": "a-value", "c": "c-value"})
    assert [key for key in my_object] == ["a", "c"]

# Generated at 2022-06-14 14:41:15.917265
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class A(Schema):
        name = String()
        age = Integer()

    assert isinstance(A.fields, dict)
    assert isinstance(A.fields['name'], String)
    assert A.fields['name'].name == 'name'
    assert isinstance(A.fields['age'], Integer)
    assert A.fields['age'].name == 'age'

    definitions = SchemaDefinitions()
    class B(Schema):
        name = String()
        age = Integer()
        assert B.fields['name'].name == 'name'
        assert B.fields['age'].name == 'age'
        assert definitions['B'] == B
        assert isinstance(B.fields['age'].definitions, SchemaDefinitions)
        assert definitions == B.fields['age'].definitions


# Generated at 2022-06-14 14:41:27.976021
# Unit test for constructor of class Schema
def test_Schema():
    class O(Schema):
        a = Array(items="string", required=True)
        b = Array(items="string", required=False)
    obj = O({"a": ["a"], "b": ["b", "c"]})
    assert obj["a"] == ["a"]
    assert obj["b"] == ["b", "c"]
    with pytest.raises(TypeError):
        obj = O({"a": 2})

    class O(Schema):
        a = Array(items="string", required=True)
        b = Array(items="string", required=False)
    obj = O({"a": ["a"], "b": ["b", "c"]})
    assert obj["a"] == ["a"]
    assert obj["b"] == ["b", "c"]

# Generated at 2022-06-14 14:41:31.007143
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Foo:
        name = "foo"

    class FooSchema(Schema):
        name = Field(type=str)

    assert FooSchema(Foo()) == FooSchema(Foo())


# Generated at 2022-06-14 14:41:43.420522
# Unit test for function set_definitions
def test_set_definitions():

    class Person(Schema):
        first_name = String()
        age = Integer()

    class Student(Person):
        gpa = Float()

    class Faculty(Person):
        role = String()

    class Course(Schema):
        id = Integer()
        title = String()
        instructor = Reference(Faculty)
        students = Array(Reference(Student))

    definitions = SchemaDefinitions(
        Person=Person,
        Student=Student,
        Faculty=Faculty,
        Course=Course,
    )

    set_definitions(Course.make_validator(), definitions)


# Generated at 2022-06-14 14:41:55.539436
# Unit test for constructor of class Schema
def test_Schema():
    x = Schema()
    assert isinstance(x, Schema)
    
    class Foo(Schema):
        a = Float()
        b = String()
        c = Boolean()
        d = Integer()
        e = Datetime()
        f = Enum("a", "b", "c")
        g = String()
        h = Integer()
        i = String()
        j = String()
    
    y = Foo(a = 9.0, b = "a", c = True, d = 0, e = parse("2020-08-23"), f = "a", g = "a", h = 1, i = "a", j = "a")
    assert isinstance(y, Foo)
    assert isinstance(y.fields, Mapping)
    assert isinstance(y.fields["a"], Field)

# Generated at 2022-06-14 14:42:04.896170
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    test_Schema = Schema()
    assert isinstance(test_Schema, Mapping)
    assert isinstance(test_Schema, typing.MutableMapping)
    assert test_Schema.fields == {}
    assert test_Schema.is_sparse == False
    assert test_Schema.__eq__(Schema()) == True
    assert test_Schema.__eq__(Unexpected()) == False
    assert test_Schema.__getitem__(0) == KeyError
    assert test_Schema.__len__() == 0
    assert test_Schema.__repr__() == "Schema()"
    assert isinstance(test_Schema.make_validator(), Object)
    assert test_Schema.validate(0) == Schema()
    assert test_Schema.validate_or_

# Generated at 2022-06-14 14:42:15.878977
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem import Schema
    from typesystem import Integer, String
    from typesystem import ValidationError
    from typesystem.fields import Array
    class Person(Schema):
        name = String()
        age = Integer(default=0)
        friends = Array(Integer)
    import random, string
    def rand_str(length=10):
        return ''.join([random.choice(string.ascii_letters + string.digits)
                        for n in range(length)])
    p1 = Person(name='p1', age=1, friends=[1, 2, 3])
    p2 = Person(name='p2', age=1, friends=[1, 2, 3])
    p3 = Person(name='p1', age=3, friends=[1, 2, 3])

# Generated at 2022-06-14 14:42:24.967258
# Unit test for function set_definitions
def test_set_definitions():
    class FieldA(Field):
        def test(self):
            return self.definitions is not None
        def test2(self):
            return self.definitions['fieldB'] is fieldB

    class FieldB(Field):
        def test(self):
            return self.definitions is not None
        def test2(self):
            return self.definitions['fieldA'] is fieldA

    class FieldC(Field):
        pass

    fieldA = FieldA()
    fieldB = FieldB()
    fieldC = FieldC()
    arrayA = Array(items=fieldA)
    arrayB = Array(items=fieldB)
    arrayC = Array(items=fieldC)
    dictA = {'fieldA': fieldA}
    dictB = {'fieldB': fieldB}

# Generated at 2022-06-14 14:42:37.592513
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    import copy
    import tempfile

    with open("/home/bkp/py/typesystem/typesystem/schemas.py", "rt") as f:
        orig_source = f.read()

# Generated at 2022-06-14 14:42:42.781721
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Person(Schema):
        age = Integer(minimum=0, maximum=100)
        name = String()
    p = Person({'age':21, 'name':'john'})
    assert p['age'] == 21
    assert type(p['age']) == int
    assert p['name'] == 'john'


# Generated at 2022-06-14 14:43:38.804235
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class TestSchema(Schema):
        field_1 = String()
        field_2 = String()
    instance = TestSchema(field_1 = "test")
    assert hasattr(instance, "field_1")
    assert not hasattr(instance, "field_2")
    assert list(instance) == ["field_1"]

test_Schema___iter__()

# Generated at 2022-06-14 14:43:42.449905
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = Field()
        age = Field()

    person = Person(name="Foo", age=1)
    assert person["name"] == person.name == "Foo"
    assert person["age"] == person.age == 1


# Generated at 2022-06-14 14:43:46.730633
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    class User(Schema):
        id = Field()

    class Post(Schema):
        user = Reference(User)
        posted_at = Field()

    set_definitions(Post.fields["user"], definitions)
    assert isinstance(Post.fields["user"], Reference)
    assert Post.fields["user"].definitions is definitions

# Generated at 2022-06-14 14:43:49.418670
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Person(Schema):
        first_name = Field()
        last_name = Field()

    p = Person(**{'first_name': 'John', 'last_name': 'Smith'})
    l = list(p)
    assert l == ['first_name', 'last_name']


# Generated at 2022-06-14 14:43:58.626090
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class TestSchema(Schema):
        a = Field()
        b = Field()
        c = Field()

    ts = TestSchema(a=1, b=2)
    assert len(ts) == 2
    ts = TestSchema(a=1, b=2, c=3)
    assert len(ts) == 3
    ts = TestSchema(a=1)
    assert len(ts) == 1
    ts = TestSchema({'a':1, 'b':2})
    assert len(ts) == 2
    ts = TestSchema({'a':1, 'b':2, 'c':3})
    assert len(ts) == 3
    ts = TestSchema({'a':1})
    assert len(ts) == 1

# Generated at 2022-06-14 14:43:59.548245
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    pass


# Generated at 2022-06-14 14:44:01.405397
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    import doctest
    doctest.run_docstring_examples(Schema.__iter__, globals(), verbose=True)

# Generated at 2022-06-14 14:44:11.152502
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class MySchema(Schema):
        def __init__(self, a, b=4, c=5):
            super().__init__(a=a, b=b, c=c)
    assert MySchema._meta.fields == {'a': Field(name='a'), 'b': Field(name='b', default=4), 'c': Field(name='c', default=5)}
    assert MySchema.fields != {'a': Field(name='a'), 'b': Field(name='b', default=4), 'c': Field(name='c', default=5)}
    assert MySchema.fields == {'a': Field(name='a'), 'b': Field(name='b', default=4), 'c': Field(name='c', default=5)}
    assert MySchema(a=1) == MySche