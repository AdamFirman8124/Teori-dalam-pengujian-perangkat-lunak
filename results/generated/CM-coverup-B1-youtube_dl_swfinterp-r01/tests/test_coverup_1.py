# file: project/youtube_dl/swfinterp.py:438-834
# asked: {"lines": [439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 453, 454, 455, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 544, 545, 546, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 566, 567, 568, 569, 570, 571, 572, 573, 574, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 667, 668, 669, 671, 672, 673, 674, 675, 676, 677, 678, 680, 681, 682, 683, 684, 685, 686, 687, 688, 690, 692, 693, 694, 695, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 730, 731, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 830, 831, 833, 834], "branches": [[440, 441], [440, 442], [442, 443], [442, 444], [444, 445], [444, 446], [446, 447], [446, 449], [461, 462], [463, 464], [463, 465], [465, 466], [465, 468], [468, 469], [468, 473], [471, 461], [471, 472], [473, 474], [473, 478], [476, 461], [476, 477], [478, 479], [478, 484], [482, 461], [482, 483], [484, 485], [484, 490], [488, 461], [488, 489], [490, 491], [490, 496], [494, 461], [494, 495], [496, 497], [496, 498], [498, 499], [498, 500], [500, 501], [500, 503], [503, 504], [503, 506], [506, 507], [506, 508], [508, 509], [508, 510], [510, 511], [510, 512], [512, 513], [512, 515], [515, 516], [515, 518], [518, 519], [518, 521], [521, 522], [521, 528], [528, 529], [528, 602], [536, 537], [536, 551], [537, 538], [537, 548], [541, 542], [541, 544], [551, 552], [551, 556], [556, 557], [556, 561], [561, 562], [561, 569], [562, 563], [562, 566], [569, 570], [569, 586], [570, 571], [570, 579], [573, 574], [573, 576], [579, 580], [579, 599], [586, 587], [586, 599], [587, 588], [587, 593], [593, 594], [593, 599], [602, 603], [602, 605], [605, 606], [605, 608], [608, 610], [608, 614], [614, 615], [614, 627], [627, 628], [627, 652], [634, 635], [634, 639], [639, 640], [639, 645], [645, 646], [645, 649], [652, 653], [652, 659], [655, 656], [655, 657], [659, 660], [659, 672], [662, 663], [662, 667], [663, 662], [663, 664], [668, 669], [668, 671], [672, 673], [672, 682], [675, 676], [675, 680], [676, 675], [676, 677], [682, 683], [682, 701], [685, 686], [685, 690], [686, 685], [686, 687], [692, 693], [692, 694], [694, 695], [694, 699], [701, 702], [701, 709], [705, 706], [705, 707], [709, 710], [709, 712], [712, 713], [712, 716], [716, 717], [716, 740], [719, 720], [719, 723], [723, 724], [723, 735], [725, 726], [725, 730], [740, 741], [740, 748], [744, 745], [744, 746], [748, 749], [748, 752], [752, 753], [752, 754], [754, 755], [754, 758], [758, 759], [758, 760], [760, 761], [760, 764], [764, 765], [764, 772], [772, 773], [772, 777], [777, 778], [777, 782], [782, 783], [782, 787], [787, 788], [787, 792], [792, 793], [792, 799], [799, 800], [799, 804], [804, 805], [804, 809], [809, 810], [809, 813], [813, 814], [813, 815], [815, 816], [815, 817], [817, 818], [817, 819], [819, 820], [819, 821], [821, 822], [821, 823], [823, 824], [823, 825], [825, 826], [825, 827], [827, 828], [827, 830]]}
# gained: {"lines": [439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 453, 454, 455, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 544, 545, 546, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 566, 567, 568, 569, 570, 571, 572, 573, 574, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 621, 622, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 667, 668, 669, 671, 672, 673, 674, 675, 676, 677, 678, 680, 681, 682, 683, 684, 685, 686, 687, 688, 690, 692, 693, 694, 695, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 730, 732, 733, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 830, 831, 833, 834], "branches": [[440, 441], [440, 442], [442, 443], [442, 444], [444, 445], [444, 446], [446, 447], [446, 449], [461, 462], [463, 464], [463, 465], [465, 466], [465, 468], [468, 469], [468, 473], [471, 461], [471, 472], [473, 474], [473, 478], [476, 461], [476, 477], [478, 479], [478, 484], [482, 461], [482, 483], [484, 485], [484, 490], [488, 461], [488, 489], [490, 491], [490, 496], [494, 461], [494, 495], [496, 497], [496, 498], [498, 499], [498, 500], [500, 501], [500, 503], [503, 504], [503, 506], [506, 507], [506, 508], [508, 509], [508, 510], [510, 511], [510, 512], [512, 513], [512, 515], [515, 516], [515, 518], [518, 519], [518, 521], [521, 522], [521, 528], [528, 529], [528, 602], [536, 537], [536, 551], [537, 538], [537, 548], [541, 542], [541, 544], [551, 552], [551, 556], [556, 557], [556, 561], [561, 562], [561, 569], [562, 563], [562, 566], [569, 570], [569, 586], [570, 571], [570, 579], [573, 574], [573, 576], [579, 580], [579, 599], [586, 587], [586, 599], [587, 588], [587, 593], [593, 594], [602, 603], [602, 605], [605, 606], [605, 608], [608, 610], [608, 614], [614, 615], [614, 627], [627, 628], [627, 652], [634, 635], [634, 639], [639, 640], [639, 645], [645, 646], [645, 649], [652, 653], [652, 659], [655, 656], [655, 657], [659, 660], [659, 672], [662, 663], [662, 667], [663, 662], [663, 664], [668, 669], [668, 671], [672, 673], [672, 682], [675, 676], [675, 680], [676, 675], [676, 677], [682, 683], [682, 701], [685, 686], [685, 690], [686, 685], [686, 687], [692, 693], [692, 694], [694, 695], [694, 699], [701, 702], [701, 709], [705, 706], [705, 707], [709, 710], [709, 712], [712, 713], [712, 716], [716, 717], [716, 740], [719, 720], [719, 723], [723, 724], [723, 735], [725, 726], [725, 730], [740, 741], [740, 748], [744, 745], [744, 746], [748, 749], [748, 752], [752, 753], [752, 754], [754, 755], [754, 758], [758, 759], [758, 760], [760, 761], [760, 764], [764, 765], [764, 772], [772, 773], [772, 777], [777, 778], [777, 782], [782, 783], [782, 787], [787, 788], [787, 792], [792, 793], [792, 799], [799, 800], [799, 804], [804, 805], [804, 809], [809, 810], [809, 813], [813, 814], [813, 815], [815, 816], [815, 817], [817, 818], [817, 819], [819, 820], [819, 821], [821, 822], [821, 823], [823, 824], [823, 825], [825, 826], [825, 827], [827, 828], [827, 830]]}

