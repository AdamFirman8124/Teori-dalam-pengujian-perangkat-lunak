

# Generated at 2022-06-14 10:35:55.489493
# Unit test for function match
def test_match():
    command = Command("pacma -S vim-athena", "error: invalid option -- 'S'")
    assert match(command)
    command = Command("pacman -y -q", "error: invalid option -- 'q'")
    assert match(command)


# Generated at 2022-06-14 10:36:10.298956
# Unit test for function match
def test_match():
    assert match(Command("pacman -qy", """error: invalid option '-q'

Usage:
    pacman -[VSLiqurstvfd] [options] ..."""))
    assert match(Command("pacman -qy", """error: invalid option '-y'

Usage:
    pacman -[VSLiqurstvfd] [options] ..."""))
    assert not match(Command("pacman -Syy", """"error: invalid option '-y'

Usage:
    pacman -[VSLiqurstvfd] [options] ..."""))
    assert not match(Command("pacman --help", """Usage:
    pacman -[VSLiqurstvfd] [options] ..."""))

# Generated at 2022-06-14 10:36:18.655593
# Unit test for function match
def test_match():
    assert match(Command('pacman -qe', 'error: invalid option \'q\''))
    assert match(Command('pacman -r', 'error: invalid option \'r\''))
    assert match(Command('pacman -s', 'error: invalid option \'s\''))
    assert match(Command('pacman -f', 'error: invalid option \'f\''))
    assert match(Command('pacman -u', 'error: invalid option \'u\''))
    assert match(Command('pacman -v', 'error: invalid option \'v\''))
    assert match(Command('pacman -d', 'error: invalid option \'d\''))
    assert not match(Command('pacman -qe', 'error: invalid option \'e\''))

# Generated at 2022-06-14 10:36:30.697140
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -Qe pkg1 pkg2 pkg3")) == "pacman -QE pkg1 pkg2 pkg3"
    assert get_new_command(Command("pacman -Qr pkg")) == "pacman -QR pkg"
    assert get_new_command(Command("pacman -Qqe pkg1 pkg2 pkg3")) == "pacman -QQE pkg1 pkg2 pkg3"
    assert get_new_command(Command("pacman -Qsqe pkg1 pkg2 pkg3")) == "pacman -QQSE pkg1 pkg2 pkg3"

# Generated at 2022-06-14 10:36:32.867097
# Unit test for function match
def test_match():
    command = Command("sudo pacman -r")
    assert match(command) is True


# Generated at 2022-06-14 10:36:38.931522
# Unit test for function get_new_command
def test_get_new_command():
    assert "pacman -Syu" == get_new_command(Command("pacman -syu", " error"))
    assert "pacman -Syu" == get_new_command(Command("pacman -syu", " error"))
    assert "pacman -Syyu" == get_new_command(Command("pacman -syyu", " error"))

# Generated at 2022-06-14 10:36:47.770910
# Unit test for function match
def test_match():
    assert match(Command('', 'error: invalid option'))
    assert match(Command('pacman', 'error: invalid option'))
    assert match(Command('', 'error: invalid option -q'))
    assert match(Command('', 'error: invalid option -s'))
    assert match(Command('', 'error: invalid option -r'))
    assert match(Command('', 'error: invalid option -u'))
    assert match(Command('', 'error: invalid option -f'))
    assert match(Command('', 'error: invalid option -d'))
    assert match(Command('', 'error: invalid option -v'))
    assert match(Command('', 'error: invalid option -t'))
    assert not match(Command('', 'error: invalid option -c'))

# Generated at 2022-06-14 10:36:49.887833
# Unit test for function match
def test_match():
    command = Command("pacman -q hello", "error: invalid option '-q'")
    assert match(command)



# Generated at 2022-06-14 10:36:55.478617
# Unit test for function match
def test_match():
    assert match(Command("pacman -Rs linux", "error: invalid option '-r'")
                 )
    assert match(Command("pacman -Us linux", "error: invalid option '-u'")
                 )

# Generated at 2022-06-14 10:37:05.700593
# Unit test for function match
def test_match():
    assert match(Command('pacman -s',
        "error: invalid option '-s'\n\nSee pacman(8) for more information.",
        '', 1))
    assert match(Command('pacman -q',
        "error: invalid option '-q'\n\nSee pacman(8) for more information.",
        '', 1))
    assert match(Command('pacman -u',
        "error: invalid option '-u'\n\nSee pacman(8) for more information.",
        '', 1))
    assert not match(Command('pacman -S',
        "Linux 5.4.7-arch1-1 (x86_64)\nresolving dependencies...",
        '', 1))
    assert not match(Command('pacman -S', '', '', 1))


# Generated at 2022-06-14 10:37:14.672831
# Unit test for function match
def test_match():
    assert match(Command("pacman -r foo", "error: invalid option '-r'\n"))
    assert match(Command("pacman -d foo", "error: invalid option '-d'\n"))
    assert match(Command("pacman -q foo", "error: invalid option '-q'\n"))
    assert match(Command("pacman -u foo", "error: invalid option '-u'\n"))



# Generated at 2022-06-14 10:37:22.780102
# Unit test for function match
def test_match():
    assert not match(Command("pacman -Syy", "", ""))
    assert match(Command("pacman -y", "", "error: invalid option '-y'"))
    assert match(Command("pacman -p", "", "error: invalid option '-p'"))
    assert match(Command("pacman -p", "", "error: invalid option '-p'"))
    assert match(Command("pacman -s", "", "error: invalid option '-s'"))
    assert match(Command("pacman -r", "", "error: invalid option '-r'"))
    assert match(Command("pacman -q", "", "error: invalid option '-q'"))
    assert match(Command("pacman -d", "", "error: invalid option '-d'"))

# Generated at 2022-06-14 10:37:28.040177
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -q', 'error: invalid option -q'))
    assert match(Command('pacman -f', 'error: invalid option -f'))
    assert not match(Command('pacman -r', 'error: invalid option -r'))


# Generated at 2022-06-14 10:37:33.985409
# Unit test for function get_new_command
def test_get_new_command():
    from tests.utils import Command

    # Test all options
    for option in "-dfqrstuv":
        command_output = "error: invalid option '{}'".format(option)
        assert get_new_command(Command(command_output)) == "pacman -{}".format(option.upper())

    # Test for more then one option

# Generated at 2022-06-14 10:37:38.219345
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -sq')) == 'pacman -Sq'
    assert get_new_command(Command('pacman -fq')) == 'pacman -Fq'

# Generated at 2022-06-14 10:37:41.220665
# Unit test for function match
def test_match():
    command = Command("pacman -v -S git")
    assert match(command)



# Generated at 2022-06-14 10:37:50.117871
# Unit test for function match
def test_match():
	# Success case 1
	command = Command("pacman -Qd")
	assert match(command)

	# Success case 2
	command = Command("pacman -Rd")
	assert match(command)

	# Failure case 1
	command = Command("pacman -Q")
	assert not match(command)

	# Failure case 2
	command = Command("pacman -Sd")
	assert not match(command)

	# Failure case 3
	command = Command("pacman -ed")
	assert not match(command)


# Generated at 2022-06-14 10:38:04.657869
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -S python-pip")) == "pacman -S python-pip"
    assert get_new_command(Command("pacman -s python-pip")) == "pacman -S python-pip"
    assert get_new_command(Command("pacman -q python-pip")) == "pacman -Q python-pip"
    assert get_new_command(Command("pacman -r python-pip")) == "pacman -R python-pip"
    assert get_new_command(Command("pacman -f python-pip")) == "pacman -F python-pip"
    assert get_new_command(Command("pacman -d python-pip")) == "pacman -D python-pip"

# Generated at 2022-06-14 10:38:10.680998
# Unit test for function match
def test_match():
    assert match(Command("pacman -q", "error: invalid option '-q'"))
    assert match(Command("pacman -r", "error: invalid option '-r'"))
    assert not match(Command("pacman -r", "error: invalid option '--r'"))
    assert not match(Command("pacman -r", "error: invalid option '-R'"))


# Generated at 2022-06-14 10:38:12.846684
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -s python")) == "pacman -S python"
    assert get_new_command(Command("pacman -q python")) == "pacman -Q python"
    assert get_new_command(Command("pacman -r python")) == "pacman -R python"

# Generated at 2022-06-14 10:38:16.490748
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -S git")
    assert get_new_command("pacman -S --asdeps git")
    assert get_new_command("pacman -u git")
    assert get_new_command("pacman -q git")
    assert get_new_command("pacman -r git")
    assert get_new_command("pacman -t git")
    assert get_new_command("pacman -R git")

