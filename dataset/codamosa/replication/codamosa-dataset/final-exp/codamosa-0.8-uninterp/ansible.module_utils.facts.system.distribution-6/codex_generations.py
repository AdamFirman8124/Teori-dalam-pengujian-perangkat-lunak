

# Generated at 2022-06-13 02:41:32.837949
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    #
    # Test on Amazon Linux
    #
    test_data = {
        'distribution': 'Amazon',
        'distribution_version': '2010.09',
    }
    test_data_etc_os_release = '''
NAME="Amazon Linux"
VERSION="2010.09"
ID="amzn"
ID_LIKE="rhel fedora"
VERSION_ID="2010.09"
PRETTY_NAME="Amazon Linux AMI 2010.09"
ANSI_COLOR="0;33"
CPE_NAME="cpe:/o:amazon:linux:2010.09:ga"
HOME_URL="http://aws.amazon.com/amazon-linux-ami/"
'''

# Generated at 2022-06-13 02:41:36.859223
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    dragonfly_facts = Distribution.get_distribution_DragonFly(module)
    assert dragonfly_facts['distribution_release'] == platform.release()

# Generated at 2022-06-13 02:41:43.288714
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'HPUX.OE.11.31-B.13.15', ''))
    distro = Distribution(module)
    facts = distro.get_distribution_HPUX()
    assert facts == {
        'distribution_version': 'B.13',
        'distribution_release': '15',
    }


# Generated at 2022-06-13 02:41:51.994453
# Unit test for method get_distribution_NetBSD of class Distribution
def test_Distribution_get_distribution_NetBSD():
    print(('Running test_Distribution_get_distribution_NetBSD'))

    module = MagicMock()
    module.run_command = MagicMock(return_value=[0, 'NetBSD 8.0_STABLE (GENERIC) #1: Thu Feb 14 11:29:56 CST 2019', ''])
    dist = Distribution(module)

    distro_data = dist.get_distribution_NetBSD()

    assert distro_data['distribution_major_version'] == '8'
    assert distro_data['distribution_version'] == '8.0'
    assert distro_data['distribution_release'] == '8.0_STABLE'


# Generated at 2022-06-13 02:41:59.015327
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    OpenBSD_release = '5.5'
    out = "OpenBSD 5.5 (GENERIC) #2: Mon Mar 31 19:40:15 MDT 2014     deraadt@amd64.openbsd.org:/usr/src/sys/arch/amd64/compile/GENERIC"
    # ommit the last two attrs. of the dict.
    OpenBSD_dict = {'distribution_release': '5.5', 'distribution_version': '5.5'}
    # initialize a Distribution object
    distributed_object = Distribution(run_command=None)
    # attrs. of distributed_object are set
    distributed_object.module.run_command = lambda x: (0, out, '')
    distributed_object.module.platform.release = lambda: OpenBSD_release
    # call to get_

# Generated at 2022-06-13 02:42:03.556825
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    test_obj = Distribution(module='dummy')
    test_obj.module.run_command = MagicMock(return_value=(0, "/usr/bin/sw_vers -productVersion\r10.8.5\r", ""))
    test_facts = test_obj.get_distribution_Darwin()
    assert test_facts == {'distribution': 'MacOSX', 'distribution_major_version': '10', 'distribution_version': '10.8.5'}

# Generated at 2022-06-13 02:42:11.125871
# Unit test for method get_distribution_SunOS of class Distribution

# Generated at 2022-06-13 02:42:13.580244
# Unit test for function get_uname
def test_get_uname():
    """
    Unit test to check results of get_uname
    """
    assert get_uname('-v') == os.uname()[3]


