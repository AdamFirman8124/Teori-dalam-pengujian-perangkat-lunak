

# Generated at 2022-06-14 09:52:00.257857
# Unit test for function match
def test_match():
    assert match(Command(script='src/manage.py migrate'))
    assert match(Command(script='src/manage.py migrate --fake'))
    assert not match(Command(script='src/manage.py shell'))



# Generated at 2022-06-14 09:52:04.813985
# Unit test for function match
def test_match():
    assert match(Command('python app/manage.py migrate'))
    assert match(Command('python app/manage.py migrate --list'))
    assert not match(Command('python manage.py runserver'))
    assert not match(Command('python app/manage.py makemigrations'))

# Generated at 2022-06-14 09:52:11.226474
# Unit test for function match
def test_match():
    assert match(Command(script='python manage.py migrate --merge'))
    assert match(Command(script='python manage.py migrate --merge something', output='--merge: will just attempt the migration'))
    assert not match(Command(script='python manage.py migrate --merge', output="""Failed to load migration_file: message: No migrations to merge."""))
    assert not match(Command(script='python manage.py migrate --fake'))



# Generated at 2022-06-14 09:52:15.892140
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', '', 0, None))
    assert not match(Command('python manage.py shell', '', '', 0, None))
    assert not match(Command('python manage.py runserver', '', '', 0, None))

# Generated at 2022-06-14 09:52:19.667604
# Unit test for function match
def test_match():
    assert match(Command('/venv/bin/python manage.py migrate --merge --settings=config.settings.local'))
    assert not match(Command('./manage.py migrate --settings=config.settings.prod'))


# Generated at 2022-06-14 09:52:29.103823
# Unit test for function match
def test_match():
    assert match(Command('venv/bin/python manage.py migrate', '', 0))
    assert match(Command('venv/bin/python manage.py migrate', '', 1))
    assert match(Command('venv/bin/python manage.py migrate', '', 2))
    assert match(Command('venv/bin/python manage.py migrate', '', 3))
    assert match(Command('venv/bin/python manage.py migrate', '', 4))
    assert match(Command('venv/bin/python manage.py migrate', '', 5))
    assert match(Command('venv/bin/python manage.py migrate', '', 6))
    assert match(Command('venv/bin/python manage.py migrate', '', 7))
    assert match(Command('venv/bin/python manage.py migrate', '', 8))
   

# Generated at 2022-06-14 09:52:33.167273
# Unit test for function match
def test_match():
    assert match(Command('/usr/bin/python manage.py migrate --merge; #', '', 1, None))
    assert not match(Command('/usr/bin/python manage.py migrate --noinput; #', '', 1, None))

# Generated at 2022-06-14 09:52:35.813126
# Unit test for function match
def test_match():
    command = Command(script='manage.py migrate --merge: will just attempt the migration')
    assert(True == match(command))

# Generated at 2022-06-14 09:52:40.801179
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert match(Command('manage.py migrate --merge'))
    assert match(Command('/Users/user/project/manage.py migrate'))
    assert not match(Command('python manage.py migrate'))
    assert not match(Command('manage.py makemigrations'))
    assert not match(Command('manage.py migrate --fake-initial'))
    assert not match(Command('manage.py migrate --fake-initial --merge'))



# Generated at 2022-06-14 09:52:50.642887
# Unit test for function match
def test_match():
    assert match(Command()) == False

# Generated at 2022-06-14 09:52:59.258615
# Unit test for function match
def test_match():
    command = Command()
    command.script = 'manage.py migrate --database db1 --noinput'
    command.output = 'Running migrations:('
    assert match(command) is False

    command = Command()
    command.script = 'manage.py migrate --database db1 --noinput'
    command.output = '--merge: will just attempt the migration'
    assert match(command) is True


