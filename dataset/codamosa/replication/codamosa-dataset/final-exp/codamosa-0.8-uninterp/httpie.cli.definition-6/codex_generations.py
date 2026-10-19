

# Generated at 2022-06-13 21:19:24.646133
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    [(auth_type, plugin_name) for auth_type, plugin_name in _AuthTypeLazyChoices()]

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    Specifies the authentication mechanism to be used, HTTP Basic authentication
    by default. Available choices are:

        {auth_plugin_names}

    '''.format(
        auth_plugin_names='\n'.join(
            '{0}{1}'.format(8 * ' ', line.strip())
            for line in wrap(', '.join(
                sorted(plugin_manager.get_auth_plugin_mapping().keys())
            ), 60)
        ).strip()
    )
)

#######################################################################
#

# Generated at 2022-06-13 21:19:35.074690
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )


auth_type_help = f'''
    Override the default (inferred) auth plugin.

    Possible values:

    {plugin_manager.get_installed_plugin_names_help()}

    '''
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=auth_type_help,
)


# Generated at 2022-06-13 21:19:41.363125
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [
        item for item in _AuthTypeLazyChoices()
    ] == ['basic', 'digest', 'jwt']


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    Defaults to Basic, but can also be e.g., Digest.

    See the documentation of the AUTHENTICATION section of the config file
    for more info.

    '''
)
#######################################################################
# Options for SSL/TLS verification
#######################################################################
ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:19:48.783673
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'Basic' in auth_type_choices
    assert 'Digest' in auth_type_choices
    assert 'OAuth1' in auth_type_choices
    assert 'OAuth2' in auth_type_choices
    assert 'Hawk' in auth_type_choices
    assert 'CookieAuth' in auth_type_choices
    assert 'MultipartAuth' in auth_type_choices
    assert 'TokenAuth' in auth_type_choices
    assert 'AWSAuthV4' in auth_type_choices
    assert 'CustomAuth' in auth_type_choices
    assert 'plugin_name' not in auth_type_choices

# Generated at 2022-06-13 21:20:03.673076
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from inspect import isclass
    from collections import abc
    assert isclass(_AuthTypeLazyChoices)
    assert issubclass(_AuthTypeLazyChoices, abc.Container)


# Generated at 2022-06-13 21:20:14.780991
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in plugin_manager.get_auth_plugin_mapping()
    assert 'digest' in plugin_manager.get_auth_plugin_mapping()
    assert all(x in _AuthTypeLazyChoices() for x in ['basic', 'digest'])
    assert all(x in _AuthTypeLazyChoices() and x in ['basic', 'digest']
               for x in _AuthTypeLazyChoices())


# Generated at 2022-06-13 21:20:22.573455
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']
auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    The auth mechanism to use, if not otherwise specified in the URL (e.g.,
    http://user:pass@example.org/).

    The following plugins are available: {0}

    '''.format(', '.join(sorted(plugin_manager.get_auth_plugin_mapping())))
)

#######################################################################
# Persistent options
#######################################################################

persistence = parser.add_argument_group(title='Persistence')


# Generated at 2022-06-13 21:20:24.531075
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices()
    # TODO: 4th arg, choices=_AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:37.324827
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        'basic', 'digest', 'hawk', 'jwt'
    ]

auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''

    The type of the auth mechanism. If not provided, HTTPie tries to guess.

    ''',
)

###########################################################################
# HTTP method
###########################################################################
method = parser.add_argument_group(title='HTTP method')
method.add_argument(
    '--method', '-m',
    help='''
    Specify an HTTP method to use. For example, '--method PUT' will make
    HTTPie send a PUT request instead of the default GET.

    ''',
)

###########################################################################

# Generated at 2022-06-13 21:20:40.078526
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    lazy_choices = _AuthTypeLazyChoices()
    assert sorted(lazy_choices) == ['basic', 'digest']



# Generated at 2022-06-13 21:20:45.543483
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'bearer' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:20:59.193747
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    type=str,
    choices=_AuthTypeLazyChoices(),
    default='auto',
    help=f'''
    The name of the authentication plugin to use. By default HTTPie will
    automatically detect the authentication type.

    The following authentication plugins are available:

        {plugin_manager.get_auth_plugin_help()}

    '''
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:21:00.561694
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert isinstance(_AuthTypeLazyChoices(), list)

# Generated at 2022-06-13 21:21:03.893893
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hawk' in choices
    assert 'ntlm' in choices
    assert 'unknown-auth-type' not in choices

# Generated at 2022-06-13 21:21:14.373501
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices
    assert 'custom' not in auth_type_lazy_choices

auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The type of HTTP authentication. The value can be one of:

        {', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))}

    '''
)


# Generated at 2022-06-13 21:21:21.687166
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    a = _AuthTypeLazyChoices()
    assert sorted(a) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    dest='auth_plugin',
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help=argparse.SUPPRESS
)

#######################################################################
# Extras
#######################################################################

# parser.add_argument(
#     '--traceback',
#     action='store_true',
#     help='''
#     Print exception traceback should one occur.
#
#     '''
# )


#######################################################################
# JSON Options
#######################################################################

json = parser.add_argument_group(title='JSON Options')

json.add

# Generated at 2022-06-13 21:21:29.699534
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    list(_AuthTypeLazyChoices())
    'oauth1.0' in _AuthTypeLazyChoices()
    'oauth2.0' in _AuthTypeLazyChoices()

auth_type_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=auth_type_choices,
    help=f'''
    Specify an authentication plugin to use.

    Available plugins:
        {', '.join(plugin_manager.get_auth_plugin_mapping().keys())}

    See:
        https://httpie.org/plugins#authenticationplugins

    '''
)


# Generated at 2022-06-13 21:21:40.960491
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert [x for x in _AuthTypeLazyChoices()]

auth.add_argument(
    '--auth-type',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    Override the default authentication mechanism.

    The default `auto` value will use the most secure mechanism
    available.  This is currently Basic and Digest, though subject
    to change in the future.

    '''
)

# Generated at 2022-06-13 21:21:47.504987
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Use the specified authentication plugin.

    '''
)

auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='''
    Do not use HTTP authentication challenge.

    This is useful when you want to send your credentials for every request.
    For example, when using token-based auth.

    '''
)

#######################################################################
# Configuration
#######################################################################

config = parser.add_argument

# Generated at 2022-06-13 21:21:52.077338
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    items = list(_AuthTypeLazyChoices())
    assert len(items) > 0
    assert all(isinstance(item, str) for item in items)
    sorted_items = sorted(items)
    assert sorted_items == items

# Generated at 2022-06-13 21:22:00.637536
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert len(list(_AuthTypeLazyChoices())) > 0

# Generated at 2022-06-13 21:22:12.940990
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    def check(lazychoices, expected_list):
        assert (
            sorted(lazychoices) == sorted(expected_list)
        )

    lazychoices = _AuthTypeLazyChoices()

    check(lazychoices, sorted(['basic', 'digest']))

    # This is safe because plugin_manager is a global variable
    # and tests are run sequentially
    plugin_manager.discover()
    plugin_manager.load_auth_plugins()
    assert plugin_manager.get_auth_plugin_mapping()

    # Authentication plugin helps add new type to lazychoices
    check(lazychoices, sorted(['basic', 'digest', 'aws']))


# Generated at 2022-06-13 21:22:14.576511
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:22:17.378826
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == plugin_manager.get_auth_plugin_mapping().keys()


# Generated at 2022-06-13 21:22:27.597816
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    assert list(auth_type_lazy_choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:22:39.623295
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'oauth2' in _AuthTypeLazyChoices()
    assert 'digest' not in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:22:51.188462
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest']


auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Choose an auth plugin. It can be one of the built-in plugins:

        {0}

        {1}

    or an auth plugin installed via a plugin manager.

    '''.format(
        ', '.join(
            sorted(plugin_manager.get_auth_plugin_mapping().keys())[:-1]
        ),
        sorted(plugin_manager.get_auth_plugin_mapping().keys())[-1]
    )
)

# Generated at 2022-06-13 21:23:01.696639
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    ))

_auth_type_validator = AuthPluginValidator(
    'Unsupported authentication method "{0}".'
)



# Generated at 2022-06-13 21:23:03.828285
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    ls = _AuthTypeLazyChoices()
    if 'digest' in ls:
        return True
    else:
        return False

# Generated at 2022-06-13 21:23:08.100416
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    core_plugin_names = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(choices) == core_plugin_names



# Generated at 2022-06-13 21:23:29.098856
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from requests.auth import HTTPBasicAuth
    from httpie.plugins import AuthPlugin
    from pprint import pprint
    from httpie.auth import AuthCredentials
    from httpie.plugins import get_auth_plugin_mapping
    from httpie.plugins import plugin_manager

    class BasicAuthPlugin(AuthPlugin):
        auth_type = 'basic'
        auth_require = False

        def get_auth(self, username=None, password=None):
            if username and password is not None:
                return HTTPBasicAuth(username=username, password=password)
            return None

        def get_credentials(self, args):
            username = args.auth
            password = None
            if ':' in args.auth:
                username, password = username.split(':', 1)
            return AuthCredentials(username, password)

# Generated at 2022-06-13 21:23:31.690531
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'dummy' in _AuthTypeLazyChoices()
    assert 'plugin-test' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:23:32.711545
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Setup
    pass




# Generated at 2022-06-13 21:23:46.448133
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    plugins = _AuthTypeLazyChoices()
    assert 'digest' in plugins
    assert next(iter(plugins)) == 'digest'

auth_type_choices = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    choices=auth_type_choices,
    help='''
    Specify an authentication method.

    '''
)


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL Options')


# Generated at 2022-06-13 21:23:58.070373
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic']
auth.add_argument(
    '--auth-type', '-t',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify a credential type.
    The available credential types depend on plugins.

    ''',
)
auth.add_argument(
    '--auth-type-help', '-A',
    metavar='TYPE',
    default=None,
    help='''
    Print help message and exit.

    '''
)

