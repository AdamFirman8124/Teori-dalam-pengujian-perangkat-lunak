

# Generated at 2026-10-25 14:20:03.739095
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Values exactly halfway round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("7.000") == 7

    # Zero and negative values
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-0.0") == 0
    assert module_0.closest_integer("-3.2") == -3
    assert module_0.closest_integer("-3.8") == -4

# Generated at 2026-10-25 14:20:26.882029
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0.0") == 0
    assert module_0.closest_integer("9.9") == 10

# Generated at 2026-10-25 14:20:59.917605
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16

    # Exact halves round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("3.000") == 3

    # Negative non-half values
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    print("All tests passed.")


test_closest_integer()

# Generated at 2026-10-25 14:21:11.592598
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10") == 10

# Generated at 2026-10-25 14:21:15.314682
# Unit test for function closest_integer

# Generated at 2026-10-25 14:21:33.339879
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("2.5") == 3

# Generated at 2026-10-25 14:22:00.371739
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("2.6") == 3

    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("-2.6") == -3

    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("15.0") == 15

# Generated at 2026-10-25 14:22:33.447190
# Unit test for function closest_integer

# Generated at 2026-10-25 14:22:39.284013
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10.5") == 11

# Generated at 2026-10-25 14:22:49.921267
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("2.0") == 2
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 14:22:58.945012
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10") == 10

# Generated at 2026-10-25 14:23:23.830186
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 14:23:49.018602
# Unit test for function closest_integer
def test_closest_integer():assert module_0.closest_integer("10") == 10

# Generated at 2026-10-25 14:24:15.642759
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("3.50") == 4
    assert module_0.closest_integer("-3.500") == -4
    assert module_0.closest_integer("0.000") == 0

# Generated at 2026-10-25 14:24:44.111599
# Unit test for function closest_integer
def test_closest_integer():
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    assert module_0.closest_integer("2.49") == 2
    assert module_0.closest_integer("2.51") == 3
    assert module_0.closest_integer("-2.49") == -2
    assert module_0.closest_integer("-2.51") == -3

    assert module_0.closest_integer("2.5000") == 3
    assert module_0.closest_integer("-2.5000") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("0") == 0

# Generated at 2026-10-25 14:24:49.578221
# Unit test for function closest_integer

# Generated at 2026-10-25 14:24:58.059375
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:00.474197
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:02.890362
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:05.307464
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:10.751020
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:13.164209
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:15.578441
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:17.993552
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:20.407907
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:22.822637
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:25.236772
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:27.653986
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:30.068243
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:32.483872
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:34.898682
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:37.313343
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:39.730257
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:42.149063
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:44.563825
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:46.997506
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:49.411695
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:51.825460
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:54.242278
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:56.656964
# Unit test for function closest_integer

# Generated at 2026-10-25 14:25:59.073974
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:01.490828
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:03.907168
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:06.323268
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:08.737808
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:11.152392
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:13.569142
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:15.981163
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:18.394553
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:20.815539
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:23.231981
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:25.644813
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:28.059710
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:30.473463
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:32.888770
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:35.304819
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:37.718985
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:40.133771
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:42.551163
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:44.966407
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:47.381936
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:49.794811
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:52.209722
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:54.623763
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:57.044435
# Unit test for function closest_integer

# Generated at 2026-10-25 14:26:59.459855
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:01.868011
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:04.287901
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:06.700961
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:09.115283
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:14.662791
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:17.078617
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:19.492506
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:21.910812
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:24.325462
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:26.742368
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:29.156896
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:31.575521
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:33.990369
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:36.405363
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:38.819890
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:41.329440
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:43.747487
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:46.163789
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:48.576340
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:50.990836
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:53.405668
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:55.819927
# Unit test for function closest_integer

# Generated at 2026-10-25 14:27:58.235031
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:00.650782
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:03.065011
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:05.477971
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:07.891581
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:10.318442
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:12.730073
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:15.145634
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:17.562252
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:19.975924
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:22.393287
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:24.807089
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:27.220096
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:29.635506
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:32.056606
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:34.471166
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:36.884369
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:39.300281
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:41.718269
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:44.135053
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:46.551929
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:48.964984
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:51.378137
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:54.730849
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:57.145291
# Unit test for function closest_integer

# Generated at 2026-10-25 14:28:59.560884
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:01.977056
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:04.395174
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:06.809242
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:09.222589
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:11.638492
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:14.053497
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:19.496676
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:21.910586
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:24.328490
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:26.819384
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:29.172780
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:31.587717
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:34.002395
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:36.417291
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:38.831967
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:41.247605
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:43.662012
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:46.078670
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:48.492689
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:50.905770
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:53.323653
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:55.737789
# Unit test for function closest_integer

# Generated at 2026-10-25 14:29:58.152957
# Unit test for function closest_integer

# Generated at 2026-10-25 14:30:00.568541
# Unit test for function closest_integer