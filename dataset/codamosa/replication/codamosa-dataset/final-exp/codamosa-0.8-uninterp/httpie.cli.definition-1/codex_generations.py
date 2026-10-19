

# Generated at 2022-06-13 21:19:22.663272
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    plugin_manager.get_auth_plugin_mapping().pop('digest')
    assert 'digest' not in _AuthTypeLazyChoices()
    plugin_manager.get_auth_plugin_mapping()['digest'] = 'dummy value'

_auth_type_choices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=None,
    choices=_auth_type_choices,
    help='''
    Specify a custom auth plugin module (e.g., "myplugin").

    '''
)


# Generated at 2022-06-13 21:19:25.340395
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:19:37.963387
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The name of an authentication plugin to use.
    Run `http --debug --plugins' to see a list of available plugins.

    This argument is required if you want to use the generic `--auth' argument
    with an non-Basic auth scheme like Digest. It is also useful when using
    plugins like OAuth1.0a where some extra steps are required to get the
    authentication credentials.

    For example, to use the Digest auth plugin:

        http --auth-type=digest -a username:password https://httpbin.org/digest-auth/auth/user/pass

    '''
)

# Generated at 2022-06-13 21:19:40.553973
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices
    assert 'basic' in choices
    assert 'non-existing' not in choices

# Generated at 2022-06-13 21:19:41.671515
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())



# Generated at 2022-06-13 21:19:49.521373
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    foo_auth_plugin = plugin_manager.get_auth_plugin_mapping()['foo-auth'] = object()
    with patch.dict(HTTPie.plugins.__dict__,
                    {'_auth_types': _AuthTypeLazyChoices()}):
        assert sorted(HTTPie.plugins._auth_types) == ['foo-auth']
    assert 'foo-auth' not in plugin_manager.get_auth_plugin_mapping()
del test__AuthTypeLazyChoices___iter__


# Generated at 2022-06-13 21:19:50.297613
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert AuthedSession()

# Generated at 2022-06-13 21:19:56.078448
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'Basic' in auth_type_lazy_choices
    assert 'Digest' in auth_type_lazy_choices

    assert 'Non existing auth' not in auth_type_lazy_choices


# Generated at 2022-06-13 21:20:10.408508
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_types = _AuthTypeLazyChoices()
    assert len(list(auth_types)) == len(plugin_manager.get_auth_plugin_mapping())


auth.add_argument(
    '--auth-type',
    metavar='BACKEND_NAME',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication method.
    By default HTTPie tries Basic and then Digest.

    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:20:21.134663
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_choices
    assert 'digest' in auth_choices
    assert sorted(list(auth_choices)) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices()
)
auth.add_argument(
    '--auth-host',
    help='''
    Provide a host name that will be used in HTTP Basic and Digest
    Authentication. It supersedes the one used in the request URL.

    This option is helpful when the host of the request is an IP address
    (which is not accepted by some authentication providers).

    '''
)

#######################################################################
# Timeouts
#######################################################################

timeout = parser.add_argument_group

# Generated at 2022-06-13 21:20:37.384669
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest', 'hawk', 'ntlm', 'oauth1', 'oauth2', 'aws'
    ]
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    dest='auth_type',
    help='''
    The authentication mechanism to be used. By default, HTTPie detects
    the auth type from the URL or from the previous response.
    When set, it overrides the detected value.

    To see the list of supported authentication plugins, run:

        $ http --debug

    To install additional plugins, use:

        $ pip install httpie-<PLUGIN>

    ''',
)

#######################################################################
# HTTP(S) Proxy
#######################################################################

# Generated at 2022-06-13 21:20:49.825185
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices())

AUTH_TYPE_LAZY_CHOICES = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    metavar='TYPE',
    choices=AUTH_TYPE_LAZY_CHOICES,
    help='''
    Specify a custom HTTP authentication plugin.

    Use with `--auth` to specify the username and password.

    ''',
)

auth.add_argument(
    '--ignore-netrc',
    action='store_true',
    help='''
    Ignore the Netrc file (~/.netrc) for authentication info.
    To force the use of the Netrc file, use --netrc.

    ''',
)


# Generated at 2022-06-13 21:20:51.959926
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    a = _AuthTypeLazyChoices()
    assert list(a) == ['basic', 'digest']

# Generated at 2022-06-13 21:21:04.604446
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from os.path import dirname, abspath
    import pkg_resources
    from httpie import __version__
    plugins_dir = abspath(dirname(dirname(dirname(__file__))))
    pkg_resources.working_set.add_entry(plugins_dir)
    pkg_resources.working_set.add_entry(abspath(dirname(dirname(__file__))))
    if pkg_resources.get_distribution('httpie-aws').version != __version__:
        pytest.skip('httpie-aws must be installed to run test')

    import httpie.plugins.builtin
    import httpie_aws
    auth_choices = _AuthTypeLazyChoices()
    assert 'aws' in auth_choices
    assert 'aws4' in auth_choices
    # Test for

# Generated at 2022-06-13 21:21:08.457790
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'plugin-name' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:19.145916
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(_AuthTypeLazyChoices()) == sorted(['basic', 'digest', 'hawk'])


auth.add_argument(
    '--auth-type',
    default=None,
    help='Authentication plugin',
    choices=_AuthTypeLazyChoices(),
)
auth.add_argument(
    '--proxy-auth', '-A',
    default=None,
    metavar='USER[:PASS]',
    help='''
    Same as --auth but applied to the proxy URL, if present.
    If only the username is provided (-a username), HTTPie will prompt
    for the password.

    '''
)

# Generated at 2022-06-13 21:21:29.531014
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """Test _AuthTypeLazyChoices class"""
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:21:40.846715
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for item in _AuthTypeLazyChoices():
        pass

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth type. Available plugins: {0}.

    '''.format(
        ', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    ),
)

