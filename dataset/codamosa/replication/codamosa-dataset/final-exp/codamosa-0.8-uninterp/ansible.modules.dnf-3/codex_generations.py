

# Generated at 2022-06-13 05:14:39.153189
# Unit test for method list_items of class DnfModule
def test_DnfModule_list_items():
    dnf_module = DnfModule(
        base=None,
        conf_file='/etc/dnf/dnf.conf',
        disable_gpg_check=False,
        disablerepo='disabled-repository',
        enablerepo='enabled-repository',
        installroot='/installroot',
        names=['python-nameko'],
        state='installed',
        update_cache=False
    )
    dnf_module.run()

# Generated at 2022-06-13 05:14:47.290458
# Unit test for constructor of class DnfModule
def test_DnfModule():
    # Test default values
    d = DnfModule()
    assert d.conf_file == '/etc/dnf/dnf.conf'
    assert d.disable_gpg_check == False
    assert d.disablerepo == []
    assert d.download_only == False
    assert d.enablerepo == []
    assert d.installroot == '/'
    assert d.list == None
    assert d.names == []
    assert d.state == None
    assert d.autoremove == False

    # Test values passed in

# Generated at 2022-06-13 05:14:49.333340
# Unit test for method is_lockfile_pid_valid of class DnfModule
def test_DnfModule_is_lockfile_pid_valid():
    assert False # TODO: implement your test here


# Generated at 2022-06-13 05:15:02.270333
# Unit test for constructor of class DnfModule
def test_DnfModule():
    """Unit test for constructor of class DnfModule."""

    # If a module has list of parameters,
    # we need to pass all arguments to constructor of class Module
    module = DnfModule(
        conf_file='/tmp/test.conf',
        disable_gpg_check=True,
        disablerepo='*',
        enablerepo='*',
        installroot='/',
        list='available',
        name='kernel*',
        state='installed',
        update_cache=True,
        update_only=True
    )

    if not module or not isinstance(module, DnfModule):
        print('test_DnfModule(): constructor of class DnfModule failed')
        sys.exit(1)


# Generated at 2022-06-13 05:15:15.019772
# Unit test for method list_items of class DnfModule
def test_DnfModule_list_items():
    dnf_module = DnfModule()
    dnf_module.base = mock.MagicMock()
    dnf_module.base.fill_sack = mock.MagicMock(return_value=None)
    # Mock the search_repo method call
    dnf_module.base.repos.search_repos.return_value = []
    dnf_module.base.sack.query().available().run()._nevra = {'module': ['buildmodule']}
    dnf_module.base.sack.query().installed().run()._nevra = []
    dnf_module.base.sack.query().available().run().filter.return_value = []
    dnf_module.base.sack.query().installed().run().filter.return_value = []

# Generated at 2022-06-13 05:15:26.624473
# Unit test for method ensure of class DnfModule
def test_DnfModule_ensure():
    """ Test DnfModule.ensure()
    """

    destdir = tempfile.mkdtemp(prefix='ansible_dnf_module_', dir=tempfile.gettempdir())
    downloaded = []
    installed = []
    removed = []

    mock_module = MockDnfModule('/tmp/foo', 'bar')
    real_module = DnfModule(mock_module)

    # Mock out the methods we care about and leave the rest to the real class
    real_module._base = Mock()
    real_module._base.conf.best = True
    real_module._base.read_comps = True
    real_module._base.conf.destdir = destdir
    real_module._base.repos.all().pkgdir = destdir
    real_module._base.resolve = Mock()


# Generated at 2022-06-13 05:15:38.615347
# Unit test for constructor of class DnfModule
def test_DnfModule():
    mod = DnfModule()
    assert mod.base is None
    assert mod.module_base is None
    assert mod.conf_file == '/etc/dnf/dnf.conf'
    assert mod.disable_gpg_check is False
    assert mod.disablerepo == []
    assert mod.download_only is False
    assert mod.download_dir is None
    assert mod.enablerepo == []
    assert mod.list == ''
    assert mod.lock_age == datetime.timedelta(seconds=900)
    assert mod.lock_type == 'write'
    assert mod.lock_timeout == 600
    assert mod.names == []
    assert mod.security is False
    assert mod.state is None
    assert mod.update_cache is False
    assert mod.update_only is False
    assert mod.valid

# Generated at 2022-06-13 05:15:39.196863
# Unit test for function main
def test_main():
    """Check function main"""



# Generated at 2022-06-13 05:15:46.993296
# Unit test for constructor of class DnfModule
def test_DnfModule():
    module_args = {
        "name": "httpd",
        "list": None,
        "state": "present",
        "conf_file": None,
        "disable_gpg_check": None,
        "disablerepo": None,
        "enablerepo": None,
        "exclude": None,
        "installroot": None,
        "releasever": None,
        "autoremove": False,
        "download_only": False,
        "download_dir": None,
        "update_cache": False,
        "update_only": False,
        "validate_certs": None,
        "with_modules": False,
    }
    dnf_module = DnfModule(module_args)
    assert dnf_module.base is None

