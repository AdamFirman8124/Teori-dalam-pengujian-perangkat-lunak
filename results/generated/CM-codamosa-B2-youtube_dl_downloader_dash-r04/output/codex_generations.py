

# Generated at 2026-11-02 19:09:06.464734
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    '''DashSegmentsFD(ydl)'''
    from youtube_dl.downloader.dashsegments import DashSegmentsFD
    ydl = None
    fd = DashSegmentsFD(ydl)
    assert fd.ydl is None
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-11-02 19:14:17.813189
# Unit test for method real_download of class DashSegmentsFD