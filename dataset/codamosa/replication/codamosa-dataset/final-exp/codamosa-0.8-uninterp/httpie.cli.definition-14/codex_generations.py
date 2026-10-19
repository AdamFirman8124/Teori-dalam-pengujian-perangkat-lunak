

# Generated at 2022-06-13 21:19:18.140186
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an HTTP auth type to use. This is useful if you have more than one
    auth mechanism configured. For example, to choose between Basic and Digest
    auth when both have been configured. This is necessary with servers such as
    nginx which do not specify an auth type.

    If not specified, HTTPie chooses the first matching mechanism.

    Also see https://httpie.org/plugins for information about third-party auth
    plugins.

    '''
)


# Generated at 2022-06-13 21:19:31.124194
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.plugins.manager import PLUGINS_DIR
    from httpie.plugins import builtin
    import os
    import glob
    import tempfile

# Generated at 2022-06-13 21:19:42.561719
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'oauth' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of auth plugin used to handle the credentials.

    Alternatively, the name of an auth plugin. Type "http --auth-type=BASIC"
    to see a detailed description of the built-in BASIC auth plugin.

    '''
)
auth.add_argument(
    '--auth-host',
    metavar='HOST',
    default=None,
    help='''
    Hostname to match against the "Host" header.
    Used by the built-in BASIC authentication plugin.

    '''
)

# Generated at 2022-06-13 21:19:46.892575
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    setAttr(plugin_manager, 'get_auth_plugin_mapping', lambda: {'item': None})
    assert 'item' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:19:50.218783
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert _AuthTypeLazyChoices() == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )

# Generated at 2022-06-13 21:20:05.235949
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.auth import BasicAuth
    class TestAuth(BasicAuth):
        auth_type = 'test'
    plugin_manager.register(TestAuth)
    assert 'test' in plugin_manager.get_auth_plugin_mapping()
    assert 'test' in _AuthTypeLazyChoices()
    plugin_manager.unregister(TestAuth)


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    '''
)

auth.add_argument(
    '--auth-host',
    default=None,
    help='''
    The authentication domain (host name only or host:port).

    '''
)

# Generated at 2022-06-13 21:20:08.215560
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(list(choices)) == sorted(list(choices))



# Generated at 2022-06-13 21:20:09.873980
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices().__contains__('foobar')


# Generated at 2022-06-13 21:20:12.024066
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for value in _AuthTypeLazyChoices():
        assert value in plugin_manager.get_auth_plugin_mapping()


# Generated at 2022-06-13 21:20:20.611824
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_types = list(_AuthTypeLazyChoices())
    assert 'basic' in auth_types
    assert 'digest' in auth_types

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Which authentication scheme to use.
    Support for other schemes can be added by installing plugins.

    '''
)
auth.add_argument(
    '--auth-plugin', '-A',
    metavar='PLUGIN_SPEC',
    default=[],
    action='append',
    help='''
    Override the authentication plugin to use.
    Can be specified multiple times.

    '''
)

#######################################################################
# Other settings
#######################################################################

settings = parser.add_argument_

# Generated at 2022-06-13 21:20:25.117564
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:37.780605
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    '''
)
auth.add_argument(
    '--auth-type-help',
    action='help',
    help='''
    Available authentication mechanism plugins:

    {auth_plugins_doc}

    '''.format(
        auth_plugins_doc=get_auth_plugins_doc()
    )
)

# Generated at 2022-06-13 21:20:49.766323
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    plugin_manager.set_auth_plugin_mapping({
        'httpie': 'Do not touch me please',
        'aws4': 'aws4',
        'aws4-hmac-sha256': 'aws4-hmac-sha256',
    })
    assert 'aws4' in auth_type_lazy_choices
    assert 'aws4-hmac-sha256' in auth_type_lazy_choices
    assert 'httpie' in auth_type_lazy_choices
    assert 'httpie-oauth' not in auth_type_lazy_choices
    assert 'httpie-hmac-auth' not in auth_type_lazy_choices




# Generated at 2022-06-13 21:21:01.372207
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The name of a registered Auth plugin.
    See `http --debug plugins-auth`
    to see the list of available plugins.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    help='''
    Don't use HTTP authentication if server responds with a 401 status
    code (default).

    Turning this off is useful to force the use of HTTP Basic Authentication,
    for example, but it's not recommended as it makes the client vulnerable to
    man-in-the-middle attacks.

    '''
)

#######################################################################
# HTTP
################################################################

# Generated at 2022-06-13 21:21:13.214975
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [item for item in _AuthTypeLazyChoices()] == [None, 'digest', 'hmac']


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism to be used.

    '''
)


