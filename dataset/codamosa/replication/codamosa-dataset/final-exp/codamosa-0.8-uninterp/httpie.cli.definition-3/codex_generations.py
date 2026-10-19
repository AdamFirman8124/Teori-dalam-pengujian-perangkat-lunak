

# Generated at 2022-06-13 21:19:11.359825
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'foo' not in choices

# Generated at 2022-06-13 21:19:13.677466
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'custom7' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:19:25.858030
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices.__contains__(_AuthTypeLazyChoices(), 'digest')


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=plugin_manager.resolve_plugin,
    choices=_AuthTypeLazyChoices(),
    help=argparse.SUPPRESS
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')
cookies.add_argument(
    '--cookie', '-C',
    dest='cookies',
    action='append',
    metavar='NAME=VALUE',
    help='''
    Add a cookie to the request. You may use multiple --cookie
    options.

    ''',
)

# Generated at 2022-06-13 21:19:38.513692
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:19:50.031085
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    Default: {default}
    '''.format(default=DEFAULT_AUTH_PLUGIN)
)

auth.add_argument(
    '--auth-digest',
    action='store_const',
    const=(DEFAULT_AUTH_PLUGIN,),
    dest='auth_type',
    help='''
    Use HTTP Digest Authentication. Shortcut for --auth-type=digest.
    '''
)

# Generated at 2022-06-13 21:19:53.051424
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'nonexisting' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:08.025019
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified auth plugin.
    If not provided, the plugin is guessed from --auth value.

    Currently available plugins:
    {available_auth_types}
    '''.format(
        available_auth_types=', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    )
)

#######################################################################
# Transport and Tunneling
#######################################################################
transport = parser.add_argument_group(title='Transport and Tunneling')
transport.add

# Generated at 2022-06-13 21:20:10.068751
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from collections import Iterable
    assert isinstance(iter(_AuthTypeLazyChoices), Iterable)

# Generated at 2022-06-13 21:20:13.960744
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    assert 'basic' in auth_type_lazy_choices



# Generated at 2022-06-13 21:20:22.282013
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'jwt' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:27.605783
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:20:30.403795
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:20:33.044798
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping()))


# Generated at 2022-06-13 21:20:35.111855
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert ('basic') in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:47.010740
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in lazy_choices
    assert 'Negotiate' in lazy_choices
    assert 'unknown' not in lazy_choices


# Generated at 2022-06-13 21:20:57.051808
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    '''
    Unit test for method __contains__ of class _AuthTypeLazyChoices
    '''
    # Unit test for method __contains__ of class _AuthTypeLazyChoices
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'pin' not in _AuthTypeLazyChoices()
    assert 'Bearer' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:21:09.303071
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'test' in auth_type_lazy_choices
    assert 'test' in auth_type_lazy_choices

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism.

    ''',
)
auth.add_argument(
    '--auth-host', '--host',
    default=None,
    help='''
    The hostname to provide the authentication for. Useful when the hostname is
    not part of the URL (e.g., Digest auth).

    ''',
)

#######################################################################
# HTTP and HTTPS proxy
#######################################################################

proxy_group = parser.add_

# Generated at 2022-06-13 21:21:21.897328
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    for item in _AuthTypeLazyChoices():
        pass

# ``requests.request`` keyword arguments.
auth_types = auth.add_mutually_exclusive_group(required=False)
auth_types.add_argument(
    '--auth-type',
    default=None,
    help='''
    Specify an authorization plugin. By default, the plugin is guessed
    from the provided credentials, i.e., if they look like a token,
    the "Bearer" plugin is used by default.
    '''
)
auth_types.add_argument(
    '--auth-type=',
    help=argparse.SUPPRESS,
    choices=_AuthTypeLazyChoices()
)

#######################################################################
# SSL
#######################################################################


# Generated at 2022-06-13 21:21:30.504021
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_AuthTypeLazyChoices(), _AuthTypeLazyChoices)
    assert 'basic' in _AuthTypeLazyChoices()
    assert sorted(['basic', 'digest']) == list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    default=AUTH_PLUGIN_MAP['basic'],
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Specify a custom auth plugin (by entry point name).
    Available plugins: {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)

#######################################################################
# Timeouts.
#######################################################################



# Generated at 2022-06-13 21:21:34.268378
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(iter(_AuthTypeLazyChoices())) == ['digest', 'jwt', 'netrc', 'oauth1', 'plugin', 'basic']


# Generated at 2022-06-13 21:21:45.563987
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


_auth_type_lazy_choices = _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:47.022326
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:21:49.155692
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    items = _AuthTypeLazyChoices()
    item = items.__iter__().__next__()
    assert item in items


# Generated at 2022-06-13 21:22:01.560522
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert set(str(x) for x in _AuthTypeLazyChoices()) == {'basic', 'digest'}
    #
    #
    plugin_manager.deregister_auth_plugin(DigestAuthPlugin)
    assert set(str(x) for x in _AuthTypeLazyChoices()) == {'basic'}
    #
    plugin_manager.deregister_auth_plugin(BasicAuthPlugin)
    assert set(str(x) for x in _AuthTypeLazyChoices()) == set()



# Generated at 2022-06-13 21:22:14.092321
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=plugin_manager.load_auth_plugin,
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of auth plugin to use.
    If the type is not provided, the appropriate plugin is automatically
    detected by inspecting the provided credentials.

    The following types are available:

        {plugins}

    '''.format(
        plugins=', '.join(sorted(plugin_manager.get_auth_plugin_mapping()))
    )
)

