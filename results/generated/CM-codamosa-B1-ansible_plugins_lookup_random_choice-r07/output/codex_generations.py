

# Generated at 2026-10-24 21:09:05.686254
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:08.110119
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:10.521873
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:12.938866
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:15.364275
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:17.783901
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:20.199779
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:22.648450
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:25.031419
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:27.449175
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:29.865677
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:32.285619
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:34.702631
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:37.117165
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:39.534156
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 21:09:41.948702
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:44.364808
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:46.783680
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:49.199216
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:51.615057
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:54.033742
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:56.449661
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:09:58.867025
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:01.283985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:03.706482
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:06.121423
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:08.539481
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:10.958093
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:13.375734
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:15.791409
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:10:23.867939
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 21:10:38.405271
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A non-empty list returns exactly the item selected by random.choice.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run(empty_terms) is empty_terms
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert str(exc) == "Unable to choose random term: selection failed"
        else:
            raise AssertionError("Expected AnsibleError to be raised")

# Generated at 2026-10-24 21:10:49.879873
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    with patch.object(random, "choice", return_value="second") as mock_choice:
        assert lookup.run(terms) == ["second"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped as AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:10:59.605368
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["alpha", "beta", "gamma"]

    # Returns the item selected by random.choice wrapped in a list.
    with patch.object(random, "choice", return_value="beta") as mock_choice:
        assert lookup.run(terms) == ["beta"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted into AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:11:08.104818
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:10.526359
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:12.942066
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:15.358786
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:17.778303
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:20.193370
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:22.610437
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:25.030124
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:27.447195
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:29.863034
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:32.279740
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:34.696203
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:37.111003
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:39.529425
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:41.943778
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:44.362030
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:11:50.298452
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:12:00.842838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty terms are returned unchanged.
    assert lookup.run([]) == []

    # A non-empty list returns the selected item wrapped in a list.
    terms = ["alpha", "beta", "gamma"]
    with patch.object(random, "choice", return_value="beta") as mock_choice:
        assert lookup.run(terms) == ["beta"]
        mock_choice.assert_called_once_with(terms)

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:12:10.331159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # A single-item list produces a deterministic result.
    terms = ["only choice"]
    assert lookup.run(terms) == ["only choice"]

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

# Generated at 2026-10-24 21:12:23.368140
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    monkeypatch.setattr(random, "choice", lambda choices: choices[1])
    assert lookup.run(terms) == ["green"]

    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    def raise_error(choices):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(AnsibleError, match="Unable to choose random term: choice failed"):
        lookup.run(terms)

# Generated at 2026-10-24 21:12:25.787730
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:28.203136
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:30.619001
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:33.033923
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:35.453575
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:37.870139
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:40.287272
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:42.703248
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:45.118728
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:47.536583
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:49.951548
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:52.368451
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:54.784433
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:57.203314
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:12:59.621189
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:02.040935
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:04.458070
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:06.877910
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:18.772606
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:13:28.906259
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:35.240226
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:13:46.341529
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:48.764667
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:13:51.181065
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:01.969664
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:14:12.323017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped as AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: invalid terms",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:14:24.331311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    # A non-empty list returns the randomly selected term in a list.
    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty and otherwise false-valued inputs are returned unchanged.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms
    assert lookup.run(None) is None

    # Errors raised by random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("choice failed")):
        with pytest.raises(AnsibleError) as exc_info:
            lookup.run(terms)

    assert str(exc_info.value) == "Unable to choose random term: choice failed"

# Generated at 2026-10-24 21:14:35.875657
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("choice failed")):
        try:
            lookup.run(terms)
        except AnsibleError as error:
            assert str(error) == "Unable to choose random term: choice failed"
        else:
            raise AssertionError("Expected AnsibleError")

# Generated at 2026-10-24 21:14:38.298250
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:40.715922
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:43.137818
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:45.689529
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:48.109646
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:14:50.528544
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:01.269914
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:15:11.614805
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A non-empty sequence returns the selected item wrapped in a list.
    def choose_second(values):
        assert values is terms
        return values[1]

    monkeypatch.setattr(random, "choice", choose_second)
    assert lookup.run(terms) == ["second"]

    # An empty sequence is returned unchanged without calling random.choice.
    def unexpected_choice(values):
        raise AssertionError("random.choice must not be called for empty terms")

    monkeypatch.setattr(random, "choice", unexpected_choice)
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    # Errors from random.choice are converted to AnsibleError.
    def failing_choice(values):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", failing_choice)

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run(terms)

    assert str(exc_info.value) == "Unable to choose random term: choice failed"

# Generated at 2026-10-24 21:15:22.468907
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    monkeypatch.setattr(random, "choice", lambda values: values[1])
    assert lookup.run(terms) == ["green"]

    # Empty input is returned unchanged.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    # Errors from random.choice are wrapped in AnsibleError.
    def raise_error(_values):
        raise ValueError("selection failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match=r"^Unable to choose random term: selection failed$",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 21:15:24.889756
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:27.571686
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:29.992913
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:32.408639
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:34.827830
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:37.405686
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:39.827013
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:42.242944
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:44.663686
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:47.223765
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:49.644198
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:52.060331
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:54.480231
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:56.895960
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:15:59.314920
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:16:01.735841
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:16:09.467930
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:16:19.095744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    result = lookup.run(terms)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # Empty input should be returned unchanged.
    assert lookup.run([]) == []

# Generated at 2026-10-24 21:16:32.293009
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch
    import pytest

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(AnsibleError, match="Unable to choose random term: selection failed"):
            lookup.run(terms)

# Generated at 2026-10-24 21:16:41.930697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A non-empty input returns the selected item wrapped in a list.
    with patch.object(random, "choice", return_value="second") as mock_choice:
        result = lookup.run(terms)

    assert result == ["second"]
    mock_choice.assert_called_once_with(terms)

    # An empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        result = lookup.run([])

    assert result == []
    mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:16:50.229258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    # A non-empty list returns the selected item wrapped in a list.
    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 21:16:52.763494
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:16:55.180117
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:16:57.596413
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:00.013749
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:02.610321
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:05.028539
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:15.438794
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:20.953555
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 21:17:30.419466
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:32.842897
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:35.258951
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:37.675224
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:40.244329
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:42.656885
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:45.077132
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:47.496517
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:49.913906
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:52.331321
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:54.903227
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:57.317477
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:17:59.735764
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:02.154379
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:04.570884
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:06.986563
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:09.406619
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:15.079112
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 21:18:30.474437
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:36.208451
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 21:18:38.627924
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:41.049423
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:43.467387
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:45.886494
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:48.302029
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:50.719572
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:53.138616
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:55.558908
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:18:57.973955
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:19:00.392293
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:19:02.808969
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 21:19:05.224752
# Unit test for method run of class LookupModule