

# Generated at 2022-06-13 21:19:26.968284
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins.builtin import BasicAuthPlugin
    auth_type = _AuthTypeLazyChoices()
    assert BasicAuthPlugin.auth_type in auth_type

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. By default, it is inferred
    from --auth, but on occasion it can be useful to specify it
    explicitly, such as when using --auth-type=ntlm with an NTLM proxy.

    The list of available types can be seen with the command:

        http --help-auth

    '''
)

# Generated at 2022-06-13 21:19:39.570793
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    list(choices)


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Force Basic or Digest authentication. By default HTTPie performs
    Basic auth when --auth is specified and Digest auth otherwise.

    '''
)


#######################################################################
# General
#######################################################################

verbosity = parser.add_argument_group(title='Verbosity')

verbosity.add_argument(
    '--traceback',
    default=False,
    action='store_true',
    help='''
    Print exception traceback should one occur.

    '''
)


# Generated at 2022-06-13 21:19:48.292411
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    ))


# Generated at 2022-06-13 21:20:03.251915
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'kerberos' not in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Currently supported:

    ''' + '\n'.join(
        '{0} {1}'.format(name, plugin_manager.get_auth_plugin_class(name).help)
        for name in sorted(plugin_manager.get_auth_plugin_mapping())
    ) + '''

'''
)

# Generated at 2022-06-13 21:20:13.956876
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = list(_AuthTypeLazyChoices())
    assert auth_type_lazy_choices == [
        'basic',
        'digest',
        'hawk',
        'ntlm',
    ]

auth_type = auth.add_argument(
    '--auth-type',
    default='basic',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used:

    {list_auth_plugins()}

    ''',
)


# ``requests.request`` keyword arguments.

# Support for http:// and https:// prefixes.
# Required so that ``requests.request`` does not complain.


# Generated at 2022-06-13 21:20:22.326114
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in auth_type_lazy_choices
    assert 'basic' in auth_type_lazy_choices
    assert 'hawk' in auth_type_lazy_choices

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify the authentication mechanism to be used.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help=f'''
    If set, do not attempt to issue an initial challenge to obtain the
    scheme-specific response.

    '''
)
auth.add_

# Generated at 2022-06-13 21:20:29.800266
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping())

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    type=AuthCredentials.validate_auth_type,
    default=None,
    metavar='TYPE',
    help='''
    The auth mechanism to be used. Available types:

    {auth_types}

    '''.format(
        auth_types='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(sorted(_AuthTypeLazyChoices())), 60)
        ).strip()
    )
)

# Generated at 2022-06-13 21:20:35.113585
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'test_auth_plugin' in _AuthTypeLazyChoices()
    assert 'non_existing_plugin' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:37.868781
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'Basic' in choices
    assert 'Digest' in choices
    assert 'foo' not in choices

# Generated at 2022-06-13 21:20:50.032228
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(
        sorted(plugin_manager.get_auth_plugin_mapping().keys())
    )

AUTH_PLUGIN_TYPES = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default=None,
    choices=AUTH_PLUGIN_TYPES,
    metavar='TYPE',
    help='''
    Use the specified authentication mechanism.

    The following authentication types are available:

    {0}
    '''
    .format('\n'.join(
        '{0}{1}'.format(8 * ' ', line.strip())
        for line in wrap(', '.join(sorted(AUTH_PLUGIN_TYPES)), 60)
    ).strip())
)

################################

# Generated at 2022-06-13 21:21:03.854334
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import_plugins()
    available_auth_types = _AuthTypeLazyChoices()
    assert(DEFAULT_AUTH_PLUGIN_NAME in available_auth_types)
    assert(not 'foobar' in available_auth_types)
    assert(len(list(available_auth_types)) == 1)

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication plugin type.
    The default depends on the hostname.
    '''
)


# Generated at 2022-06-13 21:21:14.915333
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    A = _AuthTypeLazyChoices()
    assert 'basic' in A
    assert 'Basic' in A
    assert 'BASIC' in A
    assert 'Digest' in A
    assert 'digest' in A
    assert 'DIGEST' in A

auth.add_argument(
    '--auth-type',
    # We don't want to import requests.auth, so we prefix choices with _.
    default='_httpie_basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication type to be used. Note that these values correspond to the
    Python names for requests auth classes, for example, Basic and Digest
    auth are _httpie_basic and _httpie_digest respectively.
    The default is _httpie_basic.

    '''
)

