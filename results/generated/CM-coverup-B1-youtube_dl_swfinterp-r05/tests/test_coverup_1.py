# file: project/youtube_dl/swfinterp.py:438-834
# asked: {"lines": [439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 453, 454, 455, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 544, 545, 546, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 566, 567, 568, 569, 570, 571, 572, 573, 574, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 667, 668, 669, 671, 672, 673, 674, 675, 676, 677, 678, 680, 681, 682, 683, 684, 685, 686, 687, 688, 690, 692, 693, 694, 695, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 730, 731, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 830, 831, 833, 834], "branches": [[440, 441], [440, 442], [442, 443], [442, 444], [444, 445], [444, 446], [446, 447], [446, 449], [461, 462], [463, 464], [463, 465], [465, 466], [465, 468], [468, 469], [468, 473], [471, 461], [471, 472], [473, 474], [473, 478], [476, 461], [476, 477], [478, 479], [478, 484], [482, 461], [482, 483], [484, 485], [484, 490], [488, 461], [488, 489], [490, 491], [490, 496], [494, 461], [494, 495], [496, 497], [496, 498], [498, 499], [498, 500], [500, 501], [500, 503], [503, 504], [503, 506], [506, 507], [506, 508], [508, 509], [508, 510], [510, 511], [510, 512], [512, 513], [512, 515], [515, 516], [515, 518], [518, 519], [518, 521], [521, 522], [521, 528], [528, 529], [528, 602], [536, 537], [536, 551], [537, 538], [537, 548], [541, 542], [541, 544], [551, 552], [551, 556], [556, 557], [556, 561], [561, 562], [561, 569], [562, 563], [562, 566], [569, 570], [569, 586], [570, 571], [570, 579], [573, 574], [573, 576], [579, 580], [579, 599], [586, 587], [586, 599], [587, 588], [587, 593], [593, 594], [593, 599], [602, 603], [602, 605], [605, 606], [605, 608], [608, 610], [608, 614], [614, 615], [614, 627], [627, 628], [627, 652], [634, 635], [634, 639], [639, 640], [639, 645], [645, 646], [645, 649], [652, 653], [652, 659], [655, 656], [655, 657], [659, 660], [659, 672], [662, 663], [662, 667], [663, 662], [663, 664], [668, 669], [668, 671], [672, 673], [672, 682], [675, 676], [675, 680], [676, 675], [676, 677], [682, 683], [682, 701], [685, 686], [685, 690], [686, 685], [686, 687], [692, 693], [692, 694], [694, 695], [694, 699], [701, 702], [701, 709], [705, 706], [705, 707], [709, 710], [709, 712], [712, 713], [712, 716], [716, 717], [716, 740], [719, 720], [719, 723], [723, 724], [723, 735], [725, 726], [725, 730], [740, 741], [740, 748], [744, 745], [744, 746], [748, 749], [748, 752], [752, 753], [752, 754], [754, 755], [754, 758], [758, 759], [758, 760], [760, 761], [760, 764], [764, 765], [764, 772], [772, 773], [772, 777], [777, 778], [777, 782], [782, 783], [782, 787], [787, 788], [787, 792], [792, 793], [792, 799], [799, 800], [799, 804], [804, 805], [804, 809], [809, 810], [809, 813], [813, 814], [813, 815], [815, 816], [815, 817], [817, 818], [817, 819], [819, 820], [819, 821], [821, 822], [821, 823], [823, 824], [823, 825], [825, 826], [825, 827], [827, 828], [827, 830]]}
# gained: {"lines": [439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 453, 454, 455, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 544, 545, 546, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 566, 567, 568, 569, 570, 571, 572, 573, 574, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 667, 668, 669, 671, 672, 673, 674, 675, 676, 677, 678, 680, 681, 682, 683, 684, 685, 686, 687, 688, 690, 692, 693, 694, 695, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 730, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 830, 831, 833, 834], "branches": [[440, 441], [440, 442], [442, 443], [442, 444], [444, 445], [444, 446], [446, 447], [446, 449], [461, 462], [463, 464], [463, 465], [465, 466], [465, 468], [468, 469], [468, 473], [471, 461], [471, 472], [473, 474], [473, 478], [476, 461], [476, 477], [478, 479], [478, 484], [482, 461], [482, 483], [484, 485], [484, 490], [488, 461], [488, 489], [490, 491], [490, 496], [494, 461], [494, 495], [496, 497], [496, 498], [498, 499], [498, 500], [500, 501], [500, 503], [503, 504], [503, 506], [506, 507], [506, 508], [508, 509], [508, 510], [510, 511], [510, 512], [512, 513], [512, 515], [515, 516], [515, 518], [518, 519], [518, 521], [521, 522], [521, 528], [528, 529], [528, 602], [536, 537], [536, 551], [537, 538], [537, 548], [541, 542], [541, 544], [551, 552], [551, 556], [556, 557], [556, 561], [561, 562], [561, 569], [562, 563], [562, 566], [569, 570], [569, 586], [570, 571], [570, 579], [573, 574], [573, 576], [579, 580], [586, 587], [586, 599], [587, 588], [587, 593], [593, 594], [602, 603], [602, 605], [605, 606], [605, 608], [608, 610], [608, 614], [614, 615], [614, 627], [627, 628], [627, 652], [634, 635], [634, 639], [639, 640], [639, 645], [645, 646], [645, 649], [652, 653], [652, 659], [655, 656], [655, 657], [659, 660], [659, 672], [662, 663], [662, 667], [663, 662], [663, 664], [668, 669], [668, 671], [672, 673], [672, 682], [675, 676], [675, 680], [676, 675], [676, 677], [682, 683], [682, 701], [685, 686], [685, 690], [686, 685], [686, 687], [692, 693], [692, 694], [694, 695], [694, 699], [701, 702], [701, 709], [705, 706], [705, 707], [709, 710], [709, 712], [712, 713], [712, 716], [716, 717], [716, 740], [719, 720], [719, 723], [723, 724], [723, 735], [725, 726], [725, 730], [740, 741], [740, 748], [744, 745], [744, 746], [748, 749], [748, 752], [752, 753], [752, 754], [754, 755], [754, 758], [758, 759], [758, 760], [760, 761], [760, 764], [764, 765], [764, 772], [772, 773], [772, 777], [777, 778], [777, 782], [782, 783], [782, 787], [787, 788], [787, 792], [792, 793], [792, 799], [799, 800], [799, 804], [804, 805], [804, 809], [809, 810], [809, 813], [813, 814], [813, 815], [815, 816], [815, 817], [817, 818], [817, 819], [819, 820], [819, 821], [821, 822], [821, 823], [823, 824], [823, 825], [825, 826], [825, 827], [827, 828], [827, 830]]}