# Generated at 2022-06-14 10:38:21.369710
# Unit test for function match
def test_match():
    command = Command(
        script="pacman -s",
        output="error: invalid option '-s'\nSee 'pacman --help' for more help",
    )
    assert match(command)
    assert not match(Command(script="pacman -u", output=""))

# Generated at 2022-06-14 10:38:27.667475
# Unit test for function match
def test_match():
    assert match(Command('pacman -srqf 4ever'))


# Generated at 2022-06-14 10:38:40.784689
# Unit test for function match
def test_match():
    shell = Shell()
    assert match(Command("pacman -y -u -r -f", "", shell))
    assert match(Command("pacman -y -u -r -f", "error: invalid option '-y'", shell))
    assert match(Command("pacman -y -u -r -f", "error: invalid option '-u'", shell))
    assert match(Command("pacman -y -u -r -f", "error: invalid option '-r'", shell))
    assert match(Command("pacman -y -u -r -f", "error: invalid option '-f'", shell))
    assert not match(Command("pacman -s", "", shell))
    assert not match(Command("pacman -q", "", shell))
    assert not match(Command("pacman -l", "", shell))


# Generated at 2022-06-14 10:38:52.775463
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -Syu")) == "pacman -Syu"
    assert get_new_command(Command("pacman -Sf")) == "pacman -Sf"
    assert get_new_command(Command("pacman -Suf")) == "pacman -Suf"
    assert get_new_command(Command("pacman -Ssuf")) == "pacman -Ssuf"
    assert get_new_command(Command("pacman -Ssfu")) == "pacman -Ssfu"
    assert get_new_command(Command("pacman -q")) == "pacman -Q"
    assert get_new_command(Command("pacman -v")) == "pacman -V"
    assert get_new_command(Command("pacman -t")) == "pacman -T"
   

# Generated at 2022-06-14 10:38:59.181665
# Unit test for function match
def test_match():
    assert match(Command("pacman -q foo", "error: invalid option '-q'\n"))
    assert match(Command("pacman -m foo", "error: invalid option '-m'\n"))
    assert not match(Command("papman -q foo", "error: invalid option '-q'\n"))
    assert not match(Command("pacman -q foo",
                            "error: invalid option '-q'\nusage: pacman [-Ddft] [...]\n"))



# Generated at 2022-06-14 10:39:01.560805
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -r mirrorlist')) == 'pacman -R mirrorlist'

# Generated at 2022-06-14 10:39:04.112704
# Unit test for function match
def test_match():
    match_res = match("pacman -ssutil")
    assert match_res



# Generated at 2022-06-14 10:39:14.077271
# Unit test for function match
def test_match():
    assert match(Command("pacman -S foo", "/"))
    assert match(Command("pacman -Sfoo", "/"))
    assert match(Command("pacman -S foo", "/"))
    assert match(Command("pacman -Sfoo", "/"))
    assert match(Command("pacman -si foo", "/"))
    assert match(Command("pacman -sifoo", "/"))
    assert match(Command("pacman -q foo", "/"))
    assert match(Command("pacman -qfoo", "/"))
    assert match(Command("pacman -t foo", "/"))
    assert match(Command("pacman -tfoo", "/"))
    assert match(Command("pacman -u foo", "/"))
    assert match(Command("pacman -ufoo", "/"))
    assert match(Command("pacman -v foo", "/"))
    assert match

# Generated at 2022-06-14 10:39:27.519258
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -S', '')) == 'pacman -S'
    assert get_new_command(Command('pacman -d', '')) == 'pacman -D'
    assert get_new_command(Command('pacman -q', '')) == 'pacman -Q'
    assert get_new_command(Command('pacman -r', '')) == 'pacman -R'
    assert get_new_command(Command('pacman -s', '')) == 'pacman -S'
    assert get_new_command(Command('pacman -t', '')) == 'pacman -T'
    assert get_new_command(Command('pacman -u', '')) == 'pacman -U'
    assert get_new_command(Command('pacman -v', '')) == 'pacman -V'

