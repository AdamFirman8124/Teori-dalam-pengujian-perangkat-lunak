

# Generated at 2024-05-31 00:51:48.372390
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the platform.system and distro functions
    import mock

    with mock.patch('platform.system', return_value='Linux'):
        with mock.patch('ansible.module_utils.distro.id', return_value='centos'):
            with mock.patch('ansible.module_utils.distro.version', return_value='7.5'):
                assert get_distribution_version() == '7.5'

        with mock.patch('ansible.module_utils.distro.id', return_value='debian'):
            with mock.patch('ansible.module_utils.distro.version', return_value='10'):
                with mock.patch('ansible.module_utils.distro.version', return_value='10.1', best=True):
                    assert get_distribution_version() == '10.1'


# Generated at 2024-05-31 00:51:51.646261
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:51:55.025238
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:51:58.923031
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.6.1810'
    distro.version_best = lambda: '7.6.1810'

    assert get_distribution_version() == '7.6'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'
    distro.version_best = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:52:00.250801
# Unit test for function get_distribution
def test_get_distribution():    assert get_distribution() is not None

# Generated at 2024-05-31 00:52:02.879502
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() is None

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:52:06.165356
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:08.572563
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:52:11.606151
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:52:14.909679
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:28.522891
# Unit test for function get_distribution
def test_get_distribution():    expected_distributions = {
        'amzn': 'Amazon',
        'rhel': 'Redhat',
        '': 'OtherLinux'
    }


# Generated at 2024-05-31 00:52:31.645589
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:34.719598
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:38.292214
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:52:41.435377
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:52:45.349438
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:49.574936
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mocking the distro module
    class MockDistro:
        def __init__(self, id_value, version_value, version_best_value=None):
            self._id = id_value
            self._version = version_value
            self._version_best = version_best_value

        def id(self):
            return self._id

        def version(self, best=False):
            if best and self._version_best:
                return self._version_best
            return self._version

    # Test cases

# Generated at 2024-05-31 00:52:51.942608
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:52:56.199291
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:52:58.643126
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:53:12.969375
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:53:16.853720
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.5.1804'
    distro.version_best = lambda: '7.5'

    assert get_distribution_version() == '7.5'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:53:20.206835
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:53:23.271487
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:53:26.836256
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:53:29.324802
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:53:32.576850
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.6.1810'
    distro.version_best = lambda: '7.6.1810'

    assert get_distribution_version() == '7.6'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'
    distro.version_best = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:53:37.779416
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.6.1810'
    distro.version_best = lambda: '7.6.1810'
    assert get_distribution_version() == '7.6'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'
    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'
    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None
    assert get_distribution_version() == ''

    platform.system = lambda: 'Windows'
    assert get_distribution_version() is None


# Generated at 2024-05-31 00:53:39.956290
# Unit test for function get_distribution
def test_get_distribution():    expected_distributions = {
        'amzn': 'Amazon',
        'rhel': 'Redhat',
        '': 'OtherLinux'
    }


# Generated at 2024-05-31 00:53:43.722545
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mocking the distro module
    class MockDistro:
        def __init__(self, id_value, version_value, version_best_value=None):
            self._id = id_value
            self._version = version_value
            self._version_best = version_best_value

        def id(self):
            return self._id

        def version(self, best=False):
            if best and self._version_best:
                return self._version_best
            return self._version

    # Test cases

