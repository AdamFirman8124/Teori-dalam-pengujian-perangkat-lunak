

# Generated at 2026-10-24 11:38:37.683390
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 11:38:40.097445
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 11:38:42.518563
# Unit test for function to_unsafe_text

# Generated at 2026-10-24 11:38:45.126251
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-24 11:38:47.574914
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-24 11:38:50.006481
# Unit test for constructor of class AnsibleUnsafeText

# Generated at 2026-10-24 11:38:52.439250
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:38:54.855218
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:38:57.275440
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:38:59.694515
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-24 11:39:02.114542
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-24 11:39:04.531446
# Unit test for constructor of class AnsibleUnsafe

# Generated at 2026-10-24 11:39:06.952278
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:39:09.398695
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:39:11.819350
# Unit test for method decode of class AnsibleUnsafeBytes

# Generated at 2026-10-24 11:39:26.777805
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    with mock.patch("ansible.utils.display.Display") as mock_display:
        deprecated = mock_display.return_value.deprecated

        # 1. Already-unsafe objects pass through unchanged
        unsafe_text = AnsibleUnsafeText("already unsafe")
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b"already unsafe")
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

        # 2. Text strings are wrapped as AnsibleUnsafeText
        result = UnsafeProxy("hello")
        assert type(result) is AnsibleUnsafeText
        assert isinstance(result, AnsibleUnsafeText)
        assert result == "hello"
        assert result.__UNSAFE__ is True

        # 3. Non-string objects pass through unchanged
        assert UnsafeProxy(123) == 123
        assert UnsafeProxy(None) is None

        items = ["a", "b"]
        assert UnsafeProxy(items) is items

        raw_bytes = b"hello"
        assert UnsafeProxy(raw_bytes) is raw_bytes

        # Deprecation is

# Generated at 2026-10-24 11:39:28.106883
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    with mock.patch("ansible.utils.display.Display") as mock_display:
        deprecated = mock_display.return_value.deprecated

        # 1. Already-unsafe objects pass through unchanged
        unsafe_text = AnsibleUnsafeText("already unsafe")
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b"already unsafe")
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

        # 2. Text strings are wrapped as AnsibleUnsafeText
        result = UnsafeProxy("hello")
        assert type(result) is AnsibleUnsafeText
        assert isinstance(result, AnsibleUnsafeText)
        assert result == "hello"
        assert result.__UNSAFE__ is True

        # 3. Non-string objects pass through unchanged
        assert UnsafeProxy(123) == 123
        assert UnsafeProxy(None) is None

        items = ["a", "b"]
        assert UnsafeProxy(items) is items

        raw_bytes = b"hello"
        assert UnsafeProxy(raw_bytes) is raw_bytes

        # Deprecation is

# Generated at 2026-10-24 11:39:46.559556
# Unit test for function wrap_var

# Generated at 2026-10-24 11:39:48.976927
# Unit test for function wrap_var

# Generated at 2026-10-24 11:39:51.397560
# Unit test for function wrap_var

# Generated at 2026-10-24 11:39:53.816775
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:39:56.234840
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:39:58.650894
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:01.069255
# Unit test for function wrap_var

# Generated at 2026-10-24 11:40:03.486139
# Unit test for function wrap_var

# Generated at 2026-10-24 11:40:05.901321
# Unit test for function wrap_var

# Generated at 2026-10-24 11:40:08.320216
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:10.739108
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:13.169864
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:15.591211
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:18.008936
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:20.432309
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:22.850544
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:25.267311
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:27.688170
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:30.106154
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:32.521951
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:40:45.858979
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe


# Generated at 2026-10-24 11:40:47.194203
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    with mock.patch("ansible.utils.display.Display") as mock_display:
        deprecated = mock_display.return_value.deprecated

        # 1. Already-unsafe objects pass through unchanged
        unsafe_text = AnsibleUnsafeText("already unsafe")
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b"already unsafe")
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        deprecated.assert_called_with(
            'UnsafeProxy is being deprecated. Use wrap_var or '
            'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            version='2.13',
            collection_name='ansible.builtin',
        )

        # 2. Text strings are wrapped as AnsibleUnsafeText
        result = UnsafeProxy("hello")
        assert type(result) is AnsibleUnsafeText
        assert isinstance(result, AnsibleUnsafeText)
        assert result == "hello"
        assert result.__UNSAFE__ is True

        # 3. Non-string objects pass through unchanged
        assert UnsafeProxy(123) == 123
        assert UnsafeProxy(None) is None

        items = ["a", "b"]
        assert UnsafeProxy(items) is items

        raw_bytes = b"hello"
        assert UnsafeProxy(raw_bytes) is raw_bytes

        # Deprecation is

