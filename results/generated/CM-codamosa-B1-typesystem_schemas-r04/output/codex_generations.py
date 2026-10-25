

# Generated at 2026-10-24 07:17:40.483558
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 07:17:54.835529
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 07:17:56.157040
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 07:18:29.650314
# Unit test for constructor of class Reference
def test_Reference():
    # 1. String reference: stores string, defers lookup.
    ref_str = Reference("MySchema")
    assert ref_str.to == "MySchema"
    assert ref_str.definitions is None
    assert ref_str._target_string == "MySchema"
    assert not hasattr(ref_str, "_target")
    assert ref_str.target_string == "MySchema"

    # 2. Class reference: stores class directly.
    class MySchema(Schema):
        pass

    ref_cls = Reference(MySchema)
    assert ref_cls.to is MySchema
    assert ref_cls.definitions is None
    assert ref_cls._target is MySchema
    assert not hasattr(ref_cls, "_target_string")
    # `target_string` falls back to class name.
    assert ref_cls.target_string == "MySchema"
    assert ref_cls.target is MySchema

    # 3. `definitions` mapping is retained.
    defs = SchemaDefinitions()
    ref_defs = Reference("MySchema", definitions=defs)
    assert ref_defs.definitions is defs

    # 4. String target resolves through `definitions`.
    defs["MySchema"] = MySchema
    assert ref_defs.target is MySchema

    # 5. Extra kwargs are forwarded to `Field` (e.g. `allow_null`).
    ref_null = Reference("MySchema", allow_null=True)
    assert ref_null.allow_null is True

    ref_not_null = Reference(MySchema)
    assert ref_not_null.allow_null is False

    # 6. Non-Schema class raises AssertionError.
    class NotASchema:
        pass

    try:
        Reference(NotASchema)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for non-Schema class")

    # 7. Non-str / non-class raises TypeError from `issubclass`.
    try:
        Reference(123)  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for non-class `to`")

# Generated at 2026-10-24 07:18:32.153532
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:18:34.567121
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:18:36.982367
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:18:39.398814
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:18:41.816051
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:18:44.228734
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:18:46.644383
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:18:49.059708
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:18:51.475993
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:18:54.347036
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:19:06.108071
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.fields import Integer, String

# Generated at 2026-10-24 07:19:17.983845
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Example(Schema):
        name = String()
        age = Integer()

    # All fields populated -> counts every field.
    assert len(Example(name="Tom", age=5)) == 2

    # Sparse instance -> only counts fields with attributes set.
    assert len(Example(name="Tom")) == 1
    assert Example(name="Tom").is_sparse is True

    # Nothing set -> zero.
    assert len(Example()) == 0
    assert Example().is_sparse is True

    # __len__ must agree with __iter__.
    instance = Example(name="Tom")
    assert len(instance) == len(list(iter(instance)))


def test_Schema___len___counts_defaulted_fields():
    class Example(Schema):
        name = String()
        count = Integer(default=0)

    instance = Example(name="Tom")
    assert instance.count == 0
    assert len(instance) == 2
    assert instance.is_sparse is False

# Generated at 2026-10-24 07:19:25.754952
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # Setting a new key stores the value.
    definitions["Example"] = "value"
    assert definitions["Example"] == "value"

    # Value can be any object (e.g. a Schema class).
    definitions["Another"] = {"a": 1}
    assert definitions["Another"] == {"a": 1}

    # Setting an existing key raises AssertionError.
    with pytest.raises(AssertionError):
        definitions["Example"] = "other"


def test_SchemaDefinitions___setitem___duplicate_message():
    definitions = SchemaDefinitions()
    definitions["Example"] = 1

    # Known quirk: the assert message is a raw string without an
    # f-prefix, so {key!r} is NOT interpolated â the message is the
    # literal text "Definition for {key!r} has already been set."
    with pytest.raises(AssertionError, match=r"Definition for \{key!r\} has already been set\."):
        definitions["Example"] = 2

