# -*- coding: utf-8 -*-
"""Maintainable source for Suthan K's one-page resume (content + both writers).

This single file is the editable source for the deliverables:
    Suthan_K_Resume.pdf   - A4, exactly 1 page, real PDF link annotations (ReportLab)
    Suthan_K_Resume.docx  - single-column, editable, working hyperlinks (python-docx)

LaTeX is not installed on this box (Amazon Linux 2023, arm64: no pdflatex/xelatex/
tectonic), and neither is LibreOffice, so there is no .tex -> PDF or .docx -> PDF
path here. The PDF is therefore rendered directly by ReportLab from the same
content dictionary the .docx writer uses, which keeps the two in sync.

Arial is not installed either; Liberation Sans is metric-compatible with Arial, so
it renders the PDF while the .docx asks for "Arial" by name (what Word and most ATS
parsers expect).

Usage:
    python3.13 Suthan_K_Resume_source.py [outdir]      # default: this file's folder

Layout rules (ATS-safe by construction): single column, no tables, no text boxes,
no images, no header/footer, no icons, no skill bars, standard section headings,
reverse-chronological experience, real bullet glyphs as text.
"""
import glob
import os
import sys
from datetime import datetime

# ---------------------------------------------------------------- the content
# Source of truth: the owner's supplied resume content. Nothing invented here -
# no company, date, metric or achievement that the owner did not provide.

NAME = "SUTHAN K"
TARGET_ROLE = "FULL STACK DEVELOPER | SOFTWARE ENGINEER"

LOCATION = "Trivandrum, Kerala, India"
PHONE = "+91 93843 40144"
EMAIL = "suthanks2000@gmail.com"

# (label shown, url). Labels stay short and readable; the URL is the annotation.
LINKS = [
    ("suthan.vercel.app", "https://suthan.vercel.app"),
    ("github.com/suthanks2000", "https://github.com/suthanks2000"),
    ("linkedin.com/in/suthan-k", "https://www.linkedin.com/in/suthan-k/"),
]
LINK_LABELS = ["Portfolio", "GitHub", "LinkedIn"]
EMAIL_URL = "mailto:" + EMAIL

SUMMARY = (
    "Full Stack Software Engineer with 2+ years of experience building scalable, "
    "client-facing web applications with React.js, Next.js, TypeScript, JavaScript, "
    "Node.js and Python. Cut API response time by 25% by optimising REST and GraphQL "
    "APIs. Hands-on with JWT/RBAC authentication, PostgreSQL indexing, Dockerised "
    "microservices on AWS and Azure, and CI/CD delivery in cross-functional Agile teams."
)

SKILLS = [
    ("Languages", "JavaScript (ES6+), TypeScript, Python, SQL"),
    ("Frontend", "React.js, Next.js, Redux Toolkit, HTML5, CSS3, Tailwind CSS"),
    ("Backend & APIs", "Node.js, Express.js, FastAPI, Flask, REST APIs, GraphQL, "
                       "WebSockets (SignalR), Microservices"),
    ("Databases", "PostgreSQL, MySQL, MongoDB, Redis, TimescaleDB, Prisma, TypeORM"),
    ("Cloud & DevOps", "AWS (Lambda, ECS, API Gateway, S3, RDS, SQS, CloudWatch, IAM), "
                       "Azure (Container Apps, DevOps), Docker, Nginx, GitHub Actions, "
                       "CI/CD, Cloudflare, Vercel"),
    ("Security & Testing", "JWT, RBAC, OAuth2, Keycloak, Jest, Vitest, PyTest"),
    ("Tools & Practices", "Git, Jira, Agile/Scrum, Data Structures & Algorithms"),
]

