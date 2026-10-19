

# Generated at 2022-06-14 09:52:00.730205
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert not match(Command('manage.py --merge migrate'))
    assert not match(Command('manage.py migrate --merge'))
    assert match(Command('python manage.py migrate'))
    assert not match(Command('manage.py -h'))



# Generated at 2022-06-14 09:52:09.773361
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate',
                         '',
                         'Traceback (most recent call last):\n'
                         ' File "manage.py", line 8, in <module>\n'
                         '   execute_from_command_line(sys.argv)\n'
                         'migration = Migration(infos[0], app)\n'
                         'KeyError: 0\n'))
    assert not match(Command('ls', '', ''))
    assert not match(Command('python manage.py', '', ''))
    assert not match(Command('python manage.py migrate', '', ''))



# Generated at 2022-06-14 09:52:20.788675
# Unit test for function match
def test_match():
    # Fake command
    command = type('obj', (object,), {
        'script': 'python manage.py migrate', 'output': ' --merge: will just attempt the migration'
    })
    assert match(command) is True

    # Fake command
    command = type('obj', (object,), {
        'script': 'python manage.py migrate', 'output': '--merge: will just attempt the migration'
    })
    assert match(command) is False

    # Fake command
    command = type('obj', (object,), {
        'script': 'python manage.py migrate', 'output': ' --merge: will just attempt the migration'
    })
    assert match(command) is True

# Generated at 2022-06-14 09:52:25.864537
# Unit test for function match
def test_match():
    assert match(Command('/path/to/manage.py migrate')) == True
    assert match(Command('/path/to/manage.py migrate --merge')) == False
    assert match(Command('/path/to/manage.py check')) == False
    assert match(Command('/path/to/manage.py --version')) == False


# Generated at 2022-06-14 09:52:28.901286
# Unit test for function match
def test_match():
    command = Command('manage.py migrate --merge: will just attempt the migration')
    assert match(command)

# Generated at 2022-06-14 09:52:40.709104
# Unit test for function match
def test_match():
    assert not match(Command('', ''))
    assert match(Command('foo/manage.py', 'python manage.py migrate'))
    assert match(Command('foo/manage.py', 'python manage.py migrate --merge'))
    assert not match(Command('foo/manage.py', 'python manage.py kill'))
    assert not match(Command('foo/manage.py', 'python manage.py migrate --merge:'))
    assert match(Command('foo/manage.py', 'python manage.py migrate', 'foo --merge: will just attempt the migration'))
    assert match(Command('foo/manage.py', 'python manage.py migrate', 'bar --merge: will just attempt the migration'))

# Generated at 2022-06-14 09:52:43.839659
# Unit test for function match
def test_match():
    assert match(
        command.Script(CODE_SAMPLES.MATCHING_DJANGO_MIGRATE_COMMAND, 'stdout'))


# Generated at 2022-06-14 09:52:44.857358
# Unit test for function match
def test_match():
    assert match(script) == True


# Generated at 2022-06-14 09:52:53.289814
# Unit test for function match
def test_match():
    assert match(Command(script='manage', output='')) is False
    assert match(Command(script='manage.py', output='')) is False
    assert match(Command(script='manage.py migrate', output='')) is False
    assert match(Command(script='manage.py migrate')) is False
    assert match(Command(script='manage.py migrate', output='--merge: will just attempt the migration and print output if a merge is required')) is True

# Generated at 2022-06-14 09:53:06.048469
# Unit test for function match
def test_match():
    command = Command("manage.py migrate", "", "")
    assert match(command) == False

    command = Command("manage.py migrate", "", " --merge: will just attempt the migration")
    assert match(command) == True

    command = Command("manage.py migrate", "", "--merge")
    assert match(command) == True

    command = Command("manage.py migrate --merge", "", "")
    assert match(command) == False

    command = Command("manage.py", "", "")
    assert match(command) == False

    command = Command("manage.py", "", "--merge: will just attempt the migration")
    assert match(command) == False

    command = Command("manage.py", "", "--merge")
    assert match(command) == False



# Generated at 2022-06-14 09:53:13.767775
# Unit test for function match
def test_match():
    command = Command('python manage.py migrate --merge', '', [], None)
    assert match(command) == True

    command = Command('python manage.py migrate --merge: will just attempt the migration without applying it', '', [], None)
    assert match(command) == True