####################################################################

# Generated at 2022-06-13 21:21:27.762012
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism to be used.

    By default (i.e., when this option is not specified), HTTPie
    tries to determine the auth mechanism from the HTTP response
    (i.e., it will use Basic if the server responds with a 401
    status code, or Digest if a 401 response includes the
    "WWW-Authenticate: Digest" header).

    ''',
)

# Generated at 2022-06-13 21:21:39.297538
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    type=parse_auth_type,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used
    (default: `{DEFAULT_AUTH_PLUGIN_NAME}`).

    ''',
)


#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:21:45.968547
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Default: basic.

    ''',
)
auth.add_argument(
    '--auth-single',
    default=False,
    action='store_true',
    help='''
    Prompt for and save a single set of credentials.

    '''
)
auth.add_argument(
    '--auth-private',
    default=False,
    action='store_true',
    help='''
    Don't save protected credentials to disk.

    '''
)

####################################################################

# Generated at 2022-06-13 21:21:47.607952
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices


# Generated at 2022-06-13 21:22:00.498661
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    import os
    import sys
    from httpie.plugins import plugin_manager
    from httpie.plugins.manager import AUTH_PLUGIN_PREFIX
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '../plugins/httpie_mock_auth_plugin/httpie_mock_auth_plugin.py'
    )
    plugin = plugin_manager.load_plugin(path)
    sys.modules[AUTH_PLUGIN_PREFIX + plugin.name] = plugin

# Generated at 2022-06-13 21:22:02.650977
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices


# Generated at 2022-06-13 21:22:15.539987
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'foo' not in choices


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Select the auth mechanism (if not specified, HTTPie tries to auto-detect
    it). The supported auth mechanisms are:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    Use the `http --debug` command to get more information about
    the auth plugin loading process.

    '''
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:22:18.742894
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:22:37.962309
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(
        ('basic', 'digest')
    )

auth.add_argument(
    '--auth-type',
    type=AuthCredentials,
    default=AuthCredentials('basic'),
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force Basic or Digest auth.

    By default, HTTPie tries to determine the auth type based on the provided
    username and password.

    '''
)

#######################################################################
# Request Options
#######################################################################

request_options = parser.add_argument_group(title='Request Options')


# Generated at 2022-06-13 21:22:38.891019
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:22:50.784274
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_types = _AuthTypeLazyChoices()
    assert 'basic' in auth_types
    assert 'custom' not in auth_types
    assert 'digest' in auth_types
    assert 'foo' not in auth_types
    assert sorted(auth_types) == ['basic', 'digest', 'hawk', 'ntlm']


# Generated at 2022-06-13 21:23:01.409728
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    iter(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force usage of the selected auth type (Basic, Digest).
    If not specified and --auth is given, it is guessed based on the user:pass
    input (Basic if empty password, Digest otherwise).

    '''
)
auth.add_argument(
    '--auth-type-info',
    action='store_true',
    default=False,
    # TODO: Fix this to be similar to `--help`.
    help='Show auth info'
)

# Generated at 2022-06-13 21:23:09.190462
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


AuthTypeLazyChoices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-type',
    choices=AuthTypeLazyChoices,
    help='''
    Force the specified authentication mechanism.

    By default, HTTPie tries to guess the authentication scheme
    based on the hostname.

    ''',
    dest='auth_type',
    default=None,
)
auth.add_argument(
    '--auth-type', '--auth-type',
    choices=AuthTypeLazyChoices,
    action=ExtendChoicesAction,
    help=argparse.SUPPRESS,
    dest='auth_type',
    default=None,
)

# Generated at 2022-06-13 21:23:18.646958
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type', '--auth-plugin',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify an authentication type to use. By default, HTTPie
    will try to detect the most suitable type.

    Available types:
      {0}

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

auth.add_argument(
    '--auth-no-challenge',
    default=False,
    action='store_true',
    help='''
    Disable challenge-response auth.

    ''',
)

#######################################################################
# Proxy
#######################################################################



