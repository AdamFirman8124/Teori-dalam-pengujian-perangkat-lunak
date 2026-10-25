

# Generated at 2026-10-24 15:05:51.428533
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:05:54.505757
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-24 15:05:55.836387
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_string(u"""
[global]
user=admin
host=example.com

[integration]
user=integration_user
""")

    # Existing key in section
    assert lookup.get_value('user', 'global', '', False) == 'admin'

    # Missing key -> returns default
    assert lookup.get_value('missing', 'global', 'fallback', False) == 'fallback'

    # Key exists in another section only
    assert lookup.get_value('user', 'integration', '', False) == 'integration_user'

    # Regexp: match all keys in section
    result = lookup.get_value('.*', 'global', '', True)
    assert sorted(result) == ['admin', 'example.com']

    # Regexp: partial match
    result = lookup.get_value('hos.', 'global', '', True)
    assert result == ['example.com']

    # Regexp with no matches -> empty list
    assert lookup.get_value('nomatch.*', 'global', '', True) == []

# Generated at 2026-10-24 15:06:07.985094
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from unittest.mock import MagicMock
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.plugins.lookup import LookupBase

    # 1. default constructor
    lookup = LookupModule()
    assert isinstance(lookup, LookupBase)
    assert isinstance(lookup, LookupModule)
    assert lookup._loader is None
    assert lookup._templar is None
    assert hasattr(lookup, 'run')
    assert hasattr(lookup, 'get_value')

    # 2. constructor with loader/templar
    fake_loader = MagicMock()
    fake_templar = MagicMock()
    lookup2 = LookupModule(loader=fake_loader, templar=fake_templar)
    assert lookup2._loader is fake_loader
    assert lookup2._templar is fake_templar

# Generated at 2026-10-24 15:06:11.034045
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:06:13.452830
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:06:15.862340
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:06:18.374458
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 15:06:20.786628
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 15:06:23.199619
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 15:06:25.610749
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:28.022883
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:30.571744
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:32.992622
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:35.405967
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:37.820849
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:40.232152
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:42.647642
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:06:45.904910
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-24 15:07:00.749700
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:07:03.765759
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-24 15:07:07.023796
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:21.133016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:07:23.649217
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:26.230865
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:28.645192
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:31.059006
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:33.472367
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:35.885881
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:38.445457
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:40.858095
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:43.271592
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:45.686757
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:07:48.099782
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:07:50.515462
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:07:52.928834
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:55.342845
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:07:57.760349
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:00.171802
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:02.586007
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:05.000964
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:07.414832
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:08:11.102364
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-24 15:08:14.275981
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:15.917803
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:08:20.010482
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:21.333937
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:08:24.415122
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:25.858349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:08:41.412897
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:08:43.831171
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:08:46.435308
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:08:48.850368
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:51.265037
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:53.679977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:56.092865
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:08:58.652296
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:01.260320
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:03.800570
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:06.213364
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:08.626281
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:11.342687
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:12.851465
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:09:15.903597
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:17.223542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:09:20.325178
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:21.762828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:09:23.078832
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_string(u"""
[global]
user=admin
host=example.com

[integration]
user=integration_user
""")

    # Existing key in section
    assert lookup.get_value('user', 'global', '', False) == 'admin'

    # Missing key -> returns default
    assert lookup.get_value('missing', 'global', 'fallback', False) == 'fallback'

    # Key exists in another section only
    assert lookup.get_value('user', 'integration', '', False) == 'integration_user'

    # Regexp: match all keys in section
    result = lookup.get_value('.*', 'global', '', True)
    assert sorted(result) == ['admin', 'example.com']

    # Regexp: partial match
    result = lookup.get_value('hos.', 'global', '', True)
    assert result == ['example.com']

    # Regexp with no matches -> empty list
    assert lookup.get_value('nomatch.*', 'global', '', True) == []