# Generated at 2022-06-14 10:39:31.956609
# Unit test for function match
def test_match():
    assert match(Command("pacman -syu"))
    assert match(Command("pacman -S -y"))
    assert not match(Command("pacman -S -y"))

# Generated at 2022-06-14 10:39:39.375558
# Unit test for function match
def test_match():
    assert(match(Command("pacman -Su", "error: invalid option -- 'u'")))
    assert(not match(Command("pacman -Su", "error: invalid option -- 'S'")))
    assert(match(Command("pacman -Suq", "error: invalid option -- 'u'")))
    assert(not match(Command("pacman -Suu", "error: invalid option -- 'u'")))

# Generated at 2022-06-14 10:39:47.728596
# Unit test for function match
def test_match():
    assert match(Command("pacman -u", "error: invalid option '-u'"))
    assert match(Command("pacman -s", "error: invalid option '-s'"))
    assert match(Command("pacman -r", "error: invalid option '-r'"))
    assert match(Command("pacman -f", "error: invalid option '-f'"))
    assert match(Command("pacman -q", "error: invalid option '-q'"))
    assert match(Command("pacman -d", "error: invalid option '-d'"))
    assert match(Command("pacman -v", "error: invalid option '-v'"))
    assert match(Command("pacman -t", "error: invalid option '-t'"))
    assert not match(Command("pacman -i", "error: invalid option '-i'"))


# Generated at 2022-06-14 10:39:50.993554
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -fs")) == "pacman -Fs"



# Generated at 2022-06-14 10:39:53.290116
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("corrupted", "error: invalid option -t")) == "corrupted -T"

# Generated at 2022-06-14 10:40:00.525686
# Unit test for function match
def test_match():
    assert match(Command("pacman -U /tmp/pikaur-0.x86_64.pkg.tar.xz", ""))
    assert match(Command("pacman -s python", ""))
    assert match(Command("pacman -Uv /tmp/pikaur-0.x86_64.pkg.tar.xz", ""))
    assert not match(Command("pacman -U /tmp/pikaur-0.x86_64.pkg.tar.xz", "", ""))

# Generated at 2022-06-14 10:40:11.545458
# Unit test for function match
def test_match():
    assert not match(Command("pacman -u", ""))
    assert match(Command("pacman -a", ""))
    assert match(Command("pacman -aa", ""))
    assert match(Command("pacman -as", ""))
    assert match(Command("pacman -asd", ""))
    assert not match(Command("pacman -asdf", ""))
    assert not match(Command("pacman --noprogressbar", ""))
    assert not match(Command("pacman -asdft", ""))


# Generated at 2022-06-14 10:40:14.512660
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -u')) == 'pacman -U'

# Generated at 2022-06-14 10:40:26.943038
# Unit test for function match
def test_match():
    assert match(Command('pacman -s python', ''))
    assert match(Command('pacman -r python', ''))
    assert match(Command('pacman -q python', ''))
    assert match(Command('pacman -f python', ''))
    assert match(Command('pacman -d python', ''))
    assert match(Command('pacman -v python', ''))
    assert match(Command('pacman -t python', ''))
    assert match(Command('pacman -u python', ''))
    assert match(Command('pacman -s python -d python', ''))
    assert match(Command('pacman -s python -q python -t python', ''))
    assert match(Command('sudo pacman -s python', ''))
    assert match(Command('sudo pacman -r python', ''))

# Generated at 2022-06-14 10:40:31.875867
# Unit test for function get_new_command
def test_get_new_command():
    test_command = Command(script="pacman -q -q", settings={})
    result = get_new_command(test_command)
    assert result == "pacman -Q -Q"

# Generated at 2022-06-14 10:40:36.382052
# Unit test for function get_new_command
def test_get_new_command():
    script = "pacman -sync libpng"
    command = Command(script)
    assert get_new_command(command) == "pacman -Sy libpng"

# Generated at 2022-06-14 10:40:40.628865
# Unit test for function match
def test_match():
    assert match(Command("pacman -fsdf", ""))
    assert match(Command("pacman -q", ""))
    assert not match(Command("pacman -S dfg", ""))


# Generated at 2022-06-14 10:40:44.265578
# Unit test for function match
def test_match():
    assert match(Command("pacman -su", "error: invalid option '-s'\n"))
    assert not match(Command("pacman -su", "error: invalid option '-k'\n"))



