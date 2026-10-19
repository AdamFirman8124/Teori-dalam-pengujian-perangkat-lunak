

# Generated at 2022-06-13 21:19:11.596160
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    instance = _AuthTypeLazyChoices()
    assert 'basic' in instance
    assert 'digest' in instance
    assert 'bearer' in instance
    assert 'foo' not in instance


# Generated at 2022-06-13 21:19:21.567984
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' not in choices

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an authentication plugin. Available plugins:

        {plugins}

    '''.format(
        plugins='\n'.join(
            4 * ' ' + line.strip()
            for line in wrap(', '.join(plugin_manager.get_auth_plugin_mapping().keys()), 60)
        ).strip(),
    )
)

# Generated at 2022-06-13 21:19:35.038075
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    help='''
    Force usage of a specific auth plugin.
    Choices: {choices}

    '''.format(
        choices=', '.join(plugin.name for plugin in AuthPlugin.all())
    )
)


#######################################################################
# Cookies
#######################################################################

# ``requests.request`` keyword arguments.
cookies = parser.add_argument_group(title='Cookies')
cookies.add_argument(
    '--cookie',
    dest='cookies',
    action='append',
    default=None,
    metavar='KEY=VALUE',
    help='''
    Sets a cookie.

    '''
)
cookies

# Generated at 2022-06-13 21:19:37.257072
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'dummy' in choices
    assert 'foo' not in choices

# Generated at 2022-06-13 21:19:49.484793
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(['basic', 'digest']) <= set(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Auth plugin to use.

    ''',
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='''
    If set, don't perform auth challenge. (Useful for Digest auth, for
    example.)

    ''',
)
auth.add_argument(
    '--ignore-netrc',
    dest='netrc',
    action='store_false',
    default=True,
    help='''
    Do not use the netrc credentials file.

    ''',
)

#

# Generated at 2022-06-13 21:19:56.669856
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """
    Unit test for method __contains__ of class _AuthTypeLazyChoices

    :return:
    """
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    for key in auth_type_lazy_choices:
        assert key in auth_type_lazy_choices


# Generated at 2022-06-13 21:20:10.825298
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__(): # noqa
    assert list(_AuthTypeLazyChoices()).sort() == sorted(list(iter(_AuthTypeLazyChoices())))

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Defaults to Basic if no
    mechanism is specified and the --auth option is provided.
    Note that this option is case-insensitive.
    The following authentication mechanisms are supported:

    ''' +
    '\n'.join(('\t' + '\n\t'.join(wrap(', '.join(sorted(auth_types)),
                                       width=TERMINAL_WIDTH - 8))).strip())
)

# Generated at 2022-06-13 21:20:21.216069
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin to be used.

    Available plugins are: {plugins}

    '''.format(
        plugins=', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    )
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:20:32.574999
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='AUTHTYPE',
    help='''
    Authenticate using the specified plugin.
    Plugins: {choices}
    '''.format(choices=_AuthTypeLazyChoices()),
    choices=_AuthTypeLazyChoices(),
)

auth.add_argument(
    '--auth-type-force',
    action='store_true',
    default=False,
    help='''
    If set, overrides the server's requested authentication type.
    ''',
)


# Generated at 2022-06-13 21:20:33.127459
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    list(_AuthTypeLazyChoices())
    

# Generated at 2022-06-13 21:20:38.221382
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:43.718179
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'custom' not in lazy_choices
# Unit test method __iter__ of class _AuthTypeLazyChoices

# Generated at 2022-06-13 21:20:52.281669
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    c = _AuthTypeLazyChoices()
    assert 'basic' in c
    assert 'kerberos' in c
    assert 'hawk' in c
    assert 'bar' not in c

auth.add_argument(
    '--auth-type', '-t',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism for use with --auth. Supported: basic (default),
    digest, hawk.

    ''',
)

# Generated at 2022-06-13 21:21:04.933770
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(iter(_AuthTypeLazyChoices())) == list(iter(
        sorted(plugin_manager.get_auth_plugin_mapping().keys())))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    ''',
)


#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')
cookies.add_argument(
    '--cookie', '-C',
    help='''
    Add a cookie. Option can be repeated for multiple cookies.
    Cookies are sent with all following requests until removed, e.g. with
    `--remove-cookie`.

    '''
)

# Generated at 2022-06-13 21:21:16.073092
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lc = _AuthTypeLazyChoices()
    assert 'basic' in lc
    assert 'digest' in lc
    assert 'hawk' in lc
    assert 'custom' in lc
    assert 'foo' not in lc
    assert list(lc) == ['basic', 'custom', 'digest', 'hawk']

