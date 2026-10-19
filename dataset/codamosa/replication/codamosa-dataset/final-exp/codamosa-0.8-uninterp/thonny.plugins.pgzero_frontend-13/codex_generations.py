

# Generated at 2022-06-22 13:02:40.917619
# Unit test for function update_environment
def test_update_environment():
    from thonny.plugins.run.config_page import _set_option
    import os
    test_wb = get_workbench()
    try:
        _set_option(_OPTION_NAME, True)
        test_wb.in_simple_mode()
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
        _set_option(_OPTION_NAME, False)
        test_wb.in_simple_mode()
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
    except:
        return False

# Generated at 2022-06-22 13:02:46.303780
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:02:56.224993
# Unit test for function load_plugin
def test_load_plugin():
    def option_func():
        return get_workbench().get_variable(_OPTION_NAME).get()

    assert option_func() is False

    toggle_variable()
    assert option_func() is True


if __name__ == "__main__":
    import unittest
    from unittest.mock import Mock

    from thonny import get_workbench

    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.add_command(
    	"toggle_pgzero_mode",
    	"run",
    	tr("Pygame Zero mode"),
    	toggle_variable,
    	flag_name=_OPTION_NAME,
    	group=40,
    )

# Generated at 2022-06-22 13:03:07.963635
# Unit test for function load_plugin
def test_load_plugin():
    global get_workbench
    _get_workbench = get_workbench

    class Workbench:
        def set_default(_, value):
            self._default_value = value

        def get_default(_):
            return self._default_value

        def get_variable(self, name):
            self._option_name = name
            return Variable()

        def add_command(self, name, cmd_name, label, cmd, flag_name, group):
            self._name = name
            self._cmd_name = cmd_name
            self._label = label
            self._cmd = cmd
            self._flag_name = flag_name
            self._group = group

        def in_simple_mode(self):
            self._mode = "simple"
            return True

        def get_option(self, name):
            assert self._

# Generated at 2022-06-22 13:03:15.964954
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    wb = mock.Mock()
    wb.get_option.return_value = False
    wb.in_simple_mode.return_value = False
    with mock.patch.object(thonny.workbench, "Workbench", return_value=wb):
        import thonny.plugins.pgzero_mode
        thonny.plugins.pgzero_mode.update_environment()
        assert os.environ["PGZERO_MODE"] == "False"

    wb.get_option.return_value = True
    wb.in_simple_mode.return_value = False
    with mock.patch.object(thonny.workbench, "Workbench", return_value=wb):
        import thonny.plugins.pgzero_mode
        thonny.plugins.pg

# Generated at 2022-06-22 13:03:20.767793
# Unit test for function toggle_variable
def test_toggle_variable():
    # Arrange
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_variable(_OPTION_NAME).get() == False

    # Act
    toggle_variable()

    # Assert
    assert wb.get_variable(_OPTION_NAME).get() != False

# Generated at 2022-06-22 13:03:27.211855
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import MagicMock
    get_workbench().set_default = MagicMock()
    get_workbench().add_command = MagicMock()
    load_plugin()
    get_workbench().set_default.assert_called_once_with(
        _OPTION_NAME, False
    )
    get_workbench().add_command.assert_called_once()
    get_workbench().add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

# Generated at 2022-06-22 13:03:33.011156
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    old_variable = wb.get_variable(_OPTION_NAME)
    assert old_variable.get() == False
    load_plugin()
    new_variable = wb.get_variable(_OPTION_NAME)
    assert old_variable == new_variable
    assert new_variable.get() == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert new_variable.get() == True
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:39.164372
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    # Step 1
    assert get_workbench().get_variable(_OPTION_NAME).get() is True
    # Step 2
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() is False