#######################################################################
# HTTP Method
#######################################################################

method = parser.add_argument_group(title='HTTP Method')

# Generated at 2022-06-13 21:24:01.145172
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    method = _AuthTypeLazyChoices.__iter__
    assert method(object()) is NotImplemented

# Generated at 2022-06-13 21:24:02.799458
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'bearer' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:24:12.805305
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert ('basic' in _AuthTypeLazyChoices()) is True
    assert ('kenneth' in _AuthTypeLazyChoices()) is False
    AVAILABLE_AUTHS = set(
        plugin_manager.get_auth_plugin_mapping().keys())

    # Make sure that 'digest' is in the list
    assert AVAILABLE_AUTHS.intersection({'digest'})

    assert set(_AuthTypeLazyChoices()).issubset(AVAILABLE_AUTHS)
    assert set(_AuthTypeLazyChoices()).issuperset(
        {'basic', 'digest', 'ntlm', 'hawk'}
    )


# Generated at 2022-06-13 21:24:19.560407
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == [
        AUTH_PLUGIN_KEY_BASIC,
        AUTH_PLUGIN_KEY_DIGEST,
        AUTH_PLUGIN_KEY_AWS,
        AUTH_PLUGIN_KEY_AWS_4,
        AUTH_PLUGIN_KEY_JWT
    ]



# Generated at 2022-06-13 21:24:22.397425
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices


# Generated at 2022-06-13 21:24:38.509213
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_choices = _AuthTypeLazyChoices()
    assert 'basic' in auth_type_choices


# Generated at 2022-06-13 21:24:51.544552
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices.__contains__(_AuthTypeLazyChoices, 'digest')


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_type',
    help='''
    Specify an auth mechanism. By default, HTTPie tries to guess the auth
    mechanism based on the supplied credentials. Currently supported values are:
    {supported_auth_types}
    '''.format(
        supported_auth_types=', '.join(sorted(_AuthTypeLazyChoices()))
    ),
    choices=_AuthTypeLazyChoices(),
)

#######################################################################
# Proxy
#######################################################################

proxy = parser.add_argument_group(title='Proxy')

# Generated at 2022-06-13 21:24:54.516427
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'foo' not in choices



# Generated at 2022-06-13 21:24:57.513074
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    plugin_manager.load_builtin_plugins()
    assert 'basic' in choices
    assert 'digest' in choices

# Generated at 2022-06-13 21:25:05.172035
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'auto' in lazy_choices
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'hawk' in lazy_choices
    assert 'netrc' in lazy_choices
    for auth_type in lazy_choices:
        # For each auth type, check that it is in the __iter__
        # return value, as well as in the auth plugin mapping.
        assert auth_type in lazy_choices
        assert auth_type in plugin_manager.get_auth_plugin_mapping()


# Generated at 2022-06-13 21:25:06.170609
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices().__iter__()



# Generated at 2022-06-13 21:25:14.642155
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert next(iter(_AuthTypeLazyChoices()))
assert test__AuthTypeLazyChoices___iter__()

auth.add_argument(
    '--auth-type', '-t',
    metavar='AUTHTYPE',
    default=None,
    choices=_AuthTypeLazyChoices(),
    dest='auth_plugin',
    help='''
    Specify a custom authentication plugin.

    ''',
)


#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')
ssl.add_argument(
    '--ssl',
    action='store_true',
    help='''
    Verify HTTPS connections (default: enabled).

    '''
)

# Generated at 2022-06-13 21:25:15.908791
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:21.999546
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth_plugin_mapping = _AuthTypeLazyChoices()


