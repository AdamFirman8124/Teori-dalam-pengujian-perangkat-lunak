

# Generated at 2022-06-13 02:41:36.032078
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    distfiles_obj = DistributionFiles()
    assert distfiles_obj.parse_distribution_file_Slackware('Slackware', 'foo Slackware bar', '/path', {}) == (True, {'distribution': 'Slackware', 'distribution_version': '14.2'})
    assert distfiles_obj.parse_distribution_file_Slackware('Slackware', 'foo Slackware bar Slackware 13.0', '/path', {}) == (True, {'distribution': 'Slackware', 'distribution_version': '13.0'})
    assert distfiles_obj.parse_distribution_file_Slackware('Slackware', 'foo Slackware bar Slackware Current', '/path', {}) == (True, {'distribution': 'Slackware', 'distribution_version': 'Current'})
    assert dist

# Generated at 2022-06-13 02:41:46.031744
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # Test platform.system() returns 'Darwin'
    platform.system.return_value = 'Darwin'
    # Test 'Darwin' is in systems implemented
    Distribution.systems_implemented = ('AIX', 'HP-UX', 'Darwin', 'FreeBSD', 'OpenBSD', 'SunOS', 'DragonFly', 'NetBSD')
    # Test platform.release() returns '11.1-RELEASE-p1'.
    platform.release.return_value = '11.1-RELEASE-p1'
    # Test 'TrueOS' in platform.version()
    platform.version.return_value = '11.1-STABLE-p1 TrueOS'
    # Test rc returns 0
    # Test out returns '11.1-RELEASE-p1'
    # Test err returns ''

# Generated at 2022-06-13 02:41:54.940227
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    class FailedModuleExecution(Exception):
        pass

    class Module:
        def __init__(self):
            self.run_command_error = False
            self.run_command_no_data = False
            self.run_command_no_version = False
            self.run_command_no_release = False
            self.run_command_no_major_version = False

        def run_command(self, command, use_unsafe_shell=False):
            if self.run_command_error is True:
                return 1, "", "some error"
            if self.run_command_no_data is True:
                return 0, "", ""
            if self.run_command_no_version is True:
                return 0, "Solaris 10 10/09 s10x_u8wos_08a X86",

# Generated at 2022-06-13 02:42:02.007872
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    result = {
        u'distribution': u'Mandriva',
        u'distribution_version': u'2014.0',
        u'distribution_release': u'Cooker'
    }
    with open('/tmp/test_DistributionFiles_parse_distribution_file_Mandriva', 'w') as f:
        f.write('# /etc/lsb-release: distributed by \n')
        f.write('DISTRIB_ID=MandrivaLinux\n')
        f.write('DISTRIB_RELEASE=2014.0\n')
        f.write('DISTRIB_CODENAME=Cooker\n')
        f.write('DISTRIB_DESCRIPTION="Mandriva Linux 2014.0"\n')
    dist_file = DistributionFiles(mock.Mock())
   

# Generated at 2022-06-13 02:42:09.820756
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    # Tests for method get_distribution_SunOS of class Distribution
    # TODO: deal with `platform.system()` returning different things or not
    #       being available on different platforms
    module = AnsibleModule(argument_spec={})
    facts = Distribution(module).get_distribution_SunOS()
    assert facts == {'distribution': 'Solaris',
                     'distribution_major_version': '9',
                     'distribution_release': 'Oracle Solaris 9 4/13 s9x_u8wos_08a SPARC',
                     'distribution_version': '9'}

    _platform_release.cache_clear()
    _platform_version.cache_clear()
    facts = Distribution(module).get_distribution_SunOS()

# Generated at 2022-06-13 02:42:22.702717
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    distribution_files = DistributionFiles()

    # No 'Slackware' in data
    name = 'Slackware'
    data = 'wrong data'
    path = '/etc/slackware-version'
    collected_facts = distribution_files.get_distribution_facts('NA')
    distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    # Data with 'Slackware'
    name = 'Slackware'

