

# Generated at 2022-06-13 21:19:12.654749
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(HTTPIECLIAuth()))

# Generated at 2022-06-13 21:19:14.889650
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

# Generated at 2022-06-13 21:19:27.181485
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    metavar='TYPE',
    dest='auth_plugin',
    help='''
    The authentication method to be used. By default, the authentication
    method is inferred from the provided credentials (-a).

    '''
)

#######################################################################
# HTTP
#######################################################################

http = parser.add_argument_group(title='HTTP')


# Generated at 2022-06-13 21:19:39.795186
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert ANY in lazy_choices
    assert 'basic' in lazy_choices

auth.add_argument(
    '--auth-type',
    default=None,
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    metavar='PLUGIN',
    help='''
    The authentication mechanism to be used. Invokes the corresponding plugin.

    Plugins: {plugins_list}

    Plugins are also discoverable by running: "http --auth-type=".

    '''
)

for plugin_name, plugin_class in plugin_manager.get_auth_plugin_mapping().items():
    plugin = plugin_class()
    plugin.add_parser_options(auth)

#######################################################################
# Advanced
################################

# Generated at 2022-06-13 21:19:42.826316
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert tuple(iter(_AuthTypeLazyChoices())) == (
        'basic',
        'digest',
        'hmac'
    )

# Generated at 2022-06-13 21:19:52.517673
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert (
        sorted(plugin_manager.get_auth_plugin_mapping().keys())
        ==
        list(_AuthTypeLazyChoices())
    )

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication scheme.

    The scheme is chosen automatically when the --auth option is provided.
    The scheme can be overridden with this flag.

    The default scheme is "basic", but it may be changed at any time by a
    plugin, or by HTTPie itself.

    ''',
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

ssl_verify = ssl.add_mutually_exclusive_group()
ssl_

# Generated at 2022-06-13 21:20:07.631753
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    _AuthTypeLazyChoices()

auth_plugin = auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported values are:

        {0}

    '''.format('\n'.join(
        '{0}{1}'.format(8 * ' ', line.strip())
        for line in wrap(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())), 60)
    ).strip())
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:20:16.544675
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help='''
    The authentication mechanism to be used.
    Defaults to basic.

    The plugins included with HTTPie are:

        {auth_plugins}

    '''.format(
        auth_plugins=_format_choices_list(
            plugin_manager.get_auth_plugin_mapping().keys()
        )
    )
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:20:25.622929
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins.builtin import BasicAuthPlugin, DigestAuthPlugin
    plugin_manager._clear()
    plugin_manager.install_plugin(BasicAuthPlugin())
    plugin_manager.install_plugin(DigestAuthPlugin())
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'OAuth2' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:38.177889
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # forget about any previously registered plugins
    plugin_manager.unload_all()
    _AuthTypeLazyChoices.__dict__.pop('_choices', None)
    # define two dummy plugins
    plugin_manager.register_plugin(
        'dummy_auth_1',
        import_path='tests.dummy_plugins.httpie.auth.dummy_auth_1',
    )
    plugin_manager.register_plugin(
        'dummy_auth_2',
        import_path='tests.dummy_plugins.httpie.auth.dummy_auth_2',
    )
    # choices should be sorted alphabetically
    assert sorted(list(_AuthTypeLazyChoices())) == \
           ['dummy_auth_1', 'dummy_auth_2']

# Generated at 2022-06-13 21:20:45.822809
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == \
        sorted(plugin_manager.get_auth_plugin_mapping().keys())



# Generated at 2022-06-13 21:20:59.332002
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert isinstance(lazy_choices, _AuthTypeLazyChoices)
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'foo' not in lazy_choices
    assert sorted(lazy_choices) == sorted(['basic', 'digest'])


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Auth plugin to use. Available plugins: {0}

    '''.format(
        ', '.join(
            plugin_manager.get_auth_plugin_mapping().keys()
        )
    )
)


#######################################################################
# Timeouts
#######################################################################


# Generated at 2022-06-13 21:21:07.273787
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert isinstance(_AuthTypeLazyChoices(), Iterable)
assert list(_AuthTypeLazyChoices()) == [
    'aws-sigv4',
    'bcrypt',
    'basic',
    'digest',
    'hawk',
    'gssapi',
    'ignored',
    'oauth2-jwt-bearer',
    'oauth2-mac',
]

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication scheme. TYPE is the name of the scheme
    (some are built-in, some are provided by plugin, and you can also
    implement your own).
    '''
)

auth.add_argument

# Generated at 2022-06-13 21:21:19.241318
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.plugins import builtin  # noqa
    from httpie.compat import is_py26

    lazy_choices = _AuthTypeLazyChoices()

    if is_py26:
        # Python 2.6 doesn't support ordering of dicts,
        # so we just test that the keys are present.
        assert set(lazy_choices) == {
            'basic', 'digest', 'hawk', 'bearer', 'occi'
        }
    else:
        # Any other Python version should give the keys in some order.
        assert list(lazy_choices) == [
            'basic', 'digest', 'hawk', 'bearer', 'occi'
        ]



# Generated at 2022-06-13 21:21:29.584879
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '--auth-plugin',
    default=None,
    metavar='PLUGIN',
    help='''
    Specify an auth plugin to use. The default is Basic.
    If the plugin needs extra data, you can set it with --auth-plugin-param.

    Available plugins:
    {auth_plugins}

    '''.format(
        auth_plugins='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(sorted(_AuthTypeLazyChoices())), 60)
        ).strip()
    ),
    choices=_AuthTypeLazyChoices(),
)

# Generated at 2022-06-13 21:21:40.884014
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == \
        sorted(list(_AuthTypeLazyChoices()))


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specifies the authentication mechanism.

    The default value of None chooses the most secure of the supported
    mechanisms that the server announces support for.

    Available values:

    {auth_type_choices}
    '''.format(auth_type_choices=get_auth_type_choices_help())
)


# Generated at 2022-06-13 21:21:42.050378
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:21:43.140788
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__((object()))

# Generated at 2022-06-13 21:21:48.712366
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    invalid_auth_type = 'invalid-auth-type'
    assert invalid_auth_type not in _AuthTypeLazyChoices()
    try:
        auth_type_lazy_choices = _AuthTypeLazyChoices()
        auth_type_lazy_choices.__contains__(invalid_auth_type)
    except TypeError:
        pass

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. One of:

    ''' + ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())) + '''

    By default, the mechanism is guessed from the URL and the --auth option.

    '''
)

# Generated at 2022-06-13 21:21:52.534713
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    ))


# Generated at 2022-06-13 21:22:12.038202
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    expected = sorted(plugin_manager.get_auth_plugin_mapping())
    assert set(_AuthTypeLazyChoices()) == set(expected)

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication plugin to use. Some built-in plugins are:
    {0}.
    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

# Generated at 2022-06-13 21:22:24.339055
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()
    assert 'custom' in _AuthTypeLazyChoices()
    assert 'nonexisting' not in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=lambda type: type.strip().lower(),
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Defaults to Basic if the username containing a colon (':').
    Defaults to Digest otherwise.

    ''',
)

# Generated at 2022-06-13 21:22:26.662093
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'non-existing' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:22:28.489285
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:22:39.873626
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    dest='auth_plugin',
    help='''
    Use the specified HTTP authentication plugin.
    For example, "digest" or "jwt".

    '''
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    By default, when the initial request receives a 401 response,
    HTTPie will send the same request again with the Authorization header.
    You can disable this behavior by using the --auth-no-challenge
    option.

    '''
)

################################################################

# Generated at 2022-06-13 21:22:51.387924
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(_AuthTypeLazyChoices()) == sorted(['basic', 'digest'])


auth.add_argument(
    '--auth-type',
    type=plugin.load_plugin_from_name('auth'),
    metavar='type',
    dest='auth_type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin. Use the special value "auto" to
    let HTTPie discover the auth plugin from the HTTP response.
    (default: "auto").

    '''
)


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:23:00.716895
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth_type_validator = OneOfLazyChoices(
    'auth-type', _AuthTypeLazyChoices(),
    transform_func=lambda s: s.lower(),
    error_message='Invalid auth type.'
)
auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    type=auth_type_validator,
    help=f'''
    The auth mechanism to use. Supported: {', '.join(
        sorted(plugin_manager.get_auth_plugin_mapping().keys()))}.

    '''
)


# Generated at 2022-06-13 21:23:08.258986
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert AVAILABLE_AUTH_PLUGINS == list(_AuthTypeLazyChoices())
    plugin_manager.get_auth_plugin_mapping().pop('foo')
    assert AVAILABLE_AUTH_PLUGINS != list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str,
    help='''
    Specify an alternate authentication plugin.

    ''',
    choices=_AuthTypeLazyChoices(),
)

# Generated at 2022-06-13 21:23:18.298553
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    list(plugin_manager.get_auth_plugin_mapping())
    assert 'basic' in _AuthTypeLazyChoices()
assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:23:24.754985
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices."""
    assert [i for i in _AuthTypeLazyChoices()] == sorted(list(plugin_manager.get_auth_plugin_mapping().keys()))

auth_plugin_choices = _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:43.899334
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())
auth_type_choices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=auth_type_choices,
    dest='auth_type',
    metavar='TYPE',
    help='''
    Override the default authentication plugin.

    '''
)

auth.add_argument(
    '--auth-plugin',
    metavar='MODULE_PATH',
    type=str,
    help='''
    Specify a custom authentication plugin module (python import path).
    This option takes precedence over --auth-type.

    '''
)

#######################################################################
# HTTPS
#######################################################################

ssl = parser.add_argument_group(title='HTTPS')
ssl.add_argument

# Generated at 2022-06-13 21:23:46.906908
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic',
        'digest',
        'kerberos',
        'negotiate',
    ]

# Generated at 2022-06-13 21:23:58.426296
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of auth plugin to use.

    By default, HTTPie looks for the most suitable plugin based on
    the provided --auth username and password or a .netrc file.

    ''',
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    Do not perform a challenge-response authentication (e.g. Basic).

    '''
)

# Generated at 2022-06-13 21:24:08.339218
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hawk' in choices
    assert 'custom' in choices
    assert 'not-an-auth' not in choices
    assert list(choices) == ['basic', 'custom', 'digest', 'hawk']


# Generated at 2022-06-13 21:24:22.753050
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'aws4' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication plugin to use, either explicitly or by file
    extension.

    For example, to use `aws4`, you can either use `--auth-type aws4` or
    specify the auth credentials in `~/.aws/credentials` and then pass
    the --auth-type option with a file extension that loads the `aws4` plugin
    (such as `--auth-type .aws`).

    '''
)


# Generated at 2022-06-13 21:24:34.211464
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices,
    help='''
    The authentication mechanism (only Basic is supported natively).
    You can install plugins for other types.

    ''',
)

auth.add_argument(
    '--ignore-netrc',
    action='store_true',
    help='''
    Do not use netrc for authentication.

    ''',
)

#######################################################################
# Output options
#######################################################################

headers = parser.add_argument_group(title='Headers')

# Generated at 2022-06-13 21:24:36.579714
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:44.957196
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    x = _AuthTypeLazyChoices()
    assert sorted(x) == ['basic', 'digest', 'foobar', 'my_plugin']

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The AUTH_TYPE for authentication. Supported types are:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

auth.add_argument(
    '--auth-verify-ssl',
    action='store_true',
    default=False,
    help='''
    Verify SSL certificates of HTTPS servers when using an HTTPS proxy with
    Basic/Digest auth.

    ''',
)



# Generated at 2022-06-13 21:24:56.838643
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    obj = _AuthTypeLazyChoices()
    assert 'basic' in obj


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is "basic".
    Known values are: {choices}.

    '''.format(choices=', '.join(
        sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)
auth.add_argument(
    '--auth-send',
    default='auto',
    choices=['auto', 'always', 'never'],
    help='''
    When the authentication credentials will be sent to the server.
    Possible values: auto, always, never.

    '''
)

# Generated at 2022-06-13 21:25:01.840754
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices
    assert 'digest' in _AuthTypeLazyChoices
    assert 'awesome-auth' not in _AuthTypeLazyChoices
    try:
        # noinspection PyTypeChecker
        'awesome-auth' in ''
    except TypeError:
        pass
    else:
        assert False, '__contains__ accepts non-str'

# Generated at 2022-06-13 21:25:45.105053
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['digest', 'hawk']

auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. By default, HTTPie
    tries to detect the most secure mechanism supported by the server,
    while falling back to HTTP basic.

    Available choices:

        {type_choices}

    '''.format(type_choices=_AuthTypeLazyChoices())
)

_sorted_kwargs = {
    'action': 'append_const',
    'const': SORTED_FORMAT_OPTIONS_STRING,
    'dest': 'format_options'
}

# Generated at 2022-06-13 21:25:54.069780
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie import plugin, exit_status
    from httpie.plugins.builtin import HTTBasicAuth
    class CustomAuthPlugin(HTTBasicAuth):
        auth_type = 'custom'
        def get_auth_from_url(self):
            pass
    plugin_manager.get_auth_plugin_mapping = lambda: {'custom': CustomAuthPlugin}
    assert list(_AuthTypeLazyChoices()) == ['custom']

auth.add_argument(
    '--auth-type',
    help='''
    Explicitly specify a custom auth plugin by name.
    In most cases, HTTPie can guess which plugin to use.

    ''',
    choices=_AuthTypeLazyChoices()
)

# Generated at 2022-06-13 21:26:05.025623
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='AUTHTYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force the use of a specific authentication method.

    ''',
)
auth.add_argument(
    '--auth-unix', '-U',
    action='store_true',
    help='''
    Use UNIX user account (uid and gid) as credentials.

    ''',
)

#######################################################################
# Options
#######################################################################

options = parser.add_argument_group(title='Options')

# Generated at 2022-06-13 21:26:07.630172
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:17.811513
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices()

_AuthTypeLazyChoices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices,
    help=f'''
    The authentication mechanism to be used.

    The default is "basic". This can be overridden by providing the username
    as "user:pass" or "user#pass" (as a shorthand for "user@basic"), or by
    using a URL with the user credentials embedded (e.g.,
    http://user:pass@example.org/).

    Other auth types include: {', '.join(sorted(_AuthTypeLazyChoices))}

    '''
)

#######################################################################
# Downloads
#######################################################################

downloads = parser

# Generated at 2022-06-13 21:26:33.448520
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    obj = _AuthTypeLazyChoices()
    assert 'foo' in obj

auth_plugin_mapping = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=None,
    choices=auth_plugin_mapping,
    help='''
    How to perform authentication. The value must be the name of an
    `httpie-auth-plugin <https://github.com/jakubroztocil/httpie-auth-plugin>`.

    '''
)


# Generated at 2022-06-13 21:26:46.639077
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_names = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(_AuthTypeLazyChoices()) == auth_type_names
auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    Specify the authentication type to be used. It's the same to use an auth
    plugin:

        $ http --auth-type=digest --auth=user:password ...

        $ http --digest-auth=user:password ...

    The default is 'auto'.

    '''
)


# Generated at 2022-06-13 21:26:49.034485
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ["basic", "digest", "hawk", "ntlm", "oauth1"]

# Generated at 2022-06-13 21:26:55.945239
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'bearer' in auth_type_lazy_choices
    assert 'basic' in auth_type_lazy_choices
    assert 'hawk' in auth_type_lazy_choices
    assert 'aws' in auth_type_lazy_choices


# Generated at 2022-06-13 21:27:04.119457
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    plugin_manager.load_builtin_plugins()
    plugin_manager.load_plugins()
    auth_types = _AuthTypeLazyChoices()
    assert sorted(auth_types) == sorted(get_auth_plugin_mapping().keys())

AUTH_TYPE_CHOICES = _AuthTypeLazyChoices()
AUTH_PLUGIN_MAPPING = plugin_manager.get_auth_plugin_mapping()



# Generated at 2022-06-13 21:28:14.764131
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'multipart' in _AuthTypeLazyChoices()
    assert 'non-existent' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used. The default is "auto", which will
    attempt to use best suitable authentication mechanism. Valid choices are:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

# Generated at 2022-06-13 21:28:32.388487
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'NotExistingAuthType' not in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='auto'
)

#######################################################################
# SSL
#######################################################################

ssl_verification = parser.add_argument_group(title='SSL Verification')
ssl_verification.add_argument(
    '--ssl', '--verify',
    dest='verify',
    action='store_true',
    help='''
    (default) Verify the server SSL certificate.

    '''
)

# Generated at 2022-06-13 21:28:40.249378
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(list(_AuthTypeLazyChoices())) == \
        set(list(plugin_manager.get_auth_plugin_mapping().keys()))


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. By default,
    the plugin auto-detects the mechanism based on the
    --auth option value, but the auto-detection can be
    overridden with this flag.

    The available choices are: {choices}

    '''.format(
        choices=', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    )
)


# Generated at 2022-06-13 21:28:45.554545
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # TODO: generalize style detection and apply also to ensure_styles()
    if platform.system().lower() == 'linux':
        available_styles = [
            'solarized-dark',
            'solarized-light',
            'swapoff',
        ]
    else:
        available_styles = [
            'monokai',
            'snazzy',
            'swapoff',
            'tango',
        ]
    assert list(_AuthTypeLazyChoices()) == available_styles


# Generated at 2022-06-13 21:28:49.250990
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    class AuthTypeLazyChoices(_AuthTypeLazyChoices):
        def __iter__(self):
            raise RuntimeError()

    assert 'Basic' in AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:58.480601
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():

    dummy_plugin_manager = DummyAuthPluginManager()

    AuthTypeLazyChoices = _AuthTypeLazyChoices

    # Auth plugins are not loaded yet
    assert 'bar' not in AuthTypeLazyChoices()

    # Load auth plugin
    dummy_plugin_manager.load_builtin_auth_plugins()

    # Auth plugins are now loaded
    assert 'bar' in AuthTypeLazyChoices()

    # Load another auth plugin
    dummy_plugin_manager.update_auth_plugin_mapping(
        AuthPlugin(name='foo', auth_type='foo', load=lambda: True)
    )

    # Another auth plugin is now loaded
    assert 'foo' in AuthTypeLazyChoices()


# Generated at 2022-06-13 21:29:02.017150
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert ['digest', 'jwt', 'oauth1', 'hawk'] == list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:29:04.627024
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    container = _AuthTypeLazyChoices()
    assert 'basic' in container
    assert 'does-not-exist' not in container


# Generated at 2022-06-13 21:29:13.113000
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    pass

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication type (digest or basic). If not provided the
    authentication mechanism will be chosen based on the
    HTTP response.

    '''
)
auth.add_argument(
    '--auth-host',
    default=DEFAULT_AUTH_HOST,
    metavar=DEFAULT_AUTH_HOST,
    help='''
    Host for which the provided credentials are valid.
    Default is "{default}".

    '''.format(default=DEFAULT_AUTH_HOST)
)

#######################################################################
# Cookie options
#######################################################################

cookie = parser.add_argument_group(title='Cookies')