# Generated at 2022-06-22 13:03:47.145597
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert not wb.get_option(_OPTION_NAME)
    # option to True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME)
    # option to False
    toggle_variable()
    assert not wb.get_option(_OPTION_NAME)
    # option to True
    wb.get_variable(_OPTION_NAME).set(True)
    update_environment()
    assert wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:04:00.530424
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    get_workbench().set_simple_mode()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:11.760039
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import Mock

    wb = Workbench()
    wb.set_simple_mode = Mock()
    wb.in_simple_mode = Mock(return_value=False)
    wb.set_default = Mock()
    wb.get_option = Mock(return_value=True)
    wb.get_variable = Mock(return_value=True)

    load_plugin()
    update_environment()

    wb.set_simple_mode.assert_called_with(False)
    wb.set_default.assert_called_with(_OPTION_NAME, False)
    wb.get_option.assert_called_with(_OPTION_NAME)

# Generated at 2022-06-22 13:04:20.885453
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.codeview import CodeViewText, create_code_view_text
    from thonny.workbench import Workbench
    wb = Workbench()
    load_plugin()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:31.548321
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_simple_mode(True)
    try:
        load_plugin()
        assert get_workbench().in_simple_mode()
        assert not get_workbench().app.get_option(_OPTION_NAME)

        # toggle
        toggle_variable()
        assert not get_workbench().in_simple_mode()
        assert get_workbench().app.get_option(_OPTION_NAME)

        # set back to the default value
        toggle_variable()
        assert get_workbench().in_simple_mode()
        assert not get_workbench().app.get_option(_OPTION_NAME)
    finally:
        get_workbench().set_simple_mode(False)

# Generated at 2022-06-22 13:04:42.352514
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    import copy
    import os

    class MagicMockApp:
        def in_simple_mode(self):
            return False

        def get_option(self, name):
            return False

        def get_variable(self, name):
            return MagicMock()

    get_workbench().in_simple_mode = MagicMockApp().in_simple_mode
    get_workbench().get_option = MagicMockApp().get_option
    get_workbench().get_variable = MagicMockApp().get_variable

    stored_environ = copy.deepcopy(os.environ.copy())
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    os.environ = stored_environ

# Generated at 2022-06-22 13:04:43.958649
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    # TODO: check that entries are created correctly in menu and config variables

# Generated at 2022-06-22 13:04:55.526230
# Unit test for function load_plugin
def test_load_plugin():
    workbench = get_workbench()
    assert not workbench.get_option(_OPTION_NAME)
    load_plugin(workbench)
    assert workbench.get_option(_OPTION_NAME)
    workbench.set_option(_OPTION_NAME, False)
    assert not workbench.get_option(_OPTION_NAME)
    assert "PGZERO_MODE" not in os.environ
    toggle_variable()
    assert workbench.get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    workbench.set_option(_OPTION_NAME, False)
    workbench.set_simple_mode(True)
    assert not workbench.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:05:00.097331
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:05:09.033435
# Unit test for function load_plugin
def test_load_plugin():
    """
    Verify that the plugin loads correctly, and it's able to change the
    PGZERO_MODE environment variable value to "auto" and "False".
    """
    import unittest.mock
    import thonny
    import sys

    class _Mock_workbench:
        def __init__(self, _env: dict):
            self._env = _env
            self.get_variable = lambda _: _Mock_variable()
            self.in_simple_mode = lambda: False
            self.add_command = lambda *_: None
            self.set_default = lambda *_: None
            self.get_option = lambda _: False

        def get_environment(self):
            return self._env

        def set_environment(self, env):
            self._env = env


# Generated at 2022-06-22 13:05:20.788030
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
    assert os.environ["PGZERO_MODE"] == "0"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "1"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "0"
    assert get_workbench().get_variable("run.pgzero_mode").get() == False
    get_workbench().in_simple_mode = lambda: True
    update_environment()

# Generated at 2022-06-22 13:05:37.746521
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.plugins.pgzeromode import load_plugin
    from thonny.globals import get_workbench, get_runner
    from thonny.languages import tr

    workbench = get_workbench()
    workbench.set_default = Mock()
    workbench.add_command = Mock()
    runner = get_runner()

    load_plugin()
    assert workbench.set_default.call_count == 1
    assert workbench.set_default.call_args[0][0] == "run.pgzero_mode"
    assert workbench.set_default.call_args[0][1] == False
    assert workbench.add_command.call_count == 1

