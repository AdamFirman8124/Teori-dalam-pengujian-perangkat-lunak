

# Generated at 2022-06-14 10:36:01.959023
# Unit test for function match
def test_match():
    assert match(Command("pacman -Suy", "error: invalid option '-y'"))

    assert match(Command("pacman -Sy", "error: invalid option '-y'"))

    assert match(Command("pacman -Suy", "error: invalid option '-S'"))

    assert not match(Command("pacman -Sy", "error: invalid option '-S'"))


# Generated at 2022-06-14 10:36:13.388242
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command("pacman -S bash", "error: invalid option '-S'")
    ) == "pacman -S bash"
    assert get_new_command(
        Command("pacman -s bash", "error: invalid option '-s'")
    ) == "pacman -S bash"
    assert get_new_command(
        Command("pacman -u bash", "error: invalid option '-u'")
    ) == "pacman -U bash"
    assert get_new_command(
        Command("pacman -r bash", "error: invalid option '-r'")
    ) == "pacman -R bash"
    assert get_new_command(
        Command("pacman -f bash", "error: invalid option '-f'")
    ) == "pacman -F bash"

# Generated at 2022-06-14 10:36:21.136596
# Unit test for function match
def test_match():
    assert match(Command('pacman -s git', '', 'error: invalid option -s'))
    assert match(Command('pacman -f git', '', 'error: invalid option -f'))
    assert match(Command('pacman -t git', '', 'error: invalid option -t'))
    assert not match(
        Command('pamac -s git', '', 'error: invalid option -s')
    )


# Generated at 2022-06-14 10:36:23.297315
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -u") == "pacman -U"



# Generated at 2022-06-14 10:36:34.072204
# Unit test for function match
def test_match():
    app = "pacman"
    command = Command("pacman -r package", "error: invalid option '-r'")
    assert match(command, app)

    command = Command("pacman -f package", "error: invalid option '-f'")
    assert match(command, app)

    command = Command("pacman -q package", "error: invalid option '-q'")
    assert match(command, app)

    command = Command("pacman -d package", "error: invalid option '-d'")
    assert match(command, app)

    command = Command("pacman -s package", "error: invalid option '-s'")
    assert match(command, app)

    command = Command("pacman -u package", "error: invalid option '-u'")
    assert match(command, app)


# Generated at 2022-06-14 10:36:39.978482
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -dt', 'error: invalid option -- "d"\n'))
    assert not match(Command('sudo pacman -dt', 'error: invalid option -- "z"\n'))
    assert match(Command('sudo pacman -U', 'error: invalid option -- "U"\n'))



# Generated at 2022-06-14 10:36:49.987609
# Unit test for function match
def test_match():
    assert match(Command("pacman --sync emacs", "error: invalid option '--sync'\n"))
    assert match(Command("pacman --update emacs", "error: invalid option '--update'\n"))
    assert not match(Command("pacman --sync emacs", "error: invalid option '--synch'\n"))
    assert not match(Command("pacman -s emacs", "error: invalid option '-s'\n"))
    assert not match(Command("pacman -S emacs", "error: invalid option '-S'\n"))
    assert not match(Command("pacman --sync emacs", ""))
    assert not match(Command("pacman -S emacs", ""))

# Generated at 2022-06-14 10:36:53.620829
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command(script="pacman -s", output="")) == "pacman -S"

# Generated at 2022-06-14 10:37:05.012821
# Unit test for function match
def test_match():
    assert match(Command("pacman -s", "error: invalid option '-s'"))
    assert match(Command("pacman -U", "error: invalid option '-U'"))
    assert match(Command("pacman -q", "error: invalid option '-q'"))
    assert match(Command("pacman -r", "error: invalid option '-r'"))
    assert match(Command("pacman -f", "error: invalid option '-f'"))
    assert match(Command("pacman -d", "error: invalid option '-d'"))
    assert match(Command("pacman -t", "error: invalid option '-t'"))
    assert match(Command("pacman -v", "error: invalid option '-v'"))
    assert not match(Command("pacman -S", "error: invalid option '-S'"))


