

# Generated at 2022-06-13 02:42:00.435535
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    def fake_get_uname(self, flags=[]):
        return None
    def fake_file_exist(self):
        return False
    def fake_file_get_content(self):
        return """Solaris 9 9/05 s9s_u5wos_14a SPARC
        Copyright 2005 Sun Microsystems, Inc.  All Rights Reserved.
        Use is subject to license terms.
        Assembled 23 October 2005
        """
    pltfrm = platform()
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    setattr(pltfrm,'run_command',fake_run_command)
    setattr(pltfrm,'file_exist',fake_file_exist)

# Generated at 2022-06-13 02:42:08.219670
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    # TODO: Factor out the tests into a standalone module
    def get_fake_module():
        class FakeModule(object):
            def __init__(self):
                self.params = {}
                self.run_command = MagicMock()
                self.run_command.return_value = 2, 'stdout', 'stderr'
        return FakeModule()
    module = get_fake_module()

    module.run_command.return_value = 0, '\r\r\nNetBSD 7.0 (GENERIC) #4: Thu Jul  5 17:30:22 UTC 2018\r\r\nmkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/amd64/compile/GENERIC\r\r\n', ''
    distribution = Distribution(module)
    facts = distribution

# Generated at 2022-06-13 02:42:14.580143
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    ############################
    # print("Starting test_Distribution_get_distribution_AIX ...")
    ############################

    facts = Distribution(module='Linux').get_distribution_AIX()

    assert facts['distribution_major_version'] == '7'
    assert facts['distribution_version'] == '7.1'
    assert facts['distribution_release'] == '1'

    ############################
    # print("Completed test_Distribution_get_distribution_AIX.")
    ############################

# Generated at 2022-06-13 02:42:27.447463
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_array = ['rc', 'output', 'error']
    test_module.run_command = MagicMock(return_value=test_array)

    out_expected = ['\n']
    out_expected.append("Swlist : Release level:     B.11.31.1705\n")
    out_expected.append("Swlist : Release date:      Sep 22, 2017\n")
    out_expected.append("Swlist : Revision level:    17.05\n")

    test_module.run_command = MagicMock(return_value=test_array)

    distribution = Distribution(module=test_module)


# Generated at 2022-06-13 02:42:32.102516
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    from ansible.module_utils.facts import DistributionFiles
    df = DistributionFiles()
    test_file = {'/etc/os-release': "NAME=\"Debian GNU/Linux\"\nVERSION=\"8 (jessie)\"\nID=debian\nID_LIKE=debian\nPRETTY_NAME=\"Debian GNU/Linux 8 (jessie)\"\nVERSION_ID=\"8\"\nHOME_URL=\"http://www.debian.org/\"\nSUPPORT_URL=\"http://www.debian.org/support/\"\nBUG_REPORT_URL=\"https://bugs.debian.org/\""}
    test_params = {'_ansible_tmpdir': '/tmp'}
    test_facts = {'distribution': "Debian", 'distribution_version': "NA"}
    test_dist_file_facts

# Generated at 2022-06-13 02:42:37.786203
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # create an instance of Distribution and then test get_distribution_DragonFly
    module = AnsibleModule(argument_spec=dict())
    dist = Distribution(module)
    dist.module.run_command = MagicMock(return_value=(0, '6.3-RELEASE', ''))
    assert dist.get_distribution_DragonFly() == {
        'distribution_release': '6.3-RELEASE'
    }



# Generated at 2022-06-13 02:42:47.234616
# Unit test for function get_uname
def test_get_uname():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.common.collections import ImmutableDict

    class Options:
        def __init__(self, module_name='ansible_distribution'):
            self.module_name = module_name

    class FakeModule:
        def __init__(self, params=None):
            self.params = params if params else {}

        def run_command(self, command):
            return (0, 'Linux', '')

    class FakeDistributionCollector:
        def __init__(self, module, collected_facts=None):
            self.module = module
            self.collected_facts = collected_facts if collected_facts else {}


