

# Generated at 2022-06-13 02:42:24.533120
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    mock_module = MockModule(platform_system='AIX')
    mock_module.run_command = Mock(return_value=(0, '7.2', ''))
    dist = Distribution(mock_module)

    facts = dist.get_distribution_facts()

    assert 'distribution' in facts
    assert facts['distribution'] == 'AIX'
    assert 'distribution_version' in facts
    assert facts['distribution_version'] == '7.2'
    assert 'distribution_major_version' in facts
    assert facts['distribution_major_version'] == '7'
    assert 'distribution_release' in facts
    assert facts['distribution_release'] == '2'



# Generated at 2022-06-13 02:42:32.193379
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    openwrt_data = """DISTRIB_ID=OpenWrt
DISTRIB_RELEASE=14.07
DISTRIB_REVISION=r42625
DISTRIB_CODENAME=barrier_breaker
DISTRIB_TARGET=ar71xx/generic
DISTRIB_DESCRIPTION="OpenWrt Barrier Breaker r42625"
DISTRIB_TAINTS=no-all
"""
    test_obj = DistributionFiles()
    results = test_obj.parse_distribution_file_OpenWrt(data=openwrt_data)
    expected = {'distribution': 'OpenWrt',
                'distribution_release': 'barrier_breaker',
                'distribution_version': '14.07'}
    assert results == expected



# Generated at 2022-06-13 02:42:41.414839
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():

    distribution = DistributionFiles()
    data = '''NAME="Debian GNU/Linux"
VERSION="9 (stretch)"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"'''

    collected_facts = {}
    result = distribution._DistributionFiles__parse_distribution_file_Debian('debian', data, '/etc/os-release', collected_facts)
    assert result == (True, {'distribution': 'Debian'})


# Generated at 2022-06-13 02:42:46.220916
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    """ This method test the get_distribution_AIX method of class Distribution.
    """
    test_instance = Distribution(None)
    test_data_1 = 'Oracle Solaris 11.1 X86'
    assert test_instance.get_distribution_SunOS() == {
        'distribution': 'Solaris',
        'distribution_release': 'Oracle Solaris 11.1 X86',
        'distribution_version': '11.1',
        'distribution_major_version': '11'
    }

# Generated at 2022-06-13 02:42:51.536960
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    distro_facts = DistributionFiles()
    ansible_module = AnsibleModule(argument_spec={})
    parsed_dist_file_facts = {}
    rc = False
    data = 'DISTRIB_DESCRIPTION="OpenWrt 18.06.4"\nDISTRIB_RELEASE="18.06.4"\nDISTRIB_CODENAME="Gargoyle"\nDISTRIB_TARGET="x86/generic"\nDISTRIB_ARCH="x86"\nDISTRIB_REVISION="r7258-5eb055306f"'

# Generated at 2022-06-13 02:42:53.340555
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    module = AnsibleModule()
    dist = Distribution(module)
    dist_facts = dist.get_distribution_AIX()

    assert dist_facts['distribution'] == 'AIX'
    assert dist_facts['distribution_version'] == '6.1'

# Generated at 2022-06-13 02:43:03.554095
# Unit test for method parse_distribution_file_CentOS of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_CentOS():
    centos_data = """NAME="CentOS Linux"
VERSION="8 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="8"
PLATFORM_ID="platform:el8"
PRETTY_NAME="CentOS Linux 8 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:8"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-8"
CENTOS_MANTISBT_PROJECT_VERSION="8"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="8"
"""
    centos

# Generated at 2022-06-13 02:43:09.840849
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    test_data = {
        'name': 'Debian',
        'path': '/etc/os-release',
        'data': """
NAME="Debian GNU/Linux"
ID=debian
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
VERSION_ID="9"
VERSION="9 (stretch)"
ID_LIKE=debian
ANSI_COLOR="1;31"
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
""",
        'distribution': 'Debian',
        'distribution_release': 'stretch',
        'distribution_version': '9'
    }
    obj = DistributionFiles()
    res = obj.parse_distribution_file_

