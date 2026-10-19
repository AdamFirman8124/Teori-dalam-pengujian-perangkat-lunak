

# Generated at 2022-06-13 21:19:20.588353
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert sorted(['basic', 'digest', 'oauth1']) == sorted(_AuthTypeLazyChoices())

#
# ``requests.auth.HTTPBasicAuth`` keyword arguments.
#
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=sorted(plugin_manager.get_auth_plugin_mapping().keys()),
    default='basic',
    help='''
    Specify a custom authentication plugin (custom plugins are also supported,
    see HTTPie wiki for more information).
    ''',
)

verify = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:19:33.825362
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


# Generated at 2022-06-13 21:19:36.969734
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert pluggy.PluginManager().get_auth_plugin_mapping() == dict(auth_type_lazy_choices)

# Generated at 2022-06-13 21:19:49.252191
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()))
    assert [i for i in _AuthTypeLazyChoices()] == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()))
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' not in _AuthTypeLazyChoices()
    assert 'foobar' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:20:03.953489
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Verify that the iterable is lazy
    from requests.auth import AuthBase
    from requests_toolbelt.auth.guess import GuessAuth

    class TestAuth(AuthBase):
        def __init__(self):
            pass

    with plugin_manager.with_plugins_disabled():
        choices = _AuthTypeLazyChoices()
        assert GuessAuth not in choices
        assert 'guess' not in choices

        plugin_manager.register(TestAuth)
        assert TestAuth in choices
        assert 'test' in choices

    assert TestAuth not in choices
    assert 'test' not in choices


# Generated at 2022-06-13 21:20:06.696350
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices()) == iter(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:20:08.663335
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:17.191298
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    if sys.version_info < (3, 6):
        assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']
    else:
        assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'jwt', 'hawk']

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    ''',
)

auth.add_argument(
    '--auth-endpoint',
    default=None,
    help='''\
    Override an auth provider's default authorization data endpoint.

    ''',
)


# Generated at 2022-06-13 21:20:19.581156
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'plugin_name' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:25.260628
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    '''
    >>> _AuthTypeLazyChoices().__contains__('invalid_plugin')
    False
    >>> _AuthTypeLazyChoices().__contains__('digest')
    True
    '''

# Generated at 2022-06-13 21:20:40.142635
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


auth_type_lazy_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=auth_type_lazy_choices,
    help='''
    Force using the specified HTTP authentication method. By default,
    HTTPie tries to determine the auth type by inspecting the provided user
    credentials and the server responses.

    Can be one of {0}.

    '''.format(
        ', '.join(sorted(auth_type_lazy_choices))
    ),
)

# Generated at 2022-06-13 21:20:51.213803
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == ['digest', 'hawk', 'jwt', 'netrc', 'oauth1', 'ntlm']
auth_type = auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication plugin to use. Plugins are discovered automatically and
    can be extended via entry points. See more in the `HTTPie Plugins`
    section of the documentation.

    ''',
)



# Generated at 2022-06-13 21:21:03.199584
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert choices == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication mechanism. The default is {0}.

    '''.format(DEFAULT_AUTH_PLUGIN_NAME),
)
auth.add_argument(
    '--auth-type=digest',
    dest='auth_plugin_name',
    action='store_const',
    const='digest',
    help=SUPPRESS
)

# Generated at 2022-06-13 21:21:14.840718
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert len(list(lazy_choices)) > 0


auth_type_validator = AuthTypeValidator(
    "Invalid authentication plugin name. Run 'http --plugins' for a list of available plugins."
)

# Defaults to deactivated for safety.
# Actual default is determined in RuntimeConfig.
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    type=auth_type_validator,
    help='''
    Specify a custom authentication plugin.
    Run 'http --plugins' for a list of available plugins.

    '''
)

# Generated at 2022-06-13 21:21:19.553385
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """
    Test if item is a key in the plugin_manager's __auth_plugin_mapping
    """
    assert item in plugin_manager.get_auth_plugin_mapping()

# Generated at 2022-06-13 21:21:21.792117
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'baz' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:21:30.486627
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert all(choice in choices for choice in [
        'basic',
        'digest',
        'aws',
        'hawk',
        'oauth1',
        'jwt',
        'ntlm',
    ])
    assert not any(choice in choices for choice in [
        'bogus',
        '',
        None,
    ])
    assert tuple(choices) == tuple(sorted(choices))

# A map of auth plugin aliases to the --auth-type argument.

# Generated at 2022-06-13 21:21:33.726276
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:21:43.210462
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert next(iter(choices))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication method to be used. Currently supported:

        {0}

    '''.format(
        '\n'.join(sorted('     {0}'.format(name) for name in plugin_manager.get_auth_plugin_mapping()))
    )
)

