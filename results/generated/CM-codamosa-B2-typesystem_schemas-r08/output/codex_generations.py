

# Generated at 2026-10-24 13:35:58.546185
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    # empty construction
    s = SchemaDefinitions()
    assert isinstance(s, MutableMapping)
    assert s._definitions == {}
    assert isinstance(s._definitions, dict)
    assert len(s) == 0
    assert list(s) == []

    # from dict positional arg
    s = SchemaDefinitions({"a": 1, "b": 2})
    assert s._definitions == {"a": 1, "b": 2}
    assert s["a"] == 1
    assert s["b"] == 2
    assert len(s) == 2

    # copies, does not alias input
    src = {"a": 1}
    s = SchemaDefinitions(src)
    assert s._definitions == src
    assert s._definitions is not src
    src["a"] = 999
    assert s["a"] == 1

    # from iterable of pairs
    s = SchemaDefinitions([("a", 1), ("b", 2)])
    assert s._definitions == {"a": 1, "b": 2}

    s = SchemaDefinitions((k, v) for k, v in [("x", 10)])
    assert s._definitions == {"x": 10}

    # from kwargs only
    s = SchemaDefinitions(a=1, b=2)
    assert s._definitions == {"a": 1, "b": 2}

    # from positional + kwargs merged, kwargs win
    s = SchemaDefinitions({"a": 1}, b=2)
    assert s._definitions == {"a": 1, "b": 2}

    s = SchemaDefinitions({"a": 1}, a=2)
    assert s._definitions == {"a": 2}

    # from another SchemaDefinitions (MutableMapping)
    orig = SchemaDefinitions(a=1)
    s = SchemaDefinitions(orig)
    assert s._definitions == {"a": 1}
    assert s["a"] == 1

    # too many positionals propagates TypeError from dict()
    try:
        SchemaDefinitions({}, {})
    except TypeError:
        pass
    else:
        assert False, "expected TypeError for multiple positional args"

# Generated at 2026-10-24 13:36:00.974072
# Unit test for constructor of class SchemaMetaclass

# Generated at 2026-10-24 13:36:03.391821
# Unit test for constructor of class SchemaMetaclass

# Generated at 2026-10-24 13:36:05.806479
# Unit test for constructor of class SchemaMetaclass

# Generated at 2026-10-24 13:36:08.227532
# Unit test for method __getitem__ of class Schema

# Generated at 2026-10-24 13:36:10.643292
# Unit test for method __getitem__ of class Schema

# Generated at 2026-10-24 13:36:13.057253
# Unit test for method __getitem__ of class Schema

# Generated at 2026-10-24 13:36:21.249899
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():definitions = SchemaDefinitions({"first": 1, "second": 2})

# Generated at 2026-10-24 13:36:33.628082
# Unit test for method __len__ of class SchemaDefinitions
def test_SchemaDefinitions___len__():
    definitions = SchemaDefinitions()

    assert len(definitions) == 0

    definitions["User"] = object()
    definitions["Address"] = object()

    assert len(definitions) == 2

    del definitions["User"]

    assert len(definitions) == 1

# Generated at 2026-10-24 13:37:05.365173
# Unit test for constructor of class Reference
def test_Reference():
    class Example(Schema):
        name = Field()

    # 1. String target: deferred lookup, nothing resolved yet.
    ref = Reference("Example")
    assert isinstance(ref, Field)
    assert ref.to == "Example"
    assert ref.definitions is None
    assert not hasattr(ref, "_target")
    assert ref.target_string == "Example"

    # 2. Class target: resolved immediately at construction.
    ref = Reference(Example)
    assert ref.to is Example
    assert ref.target is Example
    assert ref.target_string == "Example"

    # 3. String target + definitions: resolves lazily, then caches.
    ref = Reference("Example", definitions={"Example": Example})
    assert not hasattr(ref, "_target")
    assert ref.target is Example
    assert ref._target is Example  # cached after first access

    # 4. String target with no definitions: AssertionError on access.
    ref = Reference("Example")
    with pytest.raises(AssertionError):
        ref.target

    # 5. Non-Schema class is rejected.

# Generated at 2026-10-24 13:37:07.934683
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:37:10.347997
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:37:12.761443
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:37:15.175038
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:37:39.165179
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import Integer, String


# Generated at 2026-10-24 13:37:57.064554
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:37:59.490674
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:38:02.177975
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:38:04.594175
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:07.005060
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:09.629583
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:12.056061
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:14.471495
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:16.885187
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:19.302715
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:21.712167
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:24.125505
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:26.540941
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:38:28.955396
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:38:31.370753
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:38:33.784901
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:36.198707
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:38.611091
# Unit test for method serialize of class Reference