# Generated at 2022-06-13 05:15:53.651487
# Unit test for method run of class DnfModule
def test_DnfModule_run():
    # Arrange
    from ansible.module_utils.dnf_utils import dnf_module
    dnf_module.DnfModule.run = Fake_run
    dnf_module.DnfModule.list_items = Fake_list_items
    dnf_module.DnfBase._base = Fake_DnfBase__base
    dnf_module.DnfBase.read_comps = Fake_read_comps
    dnf_module.DnfBase._mark_package_install = Fake_mark_package_install
    dnf_module.DnfBase._is_module_installed = Fake_is_module_installed
    dnf_module.DnfBase._update_only = Fake_update_only


# Generated at 2022-06-13 05:17:57.671780
# Unit test for method list_items of class DnfModule
def test_DnfModule_list_items():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        dnf_module = DnfModule()
        dnf_module.base = mock.Mock()
        dnf_module.module = mock.Mock()
        dnf_module.module.params = {'list': 'updates'}
        dnf_module.list_items(['updates'])

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


# Generated at 2022-06-13 05:18:03.961470
# Unit test for constructor of class DnfModule

# Generated at 2022-06-13 05:18:07.928900
# Unit test for method list_items of class DnfModule
def test_DnfModule_list_items():
    test_dnf_module_instance = DnfModule()
    assert test_dnf_module_instance.list_items(test_dnf_module_instance.list) == None


# Generated at 2022-06-13 05:18:14.428634
# Unit test for method ensure of class DnfModule
def test_DnfModule_ensure():
    from ansible.module_utils.dnf.dnf import DnfModule
    d = DnfModule(autoremove=False,
                  base=None,
                  disable_gpg_check=False,
                  disablerepo=None,
                  enablerepo=None,
                  list=None,
                  module_base=None,
                  names=['httpd'],
                  state='present',
                  update_cache=False)
    d.ensure()



# Generated at 2022-06-13 05:18:25.288007
# Unit test for method list_items of class DnfModule
def test_DnfModule_list_items():
    """Test list_items() function."""

    # pylint: disable=too-few-public-methods
    class _Args(object):
        """Class to contain module arguments."""

        # pylint: disable=too-few-public-methods
        def __init__(self, names=[], state=None):
            """Initialize it."""
            self.names = names
            self.state = state
            self.conf_file = None

    class _Module(object):
        """Class to contain module functions."""
        # pylint: disable=too-few-public-methods,unused-argument,too-many-arguments
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = kwargs['fail_json']
            self.exit

# Generated at 2022-06-13 05:18:34.136441
# Unit test for method is_lockfile_pid_valid of class DnfModule
def test_DnfModule_is_lockfile_pid_valid():
    assert DnfModule(
        base_command=None,
        base=None,
        module_base=None,
        conf_file=None,
        disable_gpg_check=None,
        disablerepo=None,
        download_only=None,
        download_dir=None,
        enablerepo=None,
        installroot=None,
        list=None,
        name=None,
        state=None,
        update_cache=None,
        update_only=None,
        valid_exit_status=[0]
        ).is_lockfile_pid_valid()

# Generated at 2022-06-13 05:18:42.638430
# Unit test for constructor of class DnfModule
def test_DnfModule():
    module = AnsibleModule({
        'name': 'bash',
        'state': 'installed',
        'conf_file': '/etc/dnf/dnf.conf',
        'disablerepo': ['epel'],
        'enablerepo': ['base'],
        'installroot': '/var/tmp'
    })
    dnfmodule = DnfModule(module)
    assert dnfmodule.state == 'installed'
    assert dnfmodule.conf_file == '/etc/dnf/dnf.conf'
    assert dnfmodule.disablerepo == ['epel']
    assert dnfmodule.enablerepo == ['base']
    assert dnfmodule.installroot == '/var/tmp'


# Generated at 2022-06-13 05:18:46.080983
# Unit test for method is_lockfile_pid_valid of class DnfModule
def test_DnfModule_is_lockfile_pid_valid():
    dnf_module = DnfModule()
    assert dnf_module.is_lockfile_pid_valid("32") == True


# Generated at 2022-06-13 05:18:55.389732
# Unit test for function main
def test_main():
    p = module_utils.basic.AnsibleModule(
        **yumdnf_argument_spec
    )

    dm = DnfModule(p)

    p.fail_json = MagicMock()

    dm.base = dm._base(
        "/etc/dnf/dnf.conf",
        "disable.gpg.check",
        "disablerepo",
        "enablerepo",
        "/installroot"
    )
    dm.base.conf.disable_gpg_check = False
    dm.base.conf.disablerepo = "disablerepo"
    dm.base.conf.enablerepo = "enablerepo"
    dm.base.conf.installroot = "/installroot"
    dm.base.conf.best = True
    dm.conf_file

# Generated at 2022-06-13 05:19:05.101959
# Unit test for method is_lockfile_pid_valid of class DnfModule
def test_DnfModule_is_lockfile_pid_valid():

    # Create mock unit to be used as parameter
    mock_unit = create_autospec(unit)

    # Create mock unit providing file_exists
    mock_unit.file_exists.return_value = True

    # Create mock unit providing open_fifo
    mock_unit.open_fifo = mock_open()

    # Create an instance for the tested class
    fixture = DnfModule()

    # Create a mock variable providing unit is_lockfile_pid_valid.
    returned_value_from_function = 'fake'