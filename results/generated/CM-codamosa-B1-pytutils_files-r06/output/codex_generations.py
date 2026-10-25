

# Generated at 2026-10-24 11:43:05.794687
# Unit test for function islurp

# Generated at 2026-10-24 11:43:08.213166
# Unit test for function islurp

# Generated at 2026-10-24 11:43:10.634780
# Unit test for function islurp

# Generated at 2026-10-24 11:43:13.053835
# Unit test for function burp

# Generated at 2026-10-24 11:43:15.471717
# Unit test for function burp

# Generated at 2026-10-24 11:43:17.893087
# Unit test for function burp

# Generated at 2026-10-24 11:43:20.311572
# Unit test for function islurp

# Generated at 2026-10-24 11:43:22.731357
# Unit test for function islurp

# Generated at 2026-10-24 11:43:25.148782
# Unit test for function islurp

# Generated at 2026-10-24 11:43:27.565475
# Unit test for function burp

# Generated at 2026-10-24 11:43:29.981199
# Unit test for function burp

# Generated at 2026-10-24 11:43:32.400204
# Unit test for function burp

# Generated at 2026-10-24 11:43:34.831218
# Unit test for function burp

# Generated at 2026-10-24 11:43:37.248227
# Unit test for function burp

# Generated at 2026-10-24 11:43:39.665257
# Unit test for function burp

# Generated at 2026-10-24 11:43:42.083492
# Unit test for function islurp

# Generated at 2026-10-24 11:43:44.501409
# Unit test for function islurp

# Generated at 2026-10-24 11:43:46.919087
# Unit test for function islurp

# Generated at 2026-10-24 11:43:49.335923
# Unit test for function burp

# Generated at 2026-10-24 11:43:51.755665
# Unit test for function burp

# Generated at 2026-10-24 11:43:54.172478
# Unit test for function burp

# Generated at 2026-10-24 11:43:56.590068
# Unit test for function islurp

# Generated at 2026-10-24 11:43:59.005831
# Unit test for function islurp

# Generated at 2026-10-24 11:44:01.422460
# Unit test for function islurp

# Generated at 2026-10-24 11:44:03.836872
# Unit test for function burp

# Generated at 2026-10-24 11:44:10.283007
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-24 11:44:30.115084
# Unit test for function islurp

# Generated at 2026-10-24 11:44:45.985966
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 11:44:48.517691
# Unit test for function burp

# Generated at 2026-10-24 11:44:55.100097
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-24 11:45:13.123596
# Unit test for function burp
def test_burp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        # Write, then overwrite
        path = os.path.join(tmp, "out.txt")
        module_0.burp(path, "hello")
        with open(path) as fh:
            assert fh.read() == "hello"
        module_0.burp(path, "bye")
        with open(path) as fh:
            assert fh.read() == "bye"

        # Append
        module_0.burp(path, "!", mode="a")
        with open(path) as fh:
            assert fh.read() == "bye!"

        # Stdout via "-"
        old_stdout = sys.stdout

# Generated at 2026-10-24 11:45:15.546032
# Unit test for function islurp

# Generated at 2026-10-24 11:45:18.149454
# Unit test for function islurp

# Generated at 2026-10-24 11:45:20.568596
# Unit test for function islurp

# Generated at 2026-10-24 11:45:22.986345
# Unit test for function islurp

# Generated at 2026-10-24 11:45:25.400630
# Unit test for function islurp

# Generated at 2026-10-24 11:45:27.818383
# Unit test for function islurp

# Generated at 2026-10-24 11:45:30.232665
# Unit test for function burp

# Generated at 2026-10-24 11:45:32.650423
# Unit test for function burp

# Generated at 2026-10-24 11:45:35.068966
# Unit test for function burp

# Generated at 2026-10-24 11:45:37.486040
# Unit test for function islurp

# Generated at 2026-10-24 11:45:39.902942
# Unit test for function islurp

# Generated at 2026-10-24 11:45:42.320569
# Unit test for function islurp

# Generated at 2026-10-24 11:45:44.740759
# Unit test for function islurp

# Generated at 2026-10-24 11:45:47.158916
# Unit test for function islurp

# Generated at 2026-10-24 11:45:49.575081
# Unit test for function islurp

# Generated at 2026-10-24 11:45:51.991804
# Unit test for function islurp

# Generated at 2026-10-24 11:45:54.410752
# Unit test for function islurp

# Generated at 2026-10-24 11:45:56.826279
# Unit test for function islurp