# Generated at 2022-06-13 02:42:27.247393
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = get_test_module()
    dist = Distribution(module)

    # Test the case when the command run fails
    module.run_command = run_command_mock
    run_command_mock.side_effect = [(1, 'stdout', 'stderr')]
    hpux_facts = dist.get_distribution_HPUX()
    assert hpux_facts == {}

    # Test the case when the command fails and there is a stderr
    module.run_command = run_command_mock
    run_command_mock.side_effect = [(2, 'stdout', 'stderr')]
    hpux_facts = dist.get_distribution_HPUX()
    assert hpux_facts == {}

    # Test the case when the command run is successful

# Generated at 2022-06-13 02:42:38.432656
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    data = """
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
"""
    name = "NA"
    path = ""
    collected_facts = {}
    collected_facts['lsb'] = {}
    collected_facts['lsb']['codename'] = "NA"
    collected_facts['distribution_release'] = "NA"
    df = DistributionFiles()

# Generated at 2022-06-13 02:43:38.510062
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(argument_spec={})
    # Determining OpenBSD version
    # test data for OpenBSD 5.6
    # OpenBSD 5.6-current (GENERIC) #2: Thu Mar  5 06:51:29 MST 2015
    # testmd = mock.MagicMock(return_value=0)
    # setattr(Distribution, 'run_command', testmd)
    testout = 'OpenBSD 5.6-current (GENERIC) #2: Thu Mar  5 06:51:29 MST 2015'
    testmd = mock.MagicMock(return_value=(0,testout,''))
    setattr(module, 'run_command', testmd)
    testdata = Distribution(module).get_distribution_OpenBSD()

# Generated at 2022-06-13 02:43:50.565081
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    # TODO: add unit tests for class
    # TODO: use more advanced testing framework than unittest
    DF = DistributionFiles()
    collected_facts = {}
    import inspect
    # these are the parser methods
    test_methods = [n for n, v in inspect.getmembers(DF, predicate=inspect.ismethod) if n.startswith('parse_distribution_file_')]
    tested_methods = []
    for distro in DF.file_varieties.keys():
        method_name = 'parse_distribution_file_' + distro
        if method_name not in test_methods:
            continue
        test_data = "foo bar baz"
        result = getattr(DF, method_name)(distro, test_data, '', collected_facts)
        assert type(result)

# Generated at 2022-06-13 02:43:59.323850
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    module = AnsibleModule(argument_spec={})

    df = DistributionFiles(module)

    name = 'Amazon'
    data = 'NAME=Amazon\n'
    path = '/etc/os-release'
    collected_facts = {'distribution': 'Amazon',
        'distribution_file_path': path,
        'distribution_file_variety': name,
        'distribution_file_parsed': False,
        'distribution_major_version': '',
        'distribution_minor_version': '',
        'distribution_version': '',
        'distribution_release': '',
        'distribution_codename': '',
    }


# Generated at 2022-06-13 02:44:02.318599
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    module = Mock()
    out = 'HPUX.OE.B.02.01.000.340.0.2141.6886346.1'
    module.run_command.return_value = 0, out, ''
    distribution = Distribution(module)
    result = distribution.get_distribution_HPUX()
    assert result == {'distribution_version': 'B.02', 'distribution_release': '1'}

# Generated at 2022-06-13 02:44:10.316585
# Unit test for method parse_distribution_file_Debian of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Debian():
    test_obj = DistributionFiles()
    params = {}
    name = 'Debian'
    data = '''
NAME="Debian GNU/Linux"
ID_LIKE=debian
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
VERSION_ID="9"
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
'''
    path = '/etc/os-release'
    collected_facts = {'distribution': 'Debian', 'distribution_version': '9', 'distribution_major_version': '9'}

# Generated at 2022-06-13 02:44:22.224945
# Unit test for method get_distribution_HPUX of class Distribution
def test_Distribution_get_distribution_HPUX():
    """
    Test method get_distribution_HPUX of class Distribution
    """
    f = os.path.basename(__file__)
    if f.endswith('.pyc') or f.endswith('.pyo'):
        pytest.skip('cannot run test with a compiled python file')
    if not HAS_PLATFORM:
        pytest.skip('Platform not available')
    if not platform.system() == 'HP-UX':
        pytest.skip('test only for HP-UX')
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    hpux_facts = distribution.get_distribution_HPUX()
    assert hpux_facts == {'distribution_version': 'B.11.31', 'distribution_release': '169920'}