# Generated at 2022-06-13 02:43:16.107047
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = FakeModule()
    distribution = Distribution(module)
    distribution.module.run_command = run_command

    openbsd_facts = distribution.get_distribution_OpenBSD()
    assert openbsd_facts == {'distribution_version': '6.1', 'distribution_release': 'stabilizer'}


# Generated at 2022-06-13 02:43:26.193116
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles

# Generated at 2022-06-13 02:43:57.233707
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    df = DistributionFiles()
    assert df.parse_distribution_file_ClearLinux(name='clearlinux', data='NAME="Clear Linux"', path='/etc/os-release', collected_facts={})[1]['distribution'] == 'Clear Linux'
    assert df.parse_distribution_file_ClearLinux(name='clearlinux', data='VERSION_ID=300050', path='/etc/os-release', collected_facts={})[1]['distribution_major_version'] == '300050'
    assert df.parse_distribution_file_ClearLinux(name='clearlinux', data='ID=clear', path='/etc/os-release', collected_facts={})[1]['distribution_release'] == 'clear'


# Generated at 2022-06-13 02:44:00.087471
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    class TestModule(object):
        def run_command(self, cmd):
            return 0, '5.2.2-RELEASE', None

    distribution = Distribution(TestModule())
    assert distribution.get_distribution_DragonFly() == {'distribution_release': '5.2.2-RELEASE', 'distribution_major_version': '2', 'distribution_version': '5.2.2'}



# Generated at 2022-06-13 02:44:08.784188
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    """Test method parse_distribution_file_OpenWrt of class DistributionFiles"""

    # test with a low expectation, as the test should have failed if the wrong
    # file were parsed
    expected_parsed = {}

    # Get a tempdir to use for testing
    tempdir = get_random_tempdir()
    tempdir_abs = os.path.abspath(tempdir)

    # create a dummy OpenWrt file for testing
    # make a random temp file with the repo info
    # write a dummy line to the file
    openwrt_file = os.path.join(tempdir, 'openwrt')
    with open(openwrt_file, 'w') as f:
        f.write('DISTRIB_RELEASE="18.06.2"\n')

# Generated at 2022-06-13 02:44:17.535110
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    a = DistributionFiles(None)
    name = 'slackware'
    # pylint: disable=line-too-long
    data = '''Slackware 13.0.0
    Slackware release 13.0.0 (Slackware Current)'''
    return_dict = {'distribution': 'slackware', 'distribution_version': '13.0.0'}
    assertAllIn(a.parse_distribution_file_Slackware(name, data)) == return_dict



# Generated at 2022-06-13 02:44:25.604346
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    with pytest.raises(UnsupportedPlatform) as e:
        assert DistributionFiles().parse_distribution_file_Debian('Ubuntu', '', '', {})
    assert str(e.value) == 'Unsupported platform/version: Ubuntu'

    flatcar = DistributionFiles().parse_distribution_file_Flatcar('Flatcar', 'GROUP=stable', '', {})
    assert flatcar[1] == {'distribution_release': 'stable'}

    coreos = DistributionFiles().parse_distribution_file_Coreos('CoreOS', 'GROUP=stable', '', {})
    assert coreos[1] == {'distribution_release': 'stable'}

# Generated at 2022-06-13 02:44:35.304261
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    distfile = DistributionFiles()
    name = 'ClearLinux'
    path = '/etc/os-release'
    data = read_data_file(path)
    collected_facts = {}
    res, dist_file_facts = distfile.parse_distribution_file_ClearLinux(name, data, path, collected_facts)
    data_facts = {'distribution': 'Clear Linux',
                  'distribution_major_version': '28220',
                  'distribution_version': '28220',
                  'distribution_release': 'os'}
    assert res
    assert dist_file_facts == data_facts


# Generated at 2022-06-13 02:44:44.546136
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    test_class = DistributionFiles()

    data_with_open = """NAME=openSUSE
VERSION="42.1"
ID=opensuse
ID_LIKE="suse"
"""
    data1_with_enterprise = """PRETTY_NAME="SUSE Linux Enterprise Server 12 SP2"
VERSION="12.2"
ID="sles"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:suse:sles:12:sp2"
"""