import collections
import math
import pytest
import youtube_dl.swfinterp as SWF
from youtube_dl.utils import ExtractorError


def _enc_u30(v):
    assert 0 <= v < (1 << 28)
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v == 0:
            out.append(b)
            break
        out.append(b | 0x80)
    return bytes(out)


def _enc_s24(v):
    if v < 0:
        v += 1 << 24
    return bytes([v & 0xFF, (v >> 8) & 0xFF, (v >> 16) & 0xFF])


def _new_interp():
    interp = SWF.SWFInterpreter.__new__(SWF.SWFInterpreter)
    interp._patched_functions = {}
    interp._classes_by_name = {}
    interp.constant_strings = ['']
    interp.multinames = ['']
    return interp


def _new_class(name='C'):
    return SWF._AVMClass(0, name)


Method = collections.namedtuple('Method', ['code', 'local_count'])


def _run(interp, cls, func_name, code, args=None, local_count=10):
    if args is None:
        args = []
    cls.methods[func_name] = Method(code, local_count)
    if func_name in cls.method_pyfunctions:
        del cls.method_pyfunctions[func_name]
    f = interp.extract_function(cls, func_name)
    return f(list(args))


def _multiname():
    try:
        return SWF._Multiname(15)
    except Exception:
        try:
            return SWF._Multiname()
        except Exception:
            return object.__new__(SWF._Multiname)