# Generated at 2022-06-14 10:40:47.543849
# Unit test for function match
def test_match():
    stderr = "error: invalid option '-d'"
    command = Command(script='pacman -d', stderr=stderr)
    assert match(command)



# Generated at 2022-06-14 10:40:59.591459
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -S guake", "error: invalid option '-s'\n")) == "pacman -S guake"
    assert get_new_command(Command("yaourt -S guake", "error: invalid option '-s'\n")) == "yaourt -S guake"
    assert get_new_command(Command("pacman -s guake", "error: invalid option '-s'\n")) == "pacman -S guake"
    assert get_new_command(Command("yaourt -s guake", "error: invalid option '-s'\n")) == "yaourt -S guake"
    assert get_new_command(Command("pacman -d guake", "error: invalid option '-d'\n")) == "pacman -D guake"
    assert get_

# Generated at 2022-06-14 10:41:10.622082
# Unit test for function get_new_command
def test_get_new_command():
    actual = get_new_command(Command("pacman -r package"))
    assert actual == "pacman -R package"
    actual = get_new_command(Command("pacman -u package"))
    assert actual == "pacman -U package"
    actual = get_new_command(Command("pacman -s package"))
    assert actual == "pacman -S package"
    actual = get_new_command(Command("pacman -q package"))
    assert actual == "pacman -Q package"
    actual = get_new_command(Command("pacman -f package"))
    assert actual == "pacman -F package"
    actual = get_new_command(Command("pacman -v package"))
    assert actual == "pacman -V package"
    # command.script with multiple pacman commands
    actual = get_new_command

# Generated at 2022-06-14 10:41:13.909633
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -q") == "pacman -Q"
    assert get_new_command("pacman -r") == "pacman -R"

# Generated at 2022-06-14 10:41:19.286785
# Unit test for function match
def test_match():
	assert match(Command('pacman -Suqr', '', 'error: invalid option \'q\''))
	assert not match(Command('pacman -Suqr', '', 'error: invalid option \'q\''))
	assert not match(Command("pacman -Suqr", "", "error: invalid option \'q\'"))

# Generated at 2022-06-14 10:41:22.522760
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -Sdd asdf", "")) == "pacman -Sdd asdf"
    assert get_new_command(Command("pacman -Sy asdf", "")) == "pacman -Sy asdf"
    assert get_new_command(Command("pacman -Sq asdf", "")) == "pacman -Sq asdf"
    assert get_new_command(Command("pacman -Sr asdf", "")) == "pacman -Sr asdf"
    assert get_new_command(Command("pacman -Ss asdf", "")) == "pacman -Ss asdf"
    assert get_new_command(Command("pacman -St asdf", "")) == "pacman -St asdf"

# Generated at 2022-06-14 10:41:27.199262
# Unit test for function match
def test_match():
    assert match(Command("pacman -syu", "", "error: invalid option '-y'"))
    assert match(Command("pacman -s", "", "error: invalid option '-s'"))
    assert match(Command("pacman -y", "", "error: invalid option '-y'"))



# Generated at 2022-06-14 10:41:31.021954
# Unit test for function match
def test_match():
    assert match(Command('', '', ''))
    assert not match(Command('', '', '', stderr=''))

# Generated at 2022-06-14 10:41:46.947261
# Unit test for function match

# Generated at 2022-06-14 10:41:58.315346
# Unit test for function match
def test_match():
    assert match(Command("pacman -Y --query",
                         "error: invalid option '-Y'\nTry pacman --help for more information."))
    assert match(Command("pacman -r -r",
                         "error: invalid option '-r'\nTry pacman --help for more information."))
    assert not match(Command("pacman -S --noconfirm hello",
                             "resolving dependencies...\n\nlooking for conflicting packages...\n\nPackages (1) hello-2.8-10\n\nTotal Installed Size:  0,17 MiB\nNet Upgrade Size:       0,00 MiB\n:: Proceed with installation? [Y/n]  n"))

# Generated at 2022-06-14 10:42:03.940461
# Unit test for function match
def test_match():
    from thefuck import types
    from thefuck.types import Command

    assert match(Command('pacman -S foo bar', '\n'
            'error: invalid option \'S\'\n'
            'usage: pacman -[V] [options]\n'))
    assert not match(Command('pacman -S foo bar', '\n'
            'error: invalid option \'foo\'\n'
            'usage: pacman -[V] [options]\n'))