# Generated at 2026-10-24 11:41:05.928671
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:08.354807
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:10.773010
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:13.189619
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:15.607104
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:18.024370
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:20.442739
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:22.859939
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:25.291284
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:27.709408
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:30.130409
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:32.768742
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:35.184511
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:37.605222
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:40.018507
# Unit test for function wrap_var

# Generated at 2026-10-24 11:41:42.438477
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:44.860752
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:47.275419
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:49.694824
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:52.112061
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:54.529871
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:56.949101
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:41:59.368369
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:01.793711
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:04.210832
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:06.626969
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:09.041504
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:11.462229
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:13.882442
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:16.303149
# Unit test for method __new__ of class UnsafeProxy

# Generated at 2026-10-24 11:42:18.717693
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:21.134423
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:23.557894
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:25.966549
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:28.387875
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:30.802297
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:33.219399
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:35.635942
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:42.685658
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

# Generated at 2026-10-24 11:42:45.672374
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:47.105527
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

# Generated at 2026-10-24 11:42:49.764384
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:51.203493
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

# Generated at 2026-10-24 11:42:53.968086
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:55.405892
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

# Generated at 2026-10-24 11:42:58.069533
# Unit test for function wrap_var

# Generated at 2026-10-24 11:42:59.398483
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

# Generated at 2026-10-24 11:43:02.035936
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:03.367016
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

# Generated at 2026-10-24 11:43:05.891178
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:08.306456
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:10.727296
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:13.148998
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:15.567362
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:17.986325
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:20.404143
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:22.823166
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:25.240129
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:27.657218
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:30.075743
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:32.494805
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:34.912520
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:37.330517
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:39.759224
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:42.163323
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:44.582034
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:46.996522
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:49.413434
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:51.831062
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:54.246859
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:56.666618
# Unit test for function wrap_var

# Generated at 2026-10-24 11:43:59.085409
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:01.500377
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:03.919516
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:24.936976
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:26.326367
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

# Generated at 2026-10-24 11:44:29.130508
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:30.524706
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

# Generated at 2026-10-24 11:44:33.293857
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:34.722315
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

# Generated at 2026-10-24 11:44:37.242040
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:39.982144
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:42.397708
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:46.145423
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:48.564323
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:49.940998
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

# Generated at 2026-10-24 11:44:52.769676
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:54.079852
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

# Generated at 2026-10-24 11:44:56.716493
# Unit test for function wrap_var

# Generated at 2026-10-24 11:44:58.081523
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

# Generated at 2026-10-24 11:45:00.905791
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:02.294001
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

# Generated at 2026-10-24 11:45:05.342680
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:07.764199
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:10.185282
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:12.605148
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:15.119947
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:17.544556
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:19.963472
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:22.381846
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:24.802792
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:27.222946
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:29.641000
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:32.066940
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:34.616748
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:37.037886
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:39.451797
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:41.868805
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:44.289370
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:46.701520
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:52.429393
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:54.846254
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:57.264269
# Unit test for function wrap_var

# Generated at 2026-10-24 11:45:59.682523
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:02.102020
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:04.521847
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:06.936994
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:09.354239
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:11.773455
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:14.192548
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:16.612657
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:19.028341
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:21.441366
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:23.858933
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:26.278626
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:28.694160
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:31.112379
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:33.529995
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:35.946431
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:38.362888
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:40.781561
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:43.198767
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:45.618038
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:48.031958
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:50.448815
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:52.863926
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:55.280770
# Unit test for function wrap_var

# Generated at 2026-10-24 11:46:57.695853
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:00.111684
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:02.528265
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:12.607571
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:15.024465
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:17.441545
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:19.859135
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:22.275728
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:40.008793
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:42.735657
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:44.067824
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

# Generated at 2026-10-24 11:47:46.714026
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:48.090949
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

# Generated at 2026-10-24 11:47:50.719728
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:53.229424
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:55.645632
# Unit test for function wrap_var

# Generated at 2026-10-24 11:47:58.153518
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:00.570285
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:02.985394
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:05.404384
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:07.820439
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:10.234608
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:12.652238
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:15.067976
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:17.482657
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:19.899894
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:22.317243
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:24.735316
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:27.169071
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:29.584641
# Unit test for function wrap_var

# Generated at 2026-10-24 11:48:32.002415
# Unit test for function wrap_var