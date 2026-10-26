

# Generated at 2026-10-25 10:02:26.038641
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from unittest.mock import MagicMock
    from jinja2.utils import missing
    from ansible.template.vars import AnsibleJ2Vars

    # 1. all empty
    templar = MagicMock()
    templar.available_variables = {}
    assert len(AnsibleJ2Vars(templar, {})) == 0
    assert len(AnsibleJ2Vars(templar, {}, {})) == 0

    # 2. distinct keys are summed
    templar.available_variables = {'a': 1, 'b': 2}
    obj = AnsibleJ2Vars(templar, {'c': 3}, {'d': 4})
    assert len(obj) == 4  # {a,b,c,d}

    # 3. overlapping keys are deduplicated (set union)
    templar.available_variables = {'a': 1, 'b': 2}
    obj = AnsibleJ2Vars(templar, {'b': 20, 'c': 30}, {'c': 300, 'd': 400})
    assert len(obj) == 4  # {a,b,c,d}, not 2+2+2=6
    assert len(obj) == len(list(iter(obj)))
    assert len(obj) == len(set(iter(obj)))

    # 4. locals filtering affects __len__
    # 'l_' prefix stripped, 'context'/'environment'/'template' excluded,
    # 'missing'

# Generated at 2026-10-25 10:03:17.466440
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar:
        def __init__(self):
            self.available_variables = {'host_var': 'host_value'}
        def template(self, variable):
            return variable

    templar = DummyTemplar()
    globals_dict = {'g_var': 'g_value'}
    j2vars = Ansible

# Generated at 2026-10-25 10:03:32.219208
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:03.238924
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:04:05.987247
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:08.872738
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:11.292407
# Unit test for method add_locals of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:13.707572
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:16.122967
# Unit test for method __iter__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:04:19.878750
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:04:21.349304
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar:
        def __init__(self):
            self.available_variables = {'host_var': 'host_value'}
        def template(self, variable):
            return variable

    templar = DummyTemplar()
    globals_dict = {'g_var': 'g_value'}
    j2vars = Ansible

# Generated at 2026-10-25 10:05:02.733240
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:05:05.325941
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:07.741290
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:10.156292
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:12.569960
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:14.984286
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:17.399264
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:19.814698
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:05:33.146097
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:05:58.864584
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.vars.hostvars import HostVars


# Generated at 2026-10-25 10:06:15.849046
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:06:18.591782
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:06:21.005355
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:06:38.479539
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:07:18.106447
# Unit test for method add_locals of class AnsibleJ2Vars
def test_AnsibleJ2Vars_add_locals():
    class DummyTemplar:
        def __init__(self):
            self.available_variables = {'host_var': 'host_value'}
        def template(self, variable):
            return variable

    templar = DummyTemplar()
    globals_dict = {'g_var': 'g_value'}
    j2vars = Ansible

# Generated at 2026-10-25 10:07:20.977421
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:07:23.553980
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:07:39.290734
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:07:40.825538
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:07:42.363003
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = MagicMock()
    templar.available_variables = {}
    test_globals = {'myglobal': 'g_value'}

    # 1. locals=None -> empty _locals, stores refs