# Generated at 2022-06-14 10:37:08.450934
# Unit test for function get_new_command
def test_get_new_command():
    new_command = get_new_command(Command("pacman -q"))
    assert new_command == "pacman -Q"

# Generated at 2022-06-14 10:37:15.018853
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -s emacs") == "pacman -S emacs"
    assert get_new_command("pacman -f emacs") == "pacman -F emacs"
    assert get_new_command("pacman -u emacs") == "pacman -U emacs"

# Generated at 2022-06-14 10:37:22.892334
# Unit test for function match
def test_match():
    assert match(Command('pacman -q -r testapp', 'error: invalid option -- \'r\''))
    assert match(Command('pacman -q -r testapp', 'error: invalid option -- \'rm\''))
    assert match(Command('pacman -q -r testapp', 'error: invalid option -- \'r\'\nsyntax: pacman -[rqvt] <package(s)>'))
    assert not match(Command('pacman -q -r testapp', 'error: \'testapp\' is not a valid package name'))
    assert not match(Command('pacman -h', 'pacman -h'))
    assert not match(Command('pacman -h', 'pacman -h\nsyntax: pacman -[rqvt] <package(s)>'))

# Generated at 2022-06-14 10:37:35.736616
# Unit test for function match
def test_match():
    assert match(
        Command(
            "pacman -S python-pip", "error: invalid option '-S'\n")
        )
    assert match(
        Command(
            "pacman -q python-pip", "error: invalid option '-q'\n")
        )
    assert match(
        Command(
            "pacman -f python-pip", "error: invalid option '-f'\n")
        )
    assert match(
        Command(
            "pacman -r python-pip", "error: invalid option '-r'\n")
        )
    assert match(
        Command(
            "pacman -u python-pip", "error: invalid option '-u'\n")
        )

# Generated at 2022-06-14 10:37:48.134595
# Unit test for function match
def test_match():
    # Test commands that do not match
    assert not match(
        Command("pacman -Sw vim", "warning: vim-8.0.0531-1 is up to date -- skipping\n", "")
    )
    # Test commands that match
    assert match(
        Command("pacman -s gvim", "error: invalid option -s\n", "")
    )
    assert match(
        Command("pacman -q QT", "error: invalid option -q\n", "")
    )
    assert match(
        Command("pacman -rf foo", "error: invalid option -r\n", "")
    )
    assert match(
        Command("pacman -t bar", "error: invalid option -t\n", "")
    )

# Generated at 2022-06-14 10:37:52.891392
# Unit test for function match
def test_match():
    assert not match(Command('pacman -q', ''))
    assert match(
        Command('pacman -q --print-format \'bla  bla bla\n\'', 'error: invalid option \'--print-format\'\nType \'pacman --help\' or \'man pacman\' for help.\n')
    )



# Generated at 2022-06-14 10:38:00.378058
# Unit test for function match
def test_match():
    assert match(Command('pacman -dfqr', 'error: invalid option -f'))
    assert match(Command('pacman -h', ''))
    assert not match(Command('pacman --help', ''))

# Generated at 2022-06-14 10:38:02.448271
# Unit test for function match
def test_match():
    assert match(Command("pacman --h", "", "\n"))
    
    

# Generated at 2022-06-14 10:38:07.573296
# Unit test for function match
def test_match():
    assert match(Command("pacman -r", "error: invalid option '-r'."))
    assert not match(Command("pacman -qe", "error: invalid option '-q'."))


# Generated at 2022-06-14 10:38:12.283379
# Unit test for function match
def test_match():
    assert match(Command("pacman -Su", "error: invalid option '-s'"))
    assert match(Command("pacman -q", "error: invalid option '-q'"))
    assert match(Command("pacman -U", "error: invalid option '-U'"))

