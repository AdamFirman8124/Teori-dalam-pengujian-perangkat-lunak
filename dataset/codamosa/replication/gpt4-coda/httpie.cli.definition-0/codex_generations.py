

# Generated at 2024-03-18 05:37:56.141652
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:37:57.337226
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:38:03.099642
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Get the auth plugin mapping from the plugin manager
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # Test the __contains__ method
    for auth_type in auth_plugin_mapping:
        assert auth_type in lazy_choices

    # Test that an invalid auth type is not contained
    assert 'invalid-auth-type' not in lazy_choices

    # Test the __iter__ method
    assert sorted(auth_plugin_mapping.keys()) == sorted(list(iter(lazy_choices)))

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:38:04.877237
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import plugin_manager


# Generated at 2024-03-18 05:38:10.779246
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:16.933920
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types from the plugin manager (assuming some mock plugins)
    expected_auth_types = ['basic', 'digest', 'oauth1', 'mock']

    # Sort both lists to ensure the order is the same for comparison
    auth_types.sort()
    expected_auth_types.sort()

    # Assert that the auth types from the iterator match the expected auth types
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:19.737416
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Run the test
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:38:21.488823
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    auth_type_choices = _AuthTypeLazyChoices()

# Generated at 2024-03-18 05:38:23.637042
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    auth_type_choices = _AuthTypeLazyChoices()

# Generated at 2024-03-18 05:38:30.162791
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:34.080681
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:38:38.885951
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:40.203545
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:38:44.816132
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Run the test
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:38:50.028027
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:54.676437
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:38:56.098536
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:38:59.894978
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown_auth_type' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Call the test function
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:39:06.725257
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin_manager.get_auth_plugin_mapping() to return a fake mapping
    fake_mapping = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
    }
    plugin_manager.get_auth_plugin_mapping = lambda: fake_mapping

    # Test __contains__ method
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'unknown' not in lazy_choices

    # Test __iter__ method
    assert sorted(list(lazy_choices)) == ['basic', 'digest']

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:39:07.520906
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:39:17.421884
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic', 'digest', 'bearer', 'hawk', 'oauth1', 'ntlm', 'netrc'
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, f"Expected auth types {expected_auth_types}, but got {auth_types}"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:39:25.632483
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic',  # Basic auth is usually built-in
        'digest', # Digest auth is usually built-in
        # ... other auth types provided by plugins
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:39:26.977517
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    auth_type_choices = _AuthTypeLazyChoices()