# Generated at 2022-06-13 02:42:25.251776
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    assert Distribution(None).get_distribution_SunOS() == {'distribution': 'SmartOS', 'distribution_release': 'OpenIndiana Development oi_151a8'}

# Generated at 2022-06-13 02:42:32.754157
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    dd = DistributionFiles()
    dd.module = AnsibleModule(argument_spec={})
    name = 'Slackware'
    path = '/etc/slackware-version'
    data = 'Slackware 14.1'
    parsed_dist_file, parsed_dist_file_facts = dd.parse_distribution_file_Slackware(name, data, path)
    assert parsed_dist_file
    assert parsed_dist_file_facts == {'distribution': 'Slackware', 'distribution_version': '14.1'}
# Unit tests for method parse_distribution_file_Amazon of class DistributionFiles

# Generated at 2022-06-13 02:42:41.801722
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    distribution_file_Slackware = DistributionFiles()
    name = 'Slackware'
    path = ""
    collected_facts = {'distribution_file_facts': {}}
    data_set = [
        ("Slackware 1.1.1\n", {'distribution_file_parsed': True, 'distribution': name, 'distribution_version': '1.1.1'}),
        ("No Slackware in this\n", {'distribution_file_parsed': False, 'distribution': None, 'distribution_version': 'NA'})
    ]
    for data, expected_result in data_set:
        parsed_dist_file, parsed_dist_file_facts = distribution_file_Slackware.parse_distribution_file_Slackware(name, data, path, collected_facts)

# Generated at 2022-06-13 02:42:43.790568
# Unit test for method get_distribution_FreeBSD of class Distribution
def test_Distribution_get_distribution_FreeBSD():
    assert Distribution(None).get_distribution_FreeBSD() == {
        'distribution_release': '12.0-CURRENT'
    }

# Generated at 2022-06-13 02:44:14.474603
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    facts = DistributionFiles({})
    assert(facts.parse_distribution_file_Flatcar("flatcar", "GROUP=alpha\n", "/etc/os-release", {}) == (True, {'distribution_release': 'alpha'}))

# Generated at 2022-06-13 02:44:24.688578
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Prepare the test object
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False
    )
    df = DistributionFiles(module)
    collected_facts = {}

    # Test case 1
    name = 'Amazon'
    path = '/etc/os-release'
    data = 'NAME="Amazon Linux AMI" \
VERSION="2" \
ID="amzn" \
ID_LIKE="centos rhel fedora" \
VERSION_ID="2017.09" \
PRETTY_NAME="Amazon Linux AMI 2017.09" \
ANSI_COLOR="0;33" \
CPE_NAME="cpe:/o:amazon:linux:2017.09:ga" \
HOME_URL="http://aws.amazon.com/amazon-linux-ami/" \
'
    expected_

# Generated at 2022-06-13 02:44:36.033021
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    from ansible.module_utils.facts import Distribution

    # Mock out platform-related functions
    def mock_platform_system(self):
        return 'SunOS'

    def mock_platform_release(self):
        return '5.11'

    def mock_uname(self, module=None, flags=['-r']):
        return '5.11'

    def mock_get_file_content_release(self, _file):
        return '''\
            OpenIndiana Development oi_151a8 X86
              Copyright 2010 Oracle and/or its affiliates.  All rights reserved.
              Assembled 20 September 2011
            '''


# Generated at 2022-06-13 02:44:43.682912
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    module = AnsibleModule(argument_spec={})
    data_flatcar_os_release = 'NAME=Flatcar Container Linux \nID=flatcar \nVERSION_ID=2611.3.0 \nBUILD_ID=2018-03-27-1636 \nPRETTY_NAME="Flatcar Container Linux 2611.3.0 (2018-03-27-1636)" \nANSI_COLOR="33m" \nHOME_URL="https://www.flatcar-linux.org/" \nBUG_REPORT_URL="https://github.com/flatcar-linux/flatcar-linux/issues" \nCONTAINER="oci" \nLOGO=container-linux \n'

    dist = DistributionFiles()