# Generated at 2022-06-14 10:38:23.058645
# Unit test for function match
def test_match():
    assert match(Command(script="pacman -u -Syy"))
    assert match(Command(script="pacman -q -Syy"))
    assert match(Command(script="pacman -f -Syy"))
    assert match(Command(script="pacman -r -Syy"))
    assert match(Command(script="pacman -v -Syy"))
    assert match(Command(script="pacman -s -Syy"))
    assert match(Command(script="pacman -t -Syy"))
    assert match(Command(script="pacman -d -Syy"))
    assert match(Command(script="pacman -y -Syy"))



# Generated at 2022-06-14 10:38:31.009858
# Unit test for function get_new_command
def test_get_new_command():
    script = "sudo pacman -Sy --noconfirm qt5"
    command = Command(script, "error: invalid option '-S'")
    assert get_new_command(command) == "sudo pacman -Sy --noconfirm Qt5"

# Generated at 2022-06-14 10:38:33.728770
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -r package") == "pacman -R package"

# Generated at 2022-06-14 10:38:41.682040
# Unit test for function match
def test_match():
    from thefuck.rules.pacman_wrong_option import match

    assert match(command='', output='error: invalid option "-q"')
    assert match(command='', output='error: invalid option "--q"')
    assert match(command='', output='error: invalid option "-r"')
    assert match(command='', output='error: invalid option "--r"')
    assert match(command='', output='error: invalid option "-s"')
    assert match(command='', output='error: invalid option "--s"')
    assert match(command='', output='error: invalid option "-u"')
    assert match(command='', output='error: invalid option "--u"')
    assert match(command='', output='error: invalid option "--v"')

    assert not match(command='', output='')

# Generated at 2022-06-14 10:38:54.146376
# Unit test for function match
def test_match():
    assert match(Command('pacman -Syu'))
    assert match(Command('pacman -Suu'))
    assert match(Command('pacman -Su'))
    assert match(Command('pacman -S'))
    assert match(Command('pacman -Ss'))
    assert match(Command('pacman -Sv'))
    assert match(Command('pacman -Sq'))
    assert match(Command('pacman -Sf'))
    assert match(Command('pacman -Sd'))
    assert match(Command('pacman -Sv'))
    assert match(Command('pacman -Sv'))
    assert match(Command('sudo pacman -S'))
    assert not match(Command('pacman -Syyu'))
    assert not match(Command('pacman -Suuu'))

# Generated at 2022-06-14 10:38:59.152389
# Unit test for function match
def test_match():
    assert match(Command(script="sudo pacman -S yay", output="error: invalid option '-S'"))
    assert not match(Command(script="sudo pacman -S yay", output="error: invalid option '-s'"))
    assert not match(Command(script="sudo pacman", output="error"))
    assert not match(Command(script="ls", output="error"))


# Generated at 2022-06-14 10:39:11.763181
# Unit test for function match
def test_match():
    assert match(Command("sudo pacman -f -Ss xorg-server", ""))
    assert match(Command("pacman -f -Ss xorg-server", ""))
    assert match(Command("pacman -q -Ss xorg-server", ""))
    assert not match(Command("pacman -Ss xorg-server", ""))
    assert not match(Command("pacman -i", ""))
    assert not match(Command("apt install", ""))
    assert not match(Command("apt-get install", ""))
    assert not match(Command("aptitude install", ""))
    assert not match(Command("pacman -i xorg-server", ""))
    assert not match(Command("apt install xorg-server", ""))
    assert not match(Command("apt-get install xorg-server", ""))

# Generated at 2022-06-14 10:39:19.180254
# Unit test for function get_new_command
def test_get_new_command():
    script = "pacman -Rdd gdb"
    command = Mock(script=script, output="error: invalid option '-d'")
    assert get_new_command(command) == script.replace("-d", "-D")
    script = "pacman -U /home/packages/package.pkg.tar.xz"
    command = Mock(script=script, output="error: invalid option '-U'")
    assert get_new_command(command) == script.replace("-U", "-u")