# Generated at 2022-06-14 10:42:06.789883
# Unit test for function match
def test_match():
    command = Command("sudo pacman -rsu", "error: invalid option '-r'")
    assert match(command) is True


# Generated at 2022-06-14 10:42:09.913234
# Unit test for function match
def test_match():
    assert match(Command('pacman -Sts linux', 'error: invalid option -s'))
    assert not match(Command('pacman -Syu', ''))



# Generated at 2022-06-14 10:42:19.802516
# Unit test for function match
def test_match():
    # First test
    first_command = "pacman -S pacman -d"
    assert match(Command(first_command,
                         "error: invalid option '-d'\nTry 'pacman --help' for more information.\n",
                         ""))
    # Second test
    second_command = "pacman -S pacman -q"
    assert match(Command(second_command,
                         "error: invalid option '-q'\nTry 'pacman --help' for more information.\n",
                         ""))
    # Tests with invalid commands
    invalid_commands = ["pacman -S -df",
                        "pacman -S pacman -p"]
    for invalid_command in invalid_commands:
        assert not match(Command(invalid_command, "", ""))


# Generated at 2022-06-14 10:42:23.654434
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -Suy',
        "error: invalid option '-S'\nSee 'man pacman' for help.\n"))


# Generated at 2022-06-14 10:42:32.215700
# Unit test for function match
def test_match():
    assert match(Command("pacman -Ss", ""))
    assert match(Command("pacman -Ssss", ""))
    assert match(Command("pacman -Ss python-pytest-cache", ""))
    assert match(Command("sudo pacman -Ss", ""))
    assert not match(Command("pacman -Syu", ""))
    assert match(Command("pacman -S --help", ""))
    assert match(Command("pacman -S --version", ""))
    assert not match(Command("pacman -Syu --version", ""))



# Generated at 2022-06-14 10:42:33.637998
# Unit test for function match
def test_match():
    assert match(Command('pacman -q -y'))
    assert ma

# Generated at 2022-06-14 10:42:38.607394
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('pacman -Rs gtk2') ==  'pacman -Rs gtk2'
    assert get_new_command('pacman -Rs gtk2 -g') == 'pacman -Rs gtk2 -G'

# Generated at 2022-06-14 10:42:50.105556
# Unit test for function match
def test_match():
    assert match(Command("pacman -z", "error: invalid option -- z"))
    assert match(Command("pacman -d", "error: invalid option -- d"))
    assert match(Command("pacman -q", "error: invalid option -- q"))
    assert match(Command("pacman -r", "error: invalid option -- r"))
    assert match(Command("pacman -s", "error: invalid option -- s"))
    assert match(Command("pacman -t", "error: invalid option -- t"))
    assert match(Command("pacman -u", "error: invalid option -- u"))
    assert match(Command("pacman -v", "error: invalid option -- v"))
    assert not match(Command("pacman -r", ""))
    assert not match(Command("pacman -s", "error"))



# Generated at 2022-06-14 10:42:53.578293
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command('pacman -s i3') == "pacman -S i3"
    assert get_new_command('pacman -q i3') == "pacman -Q i3"

# Generated at 2022-06-14 10:42:56.708064
# Unit test for function get_new_command
def test_get_new_command():
    command = Command('pacman -Syu', '')
    assert get_new_command(command) == 'pacman -SyU'

# Generated at 2022-06-14 10:43:00.673587
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -q linux", "error: invalid option '-q'")) == "pacman -Q linux"
    assert get_new_command(Command("pacman -F linux", "error: invalid option '-F'")) == "pacman -Ff linux"

# Generated at 2022-06-14 10:43:09.253995
# Unit test for function match
def test_match():
    assert match(Command("pacman -Sd xz-libs", "error: invalid option -d\n"))
    assert match(Command("pacman -Sf xz-libs", "error: invalid option -f\n"))
    assert match(Command("pacman -Squ xz-libs", "error: invalid option -u\n"))
    assert match(Command("pacman -Sqr xz-libs", "error: invalid option -r\n"))

# Generated at 2022-06-14 10:43:12.659388
# Unit test for function match
def test_match():
    assert not match(Command('pacman -S'))
    assert match(Command('pacman -g'))