# Generated at 2022-06-22 13:05:49.065021
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.languages import tr
    from thonny.misc_utils import running_on_mac_os
    from thonny.ui_utils import check_variable_set_to_initial_value
    from thonny.ui_utils import check_variable_set_to_value
    from thonny.ui_utils import check_variable_value

    wb = get_workbench()
    wb.set_simple_mode(True)
    wb.clear_commands()

    load_plugin()
    check_variable_set_to_initial_value(wb, _OPTION_NAME, False, tr("Pygame Zero mode"))
    check_variable_set_to_value(wb, _OPTION_NAME, True, tr("Pygame Zero mode"))
    check

# Generated at 2022-06-22 13:05:53.862548
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_variable(_OPTION_NAME).get() == False
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == False

test_toggle_variable()

# Generated at 2022-06-22 13:06:00.907328
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny import get_workbench
    from thonny.plugins.pgzero_mode import _OPTION_NAME

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:06:02.975684
# Unit test for function toggle_variable
def test_toggle_variable():
    load_plugin()
    assert toggle_variable()

# Generated at 2022-06-22 13:06:10.148880
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_in_simple_mode(True)
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_in_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:20.086325
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.misc_utils import running_on_mac_os
    from thonny.misc_utils import running_on_rpi

    # test1: check if the function works correctly
    # set pgzero mode to True
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    # set pgzero mode to False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is False

    # test2: check the behaviour in simple mode
    get_workbench().set_simple_mode(True)
    get_workbench().set_option(_OPTION_NAME, True)
    toggle_variable()

# Generated at 2022-06-22 13:06:30.577733
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock
    from thonny.misc_utils import call_and_sink_return

    with mock.patch.dict(os.environ, {"PGZERO_MODE": "auto"}), mock.patch.dict(
        os.environ, {"THONNY_SIMPLE_MODE": "auto"}
    ):
        wb = mock.MagicMock()
        wb.get_variable.return_value = True
        wb.get_option.return_value = True
        load_plugin()

        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "auto"

        wb.in_simple_mode.return_value = False
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:06:41.238267
# Unit test for function toggle_variable
def test_toggle_variable():

    # Set up a dummy data structure that can be used by toggle_variable
    # "workbench" is the class used by thonny
    # "get_variable" is a method of the workbench class
    # "set" is a method of the Variable class (called here via get_variable)
    class workbench:
        @staticmethod
        def get_variable(name):
            class Variable:
                def __init__(self):
                    self.var_bool = False
                def get(self):
                    return self.var_bool
                def set(self, boolean):
                    self.var_bool = boolean
            return Variable()

    load_plugin()
    toggle_variable()

    # Make sure the variable is initially False
    assert workbench.get_variable("run.pgzero_mode").get() is False

    # Make sure that it

# Generated at 2022-06-22 13:06:49.033593
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.unset_option(_OPTION_NAME)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False
    assert (
        wb.get_variable(_OPTION_NAME).get() == wb.get_option(_OPTION_NAME)
        == False
    )
    assert "PGZERO_MODE" not in os.environ

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert (
        wb.get_variable(_OPTION_NAME).get() == wb.get_option(_OPTION_NAME)
        == True
    )

# Generated at 2022-06-22 13:07:00.809492
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:07:09.546224
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().in_simple_mode = MagicMock(return_value=False)
    get_workbench().set_default = MagicMock()
    get_workbench().add_command = MagicMock()
    get_workbench().get_option = MagicMock(return_value=False)
    get_workbench().get_variable = MagicMock(return_value=MagicMock())

    load_plugin()

    get_workbench().set_default.assert_called_with(_OPTION_NAME, False)
    get_workbench().add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )


# Unit test

