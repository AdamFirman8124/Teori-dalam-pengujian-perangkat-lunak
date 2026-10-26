

# Generated at 2026-10-25 11:37:00.061321
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:37:02.480802
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:37:04.983402
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:37:07.397774
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 11:37:09.817577
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 11:37:12.228416
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 11:37:14.641678
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 11:37:34.299746
# Unit test for constructor of class LookupModule
def test_LookupModule():from ansible.plugins.lookup.random_choice import LookupModule

# Generated at 2026-10-25 11:37:37.353931
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 11:37:38.718107
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

# Generated at 2026-10-25 11:37:40.083834
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

# Generated at 2026-10-25 11:37:41.600567
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

# Generated at 2026-10-25 11:37:42.975884
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

# Generated at 2026-10-25 11:37:45.758548
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

# Generated at 2026-10-25 11:37:53.747533
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

# Generated at 2026-10-25 11:37:56.164294
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:37:58.577610
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:00.991616
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:03.489969
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:06.026379
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:08.441221
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:10.857840
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:13.272298
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:15.686598
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:18.100097
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:20.515003
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:22.929357
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:25.343205
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:27.760421
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:30.172973
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:32.587850
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:35.000415
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:37.414890
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:39.830494
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:42.245760
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:44.660866
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:47.078514
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:49.489458
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:51.903253
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:54.347293
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:56.761269
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:38:59.177303
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:01.591162
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:04.006587
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:06.420760
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:08.834562
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:11.249230
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:13.663080
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:16.076917
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:18.728251
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

    # Single-element list: choice is deterministic

# Generated at 2026-10-25 11:39:20.265628
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

# Generated at 2026-10-25 11:39:21.655690
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

# Generated at 2026-10-25 11:39:23.132519
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

# Generated at 2026-10-25 11:39:24.565098
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

# Generated at 2026-10-25 11:39:26.009887
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

# Generated at 2026-10-25 11:39:27.432785
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

# Generated at 2026-10-25 11:39:29.068968
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

# Generated at 2026-10-25 11:39:30.502922
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

# Generated at 2026-10-25 11:39:31.860451
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

# Generated at 2026-10-25 11:39:33.258987
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

# Generated at 2026-10-25 11:39:34.597576
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

# Generated at 2026-10-25 11:39:36.139677
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

# Generated at 2026-10-25 11:39:37.570654
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

# Generated at 2026-10-25 11:39:42.390364
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

# Generated at 2026-10-25 11:39:44.923980
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:47.459940
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:49.874297
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:52.288979
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:54.970798
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:57.384836
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:39:59.798289
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:02.541309
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:04.953414
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:07.368053
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:09.784636
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:12.197885
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:14.612547
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:17.025800
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:19.439484
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:21.853844
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:24.269180
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:26.683865
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:29.099566
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:31.513005
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:33.927176
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:36.341319
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:38.755324
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:41.170289
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:43.586931
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:45.999590
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:48.413028
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:51.213243
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:53.627789
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:56.160035
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:40:58.553176
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:00.968003
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:03.384158
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:05.795979
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:08.209866
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:10.624618
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:13.039071
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:15.454779
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:17.869835
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:20.287552
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:22.697989
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:25.111670
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:27.526087
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:29.940115
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:32.359325
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:34.773646
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:37.187566
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:39.600736
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:42.014511
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:44.428852
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:46.847073
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:49.260520
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:51.673797
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:54.089467
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:56.504466
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:41:58.919463
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:01.335521
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:05.794102
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:08.208977
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:10.624350
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:13.038665
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:15.451594
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:17.866237
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:20.278865
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:22.694065
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:25.110450
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:27.525118
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:29.937174
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:32.350581
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:34.765425
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:37.179134
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:39.595585
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:42.009666
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:44.424582
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:46.835735
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:49.248877
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:51.662921
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:54.077763
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:56.491567
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:42:58.905910
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:01.320086
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:03.733313
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:06.146022
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:08.559769
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:10.972905
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:13.388233
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:15.803685
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:22.449873
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:24.863305
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:27.277381
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:29.690828
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:32.106639
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:34.519483
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:36.932862
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:39.347255
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:41.761365
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:44.176123
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:46.590864
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:49.006312
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:51.419903
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:53.834294
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:56.249691
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:43:58.662998
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:01.133022
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:03.548853
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:05.963677
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:08.381403
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:10.798612
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:13.210526
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:15.624303
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:18.039123
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:20.452406
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:22.869379
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:25.287125
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:27.700747
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:30.114495
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:32.529722
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:43.378826
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:45.794061
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:48.219400
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:50.622232
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:53.037795
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:55.453665
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:44:57.871773
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:45:00.284341
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:45:03.166958
# Unit test for method run of class LookupModule
def test_LookupModule_run():lookup = LookupModule()

    # Single-element list: choice is deterministic

# Generated at 2026-10-25 11:45:04.945149
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

# Generated at 2026-10-25 11:45:07.097288
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

# Generated at 2026-10-25 11:45:08.621952
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

# Generated at 2026-10-25 11:45:10.319277
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

# Generated at 2026-10-25 11:45:11.909292
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

# Generated at 2026-10-25 11:45:14.370060
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

# Generated at 2026-10-25 11:46:09.151172
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

# Generated at 2026-10-25 11:46:32.498595
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

# Generated at 2026-10-25 11:46:34.159635
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

# Generated at 2026-10-25 11:46:42.021201
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

# Generated at 2026-10-25 11:46:43.559902
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

# Generated at 2026-10-25 11:46:48.984098
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

# Generated at 2026-10-25 11:46:51.403850
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:46:53.871759
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:46:56.483709
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:46:58.898097
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:47:01.313176
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 11:47:03.728068
# Unit test for method run of class LookupModule