# Generated at 2022-06-13 02:42:53.370284
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = AnsibleModule(
        argument_spec=dict(
        )
    )
    facts = FactCollector(module=module)
    distribution = Distribution(module=module)
    facts_dict = distribution.get_distribution_SunOS()
    assert facts_dict['distribution'] == 'Solaris'


# Generated at 2022-06-13 02:42:56.707741
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    module = AnsibleModule(argument_spec={})
    distro_os = Distribution(module)
    dragonfly_facts = distro_os.get_distribution_DragonFly()
    assert type(dragonfly_facts) == dict
    assert dragonfly_facts['distribution_release'] == platform.release()
    # Check that the distribution_release is the same between platform and the distribution_release variable
    assert dragonfly_facts['distribution_release'] == platform.release()
    assert 'distribution_major_version' in dragonfly_facts
    assert 'distribution_version' in dragonfly_facts

# Generated at 2022-06-13 02:43:05.177839
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    dist_file_content = '''DISTRIB_ID=MandrivaLinux
DISTRIB_RELEASE=2007.0
DISTRIB_CODENAME=Daryna
DISTRIB_DESCRIPTION="Mandriva Linux 2007.0 (Daryna)"
DISTRIB_ID=MandrivaLinux
DISTRIB_RELEASE=2007.0
DISTRIB_CODENAME=Daryna
DISTRIB_DESCRIPTION="Mandriva Linux 2007.0 (Daryna)"'''
    name = 'Mandriva'
    path = '/etc/mandriva-release'
    collected_facts = {}
    distribution_files = DistributionFiles(None)
    # Invoke method to be tested

# Generated at 2022-06-13 02:43:56.876514
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    """Unit test for method parse_distribution_file_Slackware of class DistributionFiles"""

# Generated at 2022-06-13 02:44:01.823109
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    dist = Distribution(module=None)
    with patch.object(platform, 'system') as platform_system, \
        patch.object(platform, 'release') as platform_release, \
        patch.object(dist, 'module') as module:

        platform_system.return_value = 'DragonFly'
        platform_release.return_value = 'v5.6-RELEASE'

        module.run_command.side_effect = [
            (0, 'v5.6-RELEASE', ''),
        ]

        dist_facts = dist.get_distribution_DragonFly()

        assert dist_facts == {
            'distribution_release': 'v5.6-RELEASE',
            'distribution_major_version': '5',
            'distribution_version': '5.6',
        }


# Generated at 2022-06-13 02:44:10.007429
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    """Unit test for method parse_distribution_file_Debian of class DistributionFiles."""
    data = """PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
"""
    df = DistributionFiles()
    result, debian_facts = df.parse_distribution_file_Debian('Debian', data, '/etc/debian_version', {})
    assert result == True
    assert debian_facts['distribution'] == 'Debian'

# Generated at 2022-06-13 02:44:21.925236
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import DistributionFiles
    from ansible.module_utils.facts.collector import FacterCollector, CollectedFacts
    import ansible_collections.ansible.distribution.plugins.module_utils.facts.dist
    # Setup data
    data = "CoreOS\nGROUP=stable\nID=coreos\nVERSION_ID=1234.1.0"
    path = '/etc/os-release'
    # Create an instance of DistributionFiles
    dist = DistributionFiles(basic.AnsibleModule(
        argument_spec={}))
    # Create an instance of CollectedFacts

# Generated at 2022-06-13 02:44:31.360241
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    data = '''NAME=Fedora
VERSION="28 (Cloud Edition)"
ID=fedora
VERSION_ID=28
PRETTY_NAME="Fedora 28 (Cloud Edition)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:28"
HOME_URL="https://fedoraproject.org/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
VARIANT="Cloud Edition"
VARIANT_ID=cloud
'''
    name = 'Fedora'

