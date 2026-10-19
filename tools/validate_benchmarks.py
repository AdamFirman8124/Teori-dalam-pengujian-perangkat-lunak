#!/usr/bin/env python3
"""Validate the exact MT and CM benchmark layouts before an expensive run."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import eval_metrics as em  # noqa: E402

CODAMOSA_REQUIRED_COMMIT = "17a4c2a2ecb40b60e32a7e4a437db03573612f11"


def _git_head(repo: Path) -> str | None:
    try:
        return subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        return None


def validate() -> tuple[dict, list[str]]:
    errors: list[str] = []
    mt_ids = em.task_ids("MT")
    cm_modules = em.cm_modules()
    cm_ids = [module for _pkg, module, _path in cm_modules]
    cm_packages = {Path(pkg).parts[1] for pkg, _module, _path in cm_modules}

    if mt_ids != [f"f{i:03d}" for i in range(1, 164)]:
        errors.append("MT harus tepat 163 task berurutan f001..f163")
    mt_layouts = [em.LAYOUTS["MT"](task) for task in mt_ids]
    if any(not Path(x["put"]).is_file() for x in mt_layouts):
        errors.append("Ada PUT MT yang hilang")
    if any(not Path(x["package_txt"]).is_file() for x in mt_layouts):
        errors.append("Ada package.txt MT yang hilang")

    if len(cm_ids) != 425 or len(set(cm_ids)) != 425:
        errors.append(f"CM harus tepat 425 modul unik, ditemukan {len(cm_ids)}")
    if len(cm_packages) != 24:
        errors.append(f"CM harus tepat 24 package, ditemukan {len(cm_packages)}")
    if any(not path.is_file() for _pkg, _module, path in cm_modules):
        errors.append("Ada sumber modul CM yang hilang")

    codamosa_repo = ROOT / "dataset" / "codamosa"
    codamosa_head = _git_head(codamosa_repo)
    if codamosa_head != CODAMOSA_REQUIRED_COMMIT:
        errors.append(
            "Commit dataset/codamosa tidak sesuai: "
            f"{codamosa_head or 'tidak terdeteksi'} != {CODAMOSA_REQUIRED_COMMIT}"
        )

    coverup_repo = ROOT / "dataset" / "coverup-eval"
    report = {
        "mt": {
            "tasks": len(mt_ids),
            "first": mt_ids[0] if mt_ids else None,
            "last": mt_ids[-1] if mt_ids else None,
            "root": str(em.MT_ROOT_DIR),
        },
        "cm": {
            "modules": len(cm_ids),
            "packages": len(cm_packages),
            "manifest": str(em.CM_ROOT_DIR / "test-apps" / "cm_modules.csv"),
            "codamosa_commit": codamosa_head,
        },
        "coverup_eval_commit": _git_head(coverup_repo),
        "mutap_generation": "excluded; collaborator device",
        "valid": not errors,
        "errors": errors,
    }
    return report, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()
    report, errors = validate()
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"MT: {report['mt']['tasks']} tasks ({report['mt']['first']}..{report['mt']['last']})")
        print(f"CM: {report['cm']['modules']} modules / {report['cm']['packages']} packages")
        print("CodaMOSA commit:", report["cm"]["codamosa_commit"])
        print("MuTAP generation: excluded (collaborator device)")
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