# Generated at 2026-10-24 07:20:04.372976
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    # 1. Field attributes are collected into `fields`, ordered by
    #    creation counter, and removed from the class attributes.
    class Example(Schema):
        title = String()
        name = String()

    assert list(Example.fields.keys()) == ["title", "name"]
    assert not hasattr(Example, "title")
    assert not hasattr(Example, "name")

    # Non-Field attributes are left untouched on the class.
    assert Example.__name__ == "Example"

    # 2. Inheritance merges parent fields; child declarations win on
    #    name collisions, and the parent class is not mutated.
    class Child(Example):
        name = String(default="anonymous")
        extra = String()

    assert list(Child.fields.keys()) == ["title", "name", "extra"]
    assert Child.fields["name"].has_default()
    assert Child.fields["title"] is Example.fields["title"]

    assert "extra" not in Example.fields
    assert not Example.fields["name"].has_default()

    # 3. Passing `definitions` registers the new class under its name.
    definitions = SchemaDefinitions()

    class Pet(Schema, definitions=definitions):
        name = String()

    assert definitions["Pet"] is Pet

    # 4. `definitions` is propagated to string-referenced `Reference`
    #    fields, including those nested in `Array` and `Object` fields.
    class Person(Schema, definitions=definitions):
        pet = Reference("Pet")

    assert definitions["Person"] is Person
    assert Person.fields["pet"].definitions is definitions
    assert Person.fields["pet"].target is Pet

    class Owner(Schema, definitions=definitions):
        pets = Array(Reference("Pet"))
        home = Object(properties={"pet": Reference("Pet")})

    assert Owner.fields["pets"].items.definitions is definitions
    assert Owner.fields["home"].properties["pet"].definitions is definitions

    # The registered classes are usable through the definitions mapping.
    assert definitions["Pet"] is not None
    assert definitions["Person"] is not None
    assert definitions["Owner"] is not None

# Generated at 2026-10-24 07:20:22.071934
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing = SchemaDefinitions()

    # 1. Direct Reference
    direct = Reference(to="Target")
    assert direct.definitions is None
    module_0.set_definitions(direct, definitions)
    assert direct.definitions is definitions

    # 2. Already-set Reference is not overwritten
    preset = Reference(to="Target", definitions=existing)
    module_0.set_definitions(preset, definitions)
    assert preset.definitions is existing

    # 3. Array with single item, tuple items, and no items
    array_single_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=array_single_ref), definitions)
    assert array_single_ref.definitions is definitions

    tuple_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=(tuple_ref, String())), definitions)
    assert tuple_ref.definitions is definitions

    module_0.set_definitions(Array(items=None), definitions)  # must not raise

    # 4. Object properties, plus nested Array -> Object -> Reference
    object_ref = Reference(to="Target")
    nested_ref = Reference(to="Target")
    field = Object(
        properties={
            "direct": object_ref,
            "nested": Array(items=Object(properties={"inner": nested_ref})),
            "plain": String(),
        }
    )
    module_0.set_definitions(field, definitions)
    assert object_ref.definitions is definitions
    assert nested_ref.definitions is definitions

    # 5. Non-container field is a no-op
    module_0.set_definitions(String(), definitions)  # must not raise

# Generated at 2026-10-24 07:20:24.496441
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:20:26.914215
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:20:29.327024
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:20:31.879603
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:20:34.295732
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:20:36.712288
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:20:39.131964
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:20:41.541117
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:20:43.955327
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:20:46.371427
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:20:48.788829
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:20:51.200986
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:20:53.611710
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:20:56.027326
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:20:58.442080
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:21:01.778401
# Unit test for function set_definitions

# Generated at 2026-10-24 07:21:04.193917
# Unit test for function set_definitions

# Generated at 2026-10-24 07:21:06.608319
# Unit test for function set_definitions

