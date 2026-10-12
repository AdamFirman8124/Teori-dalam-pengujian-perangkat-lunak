import json
from pathlib import Path

p = Path('experiments_codamosa_coverup.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))

def get(i):
    return ''.join(nb['cells'][i]['source'])

def put(i, text):
    nb['cells'][i]['source'] = text.splitlines(keepends=True)

# Add task filtering and resume configuration to setup cell.
s = get(1)
anchor = "TASKS = {name: em.task_ids(name, TASK_LIMIT) for name in DATASETS}"
insert = """TASKS = {name: em.task_ids(name, TASK_LIMIT) for name in DATASETS}
_task_filter_raw = os.getenv('TASK_FILTER', '').strip()
if _task_filter_raw:
    _wanted = set()
    for _piece in _task_filter_raw.replace(';', ',').split(','):
        _piece = _piece.strip()
        if not _piece:
            continue
        if ':' in _piece:
            _ds, _tid = _piece.split(':', 1)
            _wanted.add((_ds.strip(), _tid.strip()))
        else:
            _wanted.add((None, _piece))
    TASKS = {ds: [t for t in tids if (ds, str(t)) in _wanted or (None, str(t)) in _wanted]
             for ds, tids in TASKS.items()}
    TASKS = {ds: tids for ds, tids in TASKS.items() if tids}
    print('TASK_FILTER:', _task_filter_raw, '->', TASKS)
RESUME = os.getenv('RESUME', '0').strip().lower() in {'1', 'true', 'yes'}"""
assert anchor in s
put(1, s.replace(anchor, insert))

# Make Docker preflight/build output decoding safe as well.
for _cell in (3, 4):
    s = get(_cell)
    s = s.replace('capture_output=True,\n        text=True,\n    )',
                  'capture_output=True,\n        text=True, encoding="utf-8", errors="replace",\n    )')
    s = s.replace('capture_output=True, text=True, timeout=',
                  'capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=')
    s = s.replace('capture_output=True,\n            text=True,\n            timeout=',
                  'capture_output=True,\n            text=True, encoding="utf-8", errors="replace",\n            timeout=')
    s = s.replace('(result.stdout + "\\n" + result.stderr)',
                  '((result.stdout or "") + "\\n" + (result.stderr or ""))')
    s = s.replace('result.stdout.strip()', '(result.stdout or "").strip()')
    s = s.replace('result.stderr or result.stdout',
                  '(result.stderr or "") + (result.stdout or "")')
    put(_cell, s)

# Start the task cell with active results when RESUME=1, limited to this run's tasks.
s = get(6)
anchor = "rows = []\nstatuses = []"
insert = """rows = []
statuses = []
RESUME_KEYS = set()
if RESUME:
    _active_rows, _active_statuses = _storage.ResultStore._read_active(OUT)
    _selected = {(ds, str(t)) for ds, tids in TASKS.items() for t in tids}
    rows = [r for r in _active_rows if (r.get('dataset'), str(r.get('task'))) in _selected]
    statuses = [x for x in _active_statuses
                if x.get('status') == 'OK'
                and (x.get('dataset'), str(x.get('task'))) in _selected]
    for _item in statuses:
        if _item.get('status') == 'OK':
            RESUME_KEYS.add((_item.get('method'), _item.get('model'),
                             _item.get('dataset'), str(_item.get('task'))))
    print(f'RESUME=1: loaded {len(rows)} rows and {len(statuses)} statuses.')"""
assert anchor in s
s = s.replace(anchor, insert)
s = s.replace('redact((collect.stdout + "\\n" + collect.stderr)[-3000:])',
              'redact(((collect.stdout or "") + "\\n" + (collect.stderr or ""))[-3000:])')
put(6, s)

# Add helpers and replace the matrix loop with resume-aware execution/checkpoints.
s = get(6)
old = '''# Matrix: method x model x dataset x task. Each model has isolated outputs.
for dataset, task_ids in TASKS.items():
    for task in task_ids:
        if coverup_ok:
            for model in COVERUP_MODELS:
                try:
                    print("CoverUp mencoba model:", model)
                    row = _run_coverup_task_with_model(dataset, task, model)
                    rows.append(row)
                    statuses.append({"method": "CoverUp", "model": model,
                                     "dataset": dataset, "task": str(task),
                                     "status": "OK", "message": "Generation and evaluation completed."})
                    print("CoverUp OK", model, dataset, task)
                except Exception as exc:
                    blocked("CoverUp:" + model, dataset, task, explain_error(exc))
        else:
            for model in COVERUP_MODELS:
                blocked("CoverUp:" + model, dataset, task, coverup_reason)

        if codamosa_ok:
            for model in CODAMOSA_MODELS:
                try:
                    print("CODAMOSA mencoba model:", model)
                    row = _run_codamosa_task_with_model(dataset, task, model)
                    rows.append(row)
                    statuses.append({"method": "CODAMOSA", "model": model,
                                     "dataset": dataset, "task": str(task),
                                     "status": "OK", "message": "Generation and evaluation completed."})
                    print("CODAMOSA OK", model, dataset, task)
                except Exception as exc:
                    blocked("CODAMOSA:" + model, dataset, task, explain_error(exc))
        else:
            for model in CODAMOSA_MODELS:
                blocked("CODAMOSA:" + model, dataset, task, codamosa_reason)'''
new = '''# Matrix: method x model x dataset x task. Each model has isolated outputs.
def _done(method, model, dataset, task):
    return (method, model, dataset, str(task)) in RESUME_KEYS

for dataset, task_ids in TASKS.items():
    for task in task_ids:
        if coverup_ok:
            for model in COVERUP_MODELS:
                if _done("CoverUp", model, dataset, task):
                    print(f"RESUME skip CoverUp {model} {dataset} {task}")
                    continue
                try:
                    print("CoverUp mencoba model:", model)
                    row = _run_coverup_task_with_model(dataset, task, model)
                    rows.append(row)
                    statuses.append({"method": "CoverUp", "model": model,
                                     "dataset": dataset, "task": str(task),
                                     "status": "OK", "message": "Generation and evaluation completed."})
                    print("CoverUp OK", model, dataset, task)
                except Exception as exc:
                    blocked("CoverUp:" + model, dataset, task, explain_error(exc))
        else:
            for model in COVERUP_MODELS:
                if not _done("CoverUp", model, dataset, task):
                    blocked("CoverUp:" + model, dataset, task, coverup_reason)

        if codamosa_ok:
            for model in CODAMOSA_MODELS:
                if _done("CODAMOSA", model, dataset, task):
                    print(f"RESUME skip CODAMOSA {model} {dataset} {task}")
                    continue
                try:
                    print("CODAMOSA mencoba model:", model)
                    row = _run_codamosa_task_with_model(dataset, task, model)
                    rows.append(row)
                    statuses.append({"method": "CODAMOSA", "model": model,
                                     "dataset": dataset, "task": str(task),
                                     "status": "OK", "message": "Generation and evaluation completed."})
                    print("CODAMOSA OK", model, dataset, task)
                except Exception as exc:
                    blocked("CODAMOSA:" + model, dataset, task, explain_error(exc))
        else:
            for model in CODAMOSA_MODELS:
                if not _done("CODAMOSA", model, dataset, task):
                    blocked("CODAMOSA:" + model, dataset, task, codamosa_reason)

        store.checkpoint(rows, statuses)
        print(f"Checkpoint after {dataset} {task}: rows={len(rows)} statuses={len(statuses)}")'''
assert old in s
put(6, s.replace(old, new))

p.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('patched notebook loop')
