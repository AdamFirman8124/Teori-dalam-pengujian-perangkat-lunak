import zipfile
from xml.etree import ElementTree as ET

from tools.build_interim_report import build_parts, validate_docx, write_docx


def test_builds_valid_docx(tmp_path):
    records = [{
        "method": "CoverUp",
        "model": "openai/auto",
        "dataset": "MT",
        "task": "f001",
        "status": "success",
        "failure_category": "success",
        "failure_reason": "OK",
        "matched_marker": "",
        "recommended_retry": False,
        "message": "done",
    }]
    rows = [{
        "method": "CoverUp",
        "line_pct": "100",
        "pass_rate": "100",
        "mutation_score": "80",
        "wall_time_s": "12.5",
    }]
    context = {
        "snapshot_label": "test-run",
        "status_source": "status.json",
        "rows_source": "rows.csv",
    }
    output = tmp_path / "report.docx"
    parts = build_parts(records, rows, {}, context)
    write_docx(output, parts, "Test report")
    validate_docx(output)

    with zipfile.ZipFile(output) as package:
        document = package.read("word/document.xml")
    ET.fromstring(document)
    assert b"CoverUp" in document
    assert b"Kesimpulan Sementara" in document