# Generated at 2022-06-14 09:53:19.774286
# Unit test for function match
def test_match():
    assert True == match(Command(
        script='manage.py migrate',
        output=' --merge: will just attempt the migration'))

    assert False == match(Command(
        script='manage.py migrate',
        output=' --fakemerge: will just attempt the migration'))

    assert False == match(Command(
        script='manage.py migrate',
        output=' --merge'))



# Generated at 2022-06-14 09:53:30.493302
# Unit test for function match
def test_match():
    # Test no match
    command = Command('python manage.py migrate appname 02022020')
    assert not (match(command))
    # Test match where --merge flag is not present
    command = Command('python manage.py migrate appname --fakeflag --fakeflag2 --fakeflag3')
    command.output = '--merge: will just attempt the migration'
    assert match(command)
    # Test match where --merge flag is present in args
    command = Command('python manage.py migrate appname --merge --fakeflag --fakeflag2 --fakeflag3')
    command.output = '--merge: will just attempt the migration'
    assert match(command)
    # Test match where --merge flag is present in args, but not the last arg

# Generated at 2022-06-14 09:53:39.103430
# Unit test for function match
def test_match():
    list = [
        ['manage.py migrate --settings=settings.dev', '--merge: will just attempt the migration'],
        ['manage.py migrate --settings=settings.dev', '--fake: will just attempt the migration'],
        ['manage.py migrate --settings=settings.dev', '--merge: will just attempt the migration'],
        ['manage.py migrate --settings=settings.dev', '--merge: will just attempt the migration']
    ]
    for item in list:
        command = FakeCommand(item[0], item[1])
        assert match(command) is True


# Generated at 2022-06-14 09:53:46.179597
# Unit test for function match
def test_match():
    assert True == match(Command('manage.py migrate --merge: will just attempt the migration\n'))
    assert True == match(Command('manage.py migrate --merge\n'))
    assert False == match(Command('manage.py migrate\n'))
    assert False == match(Command('manage.py makemigrations\n'))
    assert False == match(Command('manage.py makemigrations test\n'))

# Generated at 2022-06-14 09:53:52.015801
# Unit test for function match
def test_match():
    assert match("manage.py migrate --merge: will just attempt the migration") is True
    assert match("manage.py migrate") is False
    assert match("some thing else") is False
    assert match("manage.py migrate --merge") is False


# Generated at 2022-06-14 09:53:54.690359
# Unit test for function match
def test_match():
    assert match({'script': 'python manage.py migrate',
                  'output': '--merge: will just attempt the migration'})

# Generated at 2022-06-14 09:54:08.019962
# Unit test for function match
def test_match():
    command = Command(script='/usr/bin/python manage.py migrate --force-execut', output="Applying account.0001_initial... FAILED (this is a merge migration) ! Since you have unapplied migrations, your project may not work properly until they are applied.")
    assert(match(command))
    command = Command(script='/usr/bin/python manage.py migrate --force-execut', output="Applying account.0001_initial... OK")
    assert(not match(command))
    command = Command(script='/usr/bin/python manage.py migrate', output="Applying account.0001_initial... FAILED (this is a merge migration) ! Since you have unapplied migrations, your project may not work properly until they are applied.")
    assert(match(command))

# Generated at 2022-06-14 09:54:19.920311
# Unit test for function match
def test_match():
    assert (match(Command(script='python manage.py migrate',
                          stderr='',
                          stdout='DatabaseError: Real database is not available yet, '
                                 '--merge: will just attempt the migration')))
    assert (match(Command(script='python manage.py migrate -e development',
                          stderr='',
                          stdout='DatabaseError: Real database is not available yet, '
                                 '--merge: will just attempt the migration')))
    assert not match(Command(script='python manage.py migrate',
                             stderr='',
                             stdout='--merge: will just attempt the migration'))



# Generated at 2022-06-14 09:54:22.645788
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate', 
                            "",
                            "migrate --merge: will just attempt the migration"))



# Generated at 2022-06-14 09:54:38.709208
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration',
                         'will just attempt the migration, but will not create new migration files'))
    assert match(Command('python manage.py migrate --merge'))
    assert match(Command('python manage.py migrate --merge '))
    assert match(Command('python manage.py migrate --merge: '))
    assert match(Command('python manage.py migrate --merge :'))

    assert not match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py migrate --merges: will just attempt the migration'))
    assert not match(Command('python manage.py migrate --merge= will just attempt the migration'))

