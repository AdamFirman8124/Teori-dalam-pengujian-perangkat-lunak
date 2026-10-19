

# Generated at 2024-05-31 02:15:02.743506
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:04.953481
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:07.244188
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:08.570637
# Unit test for function get_all_facts
def test_get_all_facts():
    class MockModule:
        def __init__(self, params):
            self.params = params

    mock_params = {'gather_subset': ['all']}
    mock_module = MockModule(mock_params)
    result = get_all_facts(mock_module)
    assert isinstance(result, dict)
    assert 'default_ipv4' in result

# Generated at 2024-05-31 02:15:10.514842
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:12.769390
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:14.672133
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:17.035837
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:21.395934
# Unit test for function get_all_facts

# Generated at 2024-05-31 02:15:23.309389
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:32.156197
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:35.358257
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:37.138045
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:38.859664
# Unit test for function get_all_facts

# Generated at 2024-05-31 02:15:42.465342
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:44.481086
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:49.780060
# Unit test for function ansible_facts

# Generated at 2024-05-31 02:15:51.168731
# Unit test for function get_all_facts

# Generated at 2024-05-31 02:15:52.931583
# Unit test for function get_all_facts

# Generated at 2024-05-31 02:15:54.463303
# Unit test for function ansible_facts