# Generated at 2022-06-13 21:21:21.230559
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    items = _AuthTypeLazyChoices()
    assert items.__contains__('digest')
    assert items in {'digest'}
    assert 'digest' in items
    assert list(sorted(i for i in items if i.startswith('basic'))) == ['basic']

auth.add_argument(
    '--auth-type', '-t',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Force a custom auth mechanism, overriding the default auto-detection.

    For instance, use "--auth-type=digest" for Digest auth.

    '''
)

# Generated at 2022-06-13 21:21:30.887222
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_types = _AuthTypeLazyChoices()
    # Should be there because it is built-in.
    assert 'digest' in auth_types
    # Should be there because the extra plugin is persisted in the plugin
    # manager.
    assert 'my_extra_auth' in auth_types
    # Should not be there because it hasn't been registered/persisted.
    assert 'extra_auth' not in auth_types

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of auth scheme to use for the request.

    This option is ignored unless ``--auth`` is used.

    See ``--auth-plugin`` for a programmatic way of choosing
    an authentication plugin and overriding its options.

    '''
)

# ``requ

# Generated at 2022-06-13 21:21:41.862460
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for key in _AuthTypeLazyChoices():
        pass

# ``requests.auth.HTTPBasicAuth`` keyword arguments.
auth_basic = parser.add_argument_group(title='Basic/Digest Auth Options')

# Generated at 2022-06-13 21:21:48.727563
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for arg_name in _AuthTypeLazyChoices():
        assert arg_name in plugin_manager.get_auth_plugin_mapping()
        assert arg_name in _AuthTypeLazyChoices()
    assert 'foo' not in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Algorithm to use for the HTTP authentication.

    Available methods:

        {list_of_auth_plugins()}

    '''
)

# Generated at 2022-06-13 21:21:52.915251
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    empty_choices = _AuthTypeLazyChoices()
    assert 'Basic' in empty_choices
    assert 'Digest' in empty_choices
    assert 'NoOp' not in empty_choices

# Generated at 2022-06-13 21:22:08.630176
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert next(_AuthTypeLazyChoices()) == "basic"

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Use `--debug` to see a list
    of available auth plugins.
    '''
)

#######################################################################
# HTTPS
#######################################################################

https = parser.add_argument_group(title='HTTPS')
https.add_argument(
    '--verify', '-k',
    help='''
    Set to "yes" to check the host's SSL certificate. You can also pass the
    path to a CA_BUNDLE file for private cert. You can also set the
    REQUESTS_CA_BUNDLE environment variable.

    '''
)


# Generated at 2022-06-13 21:22:21.556593
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'foo' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism. The default is "auto" which will
    first try "basic", then "digest", then "aws" if the --auth
    parameter value is of the form "<key-id>:<key-secret>".

    Available types are as follows:

    '''
)

# Generated at 2022-06-13 21:22:22.429954
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Nothing
    pass

# Generated at 2022-06-13 21:22:34.578266
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lc = _AuthTypeLazyChoices()
    assert 'basic' in lc
    assert list(lc) == ['basic']

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication type to be used.
    The default is "basic".

    ''',
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')


# Generated at 2022-06-13 21:22:46.938632
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    atlc = str(_AuthTypeLazyChoices())
    assert atlc == (
        "['digest', 'hawk', 'jwt', 'netrc', 'oauth1', 'oauth2', 'spnego']"
    )

