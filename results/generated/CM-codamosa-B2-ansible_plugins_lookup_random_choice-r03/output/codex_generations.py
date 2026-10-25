

# Generated at 2026-10-25 02:38:41.824691
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:38:46.523086
# Unit test for constructor of class LookupModule
def test_LookupModule():
    from ansible.plugins.lookup.random_choice import LookupModule

    # Instantiate the lookup plugin using its default constructor
    lookup = LookupModule()

    # Verify the instance was created and has the expected type
    assert lookup is not None
    assert isinstance(lookup, LookupModule)

# Generated at 2026-10-25 02:38:53.089047
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 02:38:58.208872
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 02:38:59.602124
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:00.943254
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:02.406179
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:03.747361
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:05.093571
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:06.502696
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:07.941250
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:09.372132
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:10.802924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:12.238340
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:13.589571
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:14.927652
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:16.253040
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:17.583866
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:18.915417
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:20.233559
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:39:22.652782
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:25.070165
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:27.602936
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:30.016990
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:32.588048
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:35.002586
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:37.414601
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:39.835472
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:42.249833
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:44.661578
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:47.077149
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:49.493238
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:51.909420
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:54.322036
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:56.741483
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:39:59.155052
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:01.569811
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:03.985170
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:05.380592
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:06.723208
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:08.057488
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:09.445785
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:10.769143
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:12.151355
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:13.501158
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:14.822393
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:16.161246
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:17.537971
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:18.869290
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:20.187514
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:21.519172
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:22.837393
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:24.162792
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:25.489787
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:26.829028
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:28.168442
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:29.550734
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:30.869498
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:32.201623
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:33.525872
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:40:36.064803
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:38.479849
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:41.012181
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:43.429484
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:45.843921
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:48.260519
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:50.790694
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:53.207178
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:55.622636
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:40:58.037712
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:00.455097
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:02.867855
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:05.283237
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:25.333521
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random as _random


# Generated at 2026-10-25 02:41:26.668626
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:27.996698
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:29.868047
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:31.195429
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:32.627629
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:33.958132
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:35.290756
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:36.619342
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:38.056081
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:39.388872
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:40.716785
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:41:43.242880
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:45.769184
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:48.283861
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:52.998812
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:55.511715
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:41:57.928472
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:00.342236
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:02.756571
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:05.172153
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:07.590063
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:08.973354
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random as _random


# Generated at 2026-10-25 02:42:10.312170
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:11.655924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:13.067460
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:14.510953
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:15.943086
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:17.390120
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:18.725397
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:26.464349
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:27.838754
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:29.206046
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:30.586714
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:32.020603
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:33.387490
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:34.785536
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:36.123537
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:37.450924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:42:39.983811
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:42.547908
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:42:44.945526
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:00.024880
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:02.439367
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:04.855366
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:07.272334
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:09.688305
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:12.105784
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:14.519874
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:16.933531
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:19.347686
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:21.760649
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:24.174230
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:26.588020
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:29.002374
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:43:41.038136
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-25 02:43:42.369638
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:43:43.698232
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:43:45.047927
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:43:46.378048
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:43:47.796314
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:44:17.287541
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:19.816977
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:22.231952
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:24.646462
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:27.075950
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:29.504025
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:31.922048
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:34.336604
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:36.754231
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:39.167874
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:41.583415
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:43.997845
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:46.411906
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:48.830426
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:51.241256
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:53.656035
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:56.071405
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:44:57.462179
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random as _random


# Generated at 2026-10-25 02:44:58.790105
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:45:00.189644
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:45:01.627043
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:45:03.044696
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:03.366830
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:04.718924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:06.073924
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:07.413389
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:08.761414
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:10.112355
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:11.448954
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:12.806094
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:14.152798
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:46:15.483019
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:11.930072
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:13.262791
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:14.591037
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:16.188362
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:17.580919
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:18.915921
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:20.386678
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:21.766462
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:23.151447
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 02:48:24.474817
# Unit test for method run of class LookupModule
def test_LookupModule_run():import random
import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_returns_single_element_from_list():
    terms = ["a", "b", "c"]
    result = LookupModule().run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_empty_terms_returns_empty_list():
    assert LookupModule().run([]) == []


def test_none_terms_returns_none():
    assert LookupModule().run(None) is None


def test_single_element_list():
    result = LookupModule().run(["only"])
    assert result == ["only"]


def test_all_elements_eventually_chosen():
    terms = ["a", "b", "c"]
    chosen = set()
    for _ in range(500):
        chosen.add(LookupModule().run(terms)[0])
    assert chosen == set(terms)


def test_error_wrapped_in_ansible_error(monkeypatch):
    def boom(seq):
        raise ValueError("nope")
    monkeypatch.setattr(random, "choice", boom)
    with pytest.raises(AnsibleError, match="Unable to choose random term: nope"):
        LookupModule().run(["a", "b"])