# Generated at 2022-06-14 09:53:09.278482
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge'))
    assert match(Command('python manage.py migrate --merge'))
    assert match(Command('python3 manage.py migrate --merge'))

    assert not match(Command('manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('manage.py migrate --merge '))
    assert not match(Command('manage.py migrate'))
    assert not match(Command('manage.py migrate --merge --fake'))
    assert not match(Command('manage.py migrate --fake'))
    assert not match(Command('python3 manage.py migrate --merge2'))



# Generated at 2022-06-14 09:53:21.293296
# Unit test for function match
def test_match():
    assert match({'script': 'python manage.py makemigrations', 'output': '--merge: will just attempt the migration'})
    assert match({'script': 'python manage.py makemigrations', 'output': '--merge: will just attempt the migration'})
    assert match({'script': 'python manage.py migrate', 'output': '--merge: will just attempt the migration'})
    assert not match({'script': 'python manage.py makemigrations', 'output': '--merge: will just attempt the migration'})
    assert not match({'script': 'python manage.py makemigrations', 'output': '--merge: will just attempt the migration'})
    assert not match({'script': 'python manage.py makemigrations', 'output': '--merge: will just attempt the migration'})



# Generated at 2022-06-14 09:53:31.780007
# Unit test for function match
def test_match():
    assert match(Command('python app/manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py runserver'))

# Generated at 2022-06-14 09:53:44.854759
# Unit test for function match
def test_match():
    assert match(Command('/bin/bash -c "manage.py migrate --merge: will just attempt the migration"'))
    assert match(Command('/bin/bash -c "manage.py migrate --merge: will just attempt the migration"'))
    assert match(Command('django-admin.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py migrate --no-merge'))
    assert not match(Command('python manage.py migrate --merge: an error'))
    assert not match(Command('python manage.py migrate --merge: just attempt the migration'))

# Generated at 2022-06-14 09:53:49.887503
# Unit test for function match
def test_match():
    command = Command('django-admin manage.py')
    command.output = '''Did you forget to run migrations?
The merge process is primarily intended to help with the transition from
Django 1.9 to 1.10, but can be used to handle parallel development of new
features.

When you have a model in two different branches that have diverged, you
can use merge to combine the schema changes for those models.

By using the --merge option, a migration that would normally raise an
error will instead create a migration that merges together the changes in
both branches.
--merge: will just attempt the migration
'''
    assert match(command)



# Generated at 2022-06-14 09:53:51.672292
# Unit test for function match
def test_match():
    assert True == match(Command('manage.py migrate', ''))


# Generated at 2022-06-14 09:54:06.355151
# Unit test for function match
def test_match():
    # Normal case
    script = "python manage.py migrate/--merge # this is a comment"
    command = Command(script, 'rror: Target database is not up to date.')
    assert match(command)

    script = "/my/path/python manage.py migrate/--merge # this is a comment"
    command = Command(script, 'rror: Target database is not up to date.')
    assert match(command)

    # Lower case
    script = "python manage.py migrate/--merge # this is a comment"
    command = Command(script, 'error: Target database is not up to date.')
    assert match(command)

    # Empty script 
    command = Command('', 'rror: Target database is not up to date.')
    assert not match(command)

    # Empty output 
    script

# Generated at 2022-06-14 09:54:20.191078
# Unit test for function match
def test_match():
    # Input
    command = create_command(script=u'manage.py migrate')

# Generated at 2022-06-14 09:54:27.905339
# Unit test for function match
def test_match():
    assert(match(Command(script='manage.py migrate --fake-initial', output='--fake-initial: will insert a record for each existing table')))
    assert(not match(Command(script='manage.py migrate --fake-initial', output='you should be running a fake initial migration')))
    assert(match(Command(script='manage.py migrate --fake', output='--fake: mark migrations as run without actually running them')))
    assert(not match(Command(script='git commit', output='commit message')))



# Generated at 2022-06-14 09:54:30.708016
# Unit test for function match
def test_match():
    assert True is match(command)

# Generated at 2022-06-14 09:54:33.603568
# Unit test for function match
def test_match():
    assert match('python manage.py migrate')
    assert match('python manage.py migrate --merge') is False
    assert match('python manage.py migrate --fake')



# Generated at 2022-06-14 09:54:41.262877
# Unit test for function match
def test_match():
    assert True == match(Command('python manage.py migrate', '\n  You have 5 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.\n  Run \'python manage.py migrate\' to apply them.\n  --merge: will just attempt the migration, and log an error if it fails, but will not roll back.', ''))



# Generated at 2022-06-14 09:54:48.410007
# Unit test for function match
def test_match():
    assert match(Command('python manage.py makemigrations', ''))
    assert match(Command('python manage.py migrate', '--merge: will just attempt the migration'))
    assert not match(Command('python manage.py migrate', ''))
    assert not match(Command('python manage.py makemigrations', '--merge: will just attempt the migration'))

# Generated at 2022-06-14 09:54:52.613719
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge', '', 0))
    assert not match(Command('python manage.py migrate --merge', '', 1))
    assert not match(Command('python manage.py migrate', '', 0))



# Generated at 2022-06-14 09:54:55.566569
# Unit test for function match
def test_match():
    # True
    command = Command('python manage.py migrate --merge')
    assert(match(command))

    # False
    command = Command('python manage.py migrate')
    assert(not match(command))

# Generated at 2022-06-14 09:55:04.928348
# Unit test for function match
def test_match():
    # Test 1 - positive match, real output:
    # /home/vagrant/env/django-portfolio/bin/manage.py migrate --merge: will just attempt the migration
    command = Mock(script='/home/vagrant/env/django-portfolio/bin/manage.py migrate', output='/home/vagrant/env/django-portfolio/bin/manage.py migrate --merge: will just attempt the migration')
    assert match(command)

    # Test 2 - negative match, real output:
    # /home/vagrant/env/django-portfolio/bin/manage.py makemigrations

# Generated at 2022-06-14 09:55:13.263437
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', '', 1))
    assert not match(Command('python manage.py', '', '', 1))
    assert not match(Command('python manage.py migrate',
                             '--merge: will just attempt the migration',
                             '', 1))
    assert not match(Command('python manage.py migrate',
                             '--fake: will fail',
                             '', 1))
    assert not match(Command('python manage.py migrate',
                             '--fake: will fail',
                             '', 1))



# Generated at 2022-06-14 09:55:23.279039
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert match(Command("./manage.py migrate"))
    assert match(Command("python manage.py migrate"))
    assert match(Command("python3 manage.py migrate"))
    assert match(Command("python2 manage.py migrate"))
    assert match(Command("python3.6 manage.py migrate"))

    assert not match(Command("manage.py migrate --merge"))
    assert not match(Command("manage.py migrate --fake"))
    assert not match(Command("manage.py fake_migrate"))



# Generated at 2022-06-14 09:55:25.628424
# Unit test for function match

# Generated at 2022-06-14 09:55:41.682495
# Unit test for function match
def test_match():
    assert match({
        'script': 'manage.py migrate --database=default --noinput --merge',
        'output': u'--merge: will just attempt the migration',
        'env': {
            'CUSTOM_SETTINGS': 'dev.py'
        }
    }) is True
    assert match({
        'script': 'manage.py migrate --database=default --noinput',
        'output': u'--merge: will just attempt the migration',
        'env': {
            'CUSTOM_SETTINGS': 'dev.py'
        }
    }) is False

# Generated at 2022-06-14 09:55:45.465698
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('manage.py migrate'))
    assert not match(Command('manage.py'))
    assert not match(Command('python manage.py migrate --merge: will just attempt the migration'))


# Generated at 2022-06-14 09:55:58.527772
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --fake',
                         '',
                         'You called migrate with --fake, which has been '
                         'deprecated. Please use --fake-initial instead.'
                         '\n\n--merge: will just attempt the migration'
                         '\n\n--fake-initial: Mark the migration as having '
                         'run successfully in the past. Use this if you have '
                         'data migrations for an app, and have deleted the '
                         'app\'s tables manually. No actual database operations '
                         'will be performed.'))

