

# Generated at 2026-10-24 13:37:15.020489
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:17.693429
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 13:37:19.058877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:20.372925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:28.627326
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule(loader=None, templar=None)
    assert isinstance(lookup, LookupModule)
    assert callable(lookup.run)

# Generated at 2026-10-24 13:37:29.959561
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule(loader=None, templar=None)
    assert isinstance(lookup, LookupModule)
    assert callable(lookup.run)

# Generated at 2026-10-24 13:37:31.398840
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:32.919470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:34.335451
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:35.719478
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:37.039961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:38.355193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:39.674369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:41.009419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:42.332362
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:43.671668
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:45.015634
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:46.328145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:37:48.849016
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:51.263061
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:53.677777
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:56.235036
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:58.648026
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:01.062968
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:03.476222
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:05.890699
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:08.303831
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:10.875056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:13.288046
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:15.704080
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:18.118273
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:20.531939
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:22.945925
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:25.362042
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:27.774453
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:30.191336
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:32.603833
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:35.016956
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:37.430458
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:39.843453
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:42.256550
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:44.671479
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:47.093091
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:49.501662
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:51.911985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:54.323712
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:56.737638
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:59.152402
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:01.565779
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:03.979511
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:06.394251
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:08.809105
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:11.248020
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:13.663813
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:16.074023
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:18.489035
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:20.904388
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:23.316417
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:25.734145
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:28.144774
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:30.556630
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:32.974653
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:35.387381
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:37.799859
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:40.216488
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:42.631339
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:45.045905
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:47.460517
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:49.876490
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:52.288970
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:54.702436
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:57.113185
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:59.524476
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:01.935603
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:04.350054
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:06.763676
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:09.176845
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:11.587771
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:14.027008
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:16.415759
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:18.831905
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:21.241852
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:23.655282
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:26.067802
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:28.481688
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:30.896996
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:33.311309
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:35.722868
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:38.138140
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:40.559818
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:42.976168
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:45.387088
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:47.801579
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:50.216611
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:52.631938
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:55.044253
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:57.463771
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:59.873090
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:02.287889
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:04.699776
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:07.118192
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:09.531193
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:11.954548
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:14.366869
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:16.784255
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:19.201007
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:21.613518
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:24.025688
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:26.438494
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:28.850735
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:31.266616
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:33.679501
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:36.090636
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:38.505309
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:40.918049
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:43.329449
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:45.741638
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:48.154702
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:50.570100
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:52.983029
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:55.396386
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:57.810094
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:00.222571
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:02.635218
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:05.051757
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:07.463955
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:09.877624
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:12.291487
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:14.707715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:17.119104
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:19.533752
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:21.949291
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:25.541247
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:40.191893
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

# Generated at 2026-10-24 13:42:41.658759
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:42.964008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:44.276693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:45.598457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:46.983487
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:48.315274
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:49.623631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:50.932778
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:52.295886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # 1. Empty input returns empty list
    assert lookup.run([]) == []

    # 2. Returns exactly the element chosen by random.choice
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        return_value="press the red button",
    ) as mock_choice:
        assert lookup.run(terms) == ["press the red button"]
        mock_choice.assert_called_once_with(terms)

    # 3. Real run returns one element from terms
    for _ in range(20):
        result = lookup.run(terms)
        assert len(result) == 1
        assert result[0] in terms

    # 4. random.choice failure is wrapped in AnsibleError
    with mock.patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=IndexError("list index out of range"),
    ):
        with pytest.raises(
            AnsibleError,
            match="Unable to choose random term: list index out of range",
        ):
            lookup.run(terms)

# Generated at 2026-10-24 13:42:58.389211
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:00.899090
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:03.313767
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:05.727457
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:08.141946
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:10.556380
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:12.970316
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:15.385332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:17.801091
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:20.214269
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:22.629576
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:25.248319
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:27.666564
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:30.075452
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:32.491527
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:34.903887
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:37.337319
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:39.742300
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:42.155182
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:44.568099
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:46.983106
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:49.397341
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:51.811271
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:54.223184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:56.639292
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:59.053896
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:01.465677
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:03.880064
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:06.294869
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:08.712039
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:19.721744
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:22.135249
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:24.549105
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:26.963678
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:29.378596
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:31.792710
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:34.206633
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:36.619765
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:39.033891
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:41.447732
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:43.862291
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:46.283366
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:48.702642
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:51.119484
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:53.537784
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:55.951214
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:58.366402
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:00.779856
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:03.196499
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:05.609475
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:08.033707
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:10.437039
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:12.852041
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:15.283261
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:17.699730
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:20.116275
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:22.530821
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:24.950864
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:27.364721
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:29.787410
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:02.762182
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:05.175905
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:07.593733
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:10.027692
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:12.447123
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:14.861889
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:17.279369
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:19.697310
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:22.110365
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:24.525098
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:26.937510
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:29.350940
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:31.764866
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:34.178341
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:36.594818
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:39.010352
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:41.424450
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:43.841604
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:46.255699
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:48.669026
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:51.084569
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:53.497146
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:55.909752
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:46:58.322541
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:00.734733
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:03.148402
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:05.562149
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:07.981510
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:10.398663
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:47:12.815138
# Unit test for method run of class LookupModule