

# Generated at 2024-03-18 02:39:41.953438
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that no additional keys are present
    assert len(data) == 2, "There should be exactly two keys in the loaded data"


# Generated at 2024-03-18 02:39:46.661742
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:39:52.431828
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy stream
    dummy_stream = "dummy content"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(dummy_stream)

    # Check if the loader is an instance of the correct class
    assert isinstance(loader, AnsibleLoader)

    # Check if the loader has been initialized with the correct stream
    assert loader.stream == dummy_stream

    # If applicable, check if the loader has been initialized with the correct file_name and vault_secrets
    # (This part of the test would require additional context about how file_name and vault_secrets are used within AnsibleLoader)


# Generated at 2024-03-18 02:39:56.953100
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:40:02.826596
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:40:08.378985
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:40:15.676396
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:40:21.325982
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a mock stream
    mock_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(mock_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(mock_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:40:27.338377
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that no additional keys are present
    assert len(data) == 2, "There should be exactly two keys in the loaded data"


# Generated at 2024-03-18 02:40:33.187669
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:40:41.593997
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:40:46.271443
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:40:55.361079
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:41:01.614080
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that no additional keys are present
    assert len(data) == 2, "There should be exactly two keys in the loaded data"


# Generated at 2024-03-18 02:41:08.476310
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:41:16.205467
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader with the stream
    loader = AnsibleLoader(yaml_stream)

    # Load the first document
    data = loader.get_single_data()

    # Verify that the data is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Verify that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Verify that there are no more documents in the stream
    assert loader.check_data() is False, "There should be no more documents in the stream"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:41:18.302369
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    fake_stream = "example_key: example_value"

# Generated at 2024-03-18 02:41:26.629031
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader with the stream
    loader = AnsibleLoader(yaml_stream)

    # Load the first document
    data = loader.get_single_data()

    # Assert that the data is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that there are no more documents
    assert loader.check_data() is False, "There should be no more documents in the stream"


# Generated at 2024-03-18 02:41:33.731099
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:41:39.303965
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:41:47.499941
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert the data is loaded correctly
    assert data == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:41:52.307476
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:41:53.930164
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    fake_stream = "example_key: example_value"

# Generated at 2024-03-18 02:42:01.634558
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:07.744148
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:14.225517
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader with the stream
    loader = AnsibleLoader(yaml_stream)

    # Load the first document
    data = loader.get_single_data()

    # Assert that the data is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are as expected
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:19.405664
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:26.154500
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:42:33.422494
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:39.454307
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:42:53.648100
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:42:59.841493
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy stream
    dummy_stream = "dummy_content: test"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(dummy_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.yaml_constructors is not None
        assert loader.yaml_multi_constructors is not None

    # Test without libyaml available
    else:
        loader = AnsibleLoader(dummy_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.yaml_constructors is not None
        assert loader.yaml_multi_constructors is not None

    # Additional tests can be added here to check for specific behaviors of the AnsibleLoader


# Generated at 2024-03-18 02:43:07.728987
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:43:13.006880
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:43:17.556366
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:43:22.395971
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader after use
    loader.dispose()


# Generated at 2024-03-18 02:43:28.293048
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:43:34.489698
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that no additional keys are present
    assert len(data) == 2, "There should be exactly two keys in the loaded data"


# Generated at 2024-03-18 02:43:39.225966
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:43:44.982669
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:06.864761
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:44:11.313029
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader with the stream
    loader = AnsibleLoader(yaml_stream)

    # Load the first document
    data = loader.get_single_data()

    # Assert that the data is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are as expected
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:20.481398
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:44:24.920540
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:29.335882
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:44:34.426277
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:44:38.511517
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data == {'key': 'value', 'another_key': 'another_value'}, "Loaded data does not match expected values"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:43.489796
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data == {'key': 'value', 'another_key': 'another_value'}, "Loaded data does not match expected values"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:47.482279
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:44:52.152284
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a mock stream for testing
    mock_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(mock_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.construct_mapping(loader.get_single_node()) == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(mock_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.construct_mapping(loader.get_single_node()) == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:45:28.341066
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:45:35.968639
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader with the stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:45:41.723727
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:45:45.633189
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.construct_mapping(loader.get_single_node()) == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.construct_mapping(loader.get_single_node()) == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:45:49.548796
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:45:51.159546
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    fake_stream = "example_key: example_value"

# Generated at 2024-03-18 02:45:57.418113
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:46:03.877615
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:46:11.405601
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:46:17.129260
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:47:26.049056
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    print("All tests passed for AnsibleLoader.")


# Generated at 2024-03-18 02:47:31.301997
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Initialize AnsibleLoader with the dummy stream
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert that the data loaded is a dictionary
    assert isinstance(data, dict), "Loaded data should be a dictionary"

    # Assert that the keys and values are correctly loaded
    assert data.get('key') == 'value', "Value for 'key' should be 'value'"
    assert data.get('another_key') == 'another_value', "Value for 'another_key' should be 'another_value'"

    # Assert that no additional keys are present
    assert len(data) == 2, "There should be exactly two keys in the loaded data"


# Generated at 2024-03-18 02:47:34.892334
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Prepare a YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Create an instance of AnsibleLoader
    loader = AnsibleLoader(yaml_stream)

    # Load the data using the loader
    data = loader.get_single_data()

    # Assert the loaded data matches the expected result
    assert data == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:47:41.516787
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:47:45.610631
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        parsed_data = loader.get_single_data()
        assert parsed_data == {'key': 'value', 'another_key': 'another_value'}


# Generated at 2024-03-18 02:47:47.541671
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    fake_stream = "example_key: example_value"

# Generated at 2024-03-18 02:47:51.602161
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        assert loader.get_single_data() == {'key': 'value', 'another_key': 'another_value'}

    # Clean up the loader
    loader.dispose()


# Generated at 2024-03-18 02:47:56.328997
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:48:03.468086
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert isinstance(data, dict)
        assert data == {'key': 'value', 'another_key': 'another_value'}
        loader.dispose()


# Generated at 2024-03-18 02:48:10.171048
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():    # Create a dummy YAML stream
    yaml_stream = "key: value\nanother_key: another_value"

    # Test with libyaml available
    if HAS_LIBYAML:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}

    # Test without libyaml available
    else:
        loader = AnsibleLoader(yaml_stream)
        assert isinstance(loader, AnsibleLoader)
        # Parse the stream and get the first document
        data = loader.get_single_data()
        assert data == {'key': 'value', 'another_key': 'another_value'}

    # Test with file_name and vault_secrets parameters
    file_name = 'test_file.yml'
    vault_secrets = [('default', 'secret')]
    loader_with_params