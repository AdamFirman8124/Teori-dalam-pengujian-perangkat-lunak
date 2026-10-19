

# Generated at 2022-06-13 21:19:18.254360
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == \
           sorted(_AuthTypeLazyChoices())



# Generated at 2022-06-13 21:19:31.226298
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # To support testing this method, we temporarily add a test plugin to the
    # plugin manager.
    plugin_manager.get_auth_plugin_mapping()["wtest_test"] = Mock()
    assert "wtest_test" in _AuthTypeLazyChoices()
    # Remove the test plugin
    assert "wtest_test" not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:19:42.730568
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hawk' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to use. By default, the server response is
    analyzed and the most secure mechanism that both client and server support
    is automatically used. It is possible to explicitly select a mechanism.

    '''
)


# Generated at 2022-06-13 21:19:52.464455
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():

    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    help='''
    Specify the auth mechanism.

    Either:

        builtin:
            The default, if --auth is provided.

            Supported builtin schemes: basic, digest.

        plugin:
            Use a 3rd-party auth plugin.

            Plugins are searched for in the `HTTPIE_AUTH_PLUGIN_PATH`
            or in the directory where the `http` command is installed.

            Plugins can be disabled by setting `HTTPIE_AUTH_PLUGINS_DISABLED`
            to a list of plugin names.

    '''
)

# Generated at 2022-06-13 21:20:07.587948
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    default=AUTH_PLUGIN_DEFAULT,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication plugin to use. The default is "{AUTH_PLUGIN_DEFAULT}".

    These are currently available (case insensitive):

    {plugin_manager.get_auth_plugin_names_help()}

    '''.strip()
)

# Generated at 2022-06-13 21:20:16.514218
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    default='auto',
    metavar='TYPE',
    help=f'''
    Override the default authentication mechanism (Basic by default).
    Available plugins: {', '.join(_AuthTypeLazyChoices())}

    ''',

    choices=_AuthTypeLazyChoices()
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    Do not perform challenge response (--auth-type=basic only).

    '''
)

###############################################################################
# HTTP method
###############################################################################

method = parser.add_argument_group(title='HTTP method')

# Generated at 2022-06-13 21:20:26.060669
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == \
        list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth plugin to use. Run `http --auth-type=help` to see all
    available plugins or visit https://httpie.org/docs/plugins/authentication
    for more information.
    ''',
)


# Generated at 2022-06-13 21:20:38.496507
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.auth import basic_auth, digest_auth
    plugin_manager.auth_plugins = (basic_auth, digest_auth)
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']
    plugin_manager.auth_plugins = ()

auth.add_argument(
    '--auth-type', '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify a authentication handler. By default, the authentication
    type is guessed from the provided credentials, or, if no credentials
    are given, no authentication is used.

    Available handlers: {0}

    '''.format(
        ', '.join(
            plugin.name
            for plugin in plugin_manager.get_auth_plugins()
        )
    )
)



# Generated at 2022-06-13 21:20:45.747400
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    class __AuthTypeLazyChoicesMock(collections.abc.Iterable):
        class __AuthTypeLazyChoicesMockIterator():
            def __iter__(self):
                return iter([])
        def __iter__(self):
            return self.__AuthTypeLazyChoicesMockIterator()
    _AuthTypeLazyChoices.__bases__ = (__AuthTypeLazyChoicesMock,)
    with pytest.raises(TypeError):
        iter(_AuthTypeLazyChoices())
    del _AuthTypeLazyChoices.__bases__
del test__AuthTypeLazyChoices___iter__

# Generated at 2022-06-13 21:20:56.423772
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_plugin',
    help='Authentication plugin to use.',
    choices=_AuthTypeLazyChoices()
)
auth.add_argument(
    '--auth-use-default-credentials',
    action='store_true',
    help=f'''
    Use default credentials for Windows HTTP authentication.

    {AUTH_PLUGIN_DOCS_MSG}

    '''
)



# Generated at 2022-06-13 21:21:08.048739
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_iterable = _AuthTypeLazyChoices()
    assert list(lazy_iterable) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


auth.add_argument(
    '--auth-type',
    metavar='type',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
        Overrides the default authentication mechanism.

        Available auth types:

        - basic
        - digest
        - oauth1
        - oauth2
        - aws
        - awsv4
        - hawk

    '''
)