# Generated at 2026-10-24 07:21:09.023323
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:21:11.439564
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:21:13.854121
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:21:16.267810
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:21:18.683630
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:21:21.099171
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:21:23.512022
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:21:25.925931
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:21:28.339719
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:21:30.756586
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:21:33.172379
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:21:35.584219
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:21:36.942085
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing = SchemaDefinitions()

    # 1. Direct Reference
    direct = Reference(to="Target")
    assert direct.definitions is None
    module_0.set_definitions(direct, definitions)
    assert direct.definitions is definitions

    # 2. Already-set Reference is not overwritten
    preset = Reference(to="Target", definitions=existing)
    module_0.set_definitions(preset, definitions)
    assert preset.definitions is existing

    # 3. Array with single item, tuple items, and no items
    array_single_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=array_single_ref), definitions)
    assert array_single_ref.definitions is definitions

    tuple_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=(tuple_ref, String())), definitions)
    assert tuple_ref.definitions is definitions

    module_0.set_definitions(Array(items=None), definitions)  # must not raise

    # 4. Object properties, plus nested Array -> Object -> Reference
    object_ref = Reference(to="Target")
    nested_ref = Reference(to="Target")
    field = Object(
        properties={
            "direct": object_ref,
            "nested": Array(items=Object(properties={"inner": nested_ref})),
            "plain": String(),
        }
    )
    module_0.set_definitions(field, definitions)
    assert object_ref.definitions is definitions
    assert nested_ref.definitions is definitions

    # 5. Non-container field is a no-op
    module_0.set_definitions(String(), definitions)  # must not raise

# Generated at 2026-10-24 07:22:01.228973
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.schemas import Schema

    # 1. `to` as a class
    class Example(Schema):
        pass

    field = Reference(to=Example)
    assert field._target is Example
    assert field.target is Example
    assert field.target_string == "Example"
    assert field.definitions is None

    # 2. `to` as a string, with definitions
    field = Reference(to="Example", definitions={"Example": Example})
    assert field._target_string == "Example"
    assert field.target is Example
    assert field.target_string == "Example"

    # 3. `to` as a string, no definitions yet â target resolves lazily later
    field = Reference(to="Example")
    assert field.definitions is None
    assert field._target_string == "Example"
    try:
        field.target
        assert False, "Expected AssertionError for missing definitions"
    except AssertionError as exc:
        assert "String reference missing 'definitions'" in str(exc)

    # 4. Invalid `to` (not a Schema subclass, not a string)
    try:
        Reference(to=123)
        assert False, "Expected AssertionError for invalid target"
    except AssertionError:
        pass

    # 5. Field kwargs pass through to Field.__init__
    field = Reference(to=Example, allow_null=True, title="Ref")
    assert field.allow_null is True
    assert field.title == "Ref"

    # 6. Null validation respects allow_null
    field = Reference(to=Example, allow_null=True)
    assert field.validate(None) is None
    field = Reference(to=Example)
    try:
        field.validate(None)
        assert False, "Expected ValidationError for null"
    except ValidationError:
        pass

    # 7. set_definitions attaches definitions to unresolved references
    from typesystem.schemas import set_definitions

    field = Reference(to="Example")
    assert field.definitions is None
    set_definitions(field, {"Example": Example})
    assert field.definitions is {"Example": Example}
    assert field.target is Example

    print("All Reference constructor tests passed.")

# Generated at 2026-10-24 07:22:03.779295
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:22:06.416865
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:22:08.832713
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:22:11.247733
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:22:13.884632
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:22:16.302188
# Unit test for method validate of class Reference

# Generated at 2026-10-24 07:22:18.716589
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:22:21.133816
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:22:23.548279
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:22:25.966204
# Unit test for function set_definitions

# Generated at 2026-10-24 07:22:28.378048
# Unit test for function set_definitions

# Generated at 2026-10-24 07:22:30.798455
# Unit test for function set_definitions

