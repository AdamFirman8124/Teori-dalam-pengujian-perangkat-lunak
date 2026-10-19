

# Generated at 2022-06-22 13:02:29.910605
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().has_command("toggle_pgzero_mode")

# Generated at 2022-06-22 13:02:31.943220
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:02:35.240314
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_in_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"



# Generated at 2022-06-22 13:02:44.091600
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    mock_workbench = Mock(spec=TkWorkbench)
    mock_workbench.get_variable.return_value = Mock(spec=TkVariable)
    mock_workbench.option = Mock(spec=TkOption)
    mock_workbench.option.get.return_value = True
    mock_workbench.option.set.return_value = True
    mock_workbench.option.get_default.return_value = True
    mock_workbench.option.get_category.return_value = True
    # Error without a mock environment
    with pytest.raises(AttributeError):
        load_plugin(mock_workbench)
    # Create a real environment
    os.environ["PGZERO_MODE"] = "auto"

# Generated at 2022-06-22 13:02:52.448575
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    old_in_simple_mode = wb.in_simple_mode
    old_get_option = wb.get_option
    old_get_variable = wb.get_variable
    old_PGZERO_MODE = os.environ.get("PGZERO_MODE")


# Generated at 2022-06-22 13:02:53.096272
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:02:55.790179
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:01.193512
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_variable(_OPTION_NAME, True)
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:12.808677
# Unit test for function update_environment
def test_update_environment():
    from unittest import TestCase
    from unittest.mock import patch

    TestCase.maxDiff = None

    get_workbench().set_option(_OPTION_NAME, True)
    os.environ.pop("PGZERO_MODE", None)
    with patch("thonny.shell.ShellTextWidget.send_to_subprocess") as send_to_subprocess:
        update_environment()
        send_to_subprocess.assert_called_once_with("import os; print(os.getenv('PGZERO_MODE'))")
        send_to_subprocess.reset_mock()

        update_environment()
        send_to_subprocess.assert_not_called()

    # in simple mode PGZERO_MODE is always set to "auto"
    get_workbench().set_simple_mode

# Generated at 2022-06-22 13:03:21.954432
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import Mock, patch
    from thonny.config_ui import ConfigurationPage
    from thonny import get_workbench
    from tkinter import ttk
    from tkinter import messagebox
    
    import os

    workbench = Workbench()
    conf = workbench.get_variable("run.pgzero_mode")
    conf.set(True)

    assert os.environ["PGZERO_MODE"] == "True"

    conf.set(False)
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:32.476802
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    load_plugin()
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)



# Generated at 2022-06-22 13:03:40.990837
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    from thonny.workbench import Workbench
    wb = Workbench()
    wb.set_option(_OPTION_NAME, False)

    # Set flag to 0 and assert that the environment variable is set to "False"
    env_backup = dict(os.environ)
    get_workbench().in_simple_mode = MagicMock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    os.environ = env_backup

    # Set flag to 1 and assert that the environment variable is set to "True"
    get_workbench().set_option(_OPTION_NAME, True)
    get_workbench().in_simple_mode = MagicMock(return_value=False)

# Generated at 2022-06-22 13:03:49.887007
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.misc_utils import running_on_linux
    from thonny import get_workbench
    wb = Mock()
    wb.in_simple_mode = Mock(return_value=False)
    wb.get_option = Mock(return_value=False)
    get_workbench._impl = wb
    update_environment()
    
    if running_on_linux():
        assert os.environ["PGZERO_MODE"] == "0"
    else:
        os.environ.pop("PGZERO_MODE", None)

# Generated at 2022-06-22 13:04:00.748833
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny.misc_utils import running_on_windows

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    if running_on_windows():
        assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:02.276441
# Unit test for function load_plugin
def test_load_plugin():
    # N/A
    pass

# Generated at 2022-06-22 13:04:12.247493
# Unit test for function update_environment
def test_update_environment():
    assert os.environ.get("PGZERO_MODE", "") == ""

    orig_get_workbench = thonny.workbench.get_workbench
    workbench = FakeWorkbench()

    try:
        thonny.workbench.get_workbench = lambda: workbench

        update_environment()
        assert os.environ.get("PGZERO_MODE", "") == "False"

        workbench.options[_OPTION_NAME] = True
        update_environment()
        assert os.environ.get("PGZERO_MODE", "") == "True"
    finally:
        thonny.workbench.get_workbench = orig_get_workbench