def test_patched():
    interp = _new_interp()
    cls = _new_class('P1')
    sentinel = lambda a: 'patched'
    interp._patched_functions[(cls, 'foo')] = sentinel
    assert interp.extract_function(cls, 'foo') is sentinel


def test_pyfunction_cached():
    interp = _new_interp()
    cls = _new_class('P2')
    myf = lambda a: 123
    cls.method_pyfunctions['bar'] = myf
    assert interp.extract_function(cls, 'bar') is myf


def test_classes_by_name():
    interp = _new_interp()
    cls = _new_class('P3')
    target = _new_class('MyClass')
    interp._classes_by_name['MyClass'] = target
    f = interp.extract_function(cls, 'MyClass')
    assert isinstance(f, SWF._AVMClass_Object)
    assert f.avm_class is target


def test_missing_raises():
    interp = _new_interp()
    cls = _new_class('P4')
    with pytest.raises(ExtractorError):
        interp.extract_function(cls, 'nope')


def test_label_and_jump():
    interp = _new_interp()
    cls = _new_class('J1')
    code = bytes([9, 16]) + _enc_s24(2) + bytes([36, 99, 36, 42, 72])
    res = _run(interp, cls, 'f_jump', code, [])
    assert res == 42


def test_iftrue_both():
    interp = _new_interp()
    cls = _new_class('J2')
    code = bytes([209, 17]) + _enc_s24(3) + bytes([36, 10, 72, 36, 20, 72])
    cls.methods['f_iftrue'] = Method(code, 10)
    func = interp.extract_function(cls, 'f_iftrue')
    assert func([True]) == 20
    assert func([False]) == 10


def test_iffalse_both():
    interp = _new_interp()
    cls = _new_class('J3')
    code = bytes([209, 18]) + _enc_s24(3) + bytes([36, 10, 72, 36, 20, 72])
    cls.methods['f_iffalse'] = Method(code, 10)
    func = interp.extract_function(cls, 'f_iffalse')
    assert func([True]) == 10
    assert func([False]) == 20


def test_ifeq_both():
    interp = _new_interp()
    cls = _new_class('J4')
    code = bytes([209, 210, 19]) + _enc_s24(3) + bytes([36, 10, 72, 36, 20, 72])
    cls.methods['f_ifeq'] = Method(code, 10)
    func = interp.extract_function(cls, 'f_ifeq')
    assert func([5, 5]) == 20
    assert func([5, 6]) == 10


def test_ifne_both():
    interp = _new_interp()
    cls = _new_class('J5')
    code = bytes([209, 210, 20]) + _enc_s24(3) + bytes([36, 10, 72, 36, 20, 72])
    cls.methods['f_ifne'] = Method(code, 10)
    func = interp.extract_function(cls, 'f_ifne')
    assert func([5, 5]) == 10
    assert func([5, 6]) == 20


def test_iflt_both():
    interp = _new_interp()
    cls = _new_class('J6')
    code = bytes([209, 210, 21]) + _enc_s24(3) + bytes([36, 10, 72, 36, 20, 72])
    cls.methods['f_iflt'] = Method(code, 10)
    func = interp.extract_function(cls, 'f_iflt')
    assert func([1, 2]) == 20
    assert func([2, 1]) == 10
    assert func([1, 1]) == 10


