

# Generated at 2022-06-22 13:02:47.712122
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from test.test_base import TestConfiguration

    wb = Workbench()
    wb.set_option = Mock()
    wb.add_command = Mock()
    wb.in_simple_mode = Mock()
    wb.get_variable = Mock(return_value=0)
    wb.get_option = Mock()

    load_plugin()

    assert wb.set_default.call_args == "run.pgzero_mode", False
    assert wb.get_option.call_args == False
    assert wb.get_variable.call_args == _OPTION_NAME

# Generated at 2022-06-22 13:02:56.350595
# Unit test for function load_plugin
def test_load_plugin():
    my_workbench = Mock()
    assert hasattr(my_workbench, 'set_default')
    assert hasattr(my_workbench, 'add_command')
    assert hasattr(my_workbench, 'get_option')
    get_workbench().set_default = my_workbench.set_default
    get_workbench().add_command = my_workbench.add_command
    get_workbench().get_option = my_workbench.get_option
    load_plugin()
    command_name = my_workbench.add_command.call_args[0][0]
    assert command_name == 'toggle_pgzero_mode'
    command_category = my_workbench.add_command.call_args[0][1]
    assert command_category == 'run'
    command_label = my_work

# Generated at 2022-06-22 13:03:07.675062
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    os.environ["PGZERO_MODE"] = ""
    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == ""
    wb.in_simple_mode = lambda: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.destroy()

# Generated at 2022-06-22 13:03:21.460046
# Unit test for function load_plugin
def test_load_plugin():
    test_wb = get_workbench()
    test_wb.set_default(_OPTION_NAME, False)
    assert test_wb.get_option(_OPTION_NAME) is False
    test_wb.set_default(_OPTION_NAME, True)
    assert test_wb.get_option(_OPTION_NAME) is True
    
    # Test for toggle_variable
    assert test_wb.get_variable(_OPTION_NAME) is True
    toggle_variable()
    assert test_wb.get_variable(_OPTION_NAME) is False
    toggle_variable()
    assert test_wb.get_variable(_OPTION_NAME) is True
    # Test for update_environment
    update_environment()
    assert os.environ["PGZERO_MODE"] is "True"
    toggle_variable()
    update_environment

# Generated at 2022-06-22 13:03:22.071860
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:03:27.553635
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    update_environment()


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:03:39.315406
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny import get_workbench
    from thonny.workbench import Workbench

    get_workbench = Mock(spec=Workbench)
    wb1 = get_workbench.get_variable(_OPTION_NAME)
    wb2 = get_workbench.get_variable(_OPTION_NAME)

    wb1._get_value.return_value = False
    wb2._get_value.return_value = True

    assert os.environ.get("PGZERO_MODE") == None
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"

    get_workbench = Mock(spec=Workbench)
    wb2 = get_workbench.get_variable(_OPTION_NAME)
    assert os

# Generated at 2022-06-22 13:03:49.642650
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    # need to load this to register command handlers.
    load_plugin()
    # load_plugin() initializes PGZERO_MODE in os.environ
    assert wb.in_simple_mode() == True
    assert os.environ["PGZERO_MODE"] == "auto"
    assert wb.get_option(_OPTION_NAME) == False

    # test the function toggle_variable
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:51.407923
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False

# Generated at 2022-06-22 13:04:03.285993
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.codeview import CodeView

    get_workbench().set_default("sidebar.view.Files", True)
    get_workbench().set_default("sidebar.view.Variables", True)

    # get_workbench().set_default("run.pgzero_mode", False)
    workbench = get_workbench()
    assert not workbench.get_option("run.pgzero_mode")
    load_plugin()
    assert not workbench.get_option("run.pgzero_mode")
    assert not os.environ.get("PGZERO_MODE")

    workbench.set_option("run.pgzero_mode", True)
    # workbench.set_option("run.pgzero_mode", False)
    # assert workbench.get_option("run.pgzero_mode")
   

# Generated at 2022-06-22 13:04:16.206757
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:24.132383
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:24.863480
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:04:34.943587
# Unit test for function update_environment
def test_update_environment():

    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass

# Generated at 2022-06-22 13:04:44.586485
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import get_workbench
    from thonny.misc_utils import running_on_mac_os

    mock_workbench = Mock(get_variable=Mock(return_value=Mock()))
    mock_workbench.get_variable.return_value.get.return_value = True
    get_workbench.return_value = mock_workbench

    # Check command is added
    load_plugin()
    if running_on_mac_os():
        assert mock_workbench.add_command.call_count == 1
        assert mock_workbench.add_command.call_args[0][0] == "toggle_pgzero_mode"
    else:
        assert mock_workbench.add_command.call_count == 2

# Generated at 2022-06-22 13:04:55.664792
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock
    from thonny import get_workbench
    from thonny.plugins.run import _OPTION_NAME

    workbench_mock = Mock(spec=get_workbench())
    setattr(workbench_mock, "in_simple_mode", lambda: True)
    setattr(workbench_mock, "get_option", lambda: False)
    setattr(workbench_mock, "set_option", lambda name, value: None)

    workbench_mock.set_default(_OPTION_NAME, False)
    workbench_mock._get_variable = lambda name: None
    get_workbench.set_workbench(workbench_mock)

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

    toggle

# Generated at 2022-06-22 13:05:06.605294
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_option("view.hide_toolbar", False)
    wb.set_option("view.hide_left_panel", False)
    wb.set_option("view.hide_interpreter_locals", False)
    wb.set_default(_OPTION_NAME, False)
    load_plugin()

    check_kbshortcut_info(keys=["<Alt>p"], command_id="toggle_pgzero_mode")
    
    # When started normally, pgzero_mode should be off by default
    wb.set_simple_mode(False)
    assert not wb.get_option(_OPTION_NAME)
    
    # When started in simple mode, pgzero_mode should be on by default

# Generated at 2022-06-22 13:05:15.140867
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    load_plugin()
    cmd = wb.get_command("toggle_pgzero_mode")
    assert cmd is not None
    assert cmd.label == "Pygame Zero mode"
    assert cmd.group == 40
    var = wb.get_variable(_OPTION_NAME)
    assert not var.get()
    assert os.environ["PGZERO_MODE"] == "False"
    cmd.run()
    assert var.get()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:20.676312
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench

    workbench.setup()
    from thonny.plugins.pgzero_mode import load_plugin

    load_plugin()
    assert workbench.get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "False"


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:05:31.571006
# Unit test for function load_plugin
def test_load_plugin():
    import imp
    import logging
    import os

    logger = logging.getLogger("thonny")
    logger.setLevel("INFO")
    handler = logging.FileHandler("test.log", mode="w")
    logger.addHandler(handler)
    logger.info("test")

    workbench = imp.new_module("thonny.workbench")
    workbench.get_option = lambda x: True
    workbench.in_simple_mode = lambda: True
    workbench.add_command = lambda x, y, z, w, **kw: None
    workbench.set_default = lambda x, y: None
    sys.modules["thonny.workbench"] = workbench

    _OPTION_NAME = "run.pgzero_mode"
    _OPTION_SIMPLE = "view.simple_mode"



# Generated at 2022-06-22 13:05:51.948816
# Unit test for function update_environment
def test_update_environment():
    from thonny.test_utils import in_temporary_dir

    @in_temporary_dir
    def test():
        os.environ["PGZERO_MODE"] = "0"
        get_workbench().set_simple_mode(True)
        update_environment()
        assert os.environ["PGZERO_MODE"]=="auto"
        
        get_workbench().set_simple_mode(False)
        update_environment()
        assert os.environ["PGZERO_MODE"]=="False"
        
        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"]=="True"

    test()