# Generated at 2026-10-24 07:22:33.210497
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:22:35.634851
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:22:38.038988
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:22:40.456897
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:22:42.866652
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:22:45.280853
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:22:48.009570
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    # 1. Field attributes are collected into `fields`, ordered by
    #    creation counter, and removed from the class attributes.
    class Example(Schema):
        title = String()
        name = String()

    assert list(Example.fields.keys()) == ["title", "name"]
    assert not hasattr(Example, "title")
    assert not hasattr(Example, "name")

    # Non-Field attributes are left untouched on the class.
    assert Example.__name__ == "Example"

    # 2. Inheritance merges parent fields; child declarations win on
    #    name collisions, and the parent class is not mutated.
    class Child(Example):
        name = String(default="anonymous")
        extra = String()

    assert list(Child.fields.keys()) == ["title", "name", "extra"]
    assert Child.fields["name"].has_default()
    assert Child.fields["title"] is Example.fields["title"]

    assert "extra" not in Example.fields
    assert not Example.fields["name"].has_default()

    # 3. Passing `definitions` registers the new class under its name.
    definitions = SchemaDefinitions()

    class Pet(Schema, definitions=definitions):
        name = String()

    assert definitions["Pet"] is Pet

    # 4. `definitions` is propagated to string-referenced `Reference`
    #    fields, including those nested in `Array` and `Object` fields.
    class Person(Schema, definitions=definitions):
        pet = Reference("Pet")

    assert definitions["Person"] is Person
    assert Person.fields["pet"].definitions is definitions
    assert Person.fields["pet"].target is Pet

    class Owner(Schema, definitions=definitions):
        pets = Array(Reference("Pet"))
        home = Object(properties={"pet": Reference("Pet")})

    assert Owner.fields["pets"].items.definitions is definitions
    assert Owner.fields["home"].properties["pet"].definitions is definitions

    # The registered classes are usable through the definitions mapping.
    assert definitions["Pet"] is not None
    assert definitions["Person"] is not None
    assert definitions["Owner"] is not None

# Generated at 2026-10-24 07:22:49.315719
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing = SchemaDefinitions()

    # 1. Direct Reference
    direct = Reference(to="Target")
    assert direct.definitions is None
    module_0.set_definitions(direct, definitions)
    assert direct.definitions is definitions

    # 2. Already-set Reference is not overwritten
    preset = Reference(to="Target", definitions=existing)
    module_0.set_definitions(preset, definitions)
    assert preset.definitions is existing

    # 3. Array with single item, tuple items, and no items
    array_single_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=array_single_ref), definitions)
    assert array_single_ref.definitions is definitions

    tuple_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=(tuple_ref, String())), definitions)
    assert tuple_ref.definitions is definitions

    module_0.set_definitions(Array(items=None), definitions)  # must not raise

    # 4. Object properties, plus nested Array -> Object -> Reference
    object_ref = Reference(to="Target")
    nested_ref = Reference(to="Target")
    field = Object(
        properties={
            "direct": object_ref,
            "nested": Array(items=Object(properties={"inner": nested_ref})),
            "plain": String(),
        }
    )
    module_0.set_definitions(field, definitions)
    assert object_ref.definitions is definitions
    assert nested_ref.definitions is definitions

    # 5. Non-container field is a no-op
    module_0.set_definitions(String(), definitions)  # must not raise

# Generated at 2026-10-24 07:22:50.622461
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # Setting a new key stores the value.
    definitions["Example"] = "value"
    assert definitions["Example"] == "value"

    # Value can be any object (e.g. a Schema class).
    definitions["Another"] = {"a": 1}
    assert definitions["Another"] == {"a": 1}

    # Setting an existing key raises AssertionError.
    with pytest.raises(AssertionError):
        definitions["Example"] = "other"


def test_SchemaDefinitions___setitem___duplicate_message():
    definitions = SchemaDefinitions()
    definitions["Example"] = 1

    # Known quirk: the assert message is a raw string without an
    # f-prefix, so {key!r} is NOT interpolated â the message is the
    # literal text "Definition for {key!r} has already been set."
    with pytest.raises(AssertionError, match=r"Definition for \{key!r\} has already been set\."):
        definitions["Example"] = 2

