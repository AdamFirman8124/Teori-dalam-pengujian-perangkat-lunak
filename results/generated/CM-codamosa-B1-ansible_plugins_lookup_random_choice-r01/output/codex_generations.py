

# Generated at 2026-10-24 19:53:48.639076
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:53:51.152381
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:53:53.570445
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:53:55.985120
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:53:58.403624
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:54:00.823470
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:54:03.238445
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:54:05.658245
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:54:08.075253
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:54:10.491558
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 19:54:23.360849
# Unit test for constructor of class LookupModule
def test_LookupModule():import random

# Generated at 2026-10-24 19:54:35.250950
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    def choose(items):
        assert items is terms
        return "green"

    monkeypatch.setattr(random, "choice", choose)
    assert lookup.run(terms) == ["green"]

    # Empty terms are returned unchanged without calling random.choice.
    def unexpected_choice(items):
        raise AssertionError("random.choice should not be called")

    monkeypatch.setattr(random, "choice", unexpected_choice)
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    def failing_choice(items):
        raise ValueError("selection failed")

    monkeypatch.setattr(random, "choice", failing_choice)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: selection failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 19:54:44.851319
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:54:52.032517
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 19:54:54.454686
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:54:56.872280
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:54:59.288620
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:01.705769
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:04.121207
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:06.539125
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:08.957944
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:11.373501
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:13.938217
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:16.353277
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:18.769435
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:21.183777
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:23.600026
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:26.017475
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:28.434289
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:30.850438
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:33.266178
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:35.686729
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:38.103582
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:40.519269
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:42.935357
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:45.351128
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:55:52.756801
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 19:56:07.606266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        result = lookup.run(empty_terms)

        assert result is empty_terms
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        try:
            lookup.run(terms)
        except AnsibleError as error:
            assert "Unable to choose random term: invalid terms" in str(error)
        else:
            raise AssertionError("Expected AnsibleError to be raised")

# Generated at 2026-10-24 19:56:16.615766
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:23.784788
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 19:56:33.922990
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:36.346327
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:38.764889
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:41.179927
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:43.596950
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:46.014480
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:48.433459
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:50.851542
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:53.267150
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:55.683504
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:56:58.099890
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:57:03.008576
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 19:57:13.141078
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged and does not call random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: invalid terms",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 19:57:23.074026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="second") as mock_choice:
        assert lookup.run(terms) == ["second"]
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

# Generated at 2026-10-24 19:57:31.170651
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("boom")):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-24 19:57:42.426649
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["alpha", "beta", "gamma"]

    result = lookup.run(terms)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    assert lookup.run(["only"]) == ["only"]
    assert lookup.run([]) == []

# Generated at 2026-10-24 19:57:53.156351
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # A selected term is returned inside a list.
    terms = ["alpha", "beta", "gamma"]
    with patch.object(random, "choice", return_value="beta") as mock_choice:
        assert lookup.run(terms) == ["beta"]
        mock_choice.assert_called_once_with(terms)

    # Errors from random.choice are wrapped as AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 19:58:06.188418
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:58:11.612731
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 19:58:21.660995
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # A selected term is wrapped in a list.
    terms = ["alpha", "beta", "gamma"]
    monkeypatch.setattr(random, "choice", lambda choices: choices[1])
    assert lookup.run(terms) == ["beta"]

    # Errors from random.choice are wrapped in AnsibleError.
    def raise_choice_error(choices):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_choice_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: choice failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 19:58:31.784580
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:58:36.532002
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 19:58:47.862720
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        result = lookup.run(terms)

    assert result == ["green"]
    mock_choice.assert_called_once_with(terms)


def test_LookupModule_run_with_empty_terms():
    lookup = LookupModule()

    with patch.object(random, "choice") as mock_choice:
        result = lookup.run([])

    assert result == []
    mock_choice.assert_not_called()