# Generated at 2022-06-13 02:44:26.022636
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    distribution_facts = distribution.get_distribution_DragonFly()

    assert distribution_facts['distribution_release'] == platform.release()
    assert distribution_facts['distribution_version'] == '5.2.2'
    pass



# Generated at 2022-06-13 02:44:37.514544
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    with mock.patch.object(DistributionFiles, 'get_file_content', return_value="openSUSE Leap 42.3 (x86_64)\nVERSION = 42.3\nCODENAME = Malachite\n"):
        dist_file_facts = DistributionFiles().parse_distribution_file_SUSE('SUSE', 'openSUSE Leap 42.3 (x86_64)\nVERSION = 42.3\nCODENAME = Malachite\n', '/etc/SuSE-release', {'distribution_version': 'NA', 'lsb': {'distrib_id': 'NA', 'distrib_release': 'NA', 'distrib_codename': 'NA', 'distrib_description': 'NA'}})
        assert dist_file_facts['distribution'] == 'openSUSE'
        assert dist_file

# Generated at 2022-06-13 02:44:44.705031
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():
    df = DistributionFiles()
    m = MagicMock()
    facts = {}
    name = "Flatcar Linux"
    data = "[Flatcar]\nGROUP=stable\n"
    path = "/etc/flatcar/release"
    collected_facts = {}
    ret = df.parse_distribution_file_Flatcar(name, data, path, collected_facts)
    assert ret[0]
    assert ret[1]['distribution_release'] == 'stable'


# Generated at 2022-06-13 02:44:51.078897
# Unit test for method parse_distribution_file_CentOS of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_CentOS():
    from ansible.module_utils.facts.collector import DistributionFiles
    from ansible.module_utils.facts import Collector
    distrof = DistributionFiles(Collector)
    f = open(os.path.join(os.path.dirname(__file__), 'files/redhat_release'), 'r')
    data = f.read()
    f.close()
    centos_facts = distrof.parse_distribution_file_CentOS('redhat_release', data, '/etc/redhat-release', {})
    assert centos_facts == (False, {})
    f = open(os.path.join(os.path.dirname(__file__), 'files/redhat_release_centos_stream'), 'r')
    data = f.read()
    f.close()
    centos_facts

# Generated at 2022-06-13 02:45:44.166050
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    # Setup
    module = MockModule()
    module.run_command.side_effect = [
        (0, 'v5.6.2', ''),
        (0, 'v5.6.2', ''),
    ]
    distribution = Distribution(module=module)
    # Test
    expected = {'distribution_release': '5.6-RELEASE', 'distribution_version': '5.6.2'}
    actual = distribution.get_distribution_DragonFly()
    # Verify
    assertEqual(expected, actual, "distribution: DragonFly")

# Generated at 2022-06-13 02:45:49.101816
# Unit test for method get_distribution_Darwin of class Distribution
def test_Distribution_get_distribution_Darwin():
    for fact, value in [('distribution', 'MacOSX'),
                        ('distribution_version', '10.14'),
                        ('distribution_major_version', '10')]:
        assert(fact in distribution_object.get_distribution_Darwin())
        assert(distribution_object.get_distribution_Darwin()[fact] == value)


# Generated at 2022-06-13 02:46:00.551373
# Unit test for method parse_distribution_file_Slackware of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Slackware():
    """ tests the method parse_distribution_file_Slackware
    """
    collection_obj = DistributionFiles()
    collection_obj.module = AnsibleModule(argument_spec={})
    collection_obj.module.exit_json = Mock()
    collection_obj.module.fail_json = Mock()
    collection_obj.module.params = {}
    collection_obj.file_paths = ['/etc/slackware-version']
    collection_obj.distribution_name = 'Slackware'
    fd, temp_file = tempfile.mkstemp()
    with open(temp_file, 'w') as f:
        f.write('Slackware 12.1.0')