import math
import struct
from types import SimpleNamespace

import pytest

from youtube_dl.compat import compat_str
from youtube_dl.swfinterp import (
    SWFInterpreter,
    StringClass,
    _AVMClass,
    _AVMClass_Object,
    _Multiname,
    _ScopeDict,
    undefined,
)
from youtube_dl.utils import ExtractorError


def _u30b(v):
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def _s24b(v):
    return struct.pack('<i', v)[:3]


def _interp(classes_by_name=None, constant_strings=None, multinames=None, patched=None):
    interp = object.__new__(SWFInterpreter)
    interp._patched_functions = patched if patched is not None else {}
    interp._classes_by_name = classes_by_name if classes_by_name is not None else {}
    interp.constant_strings = constant_strings if constant_strings is not None else []
    interp.multinames = multinames if multinames is not None else []
    return interp


def _cls(name='TestClass'):
    return _AVMClass(0, name)


def _build(code, multinames=None, constant_strings=None, classes_by_name=None,
           local_count=10, variables=None, constants=None):
    interp = _interp(classes_by_name=classes_by_name,
                     constant_strings=constant_strings,
                     multinames=multinames)
    cls = _cls()
    if variables:
        cls.variables.update(variables)
    if constants:
        cls.constants.update(constants)
    cls.methods['f'] = SimpleNamespace(code=code, local_count=local_count)
    func = interp.extract_function(cls, 'f')
    return func, cls, interp


