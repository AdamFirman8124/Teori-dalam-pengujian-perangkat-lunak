

# Generated at 2024-03-18 08:20:22.220175
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:20:31.803455
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test cases for format_date

# Generated at 2024-03-18 08:20:44.098305
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:20:53.181183
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Test with day of week included
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=True) == "Saturday, April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 12, 25), dow=True) == "Monday, December 25"

    # Test with day of week excluded
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=False) == "April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 12, 25), dow=False) == "December 25"

    # Test with non-English locale
    assert Locale('fr_FR').format_day(datetime.datetime(2023, 4, 1), dow=True) == "samedi, avril 1"

# Generated at 2024-03-18 08:21:00.708337
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Saturday, April 15"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT offset for Eastern Time (ET)
    formatted_date_with_offset = locale.format

# Generated at 2024-03-18 08:21:02.431395
# Unit test for function load_gettext_translations
def test_load_gettext_translations():import os
import tempfile
import unittest
from tornado.locale import load_gettext_translations, _translations, _supported_locales, _use_gettext


# Generated at 2024-03-18 08:21:09.453428
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime, GMT offset, and relative set to False
    specific_date = datetime.datetime(2023, 3, 14, 15, 9)  # March 14, 2023, 15:09
    formatted_date = locale.format_date(specific_date, gmt_offset=0, relative=False)
    assert formatted_date == "March 14, 2023 at 3:09 pm", f"Expected 'March 14, 2023 at 3:09 pm', got '{formatted_date}'"

    # Test with a specific datetime, GMT offset, and relative set to True
    now = datetime.datetime.utcnow()
    seconds_ago = (now - specific_date).total_seconds()
    if seconds_ago < 60:
        expected = "1 second ago"

# Generated at 2024-03-18 08:21:18.521201
# Unit test for constructor of class Locale

# Generated at 2024-03-18 08:21:28.424265
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:21:35.243905
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Define a fixed date for testing
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week (dow=True)
    formatted_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_with_dow == "Saturday, April 15"

    # Test without day of week (dow=False)
    formatted_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT offset for Eastern Time (ET)
    formatted_with_offset = locale.format_day

# Generated at 2024-03-18 08:22:02.518113
# Unit test for constructor of class Locale
def test_Locale():    # Test initialization of Locale with different codes
    locale_en = Locale('en')
    assert locale_en.code == 'en'
    assert locale_en.name == 'English'
    assert not locale_en.rtl

    locale_fa = Locale('fa')
    assert locale_fa.code == 'fa'
    assert locale_fa.name == 'Farsi'
    assert locale_fa.rtl

    locale_he = Locale('he')
    assert locale_he.code == 'he'
    assert locale_he.name == 'Hebrew'
    assert locale_he.rtl

    # Test initialization with a non-existent locale code
    locale_xx = Locale('xx')
    assert locale_xx.code == 'xx'
    assert locale_xx.name == 'Unknown'
    assert not locale_xx.rtl

    # Test initialization with a locale code with country code
    locale_en_US = Locale('en_US')
    assert locale_en_US.code == 'en_US'

# Generated at 2024-03-18 08:22:09.916574
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime, GMT offset, and relative set to False
    specific_date = datetime.datetime(2023, 3, 14, 15, 9)  # Pi Day 2023, 3:14 PM
    formatted_date = locale.format_date(specific_date, gmt_offset=0, relative=False)
    assert formatted_date == "March 14, 2023 at 3:09 pm", f"Expected 'March 14, 2023 at 3:09 pm', got '{formatted_date}'"

    # Test with a specific datetime, GMT offset, and relative set to True
    now = datetime.datetime.utcnow()
    seconds_ago = (now - datetime.timedelta(seconds=45)).replace(microsecond=0)
    formatted_date = locale.format_date(seconds_ago, gmt_offset=0, relative=True)
   

# Generated at 2024-03-18 08:22:16.955256
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:22:22.873340
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:22:23.774706
# Unit test for function load_gettext_translations
def test_load_gettext_translations():import os
import tempfile
import unittest


# Generated at 2024-03-18 08:22:33.342581
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:22:39.334096
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:22:44.921074
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:22:52.729249
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Test with day of week included
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=True) == "Saturday, April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 2), dow=True) == "Sunday, April 2"
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 3), dow=True) == "Monday, April 3"

    # Test without day of week
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=False) == "April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 2), dow=False) == "April 2"

# Generated at 2024-03-18 08:22:54.210429
# Unit test for method pgettext of class GettextLocale
def test_GettextLocale_pgettext():import gettext

