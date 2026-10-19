

# Generated at 2022-06-13 02:41:53.756471
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    arguments = dict(
        name=dict(type='str', default='Amazon'),
        data=dict(type='str', default='Amazon'),
        path=dict(type='str', default='/etc/os-release'),
        collected_facts=dict(type='dict', default=dict()),
    )
    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=False,
    )


# Generated at 2022-06-13 02:42:00.671105
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    p = DistributionFiles('/tmp/ansible_facts_test')
    data = """
DISTRIB_RELEASE="18.06.1"
DISTRIB_CODENAME="CC"
DISTRIB_TARGET="ar71xx/generic"
DISTRIB_DESCRIPTION="OpenWrt SNAPSHOT r13439-b04a43e3f3"
DISTRIB_TAINTS="no-all busybox"
"""
    name = 'OpenWrt'
    path = '/etc/openwrt_release'
    collected_facts = {'distribution': 'NA', 'distribution_release': 'NA', 'distribution_version': 'NA'}
    parsed_dist_file, parsed_dist_file_facts = p.parse_distribution_file_OpenWrt(name, data, path, collected_facts)


# Generated at 2022-06-13 02:42:08.472008
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        add_file_common_args=False
    )

    module.run_command = MagicMock(side_effect=get_run_command_mock(platform.release()))
    module.os = platform
    module.platform = platform

    theDistribution = Distribution(module)

    rc, out, err = theDistribution.module.run_command("/sbin/sysctl -n kern.version")
    match = re.match(r'OpenBSD\s[0-9]+.[0-9]+-(\S+)\s.*', out)
    if match:
        expected_release = match.groups()[0]
    else:
        expected_release = 'release'

    openbsd_facts = theDistribution

# Generated at 2022-06-13 02:42:20.150752
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import Distribution
    from ansible.module_utils.facts.system import get_uname

    m = basic.AnsibleModule(argument_spec={})
    dist = Distribution(m)

    # We have to mock the `get_uname()` method because it depends on the
    # current executed system.
    import sys
    if sys.version_info[0] < 3:
        builtins = __builtins__
    else:
        import builtins

    saved_get_uname = get_uname

# Generated at 2022-06-13 02:42:32.217646
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    dist_file_object = DistributionFiles()
    data = '''
NAME="CoreOS"
ID=coreos
VERSION=1068.8.0
VERSION_ID=1068.8.0
BUILD_ID=
PRETTY_NAME="CoreOS 1068.8.0"
ANSI_COLOR="38;5;75"
HOME_URL="https://coreos.com/"
BUG_REPORT_URL="https://github.com/coreos/bugs/issues"
COREOS_BOARD=amd64-usr
'''
    coreos_facts = {'distribution_release': ''}
    collected_facts = {'distribution_release': 'NA'}
    expected_facts = {'distribution_release': 'CoreOS'}
    assert expected_facts == dist_file_object.parse_distribution_file

# Generated at 2022-06-13 02:42:41.448076
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    class Module:
        def __init__(self):
            self.run_command_result = True, "10.14.6\n", ""

        def run_command(self, command, use_unsafe_shell=False):
            return self.run_command_result

    module = Module()

    dist = Distribution(module)
    facts = dist.get_distribution_Darwin()
    assert facts['distribution'] == 'MacOSX'
    assert facts['distribution_major_version'] == '10'
    assert facts['distribution_version'] == '10.14.6'

    module.run_command_result = False, "", ""
    facts = dist.get_distribution_Darwin()
    assert facts['distribution'] is None
    assert facts['distribution_major_version'] is None

# Generated at 2022-06-13 02:42:45.745738
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    assert distribution.get_distribution_SunOS() == {'distribution': 'SmartOS',
                                                     'distribution_release': 'SmartOS 16.9.1 RELEASE joyent_20210128T011902Z',
                                                     'distribution_version': '16.9.1',
                                                     'os_family': 'Solaris'}



# Generated at 2022-06-13 02:42:50.669543
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    name = 'Mandriva'
    data = '''DISTRIB_ID=MandrivaLinux
DISTRIB_RELEASE=2010.0
DISTRIB_CODENAME=Cooker
DISTRIB_DESCRIPTION="Mandriva Linux 2010.0 (Cooker)"'''
    path = 'test'
    collected_facts = {'distribution_release': 'NA',
                       'distribution_version': 'NA'}
    dist_file_data = {'distribution': 'Mandriva',
                      'distribution_release': 'Cooker',
                      'distribution_version': '2010.0'}
    dist_file_facts = DistributionFiles().parse_distribution_file_Mandriva(name, data, path, collected_facts)
    assert dist_file_facts[1] == dist_file_data


#