# Generated at 2022-06-22 13:04:21.318818
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.config import Configuration
    from thonny.globals import get_workbench
    from thonny import THONNY_USER_DIR

    workbench = get_workbench()
    workbench.in_simple_mode = Mock(return_value=True)
    # test that mode is "auto" when in simple mode
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    workbench.in_simple_mode = Mock(return_value=False)
    # create user configuration file with default option
    user_config_path = os.path.join(THONNY_USER_DIR, "config.json")

# Generated at 2022-06-22 13:04:28.704394
# Unit test for function update_environment
def test_update_environment():
    values_to_test = [
        (False, "off"),
        (True, "auto"),
        (True, "auto"),
        (False, "off"),
    ]
    for value, expected_pgzero_mode in values_to_test:
        get_workbench().set_option(_OPTION_NAME, value)
        update_environment()
        assert os.environ["PGZERO_MODE"] == expected_pgzero_mode


# Unit tests for function toggle_variable

# Generated at 2022-06-22 13:04:38.787692
# Unit test for function update_environment
def test_update_environment():
    # TODO: make tests independent of environment variables
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_default(_OPTION_NAME, False)

    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().step_into_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().step_out_of_simple_mode()
    update_environment()
    assert os.environ

# Generated at 2022-06-22 13:04:41.864689
# Unit test for function toggle_variable
def test_toggle_variable():
    if get_workbench().get_option(_OPTION_NAME):
        assert bool(os.environ["PGZERO_MODE"])
    else:
        assert not bool(os.environ["PGZERO_MODE"])

# Generated at 2022-06-22 13:04:54.843888
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    # This test will use the Tkinter get_intvar
    from tkinter import IntVar
    from unittest.mock import patch
    from thonny.config_ui import ConfigurationPage


# Generated at 2022-06-22 13:05:03.722581
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "True"
    plugin = sys.modules[__name__]
    try:
        reload(plugin)
        assert os.environ["PGZERO_MODE"] == "False"
        exec("import thonny")
        get_workbench().set_option(_OPTION_NAME, True)
        get_workbench().in_simple_mode = lambda: False
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
    finally:
        del sys.modules[__name__]
        reload(plugin)

# Generated at 2022-06-22 13:05:10.850448
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.getenv("PGZERO_MODE") == "False"

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.getenv("PGZERO_MODE") == "True"

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.getenv("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:05:22.061902
# Unit test for function update_environment
def test_update_environment():
    # Set to non-default value
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, None)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Simulate simple mode
    get_workbench().set_option("running.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:26.268565
# Unit test for function toggle_variable
def test_toggle_variable():
    load_plugin()
    v = get_workbench().get_variable(_OPTION_NAME)
    assert not v.get()

    toggle_variable()
    assert v.get()

    toggle_variable()
    assert not v.get()


# Generated at 2022-06-22 13:05:28.146118
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert "toggle_pgzero_mode" in get_workbench().commands

# Generated at 2022-06-22 13:05:30.582461
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:05:35.513909
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.in_simple_mode = MagicMock(return_value=False)
    wb.set_option(_OPTION_NAME, True)

    update_environment()

    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:39.457664
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    var = wb.get_variable(_OPTION_NAME)
    assert not var.get()
    assert os.environ["PGZERO_MODE"] == "False"
    assert not wb.in_simple_mode()

    toggle_varia

# Generated at 2022-06-22 13:05:50.604395
# Unit test for function update_environment
def test_update_environment():
    from .thonny import Workbench
    import os
    import unittest

    class TestEnvironment(unittest.TestCase):
        def test_update_environment(self):
            from .thonny import Workbench
            from thonny.plugins.pgzero_mode import update_environment
            from thonny.workbench import get_workbench
            from thonny.languages import tr
            wb = Workbench()
            wb.set_default(_OPTION_NAME, False)
            wb.add_command(
                "toggle_pgzero_mode",
                "run",
                tr("Pygame Zero mode"),
                toggle_variable,
                flag_name=_OPTION_NAME,
                group=40,
            )
            if get_workbench().in_simple_mode():
                os.environ

# Generated at 2022-06-22 13:06:06.088395
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().in_simple_mode = lambda : False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:06:09.541968
# Unit test for function load_plugin
def test_load_plugin():
    pass

if __name__ == "__main__":
    load_plugin()

# Generated at 2022-06-22 13:06:12.201837
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:21.295583
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench

    get_workbench = Mock(return_value=Workbench.instance())
    Workbench.instance().set_default = Mock()
    Workbench.instance().add_command = Mock()
    Workbench.instance().set_in_simple_mode = Mock()
    load_plugin()
    assert get_workbench.mock_calls == [call(), call()]
    assert Workbench.instance().set_default.mock_calls == [call(_OPTION_NAME, False)]

# Generated at 2022-06-22 13:06:30.497987
# Unit test for function update_environment
def test_update_environment():
    # Setup
    os.environ.clear()
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)

    # Tests
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.get_option(_OPTION_NAME).set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Teardown
    os.environ.clear()