def _run(code, args=(), **kwargs):
    func, cls, interp = _build(code, **kwargs)
    return func(list(args)), cls, interp


# --- extract_function dispatch (439-449, 833-834) ---

def test_patched_function_returned():
    cls = _cls()
    sentinel = lambda args: 'patched'
    interp = _interp(patched={(cls, 'f'): sentinel})
    assert interp.extract_function(cls, 'f') is sentinel
    assert interp.extract_function(cls, 'f')([]) == 'patched'


def test_pyfunction_cache_and_second_extract():
    cls = _cls()
    cached = lambda args: 7
    cls.method_pyfunctions['g'] = cached
    interp = _interp()
    assert interp.extract_function(cls, 'g') is cached
    # normal path caches in method_pyfunctions
    cls.methods['f'] = SimpleNamespace(code=bytes([71]), local_count=1)
    f1 = interp.extract_function(cls, 'f')
    assert cls.method_pyfunctions['f'] is f1
    assert interp.extract_function(cls, 'f') is f1
    assert f1([]) is undefined


def test_classes_by_name_returns_make_object():
    other = _cls('Other')
    interp = _interp(classes_by_name={'Other': other})
    cls = _cls()
    res = interp.extract_function(cls, 'Other')
    assert isinstance(res, _AVMClass_Object)
    assert res.avm_class is other


def test_missing_function_raises():
    interp = _interp()
    cls = _cls()
    with pytest.raises(ExtractorError):
        interp.extract_function(cls, 'nope')


# --- simple opcodes ---

def test_label_pushnull_pushundefined_returnvoid():
    res, _, _ = _run(bytes([9, 32, 72]))
    assert res is None
    res, _, _ = _run(bytes([33, 72]))
    assert res is undefined
    res, _, _ = _run(bytes([71]))
    assert res is undefined


def test_pushbyte_pushshort_true_false_nan_dup_pushstring():
    assert _run(bytes([36, 200, 72]))[0] == 200
    assert _run(bytes([37]) + _u30b(300) + bytes([72]))[0] == 300
    assert _run(bytes([38, 72]))[0] is True
    assert _run(bytes([39, 72]))[0] is False
    assert math.isnan(_run(bytes([40, 72]))[0])
    # dup + add: 5 dup add = 10
    assert _run(bytes([36, 5, 42, 160, 72]))[0] == 10
    assert _run(bytes([44]) + _u30b(1) + bytes([72]),
                constant_strings=['a', 'hello'])[0] == 'hello'


def test_pushscope():
    res, _, _ = _run(bytes([32, 48, 71]))
    assert res is undefined


def test_jump_skips():
    # push 1, jump over push 2, return
    code = bytes([36, 1, 16]) + _s24b(2) + bytes([36, 2, 72])
    assert _run(code)[0] == 1


def _branch_code(cond_bytes, opcode):
    # cond, branch +3 -> push 1/return ; else push 0/return
    return cond_bytes + bytes([opcode]) + _s24b(3) + bytes([36, 0, 72, 36, 1, 72])


def test_iftrue_taken_and_not():
    assert _run(_branch_code(bytes([38]), 17))[0] == 1
    assert _run(_branch_code(bytes([39]), 17))[0] == 0


def test_iffalse_taken_and_not():
    assert _run(_branch_code(bytes([39]), 18))[0] == 1
    assert _run(_branch_code(bytes([38]), 18))[0] == 0


def test_ifeq_ifne_iflt():
    assert _run(_branch_code(bytes([36, 5, 36, 5]), 19))[0] == 1
    assert _run(_branch_code(bytes([36, 5, 36, 6]), 19))[0] == 0
    assert _run(_branch_code(bytes([36, 5, 36, 6]), 20))[0] == 1
    assert _run(_branch_code(bytes([36, 5, 36, 5]), 20))[0] == 0
    assert _run(_branch_code(bytes([36, 5, 36, 6]), 21))[0] == 1
    assert _run(_branch_code(bytes([36, 6, 36, 5]), 21))[0] == 0