# Generated at 2022-06-13 21:23:25.097467
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth_type = auth.add_mutually_exclusive_group()
auth_type.add_argument(
    '--auth-type', '-t',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of the auth plugin to use. The document root for the custom auth
    plugin is:

        {get_config_dir("auth")}

    This option is ignored when --auth or --auth-type are used.
    ''',
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:23:32.702012
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    metavar='{auth_type_choices}',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force Basic or Digest auth. This can be useful for Digest auth with servers
    that do not request it when Basic auth is enabled.

    Available options: {auth_type_choices}

    '''.format(
        auth_type_choices=', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    )
)

#######################################################################
#
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:23:36.705690
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(choices) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:23:40.400802
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'foo' not in choices

# Generated at 2022-06-13 21:24:03.413921
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_AuthTypeLazyChoices(), _AuthTypeLazyChoices)

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported values:

    {supported}

    When no --auth-type is specified and --auth is provided without
    a password (see above), HTTPie will prompt for the password.

    '''.format(
        supported=' '.join(sorted(plugin_manager.get_auth_plugin_mapping()))
    )
)

# Generated at 2022-06-13 21:24:13.103283
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_types = _AuthTypeLazyChoices()
    assert 'digest' in auth_types


auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism, e.g. Basic or Digest.

    By default, HTTPie will try to detect the authentication type by the
    provided credentials and automatically pick the plugin for the
    correct authentication type. This option can be used to override
    this autodetection.

    '''
)

auth.add_argument(
    '--auth-host',
    default=None,
    help='''
    Host to use for authentication.

    By default, the host of the request.

    '''
)
auth

# Generated at 2022-06-13 21:24:26.622919
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == sorted(
        _AuthTypeLazyChoices()
    )


auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    help=f'''
    The specific authentication mechanism to be used. Must be one of
    {_AuthTypeLazyChoices()}. If not specified, the default is
    to try them all. See AUTH PLUGINS section below for more details.

    '''
)
auth.add_argument(
    '--auth-endpoint',
    metavar='URL',
    help='''
    The authentication server URL. Only used with authentication plugins.

    '''
)

# Generated at 2022-06-13 21:24:36.451358
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    atlc = _AuthTypeLazyChoices()
    assert 'basic' in atlc
    assert 'digest' in atlc
    assert 'hawk' in atlc
    assert 'oauth1' in atlc
    assert 'multipass' in atlc
    assert 'foo' not in atlc

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified authentication plugin.

    If no type is provided, then the plugin is guessed from the provided URL.
    I.e., if the URL starts with https://, then Digest auth is used by default;
    otherwise, Basic auth is used.

    ''',
)

#######################################################################
# Cookies
#######################################################################

# Generated at 2022-06-13 21:24:44.084982
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # before even "main" called
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_choices
    assert 'digest' in auth_type_choices
    assert 'AlwaysFail' not in auth_type_choices
    assert 'basic' in list(auth_type_choices)


auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_TYPE,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin (e.g., "digest").

    '''
)



# Generated at 2022-06-13 21:24:44.708182
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    next(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:24:56.589162
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism. Default is "auto", which causes the
    client to attempt to determine the best authentication type by trying
    various possibilities.

    Use "basic" to perform HTTP Basic Authentication, which sends the
    username and password over the network as cleartext.
    Albeit clear text, HTTP Basic authentication is quite secure when used over
    HTTPS.

    Use "digest" to perform HTTP Digest Authentication, which avoids sending
    passwords over the wire in cleartext.

    Use "plugin" to use an authentication plugin.

    '''
)
auth

# Generated at 2022-06-13 21:24:57.939978
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:59.403317
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__(item=None)

# Generated at 2022-06-13 21:25:11.277152
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    return list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default='auto',
    # TODO: 'default' is actually not a choice
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    The authentication mechanism. The default is "auto", which means
    it's determined based on the --auth option value.

    Plugins that register a ``get_auth_plugin()`` function are
    using this dynamic ``choices`` argument to expose their auth
    mechanism as a choice.
    '''
)

#######################################################################
# SSL
#######################################################################

ssl_group = parser.add_argument_group(title='SSL Verification')

