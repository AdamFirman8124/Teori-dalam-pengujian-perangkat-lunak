# file: project/ansible/plugins/lookup/ini.py:136-204
# asked: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}
# gained: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}

import pytest
from unittest.mock import MagicMock


def _base_paramvals(**overrides):
    vals = {
        'allow_no_value': True,
        'case_sensitive': False,
        'file': 'fake.ini',
        'type': 'ini',
        'section': 'mysection',
        'default': None,
        're': False,
        'encoding': 'utf-8',
    }
    vals.update(overrides)
    return vals


def _make_lookup(monkeypatch, paramvals, contents_bytes):
    from ansible.module_utils.six.moves import configparser as cp_mod
    if not hasattr(cp_mod.ConfigParser, 'readfp'):
        monkeypatch.setattr(cp_mod.ConfigParser, 'readfp', cp_mod.ConfigParser.read_file, raising=False)
    from ansible.plugins.lookup.ini import LookupModule
    lu = LookupModule(loader=None, templar=None)
    monkeypatch.setattr(lu, 'set_options', lambda *a, **k: None)
    monkeypatch.setattr(lu, 'get_options', lambda *a, **k: paramvals)
    monkeypatch.setattr(lu, '_deprecate_inline_kv', lambda *a, **k: None)
    monkeypatch.setattr(lu, 'find_file_in_search_path', lambda *a, **k: '/fake/path.ini')

    class FakeLoader:
        def _get_file_contents(self, path):
            assert path == '/fake/path.ini'
            return (contents_bytes, True)

    lu._loader = FakeLoader()
    return lu


def test_plain_lookup(monkeypatch):
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['mykey'], variables={})
    assert ret == ['myvalue']


def test_case_sensitive_false_folds(monkeypatch):
    paramvals = _base_paramvals(case_sensitive=False)
    contents = b"[mysection]\nMyKey = upper\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['mykey'], variables={})
    assert ret == ['upper']


def test_case_sensitive_true(monkeypatch):
    paramvals = _base_paramvals(case_sensitive=True)
    contents = b"[mysection]\nMyKey = upper\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['MyKey'], variables={})
    assert ret == ['upper']
    paramvals2 = _base_paramvals(case_sensitive=True)
    lu2 = _make_lookup(monkeypatch, paramvals2, contents)
    ret2 = lu2.run(['mykey'], variables={})
    assert ret2 == []


def test_properties_type(monkeypatch):
    paramvals = _base_paramvals(type='properties')
    contents = b"myprop = myval\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['myprop'], variables={})
    assert ret == ['myval']
    assert paramvals['section'] == 'java_properties'


def test_regex_expands_mutablesequence(monkeypatch):
    paramvals = _base_paramvals(re=True)
    contents = b"[mysection]\nfoo_one = 1\nfoo_two = 2\nother = 3\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['foo_.*'], variables={})
    assert sorted(ret) == ['1', '2']


def test_default_fallback_when_missing(monkeypatch):
    paramvals = _base_paramvals(default='fallback')
    contents = b"[mysection]\nother = 1\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['missing'], variables={})
    assert ret == ['fallback']


def test_none_var_returns_empty(monkeypatch):
    paramvals = _base_paramvals(default=None)
    contents = b"[mysection]\nother = 1\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['missing'], variables={})
    assert ret == []


def test_inline_kv_success(monkeypatch):
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['mykey section=mysection'], variables={})
    assert ret == ['myvalue']
    assert paramvals['section'] == 'mysection'


def test_inline_space_key(monkeypatch):
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmy key = spaced\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['my key'], variables={})
    assert ret == ['spaced']


def test_inline_second_bare_ignored_branch(monkeypatch):
    import ansible.plugins.lookup.ini as ini_mod
    paramvals = _base_paramvals()
    contents = b"[mysection]\nkey1 = val1\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pv: ['key1', 'key2'])
    ret = lu.run(['dummy term'], variables={})
    assert ret == ['val1']


def test_inline_invalid_option(monkeypatch):
    from ansible.errors import AnsibleLookupError
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    with pytest.raises(AnsibleLookupError, match='not a valid option'):
        lu.run(['mykey badname=value'], variables={})


def test_inline_value_error(monkeypatch):
    from ansible.errors import AnsibleLookupError
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    with pytest.raises(AnsibleLookupError, match='Could not use'):
        lu.run(['mykey section=a=b'], variables={})


def test_inline_no_key_error(monkeypatch):
    from ansible.errors import AnsibleOptionsError
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    with pytest.raises(AnsibleOptionsError, match='No key to lookup'):
        lu.run(['section=mysection'], variables={})


def test_duplicate_option_error(monkeypatch):
    from ansible.errors import AnsibleLookupError
    paramvals = _base_paramvals()
    contents = b"[mysection]\nmykey = val1\nmykey = val2\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    with pytest.raises(AnsibleLookupError, match='Duplicate option'):
        lu.run(['mykey'], variables={})


def test_no_section_error(monkeypatch):
    from ansible.errors import AnsibleLookupError
    paramvals = _base_paramvals(section='missing_section')
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    with pytest.raises(AnsibleLookupError, match='No section'):
        lu.run(['mykey'], variables={})


def test_allow_none_fallback(monkeypatch):
    paramvals = {
        'allow_none': True,
        'case_sensitive': False,
        'file': 'fake.ini',
        'type': 'ini',
        'section': 'mysection',
        'default': None,
        're': False,
        'encoding': 'utf-8',
    }
    contents = b"[mysection]\nmykey = myvalue\n"
    lu = _make_lookup(monkeypatch, paramvals, contents)
    ret = lu.run(['mykey'], variables={})
    assert ret == ['myvalue']
