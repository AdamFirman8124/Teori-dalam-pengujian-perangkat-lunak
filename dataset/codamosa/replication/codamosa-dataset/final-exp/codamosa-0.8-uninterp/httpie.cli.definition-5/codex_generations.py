

# Generated at 2022-06-13 21:19:21.268742
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert iter(choices) is not None
    assert isinstance(iter(choices), collections.abc.Iterable)
    assert sorted(choices) == sorted(iter(choices))

auth.add_argument(
    '--auth-type',
    default=None,
    type=normalize_auth_value,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Default: "basic". The type of auth credentials provided with --auth.
    Possible values depend on the installed plugins.
    Run: http --auth-types to print a list of choices.

    ''',
)


# Generated at 2022-06-13 21:19:34.677343
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == []

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication method.
    '''
)

#######################################################################
# Timeouts
#######################################################################

timeouts = parser.add_argument_group(title='Timeouts')
timeouts.add_argument(
    '--timeout',
    metavar='SECONDS',
    type=float,
    default=DEFAULT_TIMEOUT,
    help=f'''
    Timeout in seconds for the connection, request, and response.

    Default: {DEFAULT_TIMEOUT} s.

    '''
)
timeouts.add_

# Generated at 2022-06-13 21:19:38.079391
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'custom' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:19:40.661136
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert set(iter(_AuthTypeLazyChoices())) == set(
        plugin_manager.get_auth_plugin_mapping().keys())



# Generated at 2022-06-13 21:19:44.461593
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    a = _AuthTypeLazyChoices()
    assert 'Basic' in a
    assert 'Digest' in a
    assert 'Fake' not in a

# Generated at 2022-06-13 21:19:52.895996
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    l = _AuthTypeLazyChoices()
    assert 'basic' in l
    assert 'digest' in l
    assert 'awsv4' not in l
    assert set(iter(l)) == {'basic', 'digest'}


auth_type_choice = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=auth_type_choice,
    dest='auth_type',
    metavar='TYPE',
    help='''
    Choose the auth type to use.
    The default is "basic" when --auth is provided and "digest" when --auth-digest is provided.
    Auto-select is skipped when --auth-type is specified in config.
    ''',
)