# Assuming CONTEXT_SEPARATOR is defined somewhere in the code
CONTEXT_SEPARATOR = "\x04"


# Generated at 2024-03-18 08:23:23.249937
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:23:31.823612
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Test with day of week included
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=True) == "Saturday, April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 12, 25), dow=True) == "Monday, December 25"

    # Test without day of week
    assert Locale('en_US').format_day(datetime.datetime(2023, 4, 1), dow=False) == "April 1"
    assert Locale('en_US').format_day(datetime.datetime(2023, 12, 25), dow=False) == "December 25"

    # Test with different locale
    assert Locale('fr_FR').format_day(datetime.datetime(2023, 4, 1), dow=True) == "samedi, avril 1"

# Generated at 2024-03-18 08:23:40.181807
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():    # Assume the following setup for the test
    locale = Locale.get('en_US')
    context = "menu"
    message = "file"
    plural_message = "files"
    count = 1

    # Test for singular translation with context
    assert locale.pgettext(context, message) == "file"

    # Test for plural translation with context
    assert locale.pgettext(context, message, plural_message, 2) == "files"

    # Test for singular translation with context and count
    assert locale.pgettext(context, message, plural_message, count) == "file"

    # Test for missing translation with context (should return the original message)
    missing_message = "nonexistent"
    assert locale.pgettext(context, missing_message) == missing_message

    # Test for missing plural translation with context (should return the original plural message)
    assert locale.pgettext(context, missing_message, plural_message, 2) == plural_message



# Generated at 2024-03-18 08:23:48.745559
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:23:55.612492
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 3, 14, 15, 9)  # March 14, 2023, 3:09 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Tuesday, March 14"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "March 14"

    # Test with a non-zero GMT offset (e.g., GMT+2 hours)
    gmt_offset = 120  # GMT offset in minutes
    formatted

# Generated at 2024-03-18 08:24:01.609971
# Unit test for method pgettext of class GettextLocale

# Generated at 2024-03-18 08:24:08.274475
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:24:17.475921
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:24:18.377934
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():import unittest


# Generated at 2024-03-18 08:24:26.461363
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:24:57.216467
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:25:04.731351
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Saturday, April 15"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "April 15"

    # Test with a non-zero GMT offset (e.g., GMT+2)
    gmt_offset = 120  # GMT offset in minutes for GMT+2

# Generated at 2024-03-18 08:25:11.046846
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:25:17.350417
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime, GMT offset, and relative set to False
    specific_date = datetime.datetime(2023, 4, 1, 15, 30)
    formatted_date = locale.format_date(specific_date, gmt_offset=0, relative=False)
    assert formatted_date == "April 1, 2023 at 3:30 pm", f"Expected 'April 1, 2023 at 3:30 pm', got '{formatted_date}'"

    # Test with a specific datetime, GMT offset, and relative set to True
    now = datetime.datetime.utcnow()
    seconds_ago = (now - datetime.timedelta(seconds=45)).replace(microsecond=0)
    formatted_date = locale.format_date(seconds_ago, gmt_offset=0, relative=True)

# Generated at 2024-03-18 08:25:19.106846
# Unit test for function load_translations
def test_load_translations():import unittest
import tempfile
import shutil
import os


# Generated at 2024-03-18 08:25:26.659749
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test cases with different dates and gmt_offset values
    test_cases = [
        (datetime.datetime(2023, 4, 1, 12, 0), 0, True, "Saturday, April 1"),
        (datetime.datetime(2023, 4, 1, 12, 0), 0, False, "April 1"),
        (datetime.datetime(2023, 12, 25, 12, 0), -300, True, "Monday, December 25"),
        (datetime.datetime(2023, 12, 25, 12, 0), -300, False, "December 25"),
    ]

    # Run the test cases
    for date, gmt_offset, dow, expected in test_cases:
        assert locale.format_day(date, gmt_offset, dow) == expected

#

# Generated at 2024-03-18 08:25:35.812722
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:25:44.541271
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup
    locale_en = Locale.get('en_US')
    locale_fr = Locale.get('fr_FR')

    # Test with relative dates in English
    now = datetime.datetime.utcnow()
    one_hour_ago = now - datetime.timedelta(hours=1)
    assert locale_en.format_date(one_hour_ago.timestamp()) == "1 hour ago"

    # Test with absolute dates in English
    assert locale_en.format_date(one_hour_ago.timestamp(), relative=False).endswith(one_hour_ago.strftime('%I:%M %p'))

    # Test with relative dates in French
    assert locale_fr.format_date(one_hour_ago.timestamp()) == "il y a 1 heure"

    # Test with full format in English
    assert locale_en.format_date(one_hour_ago.timestamp(), full_format=True) == one_hour_ago.strftime('%B %d, %Y at %I:%M %p')

    # Test with future dates in English

