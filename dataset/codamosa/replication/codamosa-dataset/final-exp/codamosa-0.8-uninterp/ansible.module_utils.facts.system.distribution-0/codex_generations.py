

# Generated at 2022-06-13 02:41:53.189506
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    d = DistributionFiles({})
    assert d.parse_distribution_file_Coreos('CoreOS', 'GROUP=stable', '/etc/os-release', {}) == (True, {'distribution_release': 'stable'})
    assert d.parse_distribution_file_Coreos('CoreOS', 'GROUP=alpha', '/etc/os-release', {}) == (True, {'distribution_release': 'alpha'})
    assert d.parse_distribution_file_Coreos('CoreOS', 'GROUP=beta', '/etc/os-release', {}) == (True, {'distribution_release': 'beta'})
    assert d.parse_distribution_file_Coreos('CoreOS', 'GROUP=alpha\n', '/etc/os-release', {}) == (True, {'distribution_release': 'alpha'})
   

# Generated at 2022-06-13 02:41:59.954681
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    # Fake distribution with method that returns 'Coreos'
    import sys
    import platform
    import platform as actual_platform
    platform_module = actual_platform
    class coreos_mock(object):
        def __getattr__(self, name):
            return getattr(actual_platform, name)
        def linux_distribution(self, *args, **kwargs):
            return ('Coreos', '', '')
        get_distribution = linux_distribution
    sys.modules['platform'] = coreos_mock()
    sys.modules['platform'].platform = coreos_mock()
    sys.modules['platform'].linux_distribution = coreos_mock()

    # Fetch facts
    m = AnsibleModule(argument_spec={})
    result = DistributionFiles().get_facts(m, m.params)

# Generated at 2022-06-13 02:42:07.823449
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    test_module = FakeModule({})
    test_dist_class = Distribution(test_module)

    test_content = "6.1.0.0"
    test_module.run_command = MagicMock(return_value=(0, test_content, ""))
    test_facts = test_dist_class.get_distribution_AIX()
    assert test_facts['distribution_major_version'] == '6'
    assert test_facts['distribution_version'] == '6.1.0'
    assert len(test_facts) == 3

    test_content = "6.1.0"
    test_module.run_command = MagicMock(return_value=(0, test_content, ""))
    test_facts = test_dist_class.get_distribution_AIX()

# Generated at 2022-06-13 02:42:19.062157
# Unit test for method parse_distribution_file_CentOS of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_CentOS():
    distribution_files = DistributionFiles()
    assertIsInstance(distribution_files.parse_distribution_file_CentOS(None, None, None, None)[0], bool)
# END Unit test for method parse_distribution_file_CentOS of class DistributionFiles

    def parse_distribution_file_CoreOS(self, name, data, path, collected_facts):
        coreos_facts = {}

        if 'CoreOS' in data:
            coreos_facts['distribution'] = 'CoreOS'
            release = re.search('COREOS_RELEASE_GROUP=(.*)', data)
            if release:
                coreos_facts['distribution_release'] = release.group(1).strip('"')
            coreos_facts.update(self.parse_distribution_file_NA(name, data, path, collected_facts))

# Generated at 2022-06-13 02:42:24.579283
# Unit test for method get_distribution_FreeBSD of class Distribution
def test_Distribution_get_distribution_FreeBSD():
    module = AnsibleModule(argument_spec={})
    distro = Distribution(module)
    freebsd_facts = {'distribution_release': '10.0-RELEASE', 'distribution_version': '10.0', 'distribution_major_version': '10'}
    assert distro.get_distribution_FreeBSD() == freebsd_facts



# Generated at 2022-06-13 02:42:32.469756
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    # Arrange
    distro_files = DistributionFiles()
    collected_facts = {'distribution_release': 'NA', 'distribution_version': '13.2'}

    # Act
    name = 'SUSE'
    data = """
NAME="openSUSE Leap"
VERSION="13.2 (Harlequin)"
VERSION_ID="13.2"
PRETTY_NAME="openSUSE Leap 13.2 (Harlequin)"
ID=opensuse
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:leap:13.2"
BUG_REPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org/"
ID_LIKE="suse"
""".strip()
    path = 'suse-release'
   

