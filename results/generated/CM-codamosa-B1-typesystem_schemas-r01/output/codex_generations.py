

# Generated at 2026-10-25 03:57:37.115301
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:57:39.642643
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:58:10.819916
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 03:58:20.907763
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})
    assert repr(person) == "Person(name='Alice', age=30)"

    sparse_person = Person({"name": "Alice"})
    assert repr(sparse_person) == "Person(name='Alice') [sparse]"

# Generated at 2026-10-25 03:58:29.137719
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    definitions["User"] = "original"
    assert definitions["User"] == "original"

    with pytest.raises(AssertionError):
        definitions["User"] = "replacement"

    # A duplicate assignment must not overwrite the original definition.
    assert definitions["User"] == "original"

# Generated at 2026-10-25 03:58:30.482878
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    # 1. Init from kwargs
    defs = SchemaDefinitions(a=1)
    assert defs["a"] == 1
    assert len(defs) == 1

    # 2. Init from a dict
    defs = SchemaDefinitions({"a": 1, "b": 2})
    assert len(defs) == 2
    assert defs["b"] == 2

    # 3. Iteration yields keys
    assert sorted(defs) == ["a", "b"]

    # 4. __setitem__ inserts new keys
    defs["c"] = 3
    assert defs["c"] == 3
    assert len(defs) == 3

    # 5. __setitem__ rejects duplicate keys
    with pytest.raises(AssertionError):
        defs["c"] = 99

    # 6. __delitem__ removes keys
    del defs["c"]
    assert "c" not in defs
    assert len(defs) == 2

    # 7. Missing keys raise KeyError
    with pytest.raises(KeyError):
        defs["missing"]

    # 8. MutableMapping mixin methods work
    defs.update({"d": 4})
    assert defs.pop("d") == 4
    assert "d" not in defs

# Generated at 2026-10-25 03:58:35.804528
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert set(iter(definitions)) == {"a", "b"}
    assert list(definitions) == list(definitions._definitions)

# Generated at 2026-10-25 03:58:38.222368
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:58:40.639875
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:59:20.349071
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 03:59:26.698035
# Unit test for method __delitem__ of class SchemaDefinitions
def test_SchemaDefinitions___delitem__():
    definitions = SchemaDefinitions({"first": 1, "second": 2})

    del definitions["first"]

    assert len(definitions) == 1
    assert "first" not in definitions
    assert definitions["second"] == 2

    with pytest.raises(KeyError):
        del definitions["first"]

# Generated at 2026-10-25 03:59:41.649484
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    validated_value = object()
    target.validate.return_value = validated_value

    reference = Reference(
        to="User",
        definitions={"User": target},
    )
    value = {"name": "Alice"}

    # Delegates validation to the resolved target and forwards strict.
    assert reference.validate(value, strict=True) is validated_value
    target.validate.assert_called_once_with(value, strict=True)

    # Null is rejected by default without calling the target.
    target.reset_mock()
    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    assert [message.text for message in exc_info.value.messages()] == [
        "May not be null."
    ]
    target.validate.assert_not_called()

    # Null is accepted when explicitly allowed.
    nullable_reference = Reference(
        to="User",
        definitions={"User": target},
        allow_null=True,
    )
    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

# Generated at 2026-10-25 03:59:50.260022
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["User"] = original

    assert definitions["User"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError, match="has already been set"):
        definitions["User"] = replacement

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:00:00.923555
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:00:09.617188
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:00:16.874664
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:00:38.659235
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        pass

    ExampleSchema.fields = {
        "name": None,
        "age": None,
    }

    schema = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different = ExampleSchema({"name": "Alice", "age": 31})

    assert schema == identical
    assert schema != different
    assert schema != {"name": "Alice", "age": 30}
    assert schema != object()

# Generated at 2026-10-25 04:00:41.077642
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:00:43.493571
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:00:45.905651
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:00:48.325307
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:00:56.912428
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:01:03.790414
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:01:13.833458
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    assert len(ExampleSchema()) == 0
    assert len(ExampleSchema({"first": "one"})) == 1
    assert len(ExampleSchema({"first": "one", "second": "two"})) == 2

    # Attributes not declared as schema fields are not counted.
    instance = ExampleSchema({"first": "one"})
    instance.extra = "ignored"
    assert len(instance) == 1

