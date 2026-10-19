

# Generated at 2022-06-13 02:41:55.697290
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    """Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles."""
    # Init
    openwrt_facts = dict()
    collected_facts = dict()
    distribution_files = DistributionFiles()
    name = 'OpenWrt'
    data = """NAME="OpenWrt"
DISTRIB_ID=OpenWrt
DISTRIB_RELEASE=18.06.2
DISTRIB_REVISION=r7258-5eb055306f
DISTRIB_CODENAME=reboot
DISTRIB_TARGET=ramips/mt7620
DISTRIB_DESCRIPTION="OpenWrt 18.06.2 r7258-5eb055306f"
DISTRIB_TAINTS=no-all maximize-coverage"""
    path = 'path'
    # Assert
    b, f

# Generated at 2022-06-13 02:42:00.466929
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    assert DistributionFiles.parse_distribution_file_Amazon(DistributionFiles(), 'Amazon', 'Amazon Linux AMI release 2016.03',
                                                             '', {'distribution_version': 'NA'}
                                                             ) == (True, {'distribution_version': '2016.03',
                                                                          'distribution_major_version': '2016',
                                                                          'distribution_minor_version': '3',
                                                                          'distribution': 'Amazon'})


# Generated at 2022-06-13 02:42:08.282845
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    dist_files = DistributionFiles()
    collected_facts = {'distribution': 'NA', 'distribution_major_version': 'NA', 'distribution_version': 'NA', 'distribution_release': 'NA'}
    facts = {}
    name = 'Debian'
    path = '/etc/os-release'
    data = 'NAME=Debian\nVERSION="8 (jessie)"\nID=debian\nID_LIKE=debian\nPRETTY_NAME="Debian GNU/Linux 8 (jessie)"\nVERSION_ID="8"\nHOME_URL="http://www.debian.org/"\nSUPPORT_URL="http://www.debian.org/support/"\nBUG_REPORT_URL="https://bugs.debian.org/"\n\n'
    parsed_dist_file, parsed_dist

# Generated at 2022-06-13 02:42:19.819458
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    # test_data array is declared here
    collected_facts = {}
    collected_facts['distribution'] = 'NA'
    collected_facts['distribution_release'] = 'NA'
    collected_facts['distribution_major_version'] = 'NA'
    collected_facts['distribution_version'] = 'NA'

# Generated at 2022-06-13 02:42:31.989454
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Amazon Linux 1
    file_data = 'NAME="Amazon Linux AMI"\nVERSION="2018.03"\nID="amzn"\nID_LIKE="rhel fedora"\nVERSION_ID="2018.03"\nPRETTY_NAME="Amazon Linux AMI 2018.03"'
    (parsed_dist_file, parsed_dist_file_facts) = DistributionFiles.parse_distribution_file_Amazon(file_data)
    assert parsed_dist_file is True
    assert parsed_dist_file_facts == {'distribution': 'Amazon'}

    # Amazon Linux 2

# Generated at 2022-06-13 02:42:37.649865
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():

    import platform

    if platform.system() == 'Darwin':
        dist = Distribution(None)
        # macos release is named '10.14.5'
        assert dist.get_distribution_Darwin()['distribution_major_version'] == '10'


if __name__ == '__main__':
    # Unit test for method get_distribution_Darwin of class Distribution
    test_Distribution_get_distribution_Darwin()

# Generated at 2022-06-13 02:42:44.538458
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():

    def test_run_command(cmd):
        cmd = cmd.split()
        out = ""
        if cmd == ["/sbin/sysctl", "-n", "kern.version"]:
            out = "NetBSD 6.1.5 (GENERIC) #0: Sat Nov  3 00:48:03 UTC 2012  root@netbsd.example.com:/usr/obj/sys/arch/amd64/compile/GENERIC"
        return 0, out, None

    def test_get_uname(module, flags):
        flags = ''.join(flags)
        uname = ""
        # Uname -r;
        if flags == "-r":
            uname = "6.1.5"
        # Uname -v;

