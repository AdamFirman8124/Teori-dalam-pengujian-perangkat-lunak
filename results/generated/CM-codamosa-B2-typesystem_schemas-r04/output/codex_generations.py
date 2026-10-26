

# Generated at 2026-10-25 07:57:41.505566
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    first_definition = object()
    second_definition = object()

    definitions = SchemaDefinitions(
        {"First": first_definition},
        Second=second_definition,
    )

    assert len(definitions) == 2
    assert dict(definitions) == {
        "First": first_definition,
        "Second": second_definition,
    }
    assert definitions["First"] is first_definition
    assert definitions["Second"] is second_definition

# Generated at 2026-10-25 07:57:43.922219
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:57:46.339835
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:57:48.755451
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:57:51.174144
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 07:57:53.588781
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 07:57:56.006993
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 07:57:58.418572
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:58:00.836367
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:58:03.251746
# Unit test for method validate of class Reference

# Generated at 2026-10-25 07:58:05.665455
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:08.079193
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:10.493821
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:13.366314
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:15.780686
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:18.195091
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 07:58:20.608605
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:58:23.023692
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:58:25.436339
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:58:35.966696
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": 1})) == 1
    assert len(ExampleSchema({"first": 1, "second": 2})) == 2
    assert len(
        ExampleSchema({"first": 1, "second": 2, "third": 3})
    ) == 3

# Generated at 2026-10-25 07:59:10.797067
# Unit test for method validate of class Reference
def test_Reference_validate():calls = []


# Generated at 2026-10-25 07:59:13.214904
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:15.654582
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:18.130842
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:20.540862
# Unit test for constructor of class Reference

# Generated at 2026-10-25 07:59:22.955084
# Unit test for constructor of class Reference

# Generated at 2026-10-25 07:59:25.539436
# Unit test for constructor of class Reference

# Generated at 2026-10-25 07:59:27.954180
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:30.368292
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:32.782205
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 07:59:35.195757
# Unit test for function set_definitions

# Generated at 2026-10-25 07:59:37.610589
# Unit test for function set_definitions

# Generated at 2026-10-25 07:59:40.024473
# Unit test for function set_definitions

# Generated at 2026-10-25 07:59:42.437863
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:59:44.862533
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:59:47.292583
# Unit test for constructor of class Schema

# Generated at 2026-10-25 07:59:49.706921
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 07:59:52.124891
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 07:59:54.538403
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 07:59:56.954000
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 07:59:59.368963
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 08:00:01.783702
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 08:00:04.198647
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:06.615027
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:09.032889
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:11.529354
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:00:13.952322
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:00:16.362616
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:00:18.777312
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:21.197608
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:23.608758
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:00:26.020875
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:00:37.560140
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:01:05.487008
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import Integer, String


# Generated at 2026-10-25 08:01:08.151748
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:01:10.567871
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:01:12.981032
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:01:15.395156
# Unit test for function set_definitions

# Generated at 2026-10-25 08:01:17.810063
# Unit test for function set_definitions

# Generated at 2026-10-25 08:01:20.224821
# Unit test for function set_definitions

# Generated at 2026-10-25 08:01:22.638386
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:01:25.051729
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:01:27.466157
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:01:29.878337
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:01:32.292357
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:01:34.705976
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:01:37.122363
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:01:39.535857
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:01:41.953918
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:01:44.362984
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:01:46.845553
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:01:49.260649
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:01:51.674104
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:02:00.068697
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:02:08.636990
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 08:02:20.136353
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Object(properties={})
        second = Object(properties={})

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": {}})) == 1
    assert len(ExampleSchema({"first": {}, "second": {}})) == 2

# Generated at 2026-10-25 08:02:23.005121
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:02:25.419313
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:02:27.960077
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:02:30.375559
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 08:02:32.788780
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 08:02:35.204080
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 08:02:37.621851
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:02:40.264967
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:02:42.679477
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:02:45.093296
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 08:02:47.507573
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 08:02:49.920959
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 08:02:52.339532
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:02:54.754529
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:03:01.711102
# Unit test for method validate of class Reference

# Generated at 2026-10-25 08:03:04.783870
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:03:23.085138
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:03:50.760557
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 08:03:53.293930
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:03:55.707496
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:04:22.939963
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:04:26.966943
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:04:29.384379
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:04:31.871316
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:04:34.449433
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:04:36.862952
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:04:39.278532
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:04:41.735870
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:04:44.155233
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:04:46.564912
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:04:48.982209
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:04:51.394883
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:04:53.814228
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:04:56.226219
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:04:58.640116
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:05:01.060035
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:05:03.477500
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:05:21.808497
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:05:23.228217
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.fields import Field

    ref = Reference("ExampleSchema")
    assert isinstance(ref, Field)
    assert ref.to == "ExampleSchema"
    assert ref.target_string == "ExampleSchema"
    assert ref.definitions is None
    assert ref.allow_null is False
    assert ref.errors == {"null": "May not be null."}

    ref_nullable = Reference("ExampleSchema", allow_null=True)
    assert ref_nullable.allow_null is True
    assert ref_nullable.validate(None) is None

    class ExampleSchema(Schema):
        name = Field()
        age = Field(default=0)

    ref_cls = Reference(ExampleSchema)
    assert ref_cls.to is ExampleSchema
    assert ref_cls.target_string == "ExampleSchema"
    assert ref_cls.target is ExampleSchema

    definitions = SchemaDefinitions()
    definitions["ExampleSchema"] = ExampleSchema
    ref_def = Reference("ExampleSchema", definitions=definitions)
    assert ref_def.definitions is definitions
    assert ref_def.target is ExampleSchema

# Generated at 2026-10-25 08:05:31.792693
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer(default=0)

    # Fully populated: fields in declaration order, repr of values.
    example = Example(name="Tom", age=13)
    assert repr(example) == "Example(name='Tom', age=13)"

    # Sparse: age not set (constructed from a partial dict).
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Default-filled field appears; missing field triggers sparse marker.
    partial = Example()
    assert repr(partial) == "Example(age=0) [sparse]"

    # None values are included as-is.
    class Nullable(Schema):
        nickname = String(allow_null=True)

    nullable = Nullable({"nickname": None})
    assert repr(nullable) == "Nullable(nickname=None)"

# Generated at 2026-10-25 08:05:34.583833
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 08:05:51.170718
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 08:05:53.768549
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:05:56.300949
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:05:58.833884
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:01.251863
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:03.853267
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:06.355995
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:21.369956
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():from typesystem.fields import String


# Generated at 2026-10-25 08:06:24.180402
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:50.986244
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:53.524256
# Unit test for constructor of class Schema

# Generated at 2026-10-25 08:06:56.109125
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:06:58.526009
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:07:00.928267
# Unit test for constructor of class Reference

# Generated at 2026-10-25 08:07:03.345304
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:07:05.760739
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:07:10.737925
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 08:07:25.585650
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:07:53.654653
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 08:07:56.072791
# Unit test for method __iter__ of class Schema