# Generated at 2022-06-13 02:44:41.540933
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    # Create a mock module to pass into the module constructor
    mock_module = MagicMock()
    # Create a mock ansible facts class to pass into the module constructor
    mock_ansible_facts = MagicMock()
    # Create a DistributionFiles object with the mock objects
    distribution_files = DistributionFiles(mock_module, mock_ansible_facts)
    # Create a dist_files data structure to test the process_dist_files method on

# Generated at 2022-06-13 02:44:46.883162
# Unit test for method get_distribution_facts of class Distribution

# Generated at 2022-06-13 02:44:48.125440
# Unit test for function get_uname
def test_get_uname():
    assert get_uname(str) is not None


# Generated at 2022-06-13 02:44:59.883378
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    df = DistributionFiles()
    distro_facts = {}
    parsed_distro_facts = {}

    # CentOS
    path = '/etc/os-release'
    name = 'CentOS'
    distro_facts['centos_path'] = path
    distro_facts['centos_name'] = name

# Generated at 2022-06-13 02:45:05.706878
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    """
    Test for method _get_distribution_facts of class Distribution
    """
    # darwin test
    import platform
    import copy
    import types
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import Distribution
    from ansible.module_utils.facts.collector.distribution import (get_file_content, get_file_lines, get_uname, get_distribution, _file_exists,
                                                                   DistributionFiles)
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

# Generated at 2022-06-13 02:45:49.503085
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    # Testing with SLES 12 SP5
    # file /etc/SuSE-release
    test1 = """
openSUSE Leap 15.2
VERSION = 15.2
CODENAME = Leap
ID = opensuse
ID_LIKE = suse
PRETTY_NAME = "openSUSE Leap 15.2"
ANSI_COLOR = "0;32"
CPE_NAME = "cpe:/o:opensuse:leap:15.2"
BUG_REPORT_URL = "https://bugs.opensuse.org"
HOME_URL = "https://www.opensuse.org/"
"""
    expected1 = {}
    expected1['distribution'] = 'SUSE'
    expected1['distribution_release'] = '15.2'

    # file /etc/os-release

# Generated at 2022-06-13 02:45:57.136083
# Unit test for method get_distribution_facts of class Distribution
def test_Distribution_get_distribution_facts():
    """get_distribution_facts was tested on Linux, MacOSX and FreeBSD systems, please extend if you have others available"""
    # this is a unit test for the get_distribution_facts method, it is not a functional test
    dist = Distribution(module=AnsibleModule)
    facts = dist.get_distribution_facts()
    assert facts
    assert any([key in facts for key in ['distribution', 'distribution_version', 'distribution_release']])


# ===========================================
# Platform module specific support methods.
#


# Generated at 2022-06-13 02:46:08.720683
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = Mock(return_value=(0, 'Solaris 10 10/09 s10x_u8wos_08a X86', ''))
    module.get_file_content = Mock(return_value='Solaris 10 10/09 s10x_u8wos_08a X86\n Some other text')
    module.file_exists = Mock(return_value=True)
    dist = Distribution(module)
    assert dist.get_distribution_SunOS() == {'distribution': 'Solaris', 'distribution_version': '10', 'distribution_major_version': '10', 'distribution_release': 'Solaris 10 10/09 s10x_u8wos_08a X86'}

# Generated at 2022-06-13 02:46:20.127592
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    d = DistributionFiles({})
    # valid case
    ddata = 'NAME="Clear Linux OS"\nVERSION="28020"\nID=clear-linux-os\nID_LIKE="fedora"\nVERSION_ID="28020"\nPRETTY_NAME="Clear Linux OS"\nANSI_COLOR="0;36"\nCPE_NAME="cpe:/o:clearlinux:clear_linux:28020"\nHOME_URL="https://clearlinux.org/"\nBUG_REPORT_URL="https://github.com/clearlinux/distribution/issues/new"\n'
    res, out = d.parse_distribution_file_ClearLinux("Clear Linux", ddata, "/etc/os-release", {'distribution_major_version': 'NA', 'distribution_version': 'NA'})


