

# Generated at 2022-06-14 10:36:02.734982
# Unit test for function match
def test_match():
    # Testing for match returns true
    assert (
        match(Command("pacman -Suqe" "error: invalid option '-q'", "")) is not None
    )
    # Testing get_new_command
    assert (get_new_command(Command("pacman -Suqe" "error: invalid option '-q'", ""))
    == 'pacman -SuQe"error: invalid option \'\\\'-q\'"')

# Generated at 2022-06-14 10:36:11.020725
# Unit test for function match
def test_match():
    for_app("pacman")(match)
    assert match(Command('pacman -S', 'error: invalid option -- \'S\''))
    assert not match(Command('pacman -S bash', 'error: invalid option -- \'S\''))

# Generated at 2022-06-14 10:36:15.586339
# Unit test for function match
def test_match():
    command = Command("pacman -Q", "error: invalid option '-Q'")
    assert match(command)

    command = Command("pacman -Qt", "error: invalid option '-Q'")
    assert match(command)

    command = Command("pacman -Qt", "")
    assert not match(command)



# Generated at 2022-06-14 10:36:29.621381
# Unit test for function match
def test_match():
    assert match(Command('pacman -Qud', 'error: invalid option \'-Q\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-d\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-q\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-u\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-r\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-f\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-s\''))
    assert match(Command('pacman -Qud', 'error: invalid option \'-t\''))

# Generated at 2022-06-14 10:36:31.332445
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -Sy')) == 'pacman -Syy'

# Generated at 2022-06-14 10:36:35.328953
# Unit test for function match
def test_match():
    assert match(Command("pacman -p", ""))
    assert not match(Command("pacman -s", ""))
    assert not match(Command("pacman -rs", ""))


# Generated at 2022-06-14 10:36:46.374975
# Unit test for function match
def test_match():
    assert match(Command("sudo pacman -f", "",
        "error: invalid option '\\-f'\n\
        Usage:  pacman \\[options\\] \\[\\-\\] \\[<operations>\\] [...]\n\
        [...]", ""))

    assert match(Command("sudo pacman -s", "",
        "error: invalid option '\\-s'\n\
        Usage:  pacman \\[options\\] \\[\\-\\] \\[<operations>\\] [...]\n\
        [...]", ""))

    assert match(Command("pacman -f", "",
        "there is no package registered matching 'f'\n\
        Do you meant 'c' or 'g'?", ""))


# Generated at 2022-06-14 10:36:49.682596
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='pacman -s pkgname')
    assert get_new_command(command) == 'pacman -S pkgname'

# Generated at 2022-06-14 10:36:54.893968
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -r vim")) == "pacman -R vim"
    assert get_new_command(Command("pacman -qe vim")) == "pacman -Qe vim"

# Generated at 2022-06-14 10:37:03.513366
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("sudo pacman -Suy") == "sudo pacman -Syu"
    assert get_new_command("sudo pacman -Suyu") == "sudo pacman -Syu"
    assert get_new_command("sudo pacman -Syu") == "sudo pacman -Syu"
    assert get_new_command("sudo pacman -Sy") == "sudo pacman -Sy"
    assert get_new_command("sudo pacman -Su") == "sudo pacman -Su"
    assert get_new_command("sudo pacman -S") == "sudo pacman -S"

# Generated at 2022-06-14 10:37:18.458566
# Unit test for function match

# Generated at 2022-06-14 10:37:23.288409
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -Suy',
            'error: invalid option \'-S\'\n\nSee pacman(8) for more information.\n'))
    assert not match(Command('sudo pacman -Suy',
            'error: invalid option \'-S\'\n\nSee pacman(8) for more information.\n',
            'sudo pacman -Syu'))


