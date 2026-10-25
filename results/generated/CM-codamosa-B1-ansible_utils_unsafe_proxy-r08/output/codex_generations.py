

# Generated at 2026-10-24 13:37:38.370409
# Unit test for function wrap_var

# Generated at 2026-10-24 13:37:39.711708
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:37:53.897232
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 13:37:56.312502
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 13:37:58.727068
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 13:38:01.142476
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 13:38:03.553989
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 13:38:05.968812
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 13:38:08.382278
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 13:38:10.932862
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 13:38:13.347196
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 13:38:15.761981
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 13:38:18.176391
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 13:38:20.590720
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 13:38:23.004847
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:25.418876
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:27.833136
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:30.245966
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:32.659241
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:35.071991
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:37.485514
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:39.898591
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:42.313066
# Unit test for function wrap_var

# Generated at 2026-10-24 13:38:44.729628
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:47.141067
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:49.556192
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:51.970840
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:54.386093
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:56.798734
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:38:59.213680
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:01.627689
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:04.042172
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:06.456078
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:08.870286
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:11.282740
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:13.695704
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:16.108262
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:18.521328
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:20.935202
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:23.352662
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:25.763901
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:28.176983
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:30.591247
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:33.004649
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:35.417485
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:37.833544
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:40.245339
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:42.660602
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:45.072705
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:47.485496
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:49.899008
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:52.311774
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:54.723830
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:57.138286
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:39:59.551667
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:01.964573
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:04.383082
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:06.792904
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:09.203961
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:11.618458
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:14.036318
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:16.444642
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:18.858024
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:21.272067
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:23.689320
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:26.100894
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:28.514070
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:30.927949
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:33.341443
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:35.752807
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:38.164698
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:40.577432
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:42.988752
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:45.401930
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 13:40:48.314349
# Unit test for function wrap_var

# Generated at 2026-10-24 13:40:50.728283
# Unit test for function wrap_var

# Generated at 2026-10-24 13:40:53.141084
# Unit test for function wrap_var

# Generated at 2026-10-24 13:40:55.567153
# Unit test for function wrap_var

# Generated at 2026-10-24 13:40:57.979601
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:00.392607
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:02.806623
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:05.220232
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:07.633675
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:10.047804
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:12.463194
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:14.882763
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:17.291586
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:19.705673
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:22.117913
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:24.531621
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:26.945540
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:29.360278
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:31.773527
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:34.187315
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:36.605752
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:39.015621
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:41.429685
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:43.842669
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:46.257106
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:48.671142
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:51.085495
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:53.499082
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:55.913660
# Unit test for function wrap_var

# Generated at 2026-10-24 13:41:58.327388
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:00.944704
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:03.357403
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:05.775236
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:08.184569
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:10.596672
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:13.010263
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:15.425142
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:17.838693
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:20.252424
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:22.666881
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:25.081719
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:26.409538
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:30.704692
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:32.044215
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:34.687718
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:36.331702
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:38.977834
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:40.739708
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:43.475346
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:44.909266
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:47.672926
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:49.029118
# Unit test for function wrap_var
def test_wrap_var():# str -> AnsibleUnsafeText, preserving content
    wrapped_str = module_0.wrap_var("hello")
    assert isinstance(wrapped_str, str)
    assert wrapped_str == "hello"
    assert getattr(wrapped_str, "__UNSAFE__", False) is True

    # bytes -> AnsibleUnsafeBytes, preserving content
    wrapped_bytes = module_0.wrap_var(b"hello")
    assert isinstance(wrapped_bytes, bytes)
    assert wrapped_bytes == b"hello"
    assert getattr(wrapped_bytes, "__UNSAFE__", False) is True

    # already-unsafe values are returned unchanged (same object)
    already = AnsibleUnsafeText(" templated ")
    assert module_0.wrap_var(already) is already

    # None passes through
    assert module_0.wrap_var(None) is None

    # list is wrapped element-wise, type preserved
    wrapped_list = module_0.wrap_var(["a", "b"])
    assert isinstance(wrapped_list, list)
    assert wrapped_list == ["a", "b"]
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_list)

    # tuple is wrapped element-wise, type preserved
    wrapped_tuple = module_0.wrap_var(("a", "b"))
    assert isinstance(wrapped_tuple, tuple)
    assert wrapped_tuple == ("a", "b")
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_tuple)

    # set is wrapped element-wise
    wrapped_set = module_0.wrap_var({"a"})
    assert isinstance(wrapped_set, set)
    assert wrapped_set == {"a"}
    assert all(getattr(item, "__UNSAFE__", False) is True for item in wrapped_set)

    # dict: both keys and values are wrapped, type preserved
    wrapped_dict = module_0.wrap_var({"k": "v"})
    assert isinstance(wrapped_dict, dict)
    assert wrapped_dict == {"k": "v"}
    for k, v in wrapped_dict.items():
        assert getattr(k, "__UNSAFE__", False) is True
        assert getattr(v, "__UNSAFE__", False) is True

    # nested structures are wrapped recursively
    nested = module_0.wrap_var({"outer": ["inner"]})
    assert nested["outer"][0] == "inner"
    assert getattr(nested["outer"][0], "__UNSAFE__", False) is True

    # non-string, non-container scalars pass through untouched
    assert module_0.wrap_var(42) == 42
    assert module_0.wrap_var(42) is not None
    assert not isinstance(module_0.wrap_var(42), AnsibleUnsafe)

# Generated at 2026-10-24 13:42:51.815108
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:54.331030
# Unit test for function wrap_var

# Generated at 2026-10-24 13:42:56.839556
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:01.027642
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:03.442409
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:05.858394
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:08.271548
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:10.684580
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:13.097986
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:15.512500
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:17.926460
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:20.340222
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:22.754796
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:25.318563
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:27.731915
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:30.145191
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:32.559149
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:34.972629
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:37.386606
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:39.798635
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:42.213493
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:44.627050
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:47.040912
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:49.454459
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:51.869921
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:54.282656
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:56.700740
# Unit test for function wrap_var

# Generated at 2026-10-24 13:43:59.111676
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:01.525349
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:03.940510
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:06.354622
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:08.770646
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:11.183072
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:18.273915
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:20.686698
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:23.100216
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:25.514085
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:27.926956
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:30.344652
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:32.754427
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:35.168927
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:37.582423
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:39.996645
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:42.410420
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:44.825157
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:47.244629
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:49.663391
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:52.080315
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:54.497736
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:56.914452
# Unit test for function wrap_var

# Generated at 2026-10-24 13:44:59.328439
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:01.743464
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:04.158488
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:06.571505
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:08.987512
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:11.400500
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:13.816049
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:16.234919
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:18.656601
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:21.069850
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:23.484495
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:25.900352
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:28.318618
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:50.737636
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:53.154229
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:55.571893
# Unit test for function wrap_var

# Generated at 2026-10-24 13:45:57.983615
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:00.401147
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:02.816681
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:05.230476
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:07.653173
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:10.070119
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:12.486896
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:14.902590
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:17.319410
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:19.736079
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:22.152521
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:24.565510
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:26.977468
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:29.390354
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:31.804166
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:34.216586
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:36.632389
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:39.046718
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:41.463705
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:43.882265
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:46.293777
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:48.706985
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:51.121222
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:53.534208
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:55.946952
# Unit test for function wrap_var

# Generated at 2026-10-24 13:46:58.359790
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:00.772228
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:27.719469
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:30.131389
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:32.542759
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:34.989610
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:37.369314
# Unit test for function wrap_var

# Generated at 2026-10-24 13:47:39.782565
# Unit test for function wrap_var