# Generated at 2024-03-18 05:39:33.578756
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin manager with some auth plugins
    plugin_manager_mock = MagicMock()
    plugin_manager_mock.get_auth_plugin_mapping.return_value = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin'
    }

    # Replace the actual plugin manager with the mock
    with patch('httpie.cli.argtypes.plugin_manager', plugin_manager_mock):
        # Test __contains__ method
        assert 'basic' in lazy_choices
        assert 'digest' in lazy_choices
        assert 'unknown' not in lazy_choices

        # Test __iter__ method
        assert sorted(list(lazy_choices)) == ['basic', 'digest']

    print("All tests passed for _AuthTypeLazyChoices.")

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:39:34.277630
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:39:42.438590
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic', 'digest', 'bearer', 'oauth1', 'ntlm', 'custom-auth'
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:39:51.095959
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin_manager.get_auth_plugin_mapping() to return a fake mapping
    fake_mapping = {
        'basic': 'HTTPBasicAuth',
        'digest': 'HTTPDigestAuth',
        'custom': 'CustomAuthPlugin'
    }
    plugin_manager.get_auth_plugin_mapping = lambda: fake_mapping

    # Test __contains__ method
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'custom' in lazy_choices
    assert 'unknown' not in lazy_choices

    # Test __iter__ method
    assert sorted(list(lazy_choices)) == ['basic', 'custom', 'digest']

    print("All tests passed for _AuthTypeLazyChoices.")

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:39:56.339904
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types from the plugin manager (assuming it's mocked or predefined for the test)
    expected_auth_types = sorted(['basic', 'digest', 'oauth1', 'custom'])

    # Assert that the auth_types list matches the expected_auth_types
    assert auth_types == expected_auth_types, f"Expected auth types {expected_auth_types}, but got {auth_types}"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:39:57.760848
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import plugin_manager


# Generated at 2024-03-18 05:40:03.743881
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed the keys from the auth plugin mapping
    auth_plugin_mapping_keys = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert items == auth_plugin_mapping_keys, "Items do not match auth plugin mapping keys"

# Call the test function
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:40:13.849075
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:40:14.677588
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:40:19.791538
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types from the plugin manager (assuming it's mocked or predefined for the test)
    expected_auth_types = sorted(['basic', 'digest', 'oauth1', 'custom'])

    # Assert that the auth_types list matches the expected list
    assert auth_types == expected_auth_types, f"Expected auth types {expected_auth_types}, but got {auth_types}"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:40:20.825831
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import plugin_manager


# Generated at 2024-03-18 05:40:28.161099
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin manager with some auth plugin mappings
    plugin_manager_mock = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
        'bearer': 'httpie.plugins.auth.BearerAuthPlugin'
    }

    # Set the mock plugin manager to the plugin_manager variable
    plugin_manager.get_auth_plugin_mapping = lambda: plugin_manager_mock

    # Test __contains__ method
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert 'bearer' in auth_type_lazy_choices
    assert 'unknown' not in auth_type_lazy_choices

    # Test __iter__ method
    assert sorted(list(auth_type_lazy_choices)) == ['basic', 'bearer', 'digest']

# Run the unit test
test__AuthType

# Generated at 2024-03-18 05:40:32.874802
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types, assuming the plugin_manager has these auth plugins
    expected_auth_types = ['basic', 'digest', 'oauth1', 'oauth2', 'custom']

    # Check if the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Call the test function
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:40:34.276151
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:40:35.001383
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:40:37.058839
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    expected_auth_types = sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2024-03-18 05:40:37.859044
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:41:03.887902
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic',  # Basic auth is usually built-in
        'digest', # Digest auth is usually built-in
        # ... other auth types from plugins
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, f"Expected auth types {expected_auth_types}, but got {auth_types}"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:41:06.450979
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("All tests passed for __contains__ method of _AuthTypeLazyChoices.")


# Generated at 2024-03-18 05:41:10.908727
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic', 'digest', 'oauth1', 'bearer', 'hawk', 'custom'
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:41:14.338137
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")


# Generated at 2024-03-18 05:41:16.476196
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:41:22.916554
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown_auth_type' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Run the test
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:41:29.001488
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin_manager.get_auth_plugin_mapping() to return a fake mapping
    fake_mapping = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
    }

    with mock.patch('httpie.plugins.manager.plugin_manager.get_auth_plugin_mapping', return_value=fake_mapping):
        # Test __contains__ method
        assert 'basic' in lazy_choices
        assert 'digest' in lazy_choices
        assert 'unknown' not in lazy_choices

        # Test __iter__ method
        assert sorted(list(lazy_choices)) == ['basic', 'digest']

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:41:32.006208
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")


# Generated at 2024-03-18 05:41:37.016423
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:41:39.221478
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    auth_type_choices = _AuthTypeLazyChoices()

# Generated at 2024-03-18 05:42:20.625547
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator
    iterator = iter(auth_type_lazy_choices)

    # Fetch all items from the iterator
    items = list(iterator)

    # Assert that the items are sorted
    assert items == sorted(items), "Items are not sorted"

    # Assert that the items are indeed auth plugin names
    for item in items:
        assert item in plugin_manager.get_auth_plugin_mapping(), \
            f"Item '{item}' is not an auth plugin name"

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:42:25.116226
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Call the test function
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:42:26.048447
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:42:27.051672
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:42:36.004467
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin manager with some auth plugins
    plugin_manager_mock = MagicMock()
    plugin_manager_mock.get_auth_plugin_mapping.return_value = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin'
    }

    # Replace the actual plugin manager with the mock
    with patch('httpie.cli.argtypes.plugin_manager', plugin_manager_mock):
        # Test __contains__ method
        assert 'basic' in lazy_choices
        assert 'digest' in lazy_choices
        assert 'unknown' not in lazy_choices

        # Test __iter__ method
        assert sorted(list(lazy_choices)) == ['basic', 'digest']

    # Restore the actual plugin manager
    with patch('httpie.cli.argtypes.plugin_manager', plugin_manager):
        pass

# Run the unit test
test__Auth

# Generated at 2024-03-18 05:42:41.544447
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin_manager has these auth plugins)
    expected_auth_types = sorted([
        'basic', 'digest', 'bearer', 'hawk', 'oauth1'
    ])

    # Assert that the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Call the test function
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:42:49.678632
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Assuming plugin_manager.get_auth_plugin_mapping() returns a dictionary
    # with the following structure for the purpose of this test:
    plugin_manager.get_auth_plugin_mapping.return_value = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
        'bearer': 'httpie.plugins.auth.BearerAuthPlugin',
    }

    # Create an instance of _AuthTypeLazyChoices
    lazy_choices = _AuthTypeLazyChoices()

    # Call the __iter__ method and convert the result to a list
    result = list(lazy_choices.__iter__())

    # Expected result is a sorted list of auth plugin keys
    expected_result = ['basic', 'bearer', 'digest']

    # Assert that the result matches the expected result
    assert result == expected_result, f"Expected {expected_result}, got {result}"