# Generated at 2022-06-14 10:37:36.002815
# Unit test for function match
def test_match():
    assert match(Command("pacman -s foo", "", "error: invalid option '-s'"))
    assert match(Command("pacman -u foo", "", "error: invalid option '-u'"))
    assert match(Command("pacman -r foo", "", "error: invalid option '-r'"))
    assert match(Command("pacman -q foo", "", "error: invalid option '-q'"))
    assert match(Command("pacman -f foo", "", "error: invalid option '-f'"))
    assert match(Command("pacman -d foo", "", "error: invalid option '-d'"))
    assert match(Command("pacman -v foo", "", "error: invalid option '-v'"))
    assert match(Command("pacman -t foo", "", "error: invalid option '-t'"))

# Generated at 2022-06-14 10:37:40.601716
# Unit test for function match
def test_match():
    assert match(Command('pacman -Syu', 'error: invalid option -u'))
    assert match(Command('pacman -S upd', 'error: invalid option -u'))
    assert not match(Command('pacman -S', 'error: invalid option -S'))


# Generated at 2022-06-14 10:37:45.962296
# Unit test for function match
def test_match():
    assert match(Command('pacman -q', '', 'error: invalid option')), match(Command('pacman -q', '', ''))
    assert not match(Command('pacman -i', '', 'error: invalid option')), match(Command('pacman -i', '', ''))

# Generated at 2022-06-14 10:37:49.514228
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("sudo pacman --version", "sudo: pacman: command not found")
    new_command = get_new_command(command)
    assert new_command == "sudo pacman --version"



# Generated at 2022-06-14 10:37:59.489445
# Unit test for function match

# Generated at 2022-06-14 10:38:04.242812
# Unit test for function get_new_command
def test_get_new_command():
    """
    This function will test the function get_new_command.
    """
    # Setup
    from thefuck.rules.pacman_invalid_option import get_new_command
    # Exercise
    command = "pacman -q"
    assert "pacman -Q" == get_new_command(command)

# Generated at 2022-06-14 10:38:12.464704
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("sudo pacman -U something")) == "sudo pacman -U something"
    assert get_new_command(Command("sudo pacman -s something")) == "sudo pacman -S something"
    assert get_new_command(Command("sudo pacman -d something")) == "sudo pacman -D something"
    assert get_new_command(Command("sudo pacman -q something")) == "sudo pacman -Q something"
    assert get_new_command(Command("sudo pacman -r something")) == "sudo pacman -R something"
    assert get_new_command(Command("sudo pacman -f something")) == "sudo pacman -F something"

# Generated at 2022-06-14 10:38:24.982707
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -Rdd", "", "error: invalid option '-d'")) == "pacman -RDD"
    assert get_new_command(Command("pacman -Q", "", "error: invalid option '-Q'")) == "pacman -Qq"
    assert get_new_command(Command("pacman -Sdd", "", "error: invalid option '-d'")) == "pacman -SDD"
    assert get_new_command(Command("pacman -Rdd", "", "error: invalid option '-d'")) == "pacman -RDD"
    assert get_new_command(Command("pacman -d", "", "error: invalid option '-d'")) == "pacman -D"

# Generated at 2022-06-14 10:38:31.896416
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="pacman -s firefox", stdout="error: invalid option '-s'")
    assert get_new_command(command) == "pacman -S firefox"

# Generated at 2022-06-14 10:38:34.132045
# Unit test for function match
def test_match():
    assert match(Command("pacman -rq supa"))
    assert not match(Command("pacman -U supa"))

# Generated at 2022-06-14 10:38:38.286973
# Unit test for function match
def test_match():
    command = Command("pacman -u", "error: invalid option '-u'")
    assert match(command)
    command = Command("pacman -p", "error: invalid option '-p'")
    assert not match(command)


# Generated at 2022-06-14 10:38:44.062395
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -S python", "error: invalid option '-S'\n")) == "pacman -S python"
    assert get_new_command(Command("pacman -r python", "error: invalid option '-r'\n")) == "pacman -R python"
    assert get_new_command(Command("pacman -f python", "error: invalid option '-f'\n")) == "pacman -F python"
    assert get_new_command(Command("pacman -q python", "error: invalid option '-q'\n")) == "pacman -Q python"
    assert get_new_command(Command("pacman -d python", "error: invalid option '-d'\n")) == "pacman -D python"

