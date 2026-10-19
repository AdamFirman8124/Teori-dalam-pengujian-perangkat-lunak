

# Generated at 2022-06-13 21:19:19.548582
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    items = set(_AuthTypeLazyChoices())
    for name, plugin in plugin_manager.get_auth_plugin_mapping().items():
        assert name in items
        assert plugin.name in items


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth plugin. See the "Authentication Plugins" section in the
    HTTPie docs (https://httpie.org/docs#authentication-plugins) for details.

    '''
)
auth.add_argument(
    '--auth-type-help',
    action=AuthPluginHelpAction,
    help='Show help for a specific auth plugin.',
)


#######################################################################
# SSL
#######################################################################


# Generated at 2022-06-13 21:19:32.552047
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    type=plugin_manager.load_auth_plugin,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Can be any of:

    {auth_types}

    Default is "auto".

    '''.format(
        auth_types='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(
                ', '.join(sorted(plugin_manager.get_auth_plugin_mapping())),
                60
            )
        ).strip(),
    )
)

# Generated at 2022-06-13 21:19:45.080903
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'plugin:' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '-t',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    type=AuthPlugin,
    help=(
        'Specify an authentication plugin ('
        'e.g., "digest" or "ntlm"). If not specified, '
        'the plugin is guessed based on the --auth provided.'
        'It can also be set to "no" to disable authentication completely. '
        'The "auto" type is by default.'
    )
)

# Generated at 2022-06-13 21:19:47.463617
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'auto' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:19:50.352852
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(
        ('basic', 'digest')
    ) == sorted(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:20:05.342196
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert list(_AuthTypeLazyChoices()) ==\
        ['basic', 'digest', 'aws-s3-bucket-name']

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    help='''
    The auth mechanism to use: {available_auth_types}.
    By default, HTTPie picks the first matching plugin.

    '''.format(
    available_auth_types='\n'.join(
        '{0}{1}'.format(8 * ' ', line.strip())
        for line in wrap(', '.join(sorted(_AuthTypeLazyChoices())), 60)
    ).strip(),
    )
)

# Generated at 2022-06-13 21:20:15.582478
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'http' in _AuthTypeLazyChoices()
assert 'http' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of HTTP authentication to use.
    If not specified, it will be inferred from the provided credentials.
    It can be one of the following:

    {help}

    '''.format(
        help=f'\n{_format_auth_types_help()}'
    )
)

#######################################################################
# Timeout
#######################################################################

timeout = parser.add_argument_group(title='Timeout')

# Generated at 2022-06-13 21:20:17.200721
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'none' in lazy_choices


# Generated at 2022-06-13 21:20:20.967150
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # type: () -> None
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'aws4' in _AuthTypeLazyChoices()
    assert 'non-existing-auth-type' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:20:32.033989
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    for choice in choices:
        assert choice in choices
    return True



# Generated at 2022-06-13 21:20:43.935721
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert choices.__contains__('basic')
    assert choices.__contains__('digest')
    # 'foo' should be a valid choice in tests.
    assert 'foo' in choices
    assert len(list(choices)) >= 3

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use. The default is "basic", which is
    usually fine unless the server requires a different one, such as "digest".
    To find out what plugins are available, run:

         $ http --debug

    ''',
)