# Generated at 2022-06-14 10:39:29.635337
# Unit test for function match
def test_match():
    assert match(Command("pacman -q", "error: invalid option '-q'\n"))
    assert match(Command("pacman -q", "error: invalid option '-q'\n"))
    assert match(Command("sudo pacman -q", "error: invalid option '-q'\n"))
    assert not match(Command("pacman -q", "error: invalid option '--q'\n"))
    assert not match(Command("pacman -q", "error: invalid option '-qq'\n"))
    assert not match(Command("pacman -q", ""))
    assert not match(Command("pacman -q", "Failed"))
    assert not match(Command("pacman -q", "error: invalid option '-'\n"))


# Generated at 2022-06-14 10:39:33.547451
# Unit test for function get_new_command

# Generated at 2022-06-14 10:39:45.458102
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -S base")) == "pacman -S base"
    assert get_new_command(Command("pacman -s base")) == "pacman -S base"
    assert get_new_command(Command("pacman -q base")) == "pacman -Q base"
    assert get_new_command(Command("pacman -r base")) == "pacman -R base"
    assert get_new_command(Command("pacman -f base")) == "pacman -F base"
    assert get_new_command(Command("pacman -d base")) == "pacman -D base"
    assert get_new_command(Command("pacman -v base")) == "pacman -V base"
    assert get_new_command(Command("pacman -t base")) == "pacman -T base"

# Generated at 2022-06-14 10:39:52.780468
# Unit test for function get_new_command

# Generated at 2022-06-14 10:40:02.480421
# Unit test for function match
def test_match():
    command = Command("pacman -u", "error: invalid option 'u'\n"
                                   "See pacman --help for more help\n")
    assert match(command)
    command = Command("pacman -s", "error: invalid option 's'\n"
                                   "See pacman --help for more help\n")
    assert match(command)
    command = Command("pacman -r", "error: invalid option 'r'\n"
                                   "See pacman --help for more help\n")
    assert match(command)
    command = Command("pacman -f", "error: invalid option 'f'\n"
                                   "See pacman --help for more help\n")
    assert match(command)

# Generated at 2022-06-14 10:40:05.034256
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -h", "")) == "pacman -H"

# Generated at 2022-06-14 10:40:15.485504
# Unit test for function match
def test_match():
    assert match(Command("pacman -q", "error: invalid option '-q'\n"))
    assert match(Command("pacman -s", "error: invalid option '-s'\n"))
    assert match(Command("pacman -a", "error: invalid option '-a'\n"))
    assert match(Command("pacman -z", "error: invalid option '-z'\n"))
    assert match(Command("pacman -d", "error: invalid option '-d'\n"))
    assert match(Command("pacman -f", "error: invalid option '-f'\n"))
    assert match(Command("pacman -v", "error: invalid option '-v'\n"))
    assert match(Command("pacman -r", "error: invalid option '-r'\n"))

# Generated at 2022-06-14 10:40:27.784964
# Unit test for function match
def test_match():
    """
    Test some pacman command matching
    """

# Generated at 2022-06-14 10:40:39.367255
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(
        Command("pacman -h", "error: invalid option '-h'\nERROR: See 'pacman --help' for more help.", "")
    ) == 'pacman -H'
    assert get_new_command(
        Command("pacman -s", "error: invalid option '-s'\nERROR: See 'pacman --help' for more help.", "")
    ) == 'pacman -S'
    assert get_new_command(
        Command("pacman -q", "error: invalid option '-q'\nERROR: See 'pacman --help' for more help.", "")
    ) == 'pacman -Q'

# Generated at 2022-06-14 10:40:42.134708
# Unit test for function match
def test_match():
    assert match(Command("pacman -S"))
    assert not match(Command("pacman -Ss"))
    assert not match(Command("pacman -S"))



# Generated at 2022-06-14 10:40:47.338323
# Unit test for function match
def test_match():
    assert match(Command("pacman -Qu"))
    assert match(Command("pacman -xu"))
    assert match(Command("pacman -rsu"))
    assert not match(Command("pacman -Qu"))
    assert not match(Command("pacman -xu"))
    assert not match(Command("pacman -rsu"))