# Generated at 2022-06-14 10:38:56.134841
# Unit test for function get_new_command
def test_get_new_command():
	assert get_new_command(Command('pacman -r $package',
	                                           output='error: invalid option -r')) == 'pacman -R $package'
	assert get_new_command(Command('pacman -u $package',
			                                               output='error: invalid option -u')) == 'pacman -U $package'
	assert get_new_command(Command('pacman -S $package',
			                                               output='error: invalid option -S')) == 'pacman -S $package'
	assert get_new_command(Command('pacman -t $package',
			                                               output='error: invalid option -t')) == 'pacman -T $package'

# Generated at 2022-06-14 10:38:59.671197
# Unit test for function match
def test_match():
    assert match(Command('pacman -ufs', '', 'error: invalid option -- s'))
    assert not match(Command('pacman -Rdd', '', 'error: invalid option -- d'))


# Generated at 2022-06-14 10:39:02.539046
# Unit test for function match
def test_match():
    command = Command("sudo pacman -qe", "error: invalid option '-q'\n")
    assert match(command)



# Generated at 2022-06-14 10:39:06.039234
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -r xfce4", "error: invalid option '-r'", "")) == "pacman -R xfce4"

# Generated at 2022-06-14 10:39:08.608032
# Unit test for function match
def test_match():
    assert match(Command('pacman -u -Su -y'))
    assert not match(Command('ls -la'))



# Generated at 2022-06-14 10:39:14.755558
# Unit test for function match
def test_match():
    assert (
        not match(Command("pacman -S blue", "", ""))
        or not match(Command("pacman -S blue", "", ""))
    )
    assert match(Command("pacman -s blue", "", ""))
    assert match(Command("pacman -q blue", "", ""))
    assert match(Command("pacman -f blue", "", ""))
    assert match(Command("pacman -d blue", "", ""))
    assert match(Command("pacman -v blue", "", ""))
    assert match(Command("pacman -t blue", "", ""))



# Generated at 2022-06-14 10:39:23.927795
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo pacman -S blabla', 'error: invalid option -- \'S\'\n')) == 'sudo pacman -S blabla'

# Generated at 2022-06-14 10:39:28.603672
# Unit test for function match
def test_match():
    # Test a mock command output
    command = Command('pacman -Suyf', 'error: invalid option')
    assert match(command)
    # Test an invalid output
    invalid_command = Command('pacman -Suyf', 'no error: invalid option')
    assert not match(invalid_command)



# Generated at 2022-06-14 10:39:31.416095
# Unit test for function match
def test_match():
    assert match(Command("pacman -Suy"))
    assert not match(Command("pacman -Suy", "error: invalid option '-'\n"))

# Generated at 2022-06-14 10:39:35.032519
# Unit test for function match
def test_match():
    assert match(Command('pacman -q --force -d --verbose', '', ''))
    assert not match(Command('pacman --help', '', ''))



# Generated at 2022-06-14 10:39:42.047603
# Unit test for function match
def test_match():
    assert match(Command('pacman -Qu'))
    assert match(Command('pacman -s'))
    assert match(Command('pacman -Q -q'))
    assert match(Command('pacman -R -u -s'))
    assert match(Command('pacman -Qi -q packa'))
    assert not match(Command('pacman -search packa'))


# Generated at 2022-06-14 10:39:45.411483
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -s a")) == "pacman -S a"

# Generated at 2022-06-14 10:39:56.445679
# Unit test for function match
def test_match():
    enabled = thefuck.types.Settings({'enabled': True}, None)
    disabled = thefuck.types.Settings({'enabled': False}, None)
    wrong_output = "error: invalid option '-d'"
    correct_output = "error: invalid option '-U'"
    assert match(thefuck.types.Command('pacman -Sd', correct_output, disabled))is None
    assert match(thefuck.types.Command('pacman -Sd', correct_output, enabled))is not None
    assert match(thefuck.types.Command('pacman -Sd', wrong_output, disabled))is None
    assert match(thefuck.types.Command('pacman -Sd', wrong_output, enabled))is not None
    assert match(thefuck.types.Command('pacman -Sdu', correct_output, disabled))is None
   

