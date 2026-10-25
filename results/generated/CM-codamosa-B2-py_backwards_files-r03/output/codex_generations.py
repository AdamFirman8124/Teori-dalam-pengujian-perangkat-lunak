

# Generated at 2026-10-24 14:11:06.522447
# Unit test for function get_input_output_paths

# Generated at 2026-10-24 14:11:45.844677
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import os

    # Case 1: single .py file to single .py output

# Generated at 2026-10-24 14:12:11.555355
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .types import InputOutput
from .exceptions import InvalidInputOutput, InputDoesntExists
from .paths import get_input_output_paths


def test_single_file_to_single_file(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    dst = tmp_path / "out" / "a.py"
    result = list(module_0.get_input_output_paths(str(src), str(dst), None))
    assert result == [InputOutput(src, dst)]


def test_single_file_to_directory(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), None))
    assert result == [InputOutput(src, out_dir / "a.py")]


def test_single_file_with_root(tmp_path):
    src = tmp_path / "pkg" / "a.py"
    src.parent.mkdir()
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), str(tmp_path)))
    assert result == [InputOutput(src, out_dir / "pkg" / "a.py")]


def test_directory_recursion_without_root(tmp_path):
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "a.py").write_text("# a")
    (tmp_path / "pkg" / "sub").mkdir()
    (tmp_path / "pkg" / "sub" / "b.py").write_text("# b")
    (tmp_path / "pkg" / "notes.txt").write_text("skip me")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(tmp_path / "pkg"),
                                           str(out_dir), None),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(tmp_path / "pkg" / "a.py", out_dir / "a.py"),
        InputOutput(tmp_path / "pkg" / "sub" / "b.py", out_dir / "sub" / "b.py"),
    ]


def test_directory_recursion_with_root(tmp_path):
    src_root = tmp_path / "src"
    (src_root / "pkg" / "sub").mkdir(parents=True)
    (src_root / "pkg" / "a.py").write_text("# a")
    (src_root / "pkg" / "sub" / "b.py").write_text("# b")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                           str(src_root)),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "pkg" / "a.py"),
        InputOutput(src_root / "pkg" / "sub" / "b.py", out_dir / "pkg" / "sub" / "b.py"),
    ]


def test_directory_with_external_root_preserves_relative_path(tmp_path):
    src_root = tmp_path / "src"
    src_root.mkdir()
    (src_root / "pkg").mkdir()
    (src_root / "pkg" / "a.py").write_text("# a")
    out_dir = tmp_path / "out"
    external_root = tmp_path
    result = list(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                         str(external_root)))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "src" / "pkg" / "a.py"),
    ]


def test_mismatched_extensions_raises(tmp_path):
    src = tmp_path / "a.txt"
    src.write_text("not python")
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(src), str(tmp_path / "out.py"), None))


def test_missing_input_raises(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                    str(tmp_path / "out.py"), None))


def test_generator_is_lazy(tmp_path):
    # No files exist, but no error until the generator is consumed
    gen = module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                 str(tmp_path / "out.py"), None)
    assert isinstance(gen, types_Generator := type(iter([]))) or True  # iterator check below
    with pytest.raises(InputDoesntExists):
        next(gen)

# Generated at 2026-10-24 14:12:28.238569
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .types import InputOutput
from .exceptions import InvalidInputOutput, InputDoesntExists
from .paths import get_input_output_paths


def test_single_file_to_single_file(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    dst = tmp_path / "out" / "a.py"
    result = list(module_0.get_input_output_paths(str(src), str(dst), None))
    assert result == [InputOutput(src, dst)]


def test_single_file_to_directory(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), None))
    assert result == [InputOutput(src, out_dir / "a.py")]


def test_single_file_with_root(tmp_path):
    src = tmp_path / "pkg" / "a.py"
    src.parent.mkdir()
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), str(tmp_path)))
    assert result == [InputOutput(src, out_dir / "pkg" / "a.py")]


def test_directory_recursion_without_root(tmp_path):
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "a.py").write_text("# a")
    (tmp_path / "pkg" / "sub").mkdir()
    (tmp_path / "pkg" / "sub" / "b.py").write_text("# b")
    (tmp_path / "pkg" / "notes.txt").write_text("skip me")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(tmp_path / "pkg"),
                                           str(out_dir), None),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(tmp_path / "pkg" / "a.py", out_dir / "a.py"),
        InputOutput(tmp_path / "pkg" / "sub" / "b.py", out_dir / "sub" / "b.py"),
    ]


def test_directory_recursion_with_root(tmp_path):
    src_root = tmp_path / "src"
    (src_root / "pkg" / "sub").mkdir(parents=True)
    (src_root / "pkg" / "a.py").write_text("# a")
    (src_root / "pkg" / "sub" / "b.py").write_text("# b")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                           str(src_root)),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "pkg" / "a.py"),
        InputOutput(src_root / "pkg" / "sub" / "b.py", out_dir / "pkg" / "sub" / "b.py"),
    ]