# Generated at 2022-06-13 02:42:47.238982
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    fact = DistributionFiles()
    assert fact.parse_distribution_file_SUSE('suse','','','','','','','') == ()
test_DistributionFiles_parse_distribution_file_SUSE()
#Unit test for method parse_distribution_file_CentOS of class DistributionFiles

# Generated at 2022-06-13 02:42:47.914906
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    pass


# Generated at 2022-06-13 02:42:54.964586
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # Create module object
    module = AnsibleModule(argument_spec={})

    # Get Distribution instance
    distro = Distribution(module)

    # Call get_distribution_DragonFly method
    result = distro.get_distribution_DragonFly()

    # Check result
    assert type(result) == dict
    assert result.keys() == {'distribution_release'}
    assert type(result['distribution_release']) == str
    assert len(result['distribution_release']) > 0



# Generated at 2022-06-13 02:43:38.337196
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    global module
    global distribution
    module.run_command = MagicMock(return_value=(0, r"HPUX_OE_10_11_20170707.332067\5.11.20170707.332067", ""))
    hpux_facts = distribution.get_distribution_HPUX()
    assert hpux_facts['distribution_version'] == "B.11"
    assert hpux_facts['distribution_release'] == "20170707"


# Generated at 2022-06-13 02:43:50.362443
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    import platform
    import ansible.module_utils.facts.system.distribution as dist
    module = FakeModule()
    sunos = dist.Distribution(module)
    sunos.module.run_command = run_command_mock
    sunos.module.get_uname = get_uname_mock
    sunos.module.get_file_content = get_file_content_mock
    sunos.module.file_exists = _file_exists_mock
    sunos_facts = sunos.get_distribution_SunOS()
    if 'SmartOS' in platform.release():
        assert sunos_facts['distribution'] == 'SmartOS'
        assert sunos_facts['distribution_version'] == '17.4.0'
        assert sunos_facts['distribution_major_version']

# Generated at 2022-06-13 02:43:59.162275
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Preparation of test context
    module = AnsibleModuleTestUtils.get_ansible_module()
    args = {"data":"Amazon Linux release 2"}
    module.params.update(args)
    method = DistributionFiles(module, "Amazon", "/etc/some/file", "/etc/some/file", {}, {})
    # Assertion section
    name = "Amazon"
    data = "Amazon Linux release 2"
    path = "/etc/some/file"
    collected_facts = {}
    expected_parsed_dist_file = True
    expected_parsed_dist_file_facts = {'distribution': 'Amazon', 'distribution_version': '2'}

# Generated at 2022-06-13 02:44:00.385154
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    """
    Test for method get_distribution_HPUX of class Distribution
    """
    pass

# Generated at 2022-06-13 02:44:06.529135
# Unit test for function get_uname
def test_get_uname():
    try:
        uname = get_uname('Linux 4.15.0-1054-aws #59~16.04.1-Ubuntu SMP Tue May 5 14:16:00 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux')
        assert uname == 'Linux 4.15.0-1054-aws #59~16.04.1-Ubuntu SMP Tue May 5 14:16:00 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux'
    except:
        assert False


# Generated at 2022-06-13 02:44:13.450880
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    data = Distribution(module=None).get_distribution_NetBSD()
    assert 'distribution_major_version' in data and data['distribution_major_version'] == '8'
    assert 'distribution_release' in data and data['distribution_release'] == 'release'
    assert 'distribution_version' in data and data['distribution_version'] == '8.0'


# Generated at 2022-06-13 02:44:22.137059
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    class ModuleMock(object):
        def __init__(self):
            self.run_command = MagicMock(return_value=(0, '7.2', ''))

# Generated at 2022-06-13 02:44:31.954175
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    testCases = [
        {
            'name':     'Mandriva',
            'data':     """
                        NAME="Mandriva Linux"
                        VERSION="2010.1 (Official) - Spring"
                        ID="mandriva"
                        ID_LIKE="rpm mandrake mandriva"
                        """
        }
    ]

    for testCase in testCases:
        df = DistributionFiles()
        kwargs = {'name': 'Mandriva', 'data': testCase['data'], 'path': '', 'collected_facts': {},
                  'file_variety': testCase['name']}
        rc, out_facts = df.parse_distribution_file_Mandriva(**kwargs)
        assert rc == True
        assert out_facts['distribution'] == testCase['name']