# Generated at 2022-06-13 02:42:40.523621
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    dfs = DistributionFiles()
    collected_facts = {'distribution': 'Flatcar', 'distribution_release': 'NA', 'distribution_version': 'NA'}
    # test for Flatcar
    distribution_file_facts = dfs.parse_distribution_file('Flatcar', 'GROUP=1234567', '', collected_facts)
    assert distribution_file_facts['distribution_release'] == '1234567'
    # test for other distribution
    distribution_file_facts = dfs.parse_distribution_file('RedHat', 'GROUP=1234567', '', collected_facts)
    assert distribution_file_facts['distribution_release'] == 'NA'



# Generated at 2022-06-13 02:42:45.210114
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    # Arrange
    module = MagicMock()
    module.run_command.return_value = (0, '/usr/bin/sw_vers -productVersion', '')

    distribution = Distribution(module)

    # Act
    darwin_facts = distribution.get_distribution_Darwin()

    # Assert
    assert darwin_facts['distribution'] == 'MacOSX'
    assert darwin_facts['distribution_major_version'] == '/usr/bin/sw_vers -productVersion'
    assert darwin_facts['distribution_version'] == '/usr/bin/sw_vers -productVersion'



# Generated at 2022-06-13 02:42:46.543210
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    assert get_distribution_file_facts()['distribution_release'] == 'stable'


# Generated at 2022-06-13 02:42:51.762010
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    test_module = Distribution(module=None)

    class Struct(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    platform_release = '8.0'
    kern_version = 'NetBSD 8.0 (GENERIC) #0: Thu Feb  8 07:41:50 UTC 2018  mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/amd64/compile/GENERIC amd64'

    test_module.module = Struct(run_command=lambda *args, **kwargs: (0, kern_version, ''))

    test_module.get_distribution_NetBSD.__globals__['platform'] = Struct(release=platform_release)

    assert test

# Generated at 2022-06-13 02:43:23.886646
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    '''
    Unit test for method parse_distribution_file_Amazon of class DistributionFiles
    :return:
    '''
    test_object = DistributionFiles()
    assert test_object
    # test 'Amazon Linux 2'
    # test for file content
    test_file_content = 'NAME="Amazon Linux"\n\n'
    # test for version
    test_version = '2'
    # test for distribution name
    test_name = 'Amazon'
    # test for distribution file path
    test_path = '/etc/os-release'
    # test for collected facts
    test_collected_facts = {}
    test_collected_facts['distribution_major_version'] = '2'
    test_collected_facts['distribution_version'] = '2.0.20191118'
    test_collected

# Generated at 2022-06-13 02:43:29.810512
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params['module_setup'] = True
    distribution = Distribution(module=module)
    # "swlist" is not installed on my test instance. So skipping this function
    hpux_facts = {}
    # hpux_facts = distribution.get_distribution_HPUX()
    assert hpux_facts == {}

# Generated at 2022-06-13 02:43:34.949408
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    module = AnsibleModule(argument_spec={})
    obj = Distribution(module)
    out = obj.get_distribution_Darwin()
    assert out['distribution'] == 'MacOSX'
    assert 'distribution_major_version' in out
    assert 'distribution_version' in out



# Generated at 2022-06-13 02:43:42.823108
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = AnsibleModule(argument_spec=dict())
    # Test with 1.0B.02.01.0.11
    rc, out, err = module.run_command(r"/usr/sbin/swlist |egrep 'HPUX.*OE.*[AB].[0-9]+\.[0-9]+'", use_unsafe_shell=True)
    rc, out, err = module.run_command(r"/usr/sbin/swlist |egrep 'HPUX.*OE.*[AB].[0-9]+\.[0-9]+'")
    assert rc == 0
    assert 'HPUX.11i.v2.OE.B.02.01.0' in out
    assert 'HPUX.11i.v2.OE.B.02.01.0' in out



# Generated at 2022-06-13 02:43:44.537542
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    #TODO: implement this test
    pass


# Generated at 2022-06-13 02:43:54.331782
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    distfile = DistributionFiles()
    dist_file_data = '''#cloud-config

coreos:
  etcd:
    # generate a new token for each unique cluster from https://discovery.etcd.io/new
    discovery: https://discovery.etcd.io/<token>
    addr: $public_ipv4:4001
    peer-addr: $public_ipv4:7001
  units:
    - name: etcd.service
      command: start
    - name: fleet.service
      command: start

users:
  - name: core
    passwd: $1$NlnxATn7$uwFW/UMJZo6L/Hj1fCcSY.'''

    coreos_facts = {}
    all_facts = {}
    # FIXME: pass in ro

# Generated at 2022-06-13 02:44:07.236184
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=False
    )

    distribution_files = DistributionFiles(module)

    # SUSE Linux Enterprise Server 11 SP1 (x86_64)
    # VERSION = 11
    # PATCHLEVEL = 1
    def test_1():
        name = 'SUSE-Enterprise-11'
        path = "/etc/SuSE-release"
        data = get_file_content(path)

        distribution_files = DistributionFiles(module)
        suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, '/etc/SuSE-release')
        assert suse_facts == dict(distribution_version='11.1')

    # SUSE Linux Enterprise Server 11 (x86_64)
    # VERSION =

