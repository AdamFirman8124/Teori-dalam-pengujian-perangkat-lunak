#!/usr/bin/env python3
"""Build an interim Word report from an experiment status snapshot."""
from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

try:
    from tools.classify_failures import classify, read_status, summarize
except ModuleNotFoundError:
    from classify_failures import classify, read_status, summarize

ROOT = Path(__file__).resolve().parent.parent
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC = "http://purl.org/dc/elements/1.1/"
DCTERMS = "http://purl.org/dc/terms/"
XSI = "http://www.w3.org/2001/XMLSchema-instance"


def read_rows(path: Path) -> list[dict]:
    if not path.exists() or not path.stat().st_size:
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _num(row: dict, key: str) -> float | None:
    try:
        value = row.get(key)
        return None if value in (None, "") else float(value)
    except (TypeError, ValueError):
        return None


def method_metrics(rows: list[dict]) -> list[list[str]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("method") or "UNKNOWN")].append(row)
    table = [["Metode", "n", "Line coverage", "Pass rate", "Mutation score", "Wall time rata-rata"]]
    for method, items in sorted(grouped.items()):
        values = {}
        for field in ("line_pct", "pass_rate", "mutation_score", "wall_time_s"):
            nums = [value for row in items if (value := _num(row, field)) is not None]
            values[field] = sum(nums) / len(nums) if nums else None
        fmt = lambda value, suffix="": "-" if value is None else f"{value:.2f}{suffix}"
        table.append([
            method, str(len(items)), fmt(values["line_pct"], "%"), fmt(values["pass_rate"], "%"),
            fmt(values["mutation_score"], "%"), fmt(values["wall_time_s"], " s"),
        ])
    return table


def status_table(records: list[dict]) -> list[list[str]]:
    counts: dict[str, Counter] = defaultdict(Counter)
    for record in records:
        counts[str(record.get("method") or "UNKNOWN")][record["failure_category"]] += 1
    categories = ("success", "model_failure", "infrastructure_failure", "unknown_failure")
    rows = [["Metode", "Sukses", "Kegagalan model", "Kegagalan infrastruktur", "Belum terklasifikasi"]]
    for method, counter in sorted(counts.items()):
        rows.append([method] + [str(counter[category]) for category in categories])
    return rows


def _run(text: str, bold: bool = False, italic: bool = False, size: int | None = None) -> str:
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if size:
        props.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def _paragraph(text: str = "", *, bold: bool = False, italic: bool = False, size: int | None = None,
               align: str | None = None, before: int = 0, after: int = 120) -> str:
    ppr = [f'<w:spacing w:before="{before}" w:after="{after}" w:line="276" w:lineRule="auto"/>']
    if align:
        ppr.append(f'<w:jc w:val="{align}"/>')
    return f'<w:p><w:pPr>{"".join(ppr)}</w:pPr>{_run(text, bold, italic, size)}</w:p>'


def _heading(text: str, level: int = 1) -> str:
    size = 32 if level == 1 else 26
    return _paragraph(text, bold=True, size=size, before=240, after=120)


def _bullet(text: str) -> str:
    return (
        '<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
        '<w:spacing w:after="80" w:line="276" w:lineRule="auto"/></w:pPr>'
        f'{_run(text)}</w:p>'
    )


def _cell(text: str, header: bool = False) -> str:
    shade = '<w:shd w:val="clear" w:color="auto" w:fill="D9EAF7"/>' if header else ""
    return f'<w:tc><w:tcPr>{shade}<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar></w:tcPr>{_paragraph(str(text), bold=header, after=0)}</w:tc>'


def _table(rows: list[list[str]]) -> str:
    borders = '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="808080"/><w:left w:val="single" w:sz="4" w:color="808080"/><w:bottom w:val="single" w:sz="4" w:color="808080"/><w:right w:val="single" w:sz="4" w:color="808080"/><w:insideH w:val="single" w:sz="4" w:color="B0B0B0"/><w:insideV w:val="single" w:sz="4" w:color="B0B0B0"/></w:tblBorders>'
    body = []
    for index, row in enumerate(rows):
        body.append(f'<w:tr>{"".join(_cell(value, index == 0) for value in row)}</w:tr>')
    return f'<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>{borders}</w:tblPr>{"".join(body)}</w:tbl>'