# Generated at 2022-06-13 02:43:00.433198
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    import ast
    ansible_module = AnsibleModule(
        argument_spec={})

    name = ast.literal_eval('clearlinux')
    data = ast.literal_eval("""
NAME="Clear Linux OS for Intel Architecture"
VERSION="28210"
ID=clear-linux-os
ID_LIKE=tizen
VERSION_ID=28210
PRETTY_NAME="Clear Linux OS for Intel Architecture 28210"
ANSI_COLOR="1;32"
CPE_NAME="cpe:/o:clearlinux:clear_linux:28210"
HOME_URL="https://clearlinux.org/"
SUPPORT_URL="https://clearlinux.org/documentation/clear-linux/tickets/"
BUG_REPORT_URL="https://github.com/clearlinux/distribution/issues/new"
        """)
    path

# Generated at 2022-06-13 02:43:07.445126
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    try:
        from __main__ import module
        d = DistributionFiles(module)
    except ImportError:
        d = DistributionFiles(None)

# Generated at 2022-06-13 02:43:49.709716
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    module = get_test_modules()


# Generated at 2022-06-13 02:43:58.647712
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    # `platform` module doesn't work on Windows and MacOSX
    import getpass
    if getpass.getuser() == 'vagrant' and os.path.exists('/usr/bin/sw_vers'):
        # Mac OS X
        distro = Distribution(AnsibleModule(
        )).get_distribution_facts()
        assert distro['distribution'] == 'MacOSX'
        assert distro['distribution_version'] == '10.14'
        assert distro['distribution_major_version'] == '10'
        assert distro['distribution_release'] == '14'
    elif 'LSB_VERSION' in os.environ:
        # Linux
        from ansible.module_utils import basic
        d = Distribution(AnsibleModule())
        distro = d.get_distribution_

# Generated at 2022-06-13 02:44:03.598481
# Unit test for method get_distribution_SunOS of class Distribution

# Generated at 2022-06-13 02:44:10.518370
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # Input parameters for method get_distribution_DragonFly
    # self:
    # Module object
    module = AnsibleModule(argument_spec={})
    # Object creation of class Distribution
    distribution = Distribution(module)
    # Calling of method get_distribution_DragonFly of class Distribution
    result = distribution.get_distribution_DragonFly()
    # Tests if the output of method get_distribution_DragonFly of class Distribution is as expected
    assert result == {'distribution_release': '5.4.3-RELEASE'}

# Generated at 2022-06-13 02:44:22.346905
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    collected_facts = {}
    d = DistributionFiles()
    path = '/etc/openwrt_release'
    name = 'openwrt'
    data = '''
DISTRIB_ID=OpenWrt
DISTRIB_RELEASE=12.09-rc1
DISTRIB_REVISION=r39074
DISTRIB_CODENAME=attitude_adjustment
DISTRIB_TARGET=ar71xx/generic
DISTRIB_DESCRIPTION="OpenWrt Attitude Adjustment 12.09-rc1 r39074"
DISTRIB_TAINTS='''
    parsed_dist_file, parsed_dist_file_facts = d.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    assert parsed_dist_file

# Generated at 2022-06-13 02:44:31.395439
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    test_host = Host()

# Generated at 2022-06-13 02:44:41.576860
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # Test case 1: test a dragonflybsd 8.3 RELEASE
    module = AnsibleModule(argument_spec=dict())
    d = Distribution(module=module)
    # set os.uname to return something that looks like dragonflybsd
    os.uname = Mock(return_value=['2.6.32-279.el6.x86_64', 'localhost.localdomain', '2.6.32-279.el6.x86_64', '#1 SMP Tue Jun 18 16:35:19 UTC 2013', 'x86_64'])
    # set platform.release to return something that looks like 8.3 RELEASE
    platform.release = Mock(return_value='8.3-RELEASE')

# Generated at 2022-06-13 02:44:52.215117
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():

    distributionFiles = DistributionFiles()
    distributionFiles.module = MagicMock()
    distributionFiles.module.get_bin_path.return_value = 'echo 1.2.3'
    collected_facts = {}

# Generated at 2022-06-13 02:45:01.954352
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():

    distro = get_distribution()
    # THIS IS ONLY FOR TESTING
    # TODO: make it a mock
    if distro.lower() != 'mandriva':
        import platform
        if 'centos' in platform.platform().lower():
            distro = 'mandriva'
        else:
            raise Exception("Mandriva test can only be run on a Mandriva or CentOS host")

    # create a DistributionFiles object
    distro_files = DistributionFiles()

    # create a CollectedFacts object
    collected_facts = CollectedFacts()

    # create a test /etc/mandriva-release file
    mandriva_release_file_path = 'tests/unittests/etc_mandriva-release'