# Generated at 2022-06-13 02:44:12.964165
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    # set up parameters of test
    os_facts = get_os_facts()
    name = 'slackware'
    data = get_file_content('/etc/slackware-version')
    path = '/etc/slackware-version'
    distfiles = DistributionFiles(None)
    collected_facts = {}
    # run test
    test_distfiles = distfiles.parse_distribution_file_Slackware(name, data, path, collected_facts)
    # compare results
    assert test_distfiles[0] == True
    # TODO: FIXME: assert test_distfiles[1] == expected_test_distfiles_result


# Generated at 2022-06-13 02:44:19.431719
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    test_module = AnsibleModule(argument_spec={})
    test_result = Distribution(test_module).get_distribution_AIX()
    test_assert = {'distribution_major_version': '7',
                   'distribution_version': '7.2',
                   'distribution_release': '2'
                   }
    assert test_result == test_assert



# Generated at 2022-06-13 02:44:29.444878
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    facts = {'distribution_release': 'NA'}
    distro_files = DistributionFiles()

# Generated at 2022-06-13 02:45:08.085658
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    def test_get_distribution_OpenBSD(module):
        return Distribution(module).get_distribution_OpenBSD()
    def set_uname(module, value):
        module.get_uname = lambda flags: value

# Generated at 2022-06-13 02:45:10.009788
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    module = AnsibleModule(argument_spec={
        'path': {'default': '/some/path', 'type': 'str'}
    })
    df = DistributionFiles(module)



# Generated at 2022-06-13 02:45:17.227602
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    fake_facts = {
        'lsb': {'distributor_id': 'Slackware', 'release': '14.2'},
        'distribution': 'Unknown',
        'distribution_release': 'NA',
        'distribution_version': 'NA'
    }
    d = DistributionFiles()
    d.distribution_file_paths = {
        "Slackware": {
            "path": "/etc/slackware-version",
            "contains": "Slackware"
        }
    }
    file = '/etc/slackware-version'
    data = 'Slackware 14.2'
    name = 'Slackware'
    (parsed, dist_facts) = d.parse_distribution_file_Slackware(name, data, file, fake_facts)

# Generated at 2022-06-13 02:45:24.062588
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    dists = DistributionFiles()
    parsed_facts = {}

    dists.process_dist_files(parsed_facts)

    assert parsed_facts

    assert parsed_facts['distribution'], "distribution should not be None"

    # TODO: if this is happening, we should raise an error
    assert parsed_facts['distribution'] != "NA", "distribution should not be NA"

    # TODO: test a bunch more values?
    # TODO: split into smaller tests? (ie, a test for each OS we check)

# Generated at 2022-06-13 02:45:29.148638
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule()
    d = Distribution(module=module)
    result = d.get_distribution_NetBSD()
    assert 'distribution' in result
    assert 'distribution_release' in result
    assert 'distribution_version' in result
    assert 'distribution_major_version' in result

# Generated at 2022-06-13 02:45:34.846516
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    # Arrange
    name = "Slackware"
    data = '''Slackware 14.0 \n'''
    path = ''
    collected_facts = {}

    # Act
    distribution_files = DistributionFiles()
    parsed_dist_file, parsed_dist_file_facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    # Assert
    assert parsed_dist_file is True and parsed_dist_file_facts['distribution_version'] == '14.0'


