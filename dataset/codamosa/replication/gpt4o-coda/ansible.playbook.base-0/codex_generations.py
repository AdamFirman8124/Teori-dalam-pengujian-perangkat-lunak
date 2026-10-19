

# Generated at 2024-05-31 19:28:33.782311
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:28:35.273250
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():    base_instance = Base()

# Generated at 2024-05-31 19:28:44.772533
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2024-05-31 19:28:47.618727
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():    # Create a mock object of FieldAttributeBase
    mock_obj = FieldAttributeBase()

    # Define test data
    test_data = {
        'name': 'test_name',
        'attribute': 'test_attribute',
        'value': 'test_value',
        'templar': 'test_templar'
    }

    # Set attributes to mock object
    mock_obj._valid_attrs = {
        'name': Mock(),
        'attribute': Mock(),
        'value': Mock(),
        'templar': Mock()
    }

    # Call the method with test data
    mock_obj.load_data(test_data)

    # Assert that the attributes are set correctly
    assert mock_obj.name == 'test_name'
    assert mock_obj.attribute == 'test_attribute'
    assert mock_obj.value == 'test_value'
    assert mock_obj.templar == 'test_templar'


# Generated at 2024-05-31 19:28:52.383485
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:28:55.728078
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():    # Create a mock object of FieldAttributeBase
    mock_obj = FieldAttributeBase()
    
    # Set some attributes to the mock object
    mock_obj._valid_attrs = {'attr1': 'value1', 'attr2': 'value2'}
    mock_obj._attributes = {'attr1': 'value1', 'attr2': 'value2'}
    mock_obj._attr_defaults = {'attr1': 'default1', 'attr2': 'default2'}
    mock_obj._loader = 'loader'
    mock_obj._variable_manager = 'variable_manager'
    mock_obj._validated = True
    mock_obj._finalized = True
    mock_obj._uuid = '1234-5678-9101'
    
    # Call the get_ds method
    ds = mock_obj.get_ds()
    
    # Assert the returned value is as expected

# Generated at 2024-05-31 19:28:59.811161
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:29:03.897657
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:29:05.503820
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():    base_instance = Base()

# Generated at 2024-05-31 19:29:10.610225
# Unit test for method validate of class FieldAttributeBase

# Generated at 2024-05-31 19:29:34.281977
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():    # Create a mock object of FieldAttributeBase
    mock_obj = FieldAttributeBase()
    
    # Set the _ds attribute
    mock_obj._ds = {'key': 'value'}
    
    # Call the get_ds method
    result = mock_obj.get_ds()
    
    # Assert the result
    assert result == {'key': 'value'}, f"Expected {{'key': 'value'}}, but got {result}"


# Generated at 2024-05-31 19:29:37.523649
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:29:40.673229
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:29:43.701796
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:29:47.144934
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:29:50.649727
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    # Create a mock object of FieldAttributeBase
    class MockFieldAttributeBase(FieldAttributeBase):
        def __init__(self):
            self._valid_attrs = {
                'name': FieldAttribute(isa='string', default='default_name'),
                'age': FieldAttribute(isa='int', default=0),
                'details': FieldAttribute(isa='class', class_type=MockDetails, default=MockDetails)
            }
            self._uuid = None
            self._finalized = False
            self._squashed = False

    class MockDetails:
        def __init__(self):
            self.info = 'default_info'

        def deserialize(self, data):
            self.info = data.get('info', 'default_info')

    # Create an instance of the mock object
    obj = MockFieldAttributeBase()

    # Define the data to deserialize

# Generated at 2024-05-31 19:29:54.275993
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:29:57.443284
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:29:59.813213
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    obj = FieldAttributeBase()

# Generated at 2024-05-31 19:30:04.805988
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():    base_instance = Base()
    
    # Mocking the get_dep_chain method to return a list of mock objects with _role_path attributes

# Generated at 2024-05-31 19:30:51.695786
# Unit test for method dump_me of class FieldAttributeBase

# Generated at 2024-05-31 19:30:55.596289
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:30:59.458141
# Unit test for method validate of class FieldAttributeBase

# Generated at 2024-05-31 19:31:02.925860
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:31:06.296010
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():    base_instance = Base()

# Generated at 2024-05-31 19:31:10.593886
# Unit test for method deserialize of class FieldAttributeBase

# Generated at 2024-05-31 19:31:13.958304
# Unit test for method dump_me of class FieldAttributeBase

# Generated at 2024-05-31 19:31:17.686696
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:31:21.274324
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:31:26.135685
# Unit test for method validate of class FieldAttributeBase

# Generated at 2024-05-31 19:31:55.036287
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():    base_instance = Base()

# Generated at 2024-05-31 19:31:59.258897
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:32:03.287187
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:32:07.736067
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:32:12.194228
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:32:15.643013
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():    base_instance = Base()

# Generated at 2024-05-31 19:32:19.362087
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:32:24.110513
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:32:29.235269
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:32:34.557777
# Unit test for method squash of class FieldAttributeBase