# Generated at 2022-06-13 02:44:35.667765
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    distribution = Distribution(module=None)
    assert distribution.get_distribution_DragonFly() == {'distribution_release': '5.7.2-RELEASE'}


# Generated at 2022-06-13 02:44:39.399381
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    distro = Distribution(None)
    facts = distro.get_distribution_AIX()
    assert facts['distribution_version'] == '7.1'
    assert facts['distribution_major_version'] == '7'
    assert facts['distribution_release'] == '1'


# Generated at 2022-06-13 02:45:14.278792
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Instance of class DistributionFiles to test
    test_instance = DistributionFiles()
    # Facts already collected
    collected_facts = {}
    # File name
    name = 'Amazon'
    # File path
    path = '/etc/os-release'

    # Test with file that does not match Red Hat distribution

# Generated at 2022-06-13 02:45:24.614697
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():

    with tempfile.NamedTemporaryFile('w') as temp:
        class MockModule(object):
            params = {}

            def fail_json(self, msg):
                pass

            def get_bin_path(self, path):
                return "/bin/%s" % path

            def run_command(self, cmd):
                return 0, '#!/bin/bash\n', ''
        temp.write('NAME="Clear Linux"\nVERSION_ID="27600"\nID="clear-linux"\n')
        temp.flush()
        module = MockModule()
        facts_d = DistributionFiles(module)
        dist = 'clear-linux'
        data = get_file_content(temp.name)
        path = '/etc/os-release'
        collected_facts = {}
        distro_facts = facts_d

# Generated at 2022-06-13 02:45:28.446881
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    assert Distribution.get_distribution_OpenBSD(None) == {'distribution_version': '6.2', 'distribution_release': 'release'}

# Generated at 2022-06-13 02:45:36.005058
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    distribution_files = DistributionFiles({"distribution": 'Unknown'})
    parsed_data = "NAME=\"Ubuntu\"\nVERSION=\"12.04.1 LTS, Precise Pangolin\"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME=\"Ubuntu precise (12.04.1 LTS)\"\nVERSION_ID=\"12.04\"\n"
    parsed_data_pangolin = "NAME=\"Ubuntu\"\nVERSION=\"12.04.5 LTS, Precise Pangolin\"\nID=ubuntu\nID_LIKE=debian\nPRETTY_NAME=\"Ubuntu precise (12.04.5 LTS)\"\nVERSION_ID=\"12.04\"\n"

# Generated at 2022-06-13 02:45:45.861030
# Unit test for method get_distribution_FreeBSD of class Distribution
def test_Distribution_get_distribution_FreeBSD():
    from ansible.module_utils.facts.os.distribution import Distribution
    from ansible.module_utils.facts import ModuleFacts

    FAKE_DIST = '''11.2-RELEASE-p3'''
    FAKE_DIST_TRUEOS = '''12.0-CURRENT'''

    module = ModuleFacts(argument_spec={}, is_playbook=False)
    module.run_command.return_value = (0, FAKE_DIST, '')
    freebsd = Distribution(module)
    distribution_facts = freebsd.get_distribution_FreeBSD()
    assert distribution_facts['distribution_major_version'] == '11'
    assert distribution_facts['distribution_version'] == '11.2'

# Generated at 2022-06-13 02:45:57.607157
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    from ansible.module_utils.facts.collector import DistributionFiles
    from ansible.module_utils.facts.collector import CollectedFacts
    from ansible.module_utils.facts.collector import BaseFile
    from ansible.module_utils.facts.collector import ParseException

    file_name = "/etc/os-release"

