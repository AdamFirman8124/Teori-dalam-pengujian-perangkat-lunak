

# Generated at 2026-10-25 09:38:13.616702
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:16.031128
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:18.447585
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:20.863107
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:23.276804
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:25.691664
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:28.107777
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:30.523382
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:32.935964
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:35.349051
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:37.765095
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:40.179976
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:42.596004
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:45.008050
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:47.426305
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:49.836358
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:52.252118
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:54.665532
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:57.079622
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:38:59.494019
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:01.908906
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:05.634276
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:07.067612
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:08.403866
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:11.469426
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:39:16.075357
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:39:18.944363
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:39:40.037259
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:42.678875
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:45.092896
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:47.509602
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:49.925446
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:52.510854
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:54.918766
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:57.332498
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:39:59.753350
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:40:02.165326
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:40:04.579870
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:40:06.997477
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:40:38.639960
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:40:56.431997
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:40:58.857704
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:01.271281
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:03.954724
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:06.367402
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:08.783774
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:11.197969
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:13.615969
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:16.026217
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:18.442988
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:41:23.474355
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:41:41.492792
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:41:59.612973
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:20.808089
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:38.727300
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:42.816482
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:45.588791
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:51.530324
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:42:54.258237
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:42:56.938381
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:42:59.353518
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:01.772598
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:04.187869
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:06.603592
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:09.017642
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:11.433976
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:13.853148
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:16.269060
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:18.685225
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:21.294557
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:23.713481
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:26.134773
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:28.549699
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:30.963596
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:33.378274
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:35.794774
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:38.214109
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:40.630619
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:43.042671
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:45.456766
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:47.875132
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:50.290582
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:52.703556
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:55.116959
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:57.530902
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:43:59.948105
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:02.361262
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:04.868506
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:07.279173
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:09.694685
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:12.111667
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:14.529142
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:16.942848
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:19.357655
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:21.773223
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:24.187932
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:26.608013
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:29.021220
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:31.436240
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:33.852424
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:36.270493
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:38.688333
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:41.101446
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:43.522695
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:45.937901
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:48.352551
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:50.771917
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:53.185284
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:55.604017
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:44:58.645678
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:01.062652
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:03.479260
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:05.897058
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:08.308419
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:10.723407
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:13.141289
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:15.557452
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:17.969314
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:20.384697
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:22.798717
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:25.217251
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:27.633239
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:28.980929
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:30.314651
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:45:49.278891
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:46:05.372508
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:46:07.972776
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:10.386828
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:12.804274
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:15.219510
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:17.632462
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:20.046747
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:22.460673
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:24.879012
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:27.294974
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:32.711121
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:34.173440
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:35.949687
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:54.728005
# Unit test for function get_sysctl
def test_get_sysctl():
    from unittest.mock import Mock, call

    # Normal parsing: '=' and ': ' separators, prefixes passed through
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\nnet.core.somaxconn: 1024\nvm.swappiness = 10\n', '')
    result = module_0.get_sysctl(module, ['-a'])
    assert result == {'net.ipv4.ip_forward': '1', 'net.core.somaxconn': '1024', 'vm.swappiness': '10'}
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', '-a'])

    # Multiline values, blank lines, stripped values
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'key1 = first\n continuation line\n\nkey2: value2  \nkey3 =  spaced  \n', '')
    result = module_0.get_sysctl(module, ['net', 'vm'])
    assert result == {'key1': 'first\n continuation line', 'key2': 'value2', 'key3': 'spaced'}
    module.run_command.assert_called_once_with(['/usr/sbin/sysctl', 'net', 'vm'])

    # Empty output on success
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, '\n\n', '')
    assert module_0.get_sysctl(module, []) == {}

    # Non-zero return code returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (1, 'net.ipv4.ip_forward = 1\n', 'error')
    assert module_0.get_sysctl(module, ['-a']) == {}

    # OSError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = OSError('missing sysctl')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to read sysctl' in str(module.warn.call_args)

    # IOError from run_command warns and returns empty dict
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.side_effect = IOError('io error')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called

    # Malformed line without separator warns and yields no entry
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    module.run_command.return_value = (0, 'no-separator-line\n', '')
    assert module_0.get_sysctl(module, ['-a']) == {}
    assert module.warn.called
    assert 'Unable to split sysctl line' in str(module.warn.call_args)

# Generated at 2026-10-25 09:46:57.168709
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:46:59.583312
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:02.185064
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:04.603818
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:07.015580
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:09.661364
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:12.076461
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:14.492714
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:16.904069
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:19.317475
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:21.731175
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:24.143937
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:26.556383
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:28.969735
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:31.383666
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:33.796697
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:36.209351
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:38.620493
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:41.074182
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:43.481454
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:45.895766
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:48.308370
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:50.721448
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:47:53.142451
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:02.038758
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:04.451951
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:06.866516
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:09.280342
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:11.695604
# Unit test for function get_sysctl

# Generated at 2026-10-25 09:48:14.110583
# Unit test for function get_sysctl