# Generated at 2026-10-24 15:09:26.265091
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:27.907970
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:09:41.715511
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:44.131150
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:46.736321
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:09:49.147251
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:51.741411
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:54.559221
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:56.971666
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:09:59.383977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:01.797362
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:04.420854
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:06.835333
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:09.247903
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:11.662234
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:14.075162
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:16.488813
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:18.902391
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:21.318697
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:23.730325
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:26.428283
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:28.842247
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:31.256653
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:33.670448
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:36.083653
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:38.499610
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:10:40.908469
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:43.322401
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:45.740370
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:48.149749
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:50.564211
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:52.977515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:55.392604
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:10:57.806718
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:00.223245
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:02.638184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:05.053143
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:23.175696
# Unit test for method run of class LookupModule
def test_LookupModule_run():import tempfile


# Generated at 2026-10-24 15:11:26.285069
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:27.619323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:11:30.783056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:32.096033
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:11:34.662547
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:37.075320
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:39.704267
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:42.116705
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:44.529655
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:46.942905
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:11:51.343431
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:53.894088
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:56.306732
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:11:58.721424
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:01.135640
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:03.552599
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:05.965015
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:08.377808
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:10.790252
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:12:13.205797
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:15.616553
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:18.030636
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:20.449481
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:22.862593
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:25.279022
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:27.688155
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:30.103055
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:32.515869
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:36.590072
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:37.934731
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:12:40.711598
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:42.158377
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:12:45.108809
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:46.529140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:12:50.656355
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:12:51.969870
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:12:58.645264
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:00.017819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:13:02.571030
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:04.985739
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:07.624700
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:10.037317
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:12.565606
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:14.979352
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:17.399106
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:19.811611
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:22.227469
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:24.643507
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:27.055598
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:29.629277
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:32.042217
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:34.455458
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:36.871402
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:39.281387
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:41.696902
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:44.106615
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:46.522380
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:48.938569
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:51.350426
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:53.760407
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:56.173770
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:13:58.587276
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:01.006715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:03.417688
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:05.832544
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:19.459145
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:21.872730
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:24.284447
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:26.696618
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:29.109222
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:31.524543
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:47.975040
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_string(u"""
[global]
user=admin
host=example.com

[integration]
user=integration_user
""")

    # Existing key in section
    assert lookup.get_value('user', 'global', '', False) == 'admin'

    # Missing key -> returns default
    assert lookup.get_value('missing', 'global', 'fallback', False) == 'fallback'

    # Key exists in another section only
    assert lookup.get_value('user', 'integration', '', False) == 'integration_user'

    # Regexp: match all keys in section
    result = lookup.get_value('.*', 'global', '', True)
    assert sorted(result) == ['admin', 'example.com']

    # Regexp: partial match
    result = lookup.get_value('hos.', 'global', '', True)
    assert result == ['example.com']

    # Regexp with no matches -> empty list
    assert lookup.get_value('nomatch.*', 'global', '', True) == []

# Generated at 2026-10-24 15:14:50.703007
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:52.019137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.plugins.lookup.ini import LookupModule

    content = "[global]\nkey1=value1\nkey2 = spaced value\n[integration]\nuser=alice\n"
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)
    with open(path, "w") as f:
        f.write(content)

    lookup = LookupModule()
    paramvals = {
        "type": "ini",
        "file": path,
        "section": "global",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": False,
        "allow_no_value": False,
    }

    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_options = lambda: paramvals
    lookup._deprecate_inline_kv = lambda: None
    lookup.find_file_in_search_path = lambda variables, subdir, fname: fname

    class FakeLoader:
        @staticmethod
        def _get_file_contents(p):
            return content.encode("utf-8"), False

    lookup._loader = FakeLoader()

    assert lookup.run(["key1"]) == ["value1"]
    assert lookup.run(["key2"]) == ["spaced value"]
    assert lookup.run(["missing_key"]) == [""]

    paramvals["section"] = "integration"
    paramvals["default"] = "nobody"
    assert lookup.run(["user"]) == ["alice"]
    assert lookup.run(["ghost"]) == ["nobody"]

    os.unlink(path)

# Generated at 2026-10-24 15:14:54.765158
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:57.179035
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:14:59.766140
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:02.178421
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:15:04.591930
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:15:07.191568
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 15:15:09.753226
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:12.168083
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:14.583752
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:17.011632
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:19.422073
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:21.836685
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:24.248505
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:26.662264
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:29.076446
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:31.490294
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:33.902102
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:15:36.317014
# Unit test for method run of class LookupModule