# Generated at 2022-06-13 21:20:05.150404
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method _AuthTypeLazyChoices.__iter__."""
    assert _AuthTypeLazyChoices().__iter__() == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to be used. No default;
    the detected type depends on --auth.

    If a custom plugin is specified, the referenced module must be
    importable. The module must define a function called get_auth_plugin().
    See builtin plugins for examples.

    '''
)



# Generated at 2022-06-13 21:20:15.454254
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '--auth-plugin',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of the HTTPie plugin that should be used to perform the
    authentication. If `'auto'`, then the plugin is autodetected
    based on the --auth option value.

    Available plugins:

        {0}

    See https://httpie.org/plugins/auth for details.

    '''.format(
        ', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    )
)


#######################################################################
# JSON options
#######################################################################


# Generated at 2022-06-13 21:20:16.716033
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:28.173617
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()


auth_type = auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Select an authentication plugin.
    '''
)


#######################################################################
# Custom configuration
#######################################################################

config = parser.add_argument_group(title='Custom Configuration')


# Generated at 2022-06-13 21:20:42.370982
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    valid_types = _AuthTypeLazyChoices()
    assert 'basic' in valid_types
    assert 'digest' in valid_types
    assert 'bearer' in valid_types

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to be used. To see the list of possible values, run:

        http --help

    '''
)

auth.add_argument(
    '--auth-prompt',
    action='store_true',
    default=False,
    help='''
    When using HTTP basic auth, prompt for the password.

    '''
)

#######################################################################
# TLS/SSL
#######################################################################


# Generated at 2022-06-13 21:20:45.023119
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    def test_return(value):
        return value
    _AuthTypeLazyChoices.__iter__ = test_return
    choices = _AuthTypeLazyChoices()
    assert ('basic' in choices) == ('basic' in plugin_manager.get_auth_plugin_mapping())


# Generated at 2022-06-13 21:20:46.390315
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:59.601580
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.

    The 'auto' mode is useful for request to APIs that support both Basic and
    Digest auth. It will attempt Digest auth first and fallback to Basic if it
    is not supported by the server.

    Possible values: {', '.join(
        sorted(plugin_manager.get_auth_plugin_mapping().keys()))}.

    '''
)

# ``requests.auth.HTTPBasicAuth`` keyword argument.

# Generated at 2022-06-13 21:21:07.702008
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():  # pragma: no cover
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'oauth1' in _AuthTypeLazyChoices()
    assert 'plugin_name' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:21:19.607269
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'custom']
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The custom authentication handler to use. Default: "{DEFAULT_AUTH_TYPE}".

    Available handlers: {', '.join(sorted(_AuthTypeLazyChoices()))}.

    '''
)
auth.add_argument(
    '--auth-plugin',
    default=None,
    help='''
    An alternative way to specify an authentication plugin.

    '''
)

#######################################################################
# HTTP method
#######################################################################

method = parser.add

# Generated at 2022-06-13 21:21:23.114590
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == \
        sorted(list(plugin_manager.get_auth_plugin_mapping()))

# Generated at 2022-06-13 21:21:30.978583
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(_AuthTypeLazyChoices()) == set(
        # for compatibility with httpie/plugins/auth/__init__.py
        [
            'basic',
            'digest',
            'hawk',
            'jwt',
            'oauth1',
            'multipart',
            'apikey',
            'gssnegotiate',
        ]
    )


# Generated at 2022-06-13 21:21:32.669119
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__(): 
    # Add your code here
    pass

# Generated at 2022-06-13 21:21:37.227965
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    instance = _AuthTypeLazyChoices()
    assert ('digest' in instance) is True
    assert ('digest' in instance) is True
    assert ('digest' in instance) is True
    assert ('bogus' in instance) is False


# Generated at 2022-06-13 21:21:47.562543
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "auto" which
    determines the authentication type based on the URL and the HTTP method.
    Available values depend on which authentication plugins are enabled. The
    following authentication plugins are enabled by default:

        {auth_plugins}

    '''.format(
        auth_plugins=humanize_choices(
            plugin_manager.get_auth_plugin_mapping().keys(),
            prefix='* ',
            wrap=30
        ),
    ),
)
# auth.add_argument(
#     '--auth-type-force',
#     metav

# Generated at 2022-06-13 21:21:49.859614
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'SomeAuthPlugin' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:22:00.258655
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest',
        'hawk', 'ntlm', 'oauth1', 'oauth2'
    ]
auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom --auth type (default: "basic").

    Plugins are searched for in:

        {plugin_dir}

    '''.format(plugin_dir=get_auth_plugin_dir()),
)


#######################################################################
# Timeouts
#######################################################################



# Generated at 2022-06-13 21:22:02.788110
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == \
        sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:22:15.723748
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert len(list(_AuthTypeLazyChoices())) > 0

# Field name "type" is special in argparse and must be specified
# using dest="auth_type".

# Generated at 2022-06-13 21:22:26.893755
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth_type = auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The available values are
    provided by auth plugins.

    '''
)
auth_type.completer = ChoicesCompleter(
    choices_getter=lambda: list(plugin_manager.get_auth_plugin_mapping()),
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:22:28.944658
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:22:32.165621
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'foobar' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:22:42.552446
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'gss_negotiate' in auth_type_lazy_choices
    assert 'my_not_existing_plugin' not in auth_type_lazy_choices


auth.add_argument(
    '--auth-type',
    default=None,
    help='''
    Specify a custom authentication plugin.
    Available built-in plugins: {choices}.
    Custom plugins can be installed with `$ pip install httpie-*-auth'.

    See https://github.com/jakubroztocil/httpie#authentication for details.

    '''.format(choices=_AuthTypeLazyChoices())
)

# Generated at 2022-06-13 21:22:52.866337
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic',
        'digest',
        'hawk',
        'oauth1',
        'ntlm',
    ]

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Currently supported values:
        {0}

    '''.format(', '.join(_AuthTypeLazyChoices())),
)
auth.add_argument(
    '--auth-send',
    action='store_true',
    help='''
    Send authentication data even if the server responds to the initial request
    with a 401 status and a WWW-Authenticate header.

    '''
)


# Generated at 2022-06-13 21:23:08.148174
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert set(choices) == set(plugin_manager.get_auth_plugin_mapping().keys())



# Generated at 2022-06-13 21:23:10.712645
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'does-not-exist' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:19.688621
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for name in _AuthTypeLazyChoices():
        plugin = plugin_manager.get_auth_plugin_mapping()[name]
        setattr(plugin, 'test_class__AuthTypeLazyChoices', True)
    assert getattr(BasicAuthPlugin, 'test_class__AuthTypeLazyChoices')
    assert getattr(DigestAuthPlugin, 'test_class__AuthTypeLazyChoices')



# Generated at 2022-06-13 21:23:26.074945
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    metavar='TYPE',
    dest='auth_plugin',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin (e.g., "digest").

    To see a list of all supported authentication plugins, run:

        http --debug

    The "auto" authentication plugin (which is the default) detects the
    scheme from the URL.

    If the scheme of the URL is not recognized by "auto",
    then the request is attempted without auth.

    Plugins are searched first in the current directory, then in
    the directory specified via --plugins-dir.

    '''
)


# Generated at 2022-06-13 21:23:27.543577
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:23:28.676911
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'token' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:43.362128
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. If not specified, HTTPie
    tries to guess it based on the --auth option value. Currently supported:

        {0}

    '''.format('\n'.join('* {type}'.format(type=type)
                         for type in _AuthTypeLazyChoices()))
)


# Generated at 2022-06-13 21:23:55.348398
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'foo' not in choices
    assert sorted(['digest']) == sorted(choices)


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The only built-in auth types
    are "basic" and "digest". If a Colon-Separated File (CSF) is used,
    the third format line will set the auth type.

    '''
)


# Generated at 2022-06-13 21:23:57.705697
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:08.240472
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from requests_toolbelt.auth.guess import GuessAuth
    plugin_manager._plugins['guess'] = GuessAuth
    assert 'guess' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    type=AuthCredentials.from_string,
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an authentication plugin. This is the same as setting the ``auth``
    option, but allows programmatic access to the plugin.
    The default is 'auto'.

    You can override the default by setting the ``auth_type`` HTTPie config
    option. Example:

        http --auth-type=jwt :5000/protected some_jwt_token

    '''
)

# Generated at 2022-06-13 21:24:34.033362
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())



# Generated at 2022-06-13 21:24:43.601041
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    >>> lazy_choices = _AuthTypeLazyChoices()
    >>> 'digest' in lazy_choices
    True
    >>> 'abc' in lazy_choices
    False

    """

