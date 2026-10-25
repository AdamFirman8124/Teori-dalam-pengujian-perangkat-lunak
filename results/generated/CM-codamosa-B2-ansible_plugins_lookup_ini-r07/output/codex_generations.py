

# Generated at 2026-10-25 01:08:39.679015
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:08:46.240640
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:09:08.668065
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

# Generated at 2026-10-25 01:09:11.083895
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:13.498201
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:15.911856
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:18.325998
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:20.741183
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:23.161343
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:25.576309
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:36.437912
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:09:43.895398
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()


# Generated at 2026-10-25 01:09:45.434740
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:09:50.856000
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:09:52.182963
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

# Generated at 2026-10-25 01:09:53.530767
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

# Generated at 2026-10-25 01:09:54.855527
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:09:57.276802
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:09:59.787991
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:10:02.203310
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:04.755813
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:07.170823
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:09.584811
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:11.999547
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:14.416154
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:16.832869
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:10:19.245613
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:10:21.667329
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:10:24.082254
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:26.500376
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:28.915054
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:31.340744
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:33.759455
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:10:45.332062
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-25 01:10:46.774690
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

# Generated at 2026-10-25 01:10:48.141221
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

# Generated at 2026-10-25 01:10:49.523130
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

# Generated at 2026-10-25 01:10:50.846332
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

# Generated at 2026-10-25 01:10:52.173713
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:10:57.227230
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:10:58.545767
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

# Generated at 2026-10-25 01:10:59.867196
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:06.428511
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:11:07.861831
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

# Generated at 2026-10-25 01:11:09.180408
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:13.492591
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:11:14.875548
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:20.483228
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:11:22.909007
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:25.448555
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:27.977644
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:30.393814
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:11:32.810302
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:11:35.224036
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:11:37.638291
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:11:40.053123
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:11:48.205662
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-25 01:11:49.638775
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:11:55.152209
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:11:56.490703
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:01.795823
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:12:03.258703
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:09.579600
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-25 01:12:15.240375
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-25 01:12:16.673277
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:19.092069
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:21.614127
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:24.030200
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:26.446265
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:29.048903
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:31.464427
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:33.879559
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:36.294764
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:38.708589
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:41.129081
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:43.547422
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:45.966055
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:48.379659
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:50.792901
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:12:53.279992
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:55.695200
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:12:58.110223
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:13:00.524231
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:02.939346
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:05.354835
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:07.771338
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:13:17.499850
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-25 01:13:18.836006
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

# Generated at 2026-10-25 01:13:20.471186
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

# Generated at 2026-10-25 01:13:21.804607
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:31.942007
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-25 01:13:37.569536
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:13:38.892743
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:45.257665
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:13:46.595874
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

# Generated at 2026-10-25 01:13:49.147787
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:13:51.661373
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:13:54.077563
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:13:56.497940
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:13:58.919526
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:01.329859
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:05.282008
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:07.699484
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:10.120203
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:11.449251
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

# Generated at 2026-10-25 01:14:12.843543
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:21.600525
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:14:22.929593
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

# Generated at 2026-10-25 01:14:24.258512
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:29.490924
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:14:30.814463
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:35.834941
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = object.__new__(LookupModule)

# Generated at 2026-10-25 01:14:42.667043
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():parser = configparser.ConfigParser()

# Generated at 2026-10-25 01:14:45.190196
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:47.604204
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:50.021600
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:52.435585
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:54.850396
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:57.430663
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:14:59.845745
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:15:02.259597
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:15:04.674148
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:15:07.282905
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:09.700488
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:12.115122
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:15.399760
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:17.813955
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:20.229274
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:22.655853
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:25.061463
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:27.477009
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:29.893327
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:32.308053
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:34.723151
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:37.137658
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:39.553017
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:41.968469
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:44.383813
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:46.798512
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:49.215332
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:51.640519
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:54.056280
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:56.476705
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:58.891772
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:01.311406
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:03.723439
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:06.138024
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:08.554186
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:10.969782
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:13.384639
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:15.799161
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:18.214292
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:20.630039
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:23.045239
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:25.461188
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:30.425295
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:32.840720
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:35.256548
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:37.671537
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:40.086560
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:42.499401
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:44.914273
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:47.329598
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:49.744134
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:16:52.162035
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:54.573513
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:56.988905
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:59.403597
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:01.817714
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:04.232271
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:06.647395
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:09.064224
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:11.480621
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:13.899116
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:23.874941
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:35.447655
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:36.879648
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:17:43.227395
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule()

# Generated at 2026-10-25 01:17:44.560146
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:17:47.096897
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:17:49.750901
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:17:52.168628
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:54.683281
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:57.100217
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:06.101455
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:08.518726
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:10.933204
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:13.348468
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:18:15.948732
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:18:23.018061
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():parser = configparser.ConfigParser()

# Generated at 2026-10-25 01:18:24.345831
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 01:18:32.893928
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():from ansible.module_utils.six.moves import configparser