# Generated at 2026-10-24 07:22:53.239924
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import String

    # 1. Field attributes are collected into `fields`, ordered by
    #    creation counter, and removed from the class attributes.
    class Example(Schema):
        title = String()
        name = String()

    assert list(Example.fields.keys()) == ["title", "name"]
    assert not hasattr(Example, "title")
    assert not hasattr(Example, "name")

    # Non-Field attributes are left untouched on the class.
    assert Example.__name__ == "Example"

    # 2. Inheritance merges parent fields; child declarations win on
    #    name collisions, and the parent class is not mutated.
    class Child(Example):
        name = String(default="anonymous")
        extra = String()

    assert list(Child.fields.keys()) == ["title", "name", "extra"]
    assert Child.fields["name"].has_default()
    assert Child.fields["title"] is Example.fields["title"]

    assert "extra" not in Example.fields
    assert not Example.fields["name"].has_default()

    # 3. Passing `definitions` registers the new class under its name.
    definitions = SchemaDefinitions()

    class Pet(Schema, definitions=definitions):
        name = String()

    assert definitions["Pet"] is Pet

    # 4. `definitions` is propagated to string-referenced `Reference`
    #    fields, including those nested in `Array` and `Object` fields.
    class Person(Schema, definitions=definitions):
        pet = Reference("Pet")

    assert definitions["Person"] is Person
    assert Person.fields["pet"].definitions is definitions
    assert Person.fields["pet"].target is Pet

    class Owner(Schema, definitions=definitions):
        pets = Array(Reference("Pet"))
        home = Object(properties={"pet": Reference("Pet")})

    assert Owner.fields["pets"].items.definitions is definitions
    assert Owner.fields["home"].properties["pet"].definitions is definitions

    # The registered classes are usable through the definitions mapping.
    assert definitions["Pet"] is not None
    assert definitions["Person"] is not None
    assert definitions["Owner"] is not None

# Generated at 2026-10-24 07:23:09.715690
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.schemas import Schema

    # 1. `to` as a class
    class Example(Schema):
        pass

    field = Reference(to=Example)
    assert field._target is Example
    assert field.target is Example
    assert field.target_string == "Example"
    assert field.definitions is None

    # 2. `to` as a string, with definitions
    field = Reference(to="Example", definitions={"Example": Example})
    assert field._target_string == "Example"
    assert field.target is Example
    assert field.target_string == "Example"

    # 3. `to` as a string, no definitions yet â target resolves lazily later
    field = Reference(to="Example")
    assert field.definitions is None
    assert field._target_string == "Example"
    try:
        field.target
        assert False, "Expected AssertionError for missing definitions"
    except AssertionError as exc:
        assert "String reference missing 'definitions'" in str(exc)

    # 4. Invalid `to` (not a Schema subclass, not a string)
    try:
        Reference(to=123)
        assert False, "Expected AssertionError for invalid target"
    except AssertionError:
        pass

    # 5. Field kwargs pass through to Field.__init__
    field = Reference(to=Example, allow_null=True, title="Ref")
    assert field.allow_null is True
    assert field.title == "Ref"

    # 6. Null validation respects allow_null
    field = Reference(to=Example, allow_null=True)
    assert field.validate(None) is None
    field = Reference(to=Example)
    try:
        field.validate(None)
        assert False, "Expected ValidationError for null"
    except ValidationError:
        pass

    # 7. set_definitions attaches definitions to unresolved references
    from typesystem.schemas import set_definitions

    field = Reference(to="Example")
    assert field.definitions is None
    set_definitions(field, {"Example": Example})
    assert field.definitions is {"Example": Example}
    assert field.target is Example

    print("All Reference constructor tests passed.")