# Generated at 2024-05-31 19:33:02.345403
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:33:06.249517
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:33:09.553549
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:33:12.815211
# Unit test for method dump_me of class FieldAttributeBase

# Generated at 2024-05-31 19:33:18.374996
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    obj = FieldAttributeBase()

# Generated at 2024-05-31 19:33:25.301621
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2024-05-31 19:33:29.868076
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    obj = FieldAttributeBase()

# Generated at 2024-05-31 19:33:33.218956
# Unit test for method deserialize of class FieldAttributeBase

# Generated at 2024-05-31 19:33:37.827461
# Unit test for method dump_me of class FieldAttributeBase

# Generated at 2024-05-31 19:33:42.294569
# Unit test for method squash of class FieldAttributeBase

# Generated at 2024-05-31 19:34:12.288114
# Unit test for method deserialize of class FieldAttributeBase

# Generated at 2024-05-31 19:34:19.899411
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    obj = FieldAttributeBase()

# Generated at 2024-05-31 19:34:24.013569
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:34:33.109566
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:34:43.844206
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:34:47.352122
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:34:52.341847
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:34:56.870679
# Unit test for method squash of class FieldAttributeBase

# Generated at 2024-05-31 19:35:02.017785
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:35:03.442721
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():    base_instance = Base()

# Generated at 2024-05-31 19:35:34.034272
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:35:37.775964
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():    # Create a mock class to simulate FieldAttributeBase
    class MockFieldAttributeBase:
        def __init__(self):
            self._valid_attrs = {
                'attr1': MockAttribute('string', 'default1'),
                'attr2': MockAttribute('int', 0),
                'attr3': MockAttribute('list', []),
                'attr4': MockAttribute('class', MockClass)
            }
            self._uuid = None
            self._finalized = False
            self._squashed = False

        def deserialize(self, data):
            if not isinstance(data, dict):
                raise AnsibleAssertionError('data (%s) should be a dict but is a %s' % (data, type(data)))

            for (name, attribute) in iteritems(self._valid_attrs):
                if name in data:
                    setattr(self, name, data[name])

# Generated at 2024-05-31 19:35:41.532472
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:35:46.094433
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2024-05-31 19:35:52.804193
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:35:57.458410
# Unit test for method validate of class FieldAttributeBase

# Generated at 2024-05-31 19:36:01.390180
# Unit test for method dump_me of class FieldAttributeBase

# Generated at 2024-05-31 19:36:04.989383
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:36:08.676010
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:36:14.479824
# Unit test for method validate of class FieldAttributeBase

# Generated at 2024-05-31 19:36:43.971392
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:36:47.898596
# Unit test for method squash of class FieldAttributeBase

# Generated at 2024-05-31 19:36:51.723105
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2024-05-31 19:36:54.759538
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2024-05-31 19:36:58.835564
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():    original = FieldAttributeBase()

# Generated at 2024-05-31 19:37:02.302857
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():    # Create a mock object of FieldAttributeBase
    mock_obj = FieldAttributeBase()
    
    # Set up the mock object's attributes
    mock_obj._valid_attrs = {
        'attr1': Mock(),
        'attr2': Mock()
    }
    mock_obj._alias_attrs = ['alias_attr']
    mock_obj._attributes = {
        'attr1': 'value1',
        'attr2': 'value2'
    }
    mock_obj._attr_defaults = {
        'attr1': 'default1',
        'attr2': 'default2'
    }
    mock_obj._loader = 'loader'
    mock_obj._variable_manager = 'variable_manager'
    mock_obj._validated = True
    mock_obj._finalized = True
    mock_obj._uuid = 'uuid'
    mock_obj._ds = 'ds_value'

    # Call the method to be tested
    result = mock_obj.dump_me()

    # Assert the expected

# Generated at 2024-05-31 19:37:06.680877
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2024-05-31 19:37:10.154285
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2024-05-31 19:37:18.117474
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():    # Create a mock object of FieldAttributeBase
    mock_obj = FieldAttributeBase()
    
    # Set up initial attributes
    mock_obj._valid_attrs = {
        'attr1': Mock(),
        'attr2': Mock(),
        'attr3': Mock()
    }
    mock_obj._alias_attrs = ['attr2']
    mock_obj._attributes = {
        'attr1': 'value1',
        'attr2': 'value2',
        'attr3': 'value3'
    }
    mock_obj._attr_defaults = {
        'attr1': 'default1',
        'attr2': 'default2',
        'attr3': 'default3'
    }
    mock_obj._loader = 'loader'
    mock_obj._variable_manager = 'variable_manager'
    mock_obj._validated = True
    mock_obj._finalized = False
    mock_obj._uuid = 'uuid'
    
    # Call the method to be tested

# Generated at 2024-05-31 19:37:22.625827
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2024-05-31 19:37:54.178202
# Unit test for method post_validate of class FieldAttributeBase