# Generated at 2022-06-13 21:20:52.377497
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)
    # On a system without any auth plugin installed, an empty list is expected.
    assert [] == [iter_item for iter_item in choices]

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force usage of a specified authentication plugin. If not specified,
    HTTPie will try to determine the design of the auth system by looking
    at the authentication challenge from the server.

    ''',
)

# Generated at 2022-06-13 21:21:05.042210
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices



# Generated at 2022-06-13 21:21:13.518841
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    class Baf(Exception):
        pass

    def mock_get_auth_plugin_mapping(self, *args, **kwargs):
        raise Baf()

    _mock_get_auth_plugin_mapping = mock_get_auth_plugin_mapping
    try:
        plugin_manager.get_auth_plugin_mapping = \
            _mock_get_auth_plugin_mapping
        assert 'basic' not in _AuthTypeLazyChoices()
    finally:
        plugin_manager.get_auth_plugin_mapping = \
            _mock_get_auth_plugin_mapping



# Generated at 2022-06-13 21:21:15.686252
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:22.204767
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)
    assert all(
        choice
        in choices
        for choice
        in sorted(plugin_manager.get_auth_plugin_mapping().keys())
    )

# Generated at 2022-06-13 21:21:23.971397
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:36.537820
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used. Only relevant if --auth
    (or an authorization plugin) is used.

    The {DEFAULT_AUTH_PLUGIN_NAME} plugin is enabled by default.

    Use `http --debug' to see a list of all available authentication plugins.

    '''
)

# Generated at 2022-06-13 21:21:44.697439
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# patches
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose the auth mechanism. The default is to autodetect it.

    ''',
)
auth.add_argument(
    '--auth-no-challenge', '-A',
    action='store_true',
    default=False,
    help='''
    Disable HTTP authentication challenge (Basic or Digest). By default, HTTPie
    automatically enters interactive mode for authentication challenges.

    '''
)

# Generated at 2022-06-13 21:21:46.179746
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

# Generated at 2022-06-13 21:22:05.456208
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choice = _AuthTypeLazyChoices()
    # pretty much as
    # return 'basic' in plugin_manager.get_auth_plugin_mapping()
    assert 'basic' in choice
    assert 'abc' not in choice


auth.add_argument(
    '--auth-type',
    default=AUTH_PLUGIN_MAP[AUTH_PLUGIN_DEFAULT],
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.
    The default is {AUTH_PLUGIN_DEFAULT}.

    The following types are available:

    {auth_plugin_help}
    '''
).completer = ChoicesCompleter(
    plugin_manager.get_auth_plugin_mapping().keys()
)


# Generated at 2022-06-13 21:22:18.914000
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.auth.plugins import _DummyDigestAuthPlugin
    assert 'digest' in plugin_manager.get_auth_plugin_mapping()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    plugin_manager.unregister(_DummyDigestAuthPlugin)
    assert 'digest' not in _AuthTypeLazyChoices()
    plugin_manager.register(_DummyDigestAuthPlugin)


# Generated at 2022-06-13 21:22:20.506452
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert 'Basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:22:23.930476
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert choices.__contains__('basic')
    assert choices.__contains__('digest')
    assert not choices.__contains__('foo')


# Generated at 2022-06-13 21:22:35.300447
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices



# Generated at 2022-06-13 21:22:37.685995
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('foo')

# Generated at 2022-06-13 21:22:41.225893
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    AUTH_TYPES = _AuthTypeLazyChoices()
    assert list(AUTH_TYPES) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))



# Generated at 2022-06-13 21:22:52.173411
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an authentication plugin. Enter "?" to view the full list. The
    default plugin is {default}.

    '''.format(
        default=DEFAULT_AUTH_PLUGIN,
    )
)

# authentication-related ``requests.request`` keyword arguments


# Generated at 2022-06-13 21:23:00.698440
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=plugin_manager.load_auth_plugin,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin (e.g., "digest").
    Use "http --auth-type=digest --help" to list its options.
    '''
)

# ``requests.request`` keyword arguments.
auth_plugin_options = parser.add_argument_group(
    title='Authentication Options',
)

# Generated at 2022-06-13 21:23:07.790767
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    for auth_type in lazy_choices:
        assert auth_type in plugin_manager.get_auth_plugin_mapping()

auth.add_argument(
    '--auth-type', '--auth-plugin',
    metavar='TYPE',
    default=AuthCredentials.DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication plugin to use.

    Use ``-a TYPE:help`` to show the help for the plugin.
    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')



# Generated at 2022-06-13 21:23:23.495212
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'kerberos', 'ntlm']

