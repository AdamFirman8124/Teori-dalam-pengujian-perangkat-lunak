

# Generated at 2026-10-25 09:09:58.783078
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 09:10:04.824417
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 09:10:06.359041
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 09:10:33.397296
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 09:10:34.828028
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 09:10:57.659338
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:11:27.069828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:11:48.350438
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:12:04.850153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:12:06.462485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:12:07.856185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:12:27.423608
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:12:48.054989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 09:12:50.473697
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:12:53.095020
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:12:55.511938
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:12:57.928821
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:00.348456
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:02.764896
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:05.181045
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:07.623181
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:10.039397
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:12.456780
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:14.872219
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:17.289450
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:19.705128
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:22.245852
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:24.661159
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:27.077346
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:29.494686
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:31.911865
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:34.328300
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:36.744626
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:39.157265
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:41.572794
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:43.993049
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:46.412495
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:48.828800
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:51.243607
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:53.659963
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:56.082788
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:13:58.497597
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:00.913750
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:03.330823
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:05.746682
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:08.164744
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:10.583974
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:12.997050
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:15.415715
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:17.831861
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:20.246804
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:22.664694
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:25.080467
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:27.496433
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:29.966636
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:32.376877
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:34.794972
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:37.210987
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:39.629474
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:42.048895
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:44.468524
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:46.882533
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:49.300654
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:51.717081
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:54.139538
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:56.554493
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:14:58.969960
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:10.948144
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch


# Generated at 2026-10-25 09:15:12.428875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:15:13.869044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:15:30.406718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:15:32.821166
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:35.235379
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:37.647777
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:40.061023
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:42.475163
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:44.888478
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:47.300425
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:49.712748
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:52.142865
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:54.558999
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:56.983470
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:15:59.398388
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:01.814067
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:13.874147
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

    # Single-element list: choice is deterministic

# Generated at 2026-10-25 09:16:19.506140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:21.030117
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:22.590437
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:24.013284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:25.549470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:27.085813
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:16:43.676519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 09:16:46.369387
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:49.004297
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:51.423273
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:53.868131
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:56.254313
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:16:58.967960
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:17:01.350391
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:17:03.767562
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:17:06.182178
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:17:22.790359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:17:29.235174
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:17:59.858276
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # 1. normal case: returns single-element list with member of terms
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

    # 2. deterministic case: mock random.choice
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="mocked") as mock_choice:
        result = lookup.run(terms)
        mock_choice.assert_called_once_with(terms)
        assert result == ["mocked"]

    # 3. single element list
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="only") as mock_choice:
        result = lookup.run(["only"])
        assert result == ["only"]

    # 4. empty list returns as-is (no choice made)
    assert lookup.run([]) == []
    assert lookup.run([], inject={"host": "test"}) == []

    # 5. extra kwargs / inject are ignored
    with patch("ansible.plugins.lookup.random_choice.random.choice", return_value="a"):
        assert lookup.run(["a", "b"], inject={}, foo="bar") == ["a"]

    # 6. exception in random.choice is wrapped as AnsibleError
    with patch(
        "ansible.plugins.lookup.random_choice.random.choice",
        side_effect=Exception("boom")
    ):
        with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
            lookup.run(terms)

# Generated at 2026-10-25 09:18:02.531211
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:04.952043
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:07.366622
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:09.783493
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:12.198890
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:14.614690
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:17.261037
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:19.678850
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:22.094579
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:24.507323
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:26.920488
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:29.338231
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:31.750217
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:34.165129
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:36.578043
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:39.000718
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:41.412581
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:43.824553
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:46.269862
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:48.685025
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:51.101522
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:53.516438
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:55.930967
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:18:58.345104
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:19:00.758746
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:19:03.173043
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:19:05.612030
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 09:19:22.206892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])

# Generated at 2026-10-25 09:19:38.981816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    lookup = LookupModule()

    for _ in range(20):
        result = lookup.run(terms)
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] in terms


def test_LookupModule_run_single_term():
    result = LookupModule().run(["only-one"])
    assert result == ["only-one"]


def test_LookupModule_run_empty_terms():
    result = LookupModule.run(LookupModule, [])
    assert result == []


def test_LookupModule_run_raises_ansible_error(mocker):
    mocker.patch("ansible.plugins.lookup.random_choice.random.choice", side_effect=RuntimeError("boom"))

    with pytest.raises(AnsibleError, match="Unable to choose random term: boom"):
        LookupModule().run(["a", "b"])