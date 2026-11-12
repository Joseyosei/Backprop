import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

D = json.load(open("/home/claude/backprop/courses.json"))
N = len(D["courses"])
FREEK = ("free", "audit", "beta", "freecert")
NFREE = sum(1 for c in D["courses"] if c["cost"] in FREEK)

INK = colors.HexColor("#0e1726")
MINT = colors.HexColor("#0b6b43")
RED = colors.HexColor("#9b1c1c")
GREY = colors.HexColor("#64748b")
LIGHT = colors.HexColor("#f6f8fb")
LINE = colors.HexColor("#e2e8f0")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=20,
                   leading=24, textColor=INK, spaceAfter=2)
SUB = ParagraphStyle("SUB", parent=ss["Normal"], fontName="Helvetica", fontSize=9.3,
                    leading=12.5, textColor=GREY, spaceAfter=11)
H2 = ParagraphStyle("H2", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=12.8,
                   leading=15.5, textColor=INK, spaceBefore=14, spaceAfter=5)
BODY = ParagraphStyle("BODY", parent=ss["Normal"], fontName="Helvetica", fontSize=9.4,
                     leading=13.4, textColor=colors.HexColor("#243246"), spaceAfter=6)
CELL = ParagraphStyle("CELL", parent=ss["Normal"], fontName="Helvetica", fontSize=8.3,
                     leading=11, textColor=colors.HexColor("#243246"))
CELLB = ParagraphStyle("CELLB", parent=CELL, fontName="Helvetica-Bold")
CELLH = ParagraphStyle("CELLH", parent=CELL, fontName="Helvetica-Bold", textColor=colors.white)
NOTE = ParagraphStyle("NOTE", parent=ss["Normal"], fontName="Helvetica", fontSize=7.7,
                     leading=10.4, textColor=GREY, spaceAfter=4)


def table(headers, rows, widths, align_center=()):
    data = [[Paragraph(h, CELLH) for h in headers]]
    for r in rows:
        data.append([Paragraph(c[1:], CELLB) if c.startswith("@") else Paragraph(c, CELL) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), INK), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("GRID", (0, 0), (-1, -1), 0.4, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 5),
          ("RIGHTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 4.5),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5)]
    for i in range(1, len(data)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    for col in align_center:
        st.append(("ALIGN", (col, 0), (col, -1), "CENTER"))
    t.setStyle(TableStyle(st))
    return t


def callout(title, body, bg="#fff8e8", bar="#c98a12"):
    inner = [[Paragraph(title, ParagraphStyle("ct", parent=CELLB, fontSize=9.8, textColor=INK, spaceAfter=3))],
             [Paragraph(body, CELL)]]
    t = Table(inner, colWidths=[165 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, colors.HexColor(bar)),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (0, 0), 7), ("BOTTOMPADDING", (0, -1), (-1, -1), 7),
        ("TOPPADDING", (0, 1), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, 0), 2)]))
    return t


s = []
s.append(Paragraph("BACKPROP", H1))
s.append(Paragraph("A course recommendation product for AI, ML and data science students worldwide: "
                   "honest assessment, brand, and what is already built &nbsp;|&nbsp; 12 November 2026", SUB))

s.append(callout("VERDICT: WEAK AS A VENTURE-BACKED STARTUP. STRONG AS A REPUTATION ASSET WITH A B2B PATH.",
  "Do not build this expecting it to be a company that raises money. Course aggregation is a crowded, "
  "low-margin, SEO-dependent category, and the product you are competing with is not another website: it is "
  "an AI assistant that answers \"what should I learn?\" for free, instantly, in any language. "
  "Build it anyway, for three reasons that are real. It is the single most credible portfolio piece you could "
  "ship for the AI Engineer roles you are applying to. It generates inbound from exactly the people who hire. "
  "And it has one genuinely defensible wedge, described below, that could be sold to universities rather than "
  "to students.", bg="#fff8e8", bar="#c98a12"))

s.append(Paragraph("THE HONEST PROBLEM: YOUR COMPETITOR IS A CHATBOT", H2))
s.append(Paragraph(
  "Any student anywhere can now ask an AI assistant what to study and get a personalised, free, instant answer. "
  "That is the same job your product does. Every course-list website, roadmap repository and curated newsletter "
  "is in the same position, and \"we have a nicer interface\" is not a defence. If the pitch is "
  "<b>recommendation</b>, you lose. A recommendation engine with no information the assistant lacks has no reason "
  "to exist.", BODY))