# Generated at 2022-06-14 09:56:06.299619
# Unit test for function match
def test_match():
    assert match(Command(script='manage.py migrate --fake', output='')) is False
    assert match(Command(script='python manage.py migrate --fake', output='')) is False
    assert match(Command(script='python manage.py migrate --fake', output=' --merge: will just attempt the migration')) is False
    assert match(Command(script='python manage.py migrate --fake', output='Try --merge: will just attempt the migration')) is True
    assert match(Command(script='python manage.py migrate', output='Try --merge: will just attempt the migration')) is True
    assert match(Command(script='python manage.py migrate --merge', output='')) is True
    assert match(Command(script='manage.py migrate --merge', output='')) is True

# Generated at 2022-06-14 09:56:16.967713
# Unit test for function match
def test_match():
    assert match(
        Command('python manage.py migrate',
                '',
                '',
                stderr='You are running migrations with the --merge option but do not have a default merge migration specified.\n'
                       'You must either create one manually or use ./manage.py makemergemigration to generate one automatically.',
                status=1))

# Generated at 2022-06-14 09:56:22.663457
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('manage.py migrate --optimize: will try to optimize some stuff'))
    assert not match(Command('manage.py migrate --something'))
    assert not match(Command('manage.py migrate'))



# Generated at 2022-06-14 09:56:34.006704
# Unit test for function match
def test_match():
    assert True == match(Command('manage.py migrate --merge'))
    assert True == match(Command('python manage.py migrate --merge'))
    assert True == match(Command('py manage.py migrate --merge'))
    assert True == match(Command('python manage.py migrate --fake --merge'))
    assert True == match(Command('manage.py migrate --fake --merge'))
    assert True == match(Command('py manage.py migrate --fake --merge'))
    assert False == match(Command('manage.py migrate'))
    assert False == match(Command('manage.py fake --merge'))
    assert False == match(Command('manage.py fake'))
    assert False == match(Command('py manage.py fake'))
    assert False == match(Command('py'))


