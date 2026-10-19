

# Generated at 2022-06-13 21:19:10.425213
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'hawk', 'jwt']


# Generated at 2022-06-13 21:19:20.503306
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert list(choices) == ['digest']

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth plugin against which to authenticate.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    default=False,
    action='store_true',
    help='''
    Allow accessing pages that require authentication without actually
    passing any credentials. This is a shortcut for --auth=:

        http --auth=: :/protected/resource

    '''
)


#######################################################################
# Cookies.
#######################################################################

cookies = parser.add_argument_

# Generated at 2022-06-13 21:19:22.786192
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:19:36.488205
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    try:
        auth_type_lazy_choices = _AuthTypeLazyChoices()
    except:
        assert False

auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The auth mechanism to use. Supported mechanisms:

        {' '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

# Generated at 2022-06-13 21:19:48.855861
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'missing' not in _AuthTypeLazyChoices()
    assert sorted(_AuthTypeLazyChoices()) == ['basic', 'digest', 'hawk']

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Default: "basic".
    The auth mechanism to be used. Usually it's best to omit this.
    Supported values: {0}

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)

#######################################################################
# Timeouts
#######################################################################

# Generated at 2022-06-13 21:20:03.733594
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest-deprecated' in _AuthTypeLazyChoices()
    assert 'gssnegotiate' in _AuthTypeLazyChoices()
    assert 'aws-sig-v4' in _AuthTypeLazyChoices()
    assert 'aws-sig-v4-deprecated' in _AuthTypeLazyChoices()

    assert '__contains__' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:14.818739
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

auth_plugin = parser.add_argument_group(title='Authentication Plugin')

# Generated at 2022-06-13 21:20:22.597210
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    foo = _AuthTypeLazyChoices()
    assert 'basic' in foo
    import sys
    assert 'basic' in foo
    sys.modules['httpie.plugins.auth'] = None  # Simulate auth plugin failure.
    assert 'basic' not in foo
    raise SystemExit
test__AuthTypeLazyChoices___contains__()


# Generated at 2022-06-13 21:20:35.009240
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices())



# Generated at 2022-06-13 21:20:43.604563
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of authentication to use.

    Can be one of:

    {help_auth_plugins}

    '''.format(
        help_auth_plugins=plugin_manager.get_help('auth_plugin_help')
    )
)
auth.add_argument(
    '--auth-export',
    action='store_true',
    default=False,
    help='''
    Export the credentials to an auth plugin.

    '''
)

# Generated at 2022-06-13 21:21:00.297029
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert set(plugin_manager.get_auth_plugin_mapping().keys()) == set(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication handler. Can be a plugin name (e.g., "basic" or "digest")
    or "auto" (default; let HTTPie decide).

    If not set explicitly, the plugin is auto-detected if possible.

    {plugin_manager.detailed_plugin_listing()}

    '''
)

#######################################################################
# Timeouts
#######################################################################

timeouts = parser.add_argument_group(title='Timeouts')

# Generated at 2022-06-13 21:21:09.403461
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'bearer' in _AuthTypeLazyChoices() # Contains by default.


# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help='''
    Auth plugin to use. Set to "auto" to automatically detect the auth scheme
    from the URL, or to a string that identifies one of the built-in auth
    plugins:

    basic, digest, post, digest-post

    '''
)
auth.add_argument(
    '--auth-disable',
    action='store_true',
    help='''
    Disable any authentication.

    '''
)

# Generated at 2022-06-13 21:21:12.992419
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
try:
    _AuthTypeLazyChoices()['basic']
except TypeError:
    pass
else:
    raise AssertionError

# Generated at 2022-06-13 21:21:16.504312
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """Unit test for method __contains__ of class _AuthTypeLazyChoices."""
    lazy = _AuthTypeLazyChoices()
    assert 'digest' in lazy


# Generated at 2022-06-13 21:21:28.818183
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert BasicAuth.name in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Default: "basic".

    ''',
    metavar='TYPE'

)
for arg in plugin_manager.get_auth_plugin_args():
    auth.add_argument(arg, action='append')


#######################################################################
# HTTP method
#######################################################################
method = parser.add_argument_group(title='Request Method')

# Generated at 2022-06-13 21:21:40.277296
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Use the specified auth plugin, e.g., Basic or Digest.

    The default, {AUTH_PLUGIN_MAP}, is to try to auto-detect the auth type
    based on the provided credentials.

    The {AUTH_PLUGIN_MAP} plugin is used if the URL looks like a filesystem
    path, or if no credentials are given, and there is a netrc entry for the
    URL.

    '''
)

# Generated at 2022-06-13 21:21:41.782017
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == AUTH_PLUGIN_MAP.keys()

# Generated at 2022-06-13 21:21:42.762531
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert plugin_manager.get_auth_plugin_mapping().keys() == _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:21:52.035881
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism that is used.

    Current choices:
        {', '.join(_AuthTypeLazyChoices()) or None}

    Use the ``--plugins`` option to show available plugins.

    '''
)
auth.add_argument(
    '--auth-type-force',
    action='store_true',
    help='''
    Forces authentication even if authentication is not required.
    '''
)


