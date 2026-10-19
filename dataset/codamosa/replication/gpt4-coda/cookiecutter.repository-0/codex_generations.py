

# Generated at 2024-03-18 05:09:14.490258
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():    from unittest.mock import patch


# Generated at 2024-03-18 05:09:20.549765
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        "gh": "https://github.com/{0}",
        "gl": "https://gitlab.com/{0}",
        "bb": "https://bitbucket.org/{0}",
    }

    # Test expansion with no colon

# Generated at 2024-03-18 05:09:26.213025
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:09:29.792800
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:09:32.863096
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:09:35.669799
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:09:41.504906
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        "gh": "https://github.com/{0}",
        "gl": "https://gitlab.com/{0}",
        "bb": "https://bitbucket.org/{0}",
    }

    # Test expansion with no colon

# Generated at 2024-03-18 05:09:45.255339
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:09:47.273427
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:09:51.512531
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:04.248091
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        "gh": "https://github.com/{0}",
        "gl": "https://gitlab.com/{0}",
        "bb": "https://bitbucket.org/{0}",
    }

    # Test expansion with no colon

# Generated at 2024-03-18 05:10:07.441708
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:10.190268
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:10.910415
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():from unittest.mock import patch


# Generated at 2024-03-18 05:10:15.449911
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:18.359486
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:19.004780
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():from unittest.mock import patch


# Generated at 2024-03-18 05:10:21.022499
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:28.580506
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    # Test abbreviation expansion
    abbreviations = {
        "gh": "https://github.com/{0}",
        "bb": "https://bitbucket.org/{0}"
    }

    # Test with no abbreviation
    assert expand_abbreviations("not-an-abbreviation", abbreviations) == "not-an-abbreviation"

    # Test with abbreviation without specifier
    assert expand_abbreviations("gh", abbreviations) == "https://github.com/{0}"

    # Test with abbreviation with specifier
    assert expand_abbreviations("gh:audreyr/cookiecutter-pypackage", abbreviations) == "https://github.com/audreyr/cookiecutter-pypackage"

    # Test with abbreviation that is not in the dictionary
    assert expand_abbreviations("gl:someone/some-repo", abbreviations) == "gl:someone/some-repo"


# Generated at 2024-03-18 05:10:31.530327
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:38.041804
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:40.687206
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:42.969653
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:45.028606
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:49.102896
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:52.479220
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:55.484150
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:10:58.411122
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:00.487618
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:11:02.742435
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:11.414508
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:14.828758
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:17.489551
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:18.953963
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:11:21.180585
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:31.848154
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:33.999309
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:36.058763
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:39.526341
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:41.597726
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:50.082067
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:52.310846
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:55.035969
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:57.419281
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:11:59.454453
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:03.594367
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:05.650085
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:08.258629
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:10.227774
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:13.932357
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:39.292698
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:12:42.877103
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:45.066051
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:46.839741
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:48.611011
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:50.877736
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:53.194063
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:56.322083
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:12:58.131355
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:00.163467
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:21.884225
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:24.411707
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:26.299073
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:28.908681
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:31.784253
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:34.235000
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:37.010725
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:39.609854
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:41.882055
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:13:51.678837
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:26.863452
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:28.296117
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, mock_open


# Generated at 2024-03-18 05:14:30.397464
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:32.484692
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:34.598536
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:37.216781
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:39.089369
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:42.386919
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:45.388918
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:14:47.759600
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:15:54.288469
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:15:56.152294
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:15:58.777799
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:00.711781
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:03.218773
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:05.418986
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:07.391205
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:11.696547
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:14.663885
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:16:17.644414
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:26.338079
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:29.070887
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:33.549602
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:35.719162
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:38.539778
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:40.942193
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:43.199073
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:46.352753
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:48.455447
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock


# Generated at 2024-03-18 05:18:52.129033
# Unit test for function determine_repo_dir
def test_determine_repo_dir():from unittest.mock import patch, MagicMock
