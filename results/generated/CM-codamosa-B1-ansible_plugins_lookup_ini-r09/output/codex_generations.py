

# Generated at 2026-10-24 13:35:39.567605
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser

    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read_string(u"""
[global]
user=admin
host=example.com

[integration]
user=integration_user
""")

    # Existing key in section
    assert lookup.get_value('user', 'global', '', False) == 'admin'

    # Missing key -> returns default
    assert lookup.get_value('missing', 'global', 'fallback', False) == 'fallback'

    # Key exists in another section only
    assert lookup.get_value('user', 'integration', '', False) == 'integration_user'

    # Regexp: match all keys in section
    result = lookup.get_value('.*', 'global', '', True)
    assert sorted(result) == ['admin', 'example.com']

    # Regexp: partial match
    result = lookup.get_value('hos.', 'global', '', True)
    assert result == ['example.com']

    # Regexp with no matches -> empty list
    assert lookup.get_value('nomatch.*', 'global', '', True) == []

# Generated at 2026-10-24 13:35:41.982609
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:35:44.557732
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:35:46.975355
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:35:49.390520
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:35:51.806095
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:35:54.335457
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:35:56.758844
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:35:59.337614
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:36:01.747521
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:36:04.165849
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:36:06.585835
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:36:08.998133
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 13:36:11.414491
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:36:13.833154
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:36:29.737306
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():import configparser

# Generated at 2026-10-24 13:37:46.946470
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:49.479152
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:51.891715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:54.472587
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:56.885711
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:37:59.305040
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:02.183228
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:04.598710
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:07.010691
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:09.635571
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:12.052944
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:14.467335
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:16.880546
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:19.293934
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:21.708291
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:24.125158
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:26.536270
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:28.952302
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:31.367339
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:33.781328
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:36.195392
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:38:38.606687
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:41.020733
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:43.434930
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:45.849715
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:48.263143
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:50.683986
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:53.094598
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:55.508841
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:38:57.922651
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:00.337793
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:02.751964
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:05.166991
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:07.585085
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:09.997673
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:12.410857
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:14.824108
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:17.237080
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:19.650714
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:22.063764
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:24.480705
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:26.890368
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:29.305100
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:31.717142
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:34.132728
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:36.545411
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:38.958443
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:41.371597
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:39:43.786167
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:46.203785
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:48.613557
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:51.062038
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:53.476146
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:55.887775
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:39:58.301531
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:00.715905
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:03.130558
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:05.545080
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:07.959094
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:10.374435
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:12.787475
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:15.202499
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:17.615429
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:20.029264
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:22.444699
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:24.859432
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:27.271130
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:29.687572
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:32.102852
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:34.518251
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:36.929695
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:39.353377
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:41.768047
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:44.178526
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:46.592056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:40:49.005708
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:51.421700
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:53.834384
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:56.251334
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:40:58.663590
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:01.079310
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:03.490196
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:05.907547
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:08.325692
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:10.734919
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:13.149394
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:15.568782
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:17.975296
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:20.390047
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:22.802842
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:25.218207
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:27.629594
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:30.043338
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:32.458677
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:34.872978
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:37.290676
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:39.703222
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:42.114105
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:44.528626
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:46.942659
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:49.356184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:51.769754
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:41:54.184607
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:56.602833
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:41:59.017942
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:01.429228
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:03.843452
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:06.255385
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:08.667161
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:11.081568
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:13.496598
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:42:15.909328
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:18.323765
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:20.737965
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:23.151727
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:25.565299
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:42:58.536200
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:00.945943
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:03.360240
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:05.776035
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:08.186811
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:10.600948
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:13.016617
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:15.430759
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:17.846371
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:20.260438
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:22.674296
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:25.244436
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:27.658398
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:43:30.070691
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:32.487242
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:34.899714
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:37.313270
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:39.728588
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:42.143333
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:44.557866
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:46.971987
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:49.384176
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:51.798673
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:54.212335
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:56.629708
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:43:59.041473
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:01.456604
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:03.871452
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:06.284602
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:08.698944
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:11.113142
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:14.567533
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:16.977932
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:19.391690
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:21.804629
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:24.218920
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:26.634183
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:29.046695
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:31.459942
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:33.874933
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:44:36.288278
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:38.702825
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:41.116486
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:43.533581
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:45.953533
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:48.374958
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:50.790617
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:53.211799
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:55.626814
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:44:58.041638
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:00.459235
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:02.874915
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 13:45:05.288975
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:07.703323
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:10.119391
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:12.536307
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:14.954863
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:17.372665
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:19.787428
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:22.215130
# Unit test for method get_value of class LookupModule

# Generated at 2026-10-24 13:45:24.618931
# Unit test for method get_value of class LookupModule