# Generated at 2026-10-24 07:23:12.134193
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:14.691457
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:17.107701
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:19.520561
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:21.934028
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:24.493798
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:28.393699
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:30.808928
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:33.222720
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:35.637194
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:38.053548
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:40.482047
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:23:42.883961
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:45.299036
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:47.714060
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:23:50.130088
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:52.544033
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:54.959694
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:23:57.375490
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:23:59.800650
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:24:02.214019
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:24:04.628089
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:24:07.044917
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:24:09.463143
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:24:11.878031
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:24:14.294910
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:24:16.707014
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:24:19.120511
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:21.534957
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:23.950195
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:26.364206
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:24:28.778488
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:24:31.192244
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:24:33.608745
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:36.021288
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:38.440657
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 07:24:41.563264
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:24:43.976415
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:24:56.563969
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:24:57.862989
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing = SchemaDefinitions()

    # 1. Direct Reference
    direct = Reference(to="Target")
    assert direct.definitions is None
    module_0.set_definitions(direct, definitions)
    assert direct.definitions is definitions

    # 2. Already-set Reference is not overwritten
    preset = Reference(to="Target", definitions=existing)
    module_0.set_definitions(preset, definitions)
    assert preset.definitions is existing

    # 3. Array with single item, tuple items, and no items
    array_single_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=array_single_ref), definitions)
    assert array_single_ref.definitions is definitions

    tuple_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=(tuple_ref, String())), definitions)
    assert tuple_ref.definitions is definitions

    module_0.set_definitions(Array(items=None), definitions)  # must not raise

    # 4. Object properties, plus nested Array -> Object -> Reference
    object_ref = Reference(to="Target")
    nested_ref = Reference(to="Target")
    field = Object(
        properties={
            "direct": object_ref,
            "nested": Array(items=Object(properties={"inner": nested_ref})),
            "plain": String(),
        }
    )
    module_0.set_definitions(field, definitions)
    assert object_ref.definitions is definitions
    assert nested_ref.definitions is definitions

    # 5. Non-container field is a no-op
    module_0.set_definitions(String(), definitions)  # must not raise

# Generated at 2026-10-24 07:25:15.156761
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class Example(Schema):
        first = String()
        second = Integer(default=2)
        third = String()

    # All fields populated: yields keys in field-definition order,
    # regardless of keyword-argument order.
    instance = Example(third="c", first="a")
    assert list(instance) == ["first", "second", "third"]
    assert list(iter(instance)) == ["first", "second", "third"]

    # Sparse instance via dict construction: only set attributes are yielded.
    sparse = Example({"first": "a"})
    assert list(sparse) == ["first"]

    # Only fields with defaults are populated when no values are given.
    empty = Example()
    assert list(empty) == ["second"]

# Generated at 2026-10-24 07:25:17.572831
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:19.986849
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:22.405349
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:24.818923
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:25:27.231827
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:25:29.650321
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 07:25:32.060403
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:34.477155
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:36.892398
# Unit test for function set_definitions

# Generated at 2026-10-24 07:25:39.305378
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:25:41.720323
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:25:44.137193
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:25:46.559807
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:25:48.973939
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:25:51.391114
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 07:25:53.805375
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:25:56.262590
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:25:58.636601
# Unit test for constructor of class Reference

# Generated at 2026-10-24 07:26:18.545946
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import Integer, String
    class Person(Schema):
        name = String(max_length=100)
        age = Integer(default=0)
    class Employee(Person):
        employee_id = Integer(default=1)
    # kwargs with default filled
    p1 = Person(name="Alice")
    assert p1.name == "Alice"
    assert p1.age == 0
    assert hasattr(p1, "name") is True
    assert hasattr(p1, "age") is True
    assert p1.is_sparse is False
    # kwargs all explicit
    p2 = Person(name="Bob", age=30)
    assert p2.name == "Bob"
    assert p2.age == 30
    assert len(p2) == 2
    assert set(iter(p2)) == {"name", "age"}
    assert p2["name"] == "Alice" if False else p2["name"] == "Bob"
    assert p2 == Person(name="Bob", age=30)
    assert (p2 == Person(name="Bob", age=31)) is False
    assert (p2 == "not-a-schema") is False

# Generated at 2026-10-24 07:26:24.984630
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:26:27.398214
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:26:29.815443
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:26:32.229695
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:26:34.646704
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:26:37.062783
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 07:26:39.476710
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:26:41.891621
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:26:44.307983
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 07:26:46.724826
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:26:49.142217
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:26:51.558861
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:26:53.972856
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:26:56.431578
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:26:58.807800
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 07:27:01.223289
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:27:03.635894
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:27:06.050630
# Unit test for constructor of class Schema