# Generated at 2024-03-18 08:25:51.173132
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance
    locale = Locale('en_US')

    # Mock datetime with fixed now
    fixed_now = datetime.datetime(2023, 4, 1, 12, 0, 0)
    with unittest.mock.patch('datetime.datetime') as mock_datetime:
        mock_datetime.utcnow.return_value = fixed_now

        # Test cases

# Generated at 2024-03-18 08:25:57.544028
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Saturday, April 15"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT offset in minutes (e.g., Eastern Time UTC-5)
    formatted

# Generated at 2024-03-18 08:26:24.653657
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:26:31.846432
# Unit test for method pgettext of class Locale
def test_Locale_pgettext():    # Setup a Locale instance with a mock translation function
    locale = Locale('en_US')
    locale.translate = MagicMock(side_effect=lambda *args, **kwargs: args[0])

    # Test cases for pgettext
    test_cases = [
        (("context", "message"), "message"),
        (("context", "message", "plural_message", 2), "plural_message"),
        (("context", "message", "plural_message", 1), "message"),
    ]

    for args, expected in test_cases:
        assert locale.pgettext(*args) == expected, f"pgettext({args}) == {expected}"

    # Verify that the mocked translate function was called with the correct arguments

# Generated at 2024-03-18 08:26:41.012938
# Unit test for method list of class Locale
def test_Locale_list():    # Test with empty list
    assert Locale('en').list([]) == ""

    # Test with one item
    assert Locale('en').list(['Apple']) == "Apple"

    # Test with two items
    assert Locale('en').list(['Apple', 'Banana']) == "Apple and Banana"

    # Test with three items
    assert Locale('en').list(['Apple', 'Banana', 'Cherry']) == "Apple, Banana and Cherry"

    # Test with four items
    assert Locale('en').list(['Apple', 'Banana', 'Cherry', 'Date']) == "Apple, Banana, Cherry and Date"

    # Test with Persian locale and two items
    assert Locale('fa').list(['سیب', 'موز']) == "سیب \u0648 موز"

    # Test with Persian locale and three items

# Generated at 2024-03-18 08:26:47.639407
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance
    locale = Locale('en_US')

    # Mock datetime and timedelta
    with unittest.mock.patch('datetime.datetime') as mock_datetime:
        # Mock now
        mock_datetime.utcnow.return_value = datetime.datetime(2023, 4, 1, 12, 0, 0)
        # Mock timedelta
        mock_datetime.timedelta = datetime.timedelta

        # Test cases

# Generated at 2024-03-18 08:26:57.691883
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:27:10.026810
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance
    locale = Locale('en_US')

    # Define a date for testing
    test_date = datetime.datetime(2023, 3, 15, 12, 30)  # March 15, 2023, at 12:30 PM

    # Test with day of week included
    formatted_with_dow = locale.format_day(test_date, gmt_offset=0, dow=True)
    assert formatted_with_dow == "Wednesday, March 15"

    # Test without day of week
    formatted_without_dow = locale.format_day(test_date, gmt_offset=0, dow=False)
    assert formatted_without_dow == "March 15"

    # Test with GMT offset (e.g., GMT+2)
    formatted_with_offset = locale.format_day(test_date, gmt_offset=120, dow=True)
    assert formatted_with_offset == "Wednesday, March 15"

    # Test with a different

# Generated at 2024-03-18 08:27:17.770714
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance
    locale = Locale('en_US')

    # Test cases with different dates and GMT offsets

# Generated at 2024-03-18 08:27:24.082562
# Unit test for method friendly_number of class Locale
def test_Locale_friendly_number():    # Test with English locale
    en_locale = Locale('en_US')
    assert en_locale.friendly_number(123) == '123'
    assert en_locale.friendly_number(1234) == '1,234'
    assert en_locale.friendly_number(1234567) == '1,234,567'

    # Test with a non-English locale (e.g., French)
    fr_locale = Locale('fr')
    assert fr_locale.friendly_number(123) == '123'
    assert fr_locale.friendly_number(1234) == '1234'  # No comma for French
    assert fr_locale.friendly_number(1234567) == '1234567'  # No comma for French

    print("All tests passed for method friendly_number.")

