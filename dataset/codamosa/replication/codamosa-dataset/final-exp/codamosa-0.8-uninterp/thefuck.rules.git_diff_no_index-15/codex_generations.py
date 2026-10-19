

# Generated at 2022-06-14 10:03:30.415739
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '', '/bin/git-diff'))
    assert match(Command('git diff -- file1 file2', '', '/bin/git-diff'))
    assert not match(Command('git diff file1', '', '/bin/git-diff'))
    assert not match(Command('git diff --no-index file1 file2', '', '/bin/git-diff'))
    assert not match(Command('git diff -- file1 file2 file3', '', '/bin/git-diff'))
    assert not match(Command('git diff -- file1', '', '/bin/git-diff'))
    assert not match(Command('git diff -w -- file1 file2', '', '/bin/git-diff'))

# Generated at 2022-06-14 10:03:36.461126
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff'))
    assert not match(Command('git diff -b'))
    assert match(Command('git diff file1 file2 file3 file4'))


# Generated at 2022-06-14 10:03:46.704699
# Unit test for function match
def test_match():
    assert (match(Command('git diff README', '', True, '', ''))
            is True)
    assert (match(Command('git diff --no-index README', '', True, '', ''))
            is False)
    assert (match(Command('git diff README CONTRIBUTING.md', '', True, '', ''))
            is True)
    assert (match(Command('git diff --no-index README CONTRIBUTING.md', '',
                         True, '', ''))
            is False)
    assert (match(Command('git diff master', '', True, '', ''))
            is False)



# Generated at 2022-06-14 10:03:50.115318
# Unit test for function get_new_command
def test_get_new_command():
    command = 'git diff foo bar'
    assert get_new_command(command) == 'git diff --no-index foo bar'

# Generated at 2022-06-14 10:03:56.542083
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git diff a/ b/') == 'git diff --no-index a/ b/'
    assert get_new_command('git diff a/ b/ c/') == 'git diff --no-index a/ b/ c/'
    #assert get_new_command('git diff') == 'git diff --no-index'

# xunit test for function get_new_command

# Generated at 2022-06-14 10:04:04.829335
# Unit test for function match
def test_match():
    assert match(Command('git diff', '', stderr='fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command('git commit', ''))
    assert not match(Command('git diff', ''))
    assert match(Command('git diff filename1', ''))
    assert match(Command('git diff --cached filename1', ''))
    assert match(Command('git diff filename1 filename2', ''))
    assert match(Command('git difffilename1 filename2', ''))
    assert not match(Command('git diff --no-index /tmp/filename1 /tmp/filename2', ''))
    assert not match(Command('git diff filename1 --no-index /tmp/filename2', ''))

# Generated at 2022-06-14 10:04:09.652101
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '',
                         stderr='fatal: Not a git repository (or any of the parent directories): .git'))
    assert not match(Command(
        'git diff file1 file2', '', stderr='fatal: Not a git repository'))
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1 file2 --diff-filter=AM'))
    assert not match(Command('git diff --no-index file1 file2'))


# Generated at 2022-06-14 10:04:21.650437
# Unit test for function match
def test_match():
    # Test 1
    # A situation in which match should return True
    command = 'git diff file1 file2'
    assert match(command)

    # Test 2
    # A situation in which match should return True
    command = 'git diff --cached SERVER-8431 file'
    assert match(command)

    # Test 3
    # A situation in which match should return False
    command = 'git diff'
    assert not match(command)

    # Test 4
    # A situation in which match should return False
    command = 'git diff --cached SERVER-8431'
    assert not match(command)

    # Test 5
    # A situation in which match should return False
    command = 'git'
    assert not match(command)



# Generated at 2022-06-14 10:04:25.353518
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff file1 file2 file3'))
    assert not match(Command('git diff --no-index file1 file2'))



