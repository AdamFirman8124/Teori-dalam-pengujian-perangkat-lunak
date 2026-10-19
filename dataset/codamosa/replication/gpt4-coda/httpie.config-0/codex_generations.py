

# Generated at 2024-03-18 05:43:48.911840
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:43:57.138200
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    from unittest.mock import patch, MagicMock

    with patch('os.environ.get') as mock_env_get, \
         patch('os.path.exists') as mock_path_exists, \
         patch('httpie.compat.is_windows', new_callable=MagicMock) as mock_is_windows:

        # Test 1: Environment variable HTTPIE_CONFIG_DIR is set
        mock_env_get.return_value = '/custom/config/dir'
        assert get_default_config_dir() == Path('/custom/config/dir')

        # Test 2: On Windows
        mock_env_get.return_value = None
        mock_is_windows.return_value = True
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # Test 3: Legacy ~/.httpie exists
        mock_is_windows.return_value = False
        mock_path_exists.return_value = True
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEG

# Generated at 2024-03-18 05:44:03.316710
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:44:14.466440
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test 2: No environment variables, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Mock environment variables for XDG_CONFIG_HOME and HTTPIE_CONFIG_DIR

# Generated at 2024-03-18 05:44:21.172030
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:44:22.727799
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:44:23.549920
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():import pytest
import tempfile
import json


# Generated at 2024-03-18 05:44:28.903554
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for testing
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                expected = Path(os.path.expandvars('%APPDATA%')) / 'httpie'
               

# Generated at 2024-03-18 05:44:29.920598
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:44:31.408128
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:44:37.170571
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:44:45.799585
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    from unittest.mock import patch, MagicMock

    with patch('os.environ.get') as mock_env_get, \
         patch('os.path.exists') as mock_path_exists, \
         patch('httpie.compat.is_windows', new_callable=MagicMock) as mock_is_windows:

        # Test 1: Environment variable HTTPIE_CONFIG_DIR is set
        mock_env_get.return_value = '/custom/config/dir'
        assert get_default_config_dir() == Path('/custom/config/dir')

        # Test 2: On Windows
        mock_env_get.return_value = None
        mock_is_windows.return_value = True
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # Test 3: Legacy ~/.httpie exists
        mock_is_windows.return_value = False
        mock_path_exists.return_value = True
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEG

# Generated at 2024-03-18 05:44:51.425032
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:45:00.844241
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:45:06.050688
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:45:13.656317
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    from unittest.mock import patch, MagicMock

    with patch('os.environ.get') as mock_env_get, \
         patch('os.path.exists') as mock_path_exists, \
         patch('httpie.compat.is_windows', new_callable=MagicMock) as mock_is_windows:

        # Test 1: Environment variable HTTPIE_CONFIG_DIR is set
        mock_env_get.return_value = '/custom/config/dir'
        assert get_default_config_dir() == Path('/custom/config/dir')

        # Test 2: On Windows
        mock_env_get.return_value = None
        mock_is_windows.return_value = True
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # Test 3: Legacy ~/.httpie exists
        mock_is_windows.return_value = False
        mock_path_exists.return_value = True
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEG

# Generated at 2024-03-18 05:45:20.626041
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:45:26.624450
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    from unittest.mock import patch, MagicMock

    with patch('os.environ.get') as mock_env_get, \
         patch('os.path.exists') as mock_path_exists, \
         patch('httpie.compat.is_windows', new=False):

        # Test 1: Environment variable HTTPIE_CONFIG_DIR is set
        mock_env_get.side_effect = lambda key, default=None: {
            ENV_HTTPIE_CONFIG_DIR: '/custom/config/dir',
            ENV_XDG_CONFIG_HOME: None
        }.get(key, default)
        assert get_default_config_dir() == Path('/custom/config/dir')

        # Reset mocks for next test
        mock_env_get.reset_mock()
        mock_path_exists.reset_mock()

        # Test 2: Windows environment
        with patch('httpie.compat.is_windows', new=True):
            assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # Test 3

