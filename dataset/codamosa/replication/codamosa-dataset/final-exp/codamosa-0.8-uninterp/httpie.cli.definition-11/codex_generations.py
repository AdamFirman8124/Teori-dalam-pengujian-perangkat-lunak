

# Generated at 2022-06-13 21:19:15.207177
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'param' in choices
    assert 'unknown' not in choices

# Generated at 2022-06-13 21:19:27.483087
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type', '-t',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Auto detect authentication type by looking at the URL. Currently, the
    following types are supported:

        {auth_types}

    '''.format(
        auth_types='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(_AuthTypeLazyChoices()), 60)
        ).strip()
    )
)

#######################################################################
# Configuration
#######################################################################

config = parser.add_argument_group(title='Configuration')

# Generated at 2022-06-13 21:19:36.434539
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help=f'''
    The plugin to use for authentication.

    The default behaviour is to guess the plugin to use based on the provided
    identifier. If the identifier looks like an email address, then the
    "hawk" plugin is used. Otherwise, the identifier is checked for a password
    separator (":"), if present "basic" authentication is used. Otherwise, the
    "digest" plugin is used.

    Valid values are: {','.join(plugin_manager.get_auth_plugin_mapping())}
    '''
)


# Generated at 2022-06-13 21:19:48.818316
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_types = plugin_manager.get_auth_plugin_mapping().keys()
    assert list(_AuthTypeLazyChoices()) == sorted(auth_types)


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.

    Currently supported:
    {helpers.format_available_plugins_list('auth', column_width=10)}

    See also: https://httpie.org/docs#authentication

    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL', description='''
TLS/SSL options (for HTTPS requests).
'''.strip())


# Generated at 2022-06-13 21:20:03.733425
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in lazy_choices
    assert 'DIGEST' not in lazy_choices

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify the authentication mechanism.
    The default is {DEFAULT_AUTH_PLUGIN_NAME}.

    Only relevant when --auth is used.
    The TYPE can be one of:

    {auth_plugin_help}

    If TYPE is the name of an installed, non-core plugin, it must be prefixed
    with 'plugin:' to avoid ambiguity (e.g., "plugin:basic").
    '''
)

# Generated at 2022-06-13 21:20:04.729575
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:15.318507
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == \
        sorted(list(_AuthTypeLazyChoices()))

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "basic",
    which is usually the only option needed and is the one assumed when
    --auth is used.

    The available types are:

    {plugin_doc_snippet}

    '''.format(
        plugin_doc_snippet='''
            {0}

        '''.format('\n            '.join(
            line.strip() for line in describe_auth_plugins().strip().splitlines()
        ))
    )
)


# Generated at 2022-06-13 21:20:22.772298
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of the auth plugin.

    If the --auth option doesn't contain the plugin name,
    it is inferred from the --auth-type option.

    '''
)


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:20:23.939627
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:26.599897
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert not 'foo' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:41.103009
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(_AuthTypeLazyChoices())

AUTH_TYPE_CHOICES = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=AUTH_TYPE_CHOICES,
    help='''
    Selects an HTTP authentication type. The default is "auto".

    Available types:

        {auth_plugins}

    '''.format(
        auth_plugins='\n '.join(
            wrap(', '.join(plugin_manager.get_auth_plugin_mapping()), 60)
        )
    )
)