# Generated at 2022-06-13 02:44:49.493753
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # test data
    name = 'Amazon'
    data = 'ID=amazon\nPRETTY_NAME="Amazon Linux 2"\nVERSION_ID="2"\n'
    path = '/etc/os-release'
    collected_facts = {'distribution': 'AmazonLinux', 'distribution_release': 'NA'}

    distributionFiles = DistributionFiles()
    distributionFile_parse_success, distributionFile_facts = distributionFiles.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert distributionFile_facts['distribution_major_version'] == 2
    assert distributionFile_parse_success is True
    assert distributionFile_facts['distribution'] == 'Amazon'



# Generated at 2022-06-13 02:44:52.493254
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    netbsd_facts = distribution.get_distribution_NetBSD()
    print(netbsd_facts)
    assert netbsd_facts['distribution'] == 'NetBSD'
    assert netbsd_facts['distribution_release'] == 'NetBSD'
    assert netbsd_facts['distribution_version'] == 'NetBSD'

# Generated at 2022-06-13 02:44:56.951578
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    assert Distribution().get_distribution_AIX() == {'distribution_major_version': '6', 'distribution_version': '6.1', 'distribution': 'AIX'}



# Generated at 2022-06-13 02:45:07.626927
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    # test case when "Clear Linux" exists in NAME
    name = "clearlinux"
    data = 'NAME="Clear Linux"'
    path = "path"
    collected_facts = {'test': 'test'}
    dfile = DistributionFiles()
    parsed, clear_facts = dfile.parse_distribution_file_ClearLinux(name, data, path, collected_facts)
    assert parsed is True
    assert clear_facts['distribution'] == 'Clear Linux'
    assert clear_facts['distribution_major_version'] is None
    assert clear_facts['distribution_version'] is None
    assert clear_facts['distribution_release'] is None

    # test case of wrong name
    name = "clearlinux"
    data = 'NAME="Clear Linux"'
    path = "path"

# Generated at 2022-06-13 02:45:10.895254
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = AnsibleModuleMock()
    module.run_command.return_value = [0, 'HPUX_OE 11.31.08.07.335898', '']
    d = Distribution(module=module)
    assert d.get_distribution_HPUX() == {'distribution_version': 'B.11','distribution_release': '335898'}


# Generated at 2022-06-13 02:45:16.767295
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    # Test Distribution by mocking get_file_content from fs.py, mocking run_command from module_utils and checking
    # the values of output variables.
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.check_mode = False
            self.fail_json = False
            self.exit_json = False
            self.os = None
            self.run_command_results = []
            self.run_command_calls = []
            self.run_command_checked = []

        def run_command(self, cmd, check_rc=True, use_unsafe_shell=False):
            logger.debug('run_command: cmd=%s, check_rc=%s, use_unsafe_shell=%s', cmd, check_rc, use_unsafe_shell)


# Generated at 2022-06-13 02:46:20.638942
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.distribution import Distribution

    dist = Distribution(module=None)
    expected = {'distribution': 'Oracle Solaris', 'distribution_version': '11.4',
                'distribution_release': 'Oracle Solaris 11.4', 'distribution_major_version': '11'}

    out = to_bytes(u"""                      Oracle Solaris 11.4 S11s_u7wos_17b SPARC
                                Copyright (c) 1983, 2018, Oracle and/or its affiliates.
                                            All rights reserved.
                                Assembled 12 October 2018
                """, encoding='ascii')


# Generated at 2022-06-13 02:46:31.658969
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    mod = AnsibleModuleMock()
    dist = DistributionFiles(mod)
    # Setup the mock data
    data = '''
        GROUP=stable
        VERSION=1910.3.1
        VERSION_ID=1910.3.1
        VERSION_CODENAME="CoreOS Container Linux by CoreOS stable release 1910.3.1"
        ID=container-linux
        ID_LIKE=coreos
        ANSI_COLOR="38;5;75"
        NAME="Container Linux by CoreOS"
        HOME_URL="https://coreos.com/os/docs/latest"
        BUG_REPORT_URL="https://issues.core-os.net/browse/CL"
    '''
    collected_facts = {'distribution_release': 'NA'}