s.append(Paragraph(
  "The category is also already occupied. Course aggregators index far more courses than you will. Developer "
  "roadmap projects have enormous audiences and years of SEO. Every provider in your list publishes its own "
  "learning paths for free, and they are better funded than you. Affiliate-driven \"best AI courses\" content "
  "is one of the most aggressively optimised niches on the web.", BODY))

s.append(Paragraph("WHERE THE ACTUAL WEDGE IS", H2))
s.append(Paragraph(
  "Three things an AI assistant structurally cannot do well, and that aggregators do not bother doing. All three "
  "came out of building your own study plan, which is why they are worth trusting.", BODY))
s.append(table(
  ["Wedge", "Why it holds", "Evidence from this project"],
  [["@1. Dated verification",
    "Models have knowledge cutoffs and will confidently name exams that no longer exist. A ledger that says "
    "\"checked by hand on this date\" is a claim a model cannot truthfully make.",
    "Nearly every AI roadmap in circulation still points people at Microsoft AI-102, AI-900 and DP-100, and the "
    "AWS ML Specialty. All four retired during 2026. The live site flags five retired exams with replacements."],
   ["@2. True cost of a credential",
    "Nobody maps which certifications are free including the proctored exam, versus free training with a paid "
    "exam, versus paid everything. This is the question students actually ask and it changes decisions.",
    "Oracle gives two genuinely free proctored AI certifications, exam included. Almost nobody knows. Meanwhile "
    "paid bootcamps bundle a cheap foundational AWS exam and charge thousands for it."],
   ["@3. Degree overlap filtering",
    "No product takes \"I am enrolled on this degree\" and returns what is redundant. Universities publish module "
    "lists; the mapping is tedious, which is exactly why it is defensible.",
    "Filtering the ITOL curriculum against a UEL MSc module list removed nine of sixteen modules as already "
    "covered. That single step is what made the plan useful rather than another list."]],
  [30 * mm, 60 * mm, 75 * mm]))

s.append(Paragraph("THE BUSINESS MODEL PROBLEM, STATED PLAINLY", H2))
s.append(Paragraph(
  "Of the %d courses on the site, %d are free. The affiliate value of a free course is zero. So roughly "
  "three quarters of your catalogue, and specifically the best of it, earns nothing. The better your advice, "
  "the less you are paid for it. Any business plan built on course affiliate revenue therefore pushes you "
  "toward recommending worse, more expensive options, which destroys the only asset you have, which is being "
  "trusted." % (N, NFREE), BODY))
s.append(table(
  ["Model", "Realistic verdict"],
  [["@Course affiliate revenue", "Reject as the primary model. It pays you to lie and it pays badly."],
   ["@Student subscription", "Very hard. Students are the least willing payers in software, and your core audience "
    "is global and price-sensitive by definition."],
   ["@University careers services (B2B)", "The strongest path. A careers team paying a small annual licence for a "
    "current, verified skills map keyed to their own module lists is a real budget line. Start with UEL, where you "
    "are a student and can get a meeting."],
   ["@Employer L&D audit", "Plausible later. \"Here is what your team should actually take, and what it really "
    "costs\" is a service, not a website."],
   ["@Free forever, as reputation", "The honest answer for year one. The product is the CV."]],
  [46 * mm, 119 * mm]))

s.append(Paragraph("BRAND AND DOMAIN", H2))
s.append(Paragraph(
  "Backpropagation is how a network learns by sending error backwards and correcting itself. That is exactly what "
  "the product does to a study plan: checks the outcome, corrects the path. It is instantly legible to the "
  "audience, it is short, and it is not a generic education word.", BODY))
s.append(table(
  ["Domain", "First year", "Renewal", "Verdict"],
  [["@backprop.school", "$9.99", "$35.00", "Recommended. Reads as a sentence and the name carries meaning for this exact audience."],
   ["@learnbackprop.com", "$12.03", "$12.03", "Buy as well. Cheapest renewal of any option and gives you a .com to redirect."],
   ["@backprop.courses", "$1.99", "$35.56", "Cheapest entry. More literal, slightly weaker as a brand."],
   ["@coursemap.dev", "$13.00", "$13.00", "Best total cost of ownership and flat renewal. Descriptive rather than brandable."],
   ["@latent.school", "$9.99", "$35.00", "Strong alternative name if Backprop feels too narrow."],
   ["@gradient.courses / epoch.courses", "$1.99", "$35.56", "Both available and both good names. Epoch risks confusion with a well known AI research organisation."]],
  [40 * mm, 20 * mm, 20 * mm, 85 * mm], align_center=(1, 2)))