# Generated at 2026-10-24 07:27:13.686770
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem import Integer, String

    class Example(Schema):
        name = String()
        age = Integer(default=0)
        email = String()

    # Fully populated instance: all fields set.
    full = Example(name="Alice", age=30, email="alice@example.com")
    assert len(full) == 3

    # Sparse instance: 'email' not provided and has no default,
    # so it is never set and must not be counted.
    sparse = Example(name="Bob")
    # age gets set from its default; email is missing.
    assert len(sparse) == 2
    assert sparse.is_sparse is True

    # Empty instance: only fields with defaults count.
    class DefaultsOnly(Schema):
        a = Integer(default=1)
        b = Integer(default=2)

    empty = DefaultsOnly()
    assert len(empty) == 2

    # len() must agree with the number of keys yielded by __iter__.
    assert len(full) == len(list(iter(full)))
    assert len(sparse) == len(list(iter(sparse)))

# Generated at 2026-10-24 07:27:14.993954
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing = SchemaDefinitions()

    # 1. Direct Reference
    direct = Reference(to="Target")
    assert direct.definitions is None
    module_0.set_definitions(direct, definitions)
    assert direct.definitions is definitions

    # 2. Already-set Reference is not overwritten
    preset = Reference(to="Target", definitions=existing)
    module_0.set_definitions(preset, definitions)
    assert preset.definitions is existing

    # 3. Array with single item, tuple items, and no items
    array_single_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=array_single_ref), definitions)
    assert array_single_ref.definitions is definitions

    tuple_ref = Reference(to="Target")
    module_0.set_definitions(Array(items=(tuple_ref, String())), definitions)
    assert tuple_ref.definitions is definitions

    module_0.set_definitions(Array(items=None), definitions)  # must not raise

    # 4. Object properties, plus nested Array -> Object -> Reference
    object_ref = Reference(to="Target")
    nested_ref = Reference(to="Target")
    field = Object(
        properties={
            "direct": object_ref,
            "nested": Array(items=Object(properties={"inner": nested_ref})),
            "plain": String(),
        }
    )
    module_0.set_definitions(field, definitions)
    assert object_ref.definitions is definitions
    assert nested_ref.definitions is definitions

    # 5. Non-container field is a no-op
    module_0.set_definitions(String(), definitions)  # must not raise

# Generated at 2026-10-24 07:27:40.056027
# Unit test for constructor of class Schema
def test_Schema():
    # Define a schema for testing
    class Example(Schema):
        name = String()
        age = Integer(default=0)

    # 1. Valid keyword arguments are set as attributes
    instance = Example(name="Tom", age=25)
    assert instance.name == "Tom"
    assert instance.age == 25

    # 2. Omitted fields with defaults get the default value
    instance = Example(name="Tom")
    assert instance.age == 0
    assert instance.is_sparse is False

    # 3. Omitted fields without defaults leave the instance sparse
    sparse = Example()
    assert sparse.is_sparse is True

    # 4. Invalid value for a field raises TypeError
    with pytest.raises(TypeError) as exc:
        Example(name=123)
    assert "Invalid argument 'name' for Example()" in str(exc.value)

    # 5. Unknown keyword argument raises TypeError
    with pytest.raises(TypeError) as exc:
        Example(name="Tom", unknown="x")
    assert "'unknown' is an invalid keyword argument for Example()." in str(exc.value)

    # 6. Single positional dict argument populates fields
    instance = Example({"name": "Tom", "age": 25})
    assert instance.name == "Tom"
    assert instance.age == 25

    # 7. Single positional object argument copies matching attributes
    class Other:
        name = "Tom"
        age = 25
        extra = "ignored"

    instance = Example(Other())
    assert instance.name == "Tom"
    assert instance.age == 25

    # 8. More than one positional argument is an error
    with pytest.raises(AssertionError):
        Example({"name": "Tom"}, {"name": "Bob"})

    # 9. Positional argument combined with kwargs is an error
    with pytest.raises(AssertionError):
        Example({"name": "Tom"}, age=25)

    # 10. Mapping-like access reflects constructor results
    instance = Example(name="Tom", age=25)
    assert dict(instance) == {"name": "Tom", "age": 25}