auth_type = auth.add_argument(
    '--auth-type', '--auth-type-force',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The plugin used for authentication, e.g. digest, oauth2, awsauth.

    Use `--auth-type help` to print available plugins.

    '''
)
auth_plugin = auth.add_argument_group(title='Plugin specific options')

#######################################################################
# Plugins
#######################################################################



# Generated at 2022-06-13 21:24:55.490299
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    Test __iter__ method of _AuthTypeLazyChoices class.
    """
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']
test__AuthTypeLazyChoices___iter__()


auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    metavar='TYPE',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use. By default, the plugin attempts to guess.
    Available choices:

        basic, digest

    ''',
)

# Generated at 2022-06-13 21:25:03.904652
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_plugin',
    type=plugin_manager.get_auth_plugin_class,
    action=plugin_manager.get_auth_plugin_class_action(),
    choices=_AuthTypeLazyChoices(),
    default=DEFAULT_AUTH_PLUGIN,
    help='''
    Authentication plugin to use. The default mode is "basic" and it
    provides support for Basic and Digest HTTP auth.

    See the --auth-type option of the http command to see a list of
    all installed authentication plugins.

    ''',
)

#######################################################################
# Proxies
#######################################################################



# Generated at 2022-06-13 21:25:13.266916
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    actual = list(_AuthTypeLazyChoices())
    actual.sort()
    expected = sorted([
        'basic',
        'digest',
        'hawk',
        'ntlm',
        'multipart',
        'oauth1',
        'oauth1a',
        'oauth2',
    ])
    assert actual == expected



# Generated at 2022-06-13 21:25:20.449138
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for auth_type in _AuthTypeLazyChoices():
        assert auth_type in plugin_manager.get_auth_plugin_mapping()