# Generated at 2022-06-13 21:22:17.985108
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'digest' in auth_type_lazy_choices


# Generated at 2022-06-13 21:22:27.951814
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    for choice in choices:
        assert choice in choices
        assert choices.__contains__(choice)
    assert 'Basic' in choices
    assert choices.__contains__('Basic')
    assert 'Digest' in choices
    assert choices.__contains__('Digest')
    try:
        assert 'OAuth2' in choices
        assert choices.__contains__('OAuth2')
    except AssertionError:
        pass  # OAuth is not a default plugin
    try:
        assert 'hawkAuth' in choices
        assert choices.__contains__('hawkAuth')
    except AssertionError:
        pass  # Hawk is not a default plugin
    assert 'nonExistentAuthType' not in choices

# Generated at 2022-06-13 21:22:39.832650
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' not in _AuthTypeLazyChoices()

# ``requests.request`` keyword arguments.
auth.add_argument(
    '--auth-type',
    default=None,

    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The available types depend on
    the plugins that are installed. Currently, the following types are supported:

        {auth_types}

    '''.format(
        auth_types=', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    )
)

# Generated at 2022-06-13 21:22:51.322377
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'bearer' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:22:54.514616
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_types = list(_AuthTypeLazyChoices())
    assert 'basic' in auth_types


# Generated at 2022-06-13 21:23:09.282388
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    _AuthTypeLazyChoices must be iterable
    """
    _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to use. The value can be One of:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)
auth.add_argument(
    '--auth-send',
    default='header',
    choices=['header', 'query'],
    help='''
    By default, HTTPie will send the credentials as an Authorization
    header. Using "query" will instead pass the credentials via an HTTP query
    parameter.

    '''
)

# Generated at 2022-06-13 21:23:18.709686
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert isinstance(_AuthTypeLazyChoices, list)

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authorization plugin to use.

    If not provided, and the username or the password contain special
    characters, the "netrc" plugin is used. Otherwise, the default plugin is
    "basic".

    For more info, see the `Authentication Plugins`_ section.

    .. _Authentication Plugins: {auth_plugins_docs}

    '''.format(auth_plugins_docs=AUTH_PLUGINS_DOCS_URL),
)

# Generated at 2022-06-13 21:23:19.720726
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:26.075351
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():

    class MockPlugin(BaseAuthPlugin):
        auth_type = 'foo'

        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, r):
            pass


    class MockPluginManager:

        @classmethod
        def register_plugin(cls, plugin, name=None):
            pass

        @classmethod
        def get_auth_plugin_mapping(cls):
            return {'foo': MockPlugin}


    class MockArgs:
        auth_type = None

    with mock.patch('httpie.cli.argtypes.plugin_manager', MockPluginManager):
        choices = _AuthTypeLazyChoices()
        assert list(choices) == ['foo']