# Generated at 2022-06-13 21:21:45.490007
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    types = _AuthTypeLazyChoices()
    assert 'basic' in types
    assert 'digest' not in types
    assert 'unreal' not in types


# Generated at 2022-06-13 21:22:04.824763
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [item for item in _AuthTypeLazyChoices()] == ['basic', 'digest']


# Generated at 2022-06-13 21:22:18.096206
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hmac' in choices
    assert 'ntlm' in choices
    assert 'hawk' in choices
    l = list(choices)
    assert l[0] == 'basic'
    assert l[1] == 'digest'
    assert l[2] == 'hmac'
    assert l[3] == 'ntlm'
    assert l[4] == 'hawk'


# Generated at 2022-06-13 21:22:22.196062
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    global _AuthTypeLazyChoices
    choices = _AuthTypeLazyChoices()
    assert list(choices) == ['digest', 'hawk', 'multipart', 'netrc', 'oauth1', 'oauth2']

# Generated at 2022-06-13 21:22:34.381568
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    pass
assert _AuthTypeLazyChoices() == sorted(set(AUTH_PLUGINS) | {'basic'})

auth.add_argument(
    '--auth-type',
    metavar='PLUGIN',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Use the specified authentication plugin. Plugins:

        {' '.join(AUTH_PLUGINS)}

    ''',
    # TODO: figure out how to properly handle sub-commands with plugins.
    # Hidden until implemented.
    # action='append',
    # default=[],
)


# Generated at 2022-06-13 21:22:36.010876
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert ('Basic' in _AuthTypeLazyChoices()) == True

# Generated at 2022-06-13 21:22:38.841967
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(_Auth_TYPES))


# Generated at 2022-06-13 21:22:40.718549
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('digest')


# Generated at 2022-06-13 21:22:51.928499
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    def assert_iter(items):
        assert list(iter(items)) == list(items)
    assert_iter(['Digest'])
    assert_iter(['Basic', 'Digest'])


# Generated at 2022-06-13 21:23:02.141269
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert HTTPBasicAuth in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    dest='auth_type',
    help='''
    The authentication mechanism to be used. Builtin mechanisms:

    ''' + (
        '\n'.join(f'    {name}' for name in sorted(AUTH_PLUGIN_MAP.keys()))
    ) + '''

    The default is '{0}'.

    Third-party pluggable authentication plugins are supported as well.
    See `http --help-auth-plugins` for details.

    '''.format(DEFAULT_AUTH_PLUGIN.get_auth_type())
)


# Generated at 2022-06-13 21:23:09.539998
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    Unit test for method __iter__ of class _AuthTypeLazyChoices.
    """
    assert _AuthTypeLazyChoices().__iter__() == ["basic", "digest", "ntlm"]

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help='''
    The authentication mechanism to be used. Supported mechanisms are:
    basic, digest and ntlm.

    '''
)

auth.add_argument(
    '--auth-send',
    default='hmac',
    choices=['hmac', 'user'],
    help='Send (digest) credentials on (non)initial requests.'
)

#######################################################################
# Transport
#######################################################################

transport = parser.add_argument

# Generated at 2022-06-13 21:23:32.396149
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
auth = parser.add_argument_group(title='Authentication')
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to be used.
    {auth_plugins_doc}
    '''.format(
        auth_plugins_doc=plugin_manager.get_auth_plugins_doc()
    )
)

