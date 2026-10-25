

# Generated at 2026-10-24 05:49:45.082090
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:49:47.495061
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:49:49.910233
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:49:52.326644
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 05:49:54.743339
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 05:49:57.163716
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 05:49:59.577662
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:50:01.992917
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:50:21.272095
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random

# Generated at 2026-10-24 05:50:31.921660
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:50:46.447276
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:50:57.856211
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:00.273910
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:02.690441
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:05.104812
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:07.633787
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random

# Generated at 2026-10-24 05:51:18.411053
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    monkeypatch.setattr(random, "choice", lambda values: values[1])

    assert lookup.run(terms) == ["green"]
    assert lookup.run([]) == []

    def raise_error(values):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match=r"Unable to choose random term: choice failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 05:51:28.242600
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:30.849225
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:33.264706
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:35.679794
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:38.095231
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:40.512543
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:42.927011
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:45.351193
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:47.763805
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:50.177873
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:52.591417
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:55.007388
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:57.421863
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:51:59.842639
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:52:02.254273
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:52:04.668405
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:52:07.083921
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:52:08.408725
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:52:20.158663
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
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

# Generated at 2026-10-24 05:52:32.551561
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A non-empty sequence returns the selected item wrapped in a list.
    monkeypatch.setattr(random, "choice", lambda values: values[1])
    assert lookup.run(terms) == ["second"]

    # An empty sequence is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    def raise_choice_error(values):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_choice_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: choice failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 05:52:43.505797
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import Mock


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    choice_mock = Mock(return_value="two")
    monkeypatch.setattr(random, "choice", choice_mock)

    assert lookup.run(terms) == ["two"]
    choice_mock.assert_called_once_with(terms)

    # Empty input is returned unchanged and does not invoke random.choice.
    choice_mock.reset_mock()
    assert lookup.run([]) == []
    choice_mock.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    choice_mock.side_effect = ValueError("choice failed")
    with pytest.raises(AnsibleError, match="Unable to choose random term: choice failed"):
        lookup.run(terms)

# Generated at 2026-10-24 05:53:00.608012
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    choice_calls = []

    def fake_choice(values):
        choice_calls.append(values)
        return "second"

    monkeypatch.setattr(random, "choice", fake_choice)

    assert lookup.run(terms) == ["second"]
    assert choice_calls == [terms]

    # Empty terms are returned unchanged, without calling random.choice.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms
    assert choice_calls == [terms]

    # Errors from random.choice are wrapped in AnsibleError.
    def failing_choice(values):
        raise ValueError("boom")

    monkeypatch.setattr(random, "choice", failing_choice)

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run(terms)

    assert str(exc_info.value) == "Unable to choose random term: boom"

# Generated at 2026-10-24 05:53:03.110183
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:53:05.627165
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:53:08.042331
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:53:10.456798
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:53:12.878380
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:53:15.619223
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random

# Generated at 2026-10-24 05:53:27.135469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # Returns the item selected by random.choice.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
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