# Generated at 2022-06-13 21:21:19.902429
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices()) == iter(sorted(_auth_plugin_mapping.keys()))
auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism to be used.

    Defaults to "auto", which instructs HTTPie to use the
    first mechanism advertised by the server, but falling back
    to "basic" if it's not advertised.

    Supported mechanisms:

        {0}

    '''.format(
        wrap(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())), 65)
    )
)
#

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:21:29.877505
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'ntlm' in _AuthTypeLazyChoices()
    assert 'hawkeye' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use: {0}
    '''.format(
        ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    )
)

# Generated at 2022-06-13 21:21:32.146877
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert isinstance(iter(_AuthTypeLazyChoices()), collections.abc.Iterator)

# Generated at 2022-06-13 21:21:42.500939
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'basic' in choices
    assert 'http' in choices
    assert 'ntlm' in choices
    assert 'hawk' in choices
    assert sorted(choices) == sorted(
        ['digest', 'basic', 'http', 'ntlm', 'hawk']
    )


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    metavar='TYPE',
    help='''
    Specify an authentication type to be used. If the type is not specified,
    HTTPie tries to guess it based on the provided credentials (URL user
    portion, --auth option), or the credentials required by the server.

    '''
)

#######################################################################


# Generated at 2022-06-13 21:21:44.632838
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_types = _AuthTypeLazyChoices()
    assert [auth_type for auth_type in auth_types] == \
        sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:21:45.938054
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:57.067191
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices().__iter__()

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication plugin used. Choices: {0}.

    The default is {1} .

    '''.format(
        ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
        DEFAULT_AUTH_PLUGIN
    )
)

# Generated at 2022-06-13 21:22:09.638884
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth_type = auth.add_mutually_exclusive_group(required=False)

# Generated at 2022-06-13 21:22:22.304014
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices


auth.add_argument(
    '--auth-type',
    default=AUTH_SESSION_TYPE_DEFAULT,
    metavar='authen_scheme',
    help='''
    The authentication scheme to use.
    Available schemes are: {auth_type_choices}
    '''.format(
        auth_type_choices=', '.join(sorted(
            plugin_manager.get_auth_plugin_mapping().keys()))
    ),
    type=str
)

# Generated at 2022-06-13 21:22:37.242114
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    [C, C]

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    type=plugin_manager.get_auth_plugin_mapping().__getitem__,
    choices=_AuthTypeLazyChoices(),
    help='''
    The login mechanism to use for authentication.
    Currently, the only supported mechanism is basic.

    '''
)

#######################################################################
# Helpers
#######################################################################

# Used by docopt


# Generated at 2022-06-13 21:22:47.071083
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()
    assert 'Integrated' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify a backend plugin for authentication.

    '''
)

auth.add_argument(
    '--proxy-auth', '-A',
    default=None,
    metavar='USER[:PASS]',
    help='''
    If only the username is provided (-a username), HTTPie will prompt
    for the password.

    ''',
)



# Generated at 2022-06-13 21:22:59.628929
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic',
        'digest',
        'gssnegotiate',
        'hawk',
        'ntlm',
        'oauth1',
    ]

from functools import partial
AuthType = partial(str, choices=_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:23:07.485802
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth_type_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    default='basic',
    choices=auth_type_choices,
    help='''Specifies which method to use for authentication.'''
)

# Generated at 2022-06-13 21:23:09.464989
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:18.833868
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.plugins.builtin import AuthPlugin
    from httpie.context import Environment

    class DummyAuthPlugin(AuthPlugin):
        name = 'dummy-auth-plugin'

    for name in _AuthTypeLazyChoices():
        string = str(name)
        assert string == 'basic' or string == 'digest'

    original_plugins = plugin_manager.get_auth_plugins()
    environment = Environment(stdin=sys.stdin.buffer,
                              stdout=sys.stdout.buffer,
                              colors=256,
                              unicode=True,
                              style=DEFAULT_STYLE,
                              error_style=DEFAULT_ERROR_STYLE)
    plugin_manager.discover_auth_plugins(environment=environment)

