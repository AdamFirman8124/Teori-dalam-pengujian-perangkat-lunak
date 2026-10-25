

# Generated at 2026-10-24 11:07:16.094838
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:18.514685
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:20.932767
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:23.508935
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:25.931704
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:28.352699
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:30.769986
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:33.187157
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:35.607598
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:38.027521
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:40.451200
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:42.875709
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:45.296996
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:47.718519
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:50.140068
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 11:07:52.562985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:54.980522
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:57.397590
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:07:59.815451
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:02.233511
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:04.651280
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:07.071350
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:09.485181
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:11.905052
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:14.324144
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:16.742735
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:19.163874
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:21.581903
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:23.996176
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:26.415372
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:42.412084
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

# Generated at 2026-10-24 11:08:43.715783
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

# Generated at 2026-10-24 11:08:45.033320
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

# Generated at 2026-10-24 11:08:46.349374
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

# Generated at 2026-10-24 11:08:47.676786
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

# Generated at 2026-10-24 11:08:48.993286
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

# Generated at 2026-10-24 11:08:50.375880
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

# Generated at 2026-10-24 11:08:51.743484
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

# Generated at 2026-10-24 11:08:54.265092
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:56.851080
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:08:59.390638
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:01.923444
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:04.343904
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:06.763122
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:09.184894
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:11.604073
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:14.023756
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:16.444128
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:18.866536
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:21.288273
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:23.704683
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:26.123977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:28.544897
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:30.965357
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:33.386935
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:35.816628
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:38.233510
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:40.664853
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:43.083985
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:45.501926
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:47.918739
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:50.338808
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:52.755992
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:55.170768
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:09:57.588980
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:00.005900
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:02.422906
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:04.839157
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:07.256251
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:09.674394
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:12.090915
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:14.507993
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:16.924829
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:19.346079
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:21.762631
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:24.179057
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:26.599838
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:29.021131
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:10:38.903170
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 11:10:40.534624
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

# Generated at 2026-10-24 11:10:41.863619
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

# Generated at 2026-10-24 11:10:43.905736
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

# Generated at 2026-10-24 11:10:45.212845
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

# Generated at 2026-10-24 11:10:46.556604
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

# Generated at 2026-10-24 11:10:47.862808
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

# Generated at 2026-10-24 11:10:49.179831
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

# Generated at 2026-10-24 11:10:50.557284
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

# Generated at 2026-10-24 11:10:51.869454
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

# Generated at 2026-10-24 11:10:53.192227
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

# Generated at 2026-10-24 11:10:54.525557
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

# Generated at 2026-10-24 11:10:55.840394
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

# Generated at 2026-10-24 11:10:57.192952
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

# Generated at 2026-10-24 11:10:58.515846
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

# Generated at 2026-10-24 11:10:59.843743
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

# Generated at 2026-10-24 11:11:01.178757
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

# Generated at 2026-10-24 11:11:02.502849
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

# Generated at 2026-10-24 11:11:03.813146
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

# Generated at 2026-10-24 11:11:05.132349
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

# Generated at 2026-10-24 11:11:07.557965
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:09.989702
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:12.409943
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:14.831617
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:17.351764
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:19.775935
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:22.197817
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:24.617211
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:27.036962
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:29.454489
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:32.096008
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:34.516646
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:37.634723
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:11:40.226398
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

# Generated at 2026-10-24 11:11:41.543959
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

# Generated at 2026-10-24 11:11:42.859035
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

# Generated at 2026-10-24 11:11:44.220558
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

# Generated at 2026-10-24 11:11:45.592911
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

# Generated at 2026-10-24 11:11:46.904269
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

# Generated at 2026-10-24 11:11:48.266968
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

# Generated at 2026-10-24 11:11:49.578015
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

# Generated at 2026-10-24 11:11:50.986256
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

# Generated at 2026-10-24 11:11:52.305889
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

# Generated at 2026-10-24 11:11:56.175895
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