# Generated at 2026-10-25 10:07:45.152943
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:08:16.372587
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:08:19.037321
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:08:21.644026
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:08:24.061830
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:08:26.476223
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:08:28.890931
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:08:47.603115
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:09:05.320474
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:09:07.368951
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:09:27.028990
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:09:29.685758
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:09:32.098932
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:09:34.512442
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:10.037280
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:10:17.613741
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:22.230447
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:10:25.095305
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:27.511883
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:30.297578
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:32.712868
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:35.131702
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:10:37.548933
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:08.293200
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from jinja2.utils import missing
    fake_templar = object()
    fake_globals = {'g1': 'gv1', 'range': range}
    # 1. locals defaults to empty dict when omitted
    v = AnsibleJ2Vars(fake_templar, fake_globals)
    assert v._templar is fake_templar
    assert v._globals is fake_globals
    assert v._locals == {}
    # 2. explicit None locals behaves the same
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals=None)
    assert v._templar is fake_templar
    assert v._globals is fake_globals
    assert v._locals == {}
    # 3. non-dict locals is ignored
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals=['not', 'a', 'dict'])
    assert v._locals == {}
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals='string')
    assert v._locals == {}
    # 4. plain locals keys are copied
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals={'foo': 'bar', 'num': 42})
    assert v._locals == {'foo': 'bar', 'num': 42}
    # 5. l_ prefix is stripped
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals={'l_foo': 'bar'})
    assert v._locals == {'foo': 'bar'}
    # 6. jinja2 internal keys are filtered out
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals={'context': 1, 'environment': 2, 'template': 3, 'keep': 4})
    assert v._locals == {'keep': 4}
    # 7. missing sentinel values are skipped
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals={'a': missing, 'b': 'ok', 'l_c': missing, 'l_d': 'ok2'})
    assert v._locals == {'b': 'ok', 'd': 'ok2'}
    # 8. combined behavior
    v = AnsibleJ2Vars(fake_templar, fake_globals, locals={'foo': 1, 'l_bar': 2, 'context': 3, 'environment': 4, 'template': 5, 'skip': missing})
    assert v._locals == {'foo': 1, 'bar': 2}
    assert 'context' not in v._locals
    assert 'environment' not in v._locals
    assert 'template' not in v._locals
    assert 'skip' not in v._locals

# Generated at 2026-10-25 10:11:26.309985
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:27.747488
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:11:30.163826
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:32.700637
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:35.115293
# Unit test for constructor of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:37.530926
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:39.945091
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:41.480134
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:11:44.448812
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:45.882948
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:11:49.060878
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:11:51.924697
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:11:53.295484
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():from ansible.template.vars import AnsibleJ2Vars

# Generated at 2026-10-25 10:11:56.091701
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class _FakeTemplar:
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, v):
            return v
    templar = _FakeTemplar({'templ_var': 'tv', 'shared': 'from_templar'})
    globals_dict = {'global_var': 'gv', 'shared': 'from_global'}
    locals_dict = {'local_var': 'lv'}
    obj = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert ('local_var' in obj) is True
    assert ('templ_var' in obj) is True
    assert ('global_var' in obj) is True
    assert ('shared' in obj) is True
    assert ('missing_key' in obj) is False
    assert ('Missing_Key_Case' in obj) is False
    obj_locals_none = AnsibleJ2Vars(templar, globals_dict, None)
    assert ('local_var' in obj_locals_none) is False
    assert ('templ_var' in obj_locals_none) is True
    assert ('global_var' in obj_locals_none) is True
    obj_empty = AnsibleJ2Vars(_FakeTemplar({}), {}, None)
    assert ('anything' in obj_empty) is False
    assert ('' in obj_empty) is False
    obj_lprefix = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar'})
    assert ('foo' in obj_lprefix) is True
    assert ('l_foo' in obj_lprefix) is False
    obj_missing = AnsibleJ2Vars(templar, {}, {'a': missing})
    assert ('a' in obj_missing) is False
    obj_excluded = AnsibleJ2Vars(templar, {}, {'context': 1, 'environment': 2, 'template': 3, 'ok': 4})
    assert ('context' in obj_excluded) is False
    assert ('environment' in obj_excluded) is False
    assert ('template' in obj_excluded) is False
    assert ('ok' in obj_excluded) is True
    obj_override = AnsibleJ2Vars(_FakeTemplar({'x': 1}), {'x': 2, 'y': 2}, {'x': 3, 'y': 3, 'z': 3})
    assert ('x' in obj_override) is True
    assert ('y' in obj_override) is True
    assert ('z' in obj_override) is True

# Generated at 2026-10-25 10:12:21.782561
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:12:24.441467
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2026-10-25 10:12:26.888371
# Unit test for method __getitem__ of class AnsibleJ2Vars