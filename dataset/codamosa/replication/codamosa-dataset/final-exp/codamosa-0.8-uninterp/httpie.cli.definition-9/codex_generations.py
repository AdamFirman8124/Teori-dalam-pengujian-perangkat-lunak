

# Generated at 2022-06-13 21:19:17.588549
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert tuple(sorted(_AuthTypeLazyChoices())) == (
        'basic',
        'digest',
        'hawk',
        'jwt',
        'netrc',
        'ntlm',
        'oauth1',
        'oauth2',
    )



# Generated at 2022-06-13 21:19:30.806182
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(_AuthTypeLazyChoices())

auth_type_validator = AuthPluginValidator(
    'You specified an unsupported authentication plugin.'
)

# Generated at 2022-06-13 21:19:42.139704
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert len(choices) > 0
    iter(choices)
    assert all(choice in choices for choice in choices)

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    dest='auth_plugin',
    help=f'''
    Specify the authentication scheme, apply it to the provided credentials,
    and embed the resulting Authorization/Proxy-Authorization header in the
    request(s).

    Available authentication schemes:
{plugin_manager.get_auth_plugin_help()}

    '''
)

ignore_stdin = argparse.ArgumentParser(
    add_help=False,  # handled by the top-level parser
    parents=[parser],
)

#######################################################################


# Generated at 2022-06-13 21:19:52.215757
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    import os
    import sys

    class MockPluginManager:
        @staticmethod
        def get_auth_plugin_mapping():
            return {'a': 'A', 'b': 'B'}

    plugin_manager_save = sys.modules.get('httpie.plugins.manager')

    sys.modules['httpie.plugins.manager'] = MockPluginManager()
    try:
        assert 'a' in _AuthTypeLazyChoices()
        assert 'b' in _AuthTypeLazyChoices()

        assert sorted(['a', 'b']) == sorted(_AuthTypeLazyChoices())
    finally:
        sys.modules['httpie.plugins.manager'] = plugin_manager_save

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
)

auth

# Generated at 2022-06-13 21:20:06.745109
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    The authentication mechanism to be used. If not set, a suitable one is
    automatically picked.

    For instance, --auth-type=digest uses HTTP Digest Authentication.
    Use --debug to see the full and final list of built-in auth plugins.

    '''
)

auth.add_argument(
    '--ignore-netrc',
    action='store_true',
    help='''
    By default, HTTPie searches the ~/.netrc file for credentials, if
    none are provided. Use this flag to disable that behaviour.

    '''
)


# Generated at 2022-06-13 21:20:09.326685
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert isinstance(_AuthTypeLazyChoices(), collections.abc.Iterable)

# Generated at 2022-06-13 21:20:20.012958
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    help='''
    Set the HTTP authentication mechanism. Use `--auth-type=help` to see
    the list of supported authentication mechanisms.

    '''
)
auth.add_argument(
    '--auth-file',
    default=None,
    metavar='FILE',
    type=argparse.FileType(),
    help='''
    The authentication data used for Digest authentication is stored in a file.
    The file is created if it doesn't exist.

    '''
)

#######################################################################
# Custom headers
#######################################################################

headers = parser.add_

# Generated at 2022-06-13 21:20:21.448546
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']

# Generated at 2022-06-13 21:20:22.818949
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:20:35.312900
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'hawk']

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help='''
    The authentication mechanism to be used.

    In addition to the built-in types, custom ones can be registered using the
    --auth-plugin command line option.

    The default is "basic".

    '''
)

# Generated at 2022-06-13 21:20:41.248646
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [
        item for item in _AuthTypeLazyChoices()
    ] == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:20:51.702696
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    pass

assert set(_AuthTypeLazyChoices()).issuperset(['basic', 'digest'])

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of credentials to send for authentication. The supported types
    depend on the version of Requests used.

    For example, supported types include:

        basic
        digest

    ''',
)
auth.add_argument(
    '--ignore-netrc',
    dest='netrc',
    action='store_false',
    default=True,
    help='''
    Do not use the ``netrc`` file even if it is available.

    ''',
)

#######################################################################
# SSL
################################

# Generated at 2022-06-13 21:20:55.446207
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    import httpie.plugins
    lazy_choices = set(_AuthTypeLazyChoices())
    assert set(httpie.plugins.__all__) <= lazy_choices