def document_xml(parts: list[str]) -> str:
    sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>'
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{W}" xmlns:r="{R}"><w:body>{"".join(parts)}{sect}</w:body></w:document>'


def styles_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr/></w:pPrDefault></w:docDefaults></w:styles>'''


def numbering_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="{W}"><w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="singleLevel"/><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:tabs><w:tab w:val="num" w:pos="720"/></w:tabs><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl></w:abstractNum><w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num></w:numbering>'''


def write_docx(path: Path, parts: list[str], title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'''
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'''
    document_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/></Relationships>'''
    core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="{CP}" xmlns:dc="{DC}" xmlns:dcterms="{DCTERMS}" xmlns:xsi="{XSI}"><dc:title>{escape(title)}</dc:title><dc:creator>Kilo</dc:creator><cp:lastModifiedBy>Kilo</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>'''
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office Word</Application></Properties>'''
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types)
        package.writestr("_rels/.rels", rels)
        package.writestr("word/document.xml", document_xml(parts))
        package.writestr("word/_rels/document.xml.rels", document_rels)
        package.writestr("word/styles.xml", styles_xml())
        package.writestr("word/numbering.xml", numbering_xml())
        package.writestr("docProps/core.xml", core)
        package.writestr("docProps/app.xml", app)


def validate_docx(path: Path) -> None:
    with zipfile.ZipFile(path) as package:
        required = {"[Content_Types].xml", "_rels/.rels", "word/document.xml", "word/styles.xml", "word/numbering.xml"}
        missing = required.difference(package.namelist())
        if missing:
            raise ValueError(f"DOCX missing parts: {sorted(missing)}")
        ET.fromstring(package.read("word/document.xml"))


def build_parts(records: list[dict], rows: list[dict], summary: dict, context: dict) -> list[str]:
    parts = [
        _paragraph("LAPORAN SEMENTARA EKSPERIMEN", bold=True, size=38, align="center", after=100),
        _paragraph("Perbandingan CoverUp dan CodaMOSA sebagai Generator Unit Test Otomatis", bold=True, size=28, align="center", after=160),
        _paragraph(f"Snapshot: {context['snapshot_label']}", italic=True, align="center"),
        _paragraph(f"Dibuat: {datetime.now().strftime('%d-%m-%Y %H:%M')}", align="center", after=300),
        _heading("1. Status Dokumen", 1),
        _paragraph("Dokumen ini merupakan laporan sementara berdasarkan snapshot yang tersedia saat pembuatan laporan. Eksperimen masih berjalan, sehingga angka tidak boleh digunakan sebagai kesimpulan final atau klaim keunggulan metode."),
        _table([
            ["Item", "Nilai"],
            ["Run/snapshot", context["snapshot_label"]],
            ["Status tercatat", str(len(records))],
            ["Baris metrik", str(len(rows))],
            ["Sumber status", context["status_source"]],
            ["Sumber metrik", context["rows_source"]],
        ]),
        _heading("2. Tujuan Eksperimen", 1),
        _paragraph("Eksperimen membandingkan CoverUp dan CodaMOSA dalam menghasilkan unit test Python. Perbandingan diarahkan pada efektivitas pengujian, validitas test yang dihasilkan, mutation score, cakupan kode, tingkat kelulusan test, waktu generasi, dan biaya pemanggilan model."),
        _heading("3. Desain dan Protokol", 1),
        _bullet("Dataset aktif terdiri atas MT sebanyak 163 task dan CM sebanyak 425 task, atau 588 task pipeline."),
        _bullet("Setiap task dijalankan oleh CoverUp dan CodaMOSA, sehingga target keseluruhan adalah 1.176 job metode-task."),
        _bullet("Hasil numerik hanya dicatat untuk job berstatus OK; BLOCKED dan INVALID_GENERATED_TEST tidak diberi skor nol."),
        _bullet("Perbandingan mutation score harus menggunakan mutant_set_id yang sama agar adil."),
        _bullet("Kegagalan model dipertahankan sebagai outcome metode, sedangkan kegagalan infrastruktur harus diulang dan tidak dimasukkan sebagai kegagalan metode."),
        _heading("4. Hasil Snapshot", 1),
        _paragraph("Distribusi status menurut metode:"),
        _table(status_table(records)),
        _paragraph("Ringkasan metrik deskriptif untuk baris yang berhasil:"),
        _table(method_metrics(rows) if rows else [["Metode", "n", "Catatan"], ["-", "0", "Belum ada baris metrik"]]),
    ]

    failures = [record for record in records if record["failure_category"] != "success"]
    parts.extend([_heading("5. Analisis Kegagalan", 1)])
    if not failures:
        parts.append(_paragraph("Snapshot tersimpan yang dianalisis tidak mengandung BLOCKED atau INVALID_GENERATED_TEST. Log konsol pagi hari menunjukkan kegagalan tambahan, tetapi status tersebut belum tersimpan pada snapshot lokal yang tersedia; karena itu kegagalan tersebut dicatat sebagai observasi log, bukan dihitung ke tabel hasil."))
    else:
        failure_rows = [["Metode", "Dataset", "Task", "Status", "Kategori", "Alasan", "Ulang?"]]
        for record in failures:
            failure_rows.append([
                str(record.get("method") or "-"), str(record.get("dataset") or "-"), record["task"], record["status"],
                record["failure_category"], record["failure_reason"], "Ya" if record["recommended_retry"] else "Tidak",
            ])
        parts.append(_table(failure_rows))

    parts.extend([
        _heading("6. Observasi dari Log Konsol Pagi Hari", 1),
        _paragraph("Log yang ditinjau mencapai 132 dari 588 task (22,4%), dengan 259 job OK dan 5 job blocked/invalid. Lima kejadian yang terlihat adalah sebagai berikut:"),
        _table([
            ["Task", "Metode", "Kejadian", "Klasifikasi", "Perlakuan"],
            ["MT f028", "CodaMOSA", "Suite utama tanpa assertion", "Kegagalan model", "Pertahankan sebagai outcome"],
            ["MT f060", "CodaMOSA", "Suite kosong/comment-only", "Kegagalan model", "Pertahankan sebagai outcome"],
            ["MT f086", "CoverUp", "Tidak menghasilkan test", "Kegagalan model", "Pertahankan sebagai outcome"],
            ["MT f121", "CodaMOSA", "Mount /input gagal; tekanan memori", "Kegagalan infrastruktur", "Ulangi setelah perbaikan"],
            ["MT f039", "CodaMOSA", "Docker exit 137/SIGKILL dan rate limit", "Kegagalan infrastruktur", "Ulangi setelah perbaikan"],
        ]),
        _paragraph("Aritmetika log konsisten: 132 task × 2 metode menghasilkan 264 job; 259 OK + 5 blocked/invalid juga berjumlah 264. Namun angka ini belum tersedia di status.json lokal yang dibaca skrip, sehingga tetap harus dikonfirmasi setelah checkpoint tersalin."),
        _heading("7. Temuan yang Layak Masuk Laporan", 1),
        _bullet("Pemisahan kegagalan model dan infrastruktur wajib dilakukan agar perbandingan metode tidak bias."),
        _bullet("INVALID_GENERATED_TEST menunjukkan generator selesai tetapi test tidak memenuhi validitas minimum, misalnya tidak memiliki fungsi test atau assertion."),
        _bullet("Exit code 137/SIGKILL menunjukkan tekanan memori host/WSL/Docker dan bukan bukti kualitas model."),
        _bullet("Rate limit provider dapat menghasilkan respons kosong dan harus diperlakukan sebagai gangguan infrastruktur sementara."),
        _bullet("ETA bersifat dinamis; laju awal tidak stabil karena durasi task, retry, API, dan evaluasi mutan berbeda-beda."),
        _heading("8. Ancaman terhadap Validitas", 1),
        _bullet("Eksperimen belum selesai dan snapshot tersimpan belum memuat seluruh progres yang terlihat di konsol."),
        _bullet("Jumlah keberhasilan per metode dapat menjadi tidak seimbang setelah filtering kegagalan."),
        _bullet("Kegagalan infrastruktur lebih banyak tampak pada CodaMOSA karena penggunaan Docker dan Pynguin; tanpa klasifikasi, hasil dapat merugikan CodaMOSA secara tidak adil."),
        _bullet("Angka rata-rata pada snapshot kecil bersifat deskriptif dan belum mendukung uji statistik atau generalisasi."),
        _heading("9. Rekomendasi Operasional", 1),
        _bullet("Kurangi TASK_WORKERS menjadi 2–3 ketika RAM tersedia turun agar menghindari OOM."),
        _bullet("Periksa quoting dan keberadaan mount /input pada pemanggilan Docker CodaMOSA."),
        _bullet("Gunakan retry dengan backoff untuk rate limit dan kegagalan jaringan, tetapi jangan mengulang suite invalid secara otomatis."),
        _bullet("Setelah run selesai, jalankan classify_failures.py, post_run.py, rescore_existing.py, dan rq_tables.py."),
        _heading("10. Kesimpulan Sementara", 1),
        _paragraph("Pipeline mampu melanjutkan run melalui mekanisme resume dan mengisolasi kegagalan per task. Berdasarkan log sementara, mayoritas job berhasil, tetapi ditemukan kegagalan validitas suite serta gangguan memori, Docker mount, dan rate limit. Belum dapat disimpulkan apakah CoverUp atau CodaMOSA lebih unggul sebelum seluruh task selesai, kegagalan infrastruktur diulang, dan analisis statistik dilakukan pada pasangan task yang sebanding."),
        _heading("Lampiran A. Perintah Analisis", 1),
        _paragraph(".venv\\Scripts\\python.exe tools\\classify_failures.py --source experiment_results"),
        _paragraph(".venv\\Scripts\\python.exe tools\\post_run.py --source experiment_results"),
        _paragraph(".venv\\Scripts\\python.exe tools\\rq_tables.py experiment_results\\rows.csv experiment_results\\paper_tables"),
        _heading("Lampiran B. Definisi Klasifikasi", 1),
        _table([
            ["Kategori", "Contoh", "Masuk success rate metode?", "Diulang?"],
            ["Kegagalan model", "Suite kosong, tanpa assertion, tidak menghasilkan test", "Ya, sebagai kegagalan", "Tidak otomatis"],
            ["Kegagalan infrastruktur", "OOM, mount Docker, rate limit, network", "Tidak", "Ya"],
            ["Belum terklasifikasi", "Pesan baru yang belum dikenali", "Ditahan", "Audit manual"],
        ]),
    ])
    return parts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--snapshot-label")
    args = parser.parse_args()

    status_path = Path(args.status)
    rows_path = Path(args.rows)
    records = [classify(item) for item in read_status(status_path)]
    rows = read_rows(rows_path)
    label = args.snapshot_label or status_path.parent.name
    summary = summarize(records, status_path, label)
    context = {
        "snapshot_label": label,
        "status_source": str(status_path.resolve()),
        "rows_source": str(rows_path.resolve()),
    }
    output = Path(args.output)
    write_docx(output, build_parts(records, rows, summary, context), "Laporan Sementara Eksperimen CoverUp dan CodaMOSA")
    validate_docx(output)
    print(f"DOCX created: {output.resolve()}")
    print(f"Rows: {len(rows)} | statuses: {len(records)} | categories: {summary['category_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
