# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow==12.0.0"]
# ///
"""Render reproducible OPA1 walkthrough panels from published JUMP_rr extracts.

The panels replace historical SLC2A2/MYT1 tutorial screenshots in the talk.
They are static views of the public table rows, not screenshots of a private
session and not new statistical analyses.  Preview JPEGs are downloaded from
the URLs embedded in the published tables and cached with hashes.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import ssl
from datetime import datetime, timezone
from pathlib import Path
import urllib.request

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "demo" / "tutorial-opa1"
OUT = ROOT / "assets" / "opa1-tutorial-screenshots"
PREVIEWS = DATA / "previews"
PROVENANCE = ROOT / "docs" / "opa1-tutorial-screenshots-provenance.json"

WIDTH, HEIGHT = 1800, 1000
NAVY = "#073B5C"
NAVY_2 = "#0B5676"
TEAL = "#008C95"
CORAL = "#E5534B"
GREEN = "#2A9D70"
GOLD = "#D99A24"
INK = "#172A36"
MUTED = "#5D6D78"
LINE = "#D6E0E6"
PALE = "#F4F7F9"
PALE_BLUE = "#E9F4F7"
WHITE = "#FFFFFF"

FONT_PATH = "/nix/store/zdxpbxr8s3npw71icfxx7x230vsqil0h-dejavu-fonts-minimal-2.37/share/fonts/truetype/DejaVuSans.ttf"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


F14 = font(14)
F16 = font(16)
F18 = font(18)
F20 = font(20)
F22 = font(22)
F24 = font(24)
F26 = font(26)
F28 = font(28)
F32 = font(32)
F40 = font(40)
F48 = font(48)


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def canvas(title: str, subtitle: str, section: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, WIDTH, 112), fill=NAVY)
    draw.rectangle((0, 112, WIDTH, 120), fill=TEAL)
    draw.rectangle((34, 26, 43, 86), fill=CORAL)
    draw.text((64, 22), title, fill=WHITE, font=F40, stroke_width=1)
    draw.text((65, 74), subtitle, fill="#D9EDF3", font=F20)
    badge_w = max(220, int(draw.textlength(section, font=F18)) + 42)
    draw.rounded_rectangle((WIDTH - badge_w - 36, 34, WIDTH - 36, 80), radius=18, fill=NAVY_2, outline="#7FC2D3", width=2)
    draw.text((WIDTH - badge_w - 15, 47), section, fill=WHITE, font=F18)
    draw.text((42, HEIGHT - 42), "Published JUMP_rr rows · OPA1 · prepared 10 Nov 2026", fill=MUTED, font=F16)
    return image, draw


def text_fit(draw: ImageDraw.ImageDraw, text: str, max_width: int, face: ImageFont.FreeTypeFont) -> str:
    text = str(text)
    if draw.textlength(text, font=face) <= max_width:
        return text
    while text and draw.textlength(text + "…", font=face) > max_width:
        text = text[:-1]
    return text + "…"


def card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, fill: str = WHITE, outline: str = LINE, radius: int = 18, width: int = 2) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chip(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, value: str, *, color: str = TEAL) -> int:
    label_w = int(draw.textlength(label, font=F18))
    value_w = int(draw.textlength(value, font=F20))
    width = label_w + value_w + 76
    draw.rounded_rectangle((x, y, x + width, y + 48), radius=14, fill=WHITE, outline=color, width=2)
    draw.text((x + 18, y + 13), label, fill=MUTED, font=F18)
    draw.text((x + 38 + label_w, y + 11), value, fill=INK, font=F20, stroke_width=1)
    return x + width + 14


def table(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    headers: list[str],
    rows: list[list[str]],
    widths: list[float],
    *,
    row_height: int = 74,
    header_height: int = 62,
    highlight_columns: set[int] | None = None,
    highlight_rows: set[int] | None = None,
) -> None:
    x0, y0, x1, y1 = box
    total = x1 - x0
    cols = [int(total * fraction) for fraction in widths]
    cols[-1] += total - sum(cols)
    card(draw, box, radius=12)
    draw.rectangle((x0 + 1, y0 + 1, x1 - 1, y0 + header_height), fill=NAVY_2)
    x = x0
    for i, (header, col_w) in enumerate(zip(headers, cols)):
        draw.text((x + 12, y0 + 19), text_fit(draw, header, col_w - 24, F18), fill=WHITE, font=F18)
        if highlight_columns and i in highlight_columns:
            draw.rectangle((x + 2, y0 + 2, x + col_w - 2, min(y1 - 2, y0 + header_height + len(rows) * row_height - 2)), outline=CORAL, width=4)
        x += col_w
    for row_i, row in enumerate(rows):
        top = y0 + header_height + row_i * row_height
        if top + row_height > y1:
            break
        fill = PALE_BLUE if highlight_rows and row_i in highlight_rows else (WHITE if row_i % 2 == 0 else PALE)
        draw.rectangle((x0 + 1, top, x1 - 1, top + row_height), fill=fill)
        x = x0
        for value, col_w in zip(row, cols):
            draw.text((x + 12, top + 23), text_fit(draw, value, col_w - 24, F18), fill=INK, font=F18)
            draw.line((x, top, x, top + row_height), fill=LINE, width=1)
            x += col_w
        draw.line((x0, top + row_height, x1, top + row_height), fill=LINE, width=1)


def parse_image(cell: str) -> str:
    payload = json.loads(cell)
    return payload["img_src"]


preview_records: dict[str, dict[str, object]] = {}


def get_preview(url: str) -> Image.Image:
    digest = hashlib.sha256(url.encode()).hexdigest()[:20]
    suffix = Path(url.split("?", 1)[0]).suffix or ".jpg"
    target = PREVIEWS / f"{digest}{suffix}"
    if not target.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "jump-hub-slides/2026-11-10"})
        context = ssl.create_default_context(cafile="/etc/ssl/certs/ca-certificates.crt")
        with urllib.request.urlopen(request, timeout=60, context=context) as response:
            target.write_bytes(response.read())
    raw = target.read_bytes()
    preview_records[url] = {
        "path": str(target.relative_to(ROOT)),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
    }
    return Image.open(io.BytesIO(raw)).convert("RGB")


def paste_cover(base: Image.Image, source: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    tw, th = x1 - x0, y1 - y0
    scale = max(tw / source.width, th / source.height)
    resized = source.resize((round(source.width * scale), round(source.height * scale)), Image.Resampling.LANCZOS)
    left = max(0, (resized.width - tw) // 2)
    top = max(0, (resized.height - th) // 2)
    base.paste(resized.crop((left, top, left + tw, top + th)), (x0, y0))


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, optimize=True)


def render_availability() -> None:
    rows = read_csv("availability-opa-prefix.csv")
    image, draw = canvas("Available genes", "Search the OPA prefix, then choose the intended gene", "GENE COVERAGE")
    draw.text((76, 160), "Search", fill=MUTED, font=F20)
    card(draw, (74, 196, 1726, 272), fill=PALE)
    draw.text((104, 217), "OPA", fill=INK, font=F28, stroke_width=1)
    draw.rounded_rectangle((1578, 207, 1698, 261), radius=12, fill=TEAL)
    draw.text((1604, 222), "Apply", fill=WHITE, font=F20)
    draw.rounded_rectangle((64, 186, 1736, 282), radius=14, outline=CORAL, width=4)
    headers = ["Gene", "CRISPR", "ORF", "A549", "HeLa DMEM", "HeLa HPLM", "Lacoste"]
    values = [[row["Gene"], row["CRISPR"], row["ORF"], row["A549"], row["HeLa_DMEM"], row["HeLa_HPLM"], row["Lacoste"]] for row in rows]
    table(draw, (74, 322, 1726, 650), headers, values, [0.24, 0.12, 0.12, 0.12, 0.14, 0.14, 0.12], row_height=84, highlight_columns={1, 2}, highlight_rows={0})
    card(draw, (74, 700, 826, 870), fill=PALE_BLUE, outline=TEAL)
    draw.text((112, 730), "Choose OPA1", fill=NAVY, font=F28, stroke_width=1)
    draw.text((112, 780), "CRISPR 1 · ORF 1", fill=INK, font=F32)
    draw.text((112, 830), "Target for this workflow", fill=MUTED, font=F20)
    card(draw, (866, 700, 1726, 870), fill=WHITE)
    draw.text((908, 730), "Carry its exact reagent IDs forward", fill=NAVY, font=F26, stroke_width=1)
    draw.text((908, 786), "CRISPR", fill=MUTED, font=F20)
    draw.text((1080, 780), "JCP2022_804796", fill=INK, font=F26)
    draw.text((908, 832), "ORF", fill=MUTED, font=F20)
    draw.text((1080, 826), "JCP2022_906243", fill=INK, font=F26)
    save(image, "01-availability.png")


def render_columns() -> None:
    row = read_csv("crispr-features.csv")[0]
    image, draw = canvas("CRISPR feature ranking", "The fields needed to interpret one OPA1 result", "COLUMN GUIDE")
    labels = [
        ("JCP2022", "Exact perturbation reagent"),
        ("Compartment", "CellProfiler object: Cells, Cytoplasm or Nuclei"),
        ("Feature + channel", "Measured morphology and image channel"),
        ("Feature significance", "Per-feature corrected p-value"),
        ("Cohen's d", "Signed effect size versus controls"),
    ]
    y = 166
    for label, definition in labels:
        card(draw, (70, y, 720, y + 116), fill=PALE if (y // 116) % 2 else WHITE)
        draw.text((100, y + 22), label, fill=NAVY, font=F24, stroke_width=1)
        draw.text((100, y + 65), definition, fill=MUTED, font=F18)
        y += 132
    draw.text((782, 162), "Example OPA1 row", fill=NAVY, font=F28, stroke_width=1)
    card(draw, (774, 204, 1728, 864), fill=WHITE)
    pairs = [
        ("Perturbation", row["Perturbation"]),
        ("JCP2022", row["JCP2022"]),
        ("Compartment", row["Compartment"]),
        ("Feature", row["Feature"] + row["Suffix"]),
        ("Channel", row["Channel"]),
        ("Feature significance", row["Feature significance"] + " (rounded)"),
        ("Cohen's d", row["Cohen's d"]),
        ("Feature rank", row["Feature Rank"]),
    ]
    y = 244
    for i, (label, value) in enumerate(pairs):
        draw.rectangle((810, y, 1694, y + 64), fill=PALE_BLUE if i in (3, 4, 6) else (WHITE if i % 2 == 0 else PALE))
        draw.text((836, y + 18), label, fill=MUTED, font=F18)
        draw.text((1120, y + 15), text_fit(draw, value, 540, F20), fill=INK, font=F20, stroke_width=1 if i in (3, 6) else 0)
        y += 70
    draw.rounded_rectangle((1088, 514, 1682, 586), radius=12, outline=CORAL, width=4)
    save(image, "02-columns.png")


def render_filters() -> None:
    image, draw = canvas("Filter the table for OPA1", "Use the official symbol or one of the published synonyms", "FILTERS")
    panels = [
        ("Exact symbol", "Perturbation", "=", "OPA1", "31 CRISPR feature rows"),
        ("Known synonym", "Synonyms", "contains", "MGM1", "the same OPA1 rows"),
        ("Add an object filter", "Compartment", "in", "Cytoplasm, Nuclei", "27 OPA1 rows"),
    ]
    y = 168
    for i, (name, column, op, value, result) in enumerate(panels):
        card(draw, (74, y, 1726, y + 206), fill=WHITE, outline=TEAL if i == 0 else LINE)
        draw.text((104, y + 24), name, fill=NAVY, font=F24, stroke_width=1)
        x = 104
        x = chip(draw, x, y + 78, "Column", column)
        x = chip(draw, x, y + 78, "Operator", op, color=GOLD)
        x = chip(draw, x, y + 78, "Value", value, color=CORAL)
        draw.rounded_rectangle((1470, y + 74, 1688, y + 132), radius=12, fill=TEAL)
        draw.text((1532, y + 91), "Apply", fill=WHITE, font=F20)
        draw.text((104, y + 154), "Result: " + result, fill=GREEN, font=F20, stroke_width=1)
        y += 226
    draw.text((106, 862), "OPA1 synonyms in JUMP_rr: BERHS · MGM1 · MTDPS14 · NPG · NTG · largeG", fill=MUTED, font=F20)
    save(image, "03-filters.png")


def render_gallery() -> None:
    rows = read_csv("crispr-images-and-controls.csv")
    treated = next(row for row in rows if row["Perturbation"] == "OPA1" and row["Plate"] == "CP-CC9-R1-06")
    image, draw = canvas("CRISPR Gallery · OPA1", "Identify the source, plate and treatment well before choosing controls", "IMAGE TABLE")
    x = 74
    for label, value in (("Perturbation", "OPA1"), ("Source", treated["Source"]), ("Plate", treated["Plate"]), ("Well", treated["Well"])):
        x = chip(draw, x, 154, label, value)
    card(draw, (74, 230, 1726, 835), fill=PALE)
    draw.text((106, 264), f"{treated['JCP2022']} · {treated['Source']} · {treated['Plate']} · {treated['Well']}", fill=NAVY, font=F28, stroke_width=1)
    thumb_w, gap = 292, 24
    for i in range(5):
        x0 = 108 + i * (thumb_w + gap)
        box = (x0, 332, x0 + thumb_w, 692)
        draw.rounded_rectangle(box, radius=10, fill=WHITE, outline=LINE, width=2)
        paste_cover(image, get_preview(parse_image(treated[f"Site {i}"])), (x0 + 8, 340, x0 + thumb_w - 8, 650))
        draw.text((x0 + 12, 662), f"Site {i}", fill=INK, font=F18)
    draw.rounded_rectangle((96, 314, 1678, 718), radius=12, outline=CORAL, width=4)
    draw.text((106, 758), "All five fields are treatment previews for the same OPA1 reagent and plate.", fill=INK, font=F24)
    save(image, "04-gallery-perturbation.png")


def render_controls() -> None:
    rows = read_csv("crispr-images-and-controls.csv")
    plate_rows = [row for row in rows if row["Source"] == "source_13" and row["Plate"] == "CP-CC9-R1-06"]
    treated = next(row for row in plate_rows if row["Perturbation"] == "OPA1")
    controls = []
    for kind in ("no-guide", "non-targeting"):
        controls.extend([row for row in plate_rows if row["Perturbation"] == kind][:2])
    selected = [treated, controls[0], controls[2], controls[1]]
    image, draw = canvas("Add plate-matched controls", "Keep source_13 and CP-CC9-R1-06 fixed; include genetic controls", "CONTROL SELECTION")
    x = chip(draw, 74, 154, "Perturbation", "OPA1, no-guide, non-targeting", color=CORAL)
    x = chip(draw, x, 154, "Plate", "CP-CC9-R1-06")
    card(draw, (74, 232, 1726, 842), fill=PALE)
    labels = ["OPA1 treatment", "No-guide control", "Non-targeting control", "No-guide control"]
    for i, (row, label) in enumerate(zip(selected, labels)):
        x0 = 102 + i * 404
        card(draw, (x0, 270, x0 + 370, 798), fill=WHITE, outline=TEAL if i == 0 else LINE)
        draw.text((x0 + 20, 296), label, fill=NAVY if i == 0 else INK, font=F22, stroke_width=1 if i == 0 else 0)
        paste_cover(image, get_preview(parse_image(row["Site 0"])), (x0 + 20, 348, x0 + 350, 654))
        draw.text((x0 + 20, 674), row["Perturbation"], fill=INK, font=F20)
        draw.text((x0 + 20, 712), row["JCP2022"], fill=MUTED, font=F18)
        draw.text((x0 + 20, 748), f"{row['Plate']} · {row['Well']} · Site 0", fill=MUTED, font=F16)
    draw.rounded_rectangle((486, 252, 1702, 818), radius=16, outline=CORAL, width=4)
    save(image, "05-gallery-controls.png")


def render_activity() -> None:
    activity = {row["modality"]: row for row in read_csv("activity.csv")}
    image, draw = canvas("Does OPA1 produce a measurable phenotype?", "Read the perturbation-level values before interpreting individual features", "ACTIVITY")
    specs = [("CRISPR knockout", activity["crispr"], 74, TEAL), ("ORF overexpression", activity["orf"], 914, GOLD)]
    for title, row, x, color in specs:
        card(draw, (x, 174, x + 812, 804), fill=WHITE, outline=color, width=3)
        draw.rectangle((x + 2, 176, x + 810, 258), fill=color)
        draw.text((x + 30, 198), title, fill=WHITE, font=F28, stroke_width=1)
        draw.text((x + 40, 304), "Perturbation", fill=MUTED, font=F20)
        draw.text((x + 368, 296), row["Perturbation"], fill=INK, font=F32, stroke_width=1)
        draw.text((x + 40, 384), "JCP2022", fill=MUTED, font=F20)
        draw.text((x + 368, 378), row["JCP2022"], fill=INK, font=F28)
        draw.text((x + 40, 476), "Corrected p-value", fill=MUTED, font=F20)
        draw.text((x + 368, 462), row["Corrected p-value"], fill=GREEN, font=F40, stroke_width=1)
        draw.text((x + 40, 576), "Phenotypic activity", fill=MUTED, font=F20)
        draw.text((x + 368, 562), row["Phenotypic activity"], fill=NAVY, font=F40, stroke_width=1)
        draw.rounded_rectangle((x + 36, 676, x + 776, 750), radius=14, fill=PALE_BLUE)
        draw.text((x + 64, 699), "Perturbation-level summary shared by all feature rows", fill=INK, font=F20)
    save(image, "06-activity.png")


def render_feature_row() -> None:
    row = read_csv("crispr-features.csv")[0]
    image, draw = canvas("What does one OPA1 feature row describe?", "One reagent × one measured CellProfiler feature", "ROW ANATOMY")
    fields = [
        ("Perturbation", row["Perturbation"]),
        ("Reagent", row["JCP2022"]),
        ("Object", row["Compartment"]),
        ("Feature", row["Feature"]),
        ("Channel + suffix", row["Channel"] + row["Suffix"]),
        ("Feature p", row["Feature significance"] + " (rounded)"),
        ("Cohen's d", row["Cohen's d"]),
        ("Feature rank", row["Feature Rank"]),
    ]
    y = 176
    for i, (label, value) in enumerate(fields):
        x = 74 if i % 2 == 0 else 914
        if i % 2 == 0 and i:
            y += 160
        card(draw, (x, y, x + 812, y + 130), fill=PALE_BLUE if label in ("Feature", "Channel + suffix", "Cohen's d") else WHITE, outline=TEAL if label in ("Feature", "Channel + suffix", "Cohen's d") else LINE)
        draw.text((x + 30, y + 22), label, fill=MUTED, font=F20)
        draw.text((x + 30, y + 68), text_fit(draw, value, 742, F26), fill=INK, font=F26, stroke_width=1 if label in ("Feature", "Cohen's d") else 0)
    draw.text((76, 846), "This is a published profile summary—not a measurement of the single image crop shown later.", fill=CORAL, font=F22, stroke_width=1)
    save(image, "07-feature-row.png")


def render_features() -> None:
    rows = read_csv("crispr-features.csv")
    image, draw = canvas("OPA1 CRISPR · top published feature rows", "Sort by feature rank, then inspect significance and signed effect size", "FEATURES")
    headers = ["Rank", "Object", "Feature", "Channel", "Feature p", "Cohen's d"]
    values = []
    for row in rows:
        values.append([row["Feature Rank"], row["Compartment"], row["Feature"] + row["Suffix"], row["Channel"] or "—", row["Feature significance"], row["Cohen's d"]])
    table(draw, (60, 170, 1740, 690), headers, values, [0.08, 0.14, 0.42, 0.10, 0.13, 0.13], row_height=86, highlight_columns={4, 5}, highlight_rows={0})
    card(draw, (60, 744, 1740, 862), fill=PALE_BLUE, outline=TEAL)
    draw.text((96, 772), "Top row", fill=NAVY, font=F22, stroke_width=1)
    draw.text((236, 768), "Cytoplasm Texture_Correlation · Mito · scale 3 · Cohen's d +3.56", fill=INK, font=F26, stroke_width=1)
    draw.text((236, 814), "Displayed 0.0 p-values are rounded; use rank and effect size for ordering tied rows.", fill=MUTED, font=F18)
    save(image, "08-crispr-features.png")


def render_orf() -> None:
    rows = read_csv("orf-features.csv")
    activity = next(row for row in read_csv("activity.csv") if row["modality"] == "orf")
    image, draw = canvas("OPA1 ORF · compare another perturbation type", "Overexpression has its own reagent, activity and feature effects", "ORF FEATURES")
    x = 74
    for label, value in (("Perturbation", "OPA1"), ("JCP2022", activity["JCP2022"]), ("Corrected p", activity["Corrected p-value"]), ("Activity", activity["Phenotypic activity"])):
        x = chip(draw, x, 152, label, value, color=GOLD if label in ("Corrected p", "Activity") else TEAL)
    headers = ["Rank", "Object", "Feature", "Channel", "Feature p", "Cohen's d"]
    values = [[row["Feature Rank"], row["Compartment"], row["Feature"] + row["Suffix"], row["Channel"] or "—", row["Feature significance"], row["Cohen's d"]] for row in rows]
    table(draw, (60, 238, 1740, 758), headers, values, [0.08, 0.14, 0.42, 0.10, 0.13, 0.13], row_height=86, highlight_columns={4, 5}, highlight_rows={0, 1})
    draw.text((74, 808), "Compare directions cautiously: ORF is not assumed to be the inverse of CRISPR.", fill=CORAL, font=F22, stroke_width=1)
    save(image, "09-orf-features.png")


def render_matches() -> None:
    rows = read_csv("crispr-similar.csv")[:4]
    image, draw = canvas("Which profiles are most similar to OPA1 CRISPR?", "Filter OPA1, sort signed profile similarity descending, then inspect images and annotations", "MATCHES")
    y = 154
    for i, row in enumerate(rows):
        card(draw, (64, y, 1736, y + 160), fill=WHITE if i % 2 == 0 else PALE)
        draw.text((92, y + 20), "OPA1", fill=NAVY, font=F24, stroke_width=1)
        paste_cover(image, get_preview(parse_image(row["Perturbation example image"])), (188, y + 12, 328, y + 148))
        draw.text((362, y + 57), "→", fill=MUTED, font=F40)
        paste_cover(image, get_preview(parse_image(row["Match example image"])), (438, y + 12, 578, y + 148))
        draw.text((610, y + 20), row["Match"], fill=INK, font=F28, stroke_width=1)
        draw.text((610, y + 72), row["Match JCP2022"], fill=MUTED, font=F18)
        draw.text((1010, y + 20), "Similarity", fill=MUTED, font=F18)
        score = row["Perturbation-Match Similarity"]
        draw.text((1010, y + 52), score, fill=GREEN, font=F40, stroke_width=1)
        draw.rounded_rectangle((1286, y + 44, 1688, y + 104), radius=13, fill=PALE_BLUE, outline=TEAL, width=2)
        draw.text((1320, y + 62), "NCBI · OMIM · GeneCards · Ensembl", fill=NAVY, font=F18)
        y += 174
    draw.text((74, 868), "Similarity is a follow-up lead, not independent evidence of a shared mechanism.", fill=CORAL, font=F20, stroke_width=1)
    save(image, "10-matches.png")


def render_export() -> None:
    rows = read_csv("crispr-features.csv")[:3]
    image, draw = canvas("Keep and share the filtered OPA1 result", "Retain the identifiers and filters alongside the exported rows", "EXPORT")
    card(draw, (70, 156, 1730, 336), fill=PALE)
    x = chip(draw, 98, 188, "Perturbation", "OPA1")
    x = chip(draw, x, 188, "Compartment", "Cytoplasm, Nuclei")
    draw.rounded_rectangle((1426, 184, 1688, 242), radius=12, fill=TEAL)
    draw.text((1498, 201), "Apply", fill=WHITE, font=F20)
    draw.text((98, 274), "27 published rows match these filters", fill=GREEN, font=F20, stroke_width=1)
    headers = ["JCP2022", "Object", "Feature", "Channel", "Cohen's d"]
    values = [[row["JCP2022"], row["Compartment"], row["Feature"] + row["Suffix"], row["Channel"] or "—", row["Cohen's d"]] for row in rows]
    table(draw, (70, 374, 1730, 696), headers, values, [0.18, 0.16, 0.42, 0.10, 0.14], row_height=82)
    draw.text((78, 748), "This data as", fill=MUTED, font=F22)
    for x, label, color in ((256, "JSON", NAVY_2), (408, "CSV", TEAL), (546, "SQL", GOLD)):
        draw.rounded_rectangle((x, 730, x + 122, 786), radius=12, fill=color)
        draw.text((x + 32, 747), label, fill=WHITE, font=F20)
    card(draw, (946, 724, 1730, 838), fill=PALE_BLUE, outline=TEAL)
    draw.text((980, 748), "Save with:", fill=NAVY, font=F20, stroke_width=1)
    draw.text((1104, 746), "OPA1 · JCP2022_804796 · CRISPR · filters · source URL", fill=INK, font=F18)
    draw.text((980, 792), "That context makes the export reusable by an agent or collaborator.", fill=MUTED, font=F18)
    save(image, "11-export.png")


def write_provenance() -> None:
    outputs = []
    for path in sorted(OUT.glob("*.png")):
        with Image.open(path) as image:
            outputs.append({
                "path": str(path.relative_to(ROOT)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
                "width": image.width,
                "height": image.height,
            })
    input_provenance = json.loads((DATA / "provenance.json").read_text())
    availability_prefix = DATA / "availability-opa-prefix.csv"
    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "gene": "OPA1",
        "generator": str(Path(__file__).relative_to(ROOT)),
        "description": "Static OPA1 walkthrough panels rendered from published JUMP_rr table extracts; no values relabeled and no new statistics calculated.",
        "table_inputs": input_provenance,
        "auxiliary_inputs": {
            "availability_opa_prefix": {
                "path": str(availability_prefix.relative_to(ROOT)),
                "sha256": hashlib.sha256(availability_prefix.read_bytes()).hexdigest(),
                "bytes": availability_prefix.stat().st_size,
                "derived_from": input_provenance["inputs"]["coverage"]["url"],
            }
        },
        "preview_images": preview_records,
        "outputs": outputs,
    }
    PROVENANCE.write_text(json.dumps(payload, indent=2) + "\n")


def main() -> None:
    if not DATA.exists():
        raise SystemExit("Run demo/query_jump.py --gene OPA1 first")
    OUT.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    render_availability()
    render_columns()
    render_filters()
    render_gallery()
    render_controls()
    render_activity()
    render_feature_row()
    render_features()
    render_orf()
    render_matches()
    render_export()
    write_provenance()
    print(f"Rendered 11 OPA1 panels in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