def test_LookupModule_run_wraps_random_choice_errors():
    lookup = LookupModule()

    with patch.object(random, "choice", side_effect=ValueError("choice failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: choice failed",
        ):
            lookup.run(["red", "green"])

# Generated at 2026-10-24 19:59:02.812254
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

import pytest

# Generated at 2026-10-24 19:59:11.212631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("test error")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: test error",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 19:59:21.039909
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # Returns the selected term wrapped in a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty terms are returned unchanged without calling random.choice.
    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        result = lookup.run(empty_terms)
        assert result is empty_terms
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert "Unable to choose random term: selection failed" in str(exc)
        else:
            raise AssertionError("Expected AnsibleError to be raised")

# Generated at 2026-10-24 19:59:31.576245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("boom")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert str(exc) == "Unable to choose random term: boom"
        else:
            raise AssertionError("Expected AnsibleError")

# Generated at 2026-10-24 19:59:42.338616
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:44.762560
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:47.180792
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:49.597822
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:52.016079
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:54.436181
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 19:59:56.852467
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:02.206807
# Unit test for method run of class LookupModule
def test_LookupModule_run():result = LookupModule().run(["only choice"])

# Generated at 2026-10-24 20:00:17.256758
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:24.224026
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 20:00:38.612176
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    # Verify a selected term is returned as a single-item list.
    monkeypatch.setattr(random, "choice", lambda choices: choices[1])
    assert lookup.run(terms) == ["two"]

    # Verify empty input is returned unchanged.
    assert lookup.run([]) == []

    # Verify selection errors are wrapped in AnsibleError.
    def raise_error(_):
        raise ValueError("selection failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: selection failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 20:00:41.031056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:43.447527
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:45.864672
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:48.284878
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:50.702702
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:53.119662
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:00:55.538454
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:03.131981
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 20:01:12.832208
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()

    terms = ["first", "second", "third"]
    monkeypatch.setattr(random, "choice", lambda choices: choices[1])

    assert lookup.run(terms) == ["second"]

    # Empty input is returned unchanged.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    # Errors from random.choice are wrapped as AnsibleError.
    def raise_error(_choices):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run(terms)

    assert str(exc_info.value) == "Unable to choose random term: choice failed"

# Generated at 2026-10-24 20:01:21.990060
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet"]

    with patch.object(random, "choice", return_value=terms[1]) as mock_choice:
        result = lookup.run(terms)

    assert result == [terms[1]]
    mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

# Generated at 2026-10-24 20:01:32.217248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A selected term is returned inside a single-item list.
    with patch.object(random, "choice", return_value="second") as mock_choice:
        assert lookup.run(terms) == ["second"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert str(exc) == "Unable to choose random term: selection failed"
        else:
            raise AssertionError("Expected AnsibleError to be raised")

# Generated at 2026-10-24 20:01:41.839356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run(empty_terms) is empty_terms
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=RuntimeError("boom")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: boom",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 20:01:44.261851
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:46.679367
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:49.097066
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:51.512754
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:53.928157
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:01:59.452229
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 20:02:06.927502
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:02:13.378605
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 20:02:22.803907
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
import random

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup import LookupBase


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["alpha", "beta", "gamma"]

    def choose_second(received_terms):
        assert received_terms is terms
        return received_terms[1]

    monkeypatch.setattr(random, "choice", choose_second)

    assert lookup.run(terms) == ["beta"]
    assert lookup.run([]) == []

    def raise_error(_terms):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: choice failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 20:02:36.481970
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # Returns the selected term wrapped in a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: invalid terms",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 20:02:47.993553
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest

# Generated at 2026-10-24 20:02:50.412077
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:02:52.829390
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:02:55.376555
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:03:02.926371
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:03:09.084222
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-24 20:03:18.402910
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 20:03:22.499631
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 20:03:35.401683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    import pytest

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        result = lookup.run(terms)

    assert result == ["green"]
    mock_choice.assert_called_once_with(terms)

    # Empty input should be returned unchanged.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    # Errors from random.choice should be converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 20:03:45.614626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 20:03:55.475719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    assert lookup.run([]) == []