# Generated at 2022-06-14 10:39:59.876026
# Unit test for function match
def test_match():
    output = "error: invalid option '-c'"
    assert match(Command("pacman -c", output))
    assert not match(Command("pacman -c", ""))

# Generated at 2022-06-14 10:40:14.238014
# Unit test for function match
def test_match():
    def guard(output):
        return match(Command(script="pacman -Ss pacman", output=output))

    assert guard("error: invalid option '-S'")
    assert guard("error: invalid option '-s'")
    assert guard("error: invalid option '-q'")
    assert guard("error: invalid option '-u'")
    assert guard("error: invalid option '-r'")
    assert guard("error: invalid option '-f'")
    assert guard("error: invalid option '-d'")
    assert guard("error: invalid option '-v'")
    assert guard("error: invalid option '-t'")
    assert not guard("error: invalid option '-z'")
    assert not guard("error: invalid option '--asdf'")

# Generated at 2022-06-14 10:40:19.581560
# Unit test for function get_new_command
def test_get_new_command():
    '''
    unit test for function get_new_command
    '''
    assert get_new_command(Command('pacman -dd', '')) == 'pacman -DD'
    assert get_new_command(Command('pacman -du', '')) == 'pacman -DU'

# Generated at 2022-06-14 10:40:37.619202
# Unit test for function match
def test_match():
    assert match(Command("pacman -d -y"))
    assert match(Command("pacman -g -f"))
    assert match(Command("pacman -u -d -y"))
    assert match(Command('pacman -d -f'))
    assert match(Command('pacman -r -d -q'))
    assert not match(Command("pacman -d -f -y"))
    assert not match(Command("pacman -S"))
    assert not match(Command("pacman -Q"))
    assert not match(Command("pacman -F"))
    assert not match(Command("pacman -T"))
    assert not match(Command("pacman -V"))


# Generated at 2022-06-14 10:40:41.655875
# Unit test for function match
def test_match():
    assert match(Command("paman -F", "error: invalid option '-F'"))
    assert not match(Command("paman --help", "usage: paman ... "))

# Generated at 2022-06-14 10:40:50.763656
# Unit test for function match
def test_match():
    assert match(Command("pacman -f", "", "error: invalid option '-f'\n"))
    assert match(Command("pacman -v -r", "", "error: invalid option '-r'\n"))
    assert match(
        Command("pacman -Su", "", "error: invalid/unknown option '-Su'\n")
    )
    assert match(Command("pacman -u", "", "error: no targets specified (use -h for help)\n"))
    assert not match(Command("pacman -U", "", "warning: target package 'asd' was not found in sync database\n"))


# Generated at 2022-06-14 10:40:58.911139
# Unit test for function match
def test_match():
    assert match(Command('pacman -u ', ''))
    assert match(Command('pacman -r ', ''))
    assert match(Command('pacman -s ', ''))
    assert not match(Command('pacman -d ', ''))
    assert not match(Command('pacman -f ', ''))
    assert match(Command('pacman -R ', ''))


# Generated at 2022-06-14 10:41:08.382537
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('pacman -U /tmp/arch/extra/gcc-libs-6.3.1-1-x86_64.pkg.tar.xz') == 'pacman -U /tmp/arch/extra/gcc-libs-6.3.1-1-x86_64.pkg.tar.xz'
    assert get_new_command('pacman -Rddn base-devel') == 'pacman -RDDN base-devel'
    assert get_new_command('pacman -Scc') == 'pacman -SCC'

# Generated at 2022-06-14 10:41:16.854170
# Unit test for function match
def test_match():
    assert match(Command("pacman -r hoge",
                         "error: invalid option '-r'\n\
                         See 'pacman --help' for more information."))
    assert not match(Command("pacman -r hoge",
                         "error: invalid option '-r'\n\
                         See 'pacman -h' for more information."))
    assert not match(Command("pacman -hoge",
                         "error: invalid option '-h'\n\
                         See 'pacman -h' for more information."))