# Generated at 2022-06-13 21:25:49.366339
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == []
    from HTTPie.compat import OrderedDict
    plugin_manager.auth_plugin_mapping = OrderedDict([
        ('A', 'b'),
        ('c', 'd')
    ])
    assert list(_AuthTypeLazyChoices()) == ['A', 'c']
    del plugin_manager.auth_plugin_mapping
AuthTypeLazyChoices = _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:51.664768
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    return 'basic' in lazy_choices

# Generated at 2022-06-13 21:26:00.501492
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hawk' in _AuthTypeLazyChoices()
    assert 'oauth1' in _AuthTypeLazyChoices()
    assert 'ntlm' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:26:04.520102
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    dummy_plugin_manager = PluginManager('HTTPie.plugins.auth')
    dummy_AuthTypeLazyChoices = _AuthTypeLazyChoices()
    assert list(iter(dummy_AuthTypeLazyChoices)) == sorted(
        dummy_plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:26:20.746461
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    By default, HTTPie tries to guess the authentication type by looking at
    the Credentials.

    ''',
)


# Generated at 2022-06-13 21:26:33.463578
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(plugin_manager.get_auth_plugin_mapping()) == list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    metavar='METHOD',
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Set the authentication method.

    ''',
)

#######################################################################
# HTTPie
#######################################################################

# ``requests.request`` keyword arguments.
httpie = parser.add_argument_group(title='HTTPie Options')

httpie.add_argument(
    '--follow',
    action='store_true',
    help='''
    Follow redirects.

    '''
)

# Generated at 2022-06-13 21:26:37.685110
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    try:
        import requests_oauthlib
    except ImportError:
        pass
    else:
        assert 'oauth1' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:53.917656
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping())


auth.add_argument(
    '--auth-type',
    metavar='',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication method to use. It can be one of:

        {plugin_list}

    The default is to try to autodetect the auth type by inspecting the
    provided credentials.

    '''.format(
        plugin_list='\n'.join(
            (8 * ' ') + line.strip() for line in
            wrap(' '.join(
                sorted(plugin_manager.get_auth_plugin_mapping().keys())
            ), 60)
        ).strip()
    )
)

# Generated at 2022-06-13 21:27:03.018566
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']


auth.add_argument(
    '--auth-type', '-t',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "basic".
    Use --auth-type=help to list all supported types.

    '''
)

# Generated at 2022-06-13 21:27:07.767435
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_Auth_Type.choices, _AuthTypeLazyChoices)
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == sorted(_Auth_Type.choices)


_Auth_Type = argparse.FileType('wt')
_Auth_Type.__name__ = '_Auth_Type'



# Generated at 2022-06-13 21:28:12.410144
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'plug' in _AuthTypeLazyChoices()
    assert 'non-existing' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:20.758108
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Authentication method.
    (default: {'auto'})

    The following methods are available:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

# Generated at 2022-06-13 21:28:22.885839
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:28:28.951597
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    it = iter(choices)
    # Consume the first item.
    next(it)
    # Get the next item.
    any(it)

# Generated at 2022-06-13 21:28:31.624346
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices.__iter__()


# Generated at 2022-06-13 21:28:39.759218
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    type=lambda s: s.lower(),
    default=requests.auth.HTTPBasicAuth,
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of HTTP authentication to use. This can be "basic",
    "digest", or a plugin name.

    '''
)
auth.add_argument(
    '--digest-auth',
    action='store_const',
    const=requests.auth.HTTPDigestAuth,
    dest='auth_type',
    help='''
    Use Digest authentication. Shortcut for --auth-type=digest.

    '''
)

# Generated at 2022-06-13 21:28:51.663254
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    for item in choices:
        assert item in choices

auth.add_argument(
    '--auth-type',
    metavar='BACKEND',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication method to be used. The default is "basic" and it supports
    arbitrary HTTP authentication schemes that can be registered via plugins.

    To see a list of plugins and their configuration options, run:

        $ http --auth-type=help
    '''
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:28:56.668831
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.output.writers.prettyjson import PrettyJSONWriter
    assert '__contains__' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:29:02.260634
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted([x for x in _AuthTypeLazyChoices()]) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

    # Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2022-06-13 21:29:06.561654
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()
    assert 'FCAuth' in _AuthTypeLazyChoices()
    assert 'HelpAuth' in _AuthTypeLazyChoices()
