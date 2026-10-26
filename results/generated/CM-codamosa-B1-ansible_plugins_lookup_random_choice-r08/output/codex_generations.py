

# Generated at 2026-10-25 14:24:19.827783
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


def test_LookupModule_run_wraps_choice_error():
    lookup = LookupModule()

    with patch.object(random, "choice", side_effect=ValueError("selection failed")):
        with pytest.raises(AnsibleError, match="Unable to choose random term: selection failed"):
            lookup.run(["red", "green"])

# Generated at 2026-10-25 14:24:27.827836
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

# Generated at 2026-10-25 14:24:29.261084
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

# Generated at 2026-10-25 14:24:40.423895
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 14:24:53.842069
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

import pytest

# Generated at 2026-10-25 14:24:59.290792
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:01.704592
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:04.118459
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:06.535519
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:11.974597
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:14.388281
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:16.801927
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:19.215965
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:21.631349
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:24.047287
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:26.460965
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:28.872259
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:31.287164
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:33.701735
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:36.116413
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:38.532867
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:40.949192
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:43.363342
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:45.794983
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:48.207061
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:50.623414
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:53.040720
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:55.452642
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:25:57.867501
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:00.285132
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:02.699642
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:05.120464
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:07.533536
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:09.947554
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:12.363475
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:14.780103
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:17.196543
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:19.614402
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:22.031286
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:24.447120
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:26.862858
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:29.277713
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:31.693925
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:34.107840
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:36.520616
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:38.934015
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:41.351367
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:43.766839
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:46.182135
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:48.595746
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:51.009626
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:53.423546
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:55.838029
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:26:58.255674
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:00.666435
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:03.079686
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:05.495885
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:07.910332
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:10.325334
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:15.874508
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:18.291591
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:20.706307
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:23.122464
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:25.539569
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:27.951242
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:30.366616
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:32.785527
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:35.199368
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:37.614360
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:40.028645
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:42.446055
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:44.863558
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:47.283999
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:49.698211
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:52.113618
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:54.528986
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:56.943027
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:27:59.357748
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:01.775268
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:04.192818
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:06.606873
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:09.021646
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:11.449745
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:13.868061
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:16.281140
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:18.696198
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:21.111175
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:23.530371
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:25.955455
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:28.365872
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:30.782900
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:33.200683
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:35.612877
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:38.028474
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:40.442246
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:42.860677
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:45.278856
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:47.688506
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:50.102975
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:52.519564
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:54.933368
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:57.347986
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:28:59.763197
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:02.180799
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:04.598414
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:07.012532
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:09.426455
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:11.841521
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:14.255984
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:19.699482
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:22.112814
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:24.529630
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:26.942118
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:29.354605
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:31.772735
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:34.187427
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:36.602277
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:39.019486
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:41.433162
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:43.847930
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:46.262956
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:48.677099
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:51.090876
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:53.509846
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:55.958252
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:29:58.590456
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:01.006308
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:03.421353
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:05.836680
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:08.252712
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:10.669662
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:13.083834
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:15.499433
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:17.911907
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:20.326636
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:22.742325
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:25.157248
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:27.573538
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:29.987505
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:32.405902
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:34.822991
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:37.257812
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:39.667870
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:42.081797
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:44.495883
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:46.910859
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:49.323686
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:51.741166
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:54.156453
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:56.573030
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:30:58.986742
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:01.405056
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:03.819655
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:06.231661
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:08.646328
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:12.932728
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:15.348391
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:17.763549
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:23.206741
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:25.622205
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:28.037179
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:30.450926
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:32.865957
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:35.281296
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:37.696722
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:40.110109
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:42.529181
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:44.945542
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:47.357688
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:49.772400
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:52.186731
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:54.601645
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:57.016067
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:31:59.430808
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:01.846545
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:04.264045
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:06.676632
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:09.090251
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:11.506698
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:13.920779
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:16.334539
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:18.750756
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:21.168851
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:23.582322
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:25.996803
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:33.584108
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:35.998551
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:38.412993
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:40.827290
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:43.251550
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:45.663231
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:48.077428
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:50.491866
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:52.930978
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:55.344733
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:32:57.759183
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:00.174651
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:02.587964
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:05.008072
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:07.420671
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:09.834417
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:12.250059
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:14.668682
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:17.082708
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:19.497265
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:21.910633
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:24.325293
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:29.764424
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:32.181723
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:34.599466
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:37.119518
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:39.532316
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:41.946324
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:44.360826
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 14:33:46.777071
# Unit test for method run of class LookupModule