# Generated at 2022-06-14 10:41:22.678627
# Unit test for function match
def test_match():
    assert match(Command('pacman -qfs'))
    assert not match(Command('pacman -Qfs'))
    assert not match(Command('pacman -Syu'))
    assert match(Command('sudo pacman -qfs'))
    #assert not match(Command('sudo pacman -Qfs'))
    #assert not match(Command('sudo pacman -Syu'))



# Generated at 2022-06-14 10:41:30.787134
# Unit test for function match
def test_match():
    assert match(Command("pacman -u file.txt", "", "error: invalid option '-u'\n"))
    assert match(Command("pacman -R file.txt", "", "error: invalid option '-R'\n"))
    assert match(Command("pacman -s file.txt", "", "error: invalid option '-s'\n"))
    assert match(Command("pacman -q file.txt", "", "error: invalid option '-q'\n"))
    assert match(Command("pacman -f file.txt", "", "error: invalid option '-f'\n"))
    assert match(Command("pacman -d file.txt", "", "error: invalid option '-d'\n"))

# Generated at 2022-06-14 10:41:35.583139
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -q', 'error: invalid option \'q\', see pacman -h')) == 'pacman -Q'
    assert get_new_command(Command('pacman -r', 'error: invalid option \'r\', see pacman -h')) == 'pacman -R'

# Generated at 2022-06-14 10:41:43.763193
# Unit test for function match
def test_match():
    assert match(Command("pacman -y update", "error: invalid option '-y'\n",))
    assert match(Command("pacman -qyr update", "error: invalid option '-y'\n",))
    assert not match(Command("pacman -y update", "error: invalid option '-Y'\n",))
    assert not match(Command("pacman -y update", "error: invalid option '-y'\n",))

# Generated at 2022-06-14 10:42:03.322688
# Unit test for function match
def test_match():
    assert match(Command('pacman -Syu', '', '', 0, ''))
    assert match(Command('pacman -r', '', '', 0, ''))
    assert match(Command('pacman -du', '', '', 0, ''))

    assert not match(Command('pacman -Syu', '', '', 0, ''))
    assert not match(Command('pacman -r', '', '', 0, ''))
    assert not match(Command('pacman -du', '', '', 0, ''))



# Generated at 2022-06-14 10:42:06.122029
# Unit test for function match
def test_match():
    assert match(command=Command('pacman -q'))
    assert not match(command=Command('pacman -Q'))



# Generated at 2022-06-14 10:42:16.373823
# Unit test for function match
def test_match():
    command = Command("pacman -s kernel")
    assert match(command)
    command = Command("pacman -y kernel")
    assert not match(command)
    command = Command("pacman -u kernel")
    assert match(command)
    command = Command("pacman -q kernel")
    assert match(command)
    command = Command("pacman -f kernel")
    assert match(command)
    command = Command("pacman -R kernel")
    assert match(command)
    command = Command("pacman -r kernel")
    assert match(command)
    command = Command("pacman -v kernel")
    assert match(command)
    command = Command("pacman lua")
    assert not match(command)


# Generated at 2022-06-14 10:42:19.171792
# Unit test for function match
def test_match():
    # Test with valid options
    assert match(Command("pacman -s hello"))
    # Test with invalid options
    assert not match(Command("pacman --version"))

# Generated at 2022-06-14 10:42:23.932660
# Unit test for function match
def test_match():
    assert match(Command('pacman -u', 'error: invalid option \'-u\'\nTry `pacman --help\' for more information.'))
    assert not match(Command('pacman -u', 'error: invalid option'))



# Generated at 2022-06-14 10:42:28.076701
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(
        "pacman -S foo", "error: invalid option '-S'\nSee 'pacman --help' for more information.",
    )

    assert get_new_command(command) == "pacman -S --needed foo"