# Generated at 2024-03-18 05:42:54.316768
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Call the test function
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:42:57.070905
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    auth_type_choices = _AuthTypeLazyChoices()

# Generated at 2024-03-18 05:42:58.021292
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 05:44:17.628296
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Call the test function
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:44:19.499859
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import plugin_manager


# Generated at 2024-03-18 05:44:24.801174
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types, assuming the plugin_manager has these auth plugins
    expected_auth_types = sorted([
        'basic', 'digest', 'oauth1', 'bearer', 'hawk', 'custom-auth'
    ])

    # Check if the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:44:30.580140
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin manager with some auth plugins
    plugin_manager_mock = MagicMock()
    plugin_manager_mock.get_auth_plugin_mapping.return_value = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
    }

    # Replace the actual plugin manager with the mock
    with patch('httpie.cli.argtypes.plugin_manager', plugin_manager_mock):
        # Test __contains__ method
        assert 'basic' in lazy_choices
        assert 'digest' in lazy_choices
        assert 'unknown' not in lazy_choices

        # Test __iter__ method
        assert sorted(list(lazy_choices)) == ['basic', 'digest']

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:44:34.382634
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin_manager.get_auth_plugin_mapping() to return a test mapping
    test_mapping = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin'
    }
    plugin_manager.get_auth_plugin_mapping = lambda: test_mapping

    # Test __contains__ method
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'unknown' not in lazy_choices

    # Test __iter__ method
    assert sorted(list(lazy_choices)) == sorted(['basic', 'digest'])

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:44:34.890268
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2024-03-18 05:44:36.014406
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:44:42.363650
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Mock plugin_manager.get_auth_plugin_mapping() to return a fake mapping
    fake_auth_plugin_mapping = {
        'basic': 'httpie.plugins.auth.BasicAuthPlugin',
        'digest': 'httpie.plugins.auth.DigestAuthPlugin',
    }

    with mock.patch('httpie.plugins.manager.plugin_manager.get_auth_plugin_mapping',
                    return_value=fake_auth_plugin_mapping):

        # Test __contains__ method
        assert 'basic' in auth_type_lazy_choices
        assert 'digest' in auth_type_lazy_choices
        assert 'unknown' not in auth_type_lazy_choices

        # Test __iter__ method
        assert sorted(list(auth_type_lazy_choices)) == ['basic', 'digest']

# Run the unit test
test__AuthTypeLazyChoices()

# Generated at 2024-03-18 05:44:43.113906
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:44:49.150985
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types from the plugin manager (assuming some mock plugins)
    expected_auth_types = ['basic', 'digest', 'oauth1', 'mock']

    # Sort both lists to ensure the order is the same for comparison
    auth_types.sort()
    expected_auth_types.sort()

    # Assert that the auth types from the iterator match the expected auth types
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:47:33.237492
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2024-03-18 05:47:35.953237
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():    # Instantiate the class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Test with a known auth type
    assert 'basic' in auth_type_lazy_choices

    # Test with an unknown auth type
    assert 'unknown' not in auth_type_lazy_choices

    print("test__AuthTypeLazyChoices___contains__ passed")

# Run the test
test__AuthTypeLazyChoices___contains__()

# Generated at 2024-03-18 05:47:36.876545
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():import unittest
from httpie.plugins import AuthPlugin


# Generated at 2024-03-18 05:47:47.548566
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types, assuming the plugin_manager has these auth plugins
    expected_auth_types = sorted([
        'basic',  # Basic auth is usually built-in
        'digest', # Digest auth is usually built-in
        'custom'  # Assume there is a custom auth plugin
    ])

    # Check if the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected auth types."

# Run the unit test
test__AuthTypeLazyChoices___iter__()

# Generated at 2024-03-18 05:47:54.335865
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():    # Instantiate the _AuthTypeLazyChoices class
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Get the iterator from the __iter__ method
    iterator = auth_type_lazy_choices.__iter__()

    # Convert the iterator to a list to test its contents
    auth_types = list(iterator)

    # Expected auth types (assuming the plugin manager has these auth plugins)
    expected_auth_types = ['basic', 'digest', 'oauth1']

    # Check if the auth_types list matches the expected_auth_types list
    assert auth_types == expected_auth_types, "The auth types do not match the expected values"

# Run the unit test
test__AuthTypeLazyChoices___iter__()