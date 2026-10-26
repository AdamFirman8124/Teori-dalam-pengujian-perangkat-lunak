

# Generated at 2026-10-25 06:41:55.200671
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 06:41:57.616113
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:00.030023
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:02.443950
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:04.874867
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:07.314111
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:09.715506
# Unit test for constructor of class DateTimeFactCollector

# Generated at 2026-10-25 06:42:20.769291
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():collector = DateTimeFactCollector()

# Generated at 2026-10-25 06:42:22.179817
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

    before = int(time.time())
    facts_dict = collector.collect()
    after = int(time.time())

    assert list(facts_dict) == ['date_time']
    dt = facts_dict['date_time']

    # every key present, nothing extra, all values are str
    assert set(dt) == EXPECTED_KEYS
    for key, value in dt.items():
        assert isinstance(value, str), '%s is %r, not str' % (key, type(value))

    # epoch/epoch_int are integers within the window the collect() call spanned
    assert dt['epoch'].lstrip('-').isdigit()
    assert dt['epoch_int'].lstrip('-').isdigit()
    epoch = int(dt['epoch_int'])
    assert before - 1 <= epoch <= after + 1
    assert int(dt['epoch']) == epoch

    # local-time fields are derived from that same epoch (no second-boundary flake)
    local = datetime.datetime.fromtimestamp(epoch)
    assert dt['year'] == local.strftime('%Y')
    assert dt['month'] == local.strftime('%m')
    assert dt['day'] == local.strftime('%d')

# Generated at 2026-10-25 06:42:23.591453
# Unit test for constructor of class DateTimeFactCollector
def test_DateTimeFactCollector():
    collector = DateTimeFactCollector()
    assert collector.name == 'date_time'
    assert collector._fact_ids == set()

    before = int(time.time())
    facts_dict = collector.collect()
    after = int(time.time())

    assert list(facts_dict) == ['date_time']
    dt = facts_dict['date_time']

    # every key present, nothing extra, all values are str
    assert set(dt) == EXPECTED_KEYS
    for key, value in dt.items():
        assert isinstance(value, str), '%s is %r, not str' % (key, type(value))

    # epoch/epoch_int are integers within the window the collect() call spanned
    assert dt['epoch'].lstrip('-').isdigit()
    assert dt['epoch_int'].lstrip('-').isdigit()
    epoch = int(dt['epoch_int'])
    assert before - 1 <= epoch <= after + 1
    assert int(dt['epoch']) == epoch

    # local-time fields are derived from that same epoch (no second-boundary flake)
    local = datetime.datetime.fromtimestamp(epoch)
    assert dt['year'] == local.strftime('%Y')
    assert dt['month'] == local.strftime('%m')
    assert dt['day'] == local.strftime('%d')

# Generated at 2026-10-25 06:42:57.672767
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:00.088117
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:02.501221
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:04.919656
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:07.336243
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:09.753143
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:12.168791
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:14.582953
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:17.028662
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:19.410899
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:21.827849
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:39.264576
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:42.127775
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:44.686979
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:47.100198
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:49.511462
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:51.925824
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:54.338859
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:56.754523
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:43:59.168895
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:01.733518
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:04.149798
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:06.566415
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:08.982307
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:11.400571
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:13.815119
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:16.246625
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:18.664370
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:21.077387
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:23.525732
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:25.942538
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:28.356364
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:30.771584
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:33.188974
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:35.602905
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:38.019488
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:40.434931
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:42.848544
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:44:45.265539
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:00.471413
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:03.290891
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:06.059849
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:08.653331
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:11.105414
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:13.497375
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:16.023711
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:18.441416
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:20.853984
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:23.269783
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:25.711231
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:28.490547
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:30.910077
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:33.322760
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:35.738980
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:38.157706
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:40.699153
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:43.119522
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:45.536402
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:47.960662
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:50.373803
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:52.788044
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:55.203679
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:45:58.011805
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:15.836695
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:18.680331
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:21.786750
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:39.693105
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:42.131534
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:44.732897
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:47.144294
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:49.567986
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:51.977455
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:54.390564
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:56.806043
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:46:59.221656
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:17.235723
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:20.144802
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:23.205787
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:25.701119
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:28.328436
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:30.743152
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:33.157909
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:35.799612
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:38.216338
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:40.632487
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:43.334841
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:45.752836
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:48.167187
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:50.581029
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:52.998568
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:55.414422
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:47:57.832646
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:00.247411
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:02.664663
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:05.082780
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:07.497086
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:09.915283
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:12.332353
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:14.747511
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:17.165944
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:19.582846
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:21.997435
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:24.416224
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:26.832446
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:29.249182
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:31.667446
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:34.082023
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:36.495816
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:38.912988
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:41.332166
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:43.745792
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:46.160012
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:48.574055
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:50.987925
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:53.452570
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:55.866625
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:48:58.281389
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:00.703839
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:03.121627
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:05.536925
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:07.951371
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:10.366926
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:12.782406
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:15.196381
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:17.615044
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:20.029725
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:22.445875
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:24.894246
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:27.276212
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:29.692637
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:32.109381
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:34.522313
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:36.937768
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:39.354333
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:41.769182
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:44.184736
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:46.603313
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:49.130874
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:51.448556
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:53.865876
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:56.334451
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:49:58.720639
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:01.134686
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:03.572820
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:05.985137
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:08.402072
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:10.816283
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:13.306300
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:15.697576
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:18.111140
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:22.155331
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:24.568594
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:26.982604
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:29.417942
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:31.833263
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:34.248549
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:36.661798
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:39.079051
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:41.493302
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:43.909302
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:46.328526
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:48.741491
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:51.158908
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:53.571392
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:55.985440
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:50:58.401937
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:00.816927
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:03.231288
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:05.646132
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:08.064194
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:10.478392
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:12.895096
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:15.312266
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:17.728343
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:20.141732
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:22.559738
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:24.977052
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:27.392122
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:29.810942
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:32.224455
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:38.122137
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:40.535102
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:42.952893
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:45.370517
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:47.784515
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:50.200796
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:52.620309
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:55.032273
# Unit test for method collect of class DateTimeFactCollector

# Generated at 2026-10-25 06:51:57.449605
# Unit test for method collect of class DateTimeFactCollector