# Generated at 2022-06-13 02:46:10.919954
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    oslevel_old = {'rc': 0, 'stdout': '7.1\n', 'stderr': ''}
    oslevel_new = {'rc': 0, 'stdout': '7.1.3.0\n', 'stderr': ''}
    module = get_platform_module(oslevel_old)
    distribution = Distribution(module)

    aix_facts = distribution.get_distribution_AIX()

    assert aix_facts['distribution_version'] == '7.1'
    assert aix_facts['distribution_major_version'] == '7'

    module = get_platform_module(oslevel_new)
    distribution = Distribution(module)

    aix_facts = distribution.get_distribution_AIX()


# Generated at 2022-06-13 02:46:17.854585
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    # Get test data from file
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    results = Distribution(module).get_distribution_SunOS()
    assert results['distribution'] == 'Solaris'
    assert results['distribution_version'] == '11.2'
    assert results['distribution_release'] == 'Oracle Solaris'
    assert results['distribution_major_version'] == '11'


# Generated at 2022-06-13 02:46:28.909943
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    dist_files = DistributionFiles()
    data = """# /etc/system-release doesn't exist in Amazon Linux 2
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"

Amazon Linux AMI release 2018.03
"""
    path = "/etc/system-release"
    facts = {'distribution': 'NA', 'distribution_version': 'NA'}

    facts = dist_files.parse_distribution_file("Amazon", data, path, facts)

# Generated at 2022-06-13 02:46:36.291898
# Unit test for method parse_distribution_file_Coreos of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Coreos():
    distro_files = DistributionFiles()
    data = "GROUP=alpha\n"
    name = 'CoreOS'
    path = '/etc/os-release'
    distro = get_distribution()
    collected_facts = {'distribution_major_version': 'NA', 'distribution_version': 'NA'}
    _result = distro_files.parse_distribution_file_Coreos(name, data, path, collected_facts)
    assert _result[0]
    assert _result[1]['distribution_release'] == 'alpha'

# Generated at 2022-06-13 02:46:39.668302
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    assert Distribution.get_distribution_SunOS(None).get('distribution',None) == 'Solaris'
    assert Distribution.get_distribution_SunOS(None).get('distribution_release',None) == 'Oracle Solaris 11.4 SPARC'
    assert Distribution.get_distribution_SunOS(None).get('distribution_version',None) == '11.4'
    assert Distribution.get_distribution_SunOS(None).get('distribution_major_version',None) == '11'

# Generated at 2022-06-13 02:46:41.702145
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    assert Distribution.get_distribution_OpenBSD(None)['distribution_version'] == platform.release()
    assert Distribution.get_distribution_OpenBSD(None)['distribution_release'] == 'RELEASE'



# Generated at 2022-06-13 02:46:43.696652
# Unit test for method process_dist_files of class DistributionFiles
def test_DistributionFiles_process_dist_files():
    # TODO: implement
    return True

# Generated at 2022-06-13 02:47:50.334203
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    dist_files = DistributionFiles()
    collected_facts = {"distribution_version":"15", "distribution_release":"NA"}
    function = dist_files.parse_distribution_file_SUSE

    # example data from 15.0 /etc/os-release
    data = '''This is the SUSE Linux Enterprise Server 15 release.
NAME="SLES"
VERSION="15"
VERSION_ID="15"
PRETTY_NAME="SUSE Linux Enterprise Server 15"
ID="sles"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:suse:sles:15"
'''
    retval = function("SUSE", data, "/etc/os-release", collected_facts)
    assert retval[0] == True
    assert retval[1]['distribution'] == 'SLES'