# Generated at 2022-06-13 02:46:40.418311
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    test_module = type('TestModule', (object,), {})()

    test_mock = type('test_mock', (object,), {})()
    test_mock.run_command.return_value = (0, '', None)
    test_mock.file_exists.return_value = True

    test_module.run_command = test_mock.run_command
    test_module.file_exists = test_mock.file_exists

    test_mock.get_file_content = MagicMock(return_value='Solaris 10 10/09 s10x_u8wos_08a X86')
    test_mock.get_uname = MagicMock(return_value='SunOS 5.10 i86pc i386 i86pc')
    test_module.get_file

# Generated at 2022-06-13 02:46:41.084567
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    assert True


# Generated at 2022-06-13 02:46:49.458218
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    import copy
    import sys

    # ansible_distribution fact are in the format:
    #    "{distribution} {distribution_version} (oracle|ojun|osol)"
    # ansible_distribution_release fact are in the format:
    #    "<major_version>.<minor_version>{-PRERELEASE}"
    #
    # Some of the asserts below only checks for the major and minor version
    # because the fact contains more information (which are implementation
    # detailled) that can be subject to changes.
    #
    # IMPORTANT: run the test in a fresh venv (virtualenv) to avoid cache issues
    #

    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 02:46:56.477498
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = ansible_modulestest._load_ansible_modules()[0]()
    distro = Distribution(module)
    expected_results = {'distribution': 'SmartOS',
                        'distribution_release': 'SmartOS joyent_20120312T043021Z',
                        'distribution_version': '20120312T043021Z'}
    test_results = distro.get_distribution_SunOS()
    assert expected_results == test_results

# Generated at 2022-06-13 02:47:01.160303
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    distfiles = DistributionFiles()
    parsed_suse, suse_facts = distfiles.parse_distribution_file_SUSE('Tumbleweed', 'openSUSE Tumbleweed', '/etc/os-release', {})
    assert parsed_suse
    assert suse_facts['distribution'] == 'openSUSE Tumbleweed'
    assert suse_facts['distribution_release'] == 'Tumbleweed'



# Generated at 2022-06-13 02:47:10.876246
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    # Create an instance of class DistributionFiles
    disf = DistributionFiles()

    # test1: return empty dict, when no dist files are present
    files = []
    dist_files = ['1.txt']
    parsed_files = {}
    facts = {'distribution': 'NA', 'distribution_version': 'NA', 'distribution_major_version': 'NA', 'distribution_release': 'NA'}
    facts = disf.process_dist_files(files, dist_files, parsed_files, facts)
    assert facts == {}, "FAIL: test1"

    # test2: return empty dict, when no dist files are present
    files = ['2.txt']
    dist_files = []
    parsed_files = {}

# Generated at 2022-06-13 02:47:18.071837
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    def run_commands(commands):
        stdout = ''
        stderr = ''
        results = {}
        for cmd in commands:
            if 'out' in commands[cmd]:
                stdout += commands[cmd]['out'] + '\n'
            if 'err' in commands[cmd]:
                stderr += commands[cmd]['err'] + '\n'
            if 'rc' in commands[cmd]:
                results[cmd] = commands[cmd]['rc']
            else:
                results[cmd] = 0
        return results, stdout, stderr

    def get_file_content(files):
        out = ''
        if isinstance(files, str):
            files = [files]
        for filename in files:
            if 'release' in filename and 'SmartOS' in filename:
                out

# Generated at 2022-06-13 02:47:25.765989
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():

    # redefine get_file_content method, return constant value
    def get_file_content_Mock(self, file):
        return ""

    # redefine run_command method, return constant value
    def run_command_Mock(self, command):
        return 0, "", ""

    # patch, we do not want to call get_file_content or run_command
    with patch.object(Distribution, 'get_file_content', get_file_content_Mock):
        with patch.object(Distribution, 'run_command', run_command_Mock):

            # create Distribution object
            distribution_obj = Distribution("Some Module")

            # call method get_distribution_AIX
            attrs = distribution_obj.get_distribution_AIX()

            # make sure result is dictionary