# Generated at 2022-06-14 10:43:21.019310
# Unit test for function match
def test_match():
    assert match(Command("pacman -Rdd nsgp", ""))
    assert not match(Command("pacman -Rdd nsgp", "", ""))
    assert not match(Command("pacman -Rdd nsgp", "", "", "", "", ""))
    assert not match(Command("pacman -S nsgp", ""))
    assert not match(Command("pacman -S nsgp", "", ""))


# Generated at 2022-06-14 10:43:26.489394
# Unit test for function match
def test_match():
    assert match(Command("pacman -S", "error: invalid option '-S'\nTry pacman -Syu"))
    assert not match(Command("pacman -S", ""))

# Generated at 2022-06-14 10:43:31.184942
# Unit test for function match
def test_match():
    assert match(Command("pacman -q something", "error: invalid option '-q'"))
    assert not match(Command("pacman -q something", "error: invalid option '-s'"))
    assert not match(Command("pacman -s something", "error: invalid option '-s'"))



# Generated at 2022-06-14 10:43:43.509264
# Unit test for function match
def test_match():
    assert match(Command('pacman -Rn', 'error: invalid option -R'))
    assert match(Command('pacman -Rn', 'error: invalid option -R', debug_mode=True))
    assert not match(Command('pacman -Rn', 'error: invalid option -R', debug_mode=False))
    assert match(Command('pacman -u', 'error: invalid option -u'))
    assert match(Command('pacman -u', 'error: invalid option -u', debug_mode=True))
    assert not match(Command('pacman -u', 'error: invalid option -u', debug_mode=False))



# Generated at 2022-06-14 10:43:58.121688
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -e vim', 'error: invalid option -e\nSee \"pacman --help\" for available options.')) == 'pacman -E vim'
    assert get_new_command(Command('pacman -u vim', 'error: invalid option -u\nSee \"pacman --help\" for available options.')) == 'pacman -U vim'
    assert get_new_command(Command('pacman -S vim', 'error: invalid option -S\nSee \"pacman --help\" for available options.')) == 'pacman -Ss vim'
    assert get_new_command(Command('pacman -q vim', 'error: invalid option -q\nSee \"pacman --help\" for available options.')) == 'pacman -Q vim'

# Generated at 2022-06-14 10:44:06.091358
# Unit test for function match
def test_match():
    assert match(Command(script="sudo pacman -s 'archlinux'",
                         stderr="error: invalid option '-s'\nSee 'pacman --help'."))
    assert not match(Command(script="sudo pacman -s 'archlinux'",
                             stderr="error: invalid option '-s'\nSee 'pacman --help'."))
    assert match(Command(script="sudo pacman -s 'archlinux'",
                         stderr="error: invalid option '-s'\nSee 'pacman --help'.",
                         env={'SUDO_USER': 'peter'}))

# Generated at 2022-06-14 10:44:11.288983
# Unit test for function match
def test_match():
    assert match(Command(script="pacman -u uni"))
    assert match(Command(script="pacman -u uni", output="error: invalid option '-u'"))
    assert not match(Command(script="pacman -u uni", output="error: invalid option '-u'\nresolving dependencies..."))


# Generated at 2022-06-14 10:44:16.391142
# Unit test for function match
def test_match():
    assert match(Command('pacman -q', 'error: invalid option -q'))
    assert not match(Command('pacman -Q', 'error: invalid option -Q'))


# Generated at 2022-06-14 10:44:28.093260
# Unit test for function get_new_command
def test_get_new_command():
    from thefuck.rules.pacman_has_upgrade_option import get_new_command

    assert get_new_command(Command(script='pacman -S bash')) == 'pacman -S bash'
    assert get_new_command(Command(script='pacman -S bash',
                                   output='error: invalid option -- \'S\'\nTry `pacman --help\' for more information.')) == 'pacman -S bash'
    assert get_new_command(Command(script='pacman -f bash',
                                   output='error: invalid option -- \'f\'\nTry `pacman --help\' for more information.')) == 'pacman -F bash'

# Generated at 2022-06-14 10:44:32.575011
# Unit test for function match
def test_match():
    assert match(Command(script='pacman -qm', stderr='error: invalid option -- \'q\''))
    assert not match(Command(script='pacman -qm', stderr='error: invalid option -- \'q\''))