# Generated at 2024-03-18 05:45:28.440905
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:45:35.803169
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    import tempfile

# Generated at 2024-03-18 05:45:44.909454
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:45:45.835534
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:45:52.460201
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file existence
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            # Test case: No environment variables set, not Windows, no legacy dir
            mock_exists.return_value = False
            is_windows = False
            expected = Path.home() / '.config' / 'httpie'
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, Windows
            is_windows = True
            expected = DEFAULT_WINDOWS_CONFIG_DIR
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, not Windows, legacy dir exists
            mock_exists.return_value = True
            is_windows = False
            expected = Path.home() / '.httpie'
            assert get_default_config_dir() == expected

            # Test case: HTTPIE_CONFIG_DIR is set

# Generated at 2024-03-18 05:45:55.004048
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:46:06.337671
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file existence
    with unittest.mock.patch.dict(os.environ, {}, clear=True):
        with unittest.mock.patch.object(Path, 'exists', return_value=False):
            # Test without any environment variables or legacy config
            assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    # Mock environment variable for HTTPIE_CONFIG_DIR
    custom_config_dir = '/custom/config/dir'
    with unittest.mock.patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: custom_config_dir}):
        assert get_default_config_dir() == Path(custom_config_dir)

    # Mock environment variable for XDG_CONFIG_HOME
    xdg_config_home = '/xdg/config/home'

# Generated at 2024-03-18 05:46:14.843534
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:46:21.165187
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    from unittest.mock import patch, MagicMock

    with patch('os.environ.get') as mock_env_get, \
         patch('os.path.exists') as mock_path_exists, \
         patch('httpie.compat.is_windows', new_callable=MagicMock) as mock_is_windows:

        # Test 1: Environment variable HTTPIE_CONFIG_DIR is set
        mock_env_get.return_value = '/custom/config/dir'
        assert get_default_config_dir() == Path('/custom/config/dir')

        # Test 2: On Windows
        mock_env_get.return_value = None
        mock_is_windows.return_value = True
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # Test 3: Legacy ~/.httpie exists
        mock_is_windows.return_value = False
        mock_path_exists.return_value = True
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEG

# Generated at 2024-03-18 05:46:29.787466
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:46:35.502286
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file existence
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            # Test case: No environment variables set, not Windows, no legacy dir
            mock_exists.return_value = False
            is_windows = False
            expected = Path.home() / '.config' / 'httpie'
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, Windows
            is_windows = True
            expected = DEFAULT_WINDOWS_CONFIG_DIR
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, not Windows, legacy dir exists
            mock_exists.return_value = True
            is_windows = False
            expected = Path.home() / '.httpie'
            assert get_default_config_dir() == expected

            # Test case: HTTPIE_CONFIG_DIR is set

# Generated at 2024-03-18 05:46:36.898687
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:46:53.060996
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test case: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
                assert get_default_config_dir() == expected

                # Test case: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test case: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default

# Generated at 2024-03-18 05:46:58.269226
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:46:59.845467
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:47:08.553198
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:47:13.567133
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:47:14.908410
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:47:19.139808
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    import pytest

# Generated at 2024-03-18 05:47:24.516515
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test 2: No environment variables, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

            # Test 4: HTTPIE_CONFIG_DIR environment variable set

# Generated at 2024-03-18 05:47:29.912936
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    import pytest

# Generated at 2024-03-18 05:47:31.031945
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:47:52.139699
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    import pytest

# Generated at 2024-03-18 05:47:53.936401
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:47:55.008887
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:47:56.376335
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:48:03.238906
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:48:04.714640
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:48:05.999705
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:48:06.941717
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:48:14.027991
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with mock.patch.dict(os.environ, {}, clear=True):
        with mock.patch('os.path.exists') as mock_exists:
            with mock.patch('httpie.compat.is_windows', new=False):

                # Test case: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test case: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with mock.patch('httpie.compat.is_windows', new=True):
                # Test case: No environment variables set, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case: HTTPIE_CONFIG_DIR environment variable is set

# Generated at 2024-03-18 05:48:19.992711
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for testing
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR

# Generated at 2024-03-18 05:48:59.249101
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Setup environment for the test
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_home = Path.home()


# Generated at 2024-03-18 05:49:07.477212
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with unittest.mock.patch.dict(os.environ, {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', new=False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', new=True):
                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected

   

# Generated at 2024-03-18 05:49:15.227340
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test case: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test case: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test case: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected

    # Test case: HT

# Generated at 2024-03-18 05:49:21.604745
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test case: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
                assert get_default_config_dir() == expected

                # Test case: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):
                # Test case: No environment variables set, Windows OS
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get

# Generated at 2024-03-18 05:49:27.290797
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with unittest.mock.patch.dict(os.environ, {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', new=False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', new=True):
                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected

           

# Generated at 2024-03-18 05:49:28.309391
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:49:29.243495
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:49:36.351998
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:49:37.279316
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:49:38.773276
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:50:44.657938
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected



# Generated at 2024-03-18 05:50:49.392986
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with unittest.mock.patch.dict(os.environ, {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

            # Test 4: HTTPIE_CONFIG_DIR environment variable is set
           

# Generated at 2024-03-18 05:50:50.655144
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:50:57.749754
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):
                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
               

# Generated at 2024-03-18 05:51:02.591500
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:51:03.419991
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:51:08.215880
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:51:09.386420
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():import pytest
import tempfile
import json


# Generated at 2024-03-18 05:51:18.091430
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    import pytest

# Generated at 2024-03-18 05:51:23.248406
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected

            # Test

# Generated at 2024-03-18 05:52:30.746906
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file existence
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            # Test case: No environment variables set, not Windows, no legacy dir
            mock_exists.return_value = False
            is_windows = False
            expected = Path.home() / '.config' / 'httpie'
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, not Windows, legacy dir exists
            mock_exists.return_value = True
            expected = Path.home() / '.httpie'
            assert get_default_config_dir() == expected

            # Test case: No environment variables set, is Windows
            is_windows = True
            expected = DEFAULT_WINDOWS_CONFIG_DIR
            assert get_default_config_dir() == expected

            # Test case: HTTPIE_CONFIG_DIR environment variable is set

# Generated at 2024-03-18 05:52:37.722772
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test 2: No environment variables, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with unittest.mock.patch('httpie.compat.is_windows', True):
                # Test 3: No environment variables, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

            # Test 4: HTTPIE_CONFIG_DIR environment variable set

# Generated at 2024-03-18 05:52:39.128401
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:52:46.341161
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system status
    with unittest.mock.patch.dict(os.environ, {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test case: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

                # Test case: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                assert get_default_config_dir() == Path.home() / '.httpie'

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test case: No environment variables set, Windows
                assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case: HTTPIE_CONFIG_DIR environment variable is set

# Generated at 2024-03-18 05:52:47.720394
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():import json
import pytest
from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:52:55.955171
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Mock environment variables and file system for the test
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('os.path.exists') as mock_exists:
            with unittest.mock.patch('httpie.compat.is_windows', False):

                # Test 1: No environment variables set, not Windows, no legacy dir
                mock_exists.return_value = False
                expected = Path.home() / '.config' / 'httpie'
                assert get_default_config_dir() == expected

                # Test 2: No environment variables set, not Windows, legacy dir exists
                mock_exists.return_value = True
                expected = Path.home() / '.httpie'
                assert get_default_config_dir() == expected

            with unittest.mock.patch('httpie.compat.is_windows', True):

                # Test 3: No environment variables set, Windows
                expected = DEFAULT_WINDOWS_CONFIG_DIR
                assert get_default_config_dir() == expected



# Generated at 2024-03-18 05:52:56.849291
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from pathlib import Path


# Generated at 2024-03-18 05:52:58.043164
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():import pytest
import tempfile
from pathlib import Path


# Generated at 2024-03-18 05:52:59.335569
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():import pytest
import tempfile
from unittest.mock import mock_open, patch


# Generated at 2024-03-18 05:53:04.755981
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    import pytest