# Generated at 2022-06-13 02:48:22.297550
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    distribution_file = DistributionFiles()
    assert distribution_file.parse_distribution_file_ClearLinux('Clear Linux', 'NAME="Clear Linux"', 'test_path', {})[1] == {'distribution': 'Clear Linux'}
    assert distribution_file.parse_distribution_file_ClearLinux('Clear Linux', 'VERSION_ID=30150', 'test_path', {})[1] == {'distribution_major_version': '30150', 'distribution_version': '30150'}
    assert distribution_file.parse_distribution_file_ClearLinux('Clear Linux', 'ID=clear-linux-os', 'test_path', {})[1] == {'distribution_release': 'clear-linux-os'}

# Generated at 2022-06-13 02:48:25.239662
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    assert Distribution().get_distribution_OpenBSD() == {'distribution_version': 'amd64-6.6', 'distribution_release': 'GENERIC.MP'}


# Generated at 2022-06-13 02:48:37.285751
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    assert Distribution.get_distribution_SunOS({'file': {'exists': True, 'read': True}, 'uname': {'-v': '0'}}) == {'distribution': 'SmartOS', 'distribution_version': '0', 'distribution_release': 'SmartOS'}
    assert Distribution.get_distribution_SunOS({'file': {'/etc/release': 'OpenIndiana Development oi_148 2017-12-06', 'exists': True, 'read': True}, 'uname': {'-v': '0'}}) == {'distribution': 'OpenIndiana', 'distribution_version': 'oi_148', 'distribution_release': 'OpenIndiana Development oi_148 2017-12-06'}

# Generated at 2022-06-13 02:48:48.833617
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    distfiles_obj = DistributionFiles()
    facts_dict = {}
    distfiles_obj.process_dist_files(facts_dict)
    result_desired = {
        'distribution_file_path': '/etc/os-release',
        'distribution_file_variety': 'RedHat',
        'distribution_file_parsed': False,
        'distribution_file_variety_id': 'redhat',
    }
    assert result_desired['distribution_file_path'] == facts_dict['distribution_file_path']
    assert result_desired['distribution_file_variety'] == facts_dict['distribution_file_variety']
    assert result_desired['distribution_file_parsed'] == facts_dict['distribution_file_parsed']
    assert result_

# Generated at 2022-06-13 02:48:52.756106
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    module = None
    dist = Distribution(module)

    expected_aix_facts = {'distribution_major_version': '7'}
    aix_facts = dist.get_distribution_AIX()
    assert aix_facts == expected_aix_facts


# Generated at 2022-06-13 02:48:54.906487
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    # XXX: not yet implemented
    # XXX: Design this to use Mock, not random data
    # XXX: Handle multiple variations of SUSE
    pass


# Generated at 2022-06-13 02:48:59.628757
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    files = DistributionFiles()
    assert files.parse_distribution_file_Amazon('Amazon', '/etc/os-release contents', '/etc/os-release', {}) == \
            (True, {'distribution': 'Amazon', 'distribution_version': '2', 'distribution_minor_version': '0', 'distribution_major_version': '2'})


# Generated at 2022-06-13 02:49:09.052156
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    facts = Distribution()
    facts.module = FakeModule()
    facts.module.run_command = run_command_mock({
        "/usr/bin/sw_vers -productVersion": (0, "1.2", "")
    })

    # This is the output we expect.
    expected_dict = {
        "distribution": "MacOSX",
        "distribution_major_version": "1",
        "distribution_version": "1.2"
    }

    # invoke the method we are testing.
    actual_dict = facts.get_distribution_Darwin()
    assert_equal(actual_dict, expected_dict)


# Generated at 2022-06-13 02:49:10.020295
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    pass