# Generated at 2026-10-24 11:45:59.244238
# Unit test for function islurp

# Generated at 2026-10-24 11:46:01.662768
# Unit test for function islurp

# Generated at 2026-10-24 11:46:04.079084
# Unit test for function islurp

# Generated at 2026-10-24 11:46:06.495733
# Unit test for function burp

# Generated at 2026-10-24 11:46:08.914278
# Unit test for function burp

# Generated at 2026-10-24 11:46:11.332612
# Unit test for function burp

# Generated at 2026-10-24 11:46:13.750253
# Unit test for function islurp

# Generated at 2026-10-24 11:46:16.167602
# Unit test for function islurp

# Generated at 2026-10-24 11:46:18.588535
# Unit test for function islurp

# Generated at 2026-10-24 11:46:21.000250
# Unit test for function islurp

# Generated at 2026-10-24 11:46:23.415508
# Unit test for function islurp

# Generated at 2026-10-24 11:46:25.834545
# Unit test for function islurp

# Generated at 2026-10-24 11:46:28.251365
# Unit test for function islurp

# Generated at 2026-10-24 11:46:30.668747
# Unit test for function islurp

# Generated at 2026-10-24 11:46:33.084290
# Unit test for function islurp

# Generated at 2026-10-24 11:46:35.502487
# Unit test for function islurp

# Generated at 2026-10-24 11:46:37.916770
# Unit test for function islurp

# Generated at 2026-10-24 11:46:40.335246
# Unit test for function islurp

# Generated at 2026-10-24 11:46:42.752141
# Unit test for function islurp

# Generated at 2026-10-24 11:46:45.169521
# Unit test for function islurp

# Generated at 2026-10-24 11:46:47.583720
# Unit test for function islurp

# Generated at 2026-10-24 11:46:50.001007
# Unit test for function islurp

# Generated at 2026-10-24 11:46:52.417430
# Unit test for function islurp

# Generated at 2026-10-24 11:46:54.834145
# Unit test for function islurp

# Generated at 2026-10-24 11:46:57.250984
# Unit test for function islurp

# Generated at 2026-10-24 11:46:59.665955
# Unit test for function islurp

# Generated at 2026-10-24 11:47:02.080539
# Unit test for function islurp

# Generated at 2026-10-24 11:47:04.500269
# Unit test for function islurp

# Generated at 2026-10-24 11:47:06.916172
# Unit test for function islurp

# Generated at 2026-10-24 11:47:09.336082
# Unit test for function islurp

# Generated at 2026-10-24 11:47:11.753580
# Unit test for function islurp

# Generated at 2026-10-24 11:47:14.172628
# Unit test for function islurp

# Generated at 2026-10-24 11:47:16.590670
# Unit test for function islurp

# Generated at 2026-10-24 11:47:19.007723
# Unit test for function burp

# Generated at 2026-10-24 11:47:21.426442
# Unit test for function burp

# Generated at 2026-10-24 11:47:24.084434
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-24 11:47:26.853030
# Unit test for function islurp

# Generated at 2026-10-24 11:47:43.502700
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 11:47:44.843968
# Unit test for function burp
def test_burp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        # Write, then overwrite
        path = os.path.join(tmp, "out.txt")
        module_0.burp(path, "hello")
        with open(path) as fh:
            assert fh.read() == "hello"
        module_0.burp(path, "bye")
        with open(path) as fh:
            assert fh.read() == "bye"

        # Append
        module_0.burp(path, "!", mode="a")
        with open(path) as fh:
            assert fh.read() == "bye!"

        # Stdout via "-"
        old_stdout = sys.stdout

# Generated at 2026-10-24 11:47:47.491414
# Unit test for function islurp

# Generated at 2026-10-24 11:47:58.805639
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:48:01.473063
# Unit test for function islurp

# Generated at 2026-10-24 11:48:03.888509
# Unit test for function islurp

# Generated at 2026-10-24 11:48:06.305810
# Unit test for function islurp

# Generated at 2026-10-24 11:48:08.722684
# Unit test for function islurp

# Generated at 2026-10-24 11:48:11.137828
# Unit test for function islurp

# Generated at 2026-10-24 11:48:13.556501
# Unit test for function islurp

# Generated at 2026-10-24 11:48:15.971213
# Unit test for function islurp

# Generated at 2026-10-24 11:48:18.389429
# Unit test for function islurp

# Generated at 2026-10-24 11:48:20.803714
# Unit test for function islurp

# Generated at 2026-10-24 11:48:23.220796
# Unit test for function burp

