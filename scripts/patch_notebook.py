import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

p = ROOT / 'experiments_codamosa_coverup.ipynb'
nb = json.loads(p.read_text(encoding='utf-8'))

# Replace the destructive output cleanup with candidate-run storage.
s = ''.join(nb['cells'][1]['source'])
old = """OUT = ROOT / 'experiment_results'
CLEAR_OLD_OUTPUTS = os.getenv('CLEAR_OLD_OUTPUTS', '1').strip().lower() not in {'0', 'false', 'no'}
if CLEAR_OLD_OUTPUTS and OUT.exists():
    print('Clearing old experiment outputs:', OUT)
    shutil.rmtree(OUT)
OUT.mkdir(parents=True, exist_ok=True)"""
new = """OUT = ROOT / 'experiment_results'
OUT.mkdir(parents=True, exist_ok=True)
import experiment_storage as _storage
store = _storage.ResultStore(OUT)
store.begin(os.getenv('RUN_LABEL', 'manual'))
print('Run candidate dir:', store.candidate)
if os.getenv('FRESH', '0').strip().lower() in {'1', 'true', 'yes'}:
    print('FRESH requested; active results are still retained and will be backed up on promote.')"""
assert old in s
nb['cells'][1]['source'] = (s.replace(old, new)).splitlines(keepends=True)

# Make all captured subprocess bytes decode predictably on Windows.
for i in (3, 6):
    s = ''.join(nb['cells'][i]['source'])
    s = s.replace('capture_output=True, text=True, timeout=',
                  'capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=')
    s = s.replace('capture_output=True,\n                text=True,\n                timeout=',
                  'capture_output=True,\n                text=True,\n                encoding="utf-8",\n                errors="replace",\n                timeout=')
    nb['cells'][i]['source'] = s.splitlines(keepends=True)

# Avoid concatenating None when a process times out or emits undecodable output.
s = ''.join(nb['cells'][6]['source'])
s = s.replace('redact(exc.stdout or exc.stderr or "")',
              'redact((exc.stdout or "") + (exc.stderr or ""))')
s = s.replace('(result.stdout + "\\n" + result.stderr)',
              '((result.stdout or "") + "\\n" + (result.stderr or ""))')
nb['cells'][6]['source'] = s.splitlines(keepends=True)

# Final writes go through the safe candidate -> backup -> active promotion path.
s = ''.join(nb['cells'][8]['source'])
old = '''(OUT / "status.json").write_text(
    json.dumps(statuses, indent=2, ensure_ascii=False), encoding="utf-8"
)
if rows:
    columns = sorted({key for row in rows for key in row})
    with (OUT / "rows.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
else:
    (OUT / "rows.csv").write_text("", encoding="utf-8")'''
new = '''expected_statuses = sum(len(task_ids) for task_ids in TASKS.values()) * (len(COVERUP_MODELS) + len(CODAMOSA_MODELS))
manifest = store.finalize(rows, statuses, expected_statuses=expected_statuses)
print("Run manifest:", json.dumps(manifest, indent=2, ensure_ascii=False))
if not manifest["promoted"]:
    print("Active results preserved; inspect candidate:", store.candidate)'''
assert old in s
nb['cells'][8]['source'] = s.replace(old, new).splitlines(keepends=True)

p.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('patched notebook')