#######################################################################
# Certificates
#######################################################################

certs = parser.add_argument_group(title='Certificates')


# Generated at 2022-06-13 21:22:03.566380
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify the authentication mechanism to be used. Available choices are:

        {', '.join(plugin_manager.get_auth_plugin_mapping().keys())}

    ''',
)

#######################################################################
# HTTPS, proxies
#######################################################################

https = parser.add_argument_group(title='HTTPS, proxies')



# Generated at 2022-06-13 21:22:23.131570
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()

auth_type_choices_validator = AuthTypeChoicesValidator('Auth type invalid.')

auth_type_help = f'''
    Select an authentication plugin. The default is "Basic".

    Available plugins:

        {plugin_manager.get_auth_plugin_mapping().keys()}

    To add a custom auth plugin, simply drop it into:

        {DEFAULT_AUTH_PLUGIN_DIR}

    '''

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    validator=auth_type_choices_validator,
    metavar='TYPE',
    help=auth_type_help,
)


# Generated at 2022-06-13 21:22:25.410328
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:22:35.862570
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    with open(PLUGIN_CONFIG_FILEPATH, 'w') as f:
        f.write(PLUGIN_CONFIG_BASIC_TEXT)
    from httpie import input
    input.KeyboardInterrupt = KeyboardInterrupt
    try:
        auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
        lazy_choices = _AuthTypeLazyChoices()
        assert 'basic' in auth_plugin_mapping
        assert 'basic' in lazy_choices
        assert 'WrongType' not in auth_plugin_mapping
        assert 'WrongType' not in lazy_choices
    finally:
        os.remove(PLUGIN_CONFIG_FILEPATH)

# Generated at 2022-06-13 21:22:48.289400
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = []
    assert len(choices) == 0
    with patch.dict('sys.modules', {'httpie import': 'placeholder'}):
        for choice in _AuthTypeLazyChoices():
            if choice in ['basic', 'digest']:
                choices.append(choice)
        assert len(choices) == 2

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used. By default, the most secure
    mechanism available is selected from: {', '.join(sorted(AUTH_PLUGINS))}.

    '''
)

# Generated at 2022-06-13 21:23:00.076080
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


_auth_type_validator = AuthTypeValidator(
    'Invalid authentication type. Valid types are: {0}'.format(
        ', '.join(_AuthTypeLazyChoices())
    )
)



# Generated at 2022-06-13 21:23:01.926781
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(choices) == sorted(plugin_manager.get_auth_plugin_mapping())


# Generated at 2022-06-13 21:23:09.481961
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    class_ = _AuthTypeLazyChoices()
    iter(class_)
    assert 'basic' in class_
    assert 'digest' in class_

auth_type_validator = AuthTypeValidator(
    'Invalid authorization type. Use "help auth" for more details.'
)


# Generated at 2022-06-13 21:23:11.747821
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == AUTH_PLUGIN_NAMES_AVAILABLE

# Generated at 2022-06-13 21:23:20.313554
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for choice in _AuthTypeLazyChoices():
        assert choice in plugin_manager.get_auth_plugin_mapping()

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='Use the specified auth plugin. Default: %(default)s'
)


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:23:26.946075
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for _ in _AuthTypeLazyChoices():
        pass

# The --auth-type option is hidden from the help output, but we need it
# for testing, so we keep it as a real option.
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help=argparse.SUPPRESS,
)

# Argument passed to the auth plugin.
auth_plugin_argument = parser.add_argument_group(title='Auth Plugin Options')

# Generated at 2022-06-13 21:23:47.241867
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(AuthPluginManager.available_auth_plugins) == sorted(list(_AuthTypeLazyChoices()))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=plugin_manager.DEFAULT_AUTH_PLUGIN,
    help=f'''
    Authentication plugin to use.
    Available plugins: {', '.join(map(repr, list(_AuthTypeLazyChoices())))}
    ''')

#######################################################################
# Timeouts.
#######################################################################

timeouts = parser.add_argument_group(title='Timeout')


# Generated at 2022-06-13 21:23:49.711243
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Figlet' in _AuthTypeLazyChoices()
assert test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:24:00.547304
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'basic' in choices
    assert 'plugin' in choices  # In case we have a plugin called 'plugin'.

auth.add_argument(
    '--auth-type',
    dest='auth_type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The type of auth to use:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    The default is "auto", which means HTTPie will first try to use Digest
    and then Basic if that fails or is not supported.

    '''
)


# Generated at 2022-06-13 21:24:04.098374
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert ['digest', 'ftp', 'ie', 'kerberos','negotiate','ntlm','scram','spnego','sql','wpad','wpas'] == [authType for authType in _AuthTypeLazyChoices()]

# Generated at 2022-06-13 21:24:13.363134
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom auth plugin from this list: {0}

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)

#######################################################################
# Install
#######################################################################

install = parser.add_argument_group(title='Install')


# Generated at 2022-06-13 21:24:26.775490
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    metavar='TYPE',
    default=DEFAULT_AUTH_PLUGINS[0],
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Authentication plugin to use, see `--auth-types' for built-in ones.
    The default plugin is {DEFAULT_AUTH_PLUGINS[0]}.

    '''
)

