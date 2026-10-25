from pathlib import Path
import tempfile
import subprocess
import pytest
import typing as T
import sys
import json
import os
from .utils import subprocess_run


async def measure_test_coverage(*, test: str, tests_dir: Path, pytest_args='',
                                log_write=None, isolate_tests=False, branch_coverage=True):
    """Runs a given test and returns the coverage obtained."""
    fd, test_path = tempfile.mkstemp(prefix="tmp_test_", suffix='.py', dir=str(tests_dir), text=True)
    os.close(fd)
    try:
        Path(test_path).write_text(test, encoding='utf-8')
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as j:
            try:
                # -qq to cut down on tokens
                p = await subprocess_run([sys.executable, '-m', 'slipcover',  *(('--branch',) if branch_coverage else ()),
                                          '--json', '--out', j.name,
                                          '-m', 'pytest', *pytest_args.split(),
                                          *(('--isolate',) if isolate_tests else ()),
                                          '-qq', '-x', '--disable-warnings', test_path],
                                         check=True, timeout=60)
                if log_write:
                    log_write(str(p.stdout, 'UTF-8', errors='ignore'))

                # not checking for JSON errors here because if pytest aborts, its RC ought to be !=0
                cov = json.loads(Path(j.name).read_text())
            finally:
                j.close()
                try:
                    os.unlink(j.name)
                except FileNotFoundError:
                    pass
    finally:
        try:
            os.unlink(test_path)
        except FileNotFoundError:
            pass

    return cov


def measure_suite_coverage(*, tests_dir: Path, source_dir: T.Optional[Path], pytest_args='',
                           trace=None, isolate_tests=False, branch_coverage=True):
    """Runs an entire test suite and returns the coverage obtained."""

    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as j:
        try:
            command = [sys.executable,
                       '-m', 'slipcover',
                             *(('--source', source_dir) if source_dir else ()),
                             *(('--branch',) if branch_coverage else ()),
                             '--json', '--out', j.name,
                       '-m', 'pytest', *pytest_args.split(), *(('--isolate',) if isolate_tests else ()),
                             '--disable-warnings', '-x', tests_dir]

            if trace: trace(command)
            env = os.environ.copy()
            if os.name == "nt":
                env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
            p = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
            if p.returncode not in (pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED):
                if trace: trace(f"tests rc={p.returncode}\n" + str(p.stdout, 'utf-8'))
                p.check_returncode()

            try:
                return json.load(j)
            except json.decoder.JSONDecodeError:
                # The JSON is broken, so pytest's execution likely aborted (e.g. a Python unhandled exception).
                p.check_returncode() # this will almost certainly raise an exception. If not, we do it ourselves:
                raise subprocess.CalledProcessError(p.returncode, command, output=p.stdout)
        finally:
            j.close()

            try:
                os.unlink(j.name)
            except FileNotFoundError:
                pass
