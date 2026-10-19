

# Generated at 2024-03-18 09:35:48.967832
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:35:53.602199
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Queen'),
        mock.call('[fromtitle] parsed title: Bohemian Rhapsody')
    ])


# Generated at 2024-03-18 09:36:04.553755
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Queen'),
        mock.call('[fromtitle] parsed title: Bohemian Rhapsody')
    ])


# Generated at 2024-03-18 09:36:14.269930
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():    # Mock downloader object
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases
    test_cases = [
        ('%(title)s - %(artist)s', 'Awesome Song - Great Artist'),
        ('%(series)s S%(season_number)02dE%(episode_number)02d - %(episode)s', 'ShowName S03E05 - The Episode Title'),
        ('%(title)s', 'SingleTitle'),
        ('Just a static string', 'Just a static string'),
        ('%(title)s_%(id)s.%(ext)s', 'VideoTitle_12345.mp4')
    ]

    for titleformat, title in test_cases:
        pp = MetadataFromTitlePP(MockDownloader(), titleformat)
        assert pp._titleformat == titleformat, "Title format is not set correctly"

# Generated at 2024-03-18 09:36:19.766377
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:36:24.208186
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:36:30.149950
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:36:36.729146
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    
    # Test successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info_dict)
    assert info_dict['artist'] == 'Queen'
    assert info_dict['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test unsuccessful extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    assert 'artist' not in info_dict
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%(artist)s - %(title)s"'
    )


# Generated at 2024-03-18 09:36:41.242447
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:36:45.644581
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:36:54.308097
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    updated_info = pp.run(info.copy())[1]

    # Assert
    assert updated_info['artist'] == 'Coldplay'
    assert updated_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:36:59.642444
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:37:05.904332
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')

# Generated at 2024-03-18 09:37:12.975759
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')

# Generated at 2024-03-18 09:37:18.317382
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:37:25.197197
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:37:31.882695
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:37:39.509988
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed artist: Queen')
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed title: Bohemian Rhapsody')


# Generated at 2024-03-18 09:37:46.732131
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():    # Test cases for the format_to_regex method
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert pp.format_to_regex('%(artist)s - %(title)s') == r'(?P<artist>.+)\ \-\ (?P<title>.+)'
    assert pp.format_to_regex('%(series)s S%(season_number)02dE%(episode_number)02d - %(episode)s') == \
        r'(?P<series>.+)\ S(?P<season_number>\d\d)E(?P<episode_number>\d\d)\ \-\ (?P<episode>.+)'
    assert pp.format_to_regex('Season %(season_number)d - Episode %(episode_number)d: %(episode)s') == \
        r'Season\ (?P<season_number>\d+)\ \-\ Episode\ (?P<episode_number>\d+):\ (?P<episode>.+)'
    assert pp.format_to_regex('%(title)s')

# Generated at 2024-03-18 09:37:53.402744
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():    # Test cases for the format_to_regex method
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert pp.format_to_regex('%(artist)s - %(title)s') == r'(?P<artist>.+)\ \-\ (?P<title>.+)'
    assert pp.format_to_regex('%(series)s S%(season_number)02dE%(episode_number)02d - %(episode)s') == \
        r'(?P<series>.+) S(?P<season_number>\d\d)E(?P<episode_number>\d\d) - (?P<episode>.+)'
    assert pp.format_to_regex('Season %(season_number)d - %(episode_number)d - %(title)s') == \
        r'Season\ (?P<season_number>\d)\ \-\ (?P<episode_number>\d)\ \-\ (?P<title>.+)'

# Generated at 2024-03-18 09:38:02.095085
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:38:09.969238
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info_dict)
    assert info_dict['artist'] == 'Queen'
    assert info_dict['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test unsuccessful extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    assert 'artist' not in info_dict
    assert info_dict['title'] == 'Unknown Format'
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format
    )


# Generated at 2024-03-18 09:38:16.470395
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    
    # Test successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info_dict)
    assert info_dict['artist'] == 'Queen'
    assert info_dict['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test unsuccessful extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    assert 'artist' not in info_dict
    assert info_dict['title'] == 'Unknown Format'
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format
    )


# Generated at 2024-03-18 09:38:21.996520
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:38:27.355484
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:38:32.445447
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Queen'),
        mock.call('[fromtitle] parsed title: Bohemian Rhapsody')
    ])