s.append(callout("THE ONE BRAND RISK, SAID OUT LOUD",
  "backprop.com, backprop.ai, backprop.io, backprop.dev and backprop.app are all already registered by other "
  "people. You can own backprop.school and learnbackprop.com, but you cannot ever upgrade to the obvious .com "
  "or .ai. If that bothers you, pick coursemap.dev or latent.school instead. Checked against the registry on "
  "12 November 2026.", bg="#fdf1f1", bar="#9b1c1c"))

s.append(Paragraph("WHAT IS ALREADY BUILT", H2))
s.append(table(
  ["Piece", "State"],
  [["@Course database", "%d courses across %d providers, each with cost, hours, level, topic, track, whether a "
    "certificate is awarded, and a written note on whether it is worth taking. %d are free." % (N, len(D["platforms"]), NFREE)],
   ["@Eight role tracks", "AI Engineer, ML Engineer, Data Scientist, MLOps and Platform, Research, Systems and GPU, "
    "Product Builder, Complete Beginner. Each filters the catalogue to what that role needs."],
   ["@Retired exam ledger", "Five 2026 retirements with their replacements, front and centre on the page. This is the wedge made visible."],
   ["@The site", "One self-contained static page, no build step, no backend, no tracking. Progress saves per browser. "
    "Search, plus filters for cost, level, topic and provider."],
   ["@Logo and brand", "Original mark: a gradient flowing backwards through three network layers. Plain SVG, scales anywhere."],
   ["@Deployment", "dist/ folder ready. Drag onto vercel.com/new, or run vercel --prod. No configuration needed."]],
  [36 * mm, 129 * mm]))

s.append(Paragraph("IF YOU DO BUILD IT: THE FIRST FOUR MOVES", H2))
s.append(table(
  ["#", "Move", "Why this order"],
  [["1", "Ship it on backprop.school this week, free, no sign-up.",
    "It is already built. A live URL is worth more than a better plan."],
   ["2", "Add a dated changelog showing what you re-verified and when.",
    "The freshness claim is the whole product. If it is not visible and dated, nobody believes it, and you have no moat."],
   ["3", "Add three more university module lists beside UEL.",
    "Degree overlap filtering is the defensible feature. Two universities is a feature; twenty is a product."],
   ["4", "Take it to the UEL careers team and ask what they would pay for.",
    "Answers the business model question with evidence instead of a guess, and costs you one meeting."]],
  [8 * mm, 62 * mm, 95 * mm]))

s.append(Spacer(1, 9))
s.append(Paragraph(
  "Sources for the course data, all retrieved 12 November 2026: nvidia.com/en-us/training and NVIDIA DLI "
  "certification pages; academy.openai.com and cookbook.openai.com; anthropic.skilljar.com and academy.claude.com; "
  "doc.rust-lang.org/book, rustlings, rust-book.cs.brown.edu, google.github.io/comprehensive-rust, github.com/huggingface/candle; "
  "react.dev/learn and nextjs.org/learn; course.fast.ai; freecodecamp.org; elementsofai.com; introtodeeplearning.com; "
  "cs224n and cs229 Stanford course pages; fullstackdeeplearning.com; wandb.ai/site/courses; github.com/microsoft/AI-For-Beginners; "
  "huggingface.co/learn; academy.langchain.com; deeplearning.ai/courses; pll.harvard.edu; education.oracle.com and "
  "blogs.oracle.com/oracleuniversity; aws.amazon.com/training and aws.amazon.com/certification; learn.microsoft.com; "
  "datacamp.com; coursera.org; kaggle.com/learn; developers.google.com/machine-learning/crash-course; linkedin.com/learning. "
  "Domain availability and pricing checked against the registry on 12 November 2026 and will change.", NOTE))

doc = SimpleDocTemplate("/home/claude/backprop/Backprop_Business_Case.pdf", pagesize=A4,
                        leftMargin=22 * mm, rightMargin=23 * mm, topMargin=18 * mm, bottomMargin=16 * mm,
                        title="Backprop: assessment, brand and build", author="Prepared for Jo Osei-Bonsu")


def footer(canvas, d):
    canvas.saveState()
    canvas.setStrokeColor(LINE); canvas.setLineWidth(0.4)
    canvas.line(22 * mm, 12 * mm, A4[0] - 23 * mm, 12 * mm)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(22 * mm, 8 * mm, "Backprop: honest assessment, brand and what is built")
    canvas.drawRightString(A4[0] - 23 * mm, 8 * mm, "Page %d" % d.page)
    canvas.restoreState()


doc.build(s, onFirstPage=footer, onLaterPages=footer)
print("built")