# Generated at 2022-06-14 10:44:38.917600
# Unit test for function match
def test_match():
    command = Command('pacman -ke', 'error: invalid option -k\nTry \'pacman --help\' for more information.')
    assert match(command)

    command = Command('pacman -q', 'error: invalid option -q\nTry \'pacman --help\' for more information.')
    assert match(command)

    command = Command('pacman -f', 'error: invalid option -f\nTry \'pacman --help\' for more information.')
    assert match(command)

    command = Command('pacman -d', 'error: invalid option -d\nTry \'pacman --help\' for more information.')
    assert match(command)

    command = Command('pacman -u', 'error: invalid option -u\nTry \'pacman --help\' for more information.')
    assert match(command)

    command = Command

# Generated at 2022-06-14 10:44:44.043100
# Unit test for function match
def test_match():
    output = "error: invalid option '-s'\nTry 'pacman --help' for more information.\n"
    assert not match(Command("pacman -s"))
    assert match(Command("pacman -s xxx", output))
    assert not match(Command("pacman -x xxx"))



# Generated at 2022-06-14 10:44:46.530441
# Unit test for function match
def test_match():
    assert match(Command("pacman -Qu", "error: invalid option '-Qu'"))


# Generated at 2022-06-14 10:45:05.270435
# Unit test for function match

# Generated at 2022-06-14 10:45:18.184876
# Unit test for function get_new_command
def test_get_new_command():
  assert get_new_command(Command('pacman -s firefox', 'error: invalid option -- \'s\'')) == 'pacman -S firefox'
  assert get_new_command(Command('pacman -R firefox', 'error: invalid option -- \'R\'')) == 'pacman -R firefox'
  assert get_new_command(Command('pacman -u firefox', 'error: invalid option -- \'u\'')) == 'pacman -U firefox'
  assert get_new_command(Command('pacman -f firefox', 'error: invalid option -- \'f\'')) == 'pacman -F firefox'
  assert get_new_command(Command('pacman -q firefox', 'error: invalid option -- \'q\'')) == 'pacman -Q firefox'

# Generated at 2022-06-14 10:45:26.345150
# Unit test for function match
def test_match():
    # test a command that should not match
    assert match(Command("pacman -Syy")) is None
    # test a command that should match
    assert match(Command("pacman -s pacman"))
    assert match(Command("pacman -f foo"))
    assert match(Command("pacman -r foo"))
    # test a command that should match, with a sudo prefix
    assert match(Command("sudo pacman -S foo"))


# Generated at 2022-06-14 10:45:29.705050
# Unit test for function match
def test_match():
    assert match(Command("pacman -s")).output == "error: invalid option '-s'"
    assert not match(Command("pacman -S"))


# Generated at 2022-06-14 10:45:38.195144
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -q')) == 'pacman -Q'
    assert get_new_command(Command('pacman -d -Q')) == 'pacman -D -Q'
    assert get_new_command(Command('pacman -srq')) == 'pacman -Srq'
    assert get_new_command(Command('pacman -ffd')) == 'pacman -Ffd'
    assert get_new_command(Command('pacman -vtu')) == 'pacman -Vtu'

# Generated at 2022-06-14 10:45:40.650815
# Unit test for function match
def test_match():
    assert match(
        Command("pacman -rs foo", "error: invalid option '-r'\n")
    )  # pacman is enabled by default



# Generated at 2022-06-14 10:45:49.761364
# Unit test for function match
def test_match():
    # Matching single character options should work
    assert match(Command('pacman -S foo', "error: invalid option '-S'"))
    assert match(Command('pacman -u foo', "error: invalid option '-u'"))
    assert match(Command('pacman -f foo', "error: invalid option '-f'"))
    assert match(Command('pacman -q foo', "error: invalid option '-q'"))
    assert match(Command('pacman -d foo', "error: invalid option '-d'"))
    assert match(Command('pacman -r foo', "error: invalid option '-r'"))
    assert match(Command('pacman -s foo', "error: invalid option '-s'"))
    assert match(Command('pacman -t foo', "error: invalid option '-t'"))

# Generated at 2022-06-14 10:45:51.520140
# Unit test for function match
def test_match():
    command_output = "error: invalid option '-q'"
    command = Command('sudo pacman -q', command_output)
    assert match(command)
