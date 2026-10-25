

# Generated at 2026-10-25 01:19:42.935379
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:19:49.584125
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:19:50.921597
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:19:52.266583
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:19:54.779810
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:19:57.299303
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:19:59.708233
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:02.120624
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:04.534388
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:06.948065
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:09.361922
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:11.776422
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:14.353866
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:16.771827
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:19.185767
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:21.600816
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:22.924644
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:24.249471
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:25.594807
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:26.923123
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:28.266158
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:29.648378
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:30.970778
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:32.293338
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:33.623715
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:35.055317
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:36.398800
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:37.734114
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:39.153238
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:40.501257
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:41.899096
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:43.223304
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:44.562941
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:45.888011
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:47.220549
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:48.547350
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:49.905244
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:51.231926
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:52.556275
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:53.870728
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:20:55.185205
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:20:57.602915
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:00.018827
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:02.432784
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:04.847813
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:07.265342
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:09.682470
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:12.109405
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:14.513424
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:16.928693
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:19.343579
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:21.760543
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:24.174676
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:26.589178
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:29.006354
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:31.422905
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:52.023530
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():tree = ast.parse("x = str(1)")

# Generated at 2026-10-25 01:21:54.427468
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:55.776072
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:21:57.154704
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:21:58.618793
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:21:59.949971
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:01.323217
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:02.699638
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:04.027651
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:05.378748
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:06.807119
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:08.240985
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:09.573122
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:11.005377
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:12.331760
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:13.770275
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:15.202962
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:16.657410
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:17.981931
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:19.304220
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:20.731942
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:22.062260
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:23.502872
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:26.141093
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:28.556958
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:30.971294
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:47.446166
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():transformer = StringTypesTransformer()

# Generated at 2026-10-25 01:22:48.776519
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:50.213483
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:51.546781
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:52.877985
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:54.223295
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:55.612790
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:56.968034
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:22:58.310622
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:22:59.768669
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:01.104187
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:02.454695
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:03.783765
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:05.181683
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:06.534375
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:07.975021
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:09.300254
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:11.066398
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:12.445124
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:14.973878
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:17.389533
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:19.909285
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:22.326326
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:24.902608
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:27.317177
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:29.731401
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:32.146844
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:34.561468
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:36.977264
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:38.373512
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:39.763127
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:41.096256
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:42.422035
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:43.788021
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:45.105468
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:46.467893
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:47.819444
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:49.150431
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:50.499494
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:51.817179
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:55.915383
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:57.249273
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:23:58.583475
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:23:59.911976
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:24:01.292303
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:02.671041
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:24:04.028786
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:05.381577
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:24:06.710085
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:08.034730
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:24:09.364931
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:10.690292
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:24:12.249404
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:14.667139
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:17.176266
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:19.714347
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:22.129279
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:24.543257
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:26.958313
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:29.373411
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:31.789057
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:34.364215
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:36.777805
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:39.192172
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:47.751841
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:50.172211
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:52.585362
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:54.999716
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:57.414150
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:24:59.830644
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:02.246132
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:04.660265
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:25.053910
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():transformer = StringTypesTransformer()

# Generated at 2026-10-25 01:25:26.406147
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:27.727014
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:29.055198
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:30.431667
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:31.753866
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:33.084913
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:34.422474
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:35.743820
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:37.109726
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:38.436423
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:39.773038
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:41.100690
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:25:43.640086
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:46.054842
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:25:48.590351
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:02.506216
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:04.923146
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:07.339342
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:09.753734
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:11.441213
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:12.777761
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:14.410524
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:15.738794
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:17.068703
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:18.391208
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:19.710210
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:21.050372
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:22.372378
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:23.718590
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:25.049927
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:26.387201
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:27.715100
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:29.051503
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:30.370228
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:26:31.697900
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:26:33.052877
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:03.214047
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:05.627813
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:08.042288
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:10.456548
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:12.872144
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:15.288008
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:16.660584
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:17.978422
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:19.311747
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:20.644529
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:21.996342
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:23.314969
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:24.673333
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:26.019630
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:27.344536
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:28.667618
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:29.986956
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:31.304902
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:32.636989
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:34.079420
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:27:35.400311
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:27:36.724129
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:31.733762
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:33.116722
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:34.446638
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:35.777422
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:37.129887
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:38.487802
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:39.847260
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:41.165834
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:42.497711
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:43.880715
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:45.205652
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:46.576960
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:47.972853
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:49.341737
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:50.656118
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:52.004093
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:53.326561
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:54.653805
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

# Generated at 2026-10-25 01:28:55.981589
# Unit test for constructor of class StringTypesTransformer

# Generated at 2026-10-25 01:28:57.367879
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("x = str(123)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.exceptions == []

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names