# Generated at 2024-03-18 09:38:39.502347
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:38:46.876911
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed artist: Queen')
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed title: Bohemian Rhapsody')
    assert info_dict['artist'] == 'Queen'
    assert info_dict['title'] == 'Bohemian Rhapsody'

    # Test failed extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format)
    assert 'artist' not in info_dict
    assert info

# Generated at 2024-03-18 09:38:52.793071
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:38:58.998153
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:39:14.593121
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:39:21.236503
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:39:29.312870
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info)
    assert info['artist'] == 'Queen'
    assert info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test case: Incorrect title format
    info = {'title': 'Unknown Title Format'}
    result, info = pp.run(info)
    assert result == []
    assert 'artist' not in info
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format
    )

    # Test case: Partially matching title

# Generated at 2024-03-18 09:39:35.890375
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info)
    assert info['artist'] == 'Queen'
    assert info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test case: Incorrect title format
    info = {'title': 'Unknown Title Format'}
    result, info = pp.run(info)
    assert result == []
    assert 'artist' not in info
    assert 'title' in info  # Original title should remain unchanged

# Generated at 2024-03-18 09:39:41.076142
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:39:48.603008
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:39:53.468950
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:39:58.735188
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:40:05.102447
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info)
    assert info['artist'] == 'Queen'
    assert info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test case: Incorrect title format
    info = {'title': 'Unknown Title Format'}
    result, info = pp.run(info)
    assert result == []
    assert 'artist' not in info
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format
    )

    # Test case: Partially matching title

# Generated at 2024-03-18 09:40:09.110531
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:40:31.044876
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:40:35.897740
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Queen'),
        mock.call('[fromtitle] parsed title: Bohemian Rhapsody')
    ])


# Generated at 2024-03-18 09:40:43.972508
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: successful extraction
    info_dict = {'title': 'Coldplay - Yellow'}
    expected_info = {'title': 'Yellow', 'artist': 'Coldplay'}
    pp.run(info_dict)
    assert info_dict == expected_info, "Metadata extraction from title failed"

    # Test case: unsuccessful extraction (no match)
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    assert 'artist' not in info_dict, "Metadata should not be extracted for unmatched format"
    assert 'title' in info_dict, "Original title should remain unchanged"

    # Test case: partial extraction (partial match)
    title_format = '%(artist)s - %(title)s - %(album)s'

# Generated at 2024-03-18 09:40:52.719722
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock objects and values
    mock_downloader = MagicMock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(mock_downloader, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Expected results
    expected_info = {
        'title': 'Yellow',
        'artist': 'Coldplay',
        'webpage_url': 'https://example.com/video'
    }

    # Run the method
    pp.run(info)

    # Assertions
    mock_downloader.to_screen.assert_any_call('[fromtitle] parsed artist: Coldplay')
    mock_downloader.to_screen.assert_any_call('[fromtitle] parsed title: Yellow')
    assert info['title'] == expected_info['title']
    assert info['artist'] == expected_info['artist']


# Generated at 2024-03-18 09:41:01.638525
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test successful extraction
    info_dict = {'title': 'Coldplay - Yellow'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed artist: Coldplay')
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed title: Yellow')
    assert info_dict['artist'] == 'Coldplay'
    assert info_dict['title'] == 'Yellow'

    # Test failed extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%(artist)s - %(title)s"'
    )
    assert 'artist' not in info_dict
    assert 'title' == 'Unknown Format'


# Generated at 2024-03-18 09:41:06.906135
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:41:14.601994
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:41:20.332344
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:41:27.689426
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:41:33.611123
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:42:13.963625
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:42:21.242854
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:42:28.555473
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    expected_info = {'title': 'Bohemian Rhapsody', 'artist': 'Queen'}
    pp.run(info_dict)
    assert info_dict['title'] == expected_info['title']
    assert info_dict['artist'] == expected_info['artist']
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test case: Incorrect title format
    info_dict = {'title': 'Unknown Title Format'}
    result, info_dict = pp.run(info_dict)
    assert result == []
    assert 'artist' not in info_dict
    assert 'title' in info_dict
    downloader

# Generated at 2024-03-18 09:42:42.817328
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:42:48.206068
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2024-03-18 09:42:54.067113
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:42:59.439220
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:43:07.669003
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])


# Generated at 2024-03-18 09:43:14.494584
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info = {'title': 'Coldplay - Yellow'}
    expected_info = {'title': 'Yellow', 'artist': 'Coldplay'}
    pp.run(info)
    assert info == expected_info, "Expected info dictionary to be updated with title and artist"

    # Test case: Incorrect title format
    info = {'title': 'Just a single string'}
    pp.run(info)
    assert 'artist' not in info, "Expected info dictionary not to have an 'artist' key"
    assert 'title' in info, "Expected info dictionary to retain the 'title' key"

    # Test case: Empty title
    info = {'title': ''}
    pp.run(info)