# Generated at 2022-06-14 10:04:30.554913
# Unit test for function match
def test_match():
    assert (
        match(Command('git diff file1 file2', '')) is True
    )
    assert (
        match(Command('git diff --no-index file1 file2', '')) is False
    )
    assert (
        match(Command('git diff -w file1 file2', '')) is True
    )
    assert (
        match(Command('git diff', '')) is False
    )


# Generated at 2022-06-14 10:04:43.425812
# Unit test for function match
def test_match():
    assert match(Command('git commit', '', stderr='error: pathspec \'abc\' did not match any file(s) known to git.'))
    assert match(Command('git diff', '', stderr='error: pathspec \'abc\' did not match any file(s) known to git.'))
    assert match(Command('git diff a b', '', stderr='error: pathspec \'abc\' did not match any file(s) known to git.'))
    assert not match(Command('git stash', '', stderr='error: pathspec \'abc\' did not match any file(s) known to git.'))
    assert not match(Command('git diff a b', '', stderr='I dunno'))

# Generated at 2022-06-14 10:04:49.628580
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff --no-index  file1 file2'))
    assert not match(Command('git diff file1'))
    assert not match(Command('git diff'))
    assert not match(Command('git '))


# Generated at 2022-06-14 10:04:54.043490
# Unit test for function match
def test_match():
    assert not match(Command('git', 'diff', 'file1', 'file2'))
    assert not match(Command('git', 'diff', '--no-index', 'file1', 'file2'))
    assert match(Command('git', 'diff', '--cached', 'file1', 'file2'))

# Generated at 2022-06-14 10:05:06.655118
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2',
                         'git diff file1 file2'))
    assert match(Command('git diff file1 file2 --some-other-arg',
                         'git diff file1 file2 --some-other-arg'))
    assert match(Command('git diff -w file1 file2',
                         'git diff -w file1 file2'))
    assert not match(Command('git diff --no-index file1 file2',
                             'git diff --no-index file1 file2'))
    assert not match(Command('git diff --no-index',
                             'git diff --no-index'))
    assert not match(Command('git diff --no-index -w file1 file2',
                             'git diff --no-index -w file1 file2'))

# Generated at 2022-06-14 10:05:09.140793
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff file1 file2')
    new_command = get_new_command(command)
    expected = 'git diff --no-index file1 file2'
    assert new_command.script == expected

# Generated at 2022-06-14 10:05:15.588736
# Unit test for function get_new_command
def test_get_new_command():

    command = Command('diff file1 file2')
    assert get_new_command(command) == 'git diff --no-index file1 file2'

    command = Command('git diff file1 file2')
    assert get_new_command(command) == 'git diff --no-index file1 file2'

# Generated at 2022-06-14 10:05:18.999397
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git diff main.py main2.py') == 'git diff --no-index main.py main2.py'


# Generated at 2022-06-14 10:05:27.652625
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1 file2', '', ''))
    assert match(Command('git diff -w file1 file2'))
    assert match(Command('git difftool file1 file2'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff file1 file2 file3'))
    assert not match(Command('git difftool file1 file2 file3'))
    assert not match(Command('git diff -w file1 file2 file3'))


# Generated at 2022-06-14 10:05:30.222300
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff file'))
    assert not match(Command('git diff --no-index file1 file2'))


# Generated at 2022-06-14 10:05:32.548956
# Unit test for function match
def test_match():
    assert match(Command('git diff foo bar'))
    assert not match(Command('git checkout -b newbranch'))
    assert not match(Command('git diff --no-index foo bar'))


# Generated at 2022-06-14 10:05:39.681787
# Unit test for function match
def test_match():
    assert match(Command('git diff 1 2'))
    assert match(Command('git diff --no-index 1 2')) is False
    assert match(Command('git status')) is False



# Generated at 2022-06-14 10:05:45.634441
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '', '', '', ''))
    assert not match(Command('git diff --no-index file1 file2', '', '', '', ''))
    assert not match(Command('git diff file1', '', '', '', ''))