# Generated at 2022-06-14 10:40:52.297058
# Unit test for function get_new_command
def test_get_new_command():
    command = "pacman -q"
    assert get_new_command(command) == "pacman -Q"
    command = "pacman -q --dbonly"
    assert get_new_command(command) == "pacman -Q --dbonly"

# Generated at 2022-06-14 10:40:55.002423
# Unit test for function match
def test_match():
    assert match(Command("pacman -u", "error: invalid option '-u'"))
    assert not match(Command("pacman -u", ""))

# Generated at 2022-06-14 10:41:10.931578
# Unit test for function match
def test_match():
    assert match(Command("pacman -q ddd", "error: invalid option '-q'"))
    assert match(Command("pacman -f ddd", "error: invalid option '-f'"))
    assert match(Command("pacman -r ddd", "error: invalid option '-r'"))
    assert match(Command("pacman -s ddd", "error: invalid option '-s'"))
    assert match(Command("pacman -u ddd", "error: invalid option '-u'"))
    assert match(Command("pacman -v ddd", "error: invalid option '-v'"))
    assert not match(Command("pacman -d ddd", "error: invalid option '-d'"))
    assert not match(Command("pacman -t ddd", "error: invalid option '-t'"))

# Generated at 2022-06-14 10:41:14.457368
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -Syu', 'error: invalid option -- \'y\''))
    assert not match(Command('sudo pacman -Syu', 'error: invalid option -- \'g\''))

# Generated at 2022-06-14 10:41:17.327124
# Unit test for function match
def test_match():
    assert match(Command("sudo pacman -Syu", "sudo: invalid option -- 'u'\nTry 'sudo --help' for more information.\n"))

# Generated at 2022-06-14 10:41:19.340817
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -S git") == "pacman -Ss git"

# Generated at 2022-06-14 10:41:29.407527
# Unit test for function match
def test_match():
    assert match(Command("pacman -s ls", "error: invalid option '-s' : use -S instead."))
    assert match(Command("pacman -q ls", "error: invalid option '-q' : use -Q instead."))
    assert match(Command("pacman -d ls", "error: invalid option '-d' : use -D instead."))
    assert match(Command("pacman -r ls", "error: invalid option '-r' : use -R instead."))
    assert match(Command("pacman -f ls", "error: invalid option '-f' : use -F instead."))
    assert match(Command("pacman -u ls", "error: invalid option '-u' : use -U instead."))

# Generated at 2022-06-14 10:41:33.942919
# Unit test for function match
def test_match():
    assert match(Command('pacman -x', ''))
    assert match(Command('pacman -Qa', ''))
    assert not match(Command('pacman -Q', ''))
    assert not match(Command('pacman -s', ''))


# Generated at 2022-06-14 10:41:38.520580
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -s first second third', '')) == 'pacman -S first second third'

# Generated at 2022-06-14 10:41:48.273052
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -u", "pacman: error: unknown option -- u")) == "pacman -U"
    assert get_new_command(Command("pacman -S packman", "pacman: error: unknown option -- s")) == "pacman -S packman"
    assert get_new_command(Command("pacman -S flag", "pacman: error: unknown option -- s")) == "pacman -S flag"
    assert get_new_command(Command("pacman -S flag", "pacman: error: unknown option -- s")) == "pacman -S flag"
    assert get_new_command(Command("pacman -f", "pacman: error: unknown option -- f")) == "pacman -F"

# Generated at 2022-06-14 10:41:52.216067
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('sudo pacman -Su')) == 'sudo pacman -SU'
    assert get_new_command(Command('sudo pacman -d')) == 'sudo pacman -D'

# Generated at 2022-06-14 10:41:55.247837
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -q -t")) == "pacman -Qt"