# Generated at 2022-06-13 02:49:16.657481
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    this = DistributionFiles()

    dd = "openSUSE 13.1 (Bottle)"
    assert this.parse_distribution_file_SUSE("openSUSE 13.1 (Bottle)", dd, "", {})[1]['distribution_release'] == 'Bottle'

    dd = "openSUSE 13.1 (Bottle) (x86_64)\nVERSION = 13.1\nCODENAME = Bottle\n"
    assert this.parse_distribution_file_SUSE("openSUSE 13.1 (Bottle) (x86_64)", dd, "", {})[1]['distribution_release'] == 'Bottle'

    dd = "openSUSE 13.2 (Harlequin) (x86_64)\nVERSION = 13.2\nCODENAME = Harlequin\n"

# Generated at 2022-06-13 02:50:16.714031
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    # pylint: disable = redefined-outer-name, too-many-locals, unused-variable
    distribution = Distribution(None)
    OS_FAMILY_MAP = distribution.OS_FAMILY_MAP
    OS_FAMILY = distribution.OS_FAMILY
    get_distribution_AIX = distribution.get_distribution_AIX
    get_distribution_HPUX = distribution.get_distribution_HPUX
    get_distribution_Darwin = distribution.get_distribution_Darwin
    get_distribution_FreeBSD = distribution.get_distribution_FreeBSD
    get_distribution_OpenBSD = distribution.get_distribution_OpenBSD
    get_distribution_DragonFly = distribution.get_distribution_DragonFly
    get_distribution_NetBSD = distribution.get_distribution

# Generated at 2022-06-13 02:50:24.451183
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = AnsibleModule(argument_spec=dict())
    test_dist = Distribution(module)

    rc, out, err = module.run_command("/usr/sbin/swlist |egrep 'HPUX.*OE.*[AB].[0-9]+\.[0-9]+'", use_unsafe_shell=True)
    data = re.search(r'HPUX.*OE.*([AB].[0-9]+\.[0-9]+)\.([0-9]+).*', out)
    if data:
        hpux_version = data.groups()[0]
        hpux_release = data.groups()[1]
    else:
        hpux_version = None
        hpux_release = None

    hpux_facts = test_dist.get_distribution_HPUX()
    assert hp

# Generated at 2022-06-13 02:50:30.177827
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    from ansible.module_utils.facts.system.distribution import Distribution
    import platform
    module = None
    distribution_obj = Distribution(module)
    platform.system = lambda : return_value_mock('SunOS')
    platform.release = lambda : return_value_mock("5.12 NexentaOS_131a8")
    platform.version = lambda : return_value_mock("Generic_142901-17 i86pc i386 i86pc Solaris")
    get_file_content = lambda x: return_value_mock("Oracle Solaris 11.4 oi_151.1.18.0.0.151.0.0 SPARCCA x86  Copyright (c) 1983, 2018, Oracle and/or its affiliates. All rights reserved.")
    get_uname = lambda x, y: return_value_mock

# Generated at 2022-06-13 02:50:33.137939
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Asserts "Amazon" distribution parsing
    # Test with single distribution_file
    # Test with distribution_files

    # Test no distribution parsing
    # Test with single distribution_file
    # Test with distribution_files

    # Test requires asserts
    pass

# Generated at 2022-06-13 02:50:36.353890
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    assert Distribution(AnsibleModuleMock()).get_distribution_AIX() == {'distribution_major_version': '6', 'distribution_version': '6.1.10.0'}


# Generated at 2022-06-13 02:50:46.733295
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    distribution_files = DistributionFiles()
    # test with SLES 11 sp4
    sles_11_sp4 = """
        openSUSE 11.4 (i586)
        VERSION = 11.4
        CODENAME = Celadon
        """
    _result, suse_11_sp4_facts = distribution_files.parse_distribution_file_SUSE('openSUSE', sles_11_sp4, '/etc/SuSE-release', {})
    assert suse_11_sp4_facts == {'distribution': 'openSUSE', 'distribution_release': 'Celadon'}
    # test with SLES 12 sp1