auth.add_argument(
    '--auth-type',
    metavar='type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism. It can be: {0}

    The default is to auto-detect the auth type. For Basic auth, auto-detection
    works by looking at the URL.

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

# Generated at 2022-06-13 21:25:25.069554
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:25:28.477900
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices_choices__iter__ = _AuthTypeLazyChoices()
    assert list(choices_choices__iter__) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:25:31.821250
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()))


# Generated at 2022-06-13 21:25:45.144723
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    return

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='Authorization plugin to use. Defaults to auto-detection.'
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='Do not issue HTTP Authentication challenges.',
)
auth.add_argument(
    '--auth-no-robots',
    dest='no_robots',
    action='store_true',
    help='Do not suppress authentication when robots.txt disallows it.',
)

# Generated at 2022-06-13 21:26:24.752146
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    class Plugin:
        auth_type = 'test'
        def get_auth(self, auth):
            pass
    plugin_manager.register(Plugin())
    assert 'test' in list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to use.
    For Basic and Digest authentication, HTTPie will query the user
    and password unless specified or cached.
    Alternatively, you can specify the value in [user[:password]] format.

    '''
)

# Generated at 2022-06-13 21:26:35.564017
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == []

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Use an authentication plugin.

    ''',
)

auth.add_argument(
    '--auth-no-challenge',
    dest='auth_require_challenge',
    action='store_false',
    default=True,
    help='''
    Don't try to receive and handle 401 challenges; immediately attempt
    to authenticate.

    '''
)

#######################################################################
# HTTP methods
#######################################################################

methods = parser.add_argument_group(title='HTTP methods')

# Generated at 2022-06-13 21:26:43.685839
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.input import _AuthTypeLazyChoices
    from mock import patch
    from httpie.plugins import AuthPluginManager
    mock_plugin_manager = AuthPluginManager()
    mock_plugin_manager.get_auth_plugin_mapping.return_value = {"A": 1, "C": 2, "B": 3}
    with patch("httpie.input.plugin_manager", mock_plugin_manager):
        it = _AuthTypeLazyChoices()
        assert list(it) == ["A", "B", "C"]

# Generated at 2022-06-13 21:26:47.097983
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' not in _AuthTypeLazyChoices()
    assert 'http-prompt' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:27:00.835608
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert BasicAuth.scheme_name in choices


auth.add_argument(
    '--auth-type',
    default=BasicAuth.scheme_name,
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    The authentication mechanism.

    Currently supported types:

    {auth_types}

    '''.format(
        auth_types=(8 * ' ').join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    )

)


#######################################################################
# other
#######################################################################


# Generated at 2022-06-13 21:27:10.800755
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

auth_type = auth.add_argument(
    '--auth-type',
    dest='auth_plugin_name',
    type=plugin_manager.get_auth_plugin_mapping().__getitem__,
    choices=_AuthTypeLazyChoices(),
    default=None,
    help=f'''
    Specify an auth plugin.

    The available auth plugins are:

        {" ".join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:27:12.797550
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    l = _AuthTypeLazyChoices()
    assert 'basic' in l
    assert not ('foobar' in l)

# Generated at 2022-06-13 21:27:20.603751
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())



# Generated at 2022-06-13 21:27:32.475831
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Authentication type to be used (default: {DEFAULT_AUTH_PLUGIN}).
    Available types: {', '.join(_AuthTypeLazyChoices())}.

    '''
)

#######################################################################
# HTTPS (TLS/SSL/HTTPS)
#######################################################################

https = parser.add_argument_group(title='HTTPS (SSL/TLS) options')

# Generated at 2022-06-13 21:27:34.045420
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:48.384338
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:58.693266
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'colon' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Specify an auth handler.  By default, the best available auth handler is
    selected.

    The option is useful for selecting a specific HTTP auth
    implementation when there are multiple available (e.g., when both Basic and
    Digest auth are available).

    '''
)

# Generated at 2022-06-13 21:29:07.822411
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from tempfile import mkdtemp
    from os.path import dirname, exists, join
    from shutil import rmtree
    from plugin import load_plugins

    auth_plugin_dir_path = mkdtemp()

# Generated at 2022-06-13 21:29:09.154386
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Bearer' in _AuthTypeLazyChoices