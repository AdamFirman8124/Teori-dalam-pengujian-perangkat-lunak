

# Generated at 2026-10-24 15:14:48.753280
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    exc = FileSkipComment("example.py")

    assert str(exc) == "example.py contains an file skip comment and was skipped."
    assert exc.file_path == "example.py"


def test_FileSkipComment_is_a_FileSkipped():
    exc = FileSkipComment("example.py")

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, Exception)

# Generated at 2026-10-24 15:14:53.250607
# Unit test for constructor of class ISortError
def test_ISortError():
    # Can be instantiated with no arguments
    error = ISortError()
    assert str(error) == ""

    # Can be instantiated with a message
    error = ISortError("something went wrong")
    assert str(error) == "something went wrong"

    # Is an Exception subclass
    assert issubclass(ISortError, Exception)

    # Is catchable as Exception
    try:
        raise ISortError("boom")
    except Exception as e:
        assert str(e) == "boom"

# Generated at 2026-10-24 15:15:09.510879
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent_profile_xyz"
    assert profile not in profiles

    exc = ProfileDoesNotExist(profile)

    assert exc.profile == profile
    assert str(exc) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

# Generated at 2026-10-24 15:15:11.925034
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:15:14.338597
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:15:16.752536
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:19.176536
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:21.589571
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:24.003413
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:26.417743
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:28.829771
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:15:31.246781
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:33.655960
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:36.069382
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:38.485039
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:40.900803
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:43.316320
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:45.731812
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:48.151490
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:50.565425
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:52.976718
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:55.389995
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:15:57.803614
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:24.095169
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = dict

    exc = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.kind is kind
    assert exc.expected_kind is expected_kind

    expected_message = (
        f"isort was told to sort a literal of type {expected_kind} "
        f"but was given a literal of type {kind}."
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-24 15:16:29.551206
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:16:30.868633
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:16:33.284539
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:35.698057
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:38.109855
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:40.522622
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:42.936345
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:45.348797
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:47.763170
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:50.405471
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:52.813483
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:55.230776
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:16:57.644143
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:00.057433
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:02.470483
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:04.883913
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:07.297706
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:09.709969
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:12.123126
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:14.537185
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:16.950283
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:19.363507
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:21.776999
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:24.193675
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:26.604572
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:29.017742
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:36.871265
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Inherits from isort's base exception
    assert isinstance(error, ISortError)

    # Constructor attributes are exposed
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Message includes both types, expected first, given second
    assert str(error) == (
        "isort was told to sort a literal of type "
        f"{expected_kind} but was given a literal of type {kind}."
    )
    assert str(error) == (
        "isort was told to sort a literal of type "
        "<class 'list'> but was given a literal of type <class 'dict'>."
    )

# Generated at 2026-10-24 15:17:38.188011
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:39.506705
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:40.824585
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Inherits from isort's base exception
    assert isinstance(error, ISortError)

    # Constructor attributes are exposed
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Message includes both types, expected first, given second
    assert str(error) == (
        "isort was told to sort a literal of type "
        f"{expected_kind} but was given a literal of type {kind}."
    )
    assert str(error) == (
        "isort was told to sort a literal of type "
        "<class 'list'> but was given a literal of type <class 'dict'>."
    )

# Generated at 2026-10-24 15:17:42.138116
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:43.449340
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:44.764405
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Inherits from isort's base exception
    assert isinstance(error, ISortError)

    # Constructor attributes are exposed
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Message includes both types, expected first, given second
    assert str(error) == (
        "isort was told to sort a literal of type "
        f"{expected_kind} but was given a literal of type {kind}."
    )
    assert str(error) == (
        "isort was told to sort a literal of type "
        "<class 'list'> but was given a literal of type <class 'dict'>."
    )

# Generated at 2026-10-24 15:17:46.070819
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:47.374557
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)
assert error.kind is list
assert error.expected_kind is dict
assert isinstance(error, ISortError)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)