# Generated at 2022-06-14 10:42:14.069693
# Unit test for function match
def test_match():
    assert match(Command('pac -q', 'error: invalid option -q\n'))
    assert match(Command('pac -s', 'error: invalid option -s\n'))
    assert match(Command('pac -u', 'error: invalid option -u\n'))
    assert match(Command('pac -v', 'error: invalid option -v\n'))
    assert match(Command('pac -t', 'error: invalid option -t\n'))
    assert match(Command('pac -d', 'error: invalid option -d\n'))
    assert match(Command('pac -f', 'error: invalid option -f\n'))
    assert match(Command('pac -r', 'error: invalid option -r\n'))
    assert not match(Command('pac -q', 'error: invalid option -x\n'))


# Generated at 2022-06-14 10:42:22.613455
# Unit test for function match
def test_match():
    assert match(Command('pacman -R foo'))
    assert match(Command('pacman -R foo', 'error: invalid option \'-R\''))
    assert match(Command('pacman -s foo'))
    assert match(Command('pacman -s foo', 'error: invalid option \'-s\''))
    assert not match(Command('pacman -s foo', 'error: invalid option \'-s\''))
    assert not match(Command('pacman s foo', 'error: invalid option \'-s\''))
    assert not match(Command('pacman -s', 'error: invalid option \'-s\''))
    assert not match(Command('pacman s', 'error: invalid option \'-s\''))


# Generated at 2022-06-14 10:42:33.416829
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command('pacman -Ss man', '')) == 'pacman -SS man'
    assert get_new_command(Command('pacman -Qs man', '')) == 'pacman -QS man'
    assert get_new_command(Command('pacman -Rs man', '')) == 'pacman -RS man'
    assert get_new_command(Command('pacman -Qd man', '')) == 'pacman -QD man'
    assert get_new_command(Command('pacman -Qu man', '')) == 'pacman -QU man'
    assert get_new_command(Command('pacman -Qt man', '')) == 'pacman -QT man'
    assert get_new_command(Command('pacman -Qr man', '')) == 'pacman -QR man'

# Generated at 2022-06-14 10:42:40.889484
# Unit test for function match
def test_match():
    assert match(Command('sudo pacman -Suy', 'error: invalid option -S'))
    assert match(Command('sudo pacman -qtdi', "error: invalid option '-q'"))
    assert not match(Command('sudo pacman -qtdi', 'error: an unknown option was passed'))
    assert not match(Command('sudo pacman -qtdi', 'error: package not found'))
    assert not match(Command('sudo pacman -qtdi', 'error: something wrong'))



# Generated at 2022-06-14 10:42:43.429175
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script='pacman -Su', stdout="error: invalid option '-S'")
    result = get_new_command(command)
    assert result == 'pacman -Su'



# Generated at 2022-06-14 10:42:49.020478
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("pacman -S git", "error: invalid option -- 'S'")
    assert get_new_command(command) == "pacman -S git"
    command = Command("pacman -qS git", "error: invalid option -- 'q'")
    assert get_new_command(command) == "pacman -Qs git"

# Generated at 2022-06-14 10:42:50.559755
# Unit test for function match
def test_match():
    assert match(Command("pacman -f"))


# Generated at 2022-06-14 10:43:01.709516
# Unit test for function match
def test_match():
    assert match(Command("pacman -S package", "", ""))
    assert match(Command("pacman -Sv package", "", ""))
    assert match(Command("pacman -Sf package", "", ""))
    assert match(Command("pacman -Sq package", "", ""))
    assert match(Command("pacman -Su package", "", ""))
    assert match(Command("pacman -Sd package", "", ""))
    assert match(Command("pacman -Sdv package", "", ""))
    assert match(Command("sudo pacman -Sdv package", "", ""))
    assert not match(Command("pacman -i package", "", ""))
    assert not match(Command("pacman -Sy package", "", ""))
    assert not match(Command("pacman -R package", "", ""))