# Generated at 2022-06-13 21:23:34.584803
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['digest', 'generic']


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Specify an authentication handler. By default, HTTPie tries to guess
    the right one.

    '''
)

auth.add_argument(
    '--auth-auth-type',
    default=None,
    help='''
    DEPRECATED, use --auth-type instead.

    Shortcut for ``--auth-type=generic``.
    '''
)


# Generated at 2022-06-13 21:23:36.620822
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'jwt' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:23:49.296023
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # test for partial match
    assert list(filter(bool, 'basic' in _AuthTypeLazyChoices())) == []
    assert list(filter(bool, 'Digest' in _AuthTypeLazyChoices())) != []

    assert list(filter(bool, 'digest' in _AuthTypeLazyChoices())) == []
    assert list(filter(bool, 'Digest' in _AuthTypeLazyChoices())) != []

    assert list(filter(bool, 'digest' in _AuthTypeLazyChoices())) == []
    assert list(filter(bool, 'Digest' in _AuthTypeLazyChoices())) != []



# Generated at 2022-06-13 21:24:00.232704
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    A = _AuthTypeLazyChoices  # shortcut
    assert 'Basic' in A(), 'Basic auth plugin should be present'
    assert 'Digest' in A(), 'Digest auth plugin should be present'
    assert A() == {'Basic', 'Digest'}, 'Keys should be present'
    assert 'Basic' in sorted(A())[0], 'Basic should be first'
    assert 'Digest' in sorted(A())[1], 'Digest should be second'
    assert len(A()) == 2, 'There should be two auth plugins'


# Generated at 2022-06-13 21:24:08.897490
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
_AuthTypeLazyChoices.__doc__ = '''
    Force using a specific method (Basic, Digest) even if the server
    doesn't advertise support for it [{choices}].

    '''.format(
        choices=', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())
        )
    )
auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help=None,
)

#######################################################################
# TLS
#######################################################################

tls = parser.add_argument_group(title='TLS Options')

# Generated at 2022-06-13 21:24:11.450784
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert not 'invalid' in choices

# Generated at 2022-06-13 21:24:28.011623
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    >>> _AuthTypeLazyChoices().__iter__().__next__()
    'basic'
    """


# Generated at 2022-06-13 21:24:33.042274
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_keys = iter(_AuthTypeLazyChoices())
    assert next(lazy_keys) == 'digest'
    assert next(lazy_keys) == 'jwt'
    assert next(lazy_keys) == 'oauth1'



# Generated at 2022-06-13 21:24:34.287483
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:40.792921
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth_type_help = f'''
    Supported authentication types:

        {", ".join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''


auth_type_default_help = (
    'Specifying the type of authentication used'
    ' when --auth is specified without a colon (:).'
    ' It defaults to "basic" but can also be set'
    ' to the empty string to let HTTPie prompt'
    ' for the type.'
)

auth_type = parser.add_argument_group(title='Authentication Options')

# Generated at 2022-06-13 21:24:53.044000
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism.

    The default is "auto", which means that HTTPie tries to auto detect the
    auth mechanism based also on the provided credentials, or falls back to
    Basic.

    ''',
)

#######################################################################
# HTTP and HTTPS
#######################################################################

http = parser.add_argument_group(title='HTTP')

# Generated at 2022-06-13 21:24:56.884631
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'oauth2' in _AuthTypeLazyChoices()

    assert 'not-a-real-type' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:00.221096
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    Unit test for method __iter__ of class _AuthTypeLazyChoices
    """
    assert sorted(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:25:08.221775
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins import default_plugins as plugins

    assert "basic" in _AuthTypeLazyChoices()
    assert "digest" in _AuthTypeLazyChoices()

    # A nonexistent plugin name.
    assert "foo" not in _AuthTypeLazyChoices()

    plugin_manager.unload_all(plugins)

    # When there are no plugins, choices shouldn't contain anything.
    assert len(_AuthTypeLazyChoices()) == 0


# Generated at 2022-06-13 21:25:11.922668
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping())

# Generated at 2022-06-13 21:25:14.914707
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert plugin_manager._load_plugins()
    assert 'digest' in _AuthTypeLazyChoices()
assert test__AuthTypeLazyChoices___contains__()

# Generated at 2022-06-13 21:25:47.458723
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:25:55.823326
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The type of HTTP authentication to use.

    --auth-type=auto
        Automatically detect the type (the default).

    --auth-type=basic
        Digest HTTP authentication (RFC 2617).

    --auth-type=digest
        Digest HTTP authentication (RFC 2617).
    '''
)


# Generated at 2022-06-13 21:26:02.819379
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert tuple(_AuthTypeLazyChoices()) == tuple(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
auth_type = auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify an authentication plugin.
    There is no need to use this option if the scheme
    of the URL is one of: basic, digest.

    '''
)



# Generated at 2022-06-13 21:26:12.632457
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices

auth.add_argument(
    '--auth-type',
    default='auto',
    type=AuthPlugin,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The method used to perform the authentication (default: "auto", which
    tries Basic first and then Digest).

    Supported types:

    {supported_plugins}

    '''
        .format(
            supported_plugins=', '.join(plugin_manager.get_auth_plugin_mapping().keys()),
        )
)

# Generated at 2022-06-13 21:26:23.816130
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert len([*_AuthTypeLazyChoices()]) > 0