def test_pushes_and_dup_and_string():
    interp = _new_interp()
    cls = _new_class('Pu1')
    assert _run(interp, cls, 'f_null', bytes([32, 72]), []) is None
    assert _run(interp, cls, 'f_undef', bytes([33, 72]), []) is SWF.undefined
    assert _run(interp, cls, 'f_byte', bytes([36, 123, 72]), []) == 123
    assert _run(interp, cls, 'f_short', bytes([37]) + _enc_u30(50) + bytes([72]), []) == 50
    assert _run(interp, cls, 'f_true', bytes([38, 72]), []) is True
    assert _run(interp, cls, 'f_false', bytes([39, 72]), []) is False
    r = _run(interp, cls, 'f_nan', bytes([40, 72]), [])
    assert isinstance(r, float) and math.isnan(r)
    assert _run(interp, cls, 'f_dup', bytes([36, 5, 42, 160, 72]), []) == 10
    interp.constant_strings = ['', 'hello']
    assert _run(interp, cls, 'f_str', bytes([44]) + _enc_u30(1) + bytes([72]), []) == 'hello'
    assert _run(interp, cls, 'f_scope', bytes([32, 48, 71]), []) is SWF.undefined


def test_getlocal_setlocal():
    interp = _new_interp()
    cls = _new_class('Loc1')
    code = bytes([209]) + bytes([99]) + _enc_u30(5) + bytes([98]) + _enc_u30(5) + bytes([72])
    assert _run(interp, cls, 'f_loc', code, [77]) == 77
    code2 = bytes([36, 11, 212, 208, 72])
    assert _run(interp, cls, 'f_l0', code2, []) == 11
    code3 = bytes([36, 12, 213, 209, 72])
    assert _run(interp, cls, 'f_l1', code3, [0]) == 12
    code4 = bytes([36, 13, 214, 210, 72])
    assert _run(interp, cls, 'f_l2', code4, [0, 0]) == 13
    code5 = bytes([36, 14, 215, 211, 72])
    assert _run(interp, cls, 'f_l3', code5, [0, 0, 0]) == 14


def test_construct():
    interp = _new_interp()
    cls = _new_class('Co1')
    target = _new_class('Targ')
    obj = target.make_object()
    code = bytes([209, 66]) + _enc_u30(0) + bytes([72])
    res = _run(interp, cls, 'f_cons', code, [obj])
    assert isinstance(res, SWF._AVMClass_Object)
    assert res.avm_class is target