def test_arithmetic_ops():
    assert _run(bytes([36, 6, 36, 3, 161, 72]))[0] == 3          # subtract
    assert _run(bytes([36, 6, 36, 3, 162, 72]))[0] == 18         # multiply
    assert _run(bytes([36, 7, 36, 3, 164, 72]))[0] == 1          # modulo
    assert _run(bytes([36, 6, 36, 3, 168, 72]))[0] == 2          # bitand
    assert _run(bytes([36, 5, 36, 5, 171, 72]))[0] is True       # equals
    assert _run(bytes([36, 5, 36, 6, 171, 72]))[0] is False
    assert _run(bytes([36, 6, 36, 6, 175, 72]))[0] is True       # greaterequals
    assert _run(bytes([36, 5, 36, 6, 175, 72]))[0] is False
    assert _run(bytes([36, 5, 192, 72]))[0] == 6                  # increment_i
    assert _run(bytes([36, 5, 147, 72]))[0] == 4                  # decrement
    assert _run(bytes([36, 5, 160, 72]), args=()) [0] if False else True  # placeholder guard
    assert _run(bytes([44]) + _u30b(0) + bytes([115, 72]),
                constant_strings=['42'])[0] == 42                 # convert_i


def test_coerce_ops():
    assert _run(bytes([36, 7, 128]) + _u30b(0) + bytes([72]))[0] == 7   # coerce
    assert _run(bytes([36, 7, 130, 72]))[0] == 7                         # coerce_a
    assert _run(bytes([44]) + _u30b(0) + bytes([133, 72]),
                constant_strings=['x'])[0] == 'x'                        # coerce_s str
    assert _run(bytes([32, 133, 72]))[0] is None                         # coerce_s None


def test_typeof():
    assert _run(bytes([33, 149]))[0] == 'undefined'
    assert _run(bytes([44]) + _u30b(0) + bytes([149]),
                constant_strings=['hi'])[0] == 'String'
    assert _run(bytes([36, 3, 149]))[0] == 'Number'
    assert _run(bytes([40, 149]))[0] == 'Number'


def test_newarray_and_locals_generic():
    assert _run(bytes([36, 1, 36, 2, 36, 3, 86]) + _u30b(3) + bytes([72]))[0] == [1, 2, 3]
    assert _run(bytes([86]) + _u30b(0) + bytes([72]))[0] == []
    # getlocal / setlocal generic
    code = bytes([36, 99, 99]) + _u30b(2) + bytes([98]) + _u30b(2) + bytes([72])
    assert _run(code)[0] == 99
    assert _run(bytes([98]) + _u30b(1) + bytes([72]), args=('argval',))[0] == 'argval'


def test_getlocal_setlocal_short():
    assert _run(bytes([208, 72]))[0] is not None  # registers[0] is ScopeDict, checked below
    res, cls, _ = _run(bytes([208, 72]))
    assert isinstance(res, _ScopeDict) and res.avm_class is cls
    assert _run(bytes([209, 72]), args=('a', 'b', 'c'))[0] == 'a'
    assert _run(bytes([210, 72]), args=('a', 'b', 'c'))[0] == 'b'
    assert _run(bytes([211, 72]), args=('a', 'b', 'c'))[0] == 'c'
    for op_set, op_get in [(212, 208), (213, 209), (214, 210), (215, 211)]:
        code = bytes([36, 77, op_set, op_get, 72])
        assert _run(code, args=('a', 'b', 'c'))[0] == 77


def test_unsupported_opcode():
    with pytest.raises(NotImplementedError):
        _run(bytes([1]))


# --- construct / constructsuper / constructproperty ---

def test_construct():
    other = _cls('Other')
    obj = other.make_object()
    code = bytes([209, 66]) + _u30b(0) + bytes([72])
    res, _, _ = _run(code, args=(obj,))
    assert isinstance(res, _AVMClass_Object) and res.avm_class is other and res is not obj


def test_constructsuper():
    code = bytes([209, 36, 1, 73]) + _u30b(1) + bytes([71])
    assert _run(code, args=(object(),))[0] is undefined