auth.add_argument(
    '--auth-type',
    metavar='',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication mechanism to be used.  One of: {0}.

    '''.format(', '.join(sorted(_AuthTypeLazyChoices())))
)

#######################################################################
#  Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:21:28.547959
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert _AuthTypeLazyChoices() == sorted(plugin_manager.get_auth_plugin_mapping().keys())
assert test__AuthTypeLazyChoices___iter__()

auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Authentication type to be used, e.g., basic, digest.

    {CLI_DOC_AUTH_PLUGIN_HOWTO}
    ''')


#######################################################################
# CLI arguments that are forwarded to the request (HTTPie specific).
#######################################################################

request_options = parser.add_argument_group(title='Request Options')


# Generated at 2022-06-13 21:21:30.068199
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('blah')

# Generated at 2022-06-13 21:21:41.222387
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(['basic', 'digest']) == list(_AuthTypeLazyChoices())

auth._add_container_action(
    'append',
    dest='auth_type',
    metavar='AUTH_TYPE',
    type=lambda x: x.lower(),
    choices=_AuthTypeLazyChoices()
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')
proxy.add_argument(
    '--proxy', '-p',
    type=ProxyValidator(),
    default=None,
    help='''
    Specify a proxy in the form [user:password@]host:port.

    To override a proxy set via environment variables, use --no-proxy.

    ''',
)

# Generated at 2022-06-13 21:21:42.965356
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [
        'basic',
        'digest',
    ] == list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:21:52.280387
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    Force the specified authentication type (Basic, Digest).
    Defaults to "auto", which first attempts Basic authentication, and
    if that fails, attempts Digest authentication.

    ''',
)

# Generated at 2022-06-13 21:22:00.436194
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """An example test method."""
    result = _AuthTypeLazyChoices().__contains__('dummy')
    assert result == False

# Generated at 2022-06-13 21:22:01.873555
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == []



# Generated at 2022-06-13 21:22:04.655450
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert dict in _AuthTypeLazyChoices()


_auth_type_lazy_choices = _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:22:17.872664
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify a custom auth plugin.

    This option is for advanced users only.

    The default plugin is "{DEFAULT_AUTH_PLUGIN}".

    Available plugins:

        {','.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

#######################################################################
# Proxy
#######################################################################

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:22:27.884619
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of the authentication plugin to use. Defaults to {default}.
    Available plugins: {choices}

    '''.format(
        default=DEFAULT_AUTH_PLUGIN_NAME,
        choices=', '.join(plugin_manager.get_auth_plugin_mapping())
    )
)

# Generated at 2022-06-13 21:22:39.833798
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    class MockAuthPluginBase(AuthPluginBase):
        name = 'mock'

    class MockAuthPlugin(MockAuthPluginBase):
        auth_type = 'mock'

    assert 'mock' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

    with plugin_manager.context():
        plugin_manager.register(MockAuthPlugin)
        assert 'mock' in _AuthTypeLazyChoices()


# ``requests.request`` keyword arguments.
auth_type = auth.add_argument_group(
    title='Authentication plugin selection'
).add_mutually_exclusive_group(required=False)

# Generated at 2022-06-13 21:22:41.620398
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert ['Basic', 'Digest'] == list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:22:52.369772
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert list(_AuthTypeLazyChoices()) == ['digest', 'jwt', 'oauth1']


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication method to be used. Currently supported: {0}.
    See also the AUTH section of the manual.

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)