EXPERIENCE = [
    {
        "title": "Software Engineer",
        "org": "Magpii Innovations",
        "dates": "Nov 2025 – Present",
        "bullets": [
            "Develop full-stack features for an Industrial IoT and Digital Twin platform "
            "(React 19, TypeScript, ASP.NET Core) and an AI-powered education management "
            "platform (Next.js, Node.js, PostgreSQL), delivered in Agile sprints.",
            "Build event-driven .NET microservices with SignalR WebSockets for real-time "
            "telemetry, handling 10,000+ concurrent events/sec at sub-100 ms latency.",
            "Deliver REST APIs with pagination, search, filtering and RBAC across 12+ "
            "modules of a live education platform used by schools, colleges and universities.",
            "Onboard clients by translating requirements into platform configuration and "
            "features, and resolve production issues on live platforms.",
        ],
    },
    {
        "title": "Junior Software Developer",
        "org": "Comorins Technologies",
        "dates": "Mar 2025 – Oct 2025",
        "bullets": [
            "Cut manual viewing coordination and booking conflicts by building client "
            "self-booking with optimised scheduling logic (React.js, Next.js, Node.js, "
            "Express.js).",
            "Improved SEO and page-load performance for an AI-powered real estate platform "
            "with server-side-rendered Next.js and TypeScript pages.",
            "Improved client engagement and retention with AI-powered follow-up automation "
            "in Python, plus analytics dashboards for client preferences and viewing "
            "performance.",
            "Secured Node.js REST APIs with JWT authentication and RBAC (MySQL/PostgreSQL), "
            "and shipped releases to Vercel through GitHub Actions CI/CD.",
        ],
    },
    {
        "title": "Junior Software Developer",
        "org": "Devaxcel Tech Pvt. Ltd.",
        "dates": "Sep 2024 – Mar 2025",
        "bullets": [
            "Cut API response time by 25% by optimising GraphQL and REST APIs, and built "
            "React, TypeScript and Redux Toolkit features for a live HealthTech platform.",
            "Managed PostgreSQL migrations, indexing and secure queries with TypeORM to keep "
            "data access fast and safe.",
            "Built and maintained order-related Node.js and TypeScript microservices within a "
            "28-service backend, so each service could be deployed and scaled independently.",
            "Automated releases to AWS Lambda through GitHub Actions CI/CD pipelines.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Enterprise Industrial IoT & Digital Twin Platform",
        "stack": "React 19, TypeScript, .NET 8/9, ASP.NET Core, SignalR, PostgreSQL, "
                 "Apache AGE, TimescaleDB, Docker, Azure Container Apps, Keycloak",
        "bullets": [
            "Built an event-driven digital twin of 7+ ASP.NET Core microservices with a "
            "React 19 operator cockpit, enabling real-time monitoring of assets across "
            "industrial plants.",
            "Cut multi-hop graph queries by 45% and sped up time-series aggregations 3x by "
            "combining Apache AGE (asset graph) and TimescaleDB (sensor telemetry) in one "
            "PostgreSQL data tier.",
            "Cut client deployment time from 3 weeks to 2 days with a metadata-driven UI "
            "configured through JSON schemas; secured with Keycloak (OIDC/OAuth2, RBAC) and "
            "tested with xUnit and Vitest (85%+ coverage).",
        ],
    },
    {
        "name": "AI-Powered Education Management Platform",
        "stack": "React, Next.js, TypeScript, Node.js, Express.js, PostgreSQL, Prisma, "
                 "Redis, Docker, AWS ECS",
        "bullets": [
            "Delivered features across 12+ modules (students, staff, library, timetable, "
            "attendance, assignments, quizzes, parent portal) supporting academic and "
            "administrative workflows for schools, colleges and universities.",
            "Resolved API and data compatibility issues by migrating database access from "
            "Prisma/MySQL to raw PostgreSQL queries, and extended AI-powered assignment and "
            "quiz workflows (subject mapping, publishing, filtering).",
        ],
    },
    {
        "name": "HealthTech App – Digital Healthcare Platform",
        "stack": "React, TypeScript, Node.js, TypeORM, PostgreSQL, GraphQL, REST APIs, "
                 "AWS (Lambda, API Gateway, S3, RDS, SQS, CloudWatch)",
        "bullets": [
            "Processed 10,000+ daily orders for medicine purchases and digital prescriptions "
            "on a live platform, with multi-stage order verification.",
            "Automated order processing and delivery-readiness workflows with AWS Lambda, and "
            "secured patient health records with JWT authentication and RBAC across "
            "microservices.",
        ],
    },
]

EDUCATION = [
    "Bachelor of Engineering (B.E.)",
    "University College of Engineering, Nagercoil | 2019 – 2022",
]

# --------------------------------------------------------------- the template
A4_W_PT, A4_H_PT = 595.276, 841.890          # 210 x 297 mm
MARGIN_PT = 0.5 * 72                          # 0.5 in, inside the 0.45-0.6 in band

ACCENT_HEX = "17365D"                         # one accent colour: deep navy
TEXT_HEX = "1A1A1A"                           # dark charcoal body text

NAME_SIZE, NAME_LEAD = 20.0, 22.0
ROLE_SIZE, ROLE_LEAD = 10.5, 12.0
BODY_SIZE, BODY_LEAD = 9.7, 11.5
HEAD_SIZE, HEAD_LEAD = 10.5, 12.0             # section headings

BULLET_AFTER = 1.2                            # between bullets
BLOCK_AFTER = 4.0                             # end of a section
SECTION_BEFORE = 6.0                          # above a section heading
SECTION_AFTER = 3.0                           # below the heading rule
ENTRY_BEFORE = 3.5                            # between jobs / projects
ENTRY_AFTER = 1.2                             # under a job / project header
BULLET_INDENT = 10.5

BULLET = "•"
SEP = "  |  "


def esc(text):
    """Escape text for ReportLab's mini-markup."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def job_header(job):
    return f"{job['title']} | {job['org']} | {job['dates']}"


# ------------------------------------------------------------------ the .docx
from docx import Document                                           # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH                       # noqa: E402
from docx.opc.constants import RELATIONSHIP_TYPE as RT              # noqa: E402
from docx.oxml import OxmlElement                                   # noqa: E402
from docx.oxml.ns import qn                                         # noqa: E402
from docx.shared import Inches, Mm, Pt, RGBColor                    # noqa: E402

# Schema order of w:pPr children. Anything injected by hand must respect it, or
# Word reports the file as corrupt.
PPR_SEQ = [
    "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
    "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens",
    "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
    "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
    "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
    "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
    "sectPr", "pPrChange",
]


def _reorder_ppr(pPr):
    rank = {n: i for i, n in enumerate(PPR_SEQ)}
    for el in sorted(pPr, key=lambda e: rank.get(e.tag.split("}")[-1], 999)):
        pPr.append(el)


def _force_font(rPr, name="Arial"):
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), name)


def _rule(par, color=ACCENT_HEX, sz="6"):
    """Thin bottom border on a paragraph - no table, no drawing object."""
    pPr = par._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), sz)          # eighths of a point
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)
    _reorder_ppr(pPr)


def _para(doc, *, before=0.0, after=BULLET_AFTER, indent=None, hanging=None,
          align=None, keep_next=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.0
    pf.widow_control = False
    if align is not None:
        p.alignment = align
    if indent is not None:
        pf.left_indent = Pt(indent)
    if hanging is not None:
        pf.first_line_indent = Pt(-hanging)
    if keep_next:
        pf.keep_with_next = True
    return p


def _run(p, text, *, size=BODY_SIZE, bold=False, color=TEXT_HEX):
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = RGBColor.from_string(color)
    _force_font(r._element.get_or_add_rPr())
    return r


def _link(p, text, url, *, size=BODY_SIZE, color=ACCENT_HEX, underline=False):
    """A real external hyperlink relationship, not just styled text."""
    r_id = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    _force_font(rPr)
    szv = OxmlElement("w:sz")
    szv.set(qn("w:val"), str(int(round(size * 2))))
    rPr.append(szv)
    col = OxmlElement("w:color")
    col.set(qn("w:val"), color)
    rPr.append(col)
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rPr.append(u)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    hl.append(run)
    p._p.append(hl)
    return hl


def _heading(doc, text):
    p = _para(doc, before=SECTION_BEFORE, after=SECTION_AFTER, keep_next=True)
    _run(p, text.upper(), size=HEAD_SIZE, bold=True, color=ACCENT_HEX)
    _rule(p)
    return p


def _bullet(doc, text, *, after=BULLET_AFTER, label=None):
    p = _para(doc, indent=BULLET_INDENT, hanging=BULLET_INDENT, after=after)
    _run(p, BULLET + "  ")
    if label:
        _run(p, label + ": ", bold=True)
    _run(p, text)
    return p


def build_docx(path):
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(BODY_SIZE)
    normal.font.color.rgb = RGBColor.from_string(TEXT_HEX)
    _force_font(normal.element.get_or_add_rPr())
    normal.paragraph_format.space_after = Pt(BULLET_AFTER)
    normal.paragraph_format.line_spacing = 1.0

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = Inches(0.5)
    sec.top_margin = sec.bottom_margin = Inches(0.5)
    sec.header_distance = sec.footer_distance = Inches(0.3)

    # --- header
    p = _para(doc, after=0.5)
    _run(p, NAME, size=NAME_SIZE, bold=True)
    p = _para(doc, after=2.5)
    _run(p, TARGET_ROLE, size=ROLE_SIZE, bold=True, color=ACCENT_HEX)

    p = _para(doc, after=1.0)
    _run(p, LOCATION + SEP + PHONE + SEP)
    _link(p, EMAIL, EMAIL_URL)

    p = _para(doc, after=2.0)
    for i, ((label_text, url), label) in enumerate(zip(LINKS, LINK_LABELS)):
        if i:
            _run(p, SEP)
        _run(p, label + ": ")
        _link(p, label_text, url)
    _rule(p, sz="8")

    # --- summary
    _heading(doc, "Professional Summary")
    p = _para(doc, after=BLOCK_AFTER)
    _run(p, SUMMARY)

    # --- skills
    _heading(doc, "Technical Skills")
    for i, (label, value) in enumerate(SKILLS):
        _bullet(doc, value, label=label,
                after=BLOCK_AFTER if i == len(SKILLS) - 1 else BULLET_AFTER)

    # --- experience
    _heading(doc, "Professional Experience")
    for i, job in enumerate(EXPERIENCE):
        p = _para(doc, before=ENTRY_BEFORE if i else 0.0, after=ENTRY_AFTER,
                  keep_next=True)
        _run(p, job["title"], bold=True)
        _run(p, " | " + job["org"] + " | ")
        _run(p, job["dates"], bold=True)
        for j, b in enumerate(job["bullets"]):
            last = (j == len(job["bullets"]) - 1) and (i == len(EXPERIENCE) - 1)
            _bullet(doc, b, after=BLOCK_AFTER if last else BULLET_AFTER)

    # --- projects
    _heading(doc, "Key Projects")
    for i, proj in enumerate(PROJECTS):
        p = _para(doc, before=ENTRY_BEFORE if i else 0.0, after=ENTRY_AFTER,
                  keep_next=True)
        _run(p, proj["name"], bold=True)
        p = _para(doc, after=ENTRY_AFTER, keep_next=True)
        _run(p, "Technologies: " + proj["stack"])
        for j, b in enumerate(proj["bullets"]):
            last = (j == len(proj["bullets"]) - 1) and (i == len(PROJECTS) - 1)
            _bullet(doc, b, after=BLOCK_AFTER if last else BULLET_AFTER)

    # --- education
    _heading(doc, "Education")
    p = _para(doc, after=0.5)
    _run(p, EDUCATION[0], bold=True)
    p = _para(doc, after=0.0)
    _run(p, EDUCATION[1])

    # Clean metadata: nothing that reveals the generator.
    cp = doc.core_properties
    cp.author = "Suthan K"
    cp.last_modified_by = "Suthan K"
    cp.title = "Suthan K - Full Stack Developer | Software Engineer"
    cp.subject = ""
    cp.comments = ""
    cp.category = ""
    cp.keywords = ""
    cp.revision = 1
    now = datetime.now().replace(microsecond=0)
    cp.created = now
    cp.modified = now

    doc.save(path)
    return path


# -------------------------------------------------------------------- the PDF
from reportlab import rl_config                                     # noqa: E402
from reportlab.lib.colors import HexColor                            # noqa: E402
from reportlab.lib.enums import TA_LEFT                              # noqa: E402
from reportlab.lib.styles import ParagraphStyle                      # noqa: E402
from reportlab.pdfbase import pdfmetrics                             # noqa: E402
from reportlab.pdfbase.ttfonts import TTFont                         # noqa: E402
from reportlab.platypus import (BaseDocTemplate, Frame,              # noqa: E402
                                HRFlowable, KeepTogether, PageTemplate,
                                Paragraph, Spacer)

FONT, FONT_B = "Arial", "Arial-Bold"
ACCENT = HexColor("#" + ACCENT_HEX)
TEXT = HexColor("#" + TEXT_HEX)


def register_fonts():
    """Arial is absent; Liberation Sans is metric-compatible with it."""
    pairs = [(FONT, ["LiberationSans-Regular.ttf", "Arial.ttf", "arial.ttf"]),
             (FONT_B, ["LiberationSans-Bold.ttf", "Arial_Bold.ttf", "arialbd.ttf"])]
    roots = ["/usr/share/fonts", "/usr/local/share/fonts",
             os.path.expanduser("~/.fonts"),
             os.path.expanduser("~/.local/share/fonts")]
    for name, candidates in pairs:
        for cand in candidates:
            hits = []
            for root in roots:
                hits += glob.glob(os.path.join(root, "**", cand), recursive=True)
            if hits:
                pdfmetrics.registerFont(TTFont(name, hits[0]))
                break
        else:
            raise SystemExit(f"no font file found for {name}")
    pdfmetrics.registerFontFamily(FONT, normal=FONT, bold=FONT_B,
                                  italic=FONT, boldItalic=FONT_B)
    rl_config.canvas_basefontname = FONT     # never fall back to un-embedded Helvetica


def _styles():
    base = dict(fontName=FONT, fontSize=BODY_SIZE, leading=BODY_LEAD, textColor=TEXT,
                alignment=TA_LEFT, spaceBefore=0, spaceAfter=BULLET_AFTER)
    s = {
        "name": ParagraphStyle("name", **{**base, "fontName": FONT_B,
                                          "fontSize": NAME_SIZE, "leading": NAME_LEAD,
                                          "spaceAfter": 1.0}),
        "role": ParagraphStyle("role", **{**base, "fontName": FONT_B,
                                          "fontSize": ROLE_SIZE, "leading": ROLE_LEAD,
                                          "textColor": ACCENT, "spaceAfter": 3.0}),
        "contact": ParagraphStyle("contact", **{**base, "spaceAfter": 1.5}),
        "section": ParagraphStyle("section", **{**base, "fontName": FONT_B,
                                                "fontSize": HEAD_SIZE,
                                                "leading": HEAD_LEAD,
                                                "textColor": ACCENT,
                                                "spaceBefore": SECTION_BEFORE,
                                                "spaceAfter": 0}),
        "body": ParagraphStyle("body", **base),
        "entry": ParagraphStyle("entry", **{**base, "spaceAfter": ENTRY_AFTER}),
        "bullet": ParagraphStyle("bullet", **{**base,
                                              "leftIndent": BULLET_INDENT + 3.5,
                                              "bulletIndent": 0,
                                              "bulletFontName": FONT,
                                              "bulletFontSize": BODY_SIZE}),
    }
    return s


def build_pdf(path):
    s = _styles()
    story = []

    def bullet(text, after=BULLET_AFTER):
        return Paragraph(text, ParagraphStyle("b", parent=s["bullet"], spaceAfter=after),
                         bulletText=BULLET)

    def heading(text):
        story.append(Paragraph(esc(text.upper()), s["section"]))
        story.append(HRFlowable(width="100%", thickness=0.7, color=ACCENT,
                                spaceBefore=2.0, spaceAfter=SECTION_AFTER))

    def link(label, url):
        return f'<link href="{url}" color="#{ACCENT_HEX}">{esc(label)}</link>'

    # --- header
    story.append(Paragraph(esc(NAME), s["name"]))
    story.append(Paragraph(esc(TARGET_ROLE), s["role"]))
    story.append(Paragraph(
        esc(LOCATION) + esc(SEP) + esc(PHONE) + esc(SEP) + link(EMAIL, EMAIL_URL),
        s["contact"]))
    story.append(Paragraph(esc(SEP).join(
        f"{label}: {link(text, url)}"
        for label, (text, url) in zip(LINK_LABELS, LINKS)),
        ParagraphStyle("c2", parent=s["contact"], spaceAfter=3.0)))
    story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT,
                            spaceBefore=0, spaceAfter=0))

    # --- summary
    heading("Professional Summary")
    story.append(Paragraph(esc(SUMMARY),
                           ParagraphStyle("sum", parent=s["body"],
                                          spaceAfter=BLOCK_AFTER)))

    # --- skills
    heading("Technical Skills")
    for i, (label, value) in enumerate(SKILLS):
        after = BLOCK_AFTER if i == len(SKILLS) - 1 else BULLET_AFTER
        story.append(bullet(f"<b>{esc(label)}:</b> {esc(value)}", after=after))

    # --- experience
    heading("Professional Experience")
    for i, job in enumerate(EXPERIENCE):
        head = Paragraph(
            f"<b>{esc(job['title'])}</b> | {esc(job['org'])} | <b>{esc(job['dates'])}</b>",
            ParagraphStyle("j", parent=s["entry"], spaceBefore=ENTRY_BEFORE if i else 0))
        first = bullet(esc(job["bullets"][0]))
        story.append(KeepTogether([head, first]))      # no orphaned job header
        for j, b in enumerate(job["bullets"][1:], start=1):
            last = (j == len(job["bullets"]) - 1) and (i == len(EXPERIENCE) - 1)
            story.append(bullet(esc(b), after=BLOCK_AFTER if last else BULLET_AFTER))

    # --- projects
    heading("Key Projects")
    for i, proj in enumerate(PROJECTS):
        head = Paragraph(f"<b>{esc(proj['name'])}</b>", ParagraphStyle(
            "pn", parent=s["entry"], spaceBefore=ENTRY_BEFORE if i else 0))
        stack = Paragraph("Technologies: " + esc(proj["stack"]), s["entry"])
        first = bullet(esc(proj["bullets"][0]))
        story.append(KeepTogether([head, stack, first]))
        for j, b in enumerate(proj["bullets"][1:], start=1):
            last = (j == len(proj["bullets"]) - 1) and (i == len(PROJECTS) - 1)
            story.append(bullet(esc(b), after=BLOCK_AFTER if last else BULLET_AFTER))

    # --- education
    heading("Education")
    story.append(Paragraph(f"<b>{esc(EDUCATION[0])}</b>",
                           ParagraphStyle("e1", parent=s["body"], spaceAfter=1.0)))
    story.append(Paragraph(esc(EDUCATION[1]),
                           ParagraphStyle("e2", parent=s["body"], spaceAfter=0)))

    doc = BaseDocTemplate(
        path, pagesize=(A4_W_PT, A4_H_PT),
        leftMargin=MARGIN_PT, rightMargin=MARGIN_PT,
        topMargin=MARGIN_PT, bottomMargin=MARGIN_PT,
        title="Suthan K - Full Stack Developer | Software Engineer",
        author="Suthan K", subject="", creator="Suthan K", keywords="",
    )
    doc.addPageTemplates([PageTemplate(id="resume", frames=[Frame(
        MARGIN_PT, MARGIN_PT, A4_W_PT - 2 * MARGIN_PT, A4_H_PT - 2 * MARGIN_PT,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="single")])])
    doc.build(story)
    return path


def main(argv):
    # Project convention: each build lands in its own vN/ folder; v1 and v2 are
    # earlier, frozen versions and are never overwritten.
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = argv[0] if argv else os.path.join(here, "v3")
    os.makedirs(outdir, exist_ok=True)
    register_fonts()
    pdf = build_pdf(os.path.join(outdir, "Suthan_K_Resume.pdf"))
    docx = build_docx(os.path.join(outdir, "Suthan_K_Resume.docx"))
    for f in (pdf, docx):
        print(f"wrote {f} ({os.path.getsize(f):,} bytes)")


if __name__ == "__main__":
    main(sys.argv[1:])
