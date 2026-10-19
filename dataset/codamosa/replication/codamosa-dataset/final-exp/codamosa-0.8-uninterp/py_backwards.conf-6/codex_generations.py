

# Generated at 2022-06-14 01:22:04.800722
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    setattr(args, 'debug', True)
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    os.system(f'pytest {os.path.basename(__file__)}')

# Generated at 2022-06-14 01:22:07.401340
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:22:10.864496
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:13.470261
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:16.905349
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:18.819458
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:22:24.774351
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace()
    init_settings(args)
    assert settings.debug is False

if __name__ == '__main__':
    assert False

# Generated at 2022-06-14 01:22:26.699425
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:22:29.266317
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:34.790639
# Unit test for function init_settings
def test_init_settings():
    settings = Settings()
    args = ['-d']
    init_settings(Namespace(debug=True))
    assert settings.debug == True
    return