# Generated at 2022-06-22 13:06:41.160581
# Unit test for function toggle_variable
def test_toggle_variable():
    return
    # simple mode
    get_workbench().set_simple_mode(True)
    try:
        get_workbench().get_variable(_OPTION_NAME).set(False)
        toggle_variable()
        assert get_workbench().get_variable(_OPTION_NAME).get() == True
    finally:
        get_workbench().set_simple_mode(False)

    # normal mode
    get_workbench().get_variable(_OPTION_NAME).set(False)
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False


    # PGZERO_MODE
    os.environ["PGZERO_MODE"] = "auto"
   

# Generated at 2022-06-22 13:06:48.971626
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    wb = Mock()
    wb.add_command = Mock()
    wb.set_default = Mock()

    globals()["get_workbench"] = Mock(return_value=wb)

    load_plugin()

    # called twice: to create option and to add command
    assert wb.add_command.call_count == 2
    assert wb.add_command.call_args_list[0][0][0] == "toggle_pgzero_mode"
    assert wb.add_command.call_args_list[1][0][0] == "toggle_pgzero_mode"
    assert wb.add_command.call_args_list[0][0][1] == "run"

# Generated at 2022-06-22 13:06:58.314060
# Unit test for function update_environment
def test_update_environment():
    # prep
    mw = get_workbench()
    mw.set_simple_mode(False)

    mw.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    mw.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # cleanup
    del os.environ["PGZERO_MODE"]
    mw.set_option(_OPTION_NAME, False)

# Generated at 2022-06-22 13:07:06.505999
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_windows
    from thonny import get_workbench
    from thonny.workbench import Workbench
    import thonny
    import os
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    #####################################################################
    # Create workbench to run in -- set simple mode
    thonny.workbench.simple_mode = True
    thonny.workbench.set_default(_OPTION_NAME, False)
    thonny.work

# Generated at 2022-06-22 13:07:12.175588
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:07:44.826164
# Unit test for function update_environment
def test_update_environment():
    # Get the current environment
    old_env = os.environ.copy()

    # Get the Thonny workbench
    wb = get_workbench()

    # Set default for the PyGame Zero mode
    wb.set_default(_OPTION_NAME, True)

    # Run the update_environment function
    update_environment()

    # Verify that the environment was changed
    assert os.environ != old_env, "Environment is not updated"

    # Verify that the new value is "False"
    assert os.environ["PGZERO_MODE"] == "True", "Environment value is not 'True'"

    # Reset the environment
    os.environ.clear()
    os.environ.update(old_env)

# Generated at 2022-06-22 13:07:56.134649
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    wb.set_option(_OPTION_NAME, False)
    assert not os.environ.get("PGZERO_MODE")
    wb.set_default(_OPTION_NAME, True)
    wb.set_option(_OPTION_NAME, False)
    assert not os.environ.get("PGZERO_MODE")
    wb.set_default(_OPTION_NAME, True)
    wb.set_option(_OPTION_NAME, True)
    assert os.environ.get("PGZERO_MODE") == "1"
    wb.set_default(_OPTION_NAME, False)
    wb.set_option(_OPTION_NAME, False)
    assert not os.environ

# Generated at 2022-06-22 13:08:01.553944
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:06.637282
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

# Generated at 2022-06-22 13:08:14.027599
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    assert os.environ.get("PGZERO_MODE") is None
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "True"

# Generated at 2022-06-22 13:08:24.273697
# Unit test for function update_environment
def test_update_environment():
    from test.test_base import clone_workbench

    wb = clone_workbench()
    wb.set_simple_mode(True)
    os.environ['PGZERO_MODE'] = 'spam'
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'auto'
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'True'
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'False'

