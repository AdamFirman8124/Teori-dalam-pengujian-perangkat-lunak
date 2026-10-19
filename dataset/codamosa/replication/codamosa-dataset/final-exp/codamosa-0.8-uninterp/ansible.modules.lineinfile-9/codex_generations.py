

# Generated at 2022-06-13 05:34:46.394129
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:34:49.349538
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    changed = False
    diff = [(" "),(" ")]
    msg, changed = check_file_attrs(module, changed, '', diff)
    assert changed



# Generated at 2022-06-13 05:34:50.136345
# Unit test for function present
def test_present():
    assert True



# Generated at 2022-06-13 05:34:54.924308
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module, changed, message, diff = (1, 2, 3, 4)
    assert check_file_attrs(module, changed, message, diff) == (1, 2, 3, 4)
    check_file_attrs(module, changed, message, diff) == changed, message and diff



# Generated at 2022-06-13 05:34:57.817206
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({})
    assert (write_changes(module, ['\n'], '/tmp/test') == None)


# Generated at 2022-06-13 05:35:05.364839
# Unit test for function absent
def test_absent():
    with open('/tmp/test_lineinfile_absent.txt', 'w') as f:
        f.write('abcdef\n')
    f.close()

    with open('/tmp/test_lineinfile_absent.txt', 'w') as f:
        f.write('abcdef\n')
        f.write('ghijkl\n')
        f.write('mnopqr\n')
        f.write('stuvwx\n')
        f.write('y0z1234\n')
        f.write('56789a\n')
    f.close()


# Generated at 2022-06-13 05:35:15.034227
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(default="/this/is/only/a/test"),
            regexp=dict(default=None),
            insertafter=dict(default=None),
            insertbefore=dict(default=None),
            backup=dict(default=False, type='bool'),
        ),
        supports_check_mode=True
    )
    dest = os.path.join(TEST_DIR, "test_absent.txt")
    # create file
    with open(dest, 'w') as f:
        f.write("This is a test.")

    regexp = '^This is a test.$'
    absent(module, dest, regexp, None, None, True)
    # ensure file is gone
    assert not os.path.exists(dest)
#

# Generated at 2022-06-13 05:35:18.988726
# Unit test for function present
def test_present():
    module = AnsibleModule({
        'dest': '/tmp/ansible_test_file',
        'state': 'present',
        'line': 'test line\n',
        'regexp': '^test regexp$'
    })
    result = present(module, '/tmp/ansible_test_file', '^test regexp$', None, 'test line\n', 'BOF', None, True, False, False, False)
    assert result is not None


# Generated at 2022-06-13 05:35:20.920690
# Unit test for function write_changes
def test_write_changes():
    write_changes(tmpdir, dest)



# Generated at 2022-06-13 05:35:21.612663
# Unit test for function write_changes
def test_write_changes():
    assert False


# Generated at 2022-06-13 05:35:55.334179
# Unit test for function absent
def test_absent():
    line = '#test'
    dest = '/tmp/test_absent'
    backup = False
    regexp = None
    search_string = None
    changed = False
    msg = ''
    found = 0
    b_dest = to_bytes(dest, errors='surrogate_or_strict')
    with open(b_dest, 'rb') as f:
        b_lines = f.readlines()
    b_line = to_bytes(line, errors='surrogate_or_strict')
    for b_cur_line in b_lines:
        match_found = b_line == b_cur_line.rstrip(b'\r\n')
        if match_found:
            found = found + 1
            break
    if found:
        msg = "%s line(s) removed" % found

# Generated at 2022-06-13 05:36:07.243258
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native, to_bytes
    from ansible.module_utils.common.collections import Mapping
    import os

    DIFF = ''.encode('utf-8')

    module_args = dict(
        path='/tmp/testfile',
        owner='root',
        group='root',
        mode='0600',
        seuser=None,
        serole=None,
        setype=None,
        searole=None,
        selevel=None
    )

    m = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    m.tmpdir = tempfile.mkdtemp(dir='/tmp')

# Generated at 2022-06-13 05:36:13.338175
# Unit test for function present
def test_present():
    def _present_mock_exec(module, dest, regexp, search_string, line, insertafter, insertbefore, create, backup, backrefs, firstmatch):
        print ("dest=%s, regexp=%s, search_string=%s, line=%s, insertafter=%s, insertbefore=%s, create=%s, backup=%s, backrefs=%s, firstmatch=%s" % (dest, regexp, search_string, line, insertafter, insertbefore, create, backup, backrefs, firstmatch))
        return


# Generated at 2022-06-13 05:36:13.782675
# Unit test for function write_changes
def test_write_changes():
    assert False


# Generated at 2022-06-13 05:36:14.483462
# Unit test for function main
def test_main():
    # not testing
    pass

# Generated at 2022-06-13 05:36:26.193150
# Unit test for function present
def test_present():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 05:36:33.976039
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={
        'dest': {'type': 'str', 'required': True},
        })

    b_content = to_bytes('this is a test\n', errors='surrogate_or_strict')
    write_changes(module, b_content, module.params['dest'])
    assert os.path.isfile(module.params['dest'])
    assert open(module.params['dest'], 'r').read() == 'this is a test\n'
    os.unlink(module.params['dest'])