# Generated at 2022-06-14 09:54:45.216725
# Unit test for function match
def test_match():
    command = Command('/venv/bin/python manage.py migrate --merge: will just attempt the migration')
    assert match(command)

    command = Command('/venv/bin/python manage.py migrate --fake')
    assert not match(command)


# Generated at 2022-06-14 09:54:57.290005
# Unit test for function match
def test_match():
    assert match(Command(script='manage.py migrate',
                         output='Operations to perform:\n  Apply all migrations: admin, contenttypes, sessions, social_django, auth\nRunning migrations:\n  No migrations to apply.\n\n--merge:',
                         path='/home/vagrant/workspace'))
    assert match(Command(script='manage.py migrate',
                         output='Operations to perform:\n  Apply all migrations: admin, contenttypes, sessions, social_django, auth\nRunning migrations:\n  No migrations to apply.\n\n--merge: will just attempt the migration',
                         path='/home/vagrant/workspace'))

# Generated at 2022-06-14 09:55:04.065671
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', 0.1, False))
    assert not match(Command('python manage.py migrate', '', 0.1, False))
    assert not match(Command('git commit -m ', '', 0.1, False))
    assert not match(Command('ls -l', '', 0.1, False))



# Generated at 2022-06-14 09:55:09.005443
# Unit test for function match

# Generated at 2022-06-14 09:55:16.804047
# Unit test for function match
def test_match():
    assert(match(Command('python manage.py migrate --merge: will just attempt the migration')))
    assert(match(Command('python manage.py migrate --merge: will just attempt the migration --here')))
    assert(match(Command('python manage.py migrate --merge')))
    assert(match(Command('python manage.py migrate')))
    assert(not match(Command('python manage.py migrate2')))
    assert(not match(Command('python manage.py m')))
    assert(not match(Command('python manage.py --merge')))
    assert(not match(Command('python manage.py')))
    assert(not match(Command('python migrate --merge')))
    assert(not match(Command('python manage.py --merge: will just attempt the migration')))



# Generated at 2022-06-14 09:55:21.476290
# Unit test for function match
def test_match():
    assert True == match(Command('python manage.py migrate', '', True))
    assert False == match(Command('python manage.py makemigrations', '', True))
    assert False == match(Command('python manage.py runserver', '', True))



# Generated at 2022-06-14 09:55:28.602570
# Unit test for function match

# Generated at 2022-06-14 09:55:31.912782
# Unit test for function match
def test_match():
    assert not match(Command('manage.py'))
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge'))

# Generated at 2022-06-14 09:55:36.394157
# Unit test for function match
def test_match():
    assert match(Command('foo')) is False
    assert match(Command('manage.py')) is False
    assert match(
        Command('manage.py migrate --merge: will just attempt the migration')) is True



# Generated at 2022-06-14 09:55:47.848915
# Unit test for function match
def test_match():
    c = Command('/usr/bin/python manage.py migrate', '', '\n' \
        'DoesNotExist: The database backend does not accept 0 as a value for AutoField.\n' \
        '--merge: will just attempt the migration, but not create a new one if the migration fails.\n',
        None)
    assert match(c)

    c = Command('/usr/bin/python manage.py migrate --merge', '', '', None)
    assert not match(c)

    c = Command('/usr/bin/python manage.py shell', '', '', None)
    assert not match(c)



# Generated at 2022-06-14 09:55:53.170042
# Unit test for function match
def test_match():
    assert match(sublime.Region(0, 0)) == False

    command = FakeCommand('python manage.py migrate --merge --database=default')
    assert match(command) == False

    command = FakeCommand('python manage.py migrate --merge')
    assert match(command) == True



# Generated at 2022-06-14 09:55:55.363717
# Unit test for function match
def test_match():
    command = (u"python manage.py migrate --merge")
    assert (True == match(command))


# Generated at 2022-06-14 09:56:01.297699
# Unit test for function match
def test_match():
    assert match(Mock(script='manage.py migrate something', output="--merge: will just attempt the migration"))
    assert match(Mock(script='manage.py migrate something --merge', output="--merge: will just attempt the migration"))
    assert not match(Mock(script='manage.py migrate something', output="--merge: won't just attempt the migration"))
    assert not match(Mock(script='manage.py migrate --merge something', output="--merge: will just attempt the migration"))



