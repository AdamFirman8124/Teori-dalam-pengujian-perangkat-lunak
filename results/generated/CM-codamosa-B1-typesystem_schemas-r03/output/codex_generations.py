

# Generated at 2026-10-25 05:26:22.058391
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_definition = object()
    replacement_definition = object()

    definitions["User"] = original_definition

    assert definitions["User"] is original_definition
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["User"] = replacement_definition

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] is original_definition
    assert len(definitions) == 1

# Generated at 2026-10-25 05:26:24.914715
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:26:50.541303
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 05:26:52.967113
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:26:55.386495
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:26:57.807926
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:27:00.227371
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:27:02.648813
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:27:05.068970
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:27:07.488420
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 05:27:09.908690
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 05:27:12.327927
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 05:27:16.990832
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:27:19.408787
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:27:21.827974
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:27:24.248253
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:27:26.665259
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:27:33.853729
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():from typesystem.fields import Integer, String


# Generated at 2026-10-25 05:27:43.835525
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": "value"})) == 1
    assert len(ExampleSchema({"first": "value", "second": None})) == 2

# Generated at 2026-10-25 05:28:01.802725
# Unit test for constructor of class Schema
def test_Schema():import pytest

# Generated at 2026-10-25 05:28:04.224386
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:06.805275
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:09.225336
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:11.644359
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:28:14.063859
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:28:16.483207
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:28:18.900210
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:21.320457
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:23.740270
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:28:26.159348
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:28:28.581081
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:28:30.996947
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:28:33.416372
# Unit test for constructor of class Schema

# Generated at 2026-10-25 05:28:35.834137
# Unit test for constructor of class Schema

# Generated at 2026-10-25 05:28:38.251593
# Unit test for constructor of class Schema

# Generated at 2026-10-25 05:28:40.670164
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:28:43.086459
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:28:45.505151
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:28:47.923902
# Unit test for function set_definitions

# Generated at 2026-10-25 05:28:50.343042
# Unit test for function set_definitions

# Generated at 2026-10-25 05:28:52.761082
# Unit test for function set_definitions

# Generated at 2026-10-25 05:28:55.180066
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:28:57.600003
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:29:00.018900
# Unit test for constructor of class Reference

# Generated at 2026-10-25 05:29:02.440213
# Unit test for function set_definitions

# Generated at 2026-10-25 05:29:04.859709
# Unit test for function set_definitions

# Generated at 2026-10-25 05:29:07.322652
# Unit test for function set_definitions

# Generated at 2026-10-25 05:29:09.740064
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:29:12.159702
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:29:14.577285
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:29:16.997092
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:29:19.416733
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:29:21.833491
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 05:29:24.253304
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:29:26.671273
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 05:29:52.190646
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 05:30:01.014171
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:30:06.524078
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:30:13.284453
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:30:29.389241
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherPerson(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    assert person == Person({"name": "Alice", "age": 30})
    assert person != Person({"name": "Bob", "age": 30})
    assert person != Person({"name": "Alice", "age": 31})
    assert person != OtherPerson({"name": "Alice", "age": 30})
    assert person != {"name": "Alice", "age": 30}

# Generated at 2026-10-25 05:30:32.013571
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:30:38.067234
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:30:47.527131
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 05:31:02.916688
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:31:08.072388
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:31:13.923526
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:31:27.864046
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    value = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different = ExampleSchema({"name": "Alice", "age": 31})

    assert value == identical
    assert value != different
    assert value != {"name": "Alice", "age": 30}
    assert value != object()

# Generated at 2026-10-25 05:31:30.656234
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:31:33.061783
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:31:35.481832
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 05:31:45.344077
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:31:57.433823
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:32:05.291751
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 05:32:30.901891
# Unit test for constructor of class Schema
def test_Schema():import pytest


# Generated at 2026-10-25 05:32:33.778676
# Unit test for method __new__ of class SchemaMetaclass