# Generated at 2022-06-14 10:42:34.480318
# Unit test for function match
def test_match():
    assert match(
        Command(
            script="pacman -f test",
            output="error: invalid option '-f'\nSee 'pacman --help' for more information.",
        )
    )
    assert not match(Command(script="sudo pacman -u test", output=""))
    assert not match(
        Command(
            script="pacman -u test",
            output="error: invalid option '-u'\nSee 'pacman --help' for more information.",
        )
    )

# Generated at 2022-06-14 10:42:43.399087
# Unit test for function match
def test_match():
    assert match(Command('pacman -U pacman.pkg.tar.xz', 'error: invalid option -- \'U\''))
    assert match(Command('pacman -s python2', 'error: invalid option -- \'s\''))
    assert match(Command('pacman -r python2', 'error: invalid option -- \'r\''))
    assert match(Command('pacman -u python2', 'error: invalid option -- \'u\''))
    assert match(Command('pacman -v python2', 'error: invalid option -- \'v\''))
    assert match(Command('pacman -t python2', 'error: invalid option -- \'t\''))
    asser

# Generated at 2022-06-14 10:42:55.613000
# Unit test for function match
def test_match():
    """
    Test match function of the 'pacman' module
    """
    command = Command("pacman -qq -y", "\nerror: invalid option '-y'")
    assert match(command)
    command = Command("pacman -u -y", "\nerror: invalid option '-y'")
    assert match(command)
    command = Command("pacman -s -y", "\nerror: invalid option '-y'")
    assert match(command)
    command = Command("pacman -q -y", "\nerror: invalid option '-y'")
    assert match(command)
    command = Command("pacman -r -y", "\nerror: invalid option '-y'")
    assert match(command)
    command = Command("pacman -f -y", "\nerror: invalid option '-y'")

# Generated at 2022-06-14 10:42:58.122083
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('error: invalid option -- s') == 'error: invalid option -- S'

# Generated at 2022-06-14 10:43:33.752469
# Unit test for function match
def test_match():
    assert match(Command(script="pacman -e", output="error: invalid option '-e'"))
    assert match(Command(script="pacman -r", output="error: invalid option '-r'"))
    assert match(Command(script="pacman -i", output="error: invalid option '-i'"))
    assert match(Command(script="pacman -g", output="error: invalid option '-g'"))
    assert match(Command(script="pacman -q", output="error: invalid option '-q'"))
    assert match(Command(script="pacman -u", output="error: invalid option '-u'"))
    assert match(Command(script="pacman -f", output="error: invalid option '-f'"))

# Generated at 2022-06-14 10:43:36.301274
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -s -y'))
    assert not match(Command('sudo pacman -S -y'))

# Generated at 2022-06-14 10:43:41.991343
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("pacman -Sy")
    assert get_new_command(command) == "pacman -Sy"
    command = Command("pacman -Syu")
    assert get_new_command(command) == "pacman -Syu"
    command = Command("pacman -Syu foo bar")
    assert get_new_command(command) == "pacman -Syu foo bar"

# Generated at 2022-06-14 10:43:49.279560
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script='pacman -S numpy')) == 'pacman -S numpy'
    assert get_new_command(Command(script='pacman -R numpy')) == 'pacman -R numpy'
    assert get_new_command(Command(script='pacman -Q numpy')) == 'pacman -Q numpy'
    assert get_new_command(Command(script='pacman -f numpy')) == 'pacman -F numpy'
    assert get_new_command(Command(script='pacman -d numpy')) == 'pacman -D numpy'
    assert get_new_command(Command(script='pacman -r numpy')) == 'pacman -R numpy'

# Generated at 2022-06-14 10:43:54.619304
# Unit test for function match
def test_match():
    assert match(Command('pacman -Syy', ''))
    assert match(Command('pacman -Suy', ''))
    assert not match(Command('pacman -S', ''))
    assert not match(Command('pacman -Syy', ''))
    assert not match(Command('pacman -Syy --needed', ''))