# Generated at 2022-06-13 21:20:45.912610
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    check parameter constr : _AuthTypeLazyChoices()
    """
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)


# Generated at 2022-06-13 21:20:59.331221
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used: basic, digest, aws, hmac.

    Default is "basic".

    ''',
)

# Generated at 2022-06-13 21:21:00.649455
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:21:10.166334
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in auth_type_lazy_choices
    assert 'basic' in auth_type_lazy_choices
    assert 'hawk' in auth_type_lazy_choices
    assert 'aws4-hmac-sha256' in auth_type_lazy_choices
    assert 'aws4-hmac-sha384' in auth_type_lazy_choices
    assert 'aws4-hmac-sha512' in auth_type_lazy_choices


# Generated at 2022-06-13 21:21:13.774785
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        AUTO_AUTH_PLUGIN_NAME,
        BASIC_AUTH_PLUGIN_NAME,
        DIGEST_AUTH_PLUGIN_NAME
    ]

# Generated at 2022-06-13 21:21:27.206314
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for item in _AuthTypeLazyChoices:
        assert item in plugin_manager.get_auth_plugin_mapping()


# ``requests.request`` keyword arguments.
auth_plugin = parser.add_argument_group(title='Authentication Plugin Options')
auth_plugin.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices,
    help='''
    The name of the authentication plugin to use (case-insensitive).

    Use `http --debug | grep Available-Auth` to get a list of available
    authentication plugins.

    '''
)

# Generated at 2022-06-13 21:21:38.821956
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    atp = _AuthTypeLazyChoices()
    assert 'digest' in atp
    assert 'basic' in atp
    assert list(sorted(['digest', 'basic'])) == list(sorted(atp))

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use.

    Available choices depend on the --auth plugin used.

    ''',
)


# Generated at 2022-06-13 21:21:45.733654
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == []

auth.add_argument(
    '--auth-type',
    metavar='{' + ','.join(_AuthTypeLazyChoices()) + '}',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use.

    If this option is not given and --auth is provided,
    HTTPie tries to guess the auth type from the credential string:

    - Basic auth: credentials are formatted as username:password
    - Digest auth: credentials are formatted as username:password
    - Bearer Token: credential string only (no colon)

    To check the supported auth plugins, run:

        $ http --plugins-auth

    '''
)

# Generated at 2022-06-13 21:21:46.697019
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:22:05.582865
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))


# Generated at 2022-06-13 21:22:19.080237
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert hasattr(_AuthTypeLazyChoices(), '__getitem__') is False
    assert hasattr(_AuthTypeLazyChoices(), '__len__') is False
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hmac' in _AuthTypeLazyChoices()
    assert 'awssigv4' in _AuthTypeLazyChoices()

auth_type = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:22:28.574120
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.plugins import AUTH_PLUGIN_NAMES
    assert list(iter(_AuthTypeLazyChoices())) == AUTH_PLUGIN_NAMES

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication plugin (implies --auth unless a plugin
    that provides its own prompt is used, in which case the plugin's
    prompt will be used, e.g. OAuth 1).

    The following plugins are available:

        {0}

    '''.format(', '.join(plugin_manager.get_auth_plugin_mapping().keys()))
)

#######################################################################
# Downloads.
#######################################################################

download = parser.add_argument_

# Generated at 2022-06-13 21:22:33.502353
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    with mock.patch.dict(sys.modules,
                         {'httpie.plugins.auth': mock.Mock(plugins=None),
                          'httpie.plugins': mock.Mock(auth=None)}):
        auth_types_lazy = _AuthTypeLazyChoices()
        assert 'basic' not in auth_types_lazy
        assert 'digest' not in auth_types_lazy

    with mock.patch.dict(sys.modules,
                         {'httpie.plugins.auth': mock.Mock(plugins=[]),
                          'httpie.plugins': mock.Mock(auth=[])}):
        auth_types_lazy = _AuthTypeLazyChoices()
        assert 'basic' not in auth_types_lazy
        assert 'digest' not in auth_types_lazy



# Generated at 2022-06-13 21:22:34.853652
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:22:47.239290
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_types = _AuthTypeLazyChoices()
    assert list(auth_types) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

auth_plugin_descriptions = f'''
    Authentication can be provided with a custom plugin, e.g.:

        -a custom,path/to/my_auth_plugin.py

    Plugins can be installed via:

        $ {exe_name} plugin install [URL|PATH]

    Available plugins:

        {", ".join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''


# Generated at 2022-06-13 21:22:59.796143
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Set the authentication mechanism. The default is "auto", which means HTTPie
    will try to determine the correct auth type based on the provided value and
    the response.

    '''
)
auth.add_argument(
    '--auth-type=basic',
    action='append_const',
    const='basic',
    dest='auth_types',
    help='''
    Shortcut for --auth-type basic.

    '''
)


# Generated at 2022-06-13 21:23:01.019876
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:23:03.156206
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert(list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys()))


# Generated at 2022-06-13 21:23:15.839749
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help=f'''
    The auth mechanism to be used.

    Defaults to {DEFAULT_AUTH_PLUGIN!r} for --auth and to null for --ignore-stdin.

    Available values: {', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))}

    If --ignore-stdin is specified, the auth plugin is not used, but the value
    is stored and applied when --auth is used.

    '''
)


#######################################################################
# SSL/TLS verification
#######################################################################

ssl = parser

# Generated at 2022-06-13 21:23:32.582912
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'krb5' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:46.350897
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an authentication plugin.

    The default choice is "basic" if --auth is used, otherwise no
    authentication is used.

    ''',
)

#######################################################################
# Options for interacting with the terminal.
#######################################################################


terminal = parser.add_argument_group(title='Terminal interaction')

# Generated at 2022-06-13 21:23:57.979317
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_AuthTypeLazyChoices(), _AuthTypeLazyChoices)


auth.add_argument(
    '--auth-type',
    dest='auth_type',
    help='''Choose an authentication type to override the default auth
    plugin. Available auth types: {0}.'''.format(', '.join(
        plugin_manager.get_auth_plugin_mapping().keys()
    )),
    default='auto',
    choices=_AuthTypeLazyChoices(),
)

# Generated at 2022-06-13 21:24:02.523053
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()


_auth_type_validator = AuthCredentialsInUrlValidator(
    'Auth credentials cannot be specified in both URL and --auth.')



# Generated at 2022-06-13 21:24:09.985763
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    type = _AuthTypeLazyChoices()
    list(type)

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specification of an authentication plugin. If not given, the authentication
    type will be guessed from --auth value.
    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')
ssl.add_argument(
    '--verify', '-k',
    dest='verify',
    action='store_true',
    default=None,
    help='''
    By default, HTTPie verifies the host's SSL certificate,
    but with this flag you can opt-out of verification.

    '''
)

# Generated at 2022-06-13 21:24:25.556796
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(AUTH_PLUGIN_MAP))



auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify the authentication mechanism. By default, it is
    auto-detected from the provided credentials.

    '''
)
auth.add_argument(
    '--auth-endpoint',
    default=None,
    metavar='URL',
    help='''
    Specify a custom endpoint for authenticating. By default the URL
    is guessed from the requested host.

    '''
)


# Generated at 2022-06-13 21:24:35.346986
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from tests.base import TestEnvironment
    from tests.compat import unittest
    from .data import BIN_FILE_ARG, FILE_PATH_ARG, JSON_FILE_ARG
    from .data import KEY_VALUE_ARG, KEY_VALUE_ARG_BYTES
    from .data import KEY_VALUE_FILE_ARG, KEY_VALUE_FILE_ARG_BYTES
    from .data import KEY_VALUE_FILE_PATH_BYTES
    from .data import KEY_VALUE_FILE_TEXT_ARG_BYTES, KEY_VALUE_TEXT_FILE_ARG_BYTES
    from .data import MULTIPLE_ITEMS_ARG, MULTIPLE_ITEMS_ARG_BYTES
    from .data import MULTIPLE_ITEMS_FILE_ARG, M

# Generated at 2022-06-13 21:24:44.710627
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == list(auth_type_lazy_choices)

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify a custom authentication plugin, e.g. {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}.
    See the built-in --help for details.

    '''
)

# Generated at 2022-06-13 21:24:56.535433
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    LazyChoices contains all auth plugins.
    """
    lazy_choices = _AuthTypeLazyChoices()
    assert list(lazy_choices.__iter__())


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    ''',
)
auth.add_argument(
    '--auth-host',
    default='127.0.0.1',
    help='''
    Hostname to be used in Basic and Digest auth.

    This allows Basic or Digest auth with a URL that doesn't include
    the hostname.

    ''',
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')


# Generated at 2022-06-13 21:25:04.681218
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hmac' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:25:28.207286
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert _AuthTypeLazyChoices.__name__ == '_AuthTypeLazyChoices'

auth.add_argument(
    '--auth-type',
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication type. Possible values depend on the authentication plugins
    you have enabled. The default is "auto" which will attempt to find the
    best plugin for the job.

    ''',
)