# Generated at 2022-06-13 02:45:05.773697
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    # Tests for method parse_distribution_file_ClearLinux
    # Returns a dict of distribution facts from a clearlinux /etc/os-release file

    # FIXME: implement
    pass

# Generated at 2022-06-13 02:45:46.048929
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector.distribution import DistributionFiles

    distribution_files = DistributionFiles()

    module = AnsibleModule({})
    distribution_files.init_module(module)


# Generated at 2022-06-13 02:45:57.840589
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    x = DistributionFiles(None)
    # test for basic case
    (dist, release) = ('flatcar', 'beta')
    parsed_data = {'distribution_release': 'beta'}
    test_content = "Ver:    %s %s\nGROUP=%s" % (dist, release, release)
    res = x.parse_distribution_file_Flatcar(dist, test_content, '/etc/os-release', {})

    assert res[0]  is True
    assert res[1]  == parsed_data

    # test for invalid case
    (dist, release) = ('coreos', 'beta')
    test_content = "Ver:    %s %s\nGROUP=%s" % (dist, release, release)

# Generated at 2022-06-13 02:46:09.343945
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    dfs = DistributionFiles()
    
    fact_file_name = 'NA'

# Generated at 2022-06-13 02:46:21.095163
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    distro_file_name = "ClearLinux"

# Generated at 2022-06-13 02:46:29.836446
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    try:
        df = DistributionFiles({}, {}, {}, {})
    except:
        df = DistributionFiles()

    assert df.parse_distribution_file_Amazon('Amazon', 'Amazon Linux release 2 (Karoo)', '/etc/os-release', {}) == (True, {'distribution': 'Amazon', 'distribution_version': '2'})
    assert df.parse_distribution_file_Amazon('Amazon', 'Amazon Linux AMI release 2013.09', '/etc/system-release', {}) == (True, {'distribution': 'Amazon', 'distribution_version': '2013.09'})


# Generated at 2022-06-13 02:46:37.804289
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    module = MagicMock()
    test_module = Distribution(module)
    # A file containing the output of the command /usr/bin/oslevel
    out = """6.1.6.0"""
    module.run_command.return_value = (0, out, '')
    assert test_module.get_distribution_AIX() == {'distribution_major_version': '6',
                                                  'distribution_version': '6.1',
                                                  'distribution_release': '1'}
    assert module.run_command.call_count == 1
    assert module.run_command.call_args == call('/usr/bin/oslevel')

# Generated at 2022-06-13 02:46:46.160202
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():

    # Setup mocked module and class
    module = AnsibleModuleMock()
    distro_files = DistributionFiles(module)

    # Unit under test
    name = 'ClearLinux'
    path = 'test_path'
    data = 'NAME="Clear Linux"'
    collected_facts = {'distribution_release': 'NA'}
    ret, ret_facts = distro_files.parse_distribution_file_ClearLinux(name, data, path, collected_facts)

    # Verify results
    assert ret is True
    assert ret_facts['distribution_release'] == 'NA'
    assert ret_facts['distribution'] == 'Clear Linux'

# Generated at 2022-06-13 02:46:51.143363
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    from ansible.module_utils.facts import Distribution
    distribution = Distribution(None)
    distribution_HPUX = distribution.get_distribution_HPUX()
    assert distribution_HPUX == {'distribution_version': 'B.11.31', 'distribution_release': '178934'}



# Generated at 2022-06-13 02:47:01.370311
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    collected_facts = {'distribution_version': 'NA'}
    dist_files = DistributionFiles({})
    name = 'NA'

# Generated at 2022-06-13 02:47:10.996534
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # test for case in which /etc/os-release
    path = '/etc/os-release'
    # test for case in which /etc/system-release exits
    path2 = '/etc/system-release'
    # test for case in which /etc/system-release doesn't exit
    path3 = '/usr/bin'
    test_data = '''
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
'''
    test_data2 = '''
2
'''
    df = DistributionFiles()
    # test for case in which /etc/os-release exits
    ret = df.parse_distribution_file_Amazon('Amazon', test_data, path, {})
    assert ret[0] is True

# Generated at 2022-06-13 02:48:07.735827
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    data = distribution.get_distribution_Darwin()
    assert data['distribution'] == "MacOSX"
    assert "/usr/bin/sw_vers -productVersion" in data['ansible_facts']['ansible_system_vendor']['cmdline']

# Generated at 2022-06-13 02:48:12.939058
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    """
    Test for method get_distribution_OpenBSD of class Distribution
    """
    module = ansible.module_utils.basic.Basic()
    # popen occurs in distribution.py
    distro = Distribution(module)
    distro_openbsd = distro.get_distribution_OpenBSD()
    expected = {}
    expected['distribution_version'] = platform.release()
    rc, out, dummy = distro.module.run_command("/sbin/sysctl -n kern.version")
    match = re.match(r'OpenBSD\s[0-9]+.[0-9]+-(\S+)\s.*', out)
    if match:
        expected['distribution_release'] = match.groups()[0]
    else:
        expected['distribution_release'] = 'release'