# Generated at 2022-06-13 21:23:24.477770
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices().__iter__()

# Generated at 2022-06-13 21:23:31.783831
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import httpie.plugins.builtin
    import httpie.plugins.generic
    import httpie.plugins.digest
    import httpie.plugins.ntlm
    from httpie.config import PluginManager
    from httpie.cli.argtypes import AuthCredentials

    pm = PluginManager()
    lazy_choices = _AuthTypeLazyChoices()
    assert list(lazy_choices) == sorted(
        ['digest', 'generic', 'ntlm']
    )
    assert 'digest' in lazy_choices
    assert 'ntlm' in lazy_choices


auth_plugin = parser.add_argument_group(title='Authentication Plugin')

# Generated at 2022-06-13 21:23:38.137300
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__(): # noqa
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest-md5', 'gss-negotiate']

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose the authentication method. By default, the authentication method is
    inferred from the --auth option value.

    ''',
)
auth.add_argument(
    '--auth-verify',
    dest='auth_verify',
    default=True,
    action='store_true',
    help='''
    Verify(by default)/disable the SSL certificate when sending a request with
    HTTPie over HTTPS with Basic or Digest auth. Disable the verification by
    using --auth-verify=no.

    '''
)

# Generated at 2022-06-13 21:23:50.315334
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    ) == sorted(list(_AuthTypeLazyChoices()))



# Generated at 2022-06-13 21:23:53.907670
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )



# Generated at 2022-06-13 21:24:02.809121
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())
    assert 'digest' in _AuthTypeLazyChoices()

auth_type = auth.add_argument(
    '--auth-type',
    default=plugin_manager.get_default_auth_plugin_name(),
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication handler to use.

    For more details, run:

        $ http --auth-type [PLUGIN_NAME] --help

    '''
)

# Generated at 2022-06-13 21:24:08.530253
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hawk' in _AuthTypeLazyChoices()
    assert 'oauth1' in _AuthTypeLazyChoices()
    assert 'ignored_plugin' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:23.006685
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    # Since this is a sorted list we can just check
    # if it starts and ends with the expected values
    assert 'basic' in choices
    assert 'auto' in choices
    assert 'aws4' in choices


# Generated at 2022-06-13 21:24:34.366091
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(list(plugin_manager.get_auth_plugin_mapping().keys()))

_auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()


# Generated at 2022-06-13 21:25:04.409225
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices1 = _AuthTypeLazyChoices()
    assert 'basic' in choices1

# Generated at 2022-06-13 21:25:13.532565
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == list(choices)


# Generated at 2022-06-13 21:25:20.850359
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    items = _AuthTypeLazyChoices()
    for item in items:
        assert item in items


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use TYPE authentication. Available types:

        {auth_types}

    '''.format(
        auth_types='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(_AuthTypeLazyChoices()), 60)
        ).strip()
    )
)


# Generated at 2022-06-13 21:25:24.279847
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    expected_iter = iter(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    actual_iter = iter(_AuthTypeLazyChoices())
    assert set(actual_iter) == set(expected_iter)

# Generated at 2022-06-13 21:25:35.305204
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(sorted(_AuthTypeLazyChoices())) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    dest='auth_plugin_name',
    help='''
    The authentication mechanism to be used. Run 'http --auth-type-help'
    to print help on all available authentication types. The default
    authentication mechanism is basic.

    ''',
)

auth.add_argument(
    '--auth-type-help',
    nargs=0,
    action=AuthTypeHelpAction,
    help='''
    Print help on available authentication types.

    ''',
)

#######################################################################
# Timeouts and retries
#######################################################################

# Generated at 2022-06-13 21:25:37.343469
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:25:42.627723
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'Basic' in auth_type_lazy_choices
    assert 'Digest' in auth_type_lazy_choices
    assert 'NoSuchAuthPlugin' not in auth_type_lazy_choices


# Generated at 2022-06-13 21:25:52.977695
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type', '-t',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported:

        basic, digest

    '''
)