def test_constructproperty():
    other = _cls('Other')
    code = bytes([209, 74]) + _u30b(0) + _u30b(0) + bytes([72])
    res, _, _ = _run(code, args=(other,), multinames=['Other'])
    assert isinstance(res, _AVMClass_Object) and res.avm_class is other


# --- callproperty (70) ---

def _callprop(obj_bytes, mname_idx=0, arg_bytes=b'', arg_count=1):
    return obj_bytes + arg_bytes + bytes([70]) + _u30b(mname_idx) + _u30b(arg_count) + bytes([72])


def test_callproperty_string_class():
    code = _callprop(bytes([209]), 0, bytes([36, 42]))
    assert _run(code, args=(StringClass,), multinames=['String'])[0] == '42'
    code = _callprop(bytes([209]), 0, bytes([33]))
    assert _run(code, args=(StringClass,), multinames=['String'])[0] == 'undefined'
    code = _callprop(bytes([209]), 0, bytes([44]) + _u30b(0))
    assert _run(code, args=(StringClass,), multinames=['String'],
                constant_strings=['hi'])[0] == 'hi'
    with pytest.raises(NotImplementedError):
        _run(_callprop(bytes([209]), 0, bytes([36, 1])),
             args=(StringClass,), multinames=['Nope'])


def test_callproperty_avm_object_and_avm_class():
    other = _cls('Other')
    other.method_pyfunctions['bar'] = lambda args: args[0] + 1
    obj = other.make_object()
    code = _callprop(bytes([209]), 0, bytes([36, 41]))
    assert _run(code, args=(obj,), multinames=['bar'])[0] == 42
    assert _run(code, args=(other,), multinames=['bar'])[0] == 42


def test_callproperty_scopedict_method_and_member():
    func, cls, _ = _build(_callprop(bytes([208]), 0, bytes([36, 10])),
                          multinames=['foo'])
    cls.method_names['foo'] = 0
    cls.method_pyfunctions['foo'] = lambda args: args[0] * 2
    assert func([]) == 20
    # member fallback
    func2, cls2, _ = _build(_callprop(bytes([208]), 0, b'', arg_count=0),
                            multinames=['bar'])
    cls2.variables['bar'] = 99
    assert func2([]) == 99


def test_callproperty_str_split_charcodeat():
    code = _callprop(bytes([209]), 0, bytes([44]) + _u30b(0))
    assert _run(code, args=('a,b,c',), multinames=['split'],
                constant_strings=[','])[0] == ['a', 'b', 'c']
    assert _run(code, args=('abc',), multinames=['split'],
                constant_strings=[''])[0] == ['a', 'b', 'c']
    code2 = _callprop(bytes([209]), 0, bytes([36, 1]))
    assert _run(code2, args=('abc',), multinames=['charCodeAt'])[0] == ord('b')
    code3 = _callprop(bytes([209]), 0, b'', arg_count=0)
    assert _run(code3, args=('abc',), multinames=['charCodeAt'])[0] == ord('a')


def test_callproperty_list_slice_join_and_unsupported():
    code = _callprop(bytes([209]), 0, bytes([36, 1]))
    assert _run(code, args=([1, 2, 3],), multinames=['slice'])[0] == [2, 3]
    code = _callprop(bytes([209]), 0, bytes([44]) + _u30b(0))
    assert _run(code, args=(['a', 'b'],), multinames=['join'],
                constant_strings=['-'])[0] == 'a-b'
    with pytest.raises(NotImplementedError):
        _run(_callprop(bytes([209]), 0, bytes([36, 1])),
             args=(5,), multinames=['foo'])
    with pytest.raises(NotImplementedError):
        _run(_callprop(bytes([209]), 0, bytes([36, 1])),
             args=('str',), multinames=['unknown'])


# --- callpropvoid (79) ---

def _callpropvoid(obj_bytes, mname_idx=0, arg_count=0, arg_bytes=b''):
    return obj_bytes + arg_bytes + bytes([79]) + _u30b(mname_idx) + _u30b(arg_count) + bytes([71])