#######################################################################
# Custom headers
#######################################################################

headers = parser.add_argument_group(title='Custom headers')


# Generated at 2022-06-13 21:21:47.421175
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for auth_type in _AuthTypeLazyChoices():
        assert auth_type in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Auth plugin to use. ``auto`` tries to determine the auth plugin to use
    based on the provided credentials (the --auth argument).
    {plugins}
    '''.format(
        plugins=plugin_manager.get_plugin_help('auth', indent=6)

    )
)

#######################################################################
# Cookies
#######################################################################


# Generated at 2022-06-13 21:21:48.451744
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('basic')


# Generated at 2022-06-13 21:22:03.385673
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['digest']


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    Use the specified authentication plugin. The default is "auto", which
    selects the plugin based on the provided credentials.

    To see a list of available authentication plugins, run `http --help-auth`.

    '''
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:22:16.476898
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=AuthCredentials,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication scheme to use.

    The default scheme is "basic" which, in combination with --auth, sends
    the credentials in the HTTP "Authorization" header.

    Available types: {plugin_manager.get_auth_plugin_mapping().keys()}

    '''
)

# Generated at 2022-06-13 21:22:20.555197
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'the_auth_type_that_does_not_exist' not in lazy_choices



# Generated at 2022-06-13 21:22:29.152326
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    valid_auth_types = {'basic', 'digest', 'custom', 'foo'}
    with plugin_manager.context() as pm:
        pm.register_auth_plugin('foo', mock.Mock(auth_type='foo'))
        assert list(_AuthTypeLazyChoices()) == sorted(valid_auth_types)
test__AuthTypeLazyChoices___iter__.apply = lambda _: None


auth.add_argument(
    '--auth-type', '--auth-plugin',
    default=None,
    help='''
    Use the specified HTTPie auth plugin.

    By default, HTTPie will try to detect the auth plugin based on the
    --auth option. You can use this option to force a different one.

    '''
)

# Generated at 2022-06-13 21:22:40.389822
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    assert sorted(list(_AuthTypeLazyChoices())) == \
        sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    dest='auth_type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    ''',
)

#######################################################################
# Miscellaneous
#######################################################################

miscellaneous = parser.add_argument_group(title='Miscellaneous')


# Generated at 2022-06-13 21:22:45.004592
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'DigestAuth' in auth_type_lazy_choices
    assert 'NonExisting' not in auth_type_lazy_choices

# Generated at 2022-06-13 21:22:46.355055
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:22:54.766573
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy = _AuthTypeLazyChoices()
    assert 'basic' in lazy
    assert sorted(lazy) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Which authentication scheme to use for the request.
    If set to "{AUTO_AUTH_PLUGIN}", HTTPie will try to guess.

    '''
)

# Generated at 2022-06-13 21:23:02.993737
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():

    # mocks
    class MockedPluginManager:
        def get_auth_plugin_mapping(self):
            return {'mock-plugin-type-1': 'mock-plugin-1', 'mock-plugin-type-2': 'mock-plugin-2'}

    import httpie.plugins
    real_plugin_manager = httpie.plugins.plugin_manager
    httpie.plugins.plugin_manager = MockedPluginManager()

    # action
    choices = list(_AuthTypeLazyChoices())

    # asserts
    assert choices == ['mock-plugin-type-1', 'mock-plugin-type-2']

    # cleanup
    httpie.plugins.plugin_manager = real_plugin_manager


auth_type_choices = _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:23:15.799517
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert choices.__contains__('basic')
    assert 'basic' in choices
    assert choices.__contains__('digest')
    assert 'digest' in choices
    assert choices.__contains__('whatever') is False
    assert 'whatever' not in choices
    assert sorted(['basic', 'digest']) == sorted(list(choices))


# ``requests.auth.HTTPBasicAuth`` keyword arguments.

# Generated at 2022-06-13 21:23:30.061747
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:23:37.008237
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(iter(_AuthTypeLazyChoices()))

# Value of the ``choices`` keyword argument in the next call of ``add_argument``
AuthTypeLazyChoices = _AuthTypeLazyChoices()


# ``requests.auth.HTTPBasicAuth`` keyword arguments.

# Generated at 2022-06-13 21:23:41.412347
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Default: "auto". A string specifying the authentication mechanism to be
    used.

    Available types:

        {', '.join(plugin_manager.get_auth_plugin_mapping().keys())}

    The "auto" type is special: If the URL contains credentials, then basic
    auth is used, else if --auth is set the digest auth is used, else no
    authentication is used.

    '''

)