# Generated at 2022-06-13 02:44:47.739407
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule(
        argument_spec = dict(),
    )

    module.run_command = MagicMock(return_value=(0, "NetBSD 3.99.XGENERIC (foo)", ""))
    actual = Distribution(module).get_distribution_NetBSD()
    assert actual["distribution_major_version"] == "3"
    assert actual["distribution_version"] == "3.99"
    assert actual["distribution_release"] == "3.99.XGENERIC"

# Generated at 2022-06-13 02:44:59.484299
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    df = DistributionFiles()
    path = '/etc/lsb-release'
    data = b'DISTRIB_ID=MandrivaLinux\nDISTRIB_RELEASE=2011.0\nDISTRIB_CODENAME=Cooker\nDISTRIB_DESCRIPTION="Mandriva Linux release 2011.0 (Cooker) (Official) Welcome Edition"\n'

# Generated at 2022-06-13 02:45:02.316439
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = FakeModule()
    dist = Distribution(module)
    hpux_facts = dist.get_distribution_HPUX()
    assert hpux_facts['distribution_release'] == '11i v3'
    assert hpux_facts['distribution_version'] == 'B.11.31'



# Generated at 2022-06-13 02:45:59.796585
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles

# Generated at 2022-06-13 02:46:04.004208
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    netbsd_facts = distribution.get_distribution_NetBSD()
    assert netbsd_facts['distribution'] == 'NetBSD'


# Generated at 2022-06-13 02:46:13.678753
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    # Create an instance of DistributionFiles
    df = DistributionFiles()

    # Create an instance of AnsibleModule
    module = AnsibleModule(argument_spec={})

    # set DistributionFiles attributes
    df.module = module

    # name = "Flatcar"
    # data = "GROUP=beta\n"
    # path = "/usr/share/coreos/lsb-release"
    # collected_facts = {"lsb": {"distcodename": "", "distid": "Flatcar", "distdescription": "Flatcar Linux", "distrelease": "", "majdistrelease": "", "minordistrelease": ""}}
    # assert df.parse_distribution_file_Flatcar(name, data, path, collected_facts) is not False



# Generated at 2022-06-13 02:46:22.878180
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    with open('test-files/test_DistributionFiles_parse_distribution_file_NA_data.txt') as f:
        data = f.read()

    name = 'NA'
    path = '/etc/os-release'
    collected_facts = {}
    distribution_file_facts = {}
    collected_facts['distribution'] = 'NA'
    collected_facts['distribution_version'] = 'NA'

    dist = DistributionFiles(name, path, data, distribution_file_facts, collected_facts)
    assert dist.parse_distribution_file_NA() == (True, {'distribution': 'Oracle Linux Server', 'distribution_version': '7.3'})



# Generated at 2022-06-13 02:46:34.071622
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    df = DistributionFiles()

    # Debian
    data = """\
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
"""
    expected = {'distribution': 'Debian'}
    name = "Debian"
    path = '/etc/os-release'

    parsed_dist_file, parsed_dist_file_facts = df.parse_distribution_file(name, data, path, {})
    assert parsed_dist_file and parsed_dist_file_facts == expected

    # Ubuntu
    data

# Generated at 2022-06-13 02:46:35.053824
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    pass


# Generated at 2022-06-13 02:46:40.136507
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    from shutil import rmtree
    from tempfile import mkdtemp
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector.network.iproute2 import parse_default_route

    test_dir = mkdtemp()
    test_sw_vers = unfrackpath('/usr/bin/sw_vers')
    test_content = "ProductVersion: 10.15.5\nBuildVersion: 19F101\n"

    with open('%s/sw_vers' % test_dir, 'w') as f:
        f.write(test_content)

    rmtree(test_sw_vers, ignore_errors=True)