auth.add_argument(
    '--auth-endpoint',
    help='''
    The authentication backend endpoint.

    It defaults to /.

    '''
)

#######################################################################
#  HTTPS, proxies, and common options
#######################################################################

https_proxy = parser.add_argument_group(title='HTTPS, Proxies, and Common Options')

# Generated at 2022-06-13 21:26:04.922970
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    metavar='AUTH_TYPE',
    default=UNSET,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specifies non-standard HTTP authentication type (plugin).
    Use `{CLI_CONFIG_FILE_PATH}' with the `auth-plugins' section to register
    your own.

    Available auth types:

        {list(plugin_manager.get_auth_plugin_names())}

    '''
)

#######################################################################
# HTTP specific options.
#######################################################################

http_options = parser.add_argument_group(title='HTTP Options')


# Generated at 2022-06-13 21:26:20.864556
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    '''
    This method tests whether items in the
    _AuthTypeLazyChoices class, which are the names of plugins registered in the
    ``plugin_manager`` module, are sorted.
    '''
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(list(choices))
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Plugin used to perform authentication.

    If not specified, try to guess it based on --auth credentials.

    '''
)

# Generated at 2022-06-13 21:27:19.572529
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'auto' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:27:27.760566
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth_plugin_type = auth.add_mutually_exclusive_group(required=False)

auth_plugin_type.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication extension to use. By default, the appropriate
    authentication method will be chosen automatically.

    If you experience any problems with auto-detection, try setting this
    explicitly.

    The available authentication extensions are:
    {auth_plugins}

    '''.format(auth_plugins=plugin_manager.get_auth_plugins_doc())
)

#######################################################################
# Proxy
####################################################################

# Generated at 2022-06-13 21:27:35.353784
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified auth plugin. Use `http --help-auth` to list all auth
    plugins.

    ''',
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')
ssl.add_argument(
    '--verify',
    action='store_true',
    help='''
    Verify SSL certificates.

    Note that this setting can be overridden by the `HTTPIE_SSL_VERIFY`
    environment variable.

    '''
)
cert = ssl.add_mutually_

# Generated at 2022-06-13 21:27:37.520910
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'not-available' not in choices

# Generated at 2022-06-13 21:27:43.853060
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert(len([x for x in _AuthTypeLazyChoices()]) > 0)


auth.add_argument(
    '--auth-type',
    default=AUTH_PLUGIN_MAP[DEFAULT_AUTH_PLUGIN],
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication plugin to be used.

    '''
)

# Generated at 2022-06-13 21:27:57.658443
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    try:
        for choice in _AuthTypeLazyChoices():
            assert choice in plugin_manager.get_auth_plugin_mapping()
    except Exception as e:
        print(e)

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help='''
    Authentication type to use. The default, auto, tries to determine
    the auth type from the URL. Otherwise, the following can be used:

        {choices}

    '''.format(
        choices=', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))
    )
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:28:04.688033
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. It's a shortcut for the
    --auth-plugin option.

    ''',
)

# Generated at 2022-06-13 21:28:08.569599
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:18.377167
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    help='''
    The authentication mechanism to be used. If not specified, the plugin with
    the highest priority is used. Must be one of:

    ''' + indent(
        ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
        8
    )
)

auth.add_argument(
    '--auth-plugin',
    choices=plugin_manager.get_auth_plugin_names(),
    help=SUPPRESS
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:28:33.179354
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_AuthTypeLazyChoices(), list)

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism, when it cannot be inferred.

    The authentication mechanism used is determined by the auth plugin and
    by the --auth option. If the former is specified, the latter is required.

    ''',
)

# ``requests.request`` keyword arguments.
auth_plugin_options = parser.add_argument_group(
    title='Authentication Plugin Options'
)
