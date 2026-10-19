

# Generated at 2024-05-31 08:47:16.100087
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:47:20.463487
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:47:27.032726
# Unit test for function check_command
def test_check_command():
    module = MockModule()
    check_command(module, 'chown user file')
    assert module.warnings == ["Consider using the file module with owner rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]

    module = MockModule()
    check_command(module, 'curl http://example.com')
    assert module.warnings == ["Consider using the get_url or uri module rather than running 'curl'.  If you need to use 'curl' because the get_url or uri module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]

    module = MockModule()
    check_command(module, 'sudo ls')
   

# Generated at 2024-05-31 08:47:31.435464
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:47:35.848615
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:47:40.972542
# Unit test for function check_command
def test_check_command():    module = AnsibleModule(argument_spec={})

# Generated at 2024-05-31 08:47:45.898978
# Unit test for function check_command
def test_check_command():    module = type('obj', (object,), {'warn': lambda x: warnings.append(x)})

# Generated at 2024-05-31 08:47:52.210904
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:47:58.124381
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:02.715182
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:16.739069
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:20.238096
# Unit test for function check_command
def test_check_command():    module = AnsibleModule(argument_spec={})

# Generated at 2024-05-31 08:48:24.764371
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:28.520954
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:32.839881
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:36.323145
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:39.980404
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:44.016415
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:47.520106
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:48:51.270910
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:13.875271
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')
    assert len(warnings) == 0

    warnings = []
    check_command(module, ['chown', 'user', 'file'])

# Generated at 2024-05-31 08:49:18.506011
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:24.081697
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, ['chmod', '755', 'file'])
    assert "Consider using the file module with mode rather than running 'chmod'" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')

# Generated at 2024-05-31 08:49:28.389537
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:35.887785
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:40.869997
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:44.479156
# Unit test for function check_command
def test_check_command():    module = AnsibleModule(argument_spec={})

# Generated at 2024-05-31 08:49:51.273769
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:55.237798
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:49:59.723185
# Unit test for function check_command
def test_check_command():    module = type('obj', (object,), {'warn': lambda x: warnings.append(x)})

# Generated at 2024-05-31 08:50:44.087705
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:50:51.694113
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, ['chmod', '755', 'file'])
    assert "Consider using the file module with mode rather than running 'chmod'" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')

# Generated at 2024-05-31 08:50:56.745445
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:51:00.315964
# Unit test for function check_command
def test_check_command():    module = AnsibleModule(argument_spec={})

# Generated at 2024-05-31 08:51:04.506317
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:51:09.100658
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:51:14.164794
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, ['chmod', '755', 'file'])
    assert "Consider using the file module with mode rather than running 'chmod'" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')

# Generated at 2024-05-31 08:51:22.376317
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:51:25.856817
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'." in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'." in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')
    assert len(warnings) == 0

# Generated at 2024-05-31 08:51:32.743918
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:53:15.451740
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, 'unknown_command')
    assert len(warnings) == 0

# Generated at 2024-05-31 08:53:19.966715
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:53:26.546270
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:53:32.688668
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:53:37.002423
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule

# Generated at 2024-05-31 08:53:43.679438
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    check_command(module, 'chown user file')
    assert "Consider using the file module with owner rather than running 'chown'" in warnings[0]

    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    warnings = []
    check_command(module, ['chmod', '755', 'file'])
    assert "Consider using the file module with mode rather than running 'chmod'" in warnings[0]

    warnings = []
    check_command(module, 'unknowncommand')

# Generated at 2024-05-31 08:53:47.748830
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    # Test case 1: command in arguments
    check_command(module, 'chown')
    assert "Consider using the file module with owner rather than running 'chown'." in warnings[0]

    # Test case 2: command in commands
    warnings = []
    check_command(module, 'curl')
    assert "Consider using the get_url or uri module rather than running 'curl'." in warnings[0]

    # Test case 3: command in become
    warnings = []
    check_command(module, 'sudo')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    # Test case 4: command not in any list
    warnings = []
    check_command(module, 'echo')

# Generated at 2024-05-31 08:53:53.398014
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    warnings = []

    # Test case 1: command in arguments
    check_command(module, 'chmod 755 /path/to/file')
    assert "Consider using the file module with mode rather than running 'chmod'" in warnings[0]

    # Test case 2: command in commands
    warnings = []
    check_command(module, 'curl http://example.com')
    assert "Consider using the get_url or uri module rather than running 'curl'" in warnings[0]

    # Test case 3: command in become
    warnings = []
    check_command(module, 'sudo ls')
    assert "Consider using 'become', 'become_method', and 'become_user' rather than running sudo" in warnings[0]

    # Test case 4: command not in any list
    warnings = []

# Generated at 2024-05-31 08:53:58.010539
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda x: warnings.append(x)
    
    warnings = []
    check_command(module, 'chown user file')
    assert warnings == ["Consider using the file module with owner rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]
    
    warnings = []
    check_command(module, 'curl http://example.com')
    assert warnings == ["Consider using the get_url or uri module rather than running 'curl'.  If you need to use 'curl' because the get_url or uri module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]
    
    warnings

# Generated at 2024-05-31 08:54:03.055170
# Unit test for function main
def test_main():    from ansible.module_utils.basic import AnsibleModule