def test_callproperty_string():
    interp = _new_interp()
    cls = _new_class('S1')
    interp.multinames = ['', 'String']
    SClass = SWF.StringClass
    code = bytes([209, 33, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_s_undef', code, [SClass]) == 'undefined'
    code2 = bytes([209, 36, 7, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_s_int', code2, [SClass]) == '7'
    code3 = bytes([209, 210, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_s_str', code3, [SClass, 'hi']) == 'hi'
    interp.multinames = ['', 'Nope']
    code4 = bytes([209, 36, 1, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    with pytest.raises(NotImplementedError):
        _run(interp, cls, 'f_s_bad', code4, [SClass])


def test_callproperty_avm_object_and_class():
    interp = _new_interp()
    cls = _new_class('S2')
    target = _new_class('T2')
    target.method_pyfunctions['foo'] = lambda args: 'foo-result'
    target2 = _new_class('T3')
    target2.method_pyfunctions['bar'] = lambda args: 'bar-result'
    interp.multinames = ['', 'foo', 'bar']
    obj = target.make_object()
    code = bytes([209, 70]) + _enc_u30(1) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_obj', code, [obj]) == 'foo-result'
    code2 = bytes([209, 70]) + _enc_u30(2) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_cls', code2, [target2]) == 'bar-result'


def test_callproperty_scopedict():
    interp = _new_interp()
    cls = _new_class('S3')
    cls.method_names['mym'] = 0
    cls.method_pyfunctions['mym'] = lambda args: 'm-res'
    cls.variables['plain'] = 'plain-val'
    interp.multinames = ['', 'mym', 'plain']
    code = bytes([209, 70]) + _enc_u30(1) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_sdm', code, [cls.variables]) == 'm-res'
    code2 = bytes([209, 70]) + _enc_u30(2) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_sdp', code2, [cls.variables]) == 'plain-val'


def test_callproperty_str_methods():
    interp = _new_interp()
    cls = _new_class('S4')
    interp.multinames = ['', 'split', 'charCodeAt']
    code = bytes([209, 210, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_split', code, ['a,b', ',']) == ['a', 'b']
    assert _run(interp, cls, 'f_split2', code, ['abc', '']) == ['a', 'b', 'c']
    code2 = bytes([209, 210, 70]) + _enc_u30(2) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_cca', code2, ['ABC', 1]) == ord('B')
    code3 = bytes([209, 70]) + _enc_u30(2) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_cca0', code3, ['XYZ']) == ord('X')


def test_callproperty_list_and_unsupported():
    interp = _new_interp()
    cls = _new_class('S5')
    interp.multinames = ['', 'slice', 'join', 'badprop']
    code = bytes([209, 210, 70]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_slice', code, [[1, 2, 3], 1]) == [2, 3]
    code2 = bytes([209, 210, 70]) + _enc_u30(2) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_join', code2, [['a', 'b'], '-']) == 'a-b'
    code3 = bytes([209, 70]) + _enc_u30(3) + _enc_u30(0) + bytes([72])
    with pytest.raises(NotImplementedError):
        _run(interp, cls, 'f_bad', code3, [12345])


def test_returnvoid_value():
    interp = _new_interp()
    cls = _new_class('R1')
    assert _run(interp, cls, 'f_rv', bytes([71]), []) is SWF.undefined
    assert _run(interp, cls, 'f_rval', bytes([36, 9, 72]), []) == 9


def test_constructsuper():
    interp = _new_interp()
    cls = _new_class('Cs1')
    dummy_target = _new_class('DT')
    dummy_obj = dummy_target.make_object()
    code = bytes([209, 73]) + _enc_u30(0) + bytes([36, 8, 72])
    assert _run(interp, cls, 'f_csup', code, [dummy_obj]) == 8
    code2 = bytes([209, 210, 73]) + _enc_u30(1) + bytes([36, 9, 72])
    assert _run(interp, cls, 'f_csup2', code2, [dummy_obj, 1]) == 9


def test_constructprop():
    interp = _new_interp()
    cls = _new_class('Cp1')
    target = _new_class('CT')
    interp.multinames = ['', 'MyCtor']
    code = bytes([209, 74]) + _enc_u30(1) + _enc_u30(0) + bytes([72])
    res = _run(interp, cls, 'f_cprop', code, [target])
    assert isinstance(res, SWF._AVMClass_Object)
    code2 = bytes([209, 210, 74]) + _enc_u30(1) + _enc_u30(1) + bytes([72])
    res2 = _run(interp, cls, 'f_cprop2', code2, [target, 1])
    assert isinstance(res2, SWF._AVMClass_Object)


def test_callpropvoid():
    interp = _new_interp()
    cls = _new_class('Cv1')
    target = _new_class('TV')
    target.method_pyfunctions['vm'] = lambda args: SWF.undefined
    interp.multinames = ['', 'vm', 'reverse', 'badvoid']
    obj = target.make_object()
    code = bytes([209, 79]) + _enc_u30(1) + _enc_u30(0) + bytes([71])
    assert _run(interp, cls, 'f_cpv', code, [obj]) is SWF.undefined
    cls2 = _new_class('Cv2')
    cls2.method_names['vm2'] = 0
    cls2.method_pyfunctions['vm2'] = lambda args: SWF.undefined
    interp2 = _new_interp()
    interp2.multinames = ['', 'vm2']
    code2 = bytes([209, 79]) + _enc_u30(1) + _enc_u30(0) + bytes([71])
    assert _run(interp2, cls2, 'f_cpv2', code2, [cls2.variables]) is SWF.undefined
    interp.multinames = ['', 'vm', 'reverse', 'badvoid']
    lst = [1, 2, 3]
    code3 = bytes([209, 79]) + _enc_u30(2) + _enc_u30(0) + bytes([71])
    assert _run(interp, cls, 'f_rev', code3, [lst]) is SWF.undefined
    assert lst == [3, 2, 1]
    code4 = bytes([209, 79]) + _enc_u30(3) + _enc_u30(0) + bytes([71])
    with pytest.raises(NotImplementedError):
        _run(interp, cls, 'f_cpvbad', code4, [123])


def test_newarray():
    interp = _new_interp()
    cls = _new_class('Na1')
    code = bytes([36, 1, 36, 2, 86]) + _enc_u30(2) + bytes([72])
    assert _run(interp, cls, 'f_na', code, []) == [1, 2]
    code2 = bytes([86]) + _enc_u30(0) + bytes([72])
    assert _run(interp, cls, 'f_na0', code2, []) == []


def test_findpropstrict():
    interp = _new_interp()
    cls = _new_class('Fp1')
    cls.variables['myv'] = 999
    interp.multinames = ['', 'myv']
    code = bytes([93]) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_fps', code, []) == 999
    bname = list(SWF._builtin_classes.keys())[0]
    interp.multinames = ['', bname]
    assert bname not in cls.variables
    assert bname not in cls.constants
    code2 = bytes([93]) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_fpsb', code2, []) is SWF._builtin_classes[bname]


def test_findproperty():
    interp = _new_interp()
    cls = _new_class('Fp2')
    cls.variables['qv'] = 111
    interp.multinames = ['', 'qv', 'absent_xyz']
    code = bytes([94]) + _enc_u30(1) + bytes([72])
    res = _run(interp, cls, 'f_fp', code, [])
    assert res is cls.variables or 'qv' in res
    code2 = bytes([94]) + _enc_u30(2) + bytes([72])
    res2 = _run(interp, cls, 'f_fp2', code2, [])
    assert res2 is cls.variables


def test_getlex():
    interp = _new_interp()
    cls = _new_class('Gl1')
    cls.variables['gx'] = 'gv'
    bname = list(SWF._builtin_classes.keys())[0]
    interp.multinames = ['', 'gx', bname, 'no_such_lex_zzz']
    code = bytes([96]) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_gl', code, []) == 'gv'
    cls.variables.pop(bname, None)
    cls.constants.pop(bname, None)
    code2 = bytes([96]) + _enc_u30(2) + bytes([72])
    assert _run(interp, cls, 'f_glb', code2, []) is SWF._builtin_classes[bname]
    code3 = bytes([96]) + _enc_u30(3) + bytes([72])
    assert _run(interp, cls, 'f_glu', code3, []) is SWF.undefined


def test_setproperty():
    interp = _new_interp()
    cls = _new_class('Sp1')
    interp.multinames = ['', 'k1']
    d = {}
    code = bytes([209, 210, 97]) + _enc_u30(1) + bytes([209, 72])
    assert _run(interp, cls, 'f_sp', code, [d, 55]) == d
    assert d == {'k1': 55}
    mn = _multiname()
    interp.multinames = ['', mn]
    d2 = {}
    code2 = bytes([209, 210, 211, 97]) + _enc_u30(1) + bytes([209, 72])
    assert _run(interp, cls, 'f_spm', code2, [d2, 'dynk', 66]) == d2
    assert d2 == {'dynk': 66}


def test_getproperty():
    interp = _new_interp()
    cls = _new_class('Gp1')
    interp.multinames = ['', 'length', 'sprop', 'mkey']
    code = bytes([209, 102]) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_gpl', code, ['abcd']) == 4
    assert _run(interp, cls, 'f_gpl2', code, [[1, 2, 3]]) == 3
    target = _new_class('ST')
    target.static_properties = {'sprop': 'sval'}
    interp.multinames = ['', 'length', 'sprop', 'mkey']
    code2 = bytes([209, 102]) + _enc_u30(2) + bytes([72])
    assert _run(interp, cls, 'f_gps', code2, [target]) == 'sval'
    code3 = bytes([209, 102]) + _enc_u30(3) + bytes([72])
    assert _run(interp, cls, 'f_gpm', code3, [{'mkey': 'mval'}]) == 'mval'
    assert _run(interp, cls, 'f_gpm2', code3, [{}]) is SWF.undefined
    mn = _multiname()
    interp.multinames = ['', mn]
    code4 = bytes([209, 210, 102]) + _enc_u30(1) + bytes([72])
    assert _run(interp, cls, 'f_gpa', code4, [[10, 20, 30], 1]) == 20


def test_initproperty():
    interp = _new_interp()
    cls = _new_class('Ip1')
    interp.multinames = ['', 'ik']
    d = {}
    code = bytes([209, 210, 104]) + _enc_u30(1) + bytes([209, 72])
    assert _run(interp, cls, 'f_ip', code, [d, 77]) == d
    assert d['ik'] == 77
    mn = _multiname()
    interp.multinames = ['', mn]
    d2 = {}
    code2 = bytes([209, 210, 211, 104]) + _enc_u30(1) + bytes([209, 72])
    assert _run(interp, cls, 'f_ipm', code2, [d2, 'ak', 88]) == d2
    assert d2['ak'] == 88


def test_convert_coerce():
    interp = _new_interp()
    cls = _new_class('Cc1')
    assert _run(interp, cls, 'f_conv', bytes([209, 115, 72]), ['42']) == 42
    code = bytes([209, 128]) + _enc_u30(0) + bytes([209, 72])
    assert _run(interp, cls, 'f_coerce', code, [5]) == 5
    assert _run(interp, cls, 'f_coercea', bytes([209, 130, 72]), [6]) == 6
    assert _run(interp, cls, 'f_coerces', bytes([32, 133, 72]), []) is None
    assert _run(interp, cls, 'f_coerces2', bytes([209, 133, 72]), ['s']) == 's'


def test_decrement_typeof():
    interp = _new_interp()
    cls = _new_class('Dt1')
    assert _run(interp, cls, 'f_dec', bytes([209, 147, 72]), [10]) == 9
    assert _run(interp, cls, 'f_type_s', bytes([209, 149]), ['x']) == 'String'
    assert _run(interp, cls, 'f_type_i', bytes([209, 149]), [1]) == 'Number'
    assert _run(interp, cls, 'f_type_f', bytes([209, 149]), [1.5]) == 'Number'
    assert _run(interp, cls, 'f_type_u', bytes([33, 149]), []) == 'undefined'


def test_arith():
    interp = _new_interp()
    cls = _new_class('Ar1')
    assert _run(interp, cls, 'f_add', bytes([209, 210, 160, 72]), [3, 4]) == 7
    assert _run(interp, cls, 'f_sub', bytes([209, 210, 161, 72]), [10, 4]) == 6
    assert _run(interp, cls, 'f_mul', bytes([209, 210, 162, 72]), [3, 5]) == 15
    assert _run(interp, cls, 'f_mod', bytes([209, 210, 164, 72]), [10, 3]) == 1
    assert _run(interp, cls, 'f_and', bytes([209, 210, 168, 72]), [6, 3]) == 2
    assert _run(interp, cls, 'f_eq', bytes([209, 210, 171, 72]), [1, 1]) is True
    assert _run(interp, cls, 'f_ge', bytes([209, 210, 175, 72]), [2, 2]) is True
    assert _run(interp, cls, 'f_ge2', bytes([209, 210, 175, 72]), [1, 2]) is False
    assert _run(interp, cls, 'f_inc', bytes([209, 192, 72]), [7]) == 8


def test_unsupported_opcode():
    interp = _new_interp()
    cls = _new_class('Un1')
    with pytest.raises(NotImplementedError):
        _run(interp, cls, 'f_un', bytes([255, 72]), [])


def test_pushscope_affects_findproperty():
    interp = _new_interp()
    cls = _new_class('Ps1')
    interp.multinames = ['', 'sk']
    new_scope = {'sk': 'skv'}
    code = bytes([209, 48, 94]) + _enc_u30(1) + bytes([72])
    res = _run(interp, cls, 'f_ps', code, [new_scope])
    assert res is new_scope or 'sk' in res
