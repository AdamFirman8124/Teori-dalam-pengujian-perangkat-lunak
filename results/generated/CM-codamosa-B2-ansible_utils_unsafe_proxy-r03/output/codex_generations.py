

# Generated at 2026-11-02 14:31:52.962326
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    instance = AnsibleUnsafe()
    assert instance is not None
    assert isinstance(instance, AnsibleUnsafe)
    assert instance.__UNSAFE__ is True
    assert AnsibleUnsafe.__UNSAFE__ is True

# Generated at 2026-11-02 14:34:55.127982
# Unit test for function wrap_var
def test_wrap_var():
    # None passes through unchanged
    assert module_0.wrap_var(None) is None

    # Text strings are wrapped in AnsibleUnsafeText
    value = module_0.wrap_var(u'a')
    assert isinstance(value, AnsibleUnsafeText)
    assert isinstance(value, text_type)
    assert value == u'a'

    # Bytes are wrapped in AnsibleUnsafeBytes
    value = module_0.wrap_var(b'a')
    assert isinstance(value, AnsibleUnsafeBytes)
    assert isinstance(value, binary_type)
    assert value == b'a'

    # Already unsafe objects are returned as-is
    obj = AnsibleUnsafeText(u'a')
    assert module_0.wrap_var(obj) is obj

    # Type conversions preserve the unsafe context
    assert isinstance(obj.encode('utf-8'), AnsibleUnsafeBytes)
    assert isinstance(obj.encode('utf-8').decode('utf-8'), AnsibleUnsafeText)

    # Non-string scalars are not wrapped
    assert module_0.wrap_var(1) == 1
    assert not isinstance(module_0.wrap_var(1), AnsibleUnsafe)
    assert not isinstance(module_0.wrap_var(True), AnsibleUnsafe)
    assert not isinstance(module_0.wrap_var(1.5), AnsibleUnsafe)

    # NativeJinjaText is wrapped in NativeJinjaUnsafeText
    value = module_0.wrap_var(NativeJinjaText(u'{{ foo }}'))
    assert isinstance(value, NativeJinjaUnsafeText)
    assert isinstance(value, NativeJinjaText)

    # Dict keys and values are wrapped
    value = module_0.wrap_var({'k': u'v'})
    assert isinstance(value, dict)
    for k, v in value.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)

    # Nested containers are wrapped recursively, preserving container types
    value = module_0.wrap_var({'k': [u'v', {u'nested': u'value'}, (u't',), set([u's'])]})
    assert isinstance(value, dict)
    assert isinstance(value['k'], list)
    assert isinstance(value['k'][0], AnsibleUnsafeText)
    assert isinstance(value['k'][1], dict)
    assert isinstance(value['k'][1]['nested'], AnsibleUnsafeText)
    assert isinstance(value['k'][2], tuple)
    assert isinstance(value['k'][2][0], AnsibleUnsafeText)
    assert isinstance(value['k'][3], set)
    assert isinstance(next(iter(value['k'][3])), AnsibleUnsafeText)

    # Lists are wrapped
    value = module_0.wrap_var([u'a', u'b'])
    assert isinstance(value, list)
    for v in value:
        assert isinstance(v, AnsibleUnsafeText)

    # Tuples are wrapped
    value = module_0.wrap_var((u'a', u'b'))
    assert isinstance(value, tuple)
    for v in value:
        assert isinstance(v, AnsibleUnsafeText)

    # Sets are wrapped
    value = module_0.wrap_var(set([u'a', u'b']))
    assert isinstance(value, set)
    for v in value:
        assert isinstance(v, AnsibleUnsafeText)

    # Nested list within list
    value = module_0.wrap_var([u'a', [u'b']])
    assert isinstance(value[0], AnsibleUnsafeText)
    assert isinstance(value[1], list)
    assert isinstance(value[1][0], AnsibleUnsafeText)