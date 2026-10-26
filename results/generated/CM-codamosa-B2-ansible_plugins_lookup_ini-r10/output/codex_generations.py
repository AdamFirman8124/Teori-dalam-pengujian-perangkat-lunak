

# Generated at 2026-10-25 06:26:07.204325
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:22.061973
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 06:26:24.478484
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:26.895413
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:29.311639
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:31.728574
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:34.145508
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:36.561309
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:38.977941
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:41.390792
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:43.846483
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:26:46.261929
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:26:48.675620
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:26:51.089909
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:26:53.508192
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:55.922924
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:58.337340
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:00.749731
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:03.164455
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:05.576893
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:07.994204
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:10.407952
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:12.821537
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:15.235789
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:17.667472
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:20.077332
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:22.491237
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:24.997972
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:27.348274
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:29.762782
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:32.179496
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:34.590168
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:37.008227
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:39.421982
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:41.838530
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:27:44.251728
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:16.946296
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

# Generated at 2026-10-25 06:28:33.532233
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

# Generated at 2026-10-25 06:28:47.470148
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:49.887120
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:52.301418
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:54.715838
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:28:57.130305
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:28:59.570137
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:01.983468
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:04.398016
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:06.812330
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:09.226094
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:11.640915
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:14.054791
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:16.467958
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:18.884934
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:21.299377
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:29:23.717731
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:26.293901
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:18.698963
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

# Generated at 2026-10-25 06:30:35.187539
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

# Generated at 2026-10-25 06:30:37.607400
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:40.307734
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:42.969344
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:45.385361
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:47.801681
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:50.215832
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:30:52.807125
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:55.296828
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:57.692532
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:00.115992
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:02.513959
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:04.930668
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:07.347610
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:09.763926
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:12.182244
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:14.601252
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:17.017296
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:19.455788
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:21.849569
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:24.270273
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:26.683538
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:29.113385
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:31.527889
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:49.220506
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

# Generated at 2026-10-25 06:31:50.596524
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:52.024750
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 06:31:53.375058
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:31:54.859757
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-25 06:31:57.512193
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:31:59.931787
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:02.345835
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:04.758144
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:07.177021
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:09.596893
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:12.301354
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:14.720489
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:17.139301
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:19.555615
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:21.971312
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:24.387909
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:26.832565
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:29.221127
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:31.638727
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:32:34.053214
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:36.470384
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:38.883570
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:41.430413
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:32:59.072000
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

# Generated at 2026-10-25 06:33:01.488364
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:03.904164
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:06.667968
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:09.085322
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:11.500514
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:13.916887
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:16.328758
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:18.747555
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:21.185434
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:23.579916
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:25.996596
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:28.410473
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:30.831247
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:33.245496
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:35.661674
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:33:38.087303
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:40.505406
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:42.919483
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:45.336754
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:47.750975
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:50.168670
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:52.983688
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:55.398894
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:33:57.814548
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:00.230546
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:02.644343
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:05.063112
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:07.480268
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:09.894529
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:12.313676
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:14.731159
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:34:17.145519
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:34:19.561669
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:34:21.978771
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:24.396750
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:26.815501
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:29.228687
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:31.641171
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:34.059787
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:36.477306
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:38.892091
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:41.311123
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:34:43.727187
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:34:46.143367
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:04.085149
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:06.595698
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:35:08.993853
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:35:11.415623
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:35:13.850732
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:16.260314
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:18.671805
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:23.862694
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:26.277295
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:28.666902
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:31.082332
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:33.498894
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:35.913891
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:38.330118
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:40.746843
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:43.162536
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:35:45.577051
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:35:47.991128
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:35:50.404963
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:36:12.082784
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-25 06:36:13.495752
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser