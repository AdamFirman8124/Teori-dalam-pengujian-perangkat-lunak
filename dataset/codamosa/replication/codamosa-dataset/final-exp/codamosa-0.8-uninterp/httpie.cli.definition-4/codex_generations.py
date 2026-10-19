

# Generated at 2022-06-13 21:19:15.724099
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:19:28.276886
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert AVAILABLE_AUTH_PLUGINS == list(_AuthTypeLazyChoices())

AUTH_TYPES = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    # There's no need to sort these, they're shown only once in --help.
    choices=AUTH_TYPES,
    help=f'''
    Force the specified auth plugin. If a plugin is not specified,
    HTTPie tries to detect it. Available plugins: {fuzzy_choices(AUTH_TYPES)}

    '''
)


# Generated at 2022-06-13 21:19:40.717824
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Which authentication method to use. The supported methods vary depending
    on the HTTP client. The default value for the HTTPie standalone, for
    example, is "basic". For the httpie client bundled with Requests, it is
    "digest".

    '''
)


# Generated at 2022-06-13 21:19:48.576402
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
choice = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    default='basic',
    choices=choice,
    help='''
    The authentication mechanism to be used.

    Currently, only the Basic authentication mechanism is supported
    natively. For other mechanisms, refer to the Plugins section.

    '''
)


# Generated at 2022-06-13 21:19:51.059625
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices


# Generated at 2022-06-13 21:19:52.916412
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:20:02.936296
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(get_parser().get_default('auth_type_lazy_choices')) == [None, 'basic']

auth_type_lazy_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_type',
    choices=auth_type_lazy_choices,
    help='''
    The authentication mechanism.
    The default value is "basic".

    ''',
)



# Generated at 2022-06-13 21:20:14.476848
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(iter(_AuthTypeLazyChoices())) == \
        set(sorted(plugin_manager.get_auth_plugin_mapping().keys()))


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help='''\
    Auth plugin to use. "auto" tries to guess.

    The currently available options (can differ by installation):
        {auth_plugins}
    '''.format(
        auth_plugins=_indent(textwrap.fill(
            ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
        )),
    )
)


# Generated at 2022-06-13 21:20:27.370056
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == plugin_manager.\
    get_auth_plugin_mapping().keys()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to use.

    By default, the plugin autodetection is attempted.

    Possible values are:

    {choices}

    '''.format(
        choices='\n'.join(
            '{0} {1}'.format(8 * ' ', line.strip()) for line in
            wrap(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())), 60).strip()
        ).strip()

    )
)

#######################################################################
#  Content negotiation
#######################################################################

content_negotiation

# Generated at 2022-06-13 21:20:31.930010
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'unsupported_plugin' not in lazy_choices


# Generated at 2022-06-13 21:20:42.982171
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert all(x in _AuthTypeLazyChoices()
               for x in plugin_manager.get_auth_plugin_mapping())
    assert not any(x not in plugin_manager.get_auth_plugin_mapping()
                   for x in _AuthTypeLazyChoices())

auth_plugin_args_parser = parser.add_argument_group(title='Auth Plugin Options')
auth.add_argument(
    '--auth-type',
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth plugin module.
    This implicitly enables '--auth'.
    See 'http --help-auth' for a list of plugin names.
    '''
)


# Generated at 2022-06-13 21:20:54.626280
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert choices == plugin_manager.get_auth_plugin_mapping().keys()


plugin_manager = PluginManager()
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Some plugins may provide extra command line arguments. To list them,
    run `$ http --help` with the plugin selected. For example:

        $ http --auth-type=jwt --help

    The following auth types are currently available:

    {plugins}
    '''.format(
        plugins='\n'.join(
            8 * ' ' + name
            for name in sorted(plugin_manager.get_auth_plugin_mapping())
        )
    )
)

# Generated at 2022-06-13 21:21:06.798685
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'socks' not in _AuthTypeLazyChoices()

auth_type_choices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=auth_type_choices,
    help=f'''
    Auth plugin to use.

    Available choices: {', '.join(auth_type_choices) or 'none'}.

    '''
)


#######################################################################
# Cookies
#######################################################################

# ``requests.request`` keyword arguments.
cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:21:09.302312
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:21:19.235012
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'ntlm' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specifies the authentication mechanism.

    Currently supported:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))}

    ''',
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='''
    Disable preemptive basic/digest/NTLM/negotiate authentication.

    '''
)


# Generated at 2022-06-13 21:21:28.319237
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    >>> from httpie.cli.args import _AuthTypeLazyChoices
    >>> choices = _AuthTypeLazyChoices()
    >>> sorted(choices)  # doctest: +ELLIPSIS
    ['Digest', 'JWT', 'OAuth1', 'OAuth2', 'basic', 'bearer', ...]
    """

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication type to be used, must be one of:
    %(choices)s

    ''',
)


# Generated at 2022-06-13 21:21:30.680779
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'ignoreme' not in choices



# Generated at 2022-06-13 21:21:41.743257
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_type',
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help='''
    Choose an specific auth type. Default is %(default)s.

    ''',
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')


# Generated at 2022-06-13 21:21:47.935442
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used. One of:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))}

    '''
)

_username_password_kwargs = {
    'metavar': 'USERNAME[:PASSWORD]',
    'help': 'The username:password string',
}

# Generated at 2022-06-13 21:22:01.010586
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_choices = _AuthTypeLazyChoices()
    assert (
        ','.join(lazy_choices)
        == 'anon,aws-sigv4,base64,bearer,digest,hawk,kerberos,oauth1'
    )


# Generated at 2022-06-13 21:22:17.765854
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str.lower,
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The type of HTTP authentication. The default is "basic".

    Any other supported value implies the use of a custom authentication
    plugin. Available values are: {', '.join(plugin_manager.get_auth_plugin_mapping())}

    '''
)


# Generated at 2022-06-13 21:22:20.307403
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('basic')
test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:22:29.235699
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '-t',
    dest='auth_type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to use (e.g., "basic", "digest")

    If not specified, an appropriate one is guessed from the provided
    credentials, the server response, and the used URL.

    ''',
)


# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:22:41.394345
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'bearer' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar="TYPE",
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help="""
        The authentication mechanism. Possible values depend on the installed
        plugins. The following types are provided by default:

        {list}

        """.format(list=indent(
            '\n'.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
            lambda line: ' ' * 4 + line
        ))
    )


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:22:52.271322
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    class FakeAuthPlugin:
        auth_type = 'fake'
        disable_auth_session = True
        auth_parse = auth_prepare_request_hook = auth_process_response = \
            plugin_manager.dummy_auth_plugin_hook

    plugin_manager.auth_plugin['fake'] = FakeAuthPlugin()
    assert sorted([
        'fake'
    ]) == sorted(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism to use. Plugins can define additional auth types.
    See ``--help-plugins``.
    '''
)


#######################################################################
# Transports
#######################################################################

transport = parser.add

# Generated at 2022-06-13 21:22:55.433469
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest', 'hawk', 'ntlm']



# Generated at 2022-06-13 21:23:03.340766
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Test method __iter__ of class _AuthTypeLazyChoices"""
    class TestPlugin(AuthPlugin):
        auth_type = 'test'
        name = 'test'
        description = 'test'
        options_spec = ''
    plugin_manager.register(TestPlugin)
    try:
        instance = _AuthTypeLazyChoices()
        assert 'test' in instance
        assert 'basic' in instance
        assert 'all' not in instance
        assert list(instance) == ['basic', 'digest', 'test']
        return instance
    finally:
        plugin_manager.unregister(TestPlugin)
_auth_type_lazy_choices = _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:23:06.923327
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():  # noqa
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:11.514499
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(sorted(_AuthTypeLazyChoices())) == iter(sorted(['digest', 'jwt', 'jwt-auth', 'kerberos', 'ntlm', 'oauth1', 'oauth1a', 'oauth2']))


# Generated at 2022-06-13 21:23:20.202615
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication method to be used for the request. HTTPie can
    auto-detect the auth method based on the provided credentials, but if a
    wrong method is detected, you can force it with this option.

    '''
)

# Generated at 2022-06-13 21:23:35.419556
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hawk' in choices
    assert 'oauth1' in choices
    assert 'aws' in choices
    assert 'aws_s3' in choices
    # assert 'aws_s3_custom_domain' in choices  # disabled because of bug in nose

auth_type = auth.add_mutually_exclusive_group(required=False)

# Generated at 2022-06-13 21:23:47.996392
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

# ``auth_type`` keyword argument
auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify the type of HTTP authentication to use.
    The default, 'auto', detects the authentication type from the provided
    credentials.

    '''
)

# ``digest_auth`` keyword argument
digest_auth = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:23:59.259010
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of the auth plugin to use, such as "basic", "jwt", or the path to
    a custom plugin. For example, "jwt" or "path/to/file.py".

    '''
)
auth.add_argument(
    '--auth-verify',
    action='store_true',
    help='''
    Verify the SSL certificate of the auth server.

    '''
)


# Generated at 2022-06-13 21:24:08.685232
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    parser.add_argument("--auth-type", choices=_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism. Currently supported:
    {0}.
    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))),
)


# Generated at 2022-06-13 21:24:23.184058
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert sorted(auth_type_lazy_choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=AUTH_PLUGIN_MAP['basic'],
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom auth plugin.

    ''',
)

# Generated at 2022-06-13 21:24:34.481321
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism, e.g., 'basic' or 'digest'.

    '''
)
auth.add_argument(
    '--auth-parse',
    dest='auth_plugin_parse',
    choices=plugin_manager.get_auth_plugin_mapping().keys(),
    help=SUPPRESS,
)

# Generated at 2022-06-13 21:24:44.348753
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert all(
        plugin_name in _AuthTypeLazyChoices()
        for plugin_name in plugin_manager.get_auth_plugin_mapping()
    )
    assert PluginNotFound('foobar') not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:56.169343
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    a = _AuthTypeLazyChoices()
    assert 'basic' in a


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str.lower,
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.
    Defaults to "basic".

    The value can be passed as a type alias:

        --auth-type=digest

    The alias is looked up in the config file under the
    "auth_plugin_aliases" key, e.g.:

        auth_plugin_aliases = {
            "digest": "digestauth",
        }

    '''
)

# TODO: support the `requests` way of not-encoding the : and @ chars
# in the

# Generated at 2022-06-13 21:25:04.494149
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=AUTH_PLUGIN_MAP['basic'],
    type=lambda t: AUTH_PLUGIN_MAP[t],
    choices=_AuthTypeLazyChoices(),
    help='''
    Override the default authentication handler.  Currently supported
    values are "basic" and "digest". See also --auth-plugin.

    ''',
)

# The argument for dynamic auth plugin loading.

# Generated at 2022-06-13 21:25:13.608291
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices."""
    input= [var for var in _AuthTypeLazyChoices()]
    output=['basic', 'digest']
    assert output==input

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Select the authentication mechanism. If a plugin is not specified, it is
    guessed from the --auth option, if provided.

    '''
)
auth.add_argument(
    '--auth-plugin',
    help='''
    Path to a custom authentication plugin (can be a directory or a module).
    '''
)

#######################################################################
# Content
#######################################################################

content = parser.add_argument_group(title='Content')
content

# Generated at 2022-06-13 21:25:37.775967
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for arg in _AuthTypeLazyChoices():
        assert arg in plugin_manager.get_auth_plugin_mapping()

auth_type_help = '''
The name of an authentication plugin. Installed plugins are:

    {installed_plugins}

To disable any installed plugins, set this to "none"; the default is "basic".
'''.format(installed_plugins=_get_installed_auth_plugins_help())

auth_type = auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help=auth_type_help)


# Generated at 2022-06-13 21:25:40.370889
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' in _AuthTypeLazyChoices()
    assert 'bar' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:48.591052
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert any([item for item in _AuthTypeLazyChoices()])

auth.add_argument(
    '--auth-type',
    type=str,
    default=__name__ + '.Authenticator',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specifies which authentication method to use.
    The default is "{__name__ + '.Authenticator'}", which is the HTTPie
    native basic and digest authentication.
    ''',
)

_auth_plugin_docs = '\n\n'.join(
    _get_auth_plugin_docs(plugin_name)
    for plugin_name in sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )
)


# Generated at 2022-06-13 21:25:50.127037
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert ('digest' in _AuthTypeLazyChoices()) is True

# Generated at 2022-06-13 21:25:51.710369
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:04.646327
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == []
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help=f'''
    Choose a custom authentication plugin.
    The following are the builtin plugins:

        {','.join(sorted(builtin_auth_plugins))}

    See https://github.com/jakubroztocil/httpie#authentication for how to
    install more.

    '''.strip()
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:26:20.746939
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    return list(_AuthTypeLazyChoices())


auth_type = auth.add_mutually_exclusive_group(required=False)

auth_type.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help=f'''
    The authentication mechanism to be used. Currently supported:

        {', '.join(plugin_manager.get_auth_plugin_mapping().keys())}

    '''
)

# Generated at 2022-06-13 21:26:25.815850
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # __iter__
    assert list(_AuthTypeLazyChoices()) == ['aws', 'basicauth', 'digest', 'gssnegotiate', 'jwt', 'kerberos', 'ntlm', 'oauth1', 'oauth2']


# Generated at 2022-06-13 21:26:36.189626
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    dest='auth_type',
    metavar='TYPE',
    help='''
    The auth mechanism to be used, e.g., basic, digest.
    The default auth plugin is selected based on the URL.

    ''',
)
auth.add_argument(
    '--auth-host',
    default=None,
    dest='auth_host',
    metavar='HOST',
    help='''
    The name of the host to use for authentication.
    This can be used when a server provides multiple hostnames on a single
    IP, but requires different authentication for each.
    '''
)

# Generated at 2022-06-13 21:26:37.641304
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert hasattr(_AuthTypeLazyChoices(), '__iter__')

# Generated at 2022-06-13 21:27:10.535076
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy = _AuthTypeLazyChoices()
    assert 'digest' in lazy
    assert 'something-does-not-exist' not in lazy

# Generated at 2022-06-13 21:27:19.303448
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert not isinstance(
        _AuthTypeLazyChoices(), (list, tuple, set)
    ), 'This class is not meant to be iterable'
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified auth TYPE.

    You can discover all the available auth types via
    ``$ http --debug | grep -i auth-type``.

    The default and the fallback auth type is "basic".

    '''
)

# Generated at 2022-06-13 21:27:27.659603
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # The test is only for syntax errors.
    _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication plugin. By default, HTTPie
    determines the authentication plugin based on the specified --auth option
    or an Auth header.

    You can always see a list of available plugins with the
    --debug-auth flag.

    '''
)


#######################################################################
# Transport
#######################################################################

transport = parser.add_argument_group(title='Transport')


# Generated at 2022-06-13 21:27:35.305225
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert list(_AuthTypeLazyChoices()) == sorted(['digest', 'jwt'])


auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help=(
        'Specify the authentication mechanism. HTTPie '
        'supports plugins that add new types. The following are '
        'the built-in ones:\n\n' +
        '\n'.join('{0}{1}'.format(8 * ' ', line.strip())
                  for line in wrap(humanize_auth(plugin_manager)))
    )
)

# --auth-type=digest

# Generated at 2022-06-13 21:27:37.961616
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'bearer' in _AuthTypeLazyChoices()  # noqa: F821

# Generated at 2022-06-13 21:27:47.905991
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest', 'hawk', 'ntlm'
    ]

auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.

    {AUTH_PLUGIN_HELP}

    '''
)

# Generated at 2022-06-13 21:27:50.046326
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in lazy_choices
    assert 'digest' not in lazy_choices


# Generated at 2022-06-13 21:27:59.690746
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(
        auth_plugin_http
    ) == sorted(
        plugin_manager.get_auth_plugin_mapping()
    )

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth plugin to use. If not provided, HTTPie
    will attempt to infer it from the provided URL.

    ''',
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    Do not allow a "challenge" request (response status code 401) to be
    issued on authentication failure.

    '''
)

# Generated at 2022-06-13 21:28:00.588200
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert all(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:28:12.883490
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest', 'hawk', 'ntlm',
    ]

auth_type = auth.add_mutually_exclusive_group() \
    .add_argument(
        '--auth-type',
        default='basic',
        choices=_AuthTypeLazyChoices(),
        help='''
        Specify the authentication mechanism to be used. The default is "basic",
        which is HTTP's default.

        '''
    )


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')