# Generated at 2026-10-24 11:11:57.486946
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

# Generated at 2026-10-24 11:11:58.815539
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

# Generated at 2026-10-24 11:12:00.139315
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

# Generated at 2026-10-24 11:12:01.481722
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

# Generated at 2026-10-24 11:12:02.808453
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

# Generated at 2026-10-24 11:12:04.173451
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

# Generated at 2026-10-24 11:12:05.557582
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

# Generated at 2026-10-24 11:12:06.887972
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

# Generated at 2026-10-24 11:12:08.223837
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

# Generated at 2026-10-24 11:12:17.610363
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:20.033837
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:22.451960
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:24.870429
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:27.504076
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:29.923789
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:32.341910
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:34.959341
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:37.557014
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:12:45.671073
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.random_choice import LookupModule

    # Case 1: non-empty list returns a single element that is one of the terms
    lookup = LookupModule()
    terms = ["a", "b", "c"]
    result = lookup.run(terms)
    assert result == [terms[0]] or result == [terms[1]] or result == [terms[2]]
    assert len(result) == 1

    # Case 2: empty list returns empty list unchanged
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []

    # Case 3: mocked random.choice returns the mocked element
    from unittest.mock import patch

    lookup = LookupModule()
    terms = ["go through the door", "drink from the goblet", "press the red button"]
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="drink from the goblet"):
        result = lookup.run(terms)
    assert result == ["drink from the goblet"]

    # Case 4: random.choice raising an exception is wrapped in AnsibleError
    from ansible.errors import AnsibleError

    lookup = LookupModule()
    with patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=Exception("boom")):
        try:
            lookup.run(["x", "y"])
            raised = False
        except AnsibleError as e:
            raised = True
            assert "boom" in str(e)
    assert raised

    # Case 5: single-element list always returns that element
    lookup = LookupModule()
    result = lookup.run(["only"])
    assert result == ["only"]

# Generated at 2026-10-24 11:12:46.980196
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

# Generated at 2026-10-24 11:12:48.298456
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

# Generated at 2026-10-24 11:12:49.618644
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

# Generated at 2026-10-24 11:12:50.926098
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

# Generated at 2026-10-24 11:12:52.250388
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

# Generated at 2026-10-24 11:12:53.564116
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

# Generated at 2026-10-24 11:13:14.388664
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:16.976898
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:19.408660
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:21.829391
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:24.250405
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:26.675515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:29.098086
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:31.524737
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:33.936252
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:36.352935
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:38.771072
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:41.192880
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:43.612853
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:46.035925
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:48.450986
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:50.870418
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:53.290487
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:55.715408
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:13:57.090906
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

# Generated at 2026-10-24 11:13:58.404487
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

# Generated at 2026-10-24 11:13:59.806157
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

# Generated at 2026-10-24 11:14:01.134085
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

# Generated at 2026-10-24 11:14:35.942582
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:38.356034
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:40.956799
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:14:42.291052
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

# Generated at 2026-10-24 11:14:43.946525
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

# Generated at 2026-10-24 11:14:45.251970
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

# Generated at 2026-10-24 11:14:46.568495
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

# Generated at 2026-10-24 11:14:47.881926
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

# Generated at 2026-10-24 11:14:49.210459
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

# Generated at 2026-10-24 11:14:50.529040
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

# Generated at 2026-10-24 11:14:51.836742
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

# Generated at 2026-10-24 11:14:53.163548
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

# Generated at 2026-10-24 11:16:04.529424
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:06.946894
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:09.367148
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:11.782887
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:14.200499
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:16.619240
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:19.036508
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:21.456700
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:23.872388
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:26.288271
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:28.705046
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:31.125545
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:33.540317
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:35.955990
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:38.375984
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:40.790974
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:43.214977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:45.631990
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 11:16:46.939512
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

# Generated at 2026-10-24 11:16:48.360737
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

# Generated at 2026-10-24 11:16:49.731168
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

# Generated at 2026-10-24 11:16:51.059211
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