

# Generated at 2024-06-01 17:08:48.207183
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:08:52.831273
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:08:56.919412
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:08:59.551424
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():    # Test case 1: Directory exists and contains cookiecutter.json
    os.makedirs('test_repo', exist_ok=True)
    with open('test_repo/cookiecutter.json', 'w') as f:
        f.write('{}')
    assert repository_has_cookiecutter_json('test_repo') == True
    os.remove('test_repo/cookiecutter.json')
    os.rmdir('test_repo')

    # Test case 2: Directory exists but does not contain cookiecutter.json
    os.makedirs('test_repo', exist_ok=True)
    assert repository_has_cookiecutter_json('test_repo') == False
    os.rmdir('test_repo')

    # Test case 3: Directory does not exist
    assert repository_has_cookiecutter_json('non_existent_repo') == False


# Generated at 2024-06-01 17:09:01.575329
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
    }


# Generated at 2024-06-01 17:09:04.569545
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:09.152393
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:12.451827
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:17.278843
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:20.607534
# Unit test for function repository_has_cookiecutter_json
def test_repository_has_cookiecutter_json():    # Test case 1: Directory exists and contains cookiecutter.json
    os.makedirs('test_repo', exist_ok=True)
    with open('test_repo/cookiecutter.json', 'w') as f:
        f.write('{}')
    assert repository_has_cookiecutter_json('test_repo') == True
    os.remove('test_repo/cookiecutter.json')
    os.rmdir('test_repo')

    # Test case 2: Directory exists but does not contain cookiecutter.json
    os.makedirs('test_repo', exist_ok=True)
    assert repository_has_cookiecutter_json('test_repo') == False
    os.rmdir('test_repo')

    # Test case 3: Directory does not exist
    assert repository_has_cookiecutter_json('non_existent_repo') == False


# Generated at 2024-06-01 17:09:26.019581
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:29.007995
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:32.588625
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
    }

# Generated at 2024-06-01 17:09:35.877450
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:38.653317
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:43.042215
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:45.940247
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:50.218667
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:09:53.397957
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
        'gl': 'https://gitlab.com/{0}.git',
    }

    # Test case 1: Template matches an abbreviation key

# Generated at 2024-06-01 17:09:56.318476
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:04.559753
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
        'gl': 'https://gitlab.com/{0}.git',
    }

    # Test case 1: Template matches an abbreviation key

# Generated at 2024-06-01 17:10:08.125495
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:11.857170
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
    }

# Generated at 2024-06-01 17:10:14.541783
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}.git',
        'gl': 'https://gitlab.com/{0}.git',
    }


# Generated at 2024-06-01 17:10:18.287715
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:21.253435
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:25.241354
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:27.807071
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
    }


# Generated at 2024-06-01 17:10:31.951095
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:35.105120
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
        'gl': 'https://gitlab.com/{0}.git',
    }

    # Test case 1: Template is in abbreviations

# Generated at 2024-06-01 17:10:47.928111
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:52.312052
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:10:55.777403
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:01.144867
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:04.698496
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}.git',
        'gl': 'https://gitlab.com/{0}.git',
    }

    # Test case 1: Template matches an abbreviation directly

# Generated at 2024-06-01 17:11:07.368197
# Unit test for function expand_abbreviations
def test_expand_abbreviations():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
        'gl': 'https://gitlab.com/{0}.git',
    }

    # Test case 1: Template matches an abbreviation key

# Generated at 2024-06-01 17:11:10.673847
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:13.523731
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:18.352699
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:22.140597
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:11:57.965035
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:02.531637
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:06.429727
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:08.460413
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    template = "https://github.com/audreyr/cookiecutter-pypackage.git"

# Generated at 2024-06-01 17:12:12.574216
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:15.950962
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:21.266912
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:24.637992
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:27.980452
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:12:31.345163
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:15.384464
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:18.734510
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:23.289341
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    abbreviations = {
        'gh': 'https://github.com/{0}.git',
        'bb': 'https://bitbucket.org/{0}',
    }

# Generated at 2024-06-01 17:13:26.640736
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:30.174787
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:33.873636
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:36.439336
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    template = "https://github.com/audreyr/cookiecutter-pypackage.git"

# Generated at 2024-06-01 17:13:39.613976
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:42.543165
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:13:45.624132
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:06.660380
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:11.069926
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:16.040651
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:19.716454
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:22.131509
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    template = "https://github.com/audreyr/cookiecutter-pypackage.git"

# Generated at 2024-06-01 17:15:24.794087
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:27.902357
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:31.043028
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:33.983152
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:15:38.920657
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:14.426666
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    abbreviations = {
        "gh": "https://github.com/{0}.git",
        "bb": "https://bitbucket.org/{0}",
    }

# Generated at 2024-06-01 17:18:17.397818
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:20.733243
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:24.084605
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:28.160516
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:31.388239
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:35.340487
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:38.856041
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile

# Generated at 2024-06-01 17:18:41.793167
# Unit test for function determine_repo_dir
def test_determine_repo_dir():    import tempfile