# Generated at 2022-06-14 09:56:50.169196
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS))
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS))
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS)) is False
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS)) is False
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS)) is False
    assert match(Command('python manage.py migrate', '', '', 0,
                         Command.WARNINGS)) is False



# Generated at 2022-06-14 09:56:55.705589
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge'))
    assert not match(Command('python manage.py migrate --fake'))
    assert not match(Command('python manage.py migrate --merge --fake'))



# Generated at 2022-06-14 09:57:00.100966
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate', ''))
    assert not match(Command('manage.py', ''))
    assert not match(Command('manage.py migrate --merge', ''))
    assert not match(Command('python manage.py migrate', ''))



# Generated at 2022-06-14 09:57:12.905028
# Unit test for function match
def test_match():
    command = Command('python manage.py migrate')
    assert match(command)

    command = Command('python manage.py migrate')
    command.output = 'merge: will just attempt the migration'
    assert not match(command)

    command = Command('python manage.py migrate')
    command.output = 'some merge: will just attempt the migration'
    assert not match(command)



# Generated at 2022-06-14 09:57:22.629730
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge', '',
             'Applying auth.0001_initial... OK\n', 1))
    assert not match(Command('manage.py migrate', '', '', 0))
    assert not match(Command('manage.py migrate --merge', '', '', 0))
    assert not match(Command('manage.py migrate --merge', '', '', 1))
    assert not match(Command('manage.py migrate --merge', '',
                 'Applying auth.0001_initial... OK\nApplying sites.0001_initial... OK\n', 1))

