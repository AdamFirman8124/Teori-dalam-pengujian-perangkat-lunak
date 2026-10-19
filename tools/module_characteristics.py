#!/usr/bin/env python3
"""Extract CM module characteristics required by RQ3 (no dependencies)."""
from __future__ import annotations

import ast
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import eval_metrics as em  # noqa: E402


def _complexity(tree: ast.AST) -> int:
    decisions = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.IfExp,
                 ast.comprehension, ast.Match)
    score = 1 + sum(isinstance(node, decisions) for node in ast.walk(tree))
    score += sum(max(0, len(node.values) - 1) for node in ast.walk(tree)
                 if isinstance(node, ast.BoolOp))
    return score


def _dependencies(tree: ast.AST, own_top_level: str) -> int:
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            imports.add(node.module.split(".")[0])
    return len(imports - {own_top_level})


def _annotation_density(tree: ast.AST) -> float:
    functions = [node for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    slots = annotated = 0
    for fn in functions:
        args = [*fn.args.posonlyargs, *fn.args.args, *fn.args.kwonlyargs]
        if fn.args.vararg:
            args.append(fn.args.vararg)
        if fn.args.kwarg:
            args.append(fn.args.kwarg)
        slots += len(args) + 1  # include return slot
        annotated += sum(arg.annotation is not None for arg in args)
        annotated += fn.returns is not None
    return annotated / slots if slots else 0.0


def main() -> int:
    out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else \
        ROOT / "experiment_results" / "module_characteristics.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for _pkg, module, path in em.cm_modules():
        source = path.read_text(encoding="utf-8", errors="replace")
        try:
            tree = ast.parse(source, filename=str(path))
        except SyntaxError:
            continue
        code_lines = sum(bool(line.strip()) and not line.lstrip().startswith("#")
                         for line in source.splitlines())
        rows.append({"task": module, "loc": code_lines,
                     "cyclomatic_complexity": _complexity(tree),
                     "external_dependencies": _dependencies(tree, module.split(".")[0]),
                     "type_annotation_density": _annotation_density(tree)})
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} CM rows to {out}")
    return 0 if len(rows) == 425 else 1


if __name__ == "__main__":
    raise SystemExit(main())