# Generated at 2022-06-14 10:43:11.402811
# Unit test for function match
def test_match():
    # Test 1
    # Input
    command = Command("pacman -s xxx", "error: invalid option '-s'")
    # Expected output
    assert match(command) == True
    # Test 2
    # Input
    command = Command("pacman -u -s xxx", "error: invalid option '-s'")
    # Expected output
    assert match(command) == True
    # Test 3
    # Input
    command = Command("pacman -s xxx", "error: invalid option '-r'")
    # Expected output
    assert match(command) == False


# Generated at 2022-06-14 10:43:17.484886
# Unit test for function match
def test_match():
    assert match(Command('pacman -Qs "somename"', "error: invalid option '-Q\nTry pacman -Ss instead."))
    assert not match(Command('pacman -Ss', "error: invalid option '-S\nTry pacman -Ss instead."))


# Generated at 2022-06-14 10:43:27.352337
# Unit test for function match
def test_match():
    assert match(Command("pacman -uq -q"))
    assert not match(Command("pacman -uq"))


# Generated at 2022-06-14 10:43:38.911016
# Unit test for function match
def test_match():
    assert match(Command('pacman -S command', "error: invalid option '-S'\n"))
    assert match(Command('pacman -u command', "error: invalid option '-u'\n"))
    assert match(Command('pacman -v command', "error: invalid option '-v'\n"))
    assert match(Command('pacman -r command', "error: invalid option '-r'\n"))
    assert match(Command('pacman -q command', "error: invalid option '-q'\n"))
    assert match(Command('pacman -d command', "error: invalid option '-d'\n"))
    assert match(Command('pacman -f command', "error: invalid option '-f'\n"))
    assert match(Command('pacman -t command', "error: invalid option '-t'\n"))

# Generated at 2022-06-14 10:43:42.677709
# Unit test for function match
def test_match():
    command = Command('pacman -u', 'error: invalid option ')
    assert match(command) is True

    command = Command('pacman -random', 'error: invalid option ')
    assert match(command) is False



# Generated at 2022-06-14 10:43:54.254337
# Unit test for function match
def test_match():
    assert match(
        Command(
            "pacman -Qqtt",
            "error: invalid option '-'",
            "",
            "",
            "",
            "",
            "",
            "",
        )
    )

    assert not match(
        Command(
            "pacman -Qqtt",
            "error: invalid option '-'",
            "",
            "",
            "",
            "",
            "",
            "",
        )
    )



# Generated at 2022-06-14 10:43:56.520590
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -s", "")) == "pacman -S"



# Generated at 2022-06-14 10:43:59.634418
# Unit test for function get_new_command
def test_get_new_command():
    command = Command(script="pacman -q pacman")
    assert get_new_command(command) == 'pacman -Q pacman'

# Generated at 2022-06-14 10:44:02.173333
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("sudo pacman -v -S nmap")) == "sudo pacman -V -S nmap"

# Generated at 2022-06-14 10:44:04.495693
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command("pacman -q foo") == "pacman -Q foo", "{}"

# Generated at 2022-06-14 10:44:07.594788
# Unit test for function match
def test_match():
    assert match(Command('pacman -a', '', 'error: invalid option \'-a\''))
    assert not match(Command('pacman -a', '', ''))


# Generated at 2022-06-14 10:44:17.391832
# Unit test for function match

# Generated at 2022-06-14 10:44:35.293134
# Unit test for function match
def test_match():
    assert match(Command('pacman -qfo foo',
                         'error: invalid option -q\nsee pacman(8) man page for available options'))
    assert match(Command('pacman -v',
                         'error: invalid option -v\nsee pacman(8) man page for available options.'))
    assert match(Command('pacman -zx',
                         'error: invalid option -z\nsee pacman(8) man page for available options'))
    assert match(Command('pacman -S -S -S --noconfirm',
                         'error: invalid option -S\nsee pacman(8) man page for available options'))
    assert not match(Command('pacman -Suy',
                             'error: invalid option -S\nsee pacman(8) man page for available options'))