# Generated at 2022-06-13 21:23:46.239284
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.plugins import builtin
    builtin.__auth_plugins__ = {}
    assert len(list(_AuthTypeLazyChoices())) == 0
    builtin.__auth_plugins__ = {'abc': None}
    assert list(_AuthTypeLazyChoices()) == ['abc']
    builtin.__auth_plugins__ = {'abc': None, 'def': None}
    assert sorted(list(_AuthTypeLazyChoices())) == ['abc', 'def']

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Run `http --help-auth` to view
    all available authentications.

    '''
)


# Generated at 2022-06-13 21:23:57.888978
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins.builtin import AuthBasicPlugin
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_dir:
        plugin_manager.directories.append(tmp_dir)
        with plugin_manager.plugin_dir_path(tmp_dir, 'test_plugin'):
            with open(plugin_manager.plugin_dir_path(tmp_dir, 'test_plugin', '__init__.py'), 'w') as f:
                f.writelines(['from httpie.plugins.auth.basic import AuthBasicPlugin\n'])
        assert 'test_plugin' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:03.618049
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'foobar' not in lazy_choices
# Add unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2022-06-13 21:24:07.538019
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert ('basic' in choices) == ('httpie.plugins.auth.basic' in plugin_manager.get_auth_plugin_mapping())

# Generated at 2022-06-13 21:24:21.472314
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    '''Unit test for method __iter__ of class _AuthTypeLazyChoices.'''
    auth_type = _AuthTypeLazyChoices()
    assert 'basic' in auth_type
    assert 'digest' in auth_type
    assert len([k for k in auth_type]) == 2
_AuthTypeLazyChoices.__name__ = 'AuthType'


# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type', '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Force the use of a specified auth plugin.

    ''',
)


# Generated at 2022-06-13 21:24:23.997872
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

# Generated at 2022-06-13 21:24:34.256540
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force usage of a particular authentication type.

    This option is useful when a URL contains an authentication realm, but
    the authentication plugin to use is not specified in that realm, or when
    using a plugin that is not discovered through the normal plugin discovery
    process.

    If a plugin is explicitly selected, any authentication information
    embedded in a URL will be ignored.

    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:24:44.258745
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # Method __contains__ of class _AuthTypeLazyChoices returns ``True`` if
    # given choice is a key in auth plugin mapping.

    # Save current plugin mapping
    original_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # Override plugin mapping with custom one
    try:
        custom_plugin_mapping = {'custom': 'custom_auth_plugin'}
        plugin_manager.get_auth_plugin_mapping = lambda: custom_plugin_mapping
        assert 'custom' in _AuthTypeLazyChoices()
    finally:
        # Rollback original plugin mapping
        plugin_manager.get_auth_plugin_mapping = lambda: original_plugin_mapping



# Generated at 2022-06-13 21:24:46.227248
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(['basic']))


# Generated at 2022-06-13 21:25:04.357164
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in lazy_choices
    assert 'multipass' not in lazy_choices

# Generated at 2022-06-13 21:25:09.168428
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """
    >>> 'digest' in _AuthTypeLazyChoices()
    True
    >>> 'oauth1' in _AuthTypeLazyChoices()
    True
    >>> 'basic' in _AuthTypeLazyChoices()
    True
    >>> 'foo' in _AuthTypeLazyChoices()
    False
    """



# Generated at 2022-06-13 21:25:18.870297
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'non_existing_auth_method' not in choices


auth.add_argument(
    '--auth-type',
    default=None,
    help=f'''
    The authentication mechanism to be used.

    One of: {sorted(plugin_manager.get_auth_plugin_mapping().keys())}

    ''',
    choices=_AuthTypeLazyChoices(),
)

auth.add_argument(
    '--auth-type-key',
    default=None,
    metavar='KEY',
    help='''
    Case sensitive key in JSON response dictionary which contains the
    auth_type.

    ''',
)

#######################################################################
# Other
#######################################################################

other = parser.add

# Generated at 2022-06-13 21:25:28.240747
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices

#######################################################################
# Misc
#######################################################################