# Generated at 2026-10-24 11:48:25.636745
# Unit test for function burp

# Generated at 2026-10-24 11:48:28.060820
# Unit test for function burp

# Generated at 2026-10-24 11:48:30.502851
# Unit test for function burp

# Generated at 2026-10-24 11:48:32.900057
# Unit test for function burp

# Generated at 2026-10-24 11:48:35.324086
# Unit test for function burp

# Generated at 2026-10-24 11:48:37.747368
# Unit test for function islurp

# Generated at 2026-10-24 11:48:40.166836
# Unit test for function islurp

# Generated at 2026-10-24 11:48:42.587281
# Unit test for function islurp

# Generated at 2026-10-24 11:48:45.010342
# Unit test for function islurp

# Generated at 2026-10-24 11:48:59.940550
# Unit test for function islurp
def test_islurp():import tempfile

# Generated at 2026-10-24 11:49:02.581659
# Unit test for function islurp

# Generated at 2026-10-24 11:49:04.981197
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:07.711133
# Unit test for function islurp

# Generated at 2026-10-24 11:49:09.073474
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:10.408269
# Unit test for function burp
def test_burp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        # Write, then overwrite
        path = os.path.join(tmp, "out.txt")
        module_0.burp(path, "hello")
        with open(path) as fh:
            assert fh.read() == "hello"
        module_0.burp(path, "bye")
        with open(path) as fh:
            assert fh.read() == "bye"

        # Append
        module_0.burp(path, "!", mode="a")
        with open(path) as fh:
            assert fh.read() == "bye!"

        # Stdout via "-"
        old_stdout = sys.stdout

# Generated at 2026-10-24 11:49:13.171354
# Unit test for function islurp

# Generated at 2026-10-24 11:49:14.485083
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:17.124721
# Unit test for function islurp

# Generated at 2026-10-24 11:49:19.789901
# Unit test for function islurp

# Generated at 2026-10-24 11:49:22.207543
# Unit test for function islurp

# Generated at 2026-10-24 11:49:24.773713
# Unit test for function islurp

# Generated at 2026-10-24 11:49:27.322753
# Unit test for function islurp

# Generated at 2026-10-24 11:49:29.740158
# Unit test for function islurp

# Generated at 2026-10-24 11:49:32.449245
# Unit test for function islurp

# Generated at 2026-10-24 11:49:33.758662
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:36.410724
# Unit test for function islurp

# Generated at 2026-10-24 11:49:37.792740
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:40.559458
# Unit test for function islurp

# Generated at 2026-10-24 11:49:42.030713
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:44.836265
# Unit test for function islurp

# Generated at 2026-10-24 11:49:46.335762
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:48.977775
# Unit test for function islurp

# Generated at 2026-10-24 11:49:50.294829
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:53.096028
# Unit test for function islurp

# Generated at 2026-10-24 11:49:54.524734
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:49:55.955271
# Unit test for function burp
def test_burp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        # Write, then overwrite
        path = os.path.join(tmp, "out.txt")
        module_0.burp(path, "hello")
        with open(path) as fh:
            assert fh.read() == "hello"
        module_0.burp(path, "bye")
        with open(path) as fh:
            assert fh.read() == "bye"

        # Append
        module_0.burp(path, "!", mode="a")
        with open(path) as fh:
            assert fh.read() == "bye!"

        # Stdout via "-"
        old_stdout = sys.stdout

# Generated at 2026-10-24 11:49:58.818871
# Unit test for function islurp

# Generated at 2026-10-24 11:50:01.238909
# Unit test for function islurp

# Generated at 2026-10-24 11:50:03.783091
# Unit test for function islurp

# Generated at 2026-10-24 11:50:06.203663
# Unit test for function burp

# Generated at 2026-10-24 11:50:08.624290
# Unit test for function burp

# Generated at 2026-10-24 11:50:11.037695
# Unit test for function burp

# Generated at 2026-10-24 11:50:14.133444
# Unit test for function islurp

# Generated at 2026-10-24 11:50:16.661270
# Unit test for function islurp

# Generated at 2026-10-24 11:50:19.077629
# Unit test for function islurp

# Generated at 2026-10-24 11:50:21.495418
# Unit test for function islurp

# Generated at 2026-10-24 11:50:23.911790
# Unit test for function islurp

# Generated at 2026-10-24 11:50:26.329720
# Unit test for function islurp

# Generated at 2026-10-24 11:50:28.745785
# Unit test for function islurp