# Generated at 2026-10-24 05:53:41.774736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch
    import pytest

    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="second") as mock_choice:
        assert lookup.run(terms) == ["second"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice().
    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run(empty_terms) is empty_terms
        mock_choice.assert_not_called()

    # Errors from random.choice() are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:53:54.448513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    terms = ["one", "two", "three"]
    result = lookup.run(terms)

    assert len(result) == 1
    assert result[0] in terms

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

# Generated at 2026-10-24 05:54:06.751408
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # A selected term is returned inside a list.
    terms = ["red", "green", "blue"]
    monkeypatch.setattr(random, "choice", lambda values: values[1])
    assert lookup.run(terms) == ["green"]

    # Errors from random.choice are wrapped as AnsibleError.
    def raise_error(values):
        raise ValueError("selection failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match=r"^Unable to choose random term: selection failed$",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 05:54:09.342883
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:54:11.963212
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:54:14.381059
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:54:24.167749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch
    import pytest

    lookup = LookupModule()

    terms = ["one", "two", "three"]
    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("choice failed")):
        with pytest.raises(
            AnsibleError,
            match=r"^Unable to choose random term: choice failed$",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:54:34.619745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        result = lookup.run(terms)

    assert result == ["green"]
    mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:54:45.807031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped as AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: invalid terms",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:55:02.776807
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

    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert str(exc) == "Unable to choose random term: selection failed"
        else:
            raise AssertionError("Expected AnsibleError")

# Generated at 2026-10-24 05:55:14.654246
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:55:17.075226
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:55:18.372075
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:55:29.804807
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("boom")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: boom",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:55:40.095534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # Returns the selected term wrapped in a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
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

# Generated at 2026-10-24 05:55:50.285286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty terms are returned unchanged without invoking random.choice.
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

# Generated at 2026-10-24 05:56:02.571210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(AnsibleError, match="Unable to choose random term: selection failed"):
            lookup.run(terms)

# Generated at 2026-10-24 05:56:12.107165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:56:22.100925
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:56:23.564418
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:56:33.909075
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    # A non-empty list returns the selected item wrapped in a list.
    monkeypatch.setattr(random, "choice", lambda choices: choices[1])
    assert lookup.run(terms) == ["second"]

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    def raise_error(choices):
        raise RuntimeError("boom")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: boom",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 05:56:46.301400
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
            raise AssertionError("Expected AnsibleError")

# Generated at 2026-10-24 05:56:57.458747
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
    with patch.object(random, "choice", side_effect=ValueError("invalid terms")):
        with pytest.raises(
            AnsibleError,
            match=r"Unable to choose random term: invalid terms",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:57:06.786239
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    def choose_green(values):
        assert values is terms
        return "green"

    monkeypatch.setattr(random, "choice", choose_green)

    assert lookup.run(terms) == ["green"]

    # Empty input is returned unchanged and does not call random.choice.
    empty_terms = []
    assert lookup.run(empty_terms) is empty_terms

    # Errors from random.choice are wrapped in AnsibleError.
    def raise_error(_values):
        raise ValueError("choice failed")

    monkeypatch.setattr(random, "choice", raise_error)

    with pytest.raises(
        AnsibleError,
        match="Unable to choose random term: choice failed",
    ):
        lookup.run(terms)

# Generated at 2026-10-24 05:57:17.542847
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:57:18.961213
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:57:29.409350
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:57:30.737284
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:57:42.721304
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    # Returns the randomly selected term wrapped in a list.
    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    # Errors from random.choice are converted to AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("test error")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: test error",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:58:00.642110
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:58:02.073246
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:58:11.392215
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:58:12.712658
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:58:22.466958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["alpha", "beta", "gamma"]

    with patch.object(random, "choice", return_value="beta") as mock_choice:
        result = lookup.run(terms)

    assert result == ["beta"]
    mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
    with patch.object(random, "choice") as mock_choice:
        result = lookup.run([])

    assert result == []
    mock_choice.assert_not_called()

# Generated at 2026-10-24 05:58:38.631236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["first", "second", "third"]

    with patch.object(random, "choice", return_value="second") as mock_choice:
        assert lookup.run(terms) == ["second"]
        mock_choice.assert_called_once_with(terms)

    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("boom")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: boom",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:58:49.587527
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    empty_terms = []
    with patch.object(random, "choice") as mock_choice:
        result = lookup.run(empty_terms)
        assert result is empty_terms
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:59:00.033496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch
    import pytest

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    # A selected term is returned inside a list.
    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged without calling random.choice.
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

# Generated at 2026-10-24 05:59:09.761337
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:59:11.199393
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:59:21.465969
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["red", "green", "blue"]

    # Returns the randomly selected term wrapped in a list.
    with patch.object(random, "choice", return_value="green") as mock_choice:
        assert lookup.run(terms) == ["green"]
        mock_choice.assert_called_once_with(terms)

    # Empty input is returned unchanged.
    assert lookup.run([]) == []

    # Errors from random.choice are wrapped in AnsibleError.
    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: selection failed",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 05:59:32.083006
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 05:59:33.723804
# Unit test for method run of class LookupModule
def test_LookupModule_run():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-24 05:59:46.421189
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["one", "two", "three"]

    with patch.object(random, "choice", return_value="two") as mock_choice:
        assert lookup.run(terms) == ["two"]
        mock_choice.assert_called_once_with(terms)

    with patch.object(random, "choice") as mock_choice:
        assert lookup.run([]) == []
        mock_choice.assert_not_called()

    with patch.object(random, "choice", side_effect=ValueError("test error")):
        try:
            lookup.run(terms)
        except AnsibleError as exc:
            assert str(exc) == "Unable to choose random term: test error"
        else:
            raise AssertionError("Expected AnsibleError to be raised")