# Generated at 2022-06-14 09:57:27.811007
# Unit test for function match
def test_match():
    assert match(Command('', '', '')) is False
    assert match(Command('manage.py', 'migrate', '')) is False
    assert match(Command('manage.py', 'migrate', '--merge: will just attempt the migration')) is True


# Generated at 2022-06-14 09:57:36.477559
# Unit test for function match
def test_match():
    command = get_command('''
    /home/user/.virtualenvs/dev/bin/python manage.py migrate --help
    Usage: manage.py migrate [options] [app_label] [migration_name]
    ''')
    assert match(command)


# Generated at 2022-06-14 09:57:43.038041
# Unit test for function match
def test_match():
    assert match(models.Command('', '', '', 'manage.py myproject migrate --merge: will just attempt the migration'))
    assert match(models.Command('', '', '', 'manage.py migrate --merge: will just attempt the migration'))
    assert match(models.Command('', '', '', 'manage.py migrate --merge'))



# Generated at 2022-06-14 09:57:46.935790
# Unit test for function match
def test_match():
    assert match(Command('$ python manage.py migrate'))
    assert match(Command('$ python manage.py migrate --merge'))
    assert match(Command('$ python manage.py migrate --merge')) is False



# Generated at 2022-06-14 09:57:55.958385
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --settings=project.production.settings -v 0', '', 1))
    assert match(Command('python manage.py migrate --settings=project.production.settings -v 0', '', 1))
    assert match(Command('python3 manage.py migrate --settings=project.production.settings -v 0', '', 1))
    assert not match(Command('manage.py migrate --settings=project.production.settings -v 0', '', 0))
    assert not match(Command('manage.py migrate --settings=project.production.settings', '', 1))
    assert not match(Command('manage.py migrate', '', 1))
    assert not match(Command('manage.py', '', 1))

# Generated at 2022-06-14 09:58:00.342077
# Unit test for function match
def test_match():
    command1 = Command('python manage.py migrate')
    assert not match(command1)

    command2 = Command('python manage.py migrate', output='--merge: will just attempt the migration')
    assert match(command2)



# Generated at 2022-06-14 09:58:04.405633
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --fake'))
    assert match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py runserver'))
    assert not match(Command('manage.py migrate'))

# Generated at 2022-06-14 09:58:06.836054
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge', '', 'Error: will attempt the migration', 1))

# Generated at 2022-06-14 09:58:13.644721
# Unit test for function match
def test_match():
    command = Command('manage.py migrate --help')

    assert match(command)

# Generated at 2022-06-14 09:58:17.103210
# Unit test for function match
def test_match():
    assert(match("manage.py migrate --merge --fake"))
    assert(not match("manage.py migrate"))
    assert(not match("manage.py migrate --fake"))
    assert(not match("manage.py migrate --noinput --fake"))



# Generated at 2022-06-14 09:58:21.975785
# Unit test for function match
def test_match():
    # Assert that the command matches
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge'))

    # Assert that the command doesn't match
    assert not match(Command('python manage.py help'))
    assert not match(Command('manage.py migrate'))

# Generated at 2022-06-14 09:58:24.398211
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert not match(Command('python manage.py showmigrations'))



# Generated at 2022-06-14 09:58:28.535539
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('manage.py migrate'))


# Generated at 2022-06-14 09:58:33.732864
# Unit test for function match
def test_match():
    assert match(command1)
    assert not match(command2)
    assert match(command3)
    assert not match(command4)
    assert match(command5)
    assert not match(command6)
    assert match(command7)
    assert not match(command8)


# Generated at 2022-06-14 09:58:39.499772
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate --help'))
    assert not match(Command('manage.py makemigrations'))
    assert not match(Command('manage.py migrate --merge'))
    assert not match(Command('echo Do not Migrate'))
    assert not match(Command('manage.py help'))



# Generated at 2022-06-14 09:58:43.443350
# Unit test for function match
def test_match():
    assert match({'output': ' --merge: will just attempt the migration'})
    assert not match({'output': 'migrate'})