# Generated at 2024-03-18 08:27:31.315673
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance
    locale = Locale("en_US")

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)
    gmt_offset = 0  # GMT

    # Test with day of week (dow=True)
    formatted_day_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_day_with_dow == "Saturday, April 15"

    # Test without day of week (dow=False)
    formatted_day_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_day_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT-5
    formatted_day_with_offset = locale.format_day(test_date, gmt_offset, dow=True)

# Generated at 2024-03-18 08:27:41.734298
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a date for testing
    test_date = datetime.datetime(2023, 3, 15, 12, 30)  # March 15, 2023, at 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Create a Locale instance for English
    en_locale = Locale.get('en_US')

    # Test format_day with day of week (dow=True)
    formatted_with_dow = en_locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_with_dow == "Wednesday, March 15", (
        f"Expected 'Wednesday, March 15', got '{formatted_with_dow}'"
    )

    # Test format_day without day of week (dow=False)
    formatted_without_dow = en_locale.format_day(test_date, gmt_offset, dow=False)

# Generated at 2024-03-18 08:28:28.362819
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:28:35.823572
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup
    locale_en = Locale.get('en_US')
    locale_fr = Locale.get('fr_FR')

    # Test with English locale, relative formatting
    now = datetime.datetime.utcnow()
    one_hour_ago = now - datetime.timedelta(hours=1)
    assert locale_en.format_date(one_hour_ago.timestamp()) == "1 hour ago"

    # Test with French locale, relative formatting
    assert locale_fr.format_date(one_hour_ago.timestamp()) == "il y a 1 heure"

    # Test with English locale, full formatting
    assert locale_en.format_date(one_hour_ago.timestamp(), relative=False, full_format=True) == one_hour_ago.strftime("%B %d, %Y at %I:%M %p")

    # Test with French locale, full formatting

# Generated at 2024-03-18 08:28:36.981751
# Unit test for function load_gettext_translations
def test_load_gettext_translations():import unittest
import tempfile
import shutil
import os


# Generated at 2024-03-18 08:28:45.776061
# Unit test for function load_gettext_translations
def test_load_gettext_translations():    import tempfile

# Generated at 2024-03-18 08:28:52.858829
# Unit test for function load_translations
def test_load_translations():    import tempfile

# Generated at 2024-03-18 08:29:00.883521
# Unit test for method format_date of class Locale
def test_Locale_format_date():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime, GMT offset, and relative=False
    specific_date = datetime.datetime(2023, 4, 1, 15, 30)
    formatted_date = locale.format_date(specific_date, gmt_offset=0, relative=False)
    assert formatted_date == "April 1, 2023 at 3:30 pm", f"Expected 'April 1, 2023 at 3:30 pm', got '{formatted_date}'"

    # Test with a specific datetime, GMT offset, and relative=True
    now = datetime.datetime.utcnow()
    seconds_ago = (now - specific_date).total_seconds()
    if seconds_ago < 60:
        expected = "1 second ago"
    elif seconds_ago < 3600:
        expected = f"{int(seconds_ago // 60)} minutes ago"

# Generated at 2024-03-18 08:29:02.479767
# Unit test for function load_gettext_translations
def test_load_gettext_translations():import os
import tempfile
import unittest


# Generated at 2024-03-18 08:29:03.830585
# Unit test for method translate of class CSVLocale
def test_CSVLocale_translate():import unittest


# Generated at 2024-03-18 08:29:11.134147
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance for testing
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT offset in minutes

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Saturday, April 15"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT offset in minutes (e.g., Eastern Time UTC-5)
    formatted

# Generated at 2024-03-18 08:29:22.111390
# Unit test for method format_day of class Locale
def test_Locale_format_day():    # Setup a Locale instance
    locale = Locale('en_US')

    # Test with a specific datetime and GMT offset
    test_date = datetime.datetime(2023, 4, 15, 12, 30)  # April 15, 2023, 12:30 PM
    gmt_offset = 0  # GMT

    # Test with day of week included
    formatted_date_with_dow = locale.format_day(test_date, gmt_offset, dow=True)
    assert formatted_date_with_dow == "Saturday, April 15"

    # Test without day of week included
    formatted_date_without_dow = locale.format_day(test_date, gmt_offset, dow=False)
    assert formatted_date_without_dow == "April 15"

    # Test with a different GMT offset
    gmt_offset = -300  # GMT -5 hours