# Generated at 2022-06-14 09:56:07.125662
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge'))
    assert match(Command('/home/user/venv/bin/python2 manage.py migrate --merge --noinput'))
    assert match(Command('python3.4 /home/user/myproject/manage.py migrate --merge'))

    assert not match(Command('manage.py migrate'))
    assert not match(Command('/home/user/venv/bin/python2 manage.py migrate --noinput'))
    assert not match(Command('python3.4 /home/user/myproject/manage.py migrate'))


# Generated at 2022-06-14 09:56:12.780970
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge'))
    assert match(Command('manage.py migrate --merge -v 3'))
    assert not match(Command('manage.py migrate'))
    assert not match(Command('manage.py migrate -v 3'))
    assert not match(Command('manage.py --merge'))


# Generated at 2022-06-14 09:56:23.510179
# Unit test for function match
def test_match():
    command = Command('python manage.py migrate')
    assert not match(command)

    command = Command('python manage.py migrate --app api')
    assert not match(command)

    command = Command('python manage.py migrate --merge')
    assert not match(command)

    command = Command('python manage.py migrate --merge')
    command.error = Exception()
    assert not match(command)

    command = Command('python manage.py migrate --merge')
    command.stderr = 'blah'
    assert not match(command)

    command = Command('python manage.py migrate --merge')
    command.output = 'blah blah blah\n'
    assert not match(command)

    command = Command(
        'python manage.py migrate --merge')

# Generated at 2022-06-14 09:56:28.299201
# Unit test for function match
def test_match():
    assert True == match(Command('python manage.py migrate', '', '', 0, None))
    assert False == match(Command('python manage.py shell --version', '', '', 0, None))
    assert False == match(Command('python manage.py addsomething', '', '', 0, None))

# Generated at 2022-06-14 09:56:31.618152
# Unit test for function match
def test_match():
    assert False is match(Command('ls', '', ''))
    assert True is match(Command('python manage.py runserver',
                                '',
                                ' --merge: will just attempt the migration'))


# Generated at 2022-06-14 09:56:35.561140
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate',
                         'This option is intended to replace the now-deprecated --merge: will just attempt the migration and then not check if the migration worked\n',
                         '', 0))
    assert match(Command('python manage.py migrate',
                         '--merge: will just attempt the migration and then not check if the migration worked\n',
                         '', 0))
    assert not match(Command('python manage.py migrate',
                             '--break: will just attempt the migration and then not check if the migration worked\n',
                             '', 0))
    assert not match(Command('python manage.py migrate',
                             '',
                             '', 0))



# Generated at 2022-06-14 09:56:49.240627
# Unit test for function match
def test_match():
    assert True == match(Command('python manage.py migrate --merge'))
    assert False == match(Command('python manage.py migrate 2'))



# Generated at 2022-06-14 09:56:55.877408
# Unit test for function match
def test_match():
    command = Command(script='manage.py myapp migrate')
    assert match(command)

    command = Command(script='manage.py myapp migrate',
                      output='--merge: will just attempt the migration')
    assert match(command)

    command = Command(script='manage.py myapp migrate',
                      output='--merge')
    assert not match(command)



# Generated at 2022-06-14 09:57:00.703953
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert not match(Command('/home/zol/manage.py migrate'))
    assert not match(Command('manage.py migrate --list'))
    assert not match(Command('manage.py showmigrate'))



# Generated at 2022-06-14 09:57:05.979677
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge')) is False
    assert match(Command('/usr/bin/manage.py migrate'))
    assert match(Command('python3 manage.py migrate'))



# Generated at 2022-06-14 09:57:14.708847
# Unit test for function match
def test_match():
    assert match(Command(script='manage.py migrate --help'))
    assert match(Command(script='manage.py migrate --dry-run'))
    assert match(Command(script='manage.py migrate --merge'))
    assert match(Command(script='manage.py migrate --fake'))
    assert not match(Command(script='manage.py migrate'))
    assert not match(Command(script='manage.py makemigrations'))
    assert not match(Command(script='manage.py sqlmigrate'))

# Generated at 2022-06-14 09:57:21.187853
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge', '', ''))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration', '', ''))
    assert not match(Command('python manage.py migrate', '', ''))
    assert not match(Command('python manage.py migrate --merge', '', '--merge: will just attempt the migration'))

