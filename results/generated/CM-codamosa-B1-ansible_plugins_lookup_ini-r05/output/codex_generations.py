

# Generated at 2026-10-24 04:52:12.375796
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:52:32.224350
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:52:34.716516
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:52:37.128294
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:39.539611
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:41.955006
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:44.371077
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:46.782538
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:49.198351
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:51.614350
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:54.024588
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:52:56.441353
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 04:53:26.894679
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:45.040274
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:47.454509
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:49.865959
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:52.277773
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:54.689430
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:57.104555
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:53:59.517522
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:01.929020
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:04.348651
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:06.759346
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:09.182459
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:11.590333
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:25.489340
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:37.066482
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:54:56.030500
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 04:54:58.445921
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:55:00.858302
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:55:03.272986
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:55:05.690938
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:08.102335
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:10.514705
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:12.924340
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:55:15.334532
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:55:23.351728
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():lookup = LookupModule.__new__(LookupModule)

# Generated at 2026-10-24 04:55:24.657796
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:34.102720
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:46.042942
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:55:47.625693
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 04:55:49.055397
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:01.426710
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:12.917343
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()


# Generated at 2026-10-24 04:56:15.336874
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:17.750007
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:28.261770
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 04:56:29.707038
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:32.224767
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:43.547950
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:44.857857
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:55.661479
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 04:56:56.978361
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:56:59.398459
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:01.814301
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:04.231183
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:06.648339
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:09.061650
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:11.473270
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:13.884779
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:16.295931
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:18.707244
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:21.118496
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:23.529788
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:25.941160
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:28.355472
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:30.766600
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:33.178130
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:35.590059
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:38.001352
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:40.412548
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:42.825564
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:45.237332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:57:47.938821
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:00.806224
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:14.335759
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 04:58:15.639580
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:18.170834
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:20.666854
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:23.080566
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:25.491018
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:28.187607
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:30.680443
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:33.103538
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:35.512774
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:38.137940
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:40.547091
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:42.961933
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:45.373630
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:47.789805
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:50.205160
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:58:52.616275
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:58:55.032460
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:58:57.447548
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 04:58:58.824807
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:59:12.554551
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:59:24.504301
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import MethodType, SimpleNamespace


# Generated at 2026-10-24 04:59:25.839077
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:59:38.745288
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 04:59:40.072964
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 04:59:41.436001
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 04:59:42.831925
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 04:59:44.139669
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 04:59:58.410497
# Unit test for method run of class LookupModule
def test_LookupModule_run():import os

# Generated at 2026-10-24 04:59:59.804946
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:00:12.904130
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:00:25.023673
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace


# Generated at 2026-10-24 05:00:26.356424
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:00:38.456003
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:00:49.599433
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:00:51.051054
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 05:00:52.367094
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 05:00:53.672759
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:03.834863
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:19.305039
# Unit test for method run of class LookupModule
def test_LookupModule_run():import types


# Generated at 2026-10-24 05:01:20.752938
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Single value is returned from the requested section."""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.read_string(INI_CONTENT)

    assert lm.get_value('user', 'global', 'default', False) == 'admin'
    assert lm.get_value('password', 'global', 'default', False) == 'secret'


def test_LookupModule_get_value_missing_key_returns_default(lookup):
    """A missing key yields the supplied default, not None."""
    assert lookup.get_value('nope', 'global', 'fallback', False) == 'fallback'
    assert lookup.get_value('nope', 'global', '', False) == ''


def test_LookupModule_get_value_regexp(lookup):
    """re=True returns a list of values for every matching key."""
    result = lookup.get_value('foo.*', 'section1', None, True)

    assert isinstance(result, list)
    assert sorted(result) == ['bar', 'baz']


def test_LookupModule_get_value_regexp_no_match_is_empty_list(lookup):
    """re=True with no match returns [] (default is ignored)."""
    assert lookup.get_value('nomatch.*', 'section1', 'fallback', True) == []


def test_LookupModule_get_value_regexp_uses_re_match_not_search(lookup):
    """re.match anchors at the start, so a suffix pattern does not match."""
    assert lookup.get_value('ser', 'global', None, True) == []


def test_LookupModule_get_value_missing_section_raises(lookup):
    """NoSectionError is not swallowed by get_value."""
    with pytest.raises(configparser.NoSectionError):
        lookup.get_value('user', 'nosuchsection', 'default', False)


def test_LookupModule_get_value_case_insensitive_by_default(lookup):
    """Default optionxform lowercases keys, so lookups are case-insensitive."""
    assert lookup.get_value('USER', 'global', 'default', False) == 'admin'


def test_LookupModule_get_value_case_sensitive(lookup):
    """With optionxform = str, key case is preserved and mismatches miss."""
    lookup.cp.optionxform = str
    assert lookup.get_value('user', 'global', 'default', False) == 'admin'
    assert lookup.get_value('USER', 'global', 'default', False) == 'default'

# Generated at 2026-10-24 05:01:22.072412
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:35.887875
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:51.469450
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:52.771874
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:55.300209
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:01:57.714957
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:02:00.383605
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:02:13.773401
# Unit test for method run of class LookupModule
def test_LookupModule_run():from types import SimpleNamespace