# Generated at 2022-06-22 13:06:02.755311
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock

    wb = Mock()
    wb.in_simple_mode = Mock(return_value=False)
    wb.get_option = Mock(return_value=False)
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.in_simple_mode = Mock(return_value=True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.in_simple_mode = Mock(return_value=False)
    wb.get_option = Mock(return_value=True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode = Mock(return_value=False)
    wb.get

# Generated at 2022-06-22 13:06:11.904933
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.register_variable(_OPTION_NAME, True)
    update_environment()
    os.environ["PGZERO_MODE"] == "True"
    wb.set_simple_mode(True)
    update_environment()
    os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    update_environment()
    os.environ["PGZERO_MODE"] == "True"
    wb.register_variable(_OPTION_NAME, False)
    update_environment()
    os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:20.444359
# Unit test for function update_environment
def test_update_environment():
    # Test the default mode
    get_workbench().in_simple_mode = lambda:False # type: ignore
    get_workbench().get_option = lambda s:False # type: ignore
    environ = os.environ.copy()
    update_environment()
    if "PGZERO_MODE" in environ:
        assert environ["PGZERO_MODE"] == os.environ["PGZERO_MODE"]
    else:
        assert os.environ["PGZERO_MODE"] == "0"
    # Test simple mode
    get_workbench().in_simple_mode = lambda:True # type: ignore
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:30.996670
# Unit test for function toggle_variable
def test_toggle_variable():
    import unittest
    import thonny.workbench
    original_get_workbench = thonny.workbench.get_workbench

    class MockWorkbench:
        def get_variable(self, name):
            if name == _OPTION_NAME:
                return True
            else:
                raise KeyError()

        def get_option(self, name):
            if name == _OPTION_NAME:
                return True
            else:
                raise KeyError()

    class MyTest(unittest.TestCase):
        def test_toggle_variable(self):
            thonny.workbench.get_workbench = lambda: MockWorkbench()
            self.assertTrue(toggle_variable())

    my_test = MyTest()

# Generated at 2022-06-22 13:06:37.221774
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    w = Workbench()
    load_plugin()

    assert w.get_option("run.pgzero_mode") == False
    assert os.environ["PGZERO_MODE"] == "False"
    assert len(w.get_variable("run.pgzero_mode", None).change_listeners) == 1

# Generated at 2022-06-22 13:06:41.779020
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:06:45.469925
# Unit test for function toggle_variable
def test_toggle_variable():
    b = get_workbench().get_variable(_OPTION_NAME)
    b.set(True)
    assert b.get() == True
    toggle_variable()
    assert b.get() == False
    toggle_variable()
    assert b.get() == True

# Generated at 2022-06-22 13:06:54.710391
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    load_plugin()
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:07:03.954469
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        old_value = os.environ["PGZERO_MODE"]
        original_mode = get_workbench().get_option(_OPTION_NAME)
    except KeyError:
        old_value = None
        os.environ["PGZERO_MODE"] = "off"
        original_mode = False

    assert get_workbench().get_option(_OPTION_NAME) == original_mode
    assert os.environ["PGZERO_MODE"] == "off"

    toggle_variable()

# Generated at 2022-06-22 13:07:33.059709
# Unit test for function update_environment
def test_update_environment():
    b = get_workbench()
    try:
        b.set_default(_OPTION_NAME, True)
        update_environment()
        assert os.getenv("PGZERO_MODE") == "True"

        b.set_default(_OPTION_NAME, False)
        update_environment()
        assert os.getenv("PGZERO_MODE") == "False"

        b.set_default(_OPTION_NAME, True)
        b.enter_simple_mode()
        update_environment()
        assert os.getenv("PGZERO_MODE") == "auto"
    finally:
        b.leave_simple_mode()

# Generated at 2022-06-22 13:07:39.135924
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().add_command = MagicMock()
    load_plugin()
    get_workbench().add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

# Generated at 2022-06-22 13:07:44.673323
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    # test environment
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:55.868020
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import patch
    from thonny import get_workbench
    wb = Workbench()
    wb.set_option("run.pgzero_mode", True)
    wb.in_simple_mode = lambda : False
    get_workbench().set_default("run.pgzero_mode", False)
    get_workbench().in_simple_mode = lambda : False
    with patch.dict(os.environ) as mock:
        update_environment()
        assert mock['PGZERO_MODE'] == "True"
        wb.in_simple_mode = lambda : True
        update_environment()
        assert mock['PGZERO_MODE'] == "False"
        get_workbench().in_simple_mode = lambda : True
        update

# Generated at 2022-06-22 13:08:03.773840
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import workbench

    workbench.Workbench = Mock()
    workbench.get_workbench = Mock()
    workbench.get_workbench().set_default = Mock()
    workbench.get_workbench().add_command = Mock()

    load_plugin()

    assert workbench.get_workbench().set_default.call_count == 1
    workbench.get_workbench().set_default.assert_called_with(_OPTION_NAME, False)
    assert workbench.get_workbench().add_command.call_count == 1
    
    # Test the toggle_variable function
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()

# Generated at 2022-06-22 13:08:15.016893
# Unit test for function load_plugin
def test_load_plugin():
    original_env = os.environ.copy()

# Generated at 2022-06-22 13:08:26.328866
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock

    wb = MagicMock()
    wb.in_simple_mode.return_value = False
    wb.get_option.return_value = False
    get_workbench.return_value = wb

    update_environment()
    wb.in_simple_mode.assert_called_once()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.get_option.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.in_simple_mode.return_value = None

# Generated at 2022-06-22 13:08:33.981795
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:43.068665
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    wb = Mock()
    wb.get_option = lambda: None
    wb.in_simple_mode = lambda: False

    wb.set_default = Mock()
    wb.add_command = Mock()

    test_plugin = sys.modules[__name__]
    test_plugin.get_workbench = lambda: wb

    test_plugin.load_plugin()

    assert "toggle_pgzero_mode" in wb.add_command.call_args_list[0][1]["command_id"]
    assert wb.in_simple_mode.called
    assert wb.set_default.called
    assert wb.add_command.called

# Generated at 2022-06-22 13:08:53.995724
# Unit test for function load_plugin
def test_load_plugin():
    # pylint: disable=import-outside-toplevel
    from thonny.plugins.pgzero_mode import load_plugin

    class TestWorkbench:
        def __init__(self):
            self._variable_dict = {}
            self._command_info_list = []

        def get_variable(self, name):
            return self._variable_dict[name]

        def set_default(self, name, value):
            self._variable_dict[name] = value

        def add_command(self, name, category, label, handler, **kwargs):
            self._command_info_list.append((name, category, label, handler, kwargs))

    wb = TestWorkbench()
    load_plugin()


# Generated at 2022-06-22 13:09:53.686465
# Unit test for function toggle_variable
def test_toggle_variable():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:10:04.739165
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os
    wb = mock.Mock()
    wb.in_simple_mode.return_value = False

    wb.add_command = mock.Mock()
    wb.get_option = mock.Mock(return_value=False)
    wb.set_default = mock.Mock()

    with mock.patch.dict("os.environ", {}):
        load_plugin()
        assert os.environ["PGZERO_MODE"] == "False"
        wb.add_command.assert_called_once()

    wb.reset_mock()
    wb.get_option.return_value = True
    with mock.patch.dict("os.environ", {}):
        load_plugin()
        assert os.environ

# Generated at 2022-06-22 13:10:14.199340
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert "auto" == os.environ["PGZERO_MODE"]

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert "True" == os.environ["PGZERO_MODE"]

    assert get

# Generated at 2022-06-22 13:10:18.461251
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    w = get_workbench()
    assert w.get_option(_OPTION_NAME) == False
    toggle_variable()

    assert w.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert w.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:10:29.393214
# Unit test for function update_environment
def test_update_environment():
    # Test if the environment variable is set to auto when in simple mode
    get_workbench().set_in_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test if the environment variable is set to true when in advanced mode
    get_workbench().set_in_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test if the environment variable is set to false when in advanced mode
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:39.227766
# Unit test for function update_environment
def test_update_environment():
    """Test that PGZERO_MODE is set to auto in simple mode"""
    from unittest import mock
    from thonny import get_workbench

    wb = get_workbench()
    old_simple_mode = wb.in_simple_mode
    wb.in_simple_mode = lambda : True

    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.in_simple_mode = lambda : False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.in_simple_mode = old_simple_mode

# Generated at 2022-06-22 13:10:42.027698
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().in_simple_mode = True
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().in_simple_mode = False
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "0"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:10:52.543510
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().enter_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().leave_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    del os.environ["PGZERO_MODE"]
    update_environment()

# Generated at 2022-06-22 13:11:00.966250
# Unit test for function update_environment
def test_update_environment():
    # configure non-simple mode
    wb = get_workbench()
    wb.set_simple_mode(False)

    # false by default
    assert os.getenv("PGZERO_MODE") == "False"

    # set to true
    wb.set_option(_OPTION_NAME, True)
    update_environment()

    assert os.getenv("PGZERO_MODE") == "True"

    # switch to simple mode
    wb.set_simple_mode(True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:11:09.891061
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from thonny.config import get_config_dir
    from thonny.config_ui import ConfigurationPage
    import os
    from thonny.misc_utils import running_on_mac_os
    from thonny.testing import run_subprocess
    from thonny.languages import install_translation
    from thonny import get_runner
    from thonny.ui_utils import CommonDialog

    if running_on_mac_os():
        raise unittest.SkipTest("This test is not suitable for Mac OS")
        
    if os.path.exists(get_config_dir()):
        raise Exception("Configuration directory must not exist!")