# Generated at 2022-06-13 02:46:43.261849
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    m = FakeModule({'PATH': "/opt/local/bin:/usr/bin:/bin:/usr/sbin:/sbin", 'LANG': "C", 'HOME': "/Users/Shared"})
    result = Distribution(m).get_distribution_Darwin()
    assert result['distribution'] == 'MacOSX'
    assert result['distribution_version'] == '10.12.6'

# Generated at 2022-06-13 02:46:50.868780
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    rc, out, dummy = module.run_command("/bin/uname -r")
    assert distribution.get_distribution_SunOS()['distribution_major_version'] == out.split('.')[1].rstrip()
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    rc, out, dummy = module.run_command("/sbin/uname -v")
    assert distribution.get_distribution_SunOS()['distribution_version'] == out.strip()

# Generated at 2022-06-13 02:46:56.556973
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    # Setup
    d = DistributionFiles()
    # Exercise
    # Verify
    assert d.parse_distribution_file_Debian('Debian', 'Debian', '/etc/lsb-release', {'distribution_release': 'NA'}) == (True, {'distribution': 'Debian'})


# Generated at 2022-06-13 02:47:56.503372
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(argument_spec=dict())
    distribution = Distribution(module=module)
    distribution_facts = distribution.get_distribution_OpenBSD()
    print(distribution_facts)

# Generated at 2022-06-13 02:47:58.891984
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = get_test_module_ansible_os_facts()
    dist_hpux = Distribution(module)
    hpux_facts = dist_hpux.get_distribution_HPUX()
    if 'distribution_version' in hpux_facts and hpux_facts['distribution_version'] == 'B.11.31':
        return True
    return False

# Generated at 2022-06-13 02:48:05.962355
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    from ansible.module_utils.facts.collector import DistributionFiles
    distribution_files_object = DistributionFiles()

# Generated at 2022-06-13 02:48:19.131171
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Initializing necessary test variables
    name = 'Amazon'
    data = 'NAME="Amazon Linux"\nVERSION="2"\nID="amzn"\nID_LIKE="centos rhel fedora"\nVERSION_ID="2"\nPRETTY_NAME="Amazon Linux 2"\nANSI_COLOR="0;33"\nCPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"\nHOME_URL="https://amazonlinux.com/"\n'
    path = '/etc/os-release'
    collected_facts = {}
    sample_data = collected_facts['distribution_version'] = 'NA'
    sample_data = collected_facts['distribution_release'] = 'NA'
    sample_data = collected_facts['distribution_file_path'] = 'NA'

# Generated at 2022-06-13 02:48:30.021583
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    DEBIAN_DATA = '''
    NAME="Ubuntu"
    VERSION="15.04 (Vivid Vervet)"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 15.04"
    VERSION_ID="15.04"
    HOME_URL="http://www.ubuntu.com/"
    SUPPORT_URL="http://help.ubuntu.com/"
    BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
    '''
    DEBIAN_RELEASE = '''
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=15.04
    DISTRIB_CODENAME=vivid
    DISTRIB_DESCRIPTION="Ubuntu 15.04"
    '''

# Generated at 2022-06-13 02:48:40.433285
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    # create an object of Distribution class
    distribution = Distribution(module='module')
    # create a mocked object of OpenBSD distribution with version 'OpenBSD 6.8 (GENERIC) #0: Sat Apr 18 17:55:33 UTC 2020''
    openBSD_distribution = MagicMock(platform.system)
    openBSD_distribution.return_value = 'OpenBSD'
    openBSD_release_version = MagicMock(platform.release)
    # create a mocked object of NetBSD distribution with version '5.1 (GENERIC) #0: Sun Nov 10 12:09:33 UTC 2019'
    netBSD_distribution = MagicMock(platform.system)
    netBSD_distribution.return_value = 'NetBSD'
    netBSD_release_version = MagicMock(platform.release)