# Generated at 2022-06-14 10:44:00.238642
# Unit test for function match
def test_match():
    assert match(Command('pacman -s bash', 'error: invalid option -s'))
    assert not match(Command('pacman -s bash', 'error: invalid option -t'))
    assert not match(Command('pacman --noconfirm -Rns package', 'error: invalid option -r'))

# Generated at 2022-06-14 10:44:11.934252
# Unit test for function match
def test_match():
    # Only tests the ones where there is no option to vary by upper/lower case
    assert match(Command("pacman -q", "error: invalid option '-q'"))
    assert match(Command("pacman -d", "error: invalid option '-d'"))
    assert match(Command("pacman -r", "error: invalid option '-r'"))
    assert match(Command("pacman -u", "error: invalid option '-u'"))

    assert match(Command("pacman -S", "error: invalid option '-S'"))
    assert match(Command("pacman -R", "error: invalid option '-R'"))
    assert match(Command("pacman -U", "error: invalid option '-U'"))
    assert match(Command("pacman -s", "error: invalid option '-s'"))

# Generated at 2022-06-14 10:44:18.091938
# Unit test for function match
def test_match():
    assert match(Command('pacman -r', 'error: invalid option -r\n'))
    assert not match(Command('pacman -r', 'error: invalid option -p\n'))
    assert not match(Command('pacman -R', 'error: invalid option -p\n'))


# Generated at 2022-06-14 10:44:19.550879
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command()) == "sudo pacman"

# Generated at 2022-06-14 10:44:29.182107
# Unit test for function match
def test_match():
    assert not match(Command('pacman -Su', ''))
    assert match(Command('pacman -Suq', 'error: invalid option -q'))
    assert match(Command('pacman -x -Su', 'error: invalid option -x'))
    assert not match(Command('pacman -Su', 'error: invalid option -x'))
    assert not match(Command('pacman -Su', 'error: invalid option -d'))
    assert not match(Command('pacman -Su', 'error: invalid option -q'))
    assert not match(Command('pacman -Suq', 'error: invalid option -x'))


# Generated at 2022-06-14 10:45:21.591502
# Unit test for function match
def test_match():
    command = Command("pacman -qy")
    assert match(command)

    command = Command("pacman -Sy")
    assert match(command)

    command = Command("pacman -qy foo")
    assert not match(command)

    command = Command("pacman -Sy foo")
    assert not match(command)

    command = Command("foo -Sy")
    assert not match(command)



# Generated at 2022-06-14 10:45:34.772500
# Unit test for function match
def test_match():
    assert match(Command("pacman -y -u", "error: invalid option '-y'\n"))
    assert match(Command("pacman -u -u", "error: invalid option '-u'\n"))
    assert match(Command("pacman -u -y", "error: invalid option '-y'\n"))
    assert match(Command("pacman -u -d", "error: invalid option '-d'\n"))
    assert match(Command("pacman -u -q", "error: invalid option '-q'\n"))
    assert match(Command("pacman -u -x", "error: invalid option '-x'\n"))
    assert match(Command("pacman -u -f", "error: invalid option '-f'\n"))

# Generated at 2022-06-14 10:45:37.663954
# Unit test for function match
def test_match():
    assert match(Command("pacman -s vim", ""))
    assert not match(Command("pacman -s vim", "", ""))

# Generated at 2022-06-14 10:45:46.443392
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -Qi") == "pacman -QI"
    assert get_new_command("pacman -Qi linux") == "pacman -QI linux"
    assert get_new_command("sudo pacman -Qi linux") == "sudo pacman -QI linux"
    assert get_new_command("pacman -s linux") == "pacman -S linux"
    assert get_new_command("sudo pacman -R linux") == "sudo pacman -R linux"

# Generated at 2022-06-14 10:45:52.000617
# Unit test for function match
def test_match():
    assert match(Command("pacman -qp", "ignore"))
    assert not match(Command("pacman -Qp", "ignore"))
    assert not match(Command("pacman -Qp", "ignore", error="error: invalid option '-Q'\n"))