# Generated at 2022-06-14 09:57:32.095172
# Unit test for function match
def test_match():
    assert match(Command(script='manage.py migrate --help',
                         output='--merge: will just attempt the migration'))
    assert match(Command(script='manage.py migrate',
                         output='--merge: will just attempt the migration'))
    assert not match(Command(script='python manage.py migrate',
                             output='--merge: will just attempt the migration'))
    assert not match(Command(script='manage.py migrate',
                             output='--whatever: will just attempt the migration'))
    assert not match(Command(script='manage.py migrate',
                             output='--whatever: will just attempt the migration'))



# Generated at 2022-06-14 09:57:39.694773
# Unit test for function match
def test_match():
    assert match(Command(
        script='python manage.py migrate',
        output='== 20170324123844 MergeAuthUserAuditlog: migrating ==\n-- merge: will just attempt the migration'))
    assert not match(Command(
        script='python manage.py migrate',
        output='== 20170324123844 MergeAuthUserAuditlog: migrating ==\n-- merge: will just attempt the migration',
        stderr='[...]'))
    assert not match(Command(
        script='python manage.py migrate',
        output='',
        stderr='[...]'))



# Generated at 2022-06-14 09:57:46.587060
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge'))
    assert not match(Command('python manage.py makemigrations'))
    assert not match(Command('python manage.py showmigrations'))
    assert not match(Command('python manage.py migrate --plan'))

# Generated at 2022-06-14 09:57:52.874945
# Unit test for function match
def test_match():
    assert True == match(Command('/usr/bin/python manage.py migrate --merge: will just attempt the migration'))
    assert False == match(Command('python manage.py migrate'))
    assert False == match(Command('python manage.py makemigrations'))
    assert False == match(Command('python manage.py migrate --fake'))

# Generated at 2022-06-14 09:58:25.559363
# Unit test for function match
def test_match():
    assert match(Command('/bin/foo', stdout='manage.py'))
    assert match(Command('/bin/foo', stdout='manage.py migrate'))
    assert match(Command('/bin/foo',
                         stdout='manage.py --merge: will just attempt the migration'))
    assert not match(Command('/bin/foo', stdout='django-admin'))
    assert not match(Command('/bin/foo', stdout='django-admin migrate'))
    assert not match(Command('/bin/foo',
                             stdout='django-admin --merge: will just attempt the migration'))
    assert match(Command('/bin/foo', stderr='manage.py'))
    assert match(Command('/bin/foo', stderr='manage.py migrate'))


# Generated at 2022-06-14 09:58:33.314505
# Unit test for function match
def test_match():
    # Simple positive test
    script = 'python manage.py migrate --merge'
    output = '--merge: will just attempt the migration'

    command = Command(script, output)
    assert match(command)

    # Should not match
    script = 'python manage.py migrate'
    output = '--merge: will just attempt the migration'

    command = Command(script, output)
    assert not match(command)



# Generated at 2022-06-14 09:58:37.078753
# Unit test for function match
def test_match():
    command = Command('manage.py migrate')
    assert match(command)
    command = Command('manage.py migrate --settings=migrations.settings')
    assert match(command)


# Generated at 2022-06-14 09:58:44.640433
# Unit test for function match
def test_match():
    assert match(Command(script=u'/Users/natesh/dev/yummy-recipes/manage.py migrate --merge: will just attempt the migration',
                         output='',
                         errors='',
                         cwd='',
                         env={}))
    assert match(Command(script=u'/Users/natesh/dev/yummy-recipes/manage.py migrate --merge: will just attempt the migration',
                         output='',
                         errors='',
                         cwd='',
                         env={}))
    assert match(Command(script=u'/Users/natesh/dev/yummy-recipes/manage.py migrate --merge: will just attempt the migration',
                         output='',
                         errors='',
                         cwd='',
                         env={}))

# Generated at 2022-06-14 09:58:49.853792
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge: will just attempt the migration\n'))
    assert match(Command('manage.py migrate\n'))
    assert not match(Command('ls\n'))
    assert not match(Command('manage.py migrate --fake\n'))


# Generated at 2022-06-14 09:59:02.947554
# Unit test for function match
def test_match():
    assert match(Command('/venv/bin/python manage.py migrate --fake'))
    assert match(Command('python manage.py migrate --fake'))
    assert match(Command('/venv/bin/python manage.py migrate'))
    assert match(Command('python manage.py migrate'))

    assert not match(Command('/venv/bin/python manage.py migrate --help'))
    assert not match(Command('python manage.py migrate --help'))
    assert not match(Command('/venv/bin/python manage.py migrate --merge'))
    assert not match(Command('python manage.py migrate --merge'))