# Generated at 2022-06-13 21:21:07.766639
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # type: () -> None
    """Test __iter__ method of class _AuthTypeLazyChoices."""
    from plugins.auth import BasicAuth
    from plugins.auth import DigestAuth
    from plugins.auth import HawkAuth
    from plugins.auth import NtlmAuth
    from plugins.auth import OAuth1Auth
    from plugins.auth import OAuth2Auth
    from plugins.auth import OAuth2ImplicitGrantAuth
    from plugins.auth import OAuth2PasswordCredentialsGrantAuth
    from plugins.auth import OAuth2RefreshingAccessTokenAuth
    from plugins.auth import OAuth2JwtBearerAuth
    from plugins.auth import BinaryAuth
    from plugins.auth import PluginAuth
    import plugins._utils as _utils


# Generated at 2022-06-13 21:21:19.658367
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Specify an authentication plugin. By default,
    HTTPie tries to determine the auth type by the --auth option value.

    '''
)

_auth_plugin_kwargs = [
    '--auth-plugin-custom-args',
    'auth-plugin-custom-args',
    ''
]

auth.add_argument(
    *_auth_plugin_kwargs,
    help='This option is reserved for plugins.'
)

#######################################################################
# Client options
#######################################################################

client = parser.add_argument_group(title='Client Options')


# Generated at 2022-06-13 21:21:29.799495
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    metavar='TYPE',
    help='''
    The auth mechanism to use. If unspecified, an appropriate one
    is picked automatically.

    The following types are available:

    {auth_plugins}

    Use `http --debug` to see how the authentication plugin is chosen.

    '''.format(
        auth_plugins='\n'.join(
            f"    {name}:{plugin.description}"
            for name, plugin in sorted(
                plugin_manager.get_auth_plugin_mapping().items()
            )
        )
    )
)



# Generated at 2022-06-13 21:21:34.379579
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from tests import TestAuthPlugin
    with plugin_manager.add_plugin(TestAuthPlugin):
        choices = _AuthTypeLazyChoices()
        assert 'test' in choices
        assert 'non-existing' not in choices



# Generated at 2022-06-13 21:21:36.676484
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # 1) 0 should be inside choice list
    assert 0 in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:44.789008
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == sorted(_AuthTypeLazyChoices())


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism.

    The following mechanisms are available:

        {mechanisms}

    '''.format(
        mechanisms='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(
                ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
                60
            )
        )
    )
)

# Generated at 2022-06-13 21:21:48.416418
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    it = iter(auth_type_lazy_choices)
    type(it) == '_AuthTypeLazyChoices'
    for i in auth_type_lazy_choices:
        i in plugin_manager.get_auth_plugin_mapping()
test__AuthTypeLazyChoices___iter__()

# Generated at 2022-06-13 21:22:03.613950
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices.__contains__(_AuthTypeLazyChoices, 'ntlm')


auth_type = auth.add_mutually_exclusive_group()
auth_type.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism while also specifying
    the credentials via --auth. The default is "basic".

    The available types are:
    {types}
    '''.format(types=', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

# Generated at 2022-06-13 21:22:16.902586
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from httpie.plugins.auth.basic import AuthPlugin as BasicAuthPlugin
    assert list(_AuthTypeLazyChoices()) == list(sorted([
        plugin.auth_type for plugin in plugin_manager.get_auth_plugins()
    ]))
    plugin_manager.unload_plugin(BasicAuthPlugin)
    assert list(_AuthTypeLazyChoices()) == list(sorted([
        plugin.auth_type for plugin in plugin_manager.get_auth_plugins()
        if plugin.auth_type != 'basic'
    ]))



# Generated at 2022-06-13 21:22:27.556135
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    class FakeAuthPlugin:
        auth_type = 'fake_auth'

    plugin_manager.register_auth_plugin(FakeAuthPlugin)
    auth_type_lazy = _AuthTypeLazyChoices()
    assert 'fake_auth' in auth_type_lazy

    plugin_manager.deregister_auth_plugin(FakeAuthPlugin)



# Generated at 2022-06-13 21:22:29.780933
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()  # noqa

# Generated at 2022-06-13 21:22:41.461049
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    try:
        assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    except:
        print(_AuthTypeLazyChoices().__iter__())
        print(list(sorted(plugin_manager.get_auth_plugin_mapping().keys())))
        raise


# Generated at 2022-06-13 21:22:44.578955
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'foo' not in _AuthTypeLazyChoices()
    assert 'jwt' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:22:57.543508
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    types = _AuthTypeLazyChoices()
    assert isinstance(types, list)
    assert 'basic' in types
    assert 'digest' in types

auth.add_argument(
    '--auth-type', '-t',
    default=None,
    dest='auth_plugin',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Force usage of a specified auth type (basic|digest|oauth1).
    '''
)

#######################################################################
# SSL
#######################################################################

ssl_group = parser.add_argument_group(title='SSL')