# Generated at 2022-06-14 10:44:39.971382
# Unit test for function match
def test_match():
    assert match(Command('pacman -u', 'error: invalid option -u'))
    assert match(Command('pacman -r', 'error: invalid option -r'))
    assert not match(Command('pacman -u', 'error: invalid option -m'))


# Generated at 2022-06-14 10:44:51.143037
# Unit test for function match
def test_match():
    assert match(Command('pacman -q', None, "error: invalid option '-q'"))
    assert match(Command('pacman -u', None, "error: invalid option '-u'"))
    assert match(Command('pacman -r', None, "error: invalid option '-r'"))
    assert match(Command('pacman -s', None, "error: invalid option '-s'"))
    assert match(Command('pacman -f', None, "error: invalid option '-f'"))
    assert match(Command('pacman -d', None, "error: invalid option '-d'"))
    assert match(Command('pacman -v', None, "error: invalid option '-v'"))
    assert match(Command('pacman -t', None, "error: invalid option '-t'"))

# Generated at 2022-06-14 10:44:56.385438
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -s s", "", "")) == "pacman -S s"
    assert get_new_command(Command("pacman -f s", "", "")) == "pacman -F s"

# Generated at 2022-06-14 10:45:00.972136
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -S", "error: invalid option '-S'")) == "pacman -S"
    assert get_new_command(Command("pacman -u", "error: invalid option '-u'")) == "pacman -U"

# Generated at 2022-06-14 10:45:10.161134
# Unit test for function match
def test_match():
    assert match(Command("pacman -S --needed base-devel", "", "", 1, ""))
    assert not match(Command("pacman -S base-devel", "", "", 1, ""))
    assert match(Command("pacman -Syu", "", "", 1, ""))
    assert match(Command("pacman -Syuu", "", "", 1, ""))
    assert match(Command("pacman -Syu", "", "", 1, ""))
    assert match(Command("pacman -Syuu", "", "", 1, ""))
    assert match(Command("pacman -Syy", "", "", 1, ""))
    assert match(Command("pacman -S --needed base-devel", "", "", 1, ""))

# Generated at 2022-06-14 10:45:21.266578
# Unit test for function match
def test_match():
    assert match(Command("pacman -S xz", "error: invalid option '-S'"))
    assert match(Command("pacman -s xz", "error: invalid option '-s'"))
    assert match(Command("pacman -u xz", "error: invalid option '-u'"))
    assert match(Command("pacman -q xz", "error: invalid option '-q'"))
    assert match(Command("pacman -f xz", "error: invalid option '-f'"))
    assert match(Command("pacman -q xz", "error: invalid option '-q'"))
    assert match(Command("pacman -d xz", "error: invalid option '-d'"))
    assert match(Command("pacman -v xz", "error: invalid option '-v'"))

# Generated at 2022-06-14 10:45:25.357099
# Unit test for function get_new_command
def test_get_new_command():
    assert get_new_command(Command("pacman -u vim")) == "pacman -U vim"
    assert get_new_command(Command("pacman -qe vim")) == "pacman -Qe vim"

# Generated at 2022-06-14 10:45:37.101996
# Unit test for function match
def test_match():
    command = Command(script='pacman -U vim-8.0.1295-1-x86_64.pkg.tar.xz', output="error: invalid option '-U'")
    assert match(command)
    command = Command(script='pacman -f vim-8.0.1295-1-x86_64.pkg.tar.xz', output="error: invalid option '-f'")
    assert match(command)
    command = Command(script='pacman -Syu vim-8.0.1295-1-x86_64.pkg.tar.xz', output="error: invalid option '-Syu'")
    assert not match(command)

# Generated at 2022-06-14 10:45:42.707395
# Unit test for function get_new_command
def test_get_new_command():
    command = Command("pacman -su", "error: invalid option -- 's'")
    assert get_new_command(command) == "pacman -Su"

    command = Command("pacman -q", "error: invalid option -- 'q'")
    assert get_new_command(command) == "pacman -Q"