# Generated at 2022-06-13 02:46:09.140229
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    # create an instance of class DistributionFiles
    dist_files = DistributionFiles(None)
    path = '/etc/os-release'
    # data contains "Debian" and "Raspbian"
    data = '''NAME="Raspbian GNU/Linux"
            VERSION_ID="9"
            VERSION="9 (stretch)"
            ID=raspbian
            ID_LIKE=debian
            HOME_URL="http://www.raspbian.org/"
            SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
            BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
            '''
    parsed_data, debian_facts = dist_files.parse_distribution_file_Debian('Debian', data, path, {})

# Generated at 2022-06-13 02:46:14.205394
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    dist = Distribution(FakeModule())
    result = dist.get_distribution_NetBSD()
    assert result
    if result['distribution_release'] == '7.1_STABLE':
        assert result['distribution_major_version'] == '7'
        assert result['distribution_version'] == '7.1'
    else:
        assert result['distribution_release'] == result['distribution_version']
        assert result['distribution_major_version'] == result['distribution_version'].split('.')[0]



# Generated at 2022-06-13 02:46:24.614072
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    def test_Distribution_get_distribution_SunOS_case1():
        # If 'Solaris' in data
        # If uname_r will contain 5.10, for solaris 11 it will have 5.11
        module = Mock()
        module.run_command = Mock(return_value=(0, '5.10', ''))
        # Case 1.1: 'Oracle Solaris' in data
        data = 'Oracle Solaris 10 8/07 s10s_u6wos_09a SPARC Copyright 2007 Sun Microsystems, Inc.  All Rights Reserved. Assembled 07 August 2007'
        sunos_facts = Distribution(module).get_distribution_SunOS()
        assert sunos_facts['distribution'] == 'Solaris'
        assert sunos_facts['distribution_version'] == '10'
        assert sunos

# Generated at 2022-06-13 02:46:31.702189
# Unit test for method get_distribution_FreeBSD of class Distribution
def test_Distribution_get_distribution_FreeBSD():
    module = type_mock()
    module.run_command.return_value = (0, "10.1-RELEASE", "")
    dist = Distribution(module)
    result = dist.get_distribution_FreeBSD()
    assert result['distribution_release'] == "10.1-RELEASE"
    assert result['distribution_version'] == "10.1"
    assert result['distribution_major_version'] == "10"


# Generated at 2022-06-13 02:47:50.224715
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    distro = DistributionFiles()
    collected_facts = dict()
    # Debian base image
    data = 'NAME="Debian GNU/Linux"\n' \
           'VERSION_ID="9"\n' \
           'VERSION="9 (stretch)"\n' \
           'ID=debian\n' \
           'HOME_URL="https://www.debian.org/"\n' \
           'SUPPORT_URL="https://www.debian.org/support"\n' \
           'BUG_REPORT_URL="https://bugs.debian.org/"\n'
    result, facts = distro.parse_distribution_file_Debian('Debian', data,
                                                          '/etc/os-release',
                                                          collected_facts)

# Generated at 2022-06-13 02:47:53.211561
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule(argument_spec={})
    distribution_NetBSD = Distribution(module)
    assert distribution_NetBSD.get_distribution_NetBSD() == {'distribution_release': '9.0', 'distribution_version': '9.0', 'distribution_major_version': '9'}

# Generated at 2022-06-13 02:48:03.062517
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # testing method parse_distribution_file_Amazon
    # setting up mock-up data
    name = 'Amazon'
    path = '/etc/os-release'
    data = 'NAME="Amazon Linux"\nVERSION="2"\nID="amzn"\nID_LIKE=\nVERSION_ID="2"\nPRETTY_NAME="Amazon Linux 2"\nANSI_COLOR="0;33"\nCPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"\nHOME_URL="https://amazonlinux.com/"\n'
    collected_facts = { 'distribution': 'Amazon', 'distribution_major_version': '2', 'distribution_version': '2'}
    # instantiating DistributionFiles
    dist_files = DistributionFiles(module)
    # calling parse_