# Generated at 2022-06-13 21:24:36.660965
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(iter(_AuthTypeLazyChoices()))

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication method to use for request.
    Available builtin auth types are: digest, basic
    Available plugin auth types can be listed by running: http --auth-type-help
    Auth type "auto" is used by default.
    It will automatically choose the most secure auth type available
    The order is (most secure to least secure): digest -> basic
    '''
)
auth.add_argument(
    '--auth-type-help',
    default=False,
    action='store_true',
    help='Print available plugin authentication types and exit.'
)

# Generated at 2022-06-13 21:24:45.039395
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    metavar='SCHEME',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication method to be used.
    It can be one of:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))}

    Or a custom scheme of your own.

    '''
)

# Generated at 2022-06-13 21:24:46.559026
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:48.109364
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:05.814273
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert list(auth_type_lazy_choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:25:17.791859
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:25:27.684833
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    The default is to infer the authentication mechanism based
    on the provided credentials. Alternatively, the mechanism
    can be explicitly specified using this option.

    '''
)

# Generated at 2022-06-13 21:25:37.374189
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom auth plugin. The plugin name is a ``requests`` auth
    plugin name (e.g. digest) or a path to a custom auth plugin
    ('/path/to/plugin.py') or package name ('package.plugin_module.PluginClass')
    ''',
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:25:39.055847
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:25:40.645975
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert AuthCredentialsPlugin.NAME in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:42.820212
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:51.518731
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__(): assert list(_AuthTypeLazyChoices())

# auth.add_argument(
#     '--auth-type', '-t',
#     default=DEFAULT_AUTH_PLUGIN,
#     choices=_AuthTypeLazyChoices(),
#     help='''
#     The authentication plugin to be used.
#
#     ''',
# )

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')
ssl.add_argument(
    '--ssl',
    action='store_true',
    help='''
    Use SSL/HTTPS (default: False).
    '''
)

# Generated at 2022-06-13 21:26:04.552793
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(['digest', 'jwt'])


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth type to be used. Defaults to auto-detection.

    '''
)

# Generated at 2022-06-13 21:26:09.483893
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    for auth_plugin in plugin_manager.get_auth_plugin_mapping():
        assert auth_plugin in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:48.369285
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import pytest
    with pytest.raises(SystemExit):
        _AuthTypeLazyChoices()

_AUTH_TYPE_LAZY_CHOICES = _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:53.394031
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Bearer' in _AuthTypeLazyChoices()
    assert 'Hawk' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:02.869729
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()))


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='AUTH_TYPE',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    A plugin name for a custom authentication handler.
    ''',
)
auth_plugin_msg = (
    'HTTPie comes with several auth plugin. Check them out at: '
    'https://github.com/jakubroztocil/httpie-plugins'
)


#######################################################################
# SSL
#######################################################################

verify = parser.add_argument_group(title='SSL Verification')


# Generated at 2022-06-13 21:27:04.063691
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:27:07.280673
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'digest',
        'hawk',
        'jwt',
        'netrc',
        'ntlm',
        'oauth1',
    ]

# Generated at 2022-06-13 21:27:14.679749
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basicauth' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help=f'The authentication type to use. (default is auto) The available types are: {_AuthTypeLazyChoices()}'
)

auth.add_argument(
    '--auth-host',
    dest='auth_host',
    help='''
    The host to send authentication information to. The default is the host
    of the URL being requested.

    '''
)


# Generated at 2022-06-13 21:27:18.642101
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'foo' not in choices

# Generated at 2022-06-13 21:27:27.383164
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__(): assert 'basic' in _AuthTypeLazyChoices()

auth_plugin = auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. See the full list of supported
    types with: http --help-auth.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    default=False,
    action='store_true',
    help='''
    By default, HTTPie performs authentication challenges itself
    (like a regular browser), but this may not work for all scenarios.
    Specify this option to disable this behaviour, which will cause HTTPie
    to let the server handle the challenges.

    '''
)

#######################################################################
# SSL
################################

# Generated at 2022-06-13 21:27:35.173634
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = set(_AuthTypeLazyChoices())
    assert choices == set(plugin_manager.get_auth_plugin_mapping().keys())
_auth_type_lazy_choices = _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:46.094129
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(['basic', 'digest']) == set(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism to be used. The default is "basic" and other
    choices are "digest", "hmac" and an auth plugin name that you installed
    via pip.

    For example, this authenticates with a GitHub API token:

        $ pip install httpie-github-auth
        $ http --auth-type=github --auth='b4ab7...' https://api.github.com

    '''
)

#######################################################################
# Miscellaneous
#######################################################################


# Generated at 2022-06-13 21:28:52.500704
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The method to use for authentication. The default is {DEFAULT_AUTH_PLUGIN}.
    Available methods:

        {", ".join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    ''',
)

# Generated at 2022-06-13 21:28:59.117534
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping())
    assert 'Basic' in choices
    with pytest.raises(AssertionError):
        assert 'Bogus' in choices


# Generated at 2022-06-13 21:29:03.308231
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'fs' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:29:12.510428
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