# Generated at 2022-06-14 09:58:51.977108
# Unit test for function match
def test_match():
    assert match({'script': 'python manage.py migrate', 'output': '--merge: will just attempt the migration'})
    assert match({'script': 'manage.py migrate', 'output': '--merge: will just attempt the migration'})
    assert not match({'script': 'python manage.py migrate', 'output': '--fake-option: will just attempt the migration'})
    assert not match({'script': 'python manage.py fake-command', 'output': '--merge: will just attempt the migration'})



# Generated at 2022-06-14 09:59:04.088870
# Unit test for function match
def test_match():
    assert(match(
        Command('python3 manage.py migrate', '', 0, '', '', '')
    ))

    assert(not match(
        Command('python3 manage.py ', '', 0, '', '', '')
    ))

    assert(not match(
        Command('python3 manage.py makemigrations', '', 0, '', '', '')
    ))

    assert(not match(
        Command('python3 manage.py makemigrations --merge', '', 0, '', '', '')
    ))



# Generated at 2022-06-14 09:59:13.601611
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert match(Command('python3 manage.py migrate'))

# Generated at 2022-06-14 09:59:18.010033
# Unit test for function match
def test_match():
    assert True == match(
        Command("python manage.py migrate --merge: will just attempt the migration"))
    assert False == match(
        Command("python manage.py migrate"))
    assert False == match(
        Command("python manage.py"))


# Generated at 2022-06-14 09:59:27.004668
# Unit test for function match
def test_match():
    command = Command(script='python manage.py migrate', output='Migrations for \'tracker\':')
    assert not match(command)

    command = Command(script='python manage.py migrate', output='--merge: will just attempt the migration')
    assert not match(command)

    command = Command(script='python manage.py migratemigrate --merge',
                      output='--merge: will just attempt the migration')
    assert not match(command)

    command = Command(script='python manage.py migrate',
                      output='--merge: will just attempt the migration')
    assert match(command)



# Generated at 2022-06-14 09:59:32.601369
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate', '', 1, None))
    assert not match(Command('python manage.py makemigrations', '', 1, None))
    assert not match(Command('python manage.py migrate --fake', '', 1, None))
    assert not match(Command('python manage.py syncdb', '', 1, None))



# Generated at 2022-06-14 09:59:45.207871
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge: will just attempt the migration', '', 3, None))
    assert match(Command('python manage.py migrate --merge', '', 3, None))
    assert match(Command('python manage.py migrate  --merge ', '', 3, None))
    assert match(Command('python manage.py migrate', '', 3, None))
    assert match(Command('python manage.py migrate   ', '', 3, None))
    assert not match(Command('manage.py migrate --merge', '', 3, None))
    assert not match(Command('python app/manage.py migrate --merge', '', 3, None))
    assert not match(
        Command('python manage.py migrate --merge --merge', '', 3, None))

# Generated at 2022-06-14 09:59:52.161836
# Unit test for function match
def test_match():
    assert match(Command(script='./manage.py migrate --fake'))
    assert match(Command(script='python manage.py migrate --fake'))
    assert not match(Command(script='python manage.py dummy'))
    assert not match(Command(script='python manage.py migrate'))
    assert match(Command(script='python manage.py migrate', output='will just attempt the migration'))
    assert not match(Command(script='python manage.py migrate', output='will just drop the migration'))

# Generated at 2022-06-14 10:00:01.471979
# Unit test for function match
def test_match():
    assert match(Command('$ python manage.py migrate\n' +
                         'You are trying to add a non-nullable field \'size\' to file without a default; ' +
                         'we can\'t do that (the database needs something to populate existing rows).\n' +
                         'Please select a fix:\n' +
                         ' 1) Provide a one-off default now (will be set on all existing rows)\n' +
                         ' 2) Quit, and let me add a default in models.py\n' +
                         'Select an option: '))


