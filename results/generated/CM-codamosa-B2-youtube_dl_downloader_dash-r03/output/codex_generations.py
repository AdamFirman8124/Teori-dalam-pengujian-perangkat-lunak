

# Generated at 2026-10-24 15:26:58.726989
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:01.142323
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:03.556876
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:05.970762
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:08.384967
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:10.797690
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:13.212998
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:15.623931
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:18.036813
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:20.449306
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:22.861798
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:25.279635
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:27:27.687042
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:30.261598
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:33.043608
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:34.477127
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:37.232779
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:39.994669
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:41.305885
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

# Generated at 2026-10-24 15:27:42.676780
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:45.381161
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:48.184389
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:49.533114
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:52.098745
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:54.695329
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:57.110612
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:27:59.522056
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:02.088068
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:04.497764
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:07.070524
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:09.486476
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:11.897278
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:14.309578
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:16.721738
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:19.136234
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:21.549031
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:23.960983
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:26.373773
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:28.786391
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:31.198007
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:33.613882
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:36.026249
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:38.440215
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:40.853127
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:43.264943
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:45.676886
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:48.090531
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:50.502377
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:52.915517
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:28:55.329331
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:28:57.742118
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:00.156965
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:02.570436
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:04.982310
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:07.395577
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:09.808729
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:12.406436
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:15.241096
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:16.561566
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:20.678867
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:23.535653
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:24.892228
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:27.577176
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:30.269185
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:31.742113
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:34.374197
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:36.787777
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:29:39.202203
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:41.636653
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:44.029199
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:46.440501
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:48.859409
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:51.272186
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:53.688700
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:56.100181
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:29:58.511254
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:00.927390
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:03.498006
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:05.912187
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:08.325006
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:10.738714
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:13.165948
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:15.577977
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:17.990710
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:20.404600
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:22.816989
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:25.231870
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:27.643219
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:30.056319
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:32.474073
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:35.201846
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:30:36.612804
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:39.514950
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:42.353226
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:43.690944
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:46.412634
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:49.139161
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:50.573192
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:53.322206
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:56.012507
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:30:57.327791
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:00.082364
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:02.849041
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:04.382708
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:07.037833
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:09.452877
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:11.951838
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:14.364544
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:16.779324
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:19.192503
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:21.807373
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:24.222056
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:26.642603
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:29.060993
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:31.475749
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:33.889667
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:36.299344
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:38.714414
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:41.128923
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:43.544843
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:45.958001
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:48.372328
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:50.785002
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:53.199247
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:31:55.612164
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:31:58.025457
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:00.438329
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:02.851955
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:05.264783
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:07.677627
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:10.091720
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:12.505886
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:14.918912
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:18.312485
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:20.726478
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:23.143033
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:25.558322
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:27.970055
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:30.416600
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:32.797008
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:35.207946
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:37.620537
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:40.033800
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:42.446519
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:44.858956
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:47.272434
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:49.687052
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:52.099467
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:32:54.512725
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:56.925484
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:32:59.337995
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:01.750099
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:04.167214
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:06.591800
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:09.003442
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:11.416612
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:13.831570
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:16.244493
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:18.657433
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:21.069934
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:23.482641
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:33:25.896450
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:33:28.308909
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:33:33.947677
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:39.228283
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:41.979866
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:44.857272
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:33:53.916694
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:34:09.436605
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:34:50.708998
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:34:53.122854
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:03.595982
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:06.460138
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:11.318904
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:14.242650
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:17.222861
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:35:18.656598
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:35:41.082256
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:35:51.404418
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:35:54.907045
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:35:58.113157
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:36:09.468460
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:36:12.893234
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 15:36:14.463783
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:37:08.534047
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:37:15.496542
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 15:37:18.332875
# Unit test for method real_download of class DashSegmentsFD