# Generated at 2022-06-13 21:23:00.940453
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:23:04.026104
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    >>> _AuthTypeLazyChoices().__contains__('digest')
    True
    >>> _AuthTypeLazyChoices().__contains__('non-existing')
    False
    """


# Generated at 2022-06-13 21:23:20.004698
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    metavar=None,
    help=f'''
    Supported auth types (default is '{DEFAULT_AUTO_DETECT_AUTH_TYPE}'):

    {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)
auth.add_argument(
    '--auth-plugin',
    default=[],
    action='append',
    metavar='AUTH_PLUGIN',
    help='''
    Use the specified AUTH_PLUGIN. Can be repeated.

    '''
)

#######################################################################
# SSL


# Generated at 2022-06-13 21:23:26.398195
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    try:
        list(_AuthTypeLazyChoices())
    except Exception:
        import sys
        import traceback
        exc_info = sys.exc_info()
        print('TRACEBACK:')
        traceback.print_tb(exc_info[2])
        print('EXCEPTION: {}'.format(exc_info[1]))
        raise
    else:
        pass

auth.add_argument(
    '--auth-type', '--auth-plugin',
    type=AuthPluginChoices(),
    default=None,
    help='''
    Force the specified authentication plugin, even if it would not be
    automatically selected for the specified URL.

    '''
)


# Generated at 2022-06-13 21:23:34.886203
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert AUTH_PLUGIN_NAME in auth_type_lazy_choices
    assert list(auth_type_lazy_choices) == sorted(AuthPlugins().get_auth_plugin_mapping().keys())



# Generated at 2022-06-13 21:23:47.675655
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_choices
    assert 'digest' in auth_type_choices
    assert 'plugin1' in auth_type_choices

    # Test iterator
    assert list(auth_type_choices) == ['basic', 'digest', 'plugin1']

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Auth type. Currently supported: {0}.

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)

#######################################################################
# HTTP and HTTPS Proxy
#######################################################################


# Generated at 2022-06-13 21:23:52.205313
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # create an instance of class _AuthTypeLazyChoices
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    # test if the object contains value
    assert 'digest' in auth_type_lazy_choices


# Generated at 2022-06-13 21:24:01.895269
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    klass = _AuthTypeLazyChoices
    assert not klass.__contains__('foo')
    assert ('foo' in klass) is False
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    auth_plugin_mapping['foo'] = object()
    assert ('foo' in klass) is True
    assert 'foo' in klass
    assert len(klass) == (len(auth_plugin_mapping) + 1)
    assert 'foo' in list(klass)
    del auth_plugin_mapping['foo']
    assert ('foo' in klass) is False
    assert 'foo' not in klass
    assert len(klass) == len(auth_plugin_mapping)

# Generated at 2022-06-13 21:24:09.727744
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('_AuthTypeLazyChoices')



# Generated at 2022-06-13 21:24:14.906291
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    options = _AuthTypeLazyChoices()
    assert [list[i] for i in [0, 1, 2]] == list(options)

# Generated at 2022-06-13 21:24:16.254108
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:24:23.522802
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_choices
    assert 'Basic' in auth_type_choices
    assert 'BASIC' in auth_type_choices
    assert 'digest' in auth_type_choices
    assert 'token' in auth_type_choices


# Generated at 2022-06-13 21:24:43.081801
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert(sorted(plugin_manager.get_auth_plugin_mapping().keys()), list(_AuthTypeLazyChoices()))

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism.

    '''
)


# Generated at 2022-06-13 21:24:54.834198
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Type of HTTP authentication to use. The default value is auto which means
    the authentication method will be guessed from the provided credentials.

    Supported types:
        {', '.join(plugin_manager.get_auth_plugin_mapping().keys())}

    '''
)

# Generated at 2022-06-13 21:25:03.904775
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['digest', 'jwt', 'netrc',
                                            'oauth1', 'basic']


auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()



# Generated at 2022-06-13 21:25:08.574056
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'multi-digest' not in _AuthTypeLazyChoices()
test__AuthTypeLazyChoices()
# End unit test for constructor of class _AuthTypeLazyChoices

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Algorithm for calculating the auth – e.g. digest, basic.

    '''
)

auth.add_argument(
    '--auth-host',
    default=None,
    metavar='HOST',
    help='''
    A host to provide the credentials for.

    '''
)

#######################################################################
# Timeouts and retries
################################

# Generated at 2022-06-13 21:25:15.839712
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type', '-t',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication type (derived from the URL if not specified).
    This can be:

        {auth_types}

    '''.format(
        auth_types='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(plugin_manager.get_auth_plugin_mapping().keys()), 60)
        ).strip(),
    )
)

# Generated at 2022-06-13 21:25:17.853415
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert (
        list(_AuthTypeLazyChoices()) ==
        sorted(plugin_manager.get_auth_plugin_mapping().keys()))

# Generated at 2022-06-13 21:25:21.681449
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'basic' in choices
    assert 'aws' in choices
    assert sorted(choices) == sorted(['aws', 'basic', 'digest'])


# Generated at 2022-06-13 21:25:23.514238
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert AUTH_PLUGIN_NAME in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:30.877822
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(['digest', 'jwt', 'basic'])


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    dest='auth_plugin',
    help='''
    The authentication mechanism to be used: {choices}.

    '''.format(
        choices=', '.join(_AuthTypeLazyChoices())
    )
)

# Generated at 2022-06-13 21:25:32.927748
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:26:07.599562
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert [key for key in _AuthTypeLazyChoices()]

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of a registered authentication plugin. Mutually exclusive with
    --auth.

    You can use "--debug" to print out a list of all plugins.

    Use it to specify a custom authentication method, e.g., Digest or
    OAuth 2.0. This is useful when the server uses a non-standard
    authentication scheme.

    '''
)


# Generated at 2022-06-13 21:26:17.821141
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = set(_AuthTypeLazyChoices())
    choices.add('something')
    assert 'something' in choices


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')
ssl.add_argument(
    '--ssl',
    default=False,
    action='store_true',
    help='''
    Verify SSL certificate.

    This option has no effect if the --insecure flag is also set,
    because the SSL verification is disabled altogether in that case.

    '''
)


# Generated at 2022-06-13 21:26:25.533344
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == sorted(_AuthTypeLazyChoices())

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication plugin to use. Use `%(prog)s --debug | grep -i auth` to
    get a list of all available authentication plugins.

    '''
)
auth.add_argument(
    '--auth-plugin',
    dest='auth_type',
    action='append',
    default=None,
    metavar='AUTH_PLUGIN',
    help=SUPPRESS
)


# Generated at 2022-06-13 21:26:27.087548
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:30.442415
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
assert test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:26:33.614254
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type = _AuthTypeLazyChoices()
    assert 'basic' in auth_type
    assert 'digest' in auth_type
    assert 'fake-auth' not in auth_type

# Generated at 2022-06-13 21:26:37.412083
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:41.344753
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert choices.__contains__('digest') is True
    assert choices.__contains__('custom') is False

# Generated at 2022-06-13 21:26:58.554667
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    a = _AuthTypeLazyChoices()
    assert 'basic' in a
    assert 'digest' in a
    assert sorted(list(a)) == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    dest='auth_type',
    metavar='TYPE',
    type=str,
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Auth plugin to use. Type should be one of: {0}.

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

#######################################################################
# HTTP method/verb.
#######################################################################

methods = parser.add_argument_group(title='HTTP method')


# Generated at 2022-06-13 21:27:09.721731
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    '''Test for _AuthTypeLazyChoices and available auth plugins.'''
    # Verify that we have some auth plugins available
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:27:47.618592
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    class _AuthTypeLazyChoicesTest(_AuthTypeLazyChoices):
        pass

    auth_type_test = _AuthTypeLazyChoicesTest()
    assert 'bearer' in auth_type_test
    assert 'digest' in auth_type_test
    assert 'hawk' in auth_type_test
    assert 'ntlm' in auth_type_test
    assert 'aws' in auth_type_test
    assert 'aws-sig-v4' in auth_type_test
    assert 'oauth1' in auth_type_test
    assert 'mock' in auth_type_test


# Generated at 2022-06-13 21:27:58.677388
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    list(lazy_choices)
    'basic' in lazy_choices

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    This is a shortcut to one of the authentication plugins.
    HTTPie looks for an authentication plugin whose name or alias matches the
    provided value.

    e.g. --auth-type=digest will activate the DigestAuth Plugin.
    Use -v to see a list of all registered plugins.

    '''
)

# Generated at 2022-06-13 21:28:01.057029
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    expected = ['basic', 'digest']
    actual = sorted(choices)
    assert expected == actual

# Generated at 2022-06-13 21:28:12.920361
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an authentication mechanism.

    The following mechanisms are available:

        {auth_types}

    The "auto" mechanism (default) detects the scheme from the URL and
    chooses the appropriate mechanism:

    - Basic and Digest auth for "http://" URLs
    - Bearer auth for "https://" URLs
    - Negotiate/NTLM auth for "http://" URLs when the "--negotiate"
      option is specified
    - Any of the above when the "--auth-type" option is explicitly specified

    '''.format(
        auth_types=fmt_auth_plugin_help()
    )
)

# Generated at 2022-06-13 21:28:14.672388
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # pylint:disable=unused-variable
    assert 'BASIC' in _AuthTypeLazyChoices()
    # pylint:enable=unused-variable

# Generated at 2022-06-13 21:28:32.354936
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


# Generated at 2022-06-13 21:28:40.220921
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    A = _AuthTypeLazyChoices()
    assert 'bearer' in A
    assert 'basic' in A
    assert 'digest' in A

auth_type_lazy_choices = _AuthTypeLazyChoices()

auth_type = auth.add_mutually_exclusive_group()
auth_type.add_argument(
    '--auth-type',
    action='store',
    choices=auth_type_lazy_choices,
    help=f'''
    Specify an auth type. By default, HTTPie guesses it based on the --auth
    option value, but this is not always possible.

    The available auth types are:
    {list_plugins()}

    '''
)

# Generated at 2022-06-13 21:28:43.525884
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().assert_contains(
        'basic',
        'digest',
        'hawk',
    )

# Generated at 2022-06-13 21:28:55.951369
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'digest' in auth_type_choices


auth_type_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '--auth-plugin',
    default=None,
    choices=auth_type_choices,
    help='''
    Specify an authentication plugin (or type). By default, HTTPie searches
    the plugin directory (see the --plugins option above) and auto-detects
    the plugin to use (based on the WWW-Authenticate header).

    '''
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')


# Generated at 2022-06-13 21:29:00.892846
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    instance = _AuthTypeLazyChoices()
    assert ('basic' in instance) is True
    assert ('digest' in instance) is True
    assert ('gssnegotiate' in instance) is False