# Generated at 2022-06-14 10:05:56.304840
# Unit test for function match
def test_match():
    assert match(Command('git diff --cached file1 file2',
                         '', ''))
    assert match(Command('git diff file1 file2',
                         '', ''))
    assert match(Command('git diff --cached file1 file2',
                         '', ''))
    assert match(Command('git diff --cached file1 file2',
                         '', ''))
    assert match(Command('git diff --cached file1 file2',
                         '', ''))
    assert match(Command('git diff --cached [file1] [file2]',
                         '', ''))
    assert match(Command('git diff --cached file1 file2 --ignore-blank-lines',
                         '', ''))
    assert not match(Command('diff --no-index file1 file2',
                             '', ''))

# Generated at 2022-06-14 10:06:02.796541
# Unit test for function match
def test_match():
    assert match(Command('git diff a b'))
    assert match(Command('git diff --no-index a b')) is False
    assert match(Command('git difftool --dir-diff a b')) is False
    assert match(Command('git difftool a b')) is False
    assert match(Command('git difftool --dir-diff HEAD')) is False
    assert match(Command('git difftool HEAD')) is False

# Generated at 2022-06-14 10:06:14.290122
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '', ''))
    assert match(Command('git diff --git a/file1 b/file2', '', ''))
    assert not match(Command('git -c diff.mnemonicprefix=false diff file1 file2', '', '')) # noqa
    assert not match(Command('git diff --no-index file1 file2', '', ''))
    assert not match(Command('git diff --no-index file1 file2 file3', '', ''))
    assert not match(Command('git diff --no-index', '', ''))


# Generated at 2022-06-14 10:06:21.335220
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('diff file1 file2') == 'git diff --no-index file1 file2'
    assert get_new_command('diff file1 file2 --ignore-all-space') == 'git diff --no-index file1 file2 --ignore-all-space'
    assert get_new_command('diff file1 file2 --ignore-all-space -w') == 'git diff --no-index file1 file2 --ignore-all-space -w'

# Generated at 2022-06-14 10:06:24.725374
# Unit test for function match
def test_match():
    assert match(Command('git diff ..'))
    assert match(Command('git diff ../...'))
    assert not match(Command('git config'))
    assert not match(Command('git diff --no-index ../..'))


# Generated at 2022-06-14 10:06:29.079243
# Unit test for function match
def test_match():
    assert not match(Command('git dif', '', ''))
    assert not match(Command('git diff', '', ''))
    assert not match(Command('git diff --', '', ''))
    assert not match(Command('git diff -', '', ''))
    assert match(Command('git diff file', '', ''))
    assert match(Command('git diff -- file', '', ''))
    assert match(Command('git diff file1 file2', '', ''))


# Generated at 2022-06-14 10:06:35.162747
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('diff file.txt fool.txt') == 'diff --no-index file.txt fool.txt'
    assert get_new_command('git diff file.txt fool.txt') == 'git diff --no-index file.txt fool.txt'
    assert get_new_command('svn diff file.txt fool.txt') == 'svn diff file.txt fool.txt'

# Generated at 2022-06-14 10:06:38.730012
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git diff a b') == 'git diff --no-index a b'
    assert get_new_command('git diff --cached a b') == 'git diff --no-index --cached a b'


# Generated at 2022-06-14 10:06:54.488239
# Unit test for function match
def test_match():
    assert match(Command('git diff file_1 file_2', stderr='usage: git diff [--no-index] <path> <path>'))
    assert not match(Command('git diff --no-index file_1 file_2', stderr='usage: git diff [--no-index] <path> <path>'))
    assert not match(Command('git diff file_1', stderr='usage: git diff [--no-index] <path> <path>'))
    assert not match(Command('git diff file_1 file_2 file_3', stderr='usage: git diff [--no-index] <path> <path>'))


# Generated at 2022-06-14 10:06:57.904275
# Unit test for function match
def test_match():
    assert match(Command('git diff', ''))
    assert not match(Command('git diff --cached', ''))
    assert match(Command('git diff file1 file2', ''))
    assert not match(Command('git diff --no-index file1 file2', ''))


