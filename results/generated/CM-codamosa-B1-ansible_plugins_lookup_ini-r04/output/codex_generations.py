

# Generated at 2026-10-25 12:02:50.751648
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 12:02:53.161888
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 12:02:55.577157
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 12:03:16.127492
# Unit test for constructor of class LookupModule
def test_LookupModule():
    """Constructor smoke test: no args, no loader."""
    lookup = LookupModule()
    assert lookup is not None
    assert lookup._loader is None


def test_LookupModule_via_loader():
    """Plugin resolves through the lookup loader."""
    lookup = lookup_loader.get('ini')
    assert isinstance(lookup, LookupModule)


def test_parse_params_preserves_spaces():
    paramvals = {'_terms': None, 'file': None, 'section': None}
    assert _parse_params('user file=/tmp/a.ini section=my section', paramvals) == [
        'user', 'file=/tmp/a.ini', 'section=my section'
    ]


def test_run_reads_value(tmp_path):
    """End-to-end: read one key out of a real ini file."""
    ini = tmp_path / 'users.ini'
    ini.write_text(u'[integration]\nuser = john\n')

    lookup = LookupModule(loader=DataLoader())
    result = lookup.run(['user'], variables={}, file=str(ini), section='integration')
    assert result == ['john']


def test_run_missing_key_returns_default(tmp_path):
    ini = tmp_path / 'users.ini'
    ini.write_text(u'[integration]\nuser = john\n')

    lookup = LookupModule(loader=DataLoader())
    result = lookup.run(['nope'], variables={}, file=str(ini),
                        section='integration', default='fallback')
    assert result == ['fallback']

# Generated at 2026-10-25 12:03:17.664600
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

# Generated at 2026-10-25 12:04:05.361863
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 12:05:27.478939
# Unit test for constructor of class LookupModule
def test_LookupModule():lookup = LookupModule()

# Generated at 2026-10-25 12:07:04.481033
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 12:07:06.027799
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 12:07:48.431815
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:08:22.725390
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:08:57.836939
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:09:00.893394
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:09:07.156440
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 12:09:09.000154
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 12:09:12.787995
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:09:15.759338
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:09:19.142021
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 12:09:20.666595
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 12:09:38.801279
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:09:44.330003
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:09:48.935815
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 12:09:50.471613
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 12:09:53.645877
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:09:56.721637
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:10:14.756741
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:10:27.131735
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:10:51.665119
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 12:11:01.640933
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 12:11:37.173347
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:11:45.774770
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:11:50.178216
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:11:57.961075
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:12:20.080005
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 12:12:30.444763
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:12:55.407667
# Unit test for method get_value of class LookupModule