# Generated at 2022-06-13 02:46:26.934438
# Unit test for method parse_distribution_file_CentOS of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_CentOS():
    import os
    cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    facts = Facts()
    dist_file_facts = DistributionFiles(facts).parse_distribution_file('CentOS', ['CentOS Stream'], None, facts.FACTS)
    assert dist_file_facts['distribution_release'] == 'Stream'
    os.chdir(cwd)


# Generated at 2022-06-13 02:46:34.328316
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    """
    Test for method get_distribution_OpenBSD
    """
    global SYS_CLASS_PATH
    module = AnsibleModule(argument_spec={})
    module.params.update(
        {
            'path': SYS_CLASS_PATH,
        }
    )
    dist = Distribution(module)
    assert dist.get_distribution_OpenBSD()['distribution_version'] == '6.7'
    assert dist.get_distribution_OpenBSD()['distribution_release'] == 'release'



# Generated at 2022-06-13 02:46:37.611996
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(argument_spec={})
    dist = Distribution(module)
    dist_facts = dist.get_distribution_OpenBSD()
    assert 'distribution_version' in dist_facts
    assert 'distribution_release' in dist_facts


# Generated at 2022-06-13 02:46:43.974472
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    df = DistributionFiles()
    df.module = type('Module', (object,), {})
    df.module.run_command = type('Command', (object,), {})
    df.module.run_command.return_value = 0, "GROUP=stable", ""
    df.module.get_bin_path = type('GetBin', (object,), {})
    df.module.get_bin_path.return_value = 'CoreOS'

    #  "TAG=976.0.0"
    facts = {}
    data = "TAG=976.0.0"

    #  "TAG=976.0.0"
    path = "/etc/os-release"
    result, flatcar_facts = df.parse_distribution_file_Flatcar('Flatcar', data, path, facts)


# Generated at 2022-06-13 02:46:50.419165
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    module = FakeAnsibleModule()
    module.run_command = MagicMock(return_value=(0, '10.13.2', ''))
    dist_obj = Distribution(module=module)
    data = dist_obj.get_distribution_Darwin()
    assert data['distribution'] == 'MacOSX'
    assert data['distribution_major_version'] == '10'
    assert data['distribution_version'] == '10.13.2'


# Generated at 2022-06-13 02:46:53.234472
# Unit test for method parse_distribution_file_Mandriva of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Mandriva():
    test_dist_facts = DistributionFiles()
    test_dist_facts.parse_distribution_file_Mandriva(name="Mandriva",
            data='NAME=Mandriva\nDISTRIB_RELEASE="2011.0"\nDISTRIB_CODENAME="\n"')


# Generated at 2022-06-13 02:47:41.948695
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    """Unit test for method parse_distribution_file_SUSE of class DistributionFiles"""
    distribution = 'SUSE'
    data = """
NAME="openSUSE Leap"
VERSION = "15.0"
ID=opensuse
VERSION_ID="15.0"
PRETTY_NAME="openSUSE Leap 15.0"
ID_LIKE="suse opensuse"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:leap:15.0"
"""
    path = '/etc/os-release'
    collected_facts = {'distribution_release': 'NA', 'distribution_version': 'NA'}
    distribution_files = DistributionFiles()
    distribution_files.module = MagicMock()

# Generated at 2022-06-13 02:47:50.490025
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    module = AnsibleModule(argument_spec={})
    dr = DistributionFiles(module)
    collected_facts = {}
    name = "clearlinux"
    data = """
    NAME="Clear Linux OS"
    VERSION="25030"
    ID=clear-linux-os
    VERSION_ID=25030
    PRETTY_NAME="Clear Linux OS 25030"
    ANSI_COLOR="1;32"
    CPE_NAME="cpe:/o:clearlinux:clearlinux_project:25030"
    HOME_URL="https://clearlinux.org/"
    SUPPORT_URL="https://clearlinux.org/support"
    BUG_REPORT_URL="https://clearlinux.org/community"
    """
    path = "/etc/os-release"

