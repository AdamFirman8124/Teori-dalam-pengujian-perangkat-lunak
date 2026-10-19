

# Generated at 2024-03-18 04:32:45.187652
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:32:51.209032
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = MockTemplar()

# Generated at 2024-03-18 04:32:59.017665
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    # Mock objects and data for testing
    mock_templar = MagicMock()
    mock_globals = {'global_var': 'global_value'}
    mock_locals = {'local_var': 'local_value', 'l_hidden': 'should_not_appear'}

    # Create an instance of AnsibleJ2Vars with the mock data
    j2_vars = AnsibleJ2Vars(mock_templar, mock_globals, mock_locals)

    # Test retrieval of a global variable
    assert j2_vars['global_var'] == 'global_value', "Failed to get global variable"

    # Test retrieval of a local variable
    assert j2_vars['local_var'] == 'local_value', "Failed to get local variable"

    # Test that hidden local variables (prefixed with 'l_') are not accessible
    with pytest.raises(KeyError):
        j2_vars['l_hidden']

    # Test retrieval of a variable from templar's available variables
   

# Generated at 2024-03-18 04:32:59.846314
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():import pytest
from ansible.template import Templar


# Generated at 2024-03-18 04:33:05.520345
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    # Mock objects and data for testing
    templar = Mock()
    globals_dict = {'global_var': 'global_value'}
    locals_dict = {'local_var': 'local_value'}
    templar.available_variables = {'available_var': 'available_value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test retrieval of local variable
    assert ansible_j2_vars['local_var'] == 'local_value'

    # Test retrieval of available variable
    assert ansible_j2_vars['available_var'] == 'available_value'

    # Test retrieval of global variable
    assert ansible_j2_vars['global_var'] == 'global_value'

    # Test that KeyError is raised for undefined variable
    with pytest.raises(KeyError):
        ansible_j2_vars['undefined_var']

    # Test that AnsibleUndefinedVariable is raised for undefined templated variable

# Generated at 2024-03-18 04:33:10.426515
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = Templar(loader=None, variables={'var1': 'value1', 'var2': 'value2'})

# Generated at 2024-03-18 04:33:14.170663
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    # Setup the templar and globals
    templar = MagicMock()
    templar.available_variables = {'a': 1, 'b': 2, 'c': 3}
    globals = {'ansible_version': '2.9.0', 'other_global_var': 'value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals)

    # Test __len__ method
    assert len(ansible_j2_vars) == 5, "Length of AnsibleJ2Vars instance should be 5"

# Generated at 2024-03-18 04:33:20.792620
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variables
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Set available variables in the templar mock
    templar.available_variables = {'templar_var': 'templar_value', 'other_templar_var': 'other_value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'ansible_version' in ansible_j2_vars
    assert 'other_global_var' in ansible_j2_vars
    assert 'local_var' in ansible_j2_vars
    assert 'another_local_var' in ansible_j2_vars
    assert 'templar_var' in ansible_j2

# Generated at 2024-03-18 04:33:26.380340
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:33:31.665960
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = MagicMock()

# Generated at 2024-03-18 04:33:44.234259
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = MockTemplar(variables={'var1': 'value1', 'var2': 'value2'})
    globals_dict = {'global1': 'gvalue1', 'range': range}
    locals_dict = {'l_var3': 'value3', 'var4': 'value4'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'var1' in ansible_j2_vars
    assert 'var2' in ansible_j2_vars
    assert 'global1' in ansible_j2_vars
    assert 'range' in ansible_j2_vars
    assert 'var3' in ansible_j2_vars
    assert 'var4' in ansible_j2_vars
    assert 'nonexistent_var' not in ansible_j2_vars


# Generated at 2024-03-18 04:33:49.553839
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:33:54.887150
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = MockTemplar(variables={'var1': 'value1', 'var2': 'value2'})
    globals_dict = {'ansible_version': '2.9.0', 'other_global': 'global_value'}
    locals_dict = {'l_localvar': 'local_value', 'another_local': 'another_value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'var1' in ansible_j2_vars
    assert 'var2' in ansible_j2_vars
    assert 'ansible_version' in ansible_j2_vars
    assert 'other_global' in ansible_j2_vars
    assert 'localvar' in ansible_j2_vars
    assert 'another_local' in ansible_j2_vars

# Generated at 2024-03-18 04:34:00.300275
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:34:05.925602
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = MockTemplar(variables={'var1': 'value1', 'var2': 'value2'})
    globals_dict = {'global1': 'gvalue1', 'global2': 'gvalue2'}
    locals_dict = {'l_var3': 'lvalue3', 'var4': 'value4'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert ansible_j2_vars.__contains__('var1') == True
    assert ansible_j2_vars.__contains__('var2') == True
    assert ansible_j2_vars.__contains__('global1') == True
    assert ansible_j2_vars.__contains__('var3') == True
    assert ansible_j2_vars.__contains__('var4') == True
    assert ansible_j2

# Generated at 2024-03-18 04:34:10.765379
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variables
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'ansible_playbook': 'test.yml'}
    locals_dict = {'l_my_local_var': 'local_value', 'my_other_var': 'other_value'}

    # Create an instance of AnsibleJ2Vars with the mock objects
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __contains__ for a local variable
    assert 'my_local_var' in ansible_j2_vars

    # Test __contains__ for a global variable
    assert 'ansible_version' in ansible_j2_vars

    # Test __contains__ for a variable available in Templar
    templar.available_variables = {'templar_var': 'value'}
    assert 'templar_var' in ansible_j2_vars

    # Test __contains__ for a variable

# Generated at 2024-03-18 04:34:17.829543
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():    templar = MagicMock()

# Generated at 2024-03-18 04:34:23.393931
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():    templar = MockTemplar()

# Generated at 2024-03-18 04:34:28.416658
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from ansible.template import Templar

    # Mock Templar and its available_variables

# Generated at 2024-03-18 04:34:37.393893
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Create an instance of AnsibleJ2Vars with the mock data
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases where the variable should be contained
    assert 'ansible_version' in ansible_j2_vars
    assert 'local_var' in ansible_j2_vars
    assert 'another_local_var' in ansible_j2_vars

    # Test cases where the variable should not be contained
    assert 'non_existent_var' not in ansible_j2_vars
    assert 'missing_var' not in ansible_j2_vars

    # Test with templar's available_variables
    templar

# Generated at 2024-03-18 04:34:53.647568
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:35:00.821159
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Setup the templar and variables
    templar = MockTemplar()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __contains__ for existing local variable
    assert 'local_var' in ansible_j2_vars

    # Test __contains__ for existing global variable
    assert 'ansible_version' in ansible_j2_vars

    # Test __contains__ for non-existing variable
    assert 'non_existent_var' not in ansible_j2_vars

    # Test __contains__ for existing templar variable
    templar.available_variables = {'templar_var': 'templar_value'}

# Generated at 2024-03-18 04:35:04.346686
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = MagicMock()

# Generated at 2024-03-18 04:35:09.867855
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():    templar = MockTemplar()

# Generated at 2024-03-18 04:35:18.843777
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variable data
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.10', 'ansible_playbook_python': '/usr/bin/python'}
    locals_dict = {'local_var': 'value', 'l_prefixed_var': 'prefixed_value'}

    # Create an instance of AnsibleJ2Vars with mock data
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __contains__ for existing local, global, and templar variables
    assert 'local_var' in ansible_j2_vars
    assert 'ansible_version' in ansible_j2_vars
    assert 'ansible_playbook_python' in ansible_j2_vars

    # Test __contains__ for a variable that should be stripped of its 'l_' prefix
    assert 'prefixed_var' in ansible_j2_vars

    # Test __contains__ for a

# Generated at 2024-03-18 04:35:26.414310
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variables
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Create an instance of AnsibleJ2Vars with the mock objects
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __contains__ for a local variable
    assert 'local_var' in ansible_j2_vars

    # Test __contains__ for a global variable
    assert 'ansible_version' in ansible_j2_vars

    # Test __contains__ for a variable available in Templar's available_variables
    templar.available_variables = {'templar_var': 'templar_value'}
    assert 'templar_var' in ansible_j2_vars

    # Test __contains__ for a

# Generated at 2024-03-18 04:35:27.564806
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():import pytest
from ansible.template import Templar


# Generated at 2024-03-18 04:35:28.554958
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():import pytest
from ansible.template import Templar


# Generated at 2024-03-18 04:35:34.726594
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:35:35.871683
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():import pytest
from ansible.template import Templar


# Generated at 2024-03-18 04:35:57.480218
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    # Setup the templar and globals
    templar = MagicMock()
    templar.available_variables = {'a': 1, 'b': 2, 'c': 3}
    globals = {'ansible_version': '2.9', 'other_global': 'value'}

    # Create an instance of AnsibleJ2Vars
    j2_vars = AnsibleJ2Vars(templar, globals)

    # Test __len__ method
    assert len(j2_vars) == 5, "Length of j2_vars should be 5, accounting for 3 templar variables and 2 globals"

# Generated at 2024-03-18 04:36:02.848074
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:36:08.307437
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:36:15.183597
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():    templar = MagicMock()

# Generated at 2024-03-18 04:36:20.042715
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():    templar = MockTemplar()

# Generated at 2024-03-18 04:36:25.137698
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:36:30.166912
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:36:35.249949
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:36:40.687557
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = Templar(loader=None, variables={'var1': 'value1', 'var2': 'value2'})

# Generated at 2024-03-18 04:36:45.137806
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:37:36.964844
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:37:42.894948
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Create a mock Templar object with a set of available variables
    class MockTemplar:
        def __init__(self, variables):
            self.available_variables = variables

    # Define globals and locals for testing
    globals_dict = {'ansible_version': '2.9.10', 'ansible_playbook': 'test_playbook.yml'}
    locals_dict = {'l_my_local_var': 'local_value', 'my_other_var': 'other_value'}

    # Create an instance of AnsibleJ2Vars with the mock Templar, globals, and locals
    templar = MockTemplar({'my_var': 'value', 'ansible_host': 'localhost'})
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'my_var' in ansible_j2_vars, "Expected 'my_var' to be in AnsibleJ2Vars"

# Generated at 2024-03-18 04:37:48.562628
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variable data
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'ansible_playbook_python': '/usr/bin/python'}
    locals_dict = {'l_my_local_var': 'local_value', 'my_other_var': 'other_value'}

    # Create an instance of AnsibleJ2Vars with the mock data
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases for __contains__ method
    assert 'ansible_version' in ansible_j2_vars
    assert 'ansible_playbook_python' in ansible_j2_vars
    assert 'my_local_var' in ansible_j2_vars
    assert 'my_other_var' in ansible_j2_vars
    assert 'non_existent_var' not in ansible_j2_vars
    assert 'l_my_local_var' not in ansible_j2_vars  # '

# Generated at 2024-03-18 04:37:57.019170
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():    templar = MagicMock()

# Generated at 2024-03-18 04:38:04.450622
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Create a mock Templar object with a set of available variables
    class MockTemplar:
        def __init__(self, variables):
            self.available_variables = variables

    # Define globals and locals for testing
    globals_dict = {'ansible_version': '2.9.0', 'ansible_playbook': 'test.yml'}
    locals_dict = {'l_my_local_var': 'local_value', 'my_other_var': 'other_value'}

    # Instantiate the AnsibleJ2Vars class with the mock Templar and variable dictionaries
    ansible_j2_vars = AnsibleJ2Vars(MockTemplar({'my_var': 'value', 'my_other_var': 'override'}), globals_dict, locals_dict)

    # Test cases
    assert 'my_var' in ansible_j2_vars, "Expected 'my_var' to be in ansible_j2_vars"

# Generated at 2024-03-18 04:38:13.432217
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():    templar = MagicMock()

# Generated at 2024-03-18 04:38:21.460664
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Setup the templar and globals
    templar = MockTemplar()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    local_vars = {'local_var1': 'value1', 'local_var2': 'value2'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, local_vars)

    # Test __contains__ for existing local variable
    assert 'local_var1' in ansible_j2_vars

    # Test __contains__ for existing global variable
    assert 'ansible_version' in ansible_j2_vars

    # Test __contains__ for non-existing variable
    assert 'non_existing_var' not in ansible_j2_vars

    # Test __contains__ for existing templar variable
    templar.available_variables = {'templar_var': 'templar_value'}
   

# Generated at 2024-03-18 04:38:28.178516
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:38:33.637394
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variables
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Set available variables in the templar mock
    templar.available_variables = {'templar_var': 'templar_value', 'other_templar_var': 'other_value'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'ansible_version' in ansible_j2_vars
    assert 'local_var' in ansible_j2_vars
    assert 'templar_var' in ansible_j2_vars
    assert 'non_existent_var' not in ansible_j2_vars
    assert 'other_global_var' in ansible

# Generated at 2024-03-18 04:38:40.851287
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    # Mock objects and data for testing
    class MockTemplar:
        def __init__(self, variables):
            self.available_variables = variables

        def template(self, variable):
            if variable == "untemplatable":
                raise AnsibleUndefinedVariable("Cannot template variable")
            return variable.upper()

    globals_dict = {'global_var': 'global_value'}
    locals_dict = {'local_var': 'local_value'}
    templar = MockTemplar({'templated_var': 'templated_value', 'untemplatable': 'untemplatable'})

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __getitem__ for local variable
    assert ansible_j2_vars['local_var'] == 'LOCAL_VALUE', "Local variable templating failed"

    # Test __getitem__ for global variable
    assert ansible_j2_vars

# Generated at 2024-03-18 04:39:32.094386
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:39:37.154506
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:39:45.638648
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    # Mock objects and data for testing
    mock_templar = MagicMock()
    mock_globals = {'global_var': 'global_value'}
    mock_locals = {'local_var': 'local_value', 'l_prefixed_var': 'prefixed_value'}

    # Create an instance of AnsibleJ2Vars with the mock data
    j2_vars = AnsibleJ2Vars(mock_templar, mock_globals, mock_locals)

    # Test retrieval of a global variable
    assert j2_vars['global_var'] == 'global_value'

    # Test retrieval of a local variable
    assert j2_vars['local_var'] == 'local_value'

    # Test retrieval of a local variable with a prefix
    assert j2_vars['prefixed_var'] == 'prefixed_value'

    # Test retrieval of a variable available in templar's available_variables
    mock_templar.available_variables = {'templar_var': 'templar_value'}
   

# Generated at 2024-03-18 04:39:50.034044
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    # Setup the templar and variables
    templar = MagicMock()
    globals_dict = {'global_var': 'value1'}
    locals_dict = {'local_var': 'value2'}

    # Create an instance of AnsibleJ2Vars with the templar and variables
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Mock available variables in the templar
    templar.available_variables = {'available_var': 'value3'}

    # Calculate the expected length
    expected_len = len(set(globals_dict.keys()) | set(locals_dict.keys()) | set(templar.available_variables.keys()))

    # Assert that the length is as expected
    assert ansible_j2_vars.__len__() == expected_len

# Generated at 2024-03-18 04:39:54.882683
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects for Templar and variable data
    templar = Mock()
    globals_dict = {'ansible_version': '2.9.0', 'ansible_playbook': 'test.yml'}
    locals_dict = {'local_var': 'value', 'l_prefixed_var': 'prefixed_value'}

    # Create an instance of AnsibleJ2Vars with the mock data
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test __contains__ for a local variable
    assert 'local_var' in ansible_j2_vars

    # Test __contains__ for a global variable
    assert 'ansible_version' in ansible_j2_vars

    # Test __contains__ for a variable available in Templar
    templar.available_variables = {'templar_var': 'templated_value'}
    assert 'templar_var' in ansible_j2_vars

    # Test __contains__ for a

# Generated at 2024-03-18 04:39:59.822600
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object

# Generated at 2024-03-18 04:40:06.141790
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Create a mock Templar object with a set of available variables
    mock_templar = MagicMock()
    mock_templar.available_variables = {'foo': 'bar', 'baz': 'qux'}

    # Create a set of global variables
    globals_dict = {'ansible_version': '2.9.10', 'inventory_hostname': 'localhost'}

    # Instantiate the AnsibleJ2Vars class with the mock Templar and global variables
    ansible_j2_vars = AnsibleJ2Vars(mock_templar, globals_dict)

    # Test cases where the variable should be contained
    assert 'foo' in ansible_j2_vars
    assert 'baz' in ansible_j2_vars
    assert 'ansible_version' in ansible_j2_vars

    # Test cases where the variable should not be contained
    assert 'nonexistent_var' not in ansible_j2_vars
    assert 'another_missing_var' not in ansible_j2_vars

# Generated at 2024-03-18 04:40:13.029434
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():    templar = MagicMock()

# Generated at 2024-03-18 04:40:17.591132
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = MockTemplar()

# Generated at 2024-03-18 04:40:22.754393
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = MockTemplar()
    globals_dict = {'ansible_version': '2.9.0', 'other_global_var': 'value'}
    locals_dict = {'local_var': 'local_value', 'another_local_var': 'another_value'}

    # Create an instance of AnsibleJ2Vars with the mock data
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases where the variable should be contained
    assert 'ansible_version' in ansible_j2_vars
    assert 'local_var' in ansible_j2_vars
    assert 'another_local_var' in ansible_j2_vars

    # Test cases where the variable should not be contained
    assert 'non_existent_var' not in ansible_j2_vars
    assert 'missing_var' not in ansible_j2_vars

    # Test cases with templar's available variables

# Generated at 2024-03-18 04:42:03.646684
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    # Mock objects and data for testing
    class MockTemplar:
        def __init__(self, variables):
            self.available_variables = variables

        def template(self, variable):
            if variable == 'undefined':
                raise AnsibleUndefinedVariable('undefined variable')
            return variable

    globals_dict = {'global_var': 'global_value'}
    locals_dict = {'local_var': 'local_value'}
    templar = MockTemplar({'templated_var': 'templated_value', 'undefined': 'undefined'})

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test retrieving a global variable
    assert ansible_j2_vars['global_var'] == 'global_value', "Failed to get global variable"

    # Test retrieving a local variable

# Generated at 2024-03-18 04:42:08.544118
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = Templar(loader=None, variables={'var1': 'value1', 'var2': 'value2'})

# Generated at 2024-03-18 04:42:14.146760
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = Templar(loader=None, variables={'var1': 'value1', 'var2': 'value2'})

# Generated at 2024-03-18 04:42:23.460525
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():    # Mock objects and data for testing
    templar = MockTemplar(variables={'var1': 'value1', 'var2': 'value2'})
    globals_dict = {'global1': 'gvalue1', 'range': range}
    locals_dict = {'l_var3': 'value3', 'var4': 'value4'}

    # Create an instance of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # Test cases
    assert 'var1' in ansible_j2_vars, "Expected 'var1' to be in ansible_j2_vars"
    assert 'var2' in ansible_j2_vars, "Expected 'var2' to be in ansible_j2_vars"
    assert 'var3' in ansible_j2_vars, "Expected 'var3' to be in ansible_j2_vars"

# Generated at 2024-03-18 04:42:29.895240
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():    templar = MockTemplar()

# Generated at 2024-03-18 04:42:36.436276
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():    from unittest.mock import MagicMock

    # Create a mock Templar object