# Generated at 2022-06-13 02:45:44.805481
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Create an object of DistributionFiles class
    distribution_files = DistributionFiles()

    # Call the method parse_distribution_file_Amazon with defined arguments
    name = 'Amazon'
    data = 'Amazon Linux release 2 (Karoo)'
    path = '/etc/system-release'
    collected_facts = {}
    expected_return_value = {'distribution': 'Amazon', 'distribution_version': '2'}
    assert distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts) == (True, expected_return_value)

    # Call the method parse_distribution_file_Amazon with defined arguments
    name = 'Amazon'

# Generated at 2022-06-13 02:45:51.153563
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    dist_file_parser = DistributionFiles()

    # Test with the OpenWrt file /etc/os-release
    collected_facts = {'distribution': 'NA'}
    name = 'OpenWrt'
    path = "/etc/os-release"
    data = """
    PRETTY_NAME="OpenWrt 18.06.4"
    NAME="OpenWrt"
    DISTRIB_ID="OpenWrt"
    DISTRIB_RELEASE="18.06.4"
    DISTRIB_REVISION="r7258-5eb055306f"
    DISTRIB_TARGET="ar71xx/generic"
    DISTRIB_ARCH="mips_24kc"
    DISTRIB_DESCRIPTION="OpenWrt 18.06.4"
    DISTRIB_TAINTS=""
    """

# Generated at 2022-06-13 02:46:03.143479
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    """Unit tests for method parse_distribution_file_Amazon of class DistributionFiles"""
    distribution_files = DistributionFiles()
    # testing for path /etc/system-release-cpe
    name = "Amazon"
    data = "Amazon Linux"
    path = "/etc/system-release-cpe"
    collected_facts = dict(distribution="NA", distribution_release="NA", distribution_version="NA")
    parsed_dist_file = "true"
    parsed_dist_file_facts = dict(distribution="Amazon", distribution_release="NA", distribution_version="2.0.20170708")
    assert distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts) == (True, parsed_dist_file_facts)
    # testing for path /etc/os-release

# Generated at 2022-06-13 02:46:12.416646
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    data_input = '''DISTRIB_ID=OpenWrt
DISTRIB_RELEASE=18.06.0
DISTRIB_REVISION=r7676-cddd7b4c77
DISTRIB_TARGET=ramips/mt7621
DISTRIB_ARCHITECTURE=mipsel_24kc
DISTRIB_DESCRIPTION="OpenWrt 18.06.0 r7676-cddd7b4c77"
DISTRIB_TAINTS='''
    name_input = 'OpenWrt' # TODO: verify the value of this parameter
    output = {'distribution': 'OpenWrt', 'distribution_version': '18.06.0', 'distribution_release': 'r7676-cddd7b4c77'}
    assert DistributionFiles.parse_distribution

# Generated at 2022-06-13 02:47:47.280974
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    df = DistributionFiles()
    df.distribution_files = {
        "Debian": "/usr/lib/os-release",
        "Ubuntu": "/etc/lsb-release",
        "Kali": "/etc/lsb-release",
        "Parrot": "/etc/lsb-release",
        "Devuan": "/etc/os-release",
        "LinuxMint": "/etc/os-release",
        "LinuxMint": "/usr/lib/os-release",
        "Cumulus": "/usr/lib/os-release",
        "SteamOS": "/usr/lib/os-release"
    }

# Generated at 2022-06-13 02:47:50.038775
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    d = Distribution(FakeModule(platform_system='NetBSD'))
    assert d.get_distribution_NetBSD() == {
        'distribution': 'NetBSD',
        'distribution_release': 'release',
        'distribution_version': 'release',
    }


# Generated at 2022-06-13 02:48:00.544574
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    d = DistributionFiles()
    clear_facts = {}
    name = 'clearlinux'
    data = '''NAME="Clear Linux OS"
VERSION="23800"
ID=clear-linux-os
VERSION_ID=23800
PRETTY_NAME="Clear Linux OS 23800"
ANSI_COLOR="1;37"
HOME_URL="https://clearlinux.org/"
SUPPORT_URL="https://clearlinux.org/support"
BUG_REPORT_URL="https://github.com/clearlinux/distribution/issues"
PRIVACY_POLICY_URL="https://clearlinux.org/privacy-policy"
BUILD_ID="mj.vmware.1"
'''
    path = '/etc/os-release'
    collected_facts = 'NA'
    # Expected true
    actual_return, actual