misc = parser.add_argument_group(title='Misc')

misc.add_argument(
    '--follow', '-F',
    action='store_true',
    default=False,
    help='''
    Follow redirects.

    '''
)
misc.add_argument(
    '--max-redirects',
    type=int,
    default=30,
    help='''
    Maximum number of redirects to follow.

    '''
)

# Generated at 2022-06-13 21:25:37.684966
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    sorted(_AuthTypeLazyChoices())

auth_type_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_type',
    choices=auth_type_choices,
    help='''
    Specify the authentication scheme used for the request.
    The explicit list of available options depends on installed plugins.

    The default is to autodetect based on the hostname, but you can force
    a plugin.

    '''
)


# Generated at 2022-06-13 21:25:50.255450
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use. By default, the plugin will attempt to
    auto-discover the appropriate auth mechanism based on the response
    WWW-Authenticate header.

    Supported mechanisms are: {plugin_auth_choices}

    '''.format(plugin_auth_choices=', '.join(
        sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)


# Generated at 2022-06-13 21:25:51.866340
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert OUTPUT_OPTIONS in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:04.115894
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force the specified authentication plugin.

    The following {num_auth_plugins} plugin(s) are available:

    {available_auth_plugins}

    '''.format(
        num_auth_plugins=len(
            plugin_manager.get_auth_plugin_mapping()),
        available_auth_plugins=', '.join(
            plugin_manager.get_auth_plugin_mapping().keys())
    )
)

#######################################################################
# Parser
#######################################################################


# Generated at 2022-06-13 21:26:20.543738
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert len(list(lazy_choices)) > 0

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force usage of a specific authentication method.
    By default HTTPie tries to guess this based on --auth.

    ''',
)


# Generated at 2022-06-13 21:26:22.320222
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:58.843784
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # Needed for plugin testing
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type', '--auth-plugin',
    default=AUTH_PLUGIN_MAP['auto'],
    metavar='TYPE',
    type=plugin_manager.resolve_auth_plugin,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify an authentication plugin. Default is "auto" (attempt all
    plugins in order).

    Available plugins: {', '.join(sorted(AUTH_PLUGIN_MAP))}
    '''
)

#######################################################################
# Persistence options
#######################################################################

persistence = parser.add_argument_group(title='Persistence')

# Generated at 2022-06-13 21:27:09.793763
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices"""
    actual = [plugin for plugin in _AuthTypeLazyChoices()]
    assert set(actual) == set(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin to use. See the plugin
    documentation for more details: {0}

    '''.format(', '.join(plugin_manager.get_plugin_urls('auth')))
)


# Generated at 2022-06-13 21:27:11.584873
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:19.967779
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'kerberos' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Force the specified authentication mechanism.
    The following auth types are supported:
    {auth_types_docs}
    '''
)
#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:27:27.941594
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Supported: basic, digest.

    If no type is specified, then the command-line client detects
    the auth type sent by the server and uses it.

    See also --auth.

    ''',
)

# Generated at 2022-06-13 21:27:30.135312
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )

# Generated at 2022-06-13 21:27:43.148318
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "basic".
    Other mechanisms supported out of the box are "digest" and "aws4".

    '''
)

SCHEME = 'SCHEME'
PARAMETERS = 'PARAMETERS'


# Generated at 2022-06-13 21:27:57.592396
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'digest', 'hawk', 'jwt', 'oauth1', 'oauth2'
    ]


# Generated at 2022-06-13 21:28:04.640649
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The special value "auto" can be
    used to select the auth mechanism based on the following precedence:
    Basic, Digest, and then Netrc, for a given URL.

    Defaults:
        Basic: --auth is present
        Digest: --auth is present
        Netrc: --netrc is used

    ''',
)


# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:28:14.921157
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    AVAILABLE_AUTHS = list(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    metavar='AUTHTYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to be used. If not set, then it's detected from the
    auth credentials.

    Available: {0} (case-insensitive)

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)


#######################################################################
# Proxy
#######################################################################

proxies = parser.add_argument_group(title='Proxies')