# Generated at 2026-10-24 15:17:48.694761
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Inherits from isort's base exception
    assert isinstance(error, ISortError)

    # Constructor attributes are exposed
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Message includes both types, expected first, given second
    assert str(error) == (
        "isort was told to sort a literal of type "
        f"{expected_kind} but was given a literal of type {kind}."
    )
    assert str(error) == (
        "isort was told to sort a literal of type "
        "<class 'list'> but was given a literal of type <class 'dict'>."
    )

# Generated at 2026-10-24 15:17:51.111506
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:53.646041
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:56.064288
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:17:58.477349
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:00.890547
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:03.305743
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:05.719737
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:08.332378
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:10.741734
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:13.157619
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:15.570178
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:17.983833
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:18:20.396005
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:18:22.808560
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:18:25.221441
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:18:27.635263
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:18:30.056274
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:18:32.466868
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:34.881012
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:37.290010
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:18:39.703169
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:18:42.115935
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:18:44.530604
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:18:46.945823
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 15:18:49.358222
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 15:18:51.770767
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 15:18:54.184941
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:18:59.368577
# Unit test for constructor of class FileSkipped
def test_FileSkipped():error = FileSkipped("file was skipped for some reason", "/path/to/file.py")

# Generated at 2026-10-24 15:19:05.237019
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    from isort.exceptions import IntroducedSyntaxErrors

    file_path = "example.py"
    exception = IntroducedSyntaxErrors(file_path)

    # Attributes set by constructor
    assert exception.file_path == file_path

    # Exception is part of the isort hierarchy
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message mentions the file path
    assert file_path in str(exception)

# Generated at 2026-10-24 15:19:06.674807
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    exc = FileSkipComment("example.py")

    assert str(exc) == "example.py contains an file skip comment and was skipped."
    assert exc.file_path == "example.py"


def test_FileSkipComment_is_a_FileSkipped():
    exc = FileSkipComment("example.py")

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, Exception)

# Generated at 2026-10-24 15:19:18.754824
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "file was skipped"
    file_path = "/path/to/file.py"

    exc = FileSkipped(message, file_path)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == file_path
    assert str(exc) == message
    assert exc.args == (message,)

    # file_path as keyword argument
    exc_kw = FileSkipped(message, file_path=file_path)
    assert exc_kw.file_path == file_path
    assert str(exc_kw) == message

# Generated at 2026-10-24 15:19:21.171401
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:23.585038
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:25.999890
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:28.412352
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:30.826336
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:33.238659
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:35.654415
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:19:38.067190
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:19:40.480781
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:19:42.893499
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:45.317186
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:47.876524
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:19:50.288714
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:52.702242
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:55.115471
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:19:57.529530
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:19:59.943757
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:20:02.367901
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:20:04.780138
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-24 15:20:07.193040
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-24 15:20:09.608793
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-24 15:20:12.022074
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:20:14.434821
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:20:16.849009
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:20:19.261925
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:20:21.678116
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:20:24.092156
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 15:20:26.505890
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:20:28.918387
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:20:31.331250
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:20:33.743312
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:20:36.156584
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:20:38.569880
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:20:40.982152
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:20:43.395150
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:20:45.807370
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:20:48.220717
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 15:20:50.634571
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 15:21:02.792702
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():err = AssignmentsFormatMismatch("not an assignment")

# Generated at 2026-10-24 15:21:04.105444
# Unit test for constructor of class ISortError
def test_ISortError():
    # Can be instantiated with no arguments
    error = ISortError()
    assert str(error) == ""

    # Can be instantiated with a message
    error = ISortError("something went wrong")
    assert str(error) == "something went wrong"

    # Is an Exception subclass
    assert issubclass(ISortError, Exception)

    # Is catchable as Exception
    try:
        raise ISortError("boom")
    except Exception as e:
        assert str(e) == "boom"

# Generated at 2026-10-24 15:21:20.611328
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "file was skipped"
    file_path = "/path/to/file.py"

    exc = FileSkipped(message, file_path)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == file_path
    assert str(exc) == message
    assert exc.args == (message,)

    # file_path as keyword argument
    exc_kw = FileSkipped(message, file_path=file_path)
    assert exc_kw.file_path == file_path
    assert str(exc_kw) == message