# Generated at 2022-06-13 02:47:53.192706
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule(argument_spec=dict())
    dist = Distribution(module)
    netbsd_facts = dist.get_distribution_NetBSD()
    assert 'distribution' in netbsd_facts
    assert netbsd_facts['distribution'] == 'NetBSD'


# Generated at 2022-06-13 02:47:58.340415
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
  assert DistributionFiles("OpenWrt", "OpenWrt", "", "", "").parse_distribution_file_OpenWrt("OpenWrt", "OpenWrt", "", "") == (True, {'distribution': ' ', 'distribution_release': ' ', 'distribution_version': ' '})


# Generated at 2022-06-13 02:48:05.613098
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    facts = {}
    distro_file = DistributionFiles(None)
    # Debian
    lines = """
PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
VERSION_ID="8"
VERSION="8 (jessie)"
ID=debian
HOME_URL="http://www.debian.org/"
SUPPORT_URL="http://www.debian.org/support/"
BUG_REPORT_URL="https://bugs.debian.org/"
"""
    success, debian_facts = distro_file.parse_distribution_file_Debian(None, lines, '/etc/os-release', facts)
    assert success and debian_facts == {'distribution': 'Debian',
                                        'distribution_release': 'jessie'}


# Generated at 2022-06-13 02:48:10.462317
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    dist_file_facts = DistributionFiles(None, None, None)
    assert dist_file_facts.parse_distribution_file_Amazon("name", "Amazon\n", "path", "collected_facts") is not None


# Generated at 2022-06-13 02:48:16.226282
# Unit test for method parse_distribution_file_OpenWrt of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_OpenWrt():
    from ansible.module_utils.facts.system.distribution import DistributionFiles
    distrofile = DistributionFiles()
    name = ''
    data = ""
    path = ''
    collected_facts = {}
    distrofile.parse_distribution_file_OpenWrt(name, data, path, collected_facts)

# Generated at 2022-06-13 02:48:27.495107
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    from ansible.collection.ansible_collections.ansible.os_family.os_family_facts.plugins.module_utils.facts.system.distribution import get_distribution_Darwin

    # patch
    import ansible.collection.ansible_collections.ansible.os_family.os_family_facts.plugins.module_utils.facts.system.distribution as distribution
    distribution.run_command = lambda cmd: (0, '10.15.5', '')

    result = get_distribution_Darwin()

    assert result == {'distribution': 'MacOSX', 'distribution_major_version': '10', 'distribution_version': '10.15.5'}
    # assert result == {'distribution': 'MacOSX', 'distribution_major_version': '10', 'distribution_version':

# Generated at 2022-06-13 02:48:38.582971
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    # Create an object of type DistributionFiles
    dist_obj = DistributionFiles({})

    # Create an object of type MockedModule
    module_obj = MockedModule({})

    # Create an object of type MockedFactsCollection
    facts_obj = MockedFactsCollection()

    # Set the distribution_file_variety as "Amazon"
    # Valid values for distribution_file_variety are
    # "Amazon", "Debian", "Mandriva", "NA", "OpenWrt", "SUSE", "Alpine", "Coreos", "Flatcar", "ClearLinux"
    name = "Amazon"
    # Set the distribution_file_path as "/etc/os-release"
    path = "/etc/os-release"
    # Set the distribution_file_content as the output of the command
    # cat /etc/os-

# Generated at 2022-06-13 02:48:46.194015
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    # NOTE: This function is a unit test for method parse_distribution_file_Slackware of class DistributionFiles
    # FIXME: Write unit test for parse_distribution_file_Slackware
    #assert parse_distribution_file_Slackware('Slackware_data', 'Slackware_path', 'Slackware_collected_facts') == 'Slackware_facts'
    # TODO: Fix the unit test
    assert False, 'FIXME: Write unit test for parse_distribution_file_Slackware'

