import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
nb_path = ROOT / "experiments_codamosa_coverup.ipynb"
env_path = ROOT / "config" / ".env.example"
nb = json.loads(nb_path.read_text(encoding="utf-8"))
def cell(cid):
    return next(c for c in nb["cells"] if c.get("id") == cid)
def source(c):
    return "".join(c["source"])
def set_source(c, value):
    c["source"] = value.splitlines(keepends=True)
setup = cell("c5d09b00")
s = source(setup).replace("os.getenv('TASK_LIMIT', '1')", "os.getenv('TASK_LIMIT', 'all')")
s = s.replace(
    "CODAMOSA_POPULATION = int(os.getenv('CODAMOSA_POPULATION', '50'))",
    "CODAMOSA_POPULATION = int(os.getenv('CODAMOSA_POPULATION', '5'))",
    1,
)
# Setup configuration is maintained directly in the notebook. Do not insert
# parallelism configuration here: repeated patch runs must remain idempotent.
set_source(setup, s if s.endswith("\n") else s + "\n")
task = cell("4ce9652a")
s = source(task)
marker = "# Matrix: method x model x dataset x task. Each model has isolated outputs."
head = s[:s.index(marker)]

# Retry belongs at the task boundary in parallel_loop_body.py. Keep each helper
# to one generator invocation so GENERATOR_ATTEMPTS is a true global bound,
# rather than accidentally multiplying nested retry loops.
old_coverup_retry = '''    result = None
    for attempt in range(1, GENERATOR_ATTEMPTS + 1):
        result = em.run_coverup(
            Path(layout["put"]), work / "tests", work,
            model=model, timeout=COVERUP_TIMEOUT,
        )
        if result.ok and result.generated_tests:
            break
        if attempt < GENERATOR_ATTEMPTS:
            print(f"CoverUp {model} {dataset} {task}: attempt {attempt} gagal; retry.")
            time.sleep(GENERATOR_RETRY_SECONDS * attempt)
'''
new_coverup_call = '''    result = em.run_coverup(
        Path(layout["put"]), work / "tests", work,
        model=model, timeout=COVERUP_TIMEOUT,
    )
'''
if old_coverup_retry in head:
    head = head.replace(old_coverup_retry, new_coverup_call, 1)

old_codamosa_retry = '''        result = None
        for attempt in range(1, GENERATOR_ATTEMPTS + 1):
            if attempt > 1:
                shutil.rmtree(output, ignore_errors=True)
                output.mkdir(parents=True)
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=CODAMOSA_SEARCH_SECONDS + 600,
                )
            except subprocess.TimeoutExpired as exc:
                if attempt == GENERATOR_ATTEMPTS:
                    raise RuntimeError(
                        "CODAMOSA container timeout.\\n" + redact((exc.stdout or "") + (exc.stderr or ""))
                    ) from exc
                print(f"CODAMOSA {model} {dataset} {task}: timeout attempt {attempt}; retry.")
                time.sleep(GENERATOR_RETRY_SECONDS * attempt)
                continue
            if result.returncode == 0:
                break
            combined = (result.stdout or "") + "\\n" + (result.stderr or "")
            transient = any(marker in combined.lower() for marker in (
                "temporary failure in name resolution", "failed to resolve",
                "connectionerror", "timeout", "timed out", "service unavailable",
            ))
            if not transient or attempt == GENERATOR_ATTEMPTS:
                break
            print(f"CODAMOSA {model} {dataset} {task}: network attempt {attempt} gagal; retry.")
            time.sleep(GENERATOR_RETRY_SECONDS * attempt)
        if result is None:
            raise RuntimeError("CODAMOSA tidak menghasilkan process result.")
'''
new_codamosa_call = '''        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=CODAMOSA_SEARCH_SECONDS + 600,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(
                "CODAMOSA container timeout.\\n"
                + redact((exc.stdout or "") + (exc.stderr or ""))
            ) from exc
'''
if old_codamosa_retry in head:
    head = head.replace(old_codamosa_retry, new_codamosa_call, 1)

body = Path(ROOT / "src" / "parallel_loop_body.py").read_text(encoding="utf-8")
driver = Path(ROOT / "src" / "parallel_loop_driver.py").read_text(encoding="utf-8")
set_source(task, head + body.rstrip() + "\n\n\n" + driver.rstrip() + "\n")
env = env_path.read_text(encoding="utf-8")
env = env.replace("CODAMOSA_SEARCH_SECONDS=15", "CODAMOSA_SEARCH_SECONDS=60")
env = env.replace("EVAL_MUTANT_LIMIT=25", "EVAL_MUTANT_LIMIT=0")
env = env.replace("EVAL_MUTANT_WORKERS=6", "EVAL_MUTANT_WORKERS=3")
env = env.replace("# Gunakan 1 untuk pilot, lalu None/all untuk full run.\nTASK_LIMIT=1",
                  "# Full run by default; set TASK_LIMIT=1 for a pilot.\nTASK_LIMIT=all")
if "TASK_WORKERS=" not in env:
    env = env.replace("EVAL_MUTANT_WORKERS=3\n", "EVAL_MUTANT_WORKERS=3\nTASK_WORKERS=2\n")
env_path.write_text(env, encoding="utf-8")
nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("parallel notebook patch applied")

print("setup patched, head chars:", len(head))