# Note that this argument doesn't need ``choices`` kwarg because it's resolved
# at runtime.
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    help='''
    Specify a custom auth plugin (Only relevant if --auth is used).

    Use `http --debug auth` to see a list of available plugins.

    ''',
    choices=_AuthTypeLazyChoices()
)


#######################################################################
# Protocol
#######################################################################


# Generated at 2022-06-13 21:22:55.660594
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins import AuthPlugin
    assert 'foobar' not in _AuthTypeLazyChoices()

    class FooBarAuthPlugin(AuthPlugin):
        auth_type = 'foobar'

    assert 'foobar' not in _AuthTypeLazyChoices()

    plugin_manager.register(FooBarAuthPlugin)
    assert 'foobar' in _AuthTypeLazyChoices()
    plugin_manager.deregister(FooBarAuthPlugin)


# Generated at 2022-06-13 21:23:03.480685
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(_AuthTypeLazyChoices()) == set(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The value should be one of:

        {auth_plugin_names}

    . If not provided, HTTPie tries to guess it based on the --auth option
    value, falling back to basic.

    '''.format(auth_plugin_names=', '.join(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )))
)

# Generated at 2022-06-13 21:23:05.737095
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:08.369709
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'A' in _AuthTypeLazyChoices()
    assert 'B' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:23:18.328270
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in auth_type_lazy_choices
    assert 'ntlm' in auth_type_lazy_choices
    assert 'jwt' not in auth_type_lazy_choices


auth_type_help = (
    f'Choose the authentication method to use. '
    f'Available choices depend on the installed plugins. '
    f'Default: {DEFAULT_AUTH_PLUGIN_NAME}'
)

# Generated at 2022-06-13 21:23:28.738250
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'custom']


# Generated at 2022-06-13 21:23:36.178820
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help='''
    Specify the authentication mechanism to be used. The value can be either
    the name of a built-in mechanism or a fully-qualified import path to a
    custom authentication plugin.

    '''
)

auth.add_argument(
    '--auth-no-challenge',
    dest='auth_no_challenge',
    default=None,
    action='store_true',
    help='''
    If set, the client will not attempt to send HTTP auth challenges in
    response to an HTTP status code 401, but will instead return the HTTP
    status code immediately.

    '''
)


# Generated at 2022-06-13 21:23:48.771060
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) \
        == sorted(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism: (basic|digest|aws).
    By default, it is guessed based on the --auth option.

    '''
)
auth.add_argument(
    '--auth-type-negotiate',
    action='store_true',
    help='''
    If set, HTTPie will use the negotiable authentication mechanism
    (`SPNEGO`_) to authenticate with the server.

    .. _`SPNEGO`: http://en.wikipedia.org/wiki/SPNEGO

    '''
)


# Generated at 2022-06-13 21:23:59.788603
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    names = [name for name in _AuthTypeLazyChoices()]
    assert names == sorted(name for name, _ in plugin_manager.get_auth_plugins())
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the AUTH_TYPE plugin to use.

    Plugins:

        {plugins}

    '''.format(
        plugins='\n        '.join(
            wrap(', '.join(
                sorted(plugin_manager.get_auth_plugin_mapping().keys())
            ), 80)
        )
    )
)


# Generated at 2022-06-13 21:24:02.414469
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(plugin_manager.get_auth_plugin_mapping().keys()) == list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:24:09.944029
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'custom' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'NTLM' in _AuthTypeLazyChoices()
    assert all(isinstance(item, str) for item in _AuthTypeLazyChoices())


# Generated at 2022-06-13 21:24:25.593036
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'kerberos' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:24:29.525689
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'azure' in _AuthTypeLazyChoices()
    assert 'foo' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:32.249321
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:34.480277
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(sorted(iter(_AuthTypeLazyChoices()))) == sorted(list(iter(_AuthTypeLazyChoices())))


# Generated at 2022-06-13 21:24:52.841707
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)
    assert 'basic' in choices
    assert 'asdfasdf' not in choices


# Generated at 2022-06-13 21:25:02.684513
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert {'basic', 'digest'}.subset(set(auth_type_lazy_choices))


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Authentication type (default: basic).

    The following types are supported:

    {plugin_manager.get_plugins_docstring(
        group='auth',
        heading_level=3,
        docstring_prefix=' ' * 6,
    ).rstrip()}

    '''
)