# Generated at 2022-06-13 21:23:04.265875
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(_AuthTypeLazyChoices())

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism. Use `http --help-auth` for a list of
    available mechanisms.

    '''
)


#######################################################################
# HTTP method
#######################################################################

method = parser.add_argument_group(title='HTTP Method')
methods = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS')
# http://bugs.python.org/issue9334
method.add_argument('--method', '-m', default='GET', choices=methods)

#######################################################################

# Generated at 2022-06-13 21:23:16.004043
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = list(_AuthTypeLazyChoices())
    assert choices == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism.

    If no auth type is specified, then HTTPie tries to guess
    based on the --auth option value.

    This is useful when the credentials are transmitted over an insecure
    connection. For instance, when the credentials are sent via HTTP,
    HTTPie can determine which auth type to use based on the challenge
    sent by the server.

    If you suspect that HTTPie is guessing the auth type incorrectly,
    you can override the guess using this option.

    '''
)

# Generated at 2022-06-13 21:23:31.819790
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_choices = _AuthTypeLazyChoices()
    assert [
        'basic',
        'digest'
    ] == list(lazy_choices)



# Generated at 2022-06-13 21:23:40.766350
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Digest' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:23:52.805133
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    import pytest

    from httpie import plugin_manager
    from httpie import args
    names = plugin_manager.get_auth_plugin_mapping().keys()

    # Test a single element in the iterator.
    a = _AuthTypeLazyChoices()
    for name in names:
        if name in a:
            assert True
        else:
            assert False

    # Test all of the elements in the iterator.
    a = _AuthTypeLazyChoices()
    assert all(name in a for name in names)


# Generated at 2022-06-13 21:24:02.125439
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin.
    Run `$ http --debug` to print a list of all installed plugins.

    '''
)

# Generated at 2022-06-13 21:24:09.803002
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    list(choices)

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism. By default, it is inferred from the username
    and password, or prompted for. The available mechanisms depend on the
    available auth plugins.

    '''
)

# Generated at 2022-06-13 21:24:25.556420
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == \
        ['digest', 'hawk', 'ntlm', 'oauth1', 'oauth2']


auth_type_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=auth_type_choices,
    help='''
    The authentication mechanism to be used.
    Currently supported: %(choices)s.

    ''',
)
auth.add_argument(
    '--auth-type-help',
    action='store_true',
    help='Print help and available options.'
)

# Generated at 2022-06-13 21:24:37.595116
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'cache' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help=f'''
    The authentication mechanism to be used.

    The default auth plugin is {DEFAULT_AUTH_PLUGIN_NAME}.

    Available plugins: {', '.join(_AuthTypeLazyChoices())}
    '''
)


# Generated at 2022-06-13 21:24:45.372781
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    class AuthTypeLazyChoicesTester(_AuthTypeLazyChoices):
        pass
    authTypeLazyChoicesTester = AuthTypeLazyChoicesTester()
    assert hasattr(authTypeLazyChoicesTester, '__contains__')
    assert hasattr(authTypeLazyChoicesTester, '__iter__')

auth.add_argument(
    '--auth-type',
    dest='auth_type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The mechanism for providing the credentials: basic, digest, oauth1, oauth2,
    hawk, netrc, ntlm, ...

    See available authentication types: http --help-auth

    '''
)


# Generated at 2022-06-13 21:24:50.220425
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert 'different' not in auth_type_lazy_choices

# Generated at 2022-06-13 21:24:52.281522
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:02.375792
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy = _AuthTypeLazyChoices()
    assert AUTH_PLUGIN_NAME in lazy


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism.

    You can use this to override the authentication method based on the URL.
    For example, to use Kerberos authentication for an URL with the `krb5`
    scheme even though it would otherwise result in an HTTP Basic Auth request:

        http --auth-type=kerberos krb5://example.org/

    '''
)

# ``requests.auth.HTTPBasicAuth`` keyword arguments.