# Generated at 2022-06-14 10:07:01.257424
# Unit test for function match
def test_match():
    assert match(Command('git diff 1.txt 2.txt', ''))
    assert match(Command('git diff', '')) is False
    assert match(Command('git diff --no-index 1.txt 2.txt', '')) is False
    assert match(Command('git diff 1.txt', '')) is False

# Generated at 2022-06-14 10:07:08.295585
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff -- something -file1 file2'))
    assert match(Command('git diff file1 file2 -something'))
    assert not match(Command('git diff --no-index -- something -file1 file2'))


# Generated at 2022-06-14 10:07:10.584745
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.types import Command
    correct_command = Command('git diff foo bar', '')
    assert get_new_command(correct_command) == 'git diff --no-index foo bar'

# Generated at 2022-06-14 10:07:11.673685
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git diff version') == 'git diff --no-index version'

# Generated at 2022-06-14 10:07:14.642771
# Unit test for function match
def test_match():
    command = Command("git diff foo.c bar.c", "", "/bin/bash")
    assert match(command)


# Generated at 2022-06-14 10:07:25.691702
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1  file2'))
    assert match(Command('git diff file1   file2'))
    assert not match(Command('git diff'))
    assert not match(Command('git'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('ls'))
    assert not match(Command('ls file1 file2'))
    assert not match(Command('ls file1   file2'))
    assert not match(Command('git diff file1 file2 file3'))
    assert not match(Command('git diff --no-index file1 file2 file3'))


# Generated at 2022-06-14 10:07:28.254275
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff a b', None)
    assert get_new_command(command) == 'git diff --no-index a b'

# Generated at 2022-06-14 10:07:39.516308
# Unit test for function match
def test_match():
    command = Command('git diff aaa bbb')
    assert match(command) is True

    command = Command('git diff --cached aaa bbb')
    assert match(command) is True

    command = Command('diff aaa bbb')
    assert match(command) is False

    command = Command('git diff')
    assert match(command) is False

    command = Command('git diff --cached')
    assert match(command) is False

    command = Command('git diff aaa bbb --no-index')
    assert match(command) is False

    command = Command('git diff aaa bbb ccc')
    assert match(command) is False


# Generated at 2022-06-14 10:07:48.457436
# Unit test for function get_new_command
def test_get_new_command():
    assert('git diff --no-index file1 file2' == get_new_command('git diff file1 file2'))

# Generated at 2022-06-14 10:07:50.555141
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git diff file1 file2', '')) == 'git diff --no-index file1 file2'

# Generated at 2022-06-14 10:07:57.960415
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', None))
    assert match(Command('git diff --cached file1 file2', None))
    assert not match(Command('git diff file1 file2 file3', None))
    assert not match(Command('git show file1 file2', None))
    assert not match(Command('git diff --no-index file1 file2', None))


# Generated at 2022-06-14 10:08:03.889464
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', ''))
    assert not match(Command('git diff --no-index file1 file2', ''))
    assert not match(Command('git diff file1 file2 file3', ''))

# Generated at 2022-06-14 10:08:14.498894
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff file1 file2', 'file1 file2 are not in a git repository')
    assert get_new_command(command) == 'git diff --no-index file1 file2'
    command = Command('git diff file1 file2 -w', 'fatal: invalid diff option/value: -w')
    assert get_new_command(command) == 'git diff --no-index file1 file2 -w'
    # Test the last one: command.stderr = ''
    command = Command('git diff file1 file2', '')
    assert get_new_command(command) == 'git diff --no-index file1 file2'

# Generated at 2022-06-14 10:08:17.364216
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', ''))
    assert not match(Command('git diff', ''))
    assert not match(Command('git diff file1', ''))
    assert not match(Command('git diff file1 file2 --no-index'))


# Generated at 2022-06-14 10:08:24.156280
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff --cached file1 file2'))
    assert match(Command('git diff --cached file1 file2 --color'))
    assert not match(Command('git diff -u file1 file2'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff file1'))


# Generated at 2022-06-14 10:08:25.218958
# Unit test for function match
def test_match():
    assert match(Command('git diff a b'))
    assert match(Command('git difftool a b'))
    assert not match(Command('gitt diff a b'))

# Generated at 2022-06-14 10:08:26.772392
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))


# Generated at 2022-06-14 10:08:29.354849
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff foo bar', '', '')
    assert get_new_command(command) == 'git diff --no-index foo bar'

# Generated at 2022-06-14 10:08:41.686900
# Unit test for function match
def test_match():

    snippet = 'git diff file1 file2'

    assert match(Command(snippet, ''))

    snippet = 'git diff file1 file2 --cached'

    assert match(Command(snippet, ''))

    snippet = 'git diff file1 file2'

    assert not match(Command(snippet, ''))


# Generated at 2022-06-14 10:08:49.398694
# Unit test for function match
def test_match():
    assert match(Command('diff file1 file2', ''))
    assert match(Command('git diff file1 file2', ''))
    assert not match(Command('diff --no-index file1 file2', ''))
    assert not match(Command('diff file1', ''))
    assert not match(Command('diff file1 file2 file3', ''))
    assert not match(Command('git diff --no-index file1 file2', ''))
    assert not match(Command('git diff file1', ''))
    assert not match(Command('git diff file1 file2 file3', ''))


# Generated at 2022-06-14 10:08:53.360825
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git diff proj1/file1 proj2/file2', '', None)) == 'git diff --no-index proj1/file1 proj2/file2'

# Generated at 2022-06-14 10:08:55.433547
# Unit test for function match
def test_match():
    assert match('git diff file1.txt file2.txt')


# Generated at 2022-06-14 10:08:59.836352
# Unit test for function match
def test_match():
    assert match(Command('git diff a b', '', ''))
    assert not match(Command('git diff --no-index a b', '', ''))
    assert not match(Command('git add a', '', ''))


# Generated at 2022-06-14 10:09:05.221339
# Unit test for function match
def test_match():
    assert match(Command('git diff a b', '', ''))
    assert not match(Command('git diff a b --no-index', '', ''))
    assert not match(Command('git diff a', '', ''))
    assert not match(Command('git lol', '', ''))


# Generated at 2022-06-14 10:09:16.250418
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('git diff file1.txt file2.txt').script == "git diff --no-index file1.txt file2.txt"
    assert get_new_command('lalala diff file1.txt file2.txt').script == 'lalala diff file1.txt file2.txt'
    assert get_new_command('git diff file1.txt file2.txt --cached').script == "git diff --cached --no-index file1.txt file2.txt"
    assert get_new_command('git diff file1.txt file2.txt --cached -b').script == "git diff -b --cached --no-index file1.txt file2.txt"


# Generated at 2022-06-14 10:09:20.784807
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff --cached'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff file1'))


