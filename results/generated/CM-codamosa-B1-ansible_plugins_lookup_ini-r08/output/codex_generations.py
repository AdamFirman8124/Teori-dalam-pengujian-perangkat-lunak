

# Generated at 2026-10-25 08:32:22.421391
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:24.855429
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:27.276715
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:29.695026
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:32.110101
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:34.528151
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:36.944232
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:32:39.366474
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:32:41.782469
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:32:44.411406
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:45.838180
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:32:47.169532
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:52.901671
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:32:54.334552
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:55.973252
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:32:57.510524
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:32:59.044768
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:00.621190
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:02.322596
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:03.857524
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:05.396252
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:06.933319
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:08.364964
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:09.798383
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:11.410426
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:12.884422
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:14.381981
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:17.375370
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:20.032453
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:22.727709
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:25.158888
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:27.570253
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:30.150427
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:32.585389
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:35.000529
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:37.414455
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:39.835736
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:33:42.252112
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:33:44.671147
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:33:46.079136
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:47.483098
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:48.879020
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:50.249270
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:33:51.614009
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:53.032668
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:54.386967
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:55.881035
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:33:57.415810
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:33:59.009520
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:34:00.610314
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:34:01.945368
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:03.455483
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:34:06.102030
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:08.681639
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:11.228828
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:13.788427
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:16.195161
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:18.612167
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:21.192925
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:23.613662
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:26.030213
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:28.450055
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:30.867054
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:33.286322
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:35.701928
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:38.118856
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:40.536193
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:42.954984
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:45.374068
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:47.794527
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:50.210209
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:52.629700
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:55.048967
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:34:57.464524
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:34:59.883981
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:02.303091
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:04.720223
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:07.138980
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:09.555018
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:11.145159
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:35:12.669795
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:35:14.204138
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:15.615260
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:35:17.033924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:35:18.469121
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:19.952337
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:35:21.456361
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:35:22.793376
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:35:24.124766
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:25.515214
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:35:28.145569
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:30.580835
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:32.996059
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:35.609921
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:38.030798
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:40.520079
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:43.956087
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:46.373084
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:48.789821
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:35:51.314159
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:53.672206
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:56.088548
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:35:58.506092
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:00.921774
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:03.338781
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:05.757491
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:08.173654
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:10.593343
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:13.010539
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:15.431410
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:17.845245
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:20.264156
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:22.679453
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:25.096144
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:27.516348
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:29.993926
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:32.407908
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:34.825695
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:37.244380
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:39.660782
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:42.077801
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:44.553297
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:46.967860
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:36:49.382250
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:51.805237
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:54.217698
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:36:58.278328
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:36:59.958550
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:04.648825
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:06.138077
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:07.544779
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:08.993254
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:10.359285
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:11.812589
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:37:13.122046
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup.ini import LookupModule


INI_CONTENT = """[section1]
key1 = value1
key2 = value2

[section2]
user = bob
"""


def _make_lookup(tmp_path, file_content=INI_CONTENT, filename="test.ini", overrides=None):
    ini_file = tmp_path / filename
    ini_file.write_text(file_content)

    lm = LookupModule()

    def _opts():
        opts = {
            'type': 'ini',
            'file': str(ini_file),
            'section': 'section1',
            're': False,
            'encoding': 'utf-8',
            'default': '',
            'case_sensitive': False,
            'allow_no_value': False,
        }
        opts.update(overrides or {})
        return opts

    lm.set_options = MagicMock()
    lm.get_options = MagicMock(side_effect=_opts)
    lm.find_file_in_search_path = MagicMock(return_value=str(ini_file))
    lm._loader = MagicMock()
    lm._loader._get_file_contents.return_value = (file_content.encode('utf-8'), False)
    return lm


def test_run_simple_key(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['key1']) == ['value1']


def test_run_regexp(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'re': True})
    assert sorted(lm.run(['key.*'])) == ['value1', 'value2']


def test_run_missing_key_returns_default(tmp_path):
    lm = _make_lookup(tmp_path)
    assert lm.run(['nonexistent']) == ['']


def test_run_missing_section_raises(tmp_path):
    lm = _make_lookup(tmp_path, overrides={'section': 'nope'})
    with pytest.raises(AnsibleLookupError):
        lm.run(['key1'])