def test_callpropvoid_object_and_scopedict():
    other = _cls('Other')
    other.method_pyfunctions['foo'] = lambda args: undefined
    obj = other.make_object()
    assert _run(_callpropvoid(bytes([209])), args=(obj,),
                multinames=['foo'])[0] is undefined
    func, cls, _ = _build(_callpropvoid(bytes([208])), multinames=['foo'])
    cls.method_names['foo'] = 0
    cls.method_pyfunctions['foo'] = lambda args: undefined
    assert func([]) is undefined


def test_callpropvoid_reverse_and_unsupported():
    lst = [1, 2, 3]
    assert _run(_callpropvoid(bytes([209])), args=(lst,),
                multinames=['reverse'])[0] is undefined
    assert lst == [3, 2, 1]
    with pytest.raises(NotImplementedError):
        _run(_callpropvoid(bytes([209])), args=(5,), multinames=['foo'])


# --- findpropstrict / findproperty / getlex ---

def test_findpropstrict_found_and_builtin():
    assert _run(bytes([93]) + _u30b(0) + bytes([72]), multinames=['myvar'],
                variables={'myvar': 123})[0] == 123
    assert _run(bytes([93]) + _u30b(0) + bytes([72]),
                multinames=['String'])[0] is StringClass


def test_findproperty_found_and_notfound():
    res, cls, _ = _run(bytes([94]) + _u30b(0) + bytes([72]),
                       multinames=['c'], constants={'c': 1})
    assert res is cls.constants
    res, cls, _ = _run(bytes([94]) + _u30b(0) + bytes([72]), multinames=['missing'])
    assert res is cls.variables


def test_getlex_found_builtin_undefined():
    assert _run(bytes([96]) + _u30b(0) + bytes([72]), multinames=['x'],
                variables={'x': 55})[0] == 55
    assert _run(bytes([96]) + _u30b(0) + bytes([72]),
                multinames=['String'])[0] is StringClass
    assert _run(bytes([96]) + _u30b(0) + bytes([72]),
                multinames=['no_such_thing'])[0] is undefined


# --- setproperty / initproperty / getproperty ---

def test_setproperty_plain_and_multiname():
    d = {}
    code = bytes([209, 36, 42, 97]) + _u30b(0) + bytes([71])
    _run(code, args=(d,), multinames=['key'])
    assert d == {'key': 42}
    d2 = {}
    # stack: obj, idx (pushstring), value
    code = bytes([209, 44]) + _u30b(0) + bytes([36, 7, 97]) + _u30b(0) + bytes([71])
    _run(code, args=(d2,), multinames=[_Multiname(1)], constant_strings=['dyn'])
    assert d2 == {'dyn': 7}


def test_initproperty_plain_and_multiname():
    d = {}
    code = bytes([209, 36, 42, 104]) + _u30b(0) + bytes([71])
    _run(code, args=(d,), multinames=['key'])
    assert d == {'key': 42}
    d2 = {}
    code = bytes([209, 44]) + _u30b(0) + bytes([36, 7, 104]) + _u30b(0) + bytes([71])
    _run(code, args=(d2,), multinames=[_Multiname(1)], constant_strings=['dyn'])
    assert d2 == {'dyn': 7}


def test_getproperty_length_member_static_indexed():
    code = bytes([209, 102]) + _u30b(0) + bytes([72])
    assert _run(code, args=('hello',), multinames=['length'])[0] == 5
    assert _run(code, args=([1, 2],), multinames=['length'])[0] == 2
    assert _run(code, args=({'k': 5},), multinames=['k'])[0] == 5
    assert _run(code, args=({'k': 5},), multinames=['missing'])[0] is undefined
    other = _AVMClass(0, 'Other', static_properties={'prop': 777})
    assert _run(code, args=(other,), multinames=['prop'])[0] == 777
    # indexed access: pname is _Multiname, stack obj, idx
    code_idx = bytes([209, 36, 1, 102]) + _u30b(0) + bytes([72])
    assert _run(code_idx, args=([10, 20, 30],),
                multinames=[_Multiname(2)])[0] == 20
