"""
Kundli Pathshala — QA Report PDF Generator + Drive Uploader
Run this after QA checks are complete, passing the report text as input.
Usage: python generate_and_upload.py "path/to/report.txt"
Or import and call generate_pdf(report_text) directly from Claude Code.
"""

import sys
import os
import base64
from datetime import datetime

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, black, white
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
except ImportError:
    print("Installing reportlab...")
    os.system("pip install reportlab")
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, black, white
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.lib.enums import TA_CENTER, TA_LEFT


DRIVE_FOLDER_ID = "1OBzjU-FplLV5JJg1xCw514Y3u7o92glv"

URLS = {
    "PFB Landing": "https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/",
    "PGA Landing": "https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/",
    "CFB Thank You": "https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/",
    "PGA Thank You": "https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/",
    "WhatsApp": "https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/",
}

# Colors
ORANGE   = HexColor("#FF6B00")
DARK     = HexColor("#1A1A2E")
LIGHT_BG = HexColor("#FFF8F0")
GRAY     = HexColor("#F5F5F5")
GREEN    = HexColor("#28A745")
RED      = HexColor("#DC3545")
YELLOW   = HexColor("#FFC107")


def build_pdf(report_text: str, output_path: str) -> str:
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title", fontSize=20, textColor=white,
        alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        "Subtitle", fontSize=11, textColor=HexColor("#FFD580"),
        alignment=TA_CENTER, fontName="Helvetica", spaceAfter=2
    )
    heading_style = ParagraphStyle(
        "Heading", fontSize=13, textColor=ORANGE,
        fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=6
    )
    body_style = ParagraphStyle(
        "Body", fontSize=9, textColor=DARK,
        fontName="Helvetica", spaceAfter=4, leading=14
    )
    mono_style = ParagraphStyle(
        "Mono", fontSize=8, textColor=DARK,
        fontName="Courier", spaceAfter=3, leading=12
    )

    today = datetime.now()
    date_str = today.strftime("%d %B %Y")
    time_str = today.strftime("%I:%M %p IST")
    filename = f"Kundli-Pathshala-QA-{today.strftime('%Y-%m-%d')}.pdf"

    story = []

    # Header banner
    header_data = [[
        Paragraph("🔱 Kundli Pathshala — Daily QA Report", title_style),
    ]]
    header_table = Table(header_data, colWidths=[6.5 * inch])
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK),
        ("ROWPADDING", (0, 0), (-1, -1), 14),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("ROUNDEDCORNERS", [8]),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))

    # Date/time row
    meta_data = [[
        Paragraph(f"Date: {date_str}", body_style),
        Paragraph(f"Run Time: {time_str}", body_style),
        Paragraph("Schedule: Daily @ 6:00 PM IST", body_style),
    ]]
    meta_table = Table(meta_data, colWidths=[2.16 * inch] * 3)
    meta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
        ("ROWPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOX", (0, 0), (-1, -1), 0.5, ORANGE),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # URLs tested
    story.append(Paragraph("Pages Tested", heading_style))
    url_rows = [["ID", "Type", "URL"]]
    for name, url in URLS.items():
        url_rows.append([name.split()[0], name.split()[1] if len(name.split()) > 1 else "", url])
    url_table = Table(url_rows, colWidths=[0.8 * inch, 0.9 * inch, 4.8 * inch])
    url_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ORANGE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ROWPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.3, HexColor("#CCCCCC")),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
    ]))
    story.append(url_table)
    story.append(Spacer(1, 14))

    # QA Report Content
    story.append(HRFlowable(width="100%", thickness=1, color=ORANGE))
    story.append(Spacer(1, 6))
    story.append(Paragraph("QA Check Results", heading_style))

    # Parse and render the report text
    for line in report_text.split("\n"):
        line = line.strip()
        if not line:
            story.append(Spacer(1, 4))
            continue
        if line.startswith("###") or line.startswith("##"):
            clean = line.lstrip("#").strip()
            story.append(Paragraph(clean, heading_style))
        elif line.startswith("|"):
            story.append(Paragraph(line, mono_style))
        elif line.startswith("✅") or line.startswith("❌") or line.startswith("⚠️"):
            story.append(Paragraph(line, body_style))
        else:
            story.append(Paragraph(line, body_style))

    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=1, color=ORANGE))
    story.append(Spacer(1, 6))

    # Footer
    footer_data = [[
        Paragraph("AstroArunPandit.org | Kundli Pathshala QA Automation", body_style),
        Paragraph(f"Generated: {date_str} @ {time_str}", body_style),
    ]]
    footer_table = Table(footer_data, colWidths=[3.25 * inch, 3.25 * inch])
    footer_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY),
        ("ROWPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("BOX", (0, 0), (-1, -1), 0.3, HexColor("#CCCCCC")),
    ]))
    story.append(footer_table)

    doc.build(story)
    return output_path


def generate_pdf(report_text: str) -> tuple[str, str]:
    """
    Generate PDF from report text.
    Returns (output_path, base64_encoded_pdf)
    """
    today = datetime.now()
    output_dir = os.path.dirname(os.path.abspath(__file__))
    filename = f"Kundli-Pathshala-QA-{today.strftime('%Y-%m-%d')}.pdf"
    output_path = os.path.join(output_dir, filename)

    build_pdf(report_text, output_path)

    with open(output_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    print(f"PDF generated: {output_path}")
    return output_path, encoded


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            report_text = f.read()
    else:
        report_text = "Test report - no content provided."

    path, _ = generate_pdf(report_text)
    print(f"PDF saved to: {path}")