# Generated at 2022-06-22 13:07:12.666559
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = Workbench()
    assert not wb.get_option(_OPTION_NAME)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME)
    toggle_variable()
    assert not wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:07:17.572723
# Unit test for function update_environment
def test_update_environment():
    workbench = get_workbench()
    try:
        workbench.in_simple_mode = lambda: True
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    finally:
        workbench.in_simple_mode = lambda: False
        del os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:07:23.318553
# Unit test for function toggle_variable
def test_toggle_variable():
    option_name = "run.pgzero_mode"
    v = get_workbench().get_variable(option_name)
    v.set(False)
    toggle_variable()
    assert v.get(), "option is not set to true"
    toggle_variable()
    assert not v.get(), "option is not set to false"

# Generated at 2022-06-22 13:07:25.979022
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False



# Generated at 2022-06-22 13:07:30.769443
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(
        _OPTION_NAME, True
    ) # preserve current value
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:37.154540
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.workbench import Workbench
    from thonny.common import IncompleteConfig
    wb = Workbench()
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ.keys()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:41.495847
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
    assert "PGZERO_MODE" in os.environ


# Generated at 2022-06-22 13:07:50.898008
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == 'False'
    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == 'True'
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == 'auto'

# Generated at 2022-06-22 13:08:23.390540
# Unit test for function update_environment
def test_update_environment():
    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    os.environ["THONNY_SIMPLE_MODE"] = "True"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:29.319077
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    if get_workbench().in_simple_mode():
        print(os.environ["PGZERO_MODE"])
        assert os.environ["PGZERO_MODE"] == "auto"
    else:
        assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:36.664580