# Generated at 2022-06-13 02:48:00.786278
# Unit test for method parse_distribution_file_ClearLinux of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_ClearLinux():
    fake_module = FakeLoadableModule()
    distfile_parser = DistributionFiles(fake_module)
    # os-release with contents from https://github.com/clearlinux/clr-distro-images/blob/master/os-release
    data = "NAME=\"Clear Linux OS\"\nID=clear-linux-os\nVERSION=\"27680\"\nVERSION_ID=\"27680\"\nPRETTY_NAME=\"Clear Linux OS (Container)\"\nANSI_COLOR=\"38;2;0;198;255\"\nHOME_URL=\"https://clearlinux.org/\"\nSUPPORT_URL=\"https://clearlinux.org/support/\"\nBUG_REPORT_URL=\"https://github.com/clearlinux/clr-distro-images/issues\"\n"
    name = "clearlinux"
    path

# Generated at 2022-06-13 02:48:06.726639
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    """Unit test for method get_distribution_DragonFly of class Distribution"""
    import sys
    import platform
    distribution_object = Distribution('')
    # DragonFly
    sys.platform = 'dragonfly'
    platform.system = lambda: 'DragonFly'
    platform.release = lambda: '3.2.1-RELEASE'
    platform.version = lambda: 'DragonFly v3.2.1.2.g8a5f002-RELEASE #1: Wed Jul 31 21:18:35 UTC 2013 root@pkgbox32.dragonflybsd.org:/usr/obj/build/home/justin/src/sys/X86_64_GENERIC x86_64'
    results = distribution_object.get_distribution_DragonFly()

# Generated at 2022-06-13 02:48:09.432047
# Unit test for method get_distribution_DragonFly of class Distribution
def test_Distribution_get_distribution_DragonFly():
    test_module = 'ansible.module_utils.facts.system.distribution'
    test_class = 'Distribution'
    test_func = 'get_distribution_DragonFly'
    test_class_instance = 'distribution'

    testcase = UnitTest(test_module, test_class, test_func, test_class_instance)

    testcase.runTest()

# Generated at 2022-06-13 02:48:21.338709
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles

# Generated at 2022-06-13 02:48:27.813232
# Unit test for method parse_distribution_file_CentOS of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_CentOS():
    df = DistributionFiles()
    name = 'CentOS'
    data = 'CentOS Stream'
    path = '/etc/centos-release'
    collected_facts = {}
    expected_results = {'distribution_release': 'Stream'}
    actual_results = df.parse_distribution_file_CentOS(name, data, path, collected_facts)
    assert expected_results == actual_results[1]



# Generated at 2022-06-13 02:48:38.822976
# Unit test for method get_distribution_SunOS of class Distribution
def test_Distribution_get_distribution_SunOS():
    '''
    Get a dict of solaris facts from the output of platform.release()
    and /etc/release
    '''

# Generated at 2022-06-13 02:48:44.773429
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module)
    facts = distribution.get_distribution_OpenBSD()
    assert facts['distribution_version'] == platform.release()
    rc, out, err = module.run_command("/sbin/sysctl -n kern.version")
    assert facts['distribution_release'] == out.split()[-2]



# Generated at 2022-06-13 02:48:55.091517
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    """Test method parse_distribution_file_Amazon of class DistributionFiles"""
    distribution_files = DistributionFiles(None)
    data = """NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"

ONE="1"
TWO="2"
TWO="22"
THREE="3"
TWO_THREE="2"
FOUR="4"
FIVE="5"
"""

# Generated at 2022-06-13 02:49:03.591258
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    out = """OpenBSD 5.7-stable (GENERIC) #1: Sun May 17 19:52:04 MDT 2015"""
    module = FakeAnsibleModule(platform=defaultdict(str, release='5.7-stable', version=out),
                               command_fn=lambda *args, **kwargs: (0, out, ''))
    dist = Distribution(module)
    dist_facts = dist.get_distribution_OpenBSD()
    assert dist_facts['distribution_version'] == '5.7'
    assert dist_facts['distribution_release'] == 'stable'