# ``requests.auth.HTTPBasicAuth`` constructor keyword arguments.
auth.add_argument(
    '--auth-type',
    type=str,
    choices=auth_plugin_mapping,
    default='basic',
    help='''
    Specify a custom auth plugin module path.
    The default is "basic", which is requests.auth.HTTPBasicAuth.
    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(
    title='SSL',
    description='Mutually exclusive with --verify.'
)

# Generated at 2022-06-13 21:25:29.900495
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(['basic'])


# Generated at 2022-06-13 21:26:04.997270
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'jwt', 'oauth2']


auth.add_argument(
    '--auth-type',
    default=None,
    type=str.lower,
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of an auth plugin, e.g. basic, digest, oauth2, etc.

    This flag must be used in combination with --auth.

    If a username contains a colon (":"), the colon cannot be used to
    indicate that a password follows. The "--auth-type" flag should be
    used to explicitly set the authentication type.

    '''
)



# Generated at 2022-06-13 21:26:20.903171
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()
    assert 'Digest' in _AuthTypeLazyChoices()
    assert 'Bearer' in _AuthTypeLazyChoices()
    assert 'OAuth1' in _AuthTypeLazyChoices()
    assert 'AWS' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:33.564813
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    test_auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in test_auth_type_lazy_choices
    assert 'digest' in test_auth_type_lazy_choices
    assert 'ntlm' in test_auth_type_lazy_choices
    assert 'foo' not in test_auth_type_lazy_choices
    if not PYTHON2:
        assert list(test_auth_type_lazy_choices) == ['basic', 'digest', 'ntlm']



# Generated at 2022-06-13 21:26:38.072108
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'foo' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:40.271329
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:26:42.481856
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:26:59.046585
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    type=AuthCredentials.type_from_argparse,
    dest='auth_type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The type of auth credentials. If the auth plugin is installed and the
    credentials provided, this option is not needed.
    The default type is basic, but when netrc is used, the default auth type is
    what's specified in netrc (can be basic or digest).

    The following credential types are currently supported:

    {types}

    Additional auth types can be supported via plugins.

    '''.format(types=AuthCredentials.format_types())
)


# Generated at 2022-06-13 21:27:03.399356
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_choices = _AuthTypeLazyChoices()
    assert list(lazy_choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:27:11.783056
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():

    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='AUTH_TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used.

    A custom authentication type
    can also be specified, in which case the corresponding plugin
    is loaded from:

        {plugin_manager.get_installed_auth_plugins_entry_points()[0].dist.location}

    '''.format(
        plugin_manager=plugin_manager
    )
)

# Generated at 2022-06-13 21:27:13.907716
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'oauth1' in _AuthTypeLazyChoices()
    assert 'bogus' not in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:16.623513
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == sorted([
        'basic',
        'digest',
        'hawk',
        'aws',
        'custom'
    ])


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default='basic',
    help=f'''
    The authentication mechanism to be used. Choices: {', '.join(sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    ))}

    '''
)
auth.add_argument(
    '--auth-netrc',
    action='store_true',
    default=False,
    help='''
    Use credentials from .netrc, if available. The default behaviour is
    to ignore .netrc.

    '''
)
auth

# Generated at 2022-06-13 21:28:20.512287
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:33.710290
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert set(auth_type_lazy_choices) == set(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The AUTH_PLUGIN to use for authentication.

    Plugins are looked up in the `httpie.plugins.auth' package namespace.

    {default_choices}

    '''.format(
        default_choices=get_auth_plugin_choices_doc(),
    )
)

# Generated at 2022-06-13 21:28:35.700400
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:38.023370
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:41.106212
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [i for i in _AuthTypeLazyChoices()] == ['digest', 'hawk']



# Generated at 2022-06-13 21:28:52.041089
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='{0}'.format(', '.join(_AuthTypeLazyChoices())),
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify a custom authentication plugin.

    ''',
)

auth.add_argument(
    '--auth-plugin',
    default=None,
    metavar='MODULE[.ATTR]',
    help='''
    Specify a custom authentication plugin. The plugin will be imported and
    the given attribute (or the module itself if no attribute is provided)
    should be a callable implementing the plugin protocol.

    ''',
)

# Generated at 2022-06-13 21:29:00.868597
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    lazy_choices = _AuthTypeLazyChoices()
    assert sorted(lazy_choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    metavar='SCHEME',
    help='''
    Specify an alternate authentication format.

    '''
)
auth.add_argument(
    '--auth-no-challenge',
    action='store_true',
    default=False,
    help='''
    Do not send an Authorization header if a credentials cache is available.
    By default, a credentials cache is used if present, but the header is
    sent anyway to avoid sending potentially sensitive credentials in the clear.

    '''
)
auth.add_argument

# Generated at 2022-06-13 21:29:11.567376
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
