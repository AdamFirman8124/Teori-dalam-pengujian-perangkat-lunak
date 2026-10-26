

# Generated at 2026-10-25 11:26:26.763592
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:29.140743
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:31.557371
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:33.971161
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:36.385419
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:38.799287
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:41.213948
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:43.630583
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:46.043896
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:48.457612
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:50.870840
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:53.286691
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:55.700624
# Unit test for function sum_squares

# Generated at 2026-10-25 11:26:58.115297
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:00.530198
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:02.947809
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:05.361188
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:07.775350
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:10.189391
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:12.637334
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:15.021684
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:17.438809
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:19.850824
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:22.266031
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:24.679858
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:27.093765
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:29.511625
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:31.926017
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:34.342319
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:36.756237
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:39.170827
# Unit test for function sum_squares

# Generated at 2026-10-25 11:27:43.137480
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 11:27:59.644582
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:28:16.213717
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:28:18.779257
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:21.192911
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:23.606408
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:26.020639
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:28.616908
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:31.033222
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:33.445568
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:35.863044
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:38.281058
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:40.696081
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:43.111301
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:45.525926
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:47.936753
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:50.350412
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:52.765700
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:55.181570
# Unit test for function sum_squares

# Generated at 2026-10-25 11:28:57.595128
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:00.012828
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:02.423155
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:04.836517
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:07.250390
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:09.764251
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:12.139381
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:14.555462
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:16.969550
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:19.384315
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:21.798657
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:24.213324
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:26.649798
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:29.060940
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:31.474988
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:33.887508
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:36.301201
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:38.778268
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:41.144250
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:43.558144
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:45.973728
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:48.387073
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:50.804763
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:53.217091
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:55.631974
# Unit test for function sum_squares

# Generated at 2026-10-25 11:29:58.046728
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:00.461606
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:02.876969
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:05.293545
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:07.710453
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:10.124449
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:12.538902
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:14.952595
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:17.366418
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:19.784110
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:22.200297
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:24.617396
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:27.030092
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:29.444978
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:31.860128
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:34.274477
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:36.688667
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:39.103274
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:41.562674
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:43.976526
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:46.393334
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:48.807370
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:51.228291
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:53.647599
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:56.061742
# Unit test for function sum_squares

# Generated at 2026-10-25 11:30:58.476109
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:00.891042
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:03.306704
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:05.721518
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:08.133318
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:10.547256
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:12.962804
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:15.378944
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:17.790879
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:20.207455
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:22.621113
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:25.034969
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:27.449702
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:29.865417
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:32.286758
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:34.697385
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:37.115839
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:39.530187
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:41.945055
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:44.359750
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:46.775188
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:49.192067
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:51.603611
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:54.017120
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:56.431848
# Unit test for function sum_squares

# Generated at 2026-10-25 11:31:58.847603
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:01.263664
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:03.680060
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:06.093204
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:08.507892
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:10.922622
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:13.338322
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:15.755339
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:18.171177
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:20.586476
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:23.000342
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:25.415161
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:27.831514
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:30.242499
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:32.663616
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:35.086211
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:37.499462
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:39.909845
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:42.326614
# Unit test for function sum_squares

# Generated at 2026-10-25 11:32:45.511370
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 11:33:17.094646
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:33:18.537242
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:33:20.017644
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:33:23.088810
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:33:25.509482
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:28.048600
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:30.465192
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:32.880542
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:35.300424
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:37.714019
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:40.128065
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:42.542256
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:44.958784
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:47.370873
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:49.788600
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:52.208672
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:54.620156
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:57.035019
# Unit test for function sum_squares

# Generated at 2026-10-25 11:33:59.449936
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:01.865894
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:04.279862
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:06.845836
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:09.123205
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:11.537716
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:13.951050
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:16.365049
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:18.777994
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:21.192350
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:23.604938
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:26.019563
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:28.433204
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:30.846539
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:33.262466
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:35.678925
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:38.103959
# Unit test for function sum_squares

# Generated at 2026-10-25 11:34:40.457470
# Unit test for function sum_squares
def test_sum_squares():assert module_0.sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 939

# Generated at 2026-10-25 11:34:58.332368
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:35:00.964357
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:03.379656
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:05.794296
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:08.208768
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:10.622550
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:13.040437
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:15.456065
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:17.871140
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:20.546523
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:22.973860
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:25.391042
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:27.801733
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:30.218907
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:32.629198
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:35.042375
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:37.461358
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:39.874342
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:42.286537
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:44.699279
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:47.112336
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:49.527542
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:51.943046
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:54.354168
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:56.770386
# Unit test for function sum_squares

# Generated at 2026-10-25 11:35:59.269237
# Unit test for function sum_squares

# Generated at 2026-10-25 11:36:01.684888
# Unit test for function sum_squares

# Generated at 2026-10-25 11:36:04.100515
# Unit test for function sum_squares

# Generated at 2026-10-25 11:36:24.648740
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()

# Generated at 2026-10-25 11:36:53.108941
# Unit test for function sum_squares
def test_sum_squares():
    # Basic example from spec
    assert module_0.sum_squares([1, 2, 3]) == 6            # 1 + 2 + 3 (no i divisible by 3 or 4 except i=0)
    assert module_0.sum_squares([]) == 0                   # empty list
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 40     # i=0:1Â²=1, i=3:4Â²=16, i=4:5Â³=125? â see breakdown below

    # Breakdown for [1,2,3,4,5]:
    # i=0: 1**2 = 1
    # i=1: 1
    # i=2: 3
    # i=3: 4**2 = 16
    # i=4: 5**3 = 125  â total = 146
    assert module_0.sum_squares([1, 2, 3, 4, 5]) == 146

    # i divisible by both 3 and 4 (i=12): must be squared, NOT cubed
    lst = list(range(13))  # [0..12]
    # i=0:0, i=3:81, i=4:64, i=6:216, i=8:512, i=9:6561, i=12:144 (squared, since i%3==0 wins)
    expected = sum(x for i, x in enumerate(lst)
                   if i % 3 != 0 and i % 4 != 0) \
             + sum(lst[i]**2 for i in range(13) if i % 3 == 0) \
             + sum(lst[i]**3 for i in range(13) if i % 4 == 0 and i % 3 != 0)
    assert module_0.sum_squares(lst) == expected

    # Negatives: squaring/cubing changes sign behavior
    # [-1, -2, -3, -4]: i=0:1, i=1:-2, i=2:-3, i=3:16 â 12
    assert module_0.sum_squares([-1, -2, -3, -4]) == 12

    print("All tests passed!")

test_sum_squares()