# Unit test for function update_environment
def test_update_environment():
    import os
    import os.path
    import tempfile
    import thonny
    thonny.set_runner_path("echo")
    thonny.initialize_backend("shell")
    thonny_dir = os.path.join(tempfile.gettempdir(), "thonny")
    os.mkdir(thonny_dir)
    thonny.set_user_dir(thonny_dir)
    thonny.UIOption("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:42.345775
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock

    get_workbench = MagicMock(return_value=MagicMock())
    get_workbench().in_simple_mode.return_value = False
    get_workbench().get_option.return_value = True
    get_workbench().add_command.return_value = None

    update_environment()
    
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:51.680648
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default("run.pgzero_mode", None)
    load_plugin()
    assert wb.get_default("run.pgzero_mode") is False
    assert wb.get_option("run.pgzero_mode") is False
    assert "PGZERO_MODE" not in os.environ
    
    wb.set_option("run.pgzero_mode", True)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:56.391055
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_in_simple_mode(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_in_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:09:02.162296
# Unit test for function load_plugin
def test_load_plugin():
    class TestWorkbench:
        def __init__(self):
            self._variables = {}
            self.options = {}
            self.commands = []

        def get_variable(self, name):
            return self._variables[name]

        def get_option(self, name):
            return self.options[name]

        def set_default(self, name, value):
            self._variables[name] = value
            self.options[name] = value

        def add_command(self, name, category, caption, handler, flag_name=None, **kwargs):
            self.commands.append(
                (
                    name,
                    category,
                    caption,
                    handler,
                    flag_name,
                    kwargs,
                )
            )


# Generated at 2022-06-22 13:09:12.057169
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

    # check that it updates the environment
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:09:13.823112
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:09:23.653156
# Unit test for function load_plugin
def test_load_plugin():
    import sys
    import subprocess

    TEST_SCRIPT_PATH = os.path.join(
        os.path.dirname(__file__), "TEST_FILES", "pgzero_mode.py"
    )

    # Clean environment
    for var in ["PGZERO_MODE"]:
        if var in os.environ:
            del os.environ[var]

    # Testing non-pgzero_mode
    load_plugin()
    assert get_workbench().in_simple_mode() == False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    subprocess.run([sys.executable, TEST_SCRIPT_PATH]).check_returncode()

    # Testing pgzero_mode
    toggle_variable()
    assert get_workbench().in_simple_mode

# Generated at 2022-06-22 13:10:01.583561
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.ui_utils import askyesno
    mw = Mock()

    _OPTION_NAME = "run.pgzero_mode"

    def get_variable(option_name):
        class ValueObject:
            def __init__(self, value):
                self._value = value

            def get(self):
                return self._value

            def set(self, value):
                self._value = value

        if option_name == _OPTION_NAME:
            return ValueObject(True)
        else:
            raise RuntimeError("Unexpected option name")

    mw.get_variable = get_variable
    mw.get_option = get_variable
    mw.in_simple_mode = lambda option_name: False


# Generated at 2022-06-22 13:10:11.146176
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    assert wb.get_option(_OPTION_NAME)
    wb.set_default(_OPTION_NAME, False)
    assert not wb.get_option(_OPTION_NAME)
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_option(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:10:13.554871
# Unit test for function toggle_variable
def test_toggle_variable():
    # Arrange
    var = get_workbench().get_variable(_OPTION_NAME)
    var.set(False)

    # Act
    toggle_variable()

    # Assert
    assert var.get() == True

# Generated at 2022-06-22 13:10:18.652354
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert os.environ.get("PGZERO_MODE", False) is False
    toggle_variable()
    assert os.environ.get("PGZERO_MODE", False) is True
    toggle_variable()
    assert os.environ.get("PGZERO_MODE", False) is False

# Generated at 2022-06-22 13:10:22.647333
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    assert not wb.get_variable(_OPTION_NAME)
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME)


load_plugin()

# Generated at 2022-06-22 13:10:28.806625
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, True)
    os.environ["PGZERO_MODE"] = str(workbench.get_option(_OPTION_NAME))
    assert os.environ.get("PGZERO_MODE") == "True"
    toggle_variable()
    assert os.environ.get("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:10:35.785969
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert "auto" == os.environ["PGZERO_MODE"]
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert 'True' == os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:10:39.623302
# Unit test for function load_plugin
def test_load_plugin():
    # This function is extremely difficult to unit test as it affects the environment,
    # so just test the update_environment function
    os.environ.pop("PGZERO_MODE", None)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:10:46.106202
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_runner, get_workbench
    from thonny.workflow import Command

    get_runner().stop_debugging()

    _OPTION_NAME = "run.pgzero_mode"
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option(_OPTION_NAME, True)

    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:55.744035
# Unit test for function update_environment
def test_update_environment():
    # Test setting on/off condition, and resetting
    os.environ["PGZERO_MODE"] = '"False"'
    assert os.environ["PGZERO_MODE"] == '"False"'
    update_environment()  # Set on, test condition
    assert os.environ["PGZERO_MODE"] == '"True"'
    update_environment()  # Set off, test condition
    assert os.environ["PGZERO_MODE"] == '"False"'

    # Test in simple mode
    os.environ["PGZERO_MODE"] = '"True"'
    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == '"auto"'
    get_workbench().set_simple_mode(False) # Set normal mode

# Generated at 2022-06-22 13:11:58.682740
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench
    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, True)

    toggle_variable()
    assert not workbench.get_variable(_OPTION_NAME).get()

# Generated at 2022-06-22 13:12:01.925020
# Unit test for function toggle_variable
def test_toggle_variable():
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False



# Generated at 2022-06-22 13:12:07.077665
# Unit test for function update_environment
def test_update_environment():
    old_env = os.environ.copy()


# Generated at 2022-06-22 13:12:09.531363
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_rpi

    if not running_on_rpi():
        return

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:12:15.818587
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "False"
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

if __name__ == "__main__":
    test_update_environment()

# Generated at 2022-06-22 13:12:23.466390
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:12:32.107789
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, True)
    with mock.patch.dict(os.environ, clear=True):
        update_environment()
        assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_default(_OPTION_NAME, False)
    with mock.patch.dict(os.environ, clear=True):
        update_environment()
        assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().change_simple_mode(True)
    with mock.patch.dict(os.environ, clear=True):
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"