# Generated at 2022-06-13 21:25:27.279326
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'PYTEST_PLUGIN_AUTH_FAKE_AUTH_TYPE' in _AuthTypeLazyChoices()
    assert 'PYTEST_PLUGIN_AUTH_FAKE_AUTH_TYPE' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:25:36.664994
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert [item for item in auth_type_lazy_choices] == ['basic', 'digest']

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin (which must be
    already installed).

    Use `http --debug list-plugins' to see a list of plugins
    and their entry points.

    '''

)


# Generated at 2022-06-13 21:25:49.271514
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from .. import plugins
    plugin_instance = plugins.get_plugin_manager()
    plugin_instance.plugin_dir = 'fake'
    auth_type = _AuthTypeLazyChoices()
    assert list(auth_type) == [None]
    plugin_instance.plugin_dir = None


# Generated at 2022-06-13 21:25:56.604095
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert sorted(list(choices)) == ['aws-sigv4', 'awsv4', 'basic', 'bearer', 'digest', 'hawk', 'negotiate', 'netrc', 'oauth', 'oauth1']

# Generated at 2022-06-13 21:26:05.872522
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert set(['foo']) <= _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:21.224206
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(['basic', 'digest']))

_auth_type_choices = _AuthTypeLazyChoices()
auth.add_argument(
    '--auth-type',
    help=f'''
    Authorization plugin to use. The available options are {_auth_type_choices}.

    ''',
    choices=_auth_type_choices,
    default=None,
    metavar='AUTH_TYPE',
)

#######################################################################
# HTTP method
#######################################################################
method = parser.add_argument_group(title='HTTP method')

# Generated at 2022-06-13 21:26:23.570204
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:26.905576
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for item in _AuthTypeLazyChoices():
        assert item in plugin_manager.get_auth_plugin_mapping()

# Generated at 2022-06-13 21:26:30.623035
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """Unit test for method __contains__ of class _AuthTypeLazyChoices
    """
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:26:38.068612
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']
auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Select the authentication mechanism. Currently supported:

    {0}

    '''.format(
        '\n'.join(
            '    {0}'.format(plugin.name)
            for plugin in plugin_manager.get_auth_plugins()
        )
    )
)

#######################################################################
# SSL
#######################################################################

ssl_group = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:27:12.385547
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type = _AuthTypeLazyChoices()
    assert tuple(auth_type) == tuple(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='\n'.join(
        '{0}{1}'.format(8 * ' ', line.strip())
        for line in wrap(
            'The authentication mechanism to be used. '
            'Defaults to "basic".', 60
        )
    ).strip()
)

# Generated at 2022-06-13 21:27:19.389079
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism. The available names are:

        {auth_types}

    '''.format(
        auth_types='\n'.join(
            (8 * ' ') + line
            for line in wrap(
                ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
                80)
        ),
    )
)

# Generated at 2022-06-13 21:27:27.686718
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The auth mechanism to use. The TYPE can be one of:

    * The name of an ``httpie.plugins.auth.*`` plugin.

    * The path to a Python file containing such an
      ``httpie.plugins.auth.*`` plugin.

    '''
)

# Generated at 2022-06-13 21:27:35.330201
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert list(_AuthTypeLazyChoices())[0] == 'basic'

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_plugin',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication scheme to be used.

    The following schemes are supported:
        {auth_types}

    To disable authentication, use:
        --auth-type=noauth

    Plugins may add additional values, run:
        http --auth-type=

    to see the full list.

    '''.format(
        auth_types=', '.join(sorted(
            plugin_manager.get_auth_plugin_mapping().keys()
        )),
    )
)

################################

# Generated at 2022-06-13 21:27:46.469504
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert set(iter(_AuthTypeLazyChoices())) == {'basic', 'digest', 'hawk'}

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the authentication mechanism to be used. If not given,
    the authentication mechanism is inferred from the provided credentials
    (if credentials are given at all).

    '''
)
auth.add_argument(
    '--auth-header', '-H',
    metavar='KEY[:VALUE]',
    action=KeyValueArg,
    default={},
    help='''
    Extra header used in the HTTP Basic or Digest auth request.
    Multiple headers are supported.

    '''
)
#######################################################################
# Transport
#######################################################################

transport = parser

# Generated at 2022-06-13 21:27:55.982589
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    assert 'bearer' in choices
auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Use the specified authentication plugin.

    Available plugins: {", ".join(sorted(plugin_manager.get_auth_plugin_mapping()))}

    '''
)



# Generated at 2022-06-13 21:27:58.479002
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()))



# Generated at 2022-06-13 21:28:02.713594
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert isinstance(_AuthTypeLazyChoices(), collections.abc.Iterable)


auth.add_argument(
    '--auth-type',
    default=None,
    help=f'''
    Use a custom auth plugin.

    To see a list of available plugins, run:

        $ http --debug

    and check the "auth_plugins" section.
    ''',
    choices=_AuthTypeLazyChoices(),
)



# Generated at 2022-06-13 21:28:13.903729
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:28:32.249390
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.plugins import builtin as builtin_plugins
    from httpie.plugins import builtin
    loaded_builtin_plugins = {
        plugin.name for plugin in builtin_plugins.plugins if plugin.loaded
    }
    # We want to know if there is any plugin that we are not aware of,
    # and if there is, we want to know, how it is called.
    discovered_plugins = {
        plugin_name
        for plugin_name in _AuthTypeLazyChoices()
        if plugin_name not in loaded_builtin_plugins
    }
    assert not discovered_plugins, discovered_plugins