#######################################################################
# Verbose
#######################################################################

verbose = parser.add_argument_group(title='Verbosity')

# Generated at 2022-06-13 21:25:33.695136
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    # Method __contains__ of class _AuthTypeLazyChoices
    # returns False for invalid auth types, even if there is a plugin for them
    assert 'invalid' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:46.243200
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
auth.add_argument(
    '--auth-type',
    dest='auth_type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of a registered plugin that handles the specified --auth
    credentials.

    Use `http --debug` to see a list of all plugins.

    '''
)

# Generated at 2022-06-13 21:25:48.424010
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():

    # Given
    auth_type = _AuthTypeLazyChoices()
    expected = True

    # When
    actual = 'basic' in auth_type

    # Then
    assert actual == expected



# Generated at 2022-06-13 21:26:01.900270
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert list(lazy_choices) == ['basic']

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. By default (auto), the appropriate
    one is chosen based on the provided credentials.

    '''
)

auth.add_argument(
    '--digest',
    default=False,
    action='store_true',
    help='Send an initial request with authentication headers to trigger '
         '407 Proxy Authentication Required.',
)

#######################################################################
# Misc
#######################################################################

misc = parser.add_argument_group(title='Miscellaneous')


# Generated at 2022-06-13 21:26:12.360210
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for item in _AuthTypeLazyChoices():
        assert item in plugin_manager.get_auth_plugin_mapping()