# Generated at 2022-06-13 21:23:53.470553
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Override the automatically inferred HTTP auth type.

    {plugin_manager.format_plugin_info(
        group='auth',
        info_type='shorthelp'
    )}

    '''
)

#######################################################################
# HTTP method
#######################################################################

# ``requests.request`` keyword arguments.
method = parser.add_argument_group(title='HTTP method')

# Generated at 2022-06-13 21:24:02.537485
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(list(_AuthTypeLazyChoices())) == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin module
    (e.g. path.to.auth_plugin) or one of the built-in plugins:

      {auth_types}

    '''.format(
        auth_types=''.join(sorted(
            c for c in _AuthTypeLazyChoices()
            if c not in HIDDEN_AUTH_PLUGINS
        ))
    )
)

#######################################################################
# Miscellaneous.
#######################################################################

miscellaneous = parser.add_argument_group(title='Miscellaneous')
miscellaneous

# Generated at 2022-06-13 21:24:09.986262
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism.

    ''',
)
auth.add_argument(
    '--auth-plugin',
    metavar='PLUGIN_NAME',
    default=None,
    help='''
    The name of the auth plugin to use.

    ''',
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:24:11.466862
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert AUTH_PLUGIN_NAME in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:25.679096
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    import httpie.plugins
    _AuthTypeLazyChoices()

_authtype_lazy_choices = _AuthTypeLazyChoices()

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_authtype_lazy_choices,
    help='''
    The authentication scheme to be used.

    ''',
)

# Generated at 2022-06-13 21:24:37.748810
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert 'basic' in _AuthTypeLazyChoices
    assert 'foo' not in _AuthTypeLazyChoices
    assert list(_AuthTypeLazyChoices) == ['basic', 'digest', 'hawk', 'jwt']

auth_type_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=auth_type_choices,
    # TODO: generate help dynamically
    help='''
    The auth mechanism to be used. The following auth types are supported:

    * basic: Basic HTTP auth.
    * digest: Digest HTTP auth.
    * hawk: Hawk HTTP auth.
    * jwt: JWT HTTP auth.

    ''',
)

#######################################################################
# HTTP(S)

# Generated at 2022-06-13 21:24:51.498525
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

_AuthTypeLazyChoices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices,
    help='''
    The authentication mechanism to be used.

    '''
)

#######################################################################
# HTTP method
#######################################################################

method = parser.add_argument_group(title='Request')

# Generated at 2022-06-13 21:25:14.015781
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # No plugins are loaded at the time of testing the core.
    assert [item for item in _AuthTypeLazyChoices()] == []
    plugin_manager.load_installed_plugins()
    assert [item for item in _AuthTypeLazyChoices()] \
        == ['basic', 'digest']

# Used by auth plugin.
AUTH_TYPES = _AuthTypeLazyChoices()

# Used by completer.py.
_auth_plugin_mapping = None



# Generated at 2022-06-13 21:25:21.096656
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.plugins import builtin as builtin_plugins

    assert iter(_AuthTypeLazyChoices()) == iter(sorted(builtin_plugins.__all__))



auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.
    Possible values depend on the installed plugins.

    Use "http --debug" to see a list of all enabled plugins
    and their default configuration.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    Prevent request from automatically sending a Basic auth
    challenge response.

    '''
)

# Generated at 2022-06-13 21:25:29.447834
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert len(list(_AuthTypeLazyChoices())) > 0

AuthType = _AuthTypeLazyChoices()

auth_plugin = parser.add_argument_group(title='Auth Plugin Options')

auth_plugin.add_argument(
    '--auth-type',
    dest='auth_type',
    metavar='AUTH_TYPE',
    choices=AuthType,
    default='auto',

    help=f'''
    Auth plugin to use. One of: {', '.join(AuthType)}.

    Plugin to use for handling HTTP authentication.
    By default, it's guessed from the URL, or auto-detected
    if the --auth flag is provided.

    '''
)