# Generated at 2022-06-13 21:23:25.270271
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for AuthTypeLazyChoices.__iter__"""
    choices = _AuthTypeLazyChoices()
    assert "basic" in choices
    assert "digest" in choices


auth.add_argument(
    '--auth-type',
    metavar='AUTHTYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify a particular auth mechanism, e.g. "basic"
    or "digest".

    '''
)


#######################################################################
# SSL
#######################################################################

ssl_verify_group = parser.add_argument_group(title='SSL Verification')

# Generated at 2022-06-13 21:23:32.906661
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' in plugin_manager.get_auth_plugin_mapping()
    assert 'NTLM' in _AuthTypeLazyChoices()
    assert 'NTLM' in plugin_manager.get_auth_plugin_mapping()
    assert 'negotiate' not in _AuthTypeLazyChoices()
    assert 'negotiate' not in plugin_manager.get_auth_plugin_mapping()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    The default is "basic", which performs base64 encoding.

    '''
)


# Generated at 2022-06-13 21:23:36.489738
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'header' in _AuthTypeLazyChoices()
    assert 'custom_auth' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:49.159620
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    for plugin_type in choices:
        assert callable(plugin_manager.get_plugin(plugin_type))


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),  # type: ignore
    help='''
    Authentication scheme to use (defaults to auto).
    Use this to access servers that use non-standard schemes that cannot be
    detected automatically.
    Available types:

    {0}

    '''.format(
        ', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))
    ),
)

#######################################################################
# Timeouts
#######################################################################

timeouts = parser.add

# Generated at 2022-06-13 21:24:05.475356
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:14.168944
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert tuple(_AuthTypeLazyChoices()) == ('digest', 'hawk', 'ntlm')

auth_type = auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of an authentication plugin to use. Available plugins: {0}

    '''.format(', '.join(sorted(_AuthTypeLazyChoices())))
)

auth_plugins_help = ' '.join(
    p.get_auth_help(auth_type)
    for p in plugin_manager.get_auth_plugins()
)


# Generated at 2022-06-13 21:24:28.118750
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'bearer' in _AuthTypeLazyChoices()
    assert 'aws' in _AuthTypeLazyChoices()
    assert 'jwt' in _AuthTypeLazyChoices()
    assert 'negotiate' in _AuthTypeLazyChoices()

auth_type_validator = AuthTypeValidator(
    'Invalid authentication type.'
)

# Generated at 2022-06-13 21:24:30.296314
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'foo' not in choices



# Generated at 2022-06-13 21:24:42.412195
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    Check that _AuthTypeLazyChoices is a iterable, and that the iterator
    contains the names of installed auth plugins.
    """
    plugin_loaded = False
    for auth_type in _AuthTypeLazyChoices():
        plugin_loaded = True
        assert auth_type in plugin_manager.get_auth_plugin_mapping()
    assert plugin_loaded

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help='''
    Choose the auth type, auto-detected by default.

    '''
)

# Generated at 2022-06-13 21:24:54.197612
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for auth_type in _AuthTypeLazyChoices():
        assert auth_type in plugins.auth.__all__


auth.add_argument(
    '--auth-type',
    default=plugins.auth.DEFAULT_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='Specify an authentication plugin. '
         'By default, the plugin is inferred from --auth.'
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='Do not try to use server-provided challenges'
)


#######################################################################
# HTTP method
#######################################################################
method = parser.add_argument_group(title='HTTP method')