# Generated at 2022-06-13 02:50:03.292591
# Unit test for method parse_distribution_file_SUSE of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_SUSE():
    # TODO:
    # this is a stub for test_parse_distribution_file_SUSE
    data_dir = os.path.dirname(os.path.dirname(__file__))
    # expected = {'distribution': 'SLES', 'distribution_version': '3.0'}
    expected = {'distribution': 'SLES_SAP', 'distribution_version': '3.0'}

    if os.path.exists(data_dir + '/system_facts/distribution_files/suse-release'):
        # Test for SLES
        df = DistributionFiles()
        collected_facts = {'distribution_release': 'NA', 'distribution_version': '3.0'}

# Generated at 2022-06-13 02:50:13.518218
# Unit test for method parse_distribution_file_NA of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_NA():
    dist_file_obj = DistributionFiles({})

# Generated at 2022-06-13 02:50:16.994173
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    module = AnsibleModule(argument_spec={})
    distrib = Distribution(module)
    data = distrib.get_distribution_OpenBSD()
    assert data['distribution_release'] == "5.5"


# Generated at 2022-06-13 02:50:24.461228
# Unit test for method parse_distribution_file_Flatcar of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Flatcar():

    # Create a DistributionFiles object
    df = DistributionFiles()

    # Create a ModuleAnsibleCore object
    ma = ModuleAnsibleCore()

    # Make a fake /etc/os-release that looks like flatcar
    fake_data = {'/etc/os-release':'NAME=Flatcar\nID=flatcar\nVERSION_ID=2512.3.0\nGROUP=stable\nLIBC=glibc'}
    # Add the fake data to the module imports
    ma.module_imports['os.path'] = os.path
    ma.module_imports['__builtin__'] = __builtin__
    ma.module_imports['platform'] = platform
    ma.module_imports['platform'].system = MagicMock(return_value = 'Linux')

# Generated at 2022-06-13 02:50:32.867036
# Unit test for method parse_distribution_file_Amazon of class DistributionFiles
def test_DistributionFiles_parse_distribution_file_Amazon():
    centos_facts = {}
    dist_file_facts = {}
    path = '/etc/os-release'
    data = "NAME=\"Amazon Linux AMI\"\nVERSION=\"2018.03\"\nID=\"amzn\"\nID_LIKE=\"rhel fedora\"\nVERSION_ID=\"2018.03\"\nPRETTY_NAME=\"Amazon Linux AMI 2018.03\"\nANSI_COLOR=\"0;33\"\nCPE_NAME=\"cpe:/o:amazon:linux:2018.03:ga\"\nHOME_URL=\"http://aws.amazon.com/amazon-linux-ami/\"\n\n"
    distribution_file_parsers = DistributionFiles(module).distribution_file_parsers

# Generated at 2022-06-13 02:50:37.478458
# Unit test for method get_distribution_AIX of class Distribution
def test_Distribution_get_distribution_AIX():
    # Create a class instance
    module = AnsibleModule(argument_spec={})
    distribution = Distribution(module=module)

    # Run the code to be tested
    result = distribution.get_distribution_AIX()

    # Check the results
    assert result['distribution_major_version'] == '7'


# Generated at 2022-06-13 02:50:47.178200
# Unit test for method get_distribution_OpenBSD of class Distribution
def test_Distribution_get_distribution_OpenBSD():
    '''
    Test that OpenBSD can be correctly identified.
    '''
    # Make our module
    module = AnsibleModule(argument_spec={}, supports_check_mode=False,
                           bypass_checks=True)
    # Instantiate Distribution instance and call the get_distribution_OpenBSD method
    distribution_instance = Distribution(module=module)
    distribution_facts = distribution_instance.get_distribution_OpenBSD()
    # Assert the distribution, distribution release and distribution version are correct
    assert_equals('OpenBSD', distribution_facts['distribution'])
    assert_equals('6.1', distribution_facts['distribution_version'])
    assert_equals('release', distribution_facts['distribution_release'])

