

# Generated at 2026-10-24 15:09:23.925729
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:09:54.101668
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:09:56.516064
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:09:58.929035
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:01.342513
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:03.758309
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:06.170326
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:08.583773
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:10.997327
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:13.410522
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:15.825184
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:18.243014
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:20.652541
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:23.067274
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:25.483573
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:27.894792
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:30.308366
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:32.722537
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:35.137285
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:37.551274
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:39.963203
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:42.376644
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:44.789875
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:47.204681
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:49.617301
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:52.030957
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:54.443943
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:10:56.857622
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:10:59.271409
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:01.685150
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:04.100169
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:06.516138
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:10.406496
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:11.823184
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:14.921279
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:17.980756
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:27.568817
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:11:28.884708
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:11:30.197228
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:11:31.507809
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:11:32.816245
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:11:35.351745
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:37.764680
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:40.176718
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:42.590672
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:45.113505
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:47.526747
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:49.944168
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:11:52.358994
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:11:54.773421
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:11:57.189218
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:11:59.603957
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:02.157053
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:04.569760
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:06.982417
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:09.394388
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:11.806751
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:14.220344
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:16.634703
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:19.047153
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:21.459229
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:23.873116
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:26.285387
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:28.699024
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:31.112372
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:12:53.017619
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:56.082260
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:12:58.765968
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:00.102724
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:02.607754
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:05.021484
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:07.626817
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:10.041531
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:12.604280
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:15.019092
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:17.437091
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:19.851251
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:22.262390
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:24.679708
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:27.091824
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:29.642856
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:32.054747
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:34.467012
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:36.881392
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:39.291929
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:41.704060
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:44.115858
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:46.530056
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:48.944211
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:13:51.356485
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:53.769124
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:56.181967
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:13:58.594204
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:01.010582
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:03.423343
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:05.838575
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:14:08.255720
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:14:10.671052
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:14:13.084991
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:15.497329
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:17.912297
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:20.323634
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:22.736788
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:25.147038
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:27.556776
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:29.969225
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:32.381738
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:33.753134
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:35.127846
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:36.438362
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:37.749438
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:39.416103
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:40.841680
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:43.578924
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:46.352626
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:47.947394
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:50.629634
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:53.326844
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:54.636007
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:14:57.168489
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:14:59.766376
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:02.183183
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:04.596183
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:07.191906
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:09.747637
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:12.161471
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:14.574889
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:16.987710
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:19.401823
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:21.814488
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:24.228746
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:26.642512
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:29.054535
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:31.467825
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:33.880346
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:36.293261
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:38.707252
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:41.122380
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:43.538574
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:45.952654
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:48.366533
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:50.780681
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:53.192627
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:15:56.349253
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:15:58.976274
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:01.780113
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:03.181534
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:05.986755
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:08.721150
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:10.134551
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:12.866267
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:15.765389
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:17.197784
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:16:18.632041
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:21.396848
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:24.136491
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:25.445562
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:16:26.763164
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:29.464821
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:32.038489
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:34.451869
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:36.863796
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:39.275549
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:41.688974
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:44.101306
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:46.513911
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:48.927083
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:51.343453
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:16:53.757430
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:01.811038
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:04.225226
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:06.637318
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:09.050349
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:11.463065
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:13.876636
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:16.289497
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:18.703995
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:21.120419
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:23.535736
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:17:25.948157
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:17:28.360796
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:17:29.832028
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:17:31.145934
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:17:32.460734
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:35.131144
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:37.871947
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:39.185918
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:17:40.521969
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:43.300221
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:45.994599
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:47.312875
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:49.877124
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:17:52.433747
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:06.038838
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:08.448103
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:10.861992
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:13.275405
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:15.696424
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:18.108252
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:20.517181
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:22.931734
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:25.345467
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:27.758328
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:30.173161
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:32.586521
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:34.999724
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:37.413181
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:39.825237
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:42.238320
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:44.654695
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:47.069996
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:49.484285
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:51.897483
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:54.309649
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:18:56.890310
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:18:59.591910
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:19:02.370630
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:19:03.720028
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = YoutubeDL({'quiet': True, 'skip_download': True})
    fd = DashSegmentsFD(ydl, ydl.params)

    # Constructor wires up dependencies correctly
    assert fd.ydl is ydl
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is ydl.params

    # Default params resolve as expected
    assert fd.params.get('fragment_retries', 0) == 0
    assert fd.params.get('skip_unavailable_fragments', True) is True

    print('test_DashSegmentsFD passed')


if __name__ == '__main__':
    test_DashSegmentsFD()

# Generated at 2026-10-24 15:19:05.034082
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:19:07.774341
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:19:10.679795
# Unit test for method real_download of class DashSegmentsFD