# Generated at 2026-10-24 13:38:41.043061
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:43.455619
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:45.869089
# Unit test for function set_definitions

# Generated at 2026-10-24 13:38:48.282882
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:50.706063
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:53.110851
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:55.523957
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:38:57.936826
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:00.351211
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:02.765735
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:05.179465
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:07.590586
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:10.041336
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:39:12.458907
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:39:14.865597
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:39:17.280796
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:39:19.691761
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:39:22.107368
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:39:24.522308
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:39:26.933903
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:39:29.346633
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:39:31.761348
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:34.177867
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:36.590100
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:39.005284
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:41.416681
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:43.832770
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:39:46.248789
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:39:48.662093
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:39:51.073862
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:39:53.484367
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:55.895454
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:39:58.307994
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:00.865399
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:03.278211
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:05.691958
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:08.105213
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:10.519600
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:12.932361
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:15.347152
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:17.760643
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:20.174328
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:40:22.588573
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:40:25.002932
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:40:27.416567
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:40:29.830402
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:32.244341
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:34.657777
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:37.069710
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:39.483160
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:41.896538
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:40:44.308702
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:46.728766
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:49.141075
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:51.554930
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:53.968730
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:56.381717
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:40:58.795531
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:01.208245
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:03.622597
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:06.036388
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:41:08.449908
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:41:10.864447
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:41:17.080746
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:19.492075
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:21.904541
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:41:24.320850
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:41:26.736519
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:41:29.147776
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:41:31.563783
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:33.986189
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:36.406761
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:38.813907
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:41.227740
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:43.642077
# Unit test for function set_definitions

# Generated at 2026-10-24 13:41:46.056469
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:41:48.469557
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:41:50.883597
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:41:53.297734
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:41:55.711903
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:41:58.126407
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:42:00.538524
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:02.953886
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:05.364120
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:07.777571
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:42:10.191042
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:42:12.605631
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:42:15.020346
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:17.435579
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:19.849310
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:42:22.263578
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:42:24.680709
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:42:29.162927
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import String

# Generated at 2026-10-24 13:42:50.895652
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()
        email = String(default="")

    # All fields populated (two explicit, one via default) -> 3
    example = Example(name="Tom", age=20)
    assert len(example) == 3

    # Sparse instance: only attributes actually set are counted -> 1
    sparse = Example({"name": "Tom"})
    assert len(sparse) == 1
    assert sparse.is_sparse

    # Nothing set (defaults are NOT applied on the dict path) -> 0
    empty = Example({})
    assert len(empty) == 0

    # Schema class with no fields at all -> 0
    class Empty(Schema):
        pass

    assert len(Empty()) == 0

# Generated at 2026-10-24 13:42:53.478040
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:42:55.891415
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:42:58.409727
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:00.914869
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:03.329056
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:05.741369
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:08.154540
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:10.567258
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:12.980836
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:15.393620
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:17.808770
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:20.222054
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:43:22.636141
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:25.242671
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:27.662185
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:30.075136
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:32.492853
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:34.905015
# Unit test for function set_definitions

# Generated at 2026-10-24 13:43:37.318118
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:43:39.732328
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:43:42.148545
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:43:44.564218
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:43:46.977364
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:43:49.388296
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:43:51.803368
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:43:54.217712
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:43:56.635497
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:01.495991
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:44:03.909637
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:44:06.325565
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:44:08.741177
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:11.155750
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:13.565685
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:15.981434
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:18.394491
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:20.806458
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:23.220674
# Unit test for function set_definitions

# Generated at 2026-10-24 13:44:25.634442
# Unit test for function set_definitions

# Generated at 2026-10-24 13:44:28.050173
# Unit test for function set_definitions

# Generated at 2026-10-24 13:44:30.463517
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:32.878103
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:35.291340
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:37.705229
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:44:40.118936
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:44:42.533312
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:44:44.952299
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:47.371653
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:49.787949
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:44:52.203817
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:54.622566
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:57.039708
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:44:59.450791
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:45:01.865443
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:45:04.283434
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-24 13:45:06.695505
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:45:09.112310
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:45:11.527424
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:45:24.207939
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:45:26.634816
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:45:29.051822
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:45:31.476519
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:45:33.896836
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 13:45:36.322222
# Unit test for method __iter__ of class Schema