# Generated at 2022-06-13 21:25:12.639696
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    class MockAuthPlugins:
        def __init__(self, plug_dict):
            self.plug_dict = plug_dict
            self.__name__ = 'MockAuthPlugins'

        def get_auth_plugin_mapping(self):
            return self.plug_dict

    class MockPluginManager:
        def get_auth_plugin_mapping(self):
            return MockAuthPlugins(dict(foo=1, bar=2, foobar=3)).get_auth_plugin_mapping()

    plugin_manager = MockPluginManager()

    assert hasattr(plugin_manager, 'get_auth_plugin_mapping')
    assert 'foo' in _AuthTypeLazyChoices()
    assert 'bar' in _AuthTypeLazyChoices()
    assert 'foobar' in _AuthTypeLazyChoices()
   

# Generated at 2022-06-13 21:25:20.250439
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == \
        ['basic', 'digest', 'hawk', 'netrc', 'oauth1', 'aws4-hmac-sha256']


auth_type_validator = AuthTypeValidator(
    'Authentication type "{0}" not supported.',
    choices=_AuthTypeLazyChoices(),
)


# Generated at 2022-06-13 21:25:28.913999
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices"""

    choices = _AuthTypeLazyChoices()
    assert sorted(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:25:37.812183
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_types = [
        'digest',
        'jwt',
        'hawk',
    ]
    mapping = {
        'digest': httpie.plugins.auth.DigestAuthPlugin,
        'jwt': httpie.plugins.auth.JWTAuthPlugin,
        'hawk': httpie.plugins.auth.HAWKAuthPlugin,
    }
    for auth_type in auth_types:
        assert auth_type in _AuthTypeLazyChoices()

    for auth_type, plugin_class in mapping.items():
        assert plugin_class == plugin_manager.get_auth_plugin_mapping()[auth_type]


# Generated at 2022-06-13 21:25:50.307474
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_list = _AuthTypeLazyChoices()
    assert iter(lazy_list)
    assert 'basic' in lazy_list
    assert 'digest' in lazy_list
    assert len(list(lazy_list)) == 2


auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    type=str,
    help=f'''

    Select authentication mechanism. HTTPie currently provides the following:

        {', '.join(plugin_manager.get_auth_plugin_mapping())}

    New mechanisms can be added via plugins.

    ''',
    choices=_AuthTypeLazyChoices()
)

# Generated at 2022-06-13 21:26:03.773422
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == list(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom auth plugin. See http://httpie.org/plugins for more info.
    By default, HTTPie tries to guess the auth plugin based on the supplied
    URL and `--auth` option.

    Available plugins:

        {0}

    '''.format(
        ', '.join(plugin_manager.get_auth_plugin_mapping().keys())
    )
)

# Generated at 2022-06-13 21:26:20.086457
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert not len(_AuthTypeLazyChoices()) == 0

auth_type = auth.add_mutually_exclusive_group()
auth_type.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=str,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an auth plugin to be used.
    '''
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='''
    Determine the auth scheme to use without sending the actual request.
    Disable automatic authentication challenge (i.e., preemptive authentication)
    Useful with non-standard authentication schemes,
    such as Amazon S3.

    '''
)


# Generated at 2022-06-13 21:26:22.966920
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'here-is-no-such-auth-method' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:27:02.417209
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'http' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type', '-t',
    type=str.lower,
    default='auto',
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help=f'''
    Choose an auth plugin. The default is "auto" which means that the plugin
    is chosen based on the provided information (empty for none, username for
    basic, and token for token). If the info is a URL, then the host is used
    to lookup the auth plugin in your config file.

    ''',
)


# Generated at 2022-06-13 21:27:11.619228
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

_CLI_HELP_AUTH_TYPE_CHOICES = '''
    Type of authentication to use. Defaults to 'basic'.

    Available choices:
    {auth_plugins_choices}

    You will have to install the corresponding plugin first. E.g.::

        $ pip install httpie-ntlm

    '''

# class _AuthTypeHelpAction(Action):
#     def __call__(self, parser, namespace, values, option_string=None):
#         auth_plugins_choices = plugin_manager.get_auth_plugin_mapping().keys()
#         msg = _CLI_HELP_AUTH_TYPE_CHOICES.format(
#             auth_plugins_choices=auth_plugins_choices
#         )
#

# Generated at 2022-06-13 21:27:22.089151
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )

    assert choices == list(_AuthTypeLazyChoices())
    assert choices[0] in _AuthTypeLazyChoices()
    assert choices[-1] in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:27:32.945502
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


auth_type_validator = AuthPluginValidator(
    'Invalid auth plugin name. See `http --help-auth`')

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    type=auth_type_validator,
    metavar='TYPE',
    help='''
    The name of a plugin (e.g., digest, oauth1) that can
    handle the specified --auth credentials.

    '''
)

#######################################################################
# Redirects and following
#######################################################################

follow = parser.add_argument_group(title='Redirects')


# Generated at 2022-06-13 21:27:41.633722
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():

    def test_contains(module_name):
        mock_module = Mock()
        mock_module.plugin_class = AuthPlugin
        with patch('httpie.core.plugins.plugin_manager.get_plugin_module', return_value=mock_module):
            assert module_name in _AuthTypeLazyChoices()

    test_contains('digest')
    test_contains('JWT')
    test_contains('hawk')
    assert 'no_such_auth' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:27:57.456719
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    print(list(_AuthTypeLazyChoices()))

auth.add_argument(
    '--auth-type', '--auth-plugin',
    dest='auth_plugin',
    metavar='NAME',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify an authentication plugin.

    Available plugins: {0}

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:28:04.348428
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert iter(_AuthTypeLazyChoices()) == iter(sorted(plugin_manager.get_auth_plugin_mapping().keys()))


auth.add_argument(
    '--auth-type',
    default=defaults.AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism for the request (the default is '%(default)s'):

    {auth_plugins}

    '''.format(
        auth_plugins='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(
                ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())), 60
            )
        )
    )
)

#######################################################################
# Timeouts


# Generated at 2022-06-13 21:28:14.734721
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    return sorted(_AuthTypeLazyChoices())
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    type=plugin_manager.get_auth_plugin_mapping().get,
    default=None,
    help='''
    Specify the auth mechanism. If no explicit type is given, then HTTPie
    tries them in the order they are listed here:

        {auth_plugins_list}

    '''.format(
        auth_plugins_list='\n'.join(
            (8 * ' ') + plugin_name for plugin_name
            in sorted(plugin_manager.get_auth_plugin_mapping().keys())
        ).strip()
    )
)

#######################################################################
# HTTP method
#######################################################################

# Generated at 2022-06-13 21:28:28.233292
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    plugin_manager = MagicMock()
    auth_type = {
        'auth_type': 'AuthType',
        'auth_class': 'AuthClass'
    }
    plugin_manager.get_auth_plugin_mapping.return_value = {
        'plugin_name': auth_type
    }
    assert list(_AuthTypeLazyChoices.__iter__(plugin_manager)) == ['plugin_name']

# Generated at 2022-06-13 21:28:38.608756
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert set(['basic', 'digest']) == set(_AuthTypeLazyChoices())


auth.add_argument('--auth-type',
                  metavar='TYPE',
                  choices=_AuthTypeLazyChoices(),
                  help=f'''
    The authentication mechanism to be used: {', '.join(sorted(list(plugin_manager.get_auth_plugin_mapping().keys())))}.

    ''')