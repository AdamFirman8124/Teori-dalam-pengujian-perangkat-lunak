

# Generated at 2026-10-25 02:07:40.288318
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 02:07:47.046730
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 02:07:54.008573
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 02:08:00.159643
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 02:08:06.399076
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

# Generated at 2026-10-25 02:08:07.735750
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

# Generated at 2026-10-25 02:08:09.163268
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

# Generated at 2026-10-25 02:08:10.596983
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

# Generated at 2026-10-25 02:08:12.030417
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

# Generated at 2026-10-25 02:08:13.351770
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

# Generated at 2026-10-25 02:08:14.795099
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

# Generated at 2026-10-25 02:08:16.127901
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

# Generated at 2026-10-25 02:08:17.559799
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

# Generated at 2026-10-25 02:08:18.994397
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

# Generated at 2026-10-25 02:08:20.426959
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

# Generated at 2026-10-25 02:08:21.767063
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

# Generated at 2026-10-25 02:08:23.191555
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

# Generated at 2026-10-25 02:08:24.574702
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

# Generated at 2026-10-25 02:08:26.162388
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

# Generated at 2026-10-25 02:08:27.519685
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

# Generated at 2026-10-25 02:08:28.864351
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

# Generated at 2026-10-25 02:08:30.264589
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

# Generated at 2026-10-25 02:08:31.699970
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

# Generated at 2026-10-25 02:08:33.148981
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

# Generated at 2026-10-25 02:08:34.542488
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

# Generated at 2026-10-25 02:08:35.880078
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

# Generated at 2026-10-25 02:08:37.236956
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

# Generated at 2026-10-25 02:08:38.572451
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

# Generated at 2026-10-25 02:08:39.936042
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

# Generated at 2026-10-25 02:08:41.423244
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

# Generated at 2026-10-25 02:08:42.860460
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

# Generated at 2026-10-25 02:08:44.178381
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

# Generated at 2026-10-25 02:08:45.618362
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

# Generated at 2026-10-25 02:08:47.248142
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

# Generated at 2026-10-25 02:08:49.780877
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:08:52.457147
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:08:54.879005
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:08:57.466495
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:08:59.980255
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:02.397429
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:04.812123
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:07.226980
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:09.830328
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:12.249740
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:14.673425
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:17.082027
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:19.495769
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:09:26.373468
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-25 02:09:27.806706
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

# Generated at 2026-10-25 02:09:29.240653
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

# Generated at 2026-10-25 02:09:30.674772
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

# Generated at 2026-10-25 02:09:32.108039
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

# Generated at 2026-10-25 02:09:33.541939
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

# Generated at 2026-10-25 02:09:34.984736
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

# Generated at 2026-10-25 02:09:36.406675
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

# Generated at 2026-10-25 02:09:37.732316
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

# Generated at 2026-10-25 02:09:39.147452
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

# Generated at 2026-10-25 02:09:40.607348
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

# Generated at 2026-10-25 02:09:42.040261
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

# Generated at 2026-10-25 02:09:43.364759
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

# Generated at 2026-10-25 02:09:44.690005
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

# Generated at 2026-10-25 02:09:46.031039
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

# Generated at 2026-10-25 02:09:47.366115
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

# Generated at 2026-10-25 02:09:48.685774
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

# Generated at 2026-10-25 02:09:50.334622
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

# Generated at 2026-10-25 02:09:51.668151
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

# Generated at 2026-10-25 02:09:52.999363
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

# Generated at 2026-10-25 02:09:54.635787
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

# Generated at 2026-10-25 02:09:55.958588
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

# Generated at 2026-10-25 02:09:57.400788
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

# Generated at 2026-10-25 02:09:59.039745
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

# Generated at 2026-10-25 02:10:00.369619
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

# Generated at 2026-10-25 02:10:01.803618
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

# Generated at 2026-10-25 02:10:03.163474
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

# Generated at 2026-10-25 02:10:07.391961
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:09.922780
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:12.337571
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:14.756459
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:17.174419
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:19.744322
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:22.164315
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:24.588423
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:27.002972
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:29.422014
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:31.838943
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:34.252461
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:36.669444
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 02:10:43.379421
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-25 02:10:44.811825
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

# Generated at 2026-10-25 02:10:46.349121
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

# Generated at 2026-10-25 02:10:47.781488
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

# Generated at 2026-10-25 02:10:49.215601
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

# Generated at 2026-10-25 02:10:50.547460
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

# Generated at 2026-10-25 02:10:56.823655
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

# Generated at 2026-10-25 02:10:58.149149
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

# Generated at 2026-10-25 02:10:59.558570
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

# Generated at 2026-10-25 02:11:00.992633
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

# Generated at 2026-10-25 02:11:02.430218
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

# Generated at 2026-10-25 02:11:03.783251
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

# Generated at 2026-10-25 02:11:05.152943
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

# Generated at 2026-10-25 02:11:06.521212
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

# Generated at 2026-10-25 02:11:07.845139
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

# Generated at 2026-10-25 02:11:09.167403
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

# Generated at 2026-10-25 02:11:22.211111
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

# Generated at 2026-10-25 02:11:23.827345
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

# Generated at 2026-10-25 02:11:25.145708
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

# Generated at 2026-10-25 02:11:26.607247
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

# Generated at 2026-10-25 02:11:27.922047
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

# Generated at 2026-10-25 02:11:29.360232
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

# Generated at 2026-10-25 02:11:30.680883
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

# Generated at 2026-10-25 02:11:31.999169
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

# Generated at 2026-10-25 02:11:33.325339
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

# Generated at 2026-10-25 02:11:34.695084
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

# Generated at 2026-10-25 02:12:01.613357
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

# Generated at 2026-10-25 02:12:03.017744
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

# Generated at 2026-10-25 02:12:04.378123
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

# Generated at 2026-10-25 02:12:05.743914
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

# Generated at 2026-10-25 02:12:07.133582
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

# Generated at 2026-10-25 02:12:08.461023
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

# Generated at 2026-10-25 02:12:09.906905
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

# Generated at 2026-10-25 02:12:11.327620
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

# Generated at 2026-10-25 02:12:12.880809
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

# Generated at 2026-10-25 02:12:14.208950
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

# Generated at 2026-10-25 02:13:01.196224
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

# Generated at 2026-10-25 02:13:02.522837
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

# Generated at 2026-10-25 02:13:03.851795
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

# Generated at 2026-10-25 02:13:05.193196
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

# Generated at 2026-10-25 02:13:06.637085
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

# Generated at 2026-10-25 02:13:08.070941
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

# Generated at 2026-10-25 02:13:09.504728
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

# Generated at 2026-10-25 02:13:11.151924
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

# Generated at 2026-10-25 02:13:12.468839
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

# Generated at 2026-10-25 02:13:13.793272
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

# Generated at 2026-10-25 02:14:58.150907
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

# Generated at 2026-10-25 02:14:59.584416
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

# Generated at 2026-10-25 02:15:00.919079
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

# Generated at 2026-10-25 02:15:02.349615
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

# Generated at 2026-10-25 02:15:03.772841
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

# Generated at 2026-10-25 02:15:05.100038
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

# Generated at 2026-10-25 02:15:06.451611
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

# Generated at 2026-10-25 02:15:07.879406
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

# Generated at 2026-10-25 02:15:09.290282
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

# Generated at 2026-10-25 02:15:10.643828
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