# Generated at 2022-06-13 02:48:51.699993
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    name="SUSE"
    data=""
    path=""
    collected_facts=dict()
    collected_facts['distribution'] = 'NA'
    collected_facts['distribution_version'] = 'NA'
    collected_facts['distribution_release'] = 'NA'
    collected_facts['distribution_file_version'] = 'NA'
    collected_facts['distribution_file_variety'] = 'NA'
    collected_facts['distribution_file_parsed'] = False
    collected_facts['distribution_file_path'] = 'NA'
    collected_facts['distribution_file_names'] = []


    # test valid data
    f = DistributionFiles(module)

# Generated at 2022-06-13 02:48:59.349789
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = Mock()
    module.run_command.return_value = (0, None, None)
    module.get_file_content.return_value = None
    module.file_exists.return_value = False

    # Test
    distro = Distribution(module=module)
    distribution_facts = distro.get_distribution_SunOS()
    # Assertion
    assert distribution_facts == {'distribution': None, 'distribution_major_version': None, 'distribution_release': None, 'distribution_version': None}

    # Test
    module.get_file_content.return_value = 'Solaris 10 1/13 s10x_u11wos_24a X86'
    module.run_command.return_value = (0, '5.11', None)

# Generated at 2022-06-13 02:49:08.129568
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    from ansible.module_utils.facts.system.distribution import DistributionFiles
    from ansible.module_utils.facts.system.distribution import Distribution
    dist = Distribution()
    dist.set(name="CoreOS", id="coreos", version_id="1234.5.6")
    dist_files = DistributionFiles()
    data = "GROUP=alpha"
    coreos_facts = dist_files.parse_distribution_file_Coreos(dist.name, data, None, dist)
    assert coreos_facts['distribution_release'] == "alpha"



# Generated at 2022-06-13 02:49:12.030914
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    '''
        Function to test module method parse_distribution_file_Debian of class DistributionFiles
    '''
    test_obj = DistributionFiles(dict())
    assert test_obj.parse_distribution_file_Debian("Debian", "\nNAME=Debian\n", "", {})[0] == True

# Generated at 2022-06-13 02:50:30.453288
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    """
    Testing method parse_distribution_file_Amazon,
    """
    fos = DistributionFiles()
    name = 'Amazon'
    data = 'Amazon'
    path = '/etc/os-release'
    collected_facts = {}
    assert fos.parse_distribution_file_Amazon(
        name, data, path, collected_facts) == (
        True, {'distribution': 'Amazon'})
    assert fos.parse_distribution_file_Amazon(
        name, None, path, collected_facts) == (
        False, {'distribution': 'Amazon'})
    assert fos.parse_distribution_file_Amazon(
        None, None, path, collected_facts) == (
        False, {})



# Generated at 2022-06-13 02:50:37.186767
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    dist = DistributionFiles()
    collected_facts = {}
    collected_facts['distribution_version'] = 'NA'
    collected_facts['distribution_release'] = 'NA'
    name = 'clearlinux'
    path = '/usr/share/clear-linux-os/clear/version'
    # output of `cat /usr/share/clear-linux-os/clear/version`
    data = '''NAME="Clear Linux OS"
VERSION="35874"
ID=clear-linux-os
ID_LIKE=fedora
VERSION_ID="35874"
PRETTY_NAME="Clear Linux OS 35874"
ANSI_COLOR="0;32"
HOME_URL="https://clearlinux.org/"
BUG_REPORT_URL="https://github.com/clearlinux/distribution/issues/"
'''
    parsed_dist

# Generated at 2022-06-13 02:50:47.440279
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    collected_facts = {}
    distribution_files = DistributionFiles({})
    name = 'Mandriva'
    data = '''
    NAME="Mandriva Linux"
    VERSION="2006.0 (Official) - Spring"
    ID=mandriva
    VERSION_ID=2006
    PRETTY_NAME="Mandriva Linux 2006.0 (Official) - Spring"
    '''
    path = '/path/to/file/'
    data_ = data.encode('utf-8')
    parsed_dist, parsed_dist_facts = distribution_files.parse_distribution_file(name, data_, path, collected_facts)
    assert 'distribution' in parsed_dist_facts
    assert parsed_dist_facts['distribution'] == 'Mandriva'
    assert 'distribution_version' in parsed_dist_