# Generated at 2022-06-13 02:49:09.460306
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule({})
    distribution = Distribution(module)
    netbsd_facts = distribution.get_distribution_NetBSD()
    assert 'distribution_release' in netbsd_facts
    assert 'distribution_major_version' in netbsd_facts
    assert 'distribution_version' in netbsd_facts

# Generated at 2022-06-13 02:49:14.619156
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    dragonfly_facts = distribution.get_distribution_DragonFly()
    info = dragonfly_facts['distribution_release']
    rc, out, dummy = module.run_command("/sbin/sysctl -n kern.version")
    expected_result = re.search(r'v(\d+)\.(\d+)\.(\d+)-(RELEASE|STABLE|CURRENT).*', out)
    if expected_result:
        expected_result = '%s.%s.%s' % expected_result.groups()[:3]
    assert dragonfly_facts['distribution_version'] is expected_result



# Generated at 2022-06-13 02:49:25.726577
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    distributionFiles = DistributionFiles(DistributionFilesTestModule())
    res = distributionFiles.parse_distribution_file_Debian('Debian', 'Ubuntu', '', {'distribution_release': 'NA'})
    assert res == (True, {'distribution': 'Ubuntu'})

    res = distributionFiles.parse_distribution_file_Debian('Debian', 'Ubuntu', '/etc/os-release', {'distribution_release': 'NA'})
    assert res == (True, {'distribution': 'Ubuntu'})

    res = distributionFiles.parse_distribution_file_Debian('Debian', '', '', {'distribution_release': 'NA'})
    assert res == (False, {})


# Generated at 2022-06-13 02:49:30.364660
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    distribution = Distribution(MagicMock())
    expected = {'distribution': 'MacOSX', 'distribution_major_version': '19', 'distribution_version': '19.0.0'}
    assert distribution.get_distribution_Darwin() == expected



# Generated at 2022-06-13 02:49:39.885492
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles

# Generated at 2022-06-13 02:49:44.827266
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    module = AnsibleModule({})
    distribution = Distribution(module)
    out = distribution.get_distribution_NetBSD()
    assert out['distribution_release'] == '7.0_STABLE'
    assert out['distribution_version'] == '7.0'
    assert out['distribution_major_version'] == '7'



# Generated at 2022-06-13 02:49:47.287666
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    module = None
    dist = Distribution(module)
    dist.get_distribution_AIX()

# Generated at 2022-06-13 02:49:55.888927
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles

# Generated at 2022-06-13 02:50:01.792493
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    print("******* In method test_Distribution_get_distribution_DragonFly *******")

    from ansible.module_utils.facts import Distribution
    from ansible.module_utils.basic import AnsibleModule

    distribution = Distribution(AnsibleModule())
    print("******* In method test_Distribution_get_distribution_DragonFly *******")
    out = distribution.get_distribution_DragonFly()
    print("******* OUTPUT: {}".format(out))


# Generated at 2022-06-13 02:50:12.678789
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles

# Generated at 2022-06-13 02:50:47.973472
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    module = AnsibleModule(argument_spec=dict())

    # Test Debian
    data = '''PRETTY_NAME="Debian GNU/Linux 8 (jessie)"
NAME="Debian GNU/Linux"
VERSION_ID="8"
VERSION="8 (jessie)"
ID=debian
HOME_URL="http://www.debian.org/"
SUPPORT_URL="http://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"'''
    path = '/etc/os-release'
    dist_variety = 'Debian'
    dist_name = 'NA'
    collected_facts = {'distribution': 'NA', 'distribution_version': 'NA', 'distribution_release': 'NA', 'distribution_major_version': 'NA'}
    dist_file_facts