# Generated at 2026-10-24 11:50:31.167976
# Unit test for function islurp

# Generated at 2026-10-24 11:50:33.586568
# Unit test for function islurp

# Generated at 2026-10-24 11:50:36.002481
# Unit test for function islurp

# Generated at 2026-10-24 11:50:38.421719
# Unit test for function islurp

# Generated at 2026-10-24 11:50:40.839675
# Unit test for function islurp

# Generated at 2026-10-24 11:50:43.259912
# Unit test for function burp

# Generated at 2026-10-24 11:50:45.677851
# Unit test for function burp

# Generated at 2026-10-24 11:50:48.093559
# Unit test for function burp

# Generated at 2026-10-24 11:50:50.513994
# Unit test for function burp

# Generated at 2026-10-24 11:50:52.930338
# Unit test for function burp

# Generated at 2026-10-24 11:50:55.349868
# Unit test for function burp

# Generated at 2026-10-24 11:50:57.764016
# Unit test for function burp

# Generated at 2026-10-24 11:51:00.184214
# Unit test for function burp

# Generated at 2026-10-24 11:51:06.291582
# Unit test for function burp
def test_burp():import tempfile

# Generated at 2026-10-24 11:51:09.276100
# Unit test for function islurp

# Generated at 2026-10-24 11:51:10.705326
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:51:12.352730
# Unit test for function burp
def test_burp():
    import io
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        # Write, then overwrite
        path = os.path.join(tmp, "out.txt")
        module_0.burp(path, "hello")
        with open(path) as fh:
            assert fh.read() == "hello"
        module_0.burp(path, "bye")
        with open(path) as fh:
            assert fh.read() == "bye"

        # Append
        module_0.burp(path, "!", mode="a")
        with open(path) as fh:
            assert fh.read() == "bye!"

        # Stdout via "-"
        old_stdout = sys.stdout

# Generated at 2026-10-24 11:51:15.416652
# Unit test for function islurp

# Generated at 2026-10-24 11:51:16.732892
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:51:23.097219
# Unit test for function islurp

# Generated at 2026-10-24 11:51:24.419274
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:51:27.076952
# Unit test for function islurp

# Generated at 2026-10-24 11:51:28.524648
# Unit test for function islurp
def test_islurp():import os

# Generated at 2026-10-24 11:51:31.072910
# Unit test for function islurp

# Generated at 2026-10-24 11:51:33.647489
# Unit test for function islurp

# Generated at 2026-10-24 11:51:36.065725
# Unit test for function islurp

# Generated at 2026-10-24 11:51:38.485935
# Unit test for function islurp

# Generated at 2026-10-24 11:51:40.905703
# Unit test for function islurp

# Generated at 2026-10-24 11:51:43.321036
# Unit test for function islurp

# Generated at 2026-10-24 11:51:45.749227
# Unit test for function islurp

# Generated at 2026-10-24 11:51:48.174307
# Unit test for function islurp

# Generated at 2026-10-24 11:51:50.598736
# Unit test for function islurp

# Generated at 2026-10-24 11:51:53.018840
# Unit test for function islurp

# Generated at 2026-10-24 11:51:55.436375
# Unit test for function islurp

# Generated at 2026-10-24 11:51:57.857157
# Unit test for function islurp

# Generated at 2026-10-24 11:52:00.273699
# Unit test for function islurp

# Generated at 2026-10-24 11:52:02.692535
# Unit test for function islurp

# Generated at 2026-10-24 11:52:05.110413
# Unit test for function islurp

# Generated at 2026-10-24 11:52:07.530016
# Unit test for function islurp

# Generated at 2026-10-24 11:52:09.948968
# Unit test for function islurp

# Generated at 2026-10-24 11:52:12.365036
# Unit test for function islurp

# Generated at 2026-10-24 11:52:14.796020
# Unit test for function islurp

# Generated at 2026-10-24 11:52:17.216032
# Unit test for function islurp

# Generated at 2026-10-24 11:52:19.632658
# Unit test for function islurp

# Generated at 2026-10-24 11:52:22.049229
# Unit test for function islurp

# Generated at 2026-10-24 11:52:24.469183
# Unit test for function islurp

# Generated at 2026-10-24 11:52:26.883794
# Unit test for function islurp

# Generated at 2026-10-24 11:52:45.033795
# Unit test for function burp

# Generated at 2026-10-24 11:52:47.449629
# Unit test for function burp

# Generated at 2026-10-24 11:52:49.864127
# Unit test for function burp