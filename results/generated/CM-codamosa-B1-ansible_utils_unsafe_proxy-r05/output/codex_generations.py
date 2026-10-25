

# Generated at 2026-10-24 11:43:06.702386
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 11:43:09.117545
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 11:43:11.538339
# Unit test for function to_unsafe_bytes

# Generated at 2026-10-24 11:43:13.959989
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:43:16.376680
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:43:18.797851
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:43:21.213180
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:43:23.630141
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:43:26.047177
# Unit test for constructor of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:43:28.463516
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:30.880082
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:33.300738
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:35.713930
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:38.129364
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:40.544397
# Unit test for constructor of class UnsafeProxy

# Generated at 2026-10-24 11:43:42.960827
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:45.376278
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:47.793817
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:50.208973
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:52.623860
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:55.042512
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:57.459566
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:59.885346
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:02.297348
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:04.712468
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:06.085224
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

# Generated at 2026-10-24 11:44:08.848977
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:10.167696
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

# Generated at 2026-10-24 11:44:12.808931
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:14.229431
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

# Generated at 2026-10-24 11:44:17.216645
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:18.584640
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

# Generated at 2026-10-24 11:44:21.310638
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:22.641241
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

# Generated at 2026-10-24 11:44:25.610674
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:26.925146
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

# Generated at 2026-10-24 11:44:29.733604
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:31.137795
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

# Generated at 2026-10-24 11:44:33.788447
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:35.234432
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

# Generated at 2026-10-24 11:44:37.654229
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:40.068952
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:42.490656
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:44.905898
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:47.442425
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:50.007410
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:52.776229
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:54.113863
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

# Generated at 2026-10-24 11:44:56.745182
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:58.080468
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

# Generated at 2026-10-24 11:45:00.837605
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:02.286944
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

# Generated at 2026-10-24 11:45:05.099503
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:07.518876
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:10.132269
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:12.553709
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:15.115702
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:17.538940
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:19.959228
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:22.378398
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:24.799666
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:27.220604
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:29.637131
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:32.058208
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:34.612762
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:37.034785
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:39.448743
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:41.865905
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:44.285897
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:46.698618
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:49.115930
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:51.533747
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:53.948403
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:56.366823
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:58.781299
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:01.201898
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:03.621077
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:06.042374
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:08.459988
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:10.879391
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:13.300223
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:15.716619
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:18.138491
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:20.553375
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:22.969126
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:25.383957
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:27.800962
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:30.220628
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:32.637731
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:35.054369
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:37.472814
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:39.891530
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:42.306158
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:44.726492
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:47.144206
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:49.560967
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:51.977867
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:54.395128
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:56.810136
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:59.226659
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:01.642667
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:04.064310
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:06.480894
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:08.899073
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:11.319525
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:13.735820
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:16.150451
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:18.601359
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:20.986182
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:23.408051
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:24.793048
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

# Generated at 2026-10-24 11:47:27.485114
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:28.879360
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

# Generated at 2026-10-24 11:47:31.675328
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:33.004688
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

# Generated at 2026-10-24 11:47:35.872407
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:37.303566
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

# Generated at 2026-10-24 11:47:40.091399
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:41.428258
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

# Generated at 2026-10-24 11:47:44.368753
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:45.682646
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

# Generated at 2026-10-24 11:47:48.361342
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:50.873753
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:53.288878
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:55.705790
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:58.122410
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:00.539603
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:02.960314
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:05.374243
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:07.790939
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:10.204628
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:12.622727
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:15.037991
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:17.453688
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:19.870302
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:22.288682
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:24.702562
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:27.134868
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:29.550755
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:31.973110
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:34.393201
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:36.813107
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:39.232617
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:41.656149
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:44.076369
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:47.042174
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:48.375194
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

# Generated at 2026-10-24 11:48:53.389045
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:54.775033
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

# Generated at 2026-10-24 11:48:57.586290
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:59.635989
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

# Generated at 2026-10-24 11:49:02.396394
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:03.980490
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

# Generated at 2026-10-24 11:49:06.801393
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:08.234727
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

# Generated at 2026-10-24 11:49:10.893608
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:12.226147
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

# Generated at 2026-10-24 11:49:15.044481
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:16.363215
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

# Generated at 2026-10-24 11:49:18.782054
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:21.309030
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:23.724591
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:26.142968
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:28.561381
# Unit test for function wrap_var

# Generated at 2026-10-24 11:49:58.309228
# Unit test for function wrap_var
def test_wrap_var():from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText

# Generated at 2026-10-24 11:50:00.734403
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:03.152412
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:05.684848
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:08.104069
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:10.520726
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:12.939654
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:19.227693
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:21.644785
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:24.061379
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:26.480467
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:28.898258
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:31.315103
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:33.731827
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:36.149675
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:38.569364
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:40.983589
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:43.398697
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:45.815021
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:48.234052
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:50.654278
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:53.073654
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:55.498277
# Unit test for function wrap_var

# Generated at 2026-10-24 11:50:57.906980
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:00.322115
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:03.642255
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:04.976024
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

# Generated at 2026-10-24 11:51:07.694797
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:09.060912
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

# Generated at 2026-10-24 11:51:11.724725
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:13.103706
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

# Generated at 2026-10-24 11:51:15.750773
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:17.064427
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

# Generated at 2026-10-24 11:51:30.709497
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:33.216667
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:35.732720
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:38.157393
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:40.571626
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:42.987505
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:45.723672
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:48.150258
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:50.565532
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:52.991715
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:55.406971
# Unit test for function wrap_var

# Generated at 2026-10-24 11:51:57.827145
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:00.244684
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:02.663884
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:05.079901
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:07.499065
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:09.918701
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:12.337952
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:14.761954
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:17.196407
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:19.613347
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:22.041239
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:24.461259
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:26.879512
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:29.298351
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:31.714300
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:34.133267
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:36.552037
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:38.971259
# Unit test for function wrap_var

# Generated at 2026-10-24 11:52:41.392272
# Unit test for function wrap_var

# Generated at 2026-10-24 11:53:01.280569
# Unit test for function wrap_var

# Generated at 2026-10-24 11:53:02.608563
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

# Generated at 2026-10-24 11:53:05.375568
# Unit test for function wrap_var

# Generated at 2026-10-24 11:53:06.722161
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