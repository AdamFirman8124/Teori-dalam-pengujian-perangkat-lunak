# file: project/ansible/plugins/lookup/ini.py:136-204
# asked: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}
# gained: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}

import pytest
import ansible.plugins.lookup.ini as ini_mod
from ansible.plugins.lookup.ini import LookupModule
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleLookupError, AnsibleOptionsError
from ansible.module_utils.six.moves import configparser
from ansible.module_utils._text import to_native


def _base_paramvals(**over):
    pv = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'dummy.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    }
    pv.update(over)
    return pv


def _make_lookup(monkeypatch, paramvals, contents):
    monkeypatch.setattr(configparser.ConfigParser, 'readfp', configparser.ConfigParser.read_file, raising=False)
    lookup = LookupModule(loader=DataLoader())
    monkeypatch.setattr(lookup, 'set_options', lambda *a, **k: None)
    monkeypatch.setattr(lookup, 'get_options', lambda *a, **k: paramvals)
    monkeypatch.setattr(lookup, 'find_file_in_search_path', lambda *a, **k: '/fake.ini')
    monkeypatch.setattr(lookup._loader, '_get_file_contents', lambda *a, **k: (contents, True))
    monkeypatch.setattr(lookup, '_deprecate_inline_kv', lambda *a, **k: None, raising=False)
    return lookup


def test_direct_single_value(monkeypatch):
    pv = _base_paramvals()
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=myval\n")
    ret = lookup.run(['mykey'], variables={})
    assert ret == ['myval']


def test_case_sensitive_true(monkeypatch):
    pv = _base_paramvals(allow_no_value=True, case_sensitive=True)
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nMyKey=CAPSVAL\n")
    ret = lookup.run(['MyKey'], variables={})
    assert ret == ['CAPSVAL']
    assert lookup.cp.optionxform == to_native


def test_allow_none_fallback(monkeypatch):
    pv = _base_paramvals(case_sensitive=False)
    del pv['allow_no_value']
    pv['allow_none'] = True
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=myval\n")
    ret = lookup.run(['mykey'], variables={})
    assert ret == ['myval']
    assert lookup.cp is not None


def test_properties_type(monkeypatch):
    pv = _base_paramvals(type='properties', section='global')
    lookup = _make_lookup(monkeypatch, pv, b"myprop=propval\n")
    ret = lookup.run(['myprop'], variables={})
    assert ret == ['propval']
    assert pv['section'] == 'java_properties'


def test_inline_kv_success(monkeypatch):
    pv = _base_paramvals(section='global')
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pvals: ['mykey', 'section=mysection'])
    lookup = _make_lookup(monkeypatch, pv, b"[mysection]\nmykey=inlineval\n")
    ret = lookup.run(['mykey section=mysection'], variables={})
    assert ret == ['inlineval']
    assert pv['section'] == 'mysection'


def test_inline_invalid_option(monkeypatch):
    pv = _base_paramvals()
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pvals: ['mykey', 'bad_opt=val'])
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")
    with pytest.raises(AnsibleLookupError, match='not a valid option'):
        lookup.run(['mykey bad_opt=val'], variables={})


def test_inline_value_error(monkeypatch):
    pv = _base_paramvals()
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pvals: ['a=b=c'])
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")
    with pytest.raises(AnsibleLookupError, match='Could not use'):
        lookup.run(['a=b=c'], variables={})


def test_inline_missing_key(monkeypatch):
    pv = _base_paramvals()
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pvals: ['section=global', 'file=dummy'])
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")
    with pytest.raises(AnsibleOptionsError, match='No key to lookup'):
        lookup.run(['section=global file=dummy'], variables={})


def test_inline_second_token_ignored(monkeypatch):
    pv = _base_paramvals()
    monkeypatch.setattr(ini_mod, '_parse_params', lambda term, pvals: ['firstkey', 'secondtoken'])
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nfirstkey=firstval\n")
    ret = lookup.run(['firstkey secondtoken'], variables={})
    assert ret == ['firstval']


def test_duplicate_option_error(monkeypatch):
    pv = _base_paramvals()
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nkey=1\nkey=2\n")
    with pytest.raises(AnsibleLookupError, match='Duplicate option'):
        lookup.run(['key'], variables={})


def test_no_section_error(monkeypatch):
    pv = _base_paramvals(section='missing')
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")

    def _raise(key, section, dflt, is_regexp):
        raise configparser.NoSectionError(section)

    monkeypatch.setattr(lookup, 'get_value', _raise)
    with pytest.raises(AnsibleLookupError, match='No section'):
        lookup.run(['mykey'], variables={})


def test_list_expansion(monkeypatch):
    pv = _base_paramvals()
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")
    monkeypatch.setattr(lookup, 'get_value', lambda *a, **k: ['v1', 'v2'])
    ret = lookup.run(['mykey'], variables={})
    assert ret == ['v1', 'v2']


def test_var_none_returns_empty(monkeypatch):
    pv = _base_paramvals()
    lookup = _make_lookup(monkeypatch, pv, b"[global]\nmykey=x\n")
    monkeypatch.setattr(lookup, 'get_value', lambda *a, **k: None)
    ret = lookup.run(['mykey'], variables={})
    assert ret == []