def test_run_properties_type(tmp_path):
    props = "user.name = bob\n"
    lm = _make_lookup(tmp_path, file_content=props, filename="user.properties",
                      overrides={'type': 'properties', 'section': 'java_properties'})
    assert lm.run(['user.name']) == ['bob']

# Generated at 2026-10-25 08:37:15.666786
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:18.081546
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:20.625293
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:23.043516
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:25.570300
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:27.989203
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:36.232422
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:38.646825
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:41.062474
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:43.480902
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:45.896191
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:48.312184
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:37:50.727715
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:53.143682
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:55.559802
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:37:57.980184
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:00.390083
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:02.804871
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:05.221017
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:07.636225
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:10.054728
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:12.467143
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:14.900551
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:17.318945
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:19.737569
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:22.153910
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:24.573128
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:26.989980
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:29.408307
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:31.827301
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:34.242733
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:36.660443
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:39.074408
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:38:41.492322
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:44.035875
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:38:46.345484
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:01.593590
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:04.009252
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:06.425007
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:08.841750
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:11.269771
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:13.685387
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:16.103151
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:18.522623
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:20.939135
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:23.354759
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:25.771845
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:28.188381
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:30.762514
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:33.061039
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:35.475916
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:37.891745
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:39:40.310097
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:39:42.729876
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:39:45.145364
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:47.594909
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:49.978322
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:52.394821
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:39:55.019008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    import pytest

    from ansible.errors import AnsibleLookupError
    from ansible.plugins.lookup.ini import LookupModule

    class FakeLoader:
        def _get_file_contents(self, path):
            with open(path, 'rb') as f:
                return f.read(), False

    fd, ini_path = tempfile.mkstemp(suffix='.ini')
    os.close(fd)
    with open(ini_path, 'w') as f:
        f.write('[integration]\nuser = alice\nhost = db01\n\n[production]\nuser = bob\n')

    fd2, props_path = tempfile.mkstemp(suffix='.properties')
    os.close(fd2)
    with open(props_path, 'w') as f:
        f.write('user.name = carol\nuser.id = 42\n')

    def make_lookup(options):
        lookup = LookupModule()
        lookup._loader = FakeLoader()
        lookup.set_options = lambda var_options=None, direct=None: None
        lookup.get_options = lambda: options
        lookup._deprecate_inline_kv = lambda: None
        lookup.find_file_in_search_path = lambda variables, kind, fname: fname
        return lookup

    base_options = {
        'file': ini_path,
        'section': 'integration',
        'type': 'ini',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }

    # simple key lookup in a named section
    lookup = make_lookup(dict(base_options))
    assert lookup.run(['user']) == ['alice']

    # missing key falls back to default
    lookup = make_lookup(dict(base_options))
    assert lookup.run(['nonexistent']) == ['']

    # regexp lookup returns all matching values in the section
    regex_options = dict(base_options, re=True)
    lookup = make_lookup(regex_options)
    assert lookup.run(['.*']) == ['alice', 'db01']

    # section switch
    prod_options = dict(base_options, section='production')
    lookup = make_lookup(prod_options)
    assert lookup.run(['user']) == ['bob']

    # java properties type: synthetic [java_properties] section is used
    props_options = {
        'file': props_path,
        'section': 'global',
        'type': 'properties',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
    }
    lookup = make_lookup(props_options)
    assert lookup.run(['user.name']) == ['carol']

    # missing section raises AnsibleLookupError
    lookup = make_lookup(dict(base_options, section='does_not_exist'))
    with pytest.raises(AnsibleLookupError):
        lookup.run(['user'])

    os.unlink(ini_path)
    os.unlink(props_path)

# Generated at 2026-10-25 08:39:56.531447
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:39:57.965140
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:40:01.652500
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:40:03.188534
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 08:40:32.339793
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:34.757500
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:37.178517
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:39.592275
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:42.048864
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:44.460219
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:46.874889
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:49.292867
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:51.709423
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:40:54.125543
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:40:56.541531
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:40:58.958491
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:41:01.374726
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:41:03.790646
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:41:06.208322
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 08:41:08.623850
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:11.038927
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:13.457783
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:15.874293
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:18.290749
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:20.735779
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:23.146859
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:25.562835
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:27.979335
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:30.394161
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:32.811640
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:35.230013
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:37.644660
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:40.059435
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 08:41:42.478045
# Unit test for method run of class LookupModule