# Generated at 2022-06-14 10:00:07.751624
# Unit test for function match
def test_match():
    red = 'manage.py makemigrations --merge: will just attempt the migration'
    yellow = 'manage.py migrate - will actually create the migration'
    white = 'manage.py'
    assert match(message.Message(body=red.split(" "))) is True
    assert match(message.Message(body=yellow.split(" "))) is False
    assert match(message.Message(body=white.split(" "))) is False



# Generated at 2022-06-14 10:00:18.098012
# Unit test for function match
def test_match():
    assert match(Command(script='./manage.py --help', output='manage.py migrate'))
    assert match(Command(script='./manage.py migrate --help', output='manage.py migrate'))
    assert match(Command(script='./manage.py migrate --merge --help', output='manage.py migrate'))
    assert match(Command(script='./manage.py migrate --merge', output=u'manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command(script='./manage.py --merge', output=u'manage.py migrate --merge: will just attempt the migration'))

# Generated at 2022-06-14 10:00:24.951594
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge'))
    assert match(Command('python manage.py makemigrations --merge'))
    assert not match(Command('python manage.py makemigrations'))
    assert not match(Command('python manage.py migrate'))


# Generated at 2022-06-14 10:00:41.617696
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert match(Command('python manage.py migrate --merge --fake'))
    assert not match(Command('python manage.py migrate --fake'))
    assert not match(Command('python manage.py makemigrations --merge', '', ''))



# Generated at 2022-06-14 10:00:46.834355
# Unit test for function match
def test_match():
    assert True == match(wrap_command('manage.py migrate', '--merge: will just attempt the migration'))
    assert True == match(wrap_command('python manage.py migrate', '--merge: will just attempt the migration'))
    assert False == match(wrap_command('manage.py migrate', ''))
    assert False == match(wrap_command('manage.py test', '--merge: will just attempt the migration'))


# Generated at 2022-06-14 10:00:51.040885
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate'))
    assert match(Command('python manage.py migrate --merge: will just attempt the migration'))
    assert not match(Command('python manage.py help'))


# Generated at 2022-06-14 10:01:03.119270
# Unit test for function match
def test_match():
    # matches
    assert True == match(Command(script='manage.py migrate'))
    assert True == match(Command(script='manage.py migrate --merge'))

    # does not match
    assert False == match(Command(script='manage.py migrate --plan'))
    assert False == match(Command(script='manage.py help'))
    assert False == match(Command(script='manage.py runserver'))
    assert False == match(Command(script='manage.py makemigrations'))



# Generated at 2022-06-14 10:01:05.888530
# Unit test for function match
def test_match():
    command = Command('manage.py', 'migrate', '', '', '', '')
    assert match(command) == True


# Generated at 2022-06-14 10:01:09.545249
# Unit test for function match
def test_match():
    assert match(Command('/usr/bin/env python manage.py migrate'
                         ' --merge: will just attempt the migration'))
    assert not match(Command('/usr/bin/env python manage.py migrate'))

# Generated at 2022-06-14 10:01:22.663267
# Unit test for function match

# Generated at 2022-06-14 10:01:32.825924
# Unit test for function match
def test_match():
    assert match(Command('manage.py migrate'))
    assert match(Command('python manage.py migrate'))
    assert match(Command('sh manage.py migrate'))
    assert match(Command('make manage.py migrate'))

    assert not match(Command('manage.py syncdb'))
    assert not match(Command('manage.py migrate'))


# Generated at 2022-06-14 10:01:37.642762
# Unit test for function match
def test_match():
    assert match(Command('/home/user/env/bin/python manage.py migrate',
                'Running migrations: \n \
                !!! the commented migration below will not be merged')), \
                'django-merge-migration failed to match a typical migrate command'


# Generated at 2022-06-14 10:01:41.119976
# Unit test for function match
def test_match():
    assert match(Command('python manage.py migrate  --merge: will just attempt the migration'))
    assert not match(Command('python manage.py curate'))