# Generated at 2022-06-13 21:26:14.978807
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:18.540670
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


# Generated at 2022-06-13 21:26:25.928238
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(sorted(HTTPiePlugin())) == list(_AuthTypeLazyChoices())


auth_type = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:26:30.534110
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():

    class MockAuthPlugin(Plugin):
        auth_type = 'mock'

    with plugin_manager.context() as pm:
        pm.register(MockAuthPlugin)
        assert 'mock' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:27:00.790624
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:10.771515
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    The authentication mechanism to be used.

    Currently supported:

        {auth_plugins}

    '''.format(
        auth_plugins='\n'.join(
            (8 * ' ') + line.strip() for line in wrap(
                ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
                60
            )
        ).strip()
    )
)

# Generated at 2022-06-13 21:27:19.473582
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:27:21.002597
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:27:25.998690
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    import httpie.plugins
    assert 'None' in _AuthTypeLazyChoices()
    plugin_manager.deregister_auth_plugin('UnknownPlugin')
    assert 'UnknownPlugin' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:34.846086
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert len(list(_AuthTypeLazyChoices())) > 0


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Supported types:

    {0}

    '''.format(
        indent(format_choices(plugin_manager.get_auth_plugin_mapping()))
    )
)

#######################################################################
# Custom headers
#######################################################################

custom_headers = parser.add_argument_group(title='Custom Headers')


# Generated at 2022-06-13 21:27:45.514999
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'bearer' in auth_type_lazy_choices
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert 'jwt' in auth_type_lazy_choices
    assert 'hawk' in auth_type_lazy_choices
    assert 'ntlm' in auth_type_lazy_choices
    assert 'aws-auth-v4' in auth_type_lazy_choices
    assert 'aws-sig-v4' in auth_type_lazy_choices
    assert 'oauth1' in auth_type_lazy_choices
    assert 'aws-sig-v4' in auth_type_l

# Generated at 2022-06-13 21:27:50.046267
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for item in _AuthTypeLazyChoices():
        assert item in plugin_manager.get_auth_plugin_mapping()



# Generated at 2022-06-13 21:27:59.718487
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth_type = auth.add_mutually_exclusive_group()
auth_type.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use a custom authentication type.

    The following authentication types, which are HTTPie plugins, are
    currently available:

        {auth_types}

    For example, to enable the "digest" authentication:

        $ http --auth-type=digest -a username https://httpbin.org/get

    '''.format(
        auth_types='\n'.join(sorted(plugin_manager.get_auth_plugin_mapping()))
    )
)

# Generated at 2022-06-13 21:28:05.853638
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(sorted(_AuthTypeLazyChoices())) == ['digest', 'hawk', 'jwt', 'netrc', 'oauth1', 'okta', 'vapid']

auth.add_argument(
    '--auth-type',
    metavar='AUTHTYPE',
    type=plugin_manager.resolve_auth_plugin,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify an auth type to be used. If not provided the auth plugin will be determined from the URL.

    {help_list_plugins('auth')}

    '''
)

auth.add_argument(
    '--auth-verify',
    action='store_true',
    help=f'''
    Verify the supplied credentials.

    '''
)

#######################################################################

# Generated at 2022-06-13 21:29:04.702246
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:29:10.772682
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == ['digest', 'hawk', 'ntlm']

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    dest='auth_plugin_name',
    help='''
    Explicitly specify an authentication mechanism.

    To discover supported mechanisms, use --print=HBhb.

    '''
)