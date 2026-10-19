

# Generated at 2022-06-14 01:21:59.242365
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:22:03.936078
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:22:05.980105
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:08.386755
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:12.513461
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == args.debug
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:22:17.072442
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:18.973081
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(Namespace(debug=True))
    assert settings.debug == True



# Generated at 2022-06-14 01:22:20.104658
# Unit test for function init_settings
def test_init_settings():
    input = Namespace()
    init_settings(input)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:24.878550
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:22:26.798229
# Unit test for function init_settings
def test_init_settings():
    settings.__init__()
    init_settings(Namespace(debug = True))
    assert settings.debug == True

# Generated at 2022-06-14 01:22:32.763038
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace())
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:22:34.860115
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True


"""
Start the game.
"""

# Generated at 2022-06-14 01:22:37.503810
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settin

# Generated at 2022-06-14 01:22:41.251682
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    init_settings(Namespace(debug=True))
    assert settings.debug is True
    init_settings(Namespace(debug=False))
    assert settings.debug is False

# Generated at 2022-06-14 01:22:43.391732
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    


# Generated at 2022-06-14 01:22:46.939030
# Unit test for function init_settings
def test_init_settings():
    args = _create_args(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:22:50.410583
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:55.978061
# Unit test for function init_settings
def test_init_settings():
    ar = Namespace()
    ar.debug = True
    init_settings(ar)
    assert settings.debug == True

if __name__ == "__main__":
    pass

# Generated at 2022-06-14 01:22:58.648467
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:23:03.086707
# Unit test for function init_settings
def test_init_settings():
  parser = init_parser()
  args = parser.parse_args('--debug'.split())

  init_settings(args)
  assert settings.debug == True



# Generated at 2022-06-14 01:23:08.925149
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False, help="Debug flag")
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:11.774938
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:14.278726
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:15.592348
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:18.344210
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:20.606749
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:21.892518
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:23:27.269296
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug == args.debug, "init_settings() \
            when called with valid arguments \
            should set settings.debug to args.debug"

# Generated at 2022-06-14 01:23:30.997725
# Unit test for function init_settings
def test_init_settings():
    class FakeArgs(Namespace):
        def __init__(self):
            self.debug = True
            self.verbose = True

    args = FakeArgs()
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:23:34.572528
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:41.670627
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True


# Generated at 2022-06-14 01:23:46.189431
# Unit test for function init_settings
def test_init_settings():
    settings = Settings()
    args = Namespace()
    
    init_settings(args)
    
    assert settings.debug is False
    
    args.debug = True
    init_settings(args)
    assert settings.debug is True

    del settings

# Generated at 2022-06-14 01:23:47.703166
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:52.051977
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, events=['file://test/sample_event.json'])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:58.019683
# Unit test for function init_settings
def test_init_settings():
    from unittest.mock import patch
    with patch('argparse.Namespace') as mock_args:
        mock_args.debug = False
        init_settings(mock_args)
        assert settings.debug == False
        mock_args.debug = True
        init_set

# Generated at 2022-06-14 01:24:01.851239
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = 1
    init_settings(args)
    assert settings.debug is True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 01:24:04.729268
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:24:07.163845
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:24:08.710903
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:24:10.404354
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert (settings.debug == True)


if __name__ == '__main__':
    pass

# Generated at 2022-06-14 01:24:26.067510
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:24:30.667612
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:32.451777
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:40.209320
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:24:43.289462
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:46.825441
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:51.574419
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:24:54.265984
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    setattr(args, 'debug', True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:25:00.080863
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False

if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:25:04.792690
# Unit test for function init_settings
def test_init_settings():
    def check(actual, expected):
        assert actual == expected

    args = Namespace()
    args.debug = True
    init_settings(args)
    actual = settings.debug
    expected = True
    check(actual, expected)

# Unit test