# Generated at 2022-06-13 02:48:03.028091
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(dict(test=dict(test_arg='test_value')))
    p = Distribution(module)
    f = p.get_distribution_OpenBSD()
    assert 'distribution_version' in f
    assert 'distribution_release' in f



# Generated at 2022-06-13 02:48:15.035818
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    """Test method parse_distribution_file_Debian of class DistributionFiles.
       Including cases:
           1. Debian
           2. Ubuntu
           3. Devuan
           4. Kali
           5. Parrot
           6. Linux Mint
    """
    # Test case 1:
    data = """
    PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
    NAME="Debian GNU/Linux"
    VERSION_ID="8"
    VERSION="8 (jessie)"
    ID=debian
    HOME_URL="http://www.debian.org/"
    SUPPORT_URL="http://www.debian.org/support/"
    BUG_REPORT_URL="https://bugs.debian.org/"
    """

# Generated at 2022-06-13 02:48:21.531131
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    """
    Unit test case to validate the parsing of
    distribution specific files.
    """
    # Create a new instance of DistributionFiles
    dist_files = DistributionFiles()
    # pylint: disable=protected-access
    collected_facts = {}

# Generated at 2022-06-13 02:48:32.737435
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    with open('tests/unittests/data/suse-release') as f:
        data = f.read()

    collected_facts = {'distribution_version': '42.3'}

    dist_files = DistributionFiles({}, collected_facts)

    (parsed, suse_facts) = dist_files.parse_distribution_file_SUSE('SUSE', data, '/etc/SuSE-release', collected_facts)

    assert parsed == True
    assert suse_facts['distribution'] == 'SLES'
    assert suse_facts['distribution_release'] == '0'
    assert suse_facts['distribution_version'] == '42.3.0'


# Tests for SLE_Module_Tools


# Generated at 2022-06-13 02:48:41.420795
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    parsed_facts = {}

# Generated at 2022-06-13 02:48:51.689995
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    # Slackware case
    distributionfiles = DistributionFiles()
    distributionfiles.module = MagicMock()
    data = '''Slackware 14.2'''
    path = '/etc/slackware-version'
    name = 'Slackware'
    collected_facts = {
        'distribution': 'Slackware',
        'distribution_version': 'NA'
    }
    expected_return = True, {'distribution': 'Slackware', 'distribution_version': '14.2'}
    return_value = distributionfiles.parse_distribution_file_Slackware(name, data, path, collected_facts)
    assert return_value == expected_return



# Generated at 2022-06-13 02:49:02.124084
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    # Test emptying facts
    # {'distribution': 'NA', 'distribution_major_version': 'NA', 'distribution_release':
    # 'NA', 'distribution_version': 'NA'} => {'distribution': 'NA', 'distribution_major_version':
    # 'NA', 'distribution_release': 'NA', 'distribution_version': 'NA'}
    path = '/etc/os-release'
    data = 'NAME="NA"\nVERSION="NA"\nID="NA"'
    facts = {'distribution': 'NA', 'distribution_major_version': 'NA',
             'distribution_release': 'NA', 'distribution_version': 'NA'}
    # instantiate class DistributionFiles
    df = DistributionFiles()
    # call method parse_distribution_file_NA
    result

# Generated at 2022-06-13 02:50:45.771988
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():

    import ansible.module_utils.distro
    import ansible.module_utils.facts.collector

    # TODO: use pytest fixtures
    # setup
    test_subject = DistributionFiles()
    test_subject.module = ansible.module_utils.facts.collector.FactsCollector()
    test_subject.module.get_bin_path = ansible.module_utils.distro.get_bin_path

    # set values
    name = 'NA'
    path = '/etc/os-release'
    data = """NAME="Fedora"
VERSION="26 (Twenty Six)"
ID=fedora
VERSION_ID=26
"""

    expected_dist = {'distribution': 'Fedora', 'distribution_version': '26 (Twenty Six)'}

    # execute method under test
    y_n, distribution_