# Generated at 2022-06-14 10:09:25.554301
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('diff a.txt b.txt') == 'git diff --no-index a.txt b.txt'
    assert get_new_command('diff -b a.txt b.txt') == 'git diff --no-index -b a.txt b.txt'

# Generated at 2022-06-14 10:09:29.270396
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command('git diff file1 file2')
    assert new_command == 'git diff --no-index file1 file2'

# Generated at 2022-06-14 10:09:49.785001
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('git diff a b', '')).script == 'git diff --no-index a b'

# Generated at 2022-06-14 10:10:02.076067
# Unit test for function match
def test_match():
    # Test if it matches
    assert match(Command('git diff file1 file2', '', '/'))
    assert match(Command('git diff file1 file2', '', '/',
                         'git diff file1 file2\n'
                         'new file mode '
                         'diff --git a/file1 b/file2\n'
                         'index 0000000..71cb8d5 100644\n'
                         '--- /dev/null\n'
                         '+++ b/file2\n'
                         '@@ -0,0 +1 @@\n'
                         '+Africa\n'))
    # Test if it does not match
    assert not match(Command('git diff --no-index file1 file2', '', '/'))
    assert not match(Command('git diff file1', '', '/'))

# Generated at 2022-06-14 10:10:08.402273
# Unit test for function get_new_command
def test_get_new_command():
    results1 = [
        u'git diff first_file.txt second_file.txt'
    ]
    
    results2 = [
        u'git diff second_file.txt first_file.txt'
    ]

    for results in results1, results2:
        assert get_new_command(results) == [u'git diff --no-index first_file.txt second_file.txt']