# Generated at 2022-06-13 21:25:03.478945
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Test _AuthTypeLazyChoices.__iter__
    pass
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin to use. If not provided, HTTPie
    will try to guess the type of authentication (Basic or Digest).
    Plugins are located in the ``httpie/plugins/auth`` directory.

    ''',
)

# Generated at 2022-06-13 21:25:13.007583
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dirname:
        # Set the plugins directory as the temporary directory
        plugin_manager.PLUGINS_DIR = temp_dirname
        # Create a file with a simple plugin
        with open(os.path.join(temp_dirname, 'test.py'), 'w') as f:
            f.write(
                'from httpie.plugins.auth.base import AuthPlugin\n'
                'import os\n'
                'class TestAuthPlugin(AuthPlugin):\n'
                '    name = "test"\n'
                '    auth_type = "test"\n'
                '    description = "Description for test"'
            )
        # Test if the plugin can be loaded and if it is contained in the class
        plugin_manager.load_plugins

# Generated at 2022-06-13 21:25:20.300614
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert hasattr(lazy_choices, '__contains__')
    assert hasattr(lazy_choices, '__iter__')

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.

    Currently supported authentication types are:

    {indent(", ".join(sorted(plugin_manager.get_auth_plugin_mapping().keys())), 4 * ' ')}

    '''.strip()
)

# Generated at 2022-06-13 21:25:28.939612
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hawk' in choices

auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_plugin',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help="""
    The name of an installed auth plugin. If not specified, a plugin is
    selected based on the provided credential information.

    """
)
auth.add_argument(
    '--auth-all',
    dest='auth_all',
    action='store_true',
    default=False,
    help='''
    Send credentials to all hosts in a URL. By default, it only sends them to
    the host of the first URL segment.

    '''
)

# Generated at 2022-06-13 21:25:45.374928
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [('Basic', 'basic'), ('Digest', 'digest')]



# Generated at 2022-06-13 21:25:55.006373
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for a in _AuthTypeLazyChoices():
        pass

auth_type_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default=BasicAuthPlugin.name,
    choices=auth_type_choices,
    help=''' {}

    '''.format(plugin_manager.get_auth_plugin_help())
)


# ~/.netrc parser.
netrc = parser.add_argument_group(title='Netrc')
netrc.add_argument(
    '--netrc-optional',
    action='store_true',
    help='''
    Do not abort if ~/.netrc doesn't exist
    (see also --netrc-file and --netrc-required).

    '''
)

# Generated at 2022-06-13 21:26:05.188405
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hmac' in choices
    assert 'custom' not in choices
    assert sorted(choices) == sorted(plugin_manager.get_auth_plugin_mapping())


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "basic".

    '''
)

auth.add_argument(
    '--auth-endpoint',
    default=None,
    help='''
    Authentication endpoint URL (e.g. "/login").

    '''
)


# Generated at 2022-06-13 21:26:21.011545
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported:

    {0}

    '''.format(
        # Keep this in-line.
        # This allows us to autogenerate the docs
        # based on the actual available plugins.
        # See the docs/generate.py script.
        ',\n'.join(
            8 * ' ' + name + (
                ' (default)' if name == DEFAULT_AUTH_PLUGIN else ''
            )
            for name in plugin_manager.get_auth_plugin_mapping().keys()
        )
    )
)

# Generated at 2022-06-13 21:26:26.038240
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    try:
        assert isinstance(choices.__iter__(), collections.abc.Iterator)
    except AttributeError:
        assert isinstance(choices.__iter__(), types.GeneratorType)


# Generated at 2022-06-13 21:26:36.343428
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """ Test lazy choices for --auth-type= option
    """
    expected = sorted([
        'basic',
        'digest',
        'hawk',
        'bearer'
    ])
    assert list(sorted(_AuthTypeLazyChoices())) == expected


auth_type = auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used: basic, digest, hawk, bearer, etc.
    By default, the plugin is guessed based on the provided URL (basic if no
    credentials provided, digest if username is provided, and hawk if a
    Bearer token is provided).

    '''
)

# Generated at 2022-06-13 21:26:48.496368
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(AUTH_PLUGIN_MAP.keys())

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify the authentication mechanism.

    The default is {AUTH_PLUGIN_MAP[DEFAULT_AUTH_PLUGIN]}.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    dest='auth_no_challenge',
    action='store_true',
    help='''
    Prevent automatic HTTP challenge response.

    ''',
)


# Generated at 2022-06-13 21:27:01.311193
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Builtin, non-plugin auth type
    assert list(_AuthTypeLazyChoices())[0] == 'basic'
    # Plugins, see plugins tests for coverage of these plugins
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'jwt' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=AuthCredentials.parse_auth_type,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.
    Defaults to "basic" if --auth is provided, otherwise none.

    Available types:

    {plugin_manager.get_supported_auth_plugins_help()}
    '''
)


# Generated at 2022-06-13 21:27:11.078827
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(HTTPieAuthPlugin.auth_types)


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism:

        {auth_types}

    This can be used to try other, experimental authentication methods,
    provided that the server supports them.

    '''.format(
        auth_types=' '.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(sorted(HTTPieAuthPlugin.auth_types)), 60)
        ).strip()
    )
)

#######################################################################
# Timeouts
#######################################################################

# Generated at 2022-06-13 21:27:12.382756
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:27:46.897480
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:58.399270
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '-t',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Force the specified HTTP authentication method to be used.
    Available methods:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

# Generated at 2022-06-13 21:28:04.996274
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_system',
    default='auto',
    metavar='AUTH_SYSTEM',
    choices=_AuthTypeLazyChoices(),
    help=''.join([
        'Authentication mechanism. ',
        'Avoid using this option as it will be removed in a future release. ',
        'The supported mechanisms are: ',
        ', '.join(plugin_manager.get_auth_plugin_mapping().keys()),
        '. The default is "auto", which will use the best plugin for the job.',
    ])
)

# Generated at 2022-06-13 21:28:15.027743
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    plugin_manager.get_auth_plugin_mapping()['test'] = lambda: None
    assert 'test' in choices
    assert ('basic', 'test') == tuple(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    type=str,
    metavar='AUTH_PLUGIN',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specifies the authentication mechanism.
    The default mechanism is 'basic'. The following are available:

        {0}

    Plugins not distributed with HTTPie are also supported.

    '''.format(', '.join(plugin_manager.get_auth_plugin_mapping().keys()))
)


# Generated at 2022-06-13 21:28:32.485655
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert HTTPBasicAuth in choices
    assert 'basic' in choices
    assert HTTPDigestAuth in choices
    assert 'digest' in choices

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    ''',
)

auth.add_argument(
    '--auth-json',
    action='store_true',
    default=None,
    help='''
    Encode the passed credentials into an application/json request body.
    Do not use with --auth.

    ''',
)


# Generated at 2022-06-13 21:28:38.352125
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    def test(expected, returned):
        assert expected == (
            returned in _AuthTypeLazyChoices()
        )
    yield test, True, 'digest'
    yield test, False, 'Digest'
    yield test, False, 'Digestaaa'
    yield test, False, 'Digest,basic'
    yield test, False, 'Digest,'
    yield test, True, 'Digest,Basic'
    yield test, False, 'Digest,Basic,'
    yield test, False, 'Digest, Basic'

# Generated at 2022-06-13 21:28:48.314911
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_choices
    assert 'digest' in auth_type_choices
    assert 'gssnegotiate' in auth_type_choices
    assert 'hawk' in auth_type_choices
    assert 'aws4' in auth_type_choices
    assert 'oauth1' in auth_type_choices


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified auth plugin instead of the default one.
    The default plugin is chosen based on the HTTP URL's scheme
    (e.g., "http://" -> basic, "https://" -> digest).

    ''',
)

# Generated at 2022-06-13 21:28:58.658995
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert test_config(
        config_dict=dict(default_options=dict(auth_type = 'basic')),
        config_file=None,
        args=['--session=test-session-3', "http://localhost:5000/"],
        output_opts=dict(
            output_options=OUTPUT_OPTIONS,
            output_options_history=OUTPUT_OPTIONS_HISTORY,
            output_options_session=OUTPUT_OPTIONS_SESSION,
            output_file=None
        ),
        env=env,
        error_exit_ok=True
    )


# Generated at 2022-06-13 21:29:07.797631
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'www' in auth_type_lazy_choices
    assert 'basic' not in auth_type_lazy_choices

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_plugin_name',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used, e.g., Basic or Digest.

    ''',
)

auth.add_argument(
    '--auth-verify',
    action='store_true',
    default=False,
    help='''
    Fail if the server returns a 401 Unauthorized.

    ''',
)

#######################################################################
# SSL
################################