# Generated at 2022-06-13 05:36:41.909346
# Unit test for function main
def test_main():
    import sys
    import os
    import tempfile
    fd, temp_file = tempfile.mkstemp()
    os.close(fd)
    fd, temp_file2 = tempfile.mkstemp()
    os.close(fd)
    args = {
        'path': 'overwrite_existing',
        'state': 'present',
        'regexp': 'regexp',
        'search_string': 'search_string',
        'line': 'line',
        'insertbefore': 'insertbefore',
        'insertafter': 'insertafter',
        'backrefs': 'backrefs',
        'create': 'create',
        'backup': 'backup',
        'firstmatch': 'firstmatch',
        'validate': 'validate',
    }

# Generated at 2022-06-13 05:36:46.895176
# Unit test for function absent
def test_absent():
    # Test for presence of line in a file
    result = absent(dest='test_file', line='test_string', backup=False)
    assert result == "test_string removed from the file"
    # Test for non-presence of line in a file
    result = absent(dest='test_file', line='test_string', backup=False)
    assert result == "test_string not present in the file"


# Generated at 2022-06-13 05:36:55.498352
# Unit test for function main
def test_main():
    import __main__ as main
    import tempfile
    global __file__
    from ansible.module_utils.common.file import mend_file
    global __dict__
    __dict__['file'] = mend_file
    __file__ = 'file'
    __dict__['_'] = mend_file
    __file__ = '_'
    src_data = '''#!/usr/bin/python
import sys

#file = sys.argv[1]

#fp = file(file)
#print fp.read()
print "hello"
'''
    src_fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    src_fp.write(src_data)
    src_fp.seek(0)
    src_fp.close()

# Generated at 2022-06-13 05:37:50.926392
# Unit test for function absent
def test_absent():
    import tempfile, shutil

    content = """A
    B
    C
    D
    E
    F
    G
    H
    I
    J
    K
"""

    (fd, dest) = tempfile.mkstemp()
    f = os.fdopen(fd, "w")
    f.write(content)
    f.close()

    m = AnsibleModule(
        argument_spec = dict(
            dest = dict(required=True),
            regexp = dict(),
            search_string = dict(),
            line = dict(required=True),
        )
    )
    m.absent(dest, regexp='B', line="B")
    with open(dest, "r") as f:
        assert f.read() == content
    os.unlink(dest)

    m.abs

# Generated at 2022-06-13 05:38:03.303720
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path'),
            owner=dict(),
            group=dict(),
            mode=dict(),
            seuser=dict(),
            serole=dict(),
            setype=dict(),
        ),
    )

    m_check_c = test_module._check_mode
    m_diff_c = test_module._diff
    test_module._check_mode = False
    test_module._diff = False

    f_args = test_module.load_file_common_arguments(test_module.params)

    # test that if no attributes are changed, the function does not return anything
    test_module.set_fs_attributes_if_different(f_args, False)
    (m, c) = check_file_attrs

# Generated at 2022-06-13 05:38:13.081537
# Unit test for function main

# Generated at 2022-06-13 05:38:19.953533
# Unit test for function present
def test_present():
    module = AnsibleModule({'src': './test/files/test.txt', 'dest': './test/files/test_copy.txt', 'regexp': '^#',
                            'line': '# Managed by Ansible'}, False)
    present(module, './test/files/test_copy.txt', '^#', None, '# Managed by Ansible', 'EOF', 'BOF', True, False, False, False)



# Generated at 2022-06-13 05:38:21.272966
# Unit test for function absent
def test_absent():
    assert absent(dest, regexp, search_string, line, backup) == True


# Generated at 2022-06-13 05:38:28.346688
# Unit test for function write_changes
def test_write_changes():
    temp_path = tempfile.mkdtemp(dir=module.tmpdir)
    dest = os.path.join(temp_path, 'destination')
    tmp = os.path.join(temp_path, 'temp')
    with open(dest, "wb") as bf:
        bf.write("~/path\n")
    with open(tmp, "wb") as bf:
        bf.write("~/path_tmp\n")
    module.atomic_move(tmp, dest)

    validate = "/bin/ls %s"
    b_validate = to_bytes(validate, errors='surrogate_or_strict')
    b_validate_with_args = to_bytes(b_validate % dest, errors='surrogate_or_strict')