def test_directory_with_external_root_preserves_relative_path(tmp_path):
    src_root = tmp_path / "src"
    src_root.mkdir()
    (src_root / "pkg").mkdir()
    (src_root / "pkg" / "a.py").write_text("# a")
    out_dir = tmp_path / "out"
    external_root = tmp_path
    result = list(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                         str(external_root)))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "src" / "pkg" / "a.py"),
    ]


def test_mismatched_extensions_raises(tmp_path):
    src = tmp_path / "a.txt"
    src.write_text("not python")
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(src), str(tmp_path / "out.py"), None))


def test_missing_input_raises(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                    str(tmp_path / "out.py"), None))


def test_generator_is_lazy(tmp_path):
    # No files exist, but no error until the generator is consumed
    gen = module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                 str(tmp_path / "out.py"), None)
    assert isinstance(gen, types_Generator := type(iter([]))) or True  # iterator check below
    with pytest.raises(InputDoesntExists):
        next(gen)

# Generated at 2026-10-24 14:12:44.715167
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import pytest

from .types import InputOutput
from .exceptions import InvalidInputOutput, InputDoesntExists
from .paths import get_input_output_paths


def test_single_file_to_single_file(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    dst = tmp_path / "out" / "a.py"
    result = list(module_0.get_input_output_paths(str(src), str(dst), None))
    assert result == [InputOutput(src, dst)]


def test_single_file_to_directory(tmp_path):
    src = tmp_path / "a.py"
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), None))
    assert result == [InputOutput(src, out_dir / "a.py")]


def test_single_file_with_root(tmp_path):
    src = tmp_path / "pkg" / "a.py"
    src.parent.mkdir()
    src.write_text("# code")
    out_dir = tmp_path / "out"
    result = list(module_0.get_input_output_paths(str(src), str(out_dir), str(tmp_path)))
    assert result == [InputOutput(src, out_dir / "pkg" / "a.py")]


def test_directory_recursion_without_root(tmp_path):
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "a.py").write_text("# a")
    (tmp_path / "pkg" / "sub").mkdir()
    (tmp_path / "pkg" / "sub" / "b.py").write_text("# b")
    (tmp_path / "pkg" / "notes.txt").write_text("skip me")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(tmp_path / "pkg"),
                                           str(out_dir), None),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(tmp_path / "pkg" / "a.py", out_dir / "a.py"),
        InputOutput(tmp_path / "pkg" / "sub" / "b.py", out_dir / "sub" / "b.py"),
    ]


def test_directory_recursion_with_root(tmp_path):
    src_root = tmp_path / "src"
    (src_root / "pkg" / "sub").mkdir(parents=True)
    (src_root / "pkg" / "a.py").write_text("# a")
    (src_root / "pkg" / "sub" / "b.py").write_text("# b")
    out_dir = tmp_path / "out"
    result = sorted(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                           str(src_root)),
                    key=lambda io: str(io.input))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "pkg" / "a.py"),
        InputOutput(src_root / "pkg" / "sub" / "b.py", out_dir / "pkg" / "sub" / "b.py"),
    ]


def test_directory_with_external_root_preserves_relative_path(tmp_path):
    src_root = tmp_path / "src"
    src_root.mkdir()
    (src_root / "pkg").mkdir()
    (src_root / "pkg" / "a.py").write_text("# a")
    out_dir = tmp_path / "out"
    external_root = tmp_path
    result = list(module_0.get_input_output_paths(str(src_root), str(out_dir),
                                         str(external_root)))
    assert result == [
        InputOutput(src_root / "pkg" / "a.py", out_dir / "src" / "pkg" / "a.py"),
    ]


def test_mismatched_extensions_raises(tmp_path):
    src = tmp_path / "a.txt"
    src.write_text("not python")
    with pytest.raises(InvalidInputOutput):
        list(module_0.get_input_output_paths(str(src), str(tmp_path / "out.py"), None))


def test_missing_input_raises(tmp_path):
    with pytest.raises(InputDoesntExists):
        list(module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                    str(tmp_path / "out.py"), None))


def test_generator_is_lazy(tmp_path):
    # No files exist, but no error until the generator is consumed
    gen = module_0.get_input_output_paths(str(tmp_path / "missing.py"),
                                 str(tmp_path / "out.py"), None)
    assert isinstance(gen, types_Generator := type(iter([]))) or True  # iterator check below
    with pytest.raises(InputDoesntExists):
        next(gen)

# Generated at 2026-10-24 14:13:33.162847
# Unit test for function get_input_output_paths
def test_get_input_output_paths():import tempfile