# Generated at 2026-10-25 04:01:24.521383
# Unit test for method validate of class Reference
def test_Reference_validate():
    calls = []

    class TargetSchema(Schema):
        @classmethod
        def module_0.validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return {"validated": value}

    reference = Reference(to=TargetSchema)

    # Non-null values are validated by the target, preserving strict mode.
    value = {"example": "value"}
    assert reference.validate(value, strict=True) == {"validated": value}
    assert calls == [(value, True)]

    # Null is rejected by default without calling the target.
    with pytest.raises(ValidationError):
        reference.validate(None)

    assert calls == [(value, True)]

    # Null is accepted when explicitly allowed, also without target validation.
    nullable_reference = Reference(to=TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None
    assert calls == [(value, True)]

# Generated at 2026-10-25 04:01:30.193813
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:01:32.727110
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:01:35.261591
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:01:37.669891
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:01:40.084452
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:01:42.499722
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:01:44.915824
# Unit test for function set_definitions

# Generated at 2026-10-25 04:01:47.330145
# Unit test for function set_definitions

# Generated at 2026-10-25 04:01:49.749941
# Unit test for function set_definitions

# Generated at 2026-10-25 04:01:52.162667
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:01:54.576667
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:02:16.067184
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:02:27.305585
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    empty = ExampleSchema({})
    sparse = ExampleSchema({"first": "one", "third": "three"})
    complete = ExampleSchema(
        {"first": "one", "second": "two", "third": "three"}
    )

    assert len(empty) == 0
    assert len(sparse) == 2
    assert len(complete) == 3

    # Attributes not declared as schema fields must not affect the length.
    sparse.extra = "ignored"
    assert len(sparse) == 2

# Generated at 2026-10-25 04:02:37.163301
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    empty = ExampleSchema()
    assert len(empty) == 0

    partial = ExampleSchema({"first": None})
    assert len(partial) == 1  # Attributes set to None still count.

    full = ExampleSchema(
        {
            "first": "one",
            "second": "two",
            "third": "three",
        }
    )
    assert len(full) == 3

    full.extra = "not a schema field"
    assert len(full) == 3

    del full.second
    assert len(full) == 2

# Generated at 2026-10-25 04:02:45.268008
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:02:52.830747
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:02:55.371210
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:02:57.788876
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:03:02.762592
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():instance = Schema()

# Generated at 2026-10-25 04:03:21.604793
# Unit test for constructor of class Schema
def test_Schema():from types import SimpleNamespace


# Generated at 2026-10-25 04:03:46.885816
# Unit test for constructor of class Schema
def test_Schema():from types import SimpleNamespace


# Generated at 2026-10-25 04:03:49.346475
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:03:51.873585
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:03:54.290033
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:03:56.711324
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:03:59.128650
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:04:04.816828
# Unit test for method __delitem__ of class SchemaDefinitions
def test_SchemaDefinitions___delitem__():definitions = SchemaDefinitions({"User": int, "Item": str})

# Generated at 2026-10-25 04:04:07.526175
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:04:24.319514
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 04:04:34.463489
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:04:42.500919
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:04:44.918360
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:04:47.515269
# Unit test for function set_definitions

# Generated at 2026-10-25 04:04:49.929877
# Unit test for function set_definitions

# Generated at 2026-10-25 04:04:52.343529
# Unit test for function set_definitions

# Generated at 2026-10-25 04:04:54.878570
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:04:57.513911
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:04:59.930935
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:05:02.346454
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:05:04.762731
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:05:07.183592
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:05:09.596504
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:05:12.012713
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:05:19.171184
# Unit test for method __delitem__ of class SchemaDefinitions
def test_SchemaDefinitions___delitem__():definitions = SchemaDefinitions({"a": 1, "b": 2})

# Generated at 2026-10-25 04:05:27.796165
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["Example"] = original

    assert definitions["Example"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = replacement

    assert definitions["Example"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:05:41.673544
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:05:48.959703
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:05:51.636967
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:05:56.206187
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:05:58.623417
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:01.039871
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:03.463519
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:05.877719
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:08.292169
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:10.705582
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:13.292710
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:15.707680
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:18.122775
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:20.543322
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:22.961760
# Unit test for function set_definitions

# Generated at 2026-10-25 04:06:25.381864
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:27.793469
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:30.209257
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:06:32.638948
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:06:35.058520
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:06:37.473254
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:06:39.900272
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:06:42.315220
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:06:44.729653
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:06:47.144709
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:06:49.562306
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:06:51.977437
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:06:54.392223
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:06:56.807090
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:06:59.221873
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:07:01.650774
# Unit test for function set_definitions

# Generated at 2026-10-25 04:07:04.064152
# Unit test for function set_definitions

# Generated at 2026-10-25 04:07:06.480123
# Unit test for function set_definitions

# Generated at 2026-10-25 04:07:10.212894
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:07:12.628173
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:07:15.081726
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:07:17.502226
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:07:19.914959
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:07:22.329881
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:07:24.744410
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:07:27.160008
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:07:29.575392
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:07:31.991295
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:07:34.411392
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:07:36.825943
# Unit test for method __iter__ of class Schema