# Generated at 2022-06-13 05:38:39.700093
# Unit test for function present
def test_present():
    dest = None
    regexp = None
    search_string = None
    line = None
    insertafter = None
    insertbefore = None
    create = None
    backup = None
    backrefs = None
    firstmatch = None

    function_params = dict(
        dest=dest, regexp=regexp, search_string=search_string, line=line, insertafter=insertafter, insertbefore=insertbefore,
        create=create, backup=backup, backrefs=backrefs, firstmatch=firstmatch
    )
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 05:38:40.503219
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 05:38:54.522995
# Unit test for function write_changes
def test_write_changes():
    # mock params
    module_params = dict(
        backup=False,
        dest='/etc/my.cnf',
        validate='/usr/sbin/mycnf-check %s',
        unsafe_writes=False,
        path='/etc/my.cnf',
        regex='^user'
    )
    # mock module
    tmpfd, tmpfile = tempfile.mkstemp(dir='/tmp')
    tmpfd2, tmpfile2 = tempfile.mkstemp(dir='/tmp')
    b_lines = [
        "line 1 user=root\n",
        "line 2 user=nobody\n"
    ]
    mock_module = AnsibleModule(
        argument_spec=module_params,
        supports_check_mode=False
    )
    # open tmpfile and write

# Generated at 2022-06-13 05:39:06.283281
# Unit test for function present

# Generated at 2022-06-13 05:42:19.570747
# Unit test for function present
def test_present():
    test_str = "some test string"
    test_regex = "some (\w+) string"
    test_line = "some replacement string"
    match_data = re.match(test_regex, test_str)
    test_regex2 = "some (\w+) (\w+) string"
    match_data2 = re.match(test_regex2, test_str)
    assert match_data is not None
    assert match_data.lastindex == 1
    assert match_data.group(1) == "test"
    test_line_match = re.match(test_regex, test_line)
    assert test_line_match is not None
    assert test_line_match.lastindex == 1
    assert test_line_match.group(1) == "replacement"

# Generated at 2022-06-13 05:42:28.835995
# Unit test for function present
def test_present():
    #Testing function with a regexp and the regexp match is in the file
    b_dest = to_bytes('./README.md', errors='surrogate_or_strict')
    b_lines = []
    b_destpath = os.path.dirname(b_dest)
    if b_destpath and not os.path.exists(b_destpath):
        os.makedirs(b_destpath)
    with open(b_dest, 'rb') as f:
        b_lines = f.readlines()
    b_linesep = to_bytes(os.linesep, errors='surrogate_or_strict')
    b_new_line = '''
        # This is a comment
        line 2
    '''
    index = [-1, -1]
    exact_line_match

# Generated at 2022-06-13 05:42:29.798290
# Unit test for function write_changes
def test_write_changes():
    pass

    #TODO: need to find a way to test 'dest' is changed correctly


# Generated at 2022-06-13 05:42:39.978705
# Unit test for function absent
def test_absent():
    # Create a temporary file.
    fd, fname = tempfile.mkstemp()
    f = open(fname, 'w')
    f.write('test\n')
    f.close()

    # Store file object as module.params['dest']
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path', required=True),
            regexp=dict(required=False),
            search_string=dict(required=False),
            line=dict(required=False),
            backup=dict(required=False, type='bool', default=False),
        ),
        supports_check_mode=True,
        check_invalid_arguments=False,
        add_file_common_args=True,
    )

# Generated at 2022-06-13 05:42:51.334840
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'file': '/tmp/testfile',
                            'pattern': '\n# line to be inserted\n',
                            'insertafter': '^# line to insert after',
                            'test': 'testfile'},
                           check_invalid_arguments=False)
    setattr(module, 'run_command', lambda *args, **kwargs: (0, None, None))

    fd, local_file = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        f.write('# line to insert after\n')
    dest = os.path.realpath(local_file)

    b_lines = to_bytes('# line to insert after\n', errors='surrogate_or_strict')

# Generated at 2022-06-13 05:42:58.793486
# Unit test for function main

# Generated at 2022-06-13 05:43:04.069867
# Unit test for function main
def test_main():
    err_msg = ''

# Generated at 2022-06-13 05:43:09.648139
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs({}, False, '', {None: {'insize': 1, 'after': 'line', 'before': 'new_line'}}) == ('ownership, perms or SE linux context changed', True)
    assert check_file_attrs({}, True, '', {None: {'insize': 1, 'after': 'line', 'before': 'new_line'}}) == ('ownership, perms or SE linux context changed', True)
    assert check_file_attrs({}, True, '', {}) == ('', False)
    assert check_file_attrs({}, True, 'message', {}) == ('message', False)
    assert check_file_attrs({}, True, 'message', {None: {}}) == ('ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 05:43:20.215950
# Unit test for function absent
def test_absent():

    filename = 'test_absent'
    with open(filename, 'w') as f:
        f.write("# Test file\n")
        f.write("Hello there\n")
        f.write("I am a test file\n")
        f.write(" asdf \n")
        f.write("foo\n")

    m = AnsibleModule(
        argument_spec=dict(
            path=dict(required=False, default=filename, aliases=['dest']),
            state=dict(default='absent', choices=['absent']),
            regexp=dict(required=False),
            line=dict(required=False),
            search_string=dict(required=False),
        ),
        supports_check_mode=True
    )


# Generated at 2022-06-13 05:43:31.509371
# Unit test for function absent
def test_absent():
    values = dict(dest="/tmp/nauman", regexp=None, search_string="4", line="4", backup=False)
    values['search_string'] = None