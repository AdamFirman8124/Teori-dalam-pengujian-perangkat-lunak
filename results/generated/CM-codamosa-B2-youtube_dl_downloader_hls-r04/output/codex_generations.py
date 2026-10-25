

# Generated at 2026-10-24 11:27:23.348660
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:27:25.874801
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:27:28.438096
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:27:30.957639
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:27:33.374282
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:27:35.799607
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:27:38.355970
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:40.775898
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:43.202138
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:45.609462
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:48.027458
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:50.461033
# Unit test for constructor of class HlsFD

# Generated at 2026-10-24 11:27:52.878803
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:27:55.300511
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:27:57.721550
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:28:00.137824
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:28:02.554921
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:28:04.973834
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:28:07.397092
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:28:34.433714
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:28:58.803372
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:01.226611
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:03.643676
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:06.060595
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:08.589131
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:29:31.242687
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:29:36.465463
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXTINF:10.0,\nsegment.ts\n#EXT-X-ENDLIST\n'

# Generated at 2026-10-24 11:29:46.529224
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    basic_manifest = '\n'.join((
        '#EXTM3U',
        '#EXT-X-TARGETDURATION:10',
        '#EXTINF:10,',
        'segment.ts',
        '#EXT-X-ENDLIST',
    ))

    try:
        # Basic VOD playlists are supported.
        can_decrypt_frag = False
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts', {})

        # Live streams and playlists with initialization maps are unsupported.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s', {})

        # Encryption methods other than NONE and AES-128 are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            'segment.ts',
            {})

        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            'segment.ts'
        )

        # AES-128 requires the optional Crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            aes_manifest + '\n#EXT-X-BYTERANGE:1000@0', {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 11:29:49.045421
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:51.465313
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:54.027715
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:56.443670
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:29:58.860692
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:01.281006
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:03.701188
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:06.119596
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:08.535788
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:10.953271
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:13.370801
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:15.786907
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:18.206179
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:20.622692
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:23.041904
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:25.460331
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:27.880456
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:30.326964
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:32.714078
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:35.131453
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:37.547830
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:39.964369
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:42.381395
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:44.799586
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:47.215760
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:49.632572
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:52.049453
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:30:54.465870
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:56.881453
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:30:59.297022
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:31:01.712516
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:31:04.137533
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:31:06.550190
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:31:08.968237
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:31:11.387067
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:31:13.807291
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:31:41.294374
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class FakeResponse(object):
        def geturl(self):
            # Verify that relative fragment URLs use the redirected manifest URL.
            return 'https://cdn.example.test/media/index.m3u8'

        def read(self):
            return manifest.encode('utf-8')

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            return FakeResponse()


# Generated at 2026-10-24 11:32:09.740396
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:12.156072
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:14.578052
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:16.995109
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:19.412348
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:21.828825
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:24.243009
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:26.660933
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:29.077597
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:31.496676
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:33.914767
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:36.329481
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:38.748643
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:41.164311
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:43.580166
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:32:45.996959
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:48.416184
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:50.830077
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:32:53.483184
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:33:07.007837
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from youtube_dl.downloader.hls import HlsFD

# Generated at 2026-10-24 11:33:47.020815
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:33:49.546237
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:33:51.958314
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:33:54.373702
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:33:57.079035
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:34:13.663978
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from youtube_dl.downloader.hls import HlsFD

# Generated at 2026-10-24 11:34:48.563120
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:34:50.981319
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:34:53.537378
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:34:55.953136
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:34:58.368733
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:35:00.787067
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:35:03.204107
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:05.621242
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:08.037142
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:29.192339
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:35:45.776129
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from youtube_dl.downloader.hls import HlsFD

# Generated at 2026-10-24 11:35:48.197720
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:50.614731
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:53.032935
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:55.449676
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:35:57.870010
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:00.285954
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:02.704058
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:05.123373
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:07.541655
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:09.960985
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:12.372363
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:14.790960
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:17.203750
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:19.621754
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:22.055606
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:24.470490
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:26.887476
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:29.304737
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:31.723332
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:34.139100
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:36.555367
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:38.971847
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:41.389891
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:43.810023
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:46.227560
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:48.644531
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:51.062640
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:36:53.476865
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:55.895735
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:36:58.315998
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:37:00.732588
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:03.152541
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:05.570741
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:07.988750
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:37:10.411886
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:37:12.831106
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 11:37:15.248253
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:17.669274
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:20.091193
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:22.513204
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:24.930992
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 11:37:27.352288
# Unit test for method real_download of class HlsFD