# Generated at 2022-06-22 13:08:31.852687
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench
    from unittest import mock

    option_name = "run.pgzero_mode"

    with mock.patch.object(Workbench, "get_option", return_value=False):
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"

    with mock.patch.object(Workbench, "get_option", return_value=True):
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:08:37.620641
# Unit test for function update_environment
def test_update_environment():
    class WB:
        def get_option(self, name):
            assert name == _OPTION_NAME
            return True

        def in_simple_mode(self):
            return True

    original_get_workbench = get_workbench
    try:
        get_workbench = lambda: WB()
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    finally:
        get_workbench = original_get_workbench

# Generated at 2022-06-22 13:08:41.138354
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)


# Generated at 2022-06-22 13:08:47.443820
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_simple_mode(None)
    update_environment()
    assert os.environ["PGZERO_MODE"] != "auto"
    workbench.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:49.334475
# Unit test for function load_plugin
def test_load_plugin():
    import thonny
    thonny.get_workbench().unset_option(_OPTION_NAME)
    load_plugin()

    # check toggle_variable
    assert thonny.get_workbench().get_option(_OPTION_NAME) is False
    toggle_variable()
    assert thonny.get_workbench().get_option(_OPTION_NAME) is True
    toggle_variable()
    assert thonny.get_workbench().get_option(_OPTION_NAME) is False

    # check update_environment
    update_environment()
    if "PGZERO_MODE" in os.environ:
        assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    update_environment()
    if "PGZERO_MODE" in os.environ:
        assert os

# Generated at 2022-06-22 13:09:56.314103
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    if _OPTION_NAME in wb.get_variables():
        wb.get_variable(_OPTION_NAME).set(False)
    # test that it's toggled on
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get()
    # test that it's toggled off
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get()

# Generated at 2022-06-22 13:10:07.092366
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
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False

if __name__ == "__main__":
    load_plugin()
    print(os.environ["PGZERO_MODE"])
    toggle_variable()
    print(os.environ["PGZERO_MODE"])
    toggle_variable()

# Generated at 2022-06-22 13:10:10.401255
# Unit test for function load_plugin
def test_load_plugin():
    print("Test not implemented")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test_load_plugin()
    print("%s" % ("OK"))

# Generated at 2022-06-22 13:10:15.507780
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().enter_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:25.006256
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    get_workbench = Mock()
    get_workbench.in_simple_mode = lambda: False
    get_workbench.get_option = Mock()
    get_workbench.set_default = Mock()
    get_workbench.add_command = Mock()

    global _OPTION_NAME
    _OPTION_NAME = "run.pgzero_mode_dummy"

    load_plugin()

    get_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
    get_workbench.add_command.assert_called_once()



# Generated at 2022-06-22 13:10:28.401736
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb._configuration = {}
    wb._configuration[_OPTION_NAME] = False
    toggle_variable()
    assert wb._configuration[_OPTION_NAME] == True


# Generated at 2022-06-22 13:10:40.159784
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, Tester, ui_utils

    workbench = Tester().show_frame(get_workbench())
    os.environ["PGZERO_MODE"] = "auto"

    def check_view() -> bool:    
        return (
            len(workbench.get_variable(_OPTION_NAME).trace_vdelete()) == 0
            and len(workbench.get_variable(_OPTION_NAME).trace_vdelete()) == 0
        )

    load_plugin()

    assert os.environ["PGZERO_MODE"] == "False"
    assert workbench.get_option(_OPTION_NAME) == False
    assert workbench.in_simple_mode() == False
    assert check_view() == True


# Generated at 2022-06-22 13:10:43.516480
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:53.671329
# Unit test for function update_environment
def test_update_environment():
    # Simple mode
    workbench = get_workbench()
    workbench.config_db["run"] = {"simple_mode": True}
    update_environment()
    os.environ["PGZERO_MODE"] == "auto"
    del os.environ["PGZERO_MODE"]
    # PGZERO_MODE defined by setting
    workbench.config_db["run"] = {"simple_mode": False, "run.pgzero_mode":True}
    update_environment()
    os.environ["PGZERO_MODE"] == "True"
    del os.environ["PGZERO_MODE"]
    # PGZERO_MODE should be undefined if not in simple mode
    workbench.config_db["run"] = {"simple_mode": False, "run.pgzero_mode":False}
    update_environment()