# Generated at 2022-06-14 10:10:16.117114
# Unit test for function match
def test_match():
    assert not match(Command('git diff file1 file2'))
    assert match(Command('git diff --cached file1 file2'))
    assert match(Command('git diff --cached HEAD file1 file2'))
    assert not match(Command('git diff -a --cached HEAD file1 file2'))
    assert not match(Command('git --no-index diff -a --cached HEAD file1 file2'))


# Generated at 2022-06-14 10:10:22.262995
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '', '', 3, 3))
    assert match(Command('git diff file1 file2 file3', '', '', 3, 3))
    assert not match(Command('git diff --no-index file1 file2', '', '', 3, 3))
    assert not match(Command('git diff', '', '', 3, 3))
    assert not match(Command('git diff -v', '', '', 3, 3))


# Generated at 2022-06-14 10:10:27.441439
# Unit test for function match
def test_match():
    assert match(Command('git diff', ''))
    assert match(Command('git diff file-1 file-2', ''))
    assert match(Command('git diff file-1 -t', ''))
    assert not match(Command('git diff --no-index', ''))

# Generated at 2022-06-14 10:10:34.402242
# Unit test for function get_new_command
def test_get_new_command():
    command1 = 'git diff a b'
    assert(get_new_command(command1) == 'git diff --no-index a b')

    command2 = 'gdiff a b'
    assert(get_new_command(command2) == 'gdiff --no-index a b')

    command3 = 'git diff -u a b'
    assert(get_new_command(command3) == 'git diff -u --no-index a b')
# End of unit test

# Generated at 2022-06-14 10:10:45.622461
# Unit test for function match
def test_match():
    command = Command('git diff foo bar', '', stderr='', stdout='', script='git diff foo bar')
    assert match(command)
    command = Command('git diff foo bar --no-index', '', stderr='', stdout='', script='git diff foo bar --no-index')
    assert not match(command)
    command = Command('git diff --no-index foo bar', '', stderr='', stdout='', script='git diff --no-index foo bar')
    assert not match(command)


# Generated at 2022-06-14 10:10:49.418962
# Unit test for function match
def test_match():
    assert match(Command('git diff dir/one.txt dir/two.txt', None))
    assert not match(Command('git diff dir/one.txt', None))
    assert not match(Command('git log dir/one.txt', None))


# Generated at 2022-06-14 10:10:56.617423
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.git_diff_no_index import get_new_command
    assert get_new_command(Command('git diff a b', '')) == 'git diff --no-index a b'
    assert get_new_command(Command('git diff --no-index a b', '')) == 'git diff --no-index a b'
    assert get_new_command(Command('git diff a b c', '')) == 'git diff a b c'