auth_type_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    choices=auth_type_choices,
    metavar='TYPE',
    help=(
        'Set the authentication plugin to use. '
        'Currently, supported auth types are: '
        '{}.'.format(', '.join(auth_type_choices))
    )
)


# Generated at 2022-06-13 21:26:37.720671
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():  # noqa
    from httpie.core import main

    main.plugin_manager = plugin_manager = Mock()
    lazy_choices = _AuthTypeLazyChoices()
    plugin_manager.get_auth_plugin_mapping.return_value = {'a': 'b'}
    assert 'a' in lazy_choices
    assert 'c' not in lazy_choices


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported:

    Basic, Digest

    ''',
)

#######################################################################
# Custom headers
#######################################################################


# Generated at 2022-06-13 21:26:41.665893
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'omitted' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:58.666162
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    import sys
    choices_set = set(_AuthTypeLazyChoices())
    assert choices_set == plugin_manager.get_auth_plugin_mapping().keys()
    print("method __iter__ of class _AuthTypeLazyChoices completed successfully", file=sys.stderr)



# Generated at 2022-06-13 21:27:04.697797
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(iter(_AuthTypeLazyChoices())) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys())
auth.add_argument(
    '--auth-type',
    type=plugin_manager.get_auth_plugin_class,
    choices=_AuthTypeLazyChoices(),
    help=f'''\
    The authentication mechanism to use.

    Available choices:
    {_format_choices_list(plugin_manager.get_auth_plugin_mapping().keys())}

    For more info on each auth type, try:

        http --help-auth-type <AUTH_TYPE>

    '''
)


#######################################################################
# SSL
#######################################################################
ssl = parser.add_argument_group(title='SSL Options')

# Generated at 2022-06-13 21:27:12.416762
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Authentication type for use with --auth.
    If this option is specified, the value can be the auth plugin name
    or any shorthand prefix of it. Otherwise, it is inferred from the
    specified --auth value.

    The following plugins are enabled:
        {plugin_list}

    See `http --help-auth` for more information.

    '''.format(plugin_list='\n        '.join(iter(_AuthTypeLazyChoices())))
)

# Generated at 2022-06-13 21:28:20.729476
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_types = _AuthTypeLazyChoices()
    assert 'bearer' in auth_types
    assert plugin_manager.get_auth_plugin_mapping() != {}
    assert 'bearer' in plugin_manager.get_auth_plugin_mapping()
    assert 'basic' in auth_types
    assert 'digest' in auth_types


# Generated at 2022-06-13 21:28:33.738720
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__(): pass
_AuthTypeLazyChoices.__doc__ = '''
    Type of authentication.
    '''
auth.add_argument(
    '--auth-type',
    default=DEFAULT_AUTH_PLUGIN,
    choices=_AuthTypeLazyChoices(),
    help='''
    Type of authentication.

    The default is appropriate for most HTTP servers.
    To enable Digest and/or Kerberos authentication, use:

        --auth-type=digest
        --auth-type=kerberos

    '''
)

auth.add_argument(
    '--auth-store',
    metavar='KEY',
    help='''
    Credentials to be used for Digest and Basic authentication may be
    obtained from a netrc file using the specified KEY.

    '''
)
#######################################################################


# Generated at 2022-06-13 21:28:49.868520
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    '''
    Test Auth Type Lazy Choices
    '''
    assert 'bearer' in _AuthTypeLazyChoices()

_auth_help_suffix = '''
    .. note::

        The auth plugins are loaded from the command line parser
        and from the common configuration.

        To enable the auth plugins from this config, use:

            $ http --session=foo --auth-type=digest ...

        To enable the auth plugins from your config file, use:

            http:
              # your config values
              auth-types:
              - digest
              - oauth2

    '''

# Generated at 2022-06-13 21:28:59.773595
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices()[0]

_auth_type_choices = _AuthTypeLazyChoices()

define_auth = auth.add_mutually_exclusive_group(required=False)
define_auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_auth_type_choices,
    help='''
    Auth plugin for use in request.
    The default is '{default}'.

    For the list of available auth plugins, use 'http --debug --auth-type'.

    '''.format(
        default=DEFAULT_AUTH_PLUGIN_NAME,
    )
)


#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument

# Generated at 2022-06-13 21:29:10.977114
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    d = _AuthTypeLazyChoices()
    assert 'basic' in d
    assert list(d) == [(n, n) for n in sorted(plugin_manager.get_auth_plugin_mapping().keys())]

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    help='''
    TYPE of authentication to use. Currently supported:

        * basic
        * digest

    The default is "basic".
    It is also the default when --auth is used without a colon (:) separator.

    ''',
    default='basic',
    choices=_AuthTypeLazyChoices(),
)