# Generated at 2026-10-24 15:21:21.944638
# Unit test for constructor of class ISortError
def test_ISortError():
    # Can be instantiated with no arguments
    error = ISortError()
    assert str(error) == ""

    # Can be instantiated with a message
    error = ISortError("something went wrong")
    assert str(error) == "something went wrong"

    # Is an Exception subclass
    assert issubclass(ISortError, Exception)

    # Is catchable as Exception
    try:
        raise ISortError("boom")
    except Exception as e:
        assert str(e) == "boom"

# Generated at 2026-10-24 15:21:24.359303
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:21:26.773596
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:21:29.186298
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:21:31.600275
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 15:21:34.011798
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 15:21:36.426438
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 15:21:38.839092
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:21:41.285254
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:21:43.667875
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:21:46.080925
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:21:48.497076
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:21:50.912579
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 15:21:53.326832
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:21:55.738812
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:21:58.155126
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 15:22:00.920543
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:22:03.623964
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:22:06.038430
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:22:08.451062
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:22:10.864569
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:22:18.186332
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():err = FormattingPluginDoesNotExist("black")

# Generated at 2026-10-24 15:22:29.142149
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():bash

# Generated at 2026-10-24 15:22:32.752239
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():error = ExistingSyntaxErrors("example.py")

# Generated at 2026-10-24 15:22:35.259397
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:22:37.844097
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:22:40.258016
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 15:22:42.672917
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:22:45.340958
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:22:47.754957
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:22:50.166344
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:22:52.578027
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:22:54.989022
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:22:57.411760
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:22:59.821083
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:23:02.234157
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:23:04.646949
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:23:07.064388
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:23:09.472957
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:23:11.888593
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:23:14.303649
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 15:23:18.988269
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():from isort.exceptions import ProfileDoesNotExist


# Generated at 2026-10-24 15:23:28.752590
# Unit test for constructor of class MissingSection
def test_MissingSection():
    error = MissingSection(import_module="requests", section="STDLIB")

    assert isinstance(error, MissingSection)
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert str(error) == (
        "Found requests import while parsing, but STDLIB was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert error.args[0] == str(error)

# Generated at 2026-10-24 15:23:30.147484
# Unit test for constructor of class ISortError
def test_ISortError():
    # Can be instantiated with no arguments
    error = ISortError()
    assert str(error) == ""

    # Can be instantiated with a message
    error = ISortError("something went wrong")
    assert str(error) == "something went wrong"

    # Is an Exception subclass
    assert issubclass(ISortError, Exception)

    # Is catchable as Exception
    try:
        raise ISortError("boom")
    except Exception as e:
        assert str(e) == "boom"

# Generated at 2026-10-24 15:23:47.658187
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "bad_option": {"value": "foo", "source": "pyproject.toml"},
        "another_bad": {"value": 123, "source": "setup.cfg"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    # stores input
    assert isinstance(exc, ISortError)
    assert exc.unsupported_settings == unsupported_settings

    # formats message via _format_option
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert "\t- bad_option = foo  (source: 'pyproject.toml')" in message
    assert "\t- another_bad = 123  (source: 'setup.cfg')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in message

    # exact formatting for single option
    single = {"unknown_opt": {"value": "bar", "source": "isort.cfg"}}
    single_exc = UnsupportedSettings(single)
    expected_errors = "\t- unknown_opt = bar  (source: 'isort.cfg')"
    expected_msg = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert single_exc.args[0] == expected_msg

# Generated at 2026-10-24 15:23:50.169593
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:23:52.581927
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 15:23:54.996228
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:23:57.414168
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:23:59.825798
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:02.239774
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:24:04.651654
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:24:07.066381
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-24 15:24:09.478658
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:11.894415
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:14.311655
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:16.725601
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:24:19.138216
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:24:21.555219
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-24 15:24:23.964302
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:26.377450
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:28.789926
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-24 15:24:31.206060
# Unit test for constructor of class LiteralParsingFailure