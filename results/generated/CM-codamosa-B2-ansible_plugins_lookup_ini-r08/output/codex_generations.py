

# Generated at 2026-10-24 07:59:39.175803
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:59:50.294807
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 08:00:05.142325
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 08:00:14.867722
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 08:00:28.516489
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 08:00:40.744305
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 08:00:52.288837
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_file(StringIO(
        "[test]\n"
        "foo = bar\n"
        "foobar = baz\n"
        "other = value\n"
    ))

    # Retrieve an existing key.
    assert lookup.get_value("foo", "test", "default", False) == "bar"

    # Return the default when the key does not exist.
    assert lookup.get_value("missing", "test", "default", False) == "default"

    # Retrieve all values whose keys match the regular expression.
    assert lookup.get_value(r"^foo", "test", "default", True) == ["bar", "baz"]

# Generated at 2026-10-24 08:01:08.744874
# Unit test for method run of class LookupModule