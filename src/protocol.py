from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "experiment.toml"


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def require_environment(config: dict[str, Any]) -> None:
    missing = []
    for backbone in config["backbones"].values():
        for key in ("base_url_env", "api_key_env"):
            name = backbone[key]
            if not os.environ.get(name):
                missing.append(name)
    if missing:
        raise RuntimeError("Missing required environment variables: " + ", ".join(sorted(set(missing))))


def resolve_path(value: str) -> Path:
    return (ROOT / value).resolve()