# Generated at 2024-03-18 09:43:21.261955
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test cases
    test_cases = [
        {'title': 'Artist Name - Song Title', 'expected': {'artist': 'Artist Name', 'title': 'Song Title'}},
        {'title': 'Another Artist - Another Song Title', 'expected': {'artist': 'Another Artist', 'title': 'Another Song Title'}},
        {'title': 'No delimiter', 'expected': None},
    ]

    for case in test_cases:
        info = {'title': case['title']}
        _, result_info = pp.run(info)

        if case['expected'] is None:
            assert 'artist' not in result_info and 'title' not in result_info, f"Metadata should not be extracted from title: {case['title']}"

# Generated at 2024-03-18 09:44:39.052364
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Correct title format
    info = {'title': 'Coldplay - Yellow'}
    pp.run(info)
    assert info['artist'] == 'Coldplay'
    assert info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Yellow')

    # Test case: Incorrect title format
    info = {'title': 'Unknown Format'}
    pp.run(info)
    assert 'artist' not in info
    assert info['title'] == 'Unknown Format'
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format
    )

    # Test case: Missing title part
    info = {'title': 'Adele - '}


# Generated at 2024-03-18 09:44:49.815369
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test cases
    test_cases = [
        {'title': 'Artist Name - Song Title', 'expected': {'artist': 'Artist Name', 'title': 'Song Title'}},
        {'title': 'Another Artist - Another Song Title', 'expected': {'artist': 'Another Artist', 'title': 'Another Song Title'}},
        {'title': 'No delimiter', 'expected': None},
    ]

    for case in test_cases:
        info = {'title': case['title']}
        expected = case['expected']
        output, info = pp.run(info)

        if expected is None:
            assert not output and 'artist' not in info and 'title' not in info, "Failed to ignore invalid title format"

# Generated at 2024-03-18 09:44:56.306873
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Queen - Bohemian Rhapsody'}

    # Execute
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Queen'
    assert result_info['title'] == 'Bohemian Rhapsody'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Queen'),
        mock.call('[fromtitle] parsed title: Bohemian Rhapsody')
    ])


# Generated at 2024-03-18 09:45:02.265312
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:45:09.110238
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed artist: Queen')
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed title: Bohemian Rhapsody')
    assert info_dict['artist'] == 'Queen'
    assert info_dict['title'] == 'Bohemian Rhapsody'

    # Test case: Unsuccessful extraction
    info_dict = {'title': 'Unknown Format'}
    pp.run(info_dict)
    downloader_mock.to_screen.assert_called_with(
        '[fromtitle] Could not interpret title of video as "%s"' % title_format)
    assert 'artist' not in info

# Generated at 2024-03-18 09:45:21.774054
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    title_format = '%(artist)s - %(title)s'
    downloader_mock = mock.Mock()
    pp = MetadataFromTitlePP(downloader_mock, title_format)

    # Test case: Successful extraction
    info_dict = {'title': 'Queen - Bohemian Rhapsody'}
    expected_info = {'title': 'Bohemian Rhapsody', 'artist': 'Queen'}
    pp.run(info_dict)
    assert info_dict['title'] == expected_info['title']
    assert info_dict['artist'] == expected_info['artist']
    downloader_mock.to_screen.assert_called_with('[fromtitle] parsed title: Bohemian Rhapsody')

    # Test case: Unsuccessful extraction
    info_dict = {'title': 'Unknown Format'}
    result, info_dict = pp.run(info_dict)
    assert result == []
    assert info_dict['title'] == 'Unknown Format'

# Generated at 2024-03-18 09:45:27.423833
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:45:33.766488
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Mock downloader object with a to_screen method
    class MockDownloader:
        def to_screen(self, message):
            print(message)

    # Test cases

# Generated at 2024-03-18 09:45:38.614094
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():    # Setup
    downloader_mock = mock.Mock()
    title_format = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader_mock, title_format)
    info = {'title': 'Coldplay - Yellow'}

    # Run
    _, result_info = pp.run(info)

    # Assert
    assert result_info['artist'] == 'Coldplay'
    assert result_info['title'] == 'Yellow'
    downloader_mock.to_screen.assert_has_calls([
        mock.call('[fromtitle] parsed artist: Coldplay'),
        mock.call('[fromtitle] parsed title: Yellow')
    ])