# Generated at 2022-06-13 21:25:37.980334
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Which authentication scheme to use.

    Either of the builtin schemes:

        {0}

    Or a registered plugin module name.

    '''.format('basic, digest')
)
auth.add_argument(
    '--auth-plugin',
    help='''
    The name of a plugin to use for a custom authentication scheme.
    Typically the name would be "httpie-<name>-auth" where <name> is the
    scheme.

    '''
)

# Generated at 2022-06-13 21:25:50.473880
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    old_names = set(choices.__iter__())
    plugin_manager.plugin_dir = 'tests/plugins/auth'
    new_names = set(choices.__iter__())
    assert new_names > old_names
    plugin_manager.plugin_dir = None


# Generated at 2022-06-13 21:26:03.877750
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    _AuthTypeLazyChoices()

auth_type = auth.add_argument(
    '--auth-type',
    metavar='',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default depends
    on the supplied credentials.

    '''
)
auth_type.completer = WordCompleter(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

# ``requests.auth.HTTPBasicAuth`` keyword arguments.

# Generated at 2022-06-13 21:26:20.127996
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'hawk',
                                            'netrc']

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified HTTP auth type.

    The following auth types are available:

    {auth_types}

    '''.format(auth_types=plugin_manager.get_plugin_help('auth'))
)

basic_auth = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:26:26.774069
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    plugin_manager.get_auth_plugin_mapping()
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'ntlm' in choices


_lazy_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_lazy_choices,
    help='''
    The authentication mechanism to be used.

    The default value is inferred based on the provided --auth
    information.

    ''',
)

# Generated at 2022-06-13 21:26:36.654629
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(_AUTH_TYPES)
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Available types:

        {auth_types}

    '''
).completer = ChoiceCompleter(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:26:38.029865
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:27:17.356579
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    for item in [
        'basic',
        'digest',
        'aws',
        'awsv4',
        'aws-sigv4',
        'kerberos',
        'hawk',
        'ntlm',
        'oauth1',
        'spnego',
    ]:
        assert item in lazy_choices

    assert 'yolo' not in lazy_choices


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Run an authentication helper to generate the value of --auth.
    Run `http --auth-type=TYPE --help` to learn more.
    '''
)

# Generated at 2022-06-13 21:27:26.490600
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    dest='auth_plugin_name',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The name of the HTTP authentication plugin.

    The supported authentication types are: {', '.join(
        sorted(plugin_manager.get_auth_plugin_mapping().keys()))}.

    You can also install plugins, see `http --help-plugins`.
    ''',
)


# Generated at 2022-06-13 21:27:34.901821
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    return list(_AuthTypeLazyChoices())

# help for positional argument "url" for method add_argument of
# class ArgumentParser.
# used for constructing help message for command line argument --auth-type
_url_helper = 'URL of the resource to be accessed.'



# Generated at 2022-06-13 21:27:41.861918
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'foo' not in lazy_choices
    assert '' not in lazy_choices
    assert 'basic' in lazy_choices

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use "plugin" to load a custom auth plugin from a Python module '''
         '''specified via --auth-plugin-module.
    ''',
)

auth.add_argument(
    '--auth-plugin-module',
    help='''
    If --auth-type=plugin, then this should specify the custom auth plugin
    module.
    ''',
)


# Generated at 2022-06-13 21:27:49.348515
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    AuthTypeLazyChoices=_AuthTypeLazyChoices()
    assert (AuthTypeLazyChoices.__contains__('digest'))


# Generated at 2022-06-13 21:27:59.441446
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    plugin_manager.get_auth_plugin_mapping()['ntlm']
    assert 'ntlm' in _AuthTypeLazyChoices()
    plugin_manager._loaded_plugins.clear()
    assert 'ntlm' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:05.677906
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from tests.compat import StringIO
    from httpie.plugins import builtin
    from httpie import inputs
    from httpie.cli import parser

    buf = StringIO()
    parser.print_help(file=buf)
    buf.seek(0)
    help_txt = buf.read()

    loaded_plugins = {
        'builtin': list(builtin.__all__)
    }
    BuiltinAuthPlugin = inputs.AuthCredentials(
        username="test",
        password="test",
        auth_type="builtin",
        args=['test', 'test']
    )

# Generated at 2022-06-13 21:28:14.678410
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type = _AuthTypeLazyChoices()
    assert '_AuthTypeLazyChoices' in auth_type
    assert 'basic' in auth_type
    assert 'basic' in auth_type

    assert sorted(auth_type) == sorted(['basic', 'digest'])



# Generated at 2022-06-13 21:28:18.548915
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:23.374355
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Setup
    choices = _AuthTypeLazyChoices()
    # Exercise
    # Verify
    assert iter(choices) is not None