# Generated at 2022-06-13 02:48:15.088072
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    """Test parsing of distribution file '/etc/faketest_file' as an Amazon Linux distribution"""
    collected_facts = {}
    collected_facts['lsb'] = {}
    collected_facts['lsb']['distributor_id'] = 'NA'
    collected_facts['lsb']['description'] = 'NA'
    collected_facts['lsb']['release'] = 'NA'
    collected_facts['lsb']['codename'] = 'NA'
    collected_facts['distribution'] = 'NA'
    collected_facts['distribution_release'] = 'NA'
    collected_facts['distribution_version'] = 'NA'
    collected_facts['distribution_major_version'] = 'NA'
    collected_facts['distribution_file_parsed'] = False

# Generated at 2022-06-13 02:48:25.488228
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():

    def setup_mocks(module, os_family, platform_system, default_name, uname_s_name, is_file_name, get_file_content_name):
        """
        Mock out methods and create a Distribution instance to test
        """
        # Create a fake module object
        module = MagicMock()

        # Mock out run_command because this is called in Distribution.__init__
        module.run_command = MagicMock()

        # Mock out get_file_content because this is called in Distribution.__init__
        module.get_file_content = MagicMock()

        # Mock out the os.path.isfile call in Distribution.__init__
        fake_isfile = MagicMock(return_value=False)
        module.isfile = fake_isfile

        module.get_file_content = MagicM

# Generated at 2022-06-13 02:48:37.554211
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    dist = DistributionFiles()
    facts = {}
    # test with valid data
    data = """# /etc/os-release: system-release(5) file for buildroot-based systems
NAME="openwrt"
VERSION="barrier_breaker (14.07)"
ID="openwrt"
ID_LIKE="lede buildroot"
VERSION_ID="14.07"
PRETTY_NAME="OpenWrt Barrier Breaker (14.07)"
CPE_NAME="cpe:/o:openwrt:openwrt:14.07"
HOME_URL="http://openwrt.org/"
SUPPORT_URL="http://wiki.openwrt.org/doc/howto/generic.factory.reset"
BUG_REPORT_URL="http://bugs.openwrt.org"
"""
    # test with valid data,

# Generated at 2022-06-13 02:48:48.477597
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    input_data = '''MANDRIVA_RELEASE="2009.1"
MANDRIVA_CODENAME="Adelie"'''
    collected_facts_data = {'distribution': 'Mandriva',
                            'distribution_version': '2009.1'
                            }
    file_path = '/etc/mandriva-release'
    dist_file_obj = DistributionFiles(module_ansible)
    output = dist_file_obj.parse_distribution_file_Mandriva('Mandriva', input_data, file_path, collected_facts_data)
    assert output == (True, {'distribution': 'Mandriva', 'distribution_release': 'Adelie', 'distribution_version': '2009.1'})



# Generated at 2022-06-13 02:48:56.898625
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    dist_file_facts = DistributionFiles()
    name = 'Slackware'
    data = '''
Slackware 14.2.0
'''
    path = '/etc/slackware-version'
    facts = {
        'distribution': 'NA',
        'distribution_major_version': 'NA',
        'distribution_minor_version': 'NA',
        'distribution_version': 'NA'
    }
    res, slackware_facts = dist_file_facts.parse_distribution_file_Slackware(name, data, path, facts)
    assert res
    assert slackware_facts['distribution'] == name
    assert slackware_facts['distribution_version'] == '14.2.0'



# Generated at 2022-06-13 02:49:08.533341
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    m = ansible.module_utils.basic.AnsibleModule(
    )
    m.run_command = MagicMock(return_value=(0, '', ''))
    df = DistributionFiles(m)
    name = "Mandriva"

# Generated at 2022-06-13 02:49:14.853783
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    module = AnsibleModule(supports_check_mode=True)

    distributed_files = DistributionFiles(module)
    cmd = "cat /etc/slackware-version"
    rc, out, err = module.run_command(cmd)
    result = distributed_files.parse_distribution_file_Slackware('Slackware', out, '/etc/slackware-version', {})
    assert result[0] == True
    assert result[1]['distribution'] == 'Slackware'
    assert result[1]['distribution_version'] == '14.1'