# Generated at 2022-06-13 02:48:17.024727
# Unit test for function get_uname
def test_get_uname():
    assert get_uname('python3 -c "import ansible.module_utils.common.sys_info as sys_info; \
        (rc, out, err) = sys_info.get_uname(None, flags=`-v`); print(out)"')



# Generated at 2022-06-13 02:48:28.285352
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    # The following are examples of /etc/release data that the method has been tested with
    # SmartOS 12.5.1 20121005: HEAD illumos c0538f0b8a i86pc i386 i86pc Solaris
    # IlluminOS illumos-745eac6d  illumos-74c8cc0f  illumos-6d7e6aa59b  illumos-881257df  i86pc  i386   i86pc Solaris

    # Set up the args required by the method get_distribution_SunOS
    module = argparse.Namespace()
    module.run_command = FakeRunCommand
    module.params = {}
    # Each call to run_command will return a different output
    # For example: 'uname -a' will return 'SunOS localhost 5.11 11.4.0.

# Generated at 2022-06-13 02:48:34.126092
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )

    obj = Distribution(module)

    rc, out, err = module.run_command("/sbin/sysctl -n kern.version")
    obj.get_distribution_DragonFly()



# Generated at 2022-06-13 02:48:42.234463
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    data = """
    NAME=CoreOS
    ID=coreos
    VERSION=1031.4.0
    VERSION_ID=1031.4.0
    BUILD_ID=
    PRETTY_NAME="CoreOS 1031.4.0 (Andrew, alpha)"
    ANSI_COLOR="38;5;75"
    HOME_URL="https://coreos.com/"
    BUG_REPORT_URL="https://issues.core-os.net/"
    COREOS_BOARD=amd64-usr
    """
    df = DistributionFiles()
    parse_distribution_file_Coreos = df.parse_distribution_file_Coreos
    parsed_dist_file = parse_distribution_file_Coreos('Coreos', data, 'path', {})

# Generated at 2022-06-13 02:48:53.351613
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    name = 'Slackware'
    path = '/etc/slackware-version'
    dist_file_facts = {}
    dist_file_facts['distribution_file_path'] = path
    dist_file_facts['distribution_file_variety'] = name

    dist_files_inst = DistributionFiles()

    file_content = 'Slackware 12.0.1\n'
    parsed_dist_file_facts = dist_files_inst.parse_distribution_file_Slackware(name, file_content, path, dist_file_facts)
    assert parsed_dist_file_facts == (True, {'distribution': 'Slackware', 'distribution_version': '12.0.1'})

    file_content = 'Slackware noosfero\n'
    parsed_dist_file_facts

# Generated at 2022-06-13 02:49:00.211425
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    # Input data to the method
    name = 'NA'
    data = 'NAME="openSUSE Tumbleweed"\n'
    path = '/etc/os-release'
    collected_facts = {'distribution_version': 'NA'}
    # Expected result from the method
    expected_result = True, {'distribution': 'openSUSE Tumbleweed'}
    # Actual result from the method
    dist_file_parsing = DistributionFiles()
    actual_result = dist_file_parsing.parse_distribution_file_NA(name, data, path, collected_facts)
    # Assert expected result == actual result
    assert expected_result == actual_result, "Expected {0}, got {1}".format(expected_result, actual_result)



# Generated at 2022-06-13 02:49:11.193502
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    """
    Test against fixtures that get_distribution_Darwin()
    should return a dictionary with 'distribution' = MacOSX and
    'distribution_version' = 10.10.5
    """
    mac_fixture = [('sw_vers.stdout', 'ProductName:    Mac OS X\nProductVersion: 10.10.5\nBuildVersion:   14F27\n'),
                   ('sw_vers.rc', 0)]
    mac_ansible_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    mac_module_mock = AnsibleModule(mac_ansible_module, mac_fixture)
    mac_distribution_method_instance = Distribution(mac_module_mock)
    mac_distribution_method_facts = mac_distribution_method_instance.get_

# Generated at 2022-06-13 02:49:22.182088
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = MockOS(distro='NetBSD', version_detail=(7, 2, 1))
    distribution_obj = Distribution(module)
    expected_output = {
        'distribution_release': '7.2.1',
        'distribution_major_version': '7',
        'distribution_version': '7.2'
    }
    os_version = "7.2.1 (GENERIC) #0: 2019-04-08 20:58:00 UTC"
    collect_uname = "NetBSD 7.2 (GENERIC)\n"