# Generated at 2022-06-14 10:11:33.212315
# Unit test for function match
def test_match():
    assert match(Command('git diff'))
    assert match(Command('git diff file1 file2'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff --no-index'))
    assert not match(Command('git diff file'))
    assert not match(Command('git diff file1 file2 file3'))
    assert not match(Command('git diff'))


# Generated at 2022-06-14 10:11:42.026021
# Unit test for function match
def test_match():
    assert match(Command('diff foo bar', '', ''))
    assert match(Command('git diff foo bar', '', ''))
    assert not match(Command('diff --no-index foo bar', '', ''))
    assert not match(Command('git diff --no-index foo bar', '', ''))
    assert not match(Command('git diff foo', '', ''))


# Generated at 2022-06-14 10:11:46.970112
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1 file2 -u'))
    assert not match(Command('git diff'))
    assert not match(Command('git diff --cached file1 file2'))
    assert not match(Command('git diff --no-index file1 file2'))



# Generated at 2022-06-14 10:11:51.269452
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff src/file1.txt src/file2.txt')
    assert get_new_command(command) == 'git diff --no-index src/file1.txt src/file2.txt'


enabled_by_default = True

# Generated at 2022-06-14 10:11:56.646237
# Unit test for function match
def test_match():
    command = 'git diff file1 file2'
    assert(match(command))

    command = 'git diff --no-index file1 file2'
    assert(not match(command))

    command = 'git add file1 file2'
    assert(not match(command))



# Generated at 2022-06-14 10:12:07.283629
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2', '', '')) is True
    assert match(Command('git diff file1 file2 file3', '', '')) is False
    assert match(Command('git diff --no-index file1 file2', '', '')) is False
    assert match(Command('git diff', '', '')) is False
    assert match(Command('git diff --no-index file1 file2', '', '')) is False
    assert match(Command('git diff file1 file2 --no-index', '', '')) is False


# Generated at 2022-06-14 10:12:11.594260
# Unit test for function match
def test_match():
    assert match(Command('git diff filea fileb', 
            '', 
            ''))
    assert not match(Command('git diff',
            '',
            ''))
    assert not match(Command('git diff --no-index filea fileb',
            '',
            ''))


# Generated at 2022-06-14 10:12:18.871349
# Unit test for function get_new_command
def test_get_new_command():
    assert 'git diff --no-index file1 file2' == get_new_command('git diff file1 file2')
    assert 'git diff --no-index file1 file2' == get_new_command('git diff file1 file2 --cached')
    assert 'git diff --no-index file1 file2' == get_new_command('git diff --cached file1 file2')
    assert 'git diff --no-index file1 file2' == get_new_command('git diff --cached --no-color file1 file2')
    assert 'git diff --no-index --cached file1 file2' == get_new_command('git diff --cached --no-index file1 file2')

# Generated at 2022-06-14 10:12:26.574624
# Unit test for function match
def test_match():
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1 file2 -w'))
    assert match(Command('git diff file1 file2 --word-diff'))
    assert not match(Command('git diff --no-index'))
    assert not match(Command('git diff --no-index file1 file2'))


# Generated at 2022-06-14 10:12:34.197836
# Unit test for function match
def test_match():
    command = Command('git diff README.md COMMIT', '/bin/git')
    assert match(command)

    command = Command('git diff --no-index README.md COMMIT', '/bin/git')
    assert not match(command)

    command = Command('git diff README.md', '/bin/git')
    assert not match(command)


# Generated at 2022-06-14 10:13:08.722657
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('git diff file1 file2', '')
    assert get_new_command(command) == 'git diff --no-index file1 file2'
    command = Command('git diff -b file1 file2', '')
    assert get_new_command(command) == 'git diff -b --no-index file1 file2'

# Generated at 2022-06-14 10:13:16.599072
# Unit test for function match
def test_match():
    assert match(Command('git diff'))
    assert match(Command('git diff file1 file2'))
    assert match(Command('git diff file1 file2 -w -b'))
    assert not match(Command('git diff --no-index file1 file2'))
    assert not match(Command('git diff --no-index file1 file2 -w -b'))
    assert not match(Command('git diff file1'))


# Generated at 2022-06-14 10:13:23.536608
# Unit test for function match
def test_match():
    assert match(Command(script='git diff file1 file2'))
    assert match(Command(script='git diff -p file1 file2'))
    assert match(Command(script='git diff --color file1 file2'))
    assert match(Command(script='git diff --no-index file1 file2'))
    assert match(Command(script='git diff file1'))
    assert match(Command(script='git diff'))
    assert match(Command(script='git diff --color'))
    assert not match(Command(script='git difftool'))