# Generated at 2024-05-31 00:54:08.332281
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:54:12.285613
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:54:16.669248
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    # Mock platform.system to return 'Linux'
    platform.system = lambda: 'Linux'
    
    # Mock distro.os_release_info to return a dictionary with 'version_codename'
    distro.os_release_info = lambda: {'version_codename': 'focal'}
    assert get_distribution_codename() == 'focal'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' but with 'ubuntu_codename'
    distro.os_release_info = lambda: {'ubuntu_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' and 'ubuntu_codename'
    distro.os_release_info = lambda: {}
    distro.id = lambda: 'ubuntu'
    distro.lsb_release_info = lambda: {'codename': 'xenial'}
    assert get_distribution_codename() == 'xenial'
    
    # Mock

# Generated at 2024-05-31 00:54:18.314879
# Unit test for function get_distribution
def test_get_distribution():    assert get_distribution() is not None

# Generated at 2024-05-31 00:54:23.835520
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:54:28.603653
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    # Mock platform.system to return 'Linux'
    platform.system = lambda: 'Linux'
    
    # Mock distro.os_release_info to return a dictionary with 'version_codename'
    distro.os_release_info = lambda: {'version_codename': 'focal'}
    assert get_distribution_codename() == 'focal'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' but with 'ubuntu_codename'
    distro.os_release_info = lambda: {'ubuntu_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' and 'ubuntu_codename'
    distro.os_release_info = lambda: {}
    distro.id = lambda: 'ubuntu'
    distro.lsb_release_info = lambda: {'codename': 'xenial'}
    assert get_distribution_codename() == 'xenial'
    
    # Mock

# Generated at 2024-05-31 00:54:32.539655
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:54:34.527902
# Unit test for function get_distribution
def test_get_distribution():    expected_distributions = {
        'amzn': 'Amazon',
        'rhel': 'Redhat',
        '': 'OtherLinux'
    }


# Generated at 2024-05-31 00:54:37.703221
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:54:41.479487
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:07.484071
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.6.1810'
    distro.version_best = lambda: '7.6.1810'

    assert get_distribution_version() == '7.6'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:55:10.960567
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:15.265134
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:19.412805
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:55:23.114265
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:25.972827
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:29.015959
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mocking the distro module
    class MockDistro:
        def __init__(self, id_value, version_value, version_best_value=None):
            self._id = id_value
            self._version = version_value
            self._version_best = version_best_value

        def id(self):
            return self._id

        def version(self, best=False):
            if best and self._version_best:
                return self._version_best
            return self._version

    # Test cases

# Generated at 2024-05-31 00:55:32.655684
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    # Mock platform.system to return 'Linux'
    platform.system = lambda: 'Linux'
    
    # Mock distro.os_release_info to return a dictionary with 'version_codename'
    distro.os_release_info = lambda: {'version_codename': 'focal'}
    assert get_distribution_codename() == 'focal'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' but with 'ubuntu_codename'
    distro.os_release_info = lambda: {'ubuntu_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'
    
    # Mock distro.os_release_info to return a dictionary without 'version_codename' and 'ubuntu_codename'
    distro.os_release_info = lambda: {}
    distro.id = lambda: 'ubuntu'
    distro.lsb_release_info = lambda: {'codename': 'xenial'}
    assert get_distribution_codename() == 'xenial'
    
    # Mock

# Generated at 2024-05-31 00:55:35.794423
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:55:38.947122
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:56:28.909708
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.6.1810'
    distro.version_best = lambda: '7.6.1810'

    assert get_distribution_version() == '7.6'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:56:34.220829
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:56:35.915287
# Unit test for function get_distribution
def test_get_distribution():    expected_distributions = {
        'amzn': 'Amazon',
        'rhel': 'Redhat',
        '': 'OtherLinux'
    }


# Generated at 2024-05-31 00:56:38.789761
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:56:41.717573
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:56:45.190168
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.5.1804'
    distro.version_best = lambda: '7.5'

    assert get_distribution_version() == '7.5'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'
    distro.version_best = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:56:48.877159
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:56:50.787664
# Unit test for function get_distribution
def test_get_distribution():    expected_distributions = {
        'amzn': 'Amazon',
        'rhel': 'Redhat',
        '': 'OtherLinux'
    }


# Generated at 2024-05-31 00:56:54.312163
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:56:57.698522
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:57:47.583805
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() is None

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:57:51.191076
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:57:53.187128
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:57:56.493299
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.5.1804'
    distro.version_best = lambda: '7.5'

    assert get_distribution_version() == '7.5'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '18.04'

    assert get_distribution_version() == '18.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:57:59.534702
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:58:00.224306
# Unit test for function get_distribution
def test_get_distribution():    assert get_distribution() is not None

# Generated at 2024-05-31 00:58:01.267898
# Unit test for function get_distribution
def test_get_distribution():    assert get_distribution() is not None

# Generated at 2024-05-31 00:58:04.667303
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:58:08.789664
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:58:12.960924
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:58:59.548217
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 00:59:03.611410
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:59:08.371076
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:59:12.002993
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:59:16.181243
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:59:19.767237
# Unit test for function get_distribution_version
def test_get_distribution_version():    # Mock the distro module functions
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.5.1804'
    distro.version_best = lambda: '7.5.1804'

    assert get_distribution_version() == '7.5'

    distro.id = lambda: 'debian'
    distro.version = lambda: '10'
    distro.version_best = lambda: '10.1'

    assert get_distribution_version() == '10.1'

    distro.id = lambda: 'ubuntu'
    distro.version = lambda: '20.04'

    assert get_distribution_version() == '20.04'

    distro.id = lambda: 'unknown'
    distro.version = lambda: None

    assert get_distribution_version() == ''


# Generated at 2024-05-31 00:59:23.087228
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:59:26.604918
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 00:59:30.839767
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 00:59:33.011259
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() is None

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 01:00:22.554411
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 01:00:26.464448
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 01:00:29.719957
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 01:00:33.360797
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 01:00:36.005946
# Unit test for function get_distribution
def test_get_distribution():    # Mock the platform.system and distro.id functions
    original_platform_system = platform.system
    original_distro_id = distro.id

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'

    distro.id = lambda: 'rhel'
    assert get_distribution() == 'Redhat'

    distro.id = lambda: ''
    assert get_distribution() == 'OtherLinux'

    platform.system = lambda: 'Windows'
    assert get_distribution() == ''

    # Restore the original functions
    platform.system = original_platform_system
    distro.id = original_distro_id


# Generated at 2024-05-31 01:00:39.432346
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 01:00:45.150190
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 01:00:48.124740
# Unit test for function get_platform_subclass

# Generated at 2024-05-31 01:00:51.159047
# Unit test for function get_distribution_codename
def test_get_distribution_codename():    import pytest

# Generated at 2024-05-31 01:00:54.130024
# Unit test for function get_platform_subclass