# Generated at 2022-06-14 09:59:06.206578
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge: will just attempt the migration',
                         'User warning: You have a mix of Django Bootstrap3 and Bootstrap 2...\n'))
    assert not match(Command('something else'))

# Generated at 2022-06-14 09:59:16.367787
# Unit test for function match
def test_match():

    assert match(Command(script='manage.py migrate'))
    assert match(Command(script='manage.py migrate --merge'))
    assert match(Command(script='manage.py migrate --merge',
                         stderr='Error: --merge: will just attempt the migration'))
    assert not match(Command(script='manage.py migrate --merge',
                             stderr='Error: --merge: will just attempt the migration',
                             output='Applying contenttypes.0001_initial... OK'))
    assert not match(Command(script='manage.py migrate --merge'))



# Generated at 2022-06-14 09:59:22.610453
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --fake -v'))
    assert match(Command('python manage.py migrate --fake -v --merge'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('python manage.py list'))



# Generated at 2022-06-14 09:59:29.363605
# Unit test for function match
def test_match():
    assert match(
        Command('manage.py migrate --merge: will just attempt the migration', '', ''))
    assert match(
        Command('manage.py migrate --merge', '', ''))
    assert not match(
        Command('manage.py migrate --fake', '', ''))
    assert not match(
        Command('manage.py migrate', '', ''))
    assert not match(
        Command('python manage.py migrate', '', ''))



# Generated at 2022-06-14 10:00:18.412777
# Unit test for function match
def test_match():
    assert not match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))

# Generated at 2022-06-14 10:00:24.744337
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --help'))
    assert match(Command('python manage.py migrate --merge: will just attemp the migration'))
    assert not match(Command('python manage.py'))
    assert not match(Command('python manage.py other_action'))



# Generated at 2022-06-14 10:00:36.129474
# Unit test for function match
def test_match():
    """
    Test that match function is performing correctly
    """

# Generated at 2022-06-14 10:00:40.821205
# Unit test for function match
def test_match():
    command = Command('manage.py migrate')
    assert not match(command)
    command = Command('manage.py migrate --merge')
    assert not match(command)
    command = Command('manage.py migrate')
    command.error = Exception('--merge: will just attempt the migration')
    assert match(command)



# Generated at 2022-06-14 10:00:47.410148
# Unit test for function match

# Generated at 2022-06-14 10:00:55.941162
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', ''))
    assert match(Command('python manage.py migrate', '', '--merge'))
    assert not match(Command('manage.py migrate', '', ''))
    assert not match(Command('python manage.py syncdb', '', ''))
    assert not match(Command('python manage.py migrate --fake', '', ''))
    assert not match(Command('python manage.py migrate --fake --merge', '', ''))
    assert not match(Command('python manage.py test_migrate', '', ''))



# Generated at 2022-06-14 10:01:01.545068
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', '', '', '', ''))
    assert match(Command('python manage.py migrate --run-syncdb', '', '', '', '', ''))
    assert not match(Command('python manage.py migrate_schemas --run-syncdb', '', '', '', '', ''))

# Generated at 2022-06-14 10:01:05.341032
# Unit test for function match
def test_match():
    assert match('manage.py migrate')
    assert match('manage.py migrate --merge')
    assert not match('python manage.py migrate')
    assert not match('manage.py r')

# Generated at 2022-06-14 10:01:15.013756
# Unit test for function match
def test_match():
    assert match(Command('ls | grep manage.py'))
    assert match(Command('ls | grep manage.py ; ls'))
    assert match(Command('ls | grep manage.py && ls'))
    assert match(Command('ls | grep manage.py && ls; ls'))
    assert match(Command('manage.py migrate --merge'))
    assert match(Command('python manage.py migrate --merge'))
    assert match(Command('python3 manage.py migrate --merge'))
    assert match(Command('python3.5 manage.py migrate --merge'))
    assert match(Command('python3.5 manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))

# Generated at 2022-06-14 10:01:21.783201
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py migrate --fake'))
    # assert not match(Command())
    # assert not match(Command(''))
    # assert not match(None)

