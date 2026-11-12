import json

d = json.load(open("/home/claude/backprop/courses.json"))

# ---------------- new platforms ----------------
d["platforms"].update({
 "ibm": {"name": "IBM", "kind": "mixed"},
 "ka":  {"name": "Khan / 3Blue1Brown", "kind": "free"},
 "owasp": {"name": "OWASP", "kind": "free"},
 "oss": {"name": "Open source / community", "kind": "free"},
})

# ---------------- new topics ----------------
d["topics"].update({
 "math": "Maths foundations",
 "de":   "Data engineering and SQL",
 "sec":  "AI security and red-teaming",
 "rl":   "Reinforcement learning",
 "qc":   "Quantum computing",
 "aud":  "Speech and audio",
 "ts":   "Time series and forecasting",
 "career": "Career, interview and portfolio",
})

TRACKS = {
 "math": ["mle", "ds", "res", "new"], "de": ["ops", "ds", "mle"],
 "sec": ["aie", "ops", "res"], "rl": ["res", "mle"],
 "qc": ["res", "sys"], "aud": ["aie", "res"],
 "ts": ["ds", "mle"], "career": ["aie", "mle", "ds", "new", "prod"],
}

# (platform, name, topic, cost, hours, core, cert, url, why, level)
NEW = [
 # ---------------- IBM ----------------
 ("ibm", "IBM SkillsBuild: AI Fundamentals", "llm", "freecert", "~10 hrs", True, True,
  "https://skillsbuild.org/",
  "Free, and the badge is hosted on Credly, which matters more than it sounds: an employer can verify it, unlike the unverifiable PDF most free courses hand out. Machine learning concepts, NLP and responsible AI. Keep one distinction straight: IBM SkillsBuild is free; IBM's professional certificates on Coursera are a subscription. Same brand, different wallet.", "beginner"),
 ("ibm", "IBM SkillsBuild: AI Literacy", "eth", "freecert", "~4 hrs", False, True,
  "https://skillsbuild.org/",
  "Free with a credential. Recognising AI and using it responsibly. Four hours, and the right thing to send a non-technical friend or colleague.", "beginner"),
 ("ibm", "IBM SkillsBuild: 100+ free courses and badges", "career", "freecert", "2 to 20+ hrs each", False, True,
  "https://skillsbuild.org/",
  "100% free learning across AI, cybersecurity, data and cloud, with verifiable digital credentials. One honest caveat IBM states itself: it is a training platform, not an internship, scholarship or job offer. Do not describe a badge on your CV as a degree or a separate IBM certification.", "beginner"),
 ("ibm", "Cognitive Class by IBM", "ml", "freecert", "self-paced", False, True,
  "https://cognitiveclass.ai/",
  "Free, with badges. IBM's older technical learning platform, still live, with hands-on data science and ML courses in notebooks. Less polished than SkillsBuild and more technical, which for you is the right trade.", "intermediate"),
 ("ibm", "IBM Data Science Professional Certificate", "ml", "sub", "multi-month", False, True,
  "https://www.ibm.com/training/",
  "The best known of IBM's professional certificates. Comprehensive and well structured, but it is a subscription and it overlaps heavily with your MSc. Take it only if you want the IBM name on the CV rather than the knowledge.", "beginner"),
 ("ibm", "IBM Generative AI Engineering Professional Certificate", "llm", "sub", "multi-month", False, True,
  "https://www.ibm.com/training/",
  "IBM's newer generative AI engineering pathway. Reasonable content, but check it against the free Hugging Face, Anthropic and LangChain Academy courses first: they cover the same ground, are first-party, and cost nothing.", "intermediate"),
 ("ibm", "IBM Data Engineering Professional Certificate", "de", "sub", "multi-month", True, True,
  "https://www.ibm.com/training/",
  "The strongest of IBM's certificates for your purposes, because data engineering is the gap in almost every AI Engineer profile. Pipelines, warehousing, ETL, SQL at depth.", "intermediate"),
 ("ibm", "IBM Applied AI Developer", "llm", "sub", "multi-month", False, True,
  "https://www.ibm.com/training/",
  "Building and deploying AI applications on IBM's stack. Useful mainly if you are targeting an employer that runs IBM watsonx.", "intermediate"),
 ("ibm", "IBM Cybersecurity Analyst Professional Certificate", "sec", "sub", "multi-month", False, True,
  "https://www.ibm.com/training/",
  "Not AI, but it connects to your existing networking and security certifications, and AI security roles increasingly want both.", "intermediate"),
 ("ibm", "IBM Quantum Learning and Qiskit", "qc", "free", "self-paced", False, False,
  "https://www.ibm.com/quantum",
  "Free. IBM's quantum courses and the Qiskit SDK, with access to real quantum hardware on the free tier. Not useful for an AI Engineer job today. Genuinely interesting if you want a research angle nobody else in your cohort has, and King's and Oxford both teach quantum modules alongside AI.", "advanced"),

 # ---------------- Maths foundations ----------------
 ("ka", "Essence of Linear Algebra (3Blue1Brown)", "math", "free", "~3 hrs", True, False,
  "https://www.3blue1brown.com/topics/linear-algebra",
  "Free. The series that makes eigenvectors and matrix multiplication finally mean something geometrically rather than procedurally. Watch this before any maths-heavy ML course and the course gets easier.", "beginner"),
 ("ka", "Khan Academy: Linear Algebra, Probability and Statistics", "math", "free", "self-paced", True, False,
  "https://www.khanacademy.org/math/linear-algebra",
  "Free. The actual practice to go with the intuition. Vectors, matrices, eigenvalues, then probability and statistics. Unglamorous and the reason most people stall in deep learning.", "beginner"),
 ("cs", "Mathematics for Machine Learning (Imperial College London)", "math", "audit", "~4 months", True, True,
  "https://www.coursera.org/specializations/mathematics-machine-learning",
  "Free to audit. Linear algebra, multivariate calculus and PCA, taught specifically for machine learning rather than as pure maths. The single best structured fix if your maths is the weak link.", "intermediate"),
 ("oss", "StatQuest", "math", "free", "self-paced", False, False,
  "https://statquest.org/",
  "Free. Statistics and machine learning explained one concept at a time, clearly and without pretence. The standard answer when someone says they do not understand p-values, ROC curves or gradient descent.", "beginner"),
 ("un", "MIT 18.06 Linear Algebra (OpenCourseWare)", "math", "free", "~1 semester", False, False,
  "https://ocw.mit.edu/",
  "Free. Gilbert Strang's course, and still the reference. Heavy, and worth it only if you want to go into research rather than application.", "advanced"),

 # ---------------- Data engineering and SQL ----------------
 ("oss", "SQLBolt", "de", "free", "~4 hrs", True, False,
  "https://sqlbolt.com/",
  "Free, interactive, no sign-up. SQL from nothing to joins and subqueries in an afternoon. Almost every data and AI role tests SQL and almost every course list forgets it.", "beginner"),
 ("oss", "Mode SQL Tutorial", "de", "free", "~6 hrs", False, False,
  "https://mode.com/sql-tutorial/",
  "Free. Intermediate and advanced SQL with real analytics problems, including window functions and performance tuning.", "intermediate"),
 ("dc", "Data Engineer career track", "de", "sub", "~80 hrs", False, True,
  "https://www.datacamp.com/tracks/career",
  "Pipelines, warehousing, Airflow and Spark. The structured route if the IBM data engineering certificate looks too long.", "intermediate"),
 ("oss", "dbt Fundamentals", "de", "free", "~5 hrs", False, True,
  "https://www.getdbt.com/",
  "Free with a certificate. dbt is how modern data teams transform data, and it appears in data engineering job specs constantly. Short, and almost nobody applying for AI roles has it.", "intermediate"),

 # ---------------- AI security and red-teaming ----------------
 ("owasp", "OWASP Top 10 for LLM Applications", "sec", "free", "~3 hrs", True, False,
  "https://owasp.org/",
  "Free. Prompt injection, insecure output handling, training data poisoning, model denial of service. This is the vocabulary security-conscious employers expect, and it is a reading list rather than a course, so it costs you an afternoon.", "intermediate"),
 ("oss", "Gandalf by Lakera: prompt injection practice", "sec", "free", "~1 hr", False, False,
  "https://gandalf.lakera.ai/",
  "Free. A game where you try to extract a secret from an LLM through increasingly hardened defences. The fastest way to actually understand prompt injection rather than read about it. Genuinely good interview material.", "beginner"),
 ("hf", "Hugging Face: red-teaming and model safety material", "sec", "free", "self-directed", False, False,
  "https://huggingface.co/learn",
  "Free. Evaluation and safety material across the HF courses and cookbook. Thinner than the rest of this topic, which reflects the field rather than the list.", "advanced"),

 # ---------------- Reinforcement learning ----------------
 ("hf", "Hugging Face Deep Reinforcement Learning Course", "rl", "free", "8 units", True, True,
  "https://huggingface.co/learn/deep-rl-course/unit0/introduction",
  "Free and certified. Q-learning through to policy gradients and PPO, training agents you can push to the Hub and compare on a leaderboard. The best free RL course that ends in something you can show someone.", "intermediate"),
 ("oa", "Spinning Up in Deep RL (OpenAI)", "rl", "free", "self-paced", False, False,
  "https://spinningup.openai.com/",
  "Free. OpenAI's own educational RL resource: the key algorithms, the maths behind them, and clean reference implementations. Written to get people productive in RL research quickly.", "advanced"),
 ("oss", "DeepMind x UCL Reinforcement Learning lecture series", "rl", "free", "~10 lectures", False, False,
  "https://www.youtube.com/@GoogleDeepMind",
  "Free. The canonical lecture series. Dense, mathematical, and the standard reference if you want RL properly rather than practically.", "advanced"),

 # ---------------- Speech and audio ----------------
 ("hf", "Hugging Face Audio Course", "aud", "free", "multi-unit", False, True,
  "https://huggingface.co/learn/audio-course/chapter0/introduction",
  "Free with a certificate. Audio classification, speech recognition with Whisper, and text to speech. Relevant if you are entering voice-related work, and close to nobody in an AI Engineer applicant pool has done it.", "intermediate"),

 # ---------------- Time series ----------------
 ("oss", "Forecasting: Principles and Practice (Hyndman and Athanasopoulos)", "ts", "free", "self-paced", True, False,
  "https://otexts.com/fpp3/",
  "Free online textbook and the standard reference for forecasting. Time series is everywhere in real commercial data and is skipped by almost every AI curriculum, including most of the ones on this page.", "intermediate"),
 ("gg", "Kaggle Learn: Time Series", "ts", "free", "~4 hrs", False, False,
  "https://www.kaggle.com/learn",
  "Free. Trend, seasonality and lag features, applied. The quick practical version of the textbook above.", "beginner"),

 # ---------------- Career ----------------
 ("oss", "Tech Interview Handbook", "career", "free", "reference", True, False,
  "https://www.techinterviewhandbook.org/",
  "Free. Behavioural questions, resume structure, negotiation and the algorithm topics that actually come up, ranked by frequency. Use it as a checklist rather than a course.", "beginner"),
 ("oss", "ML system design interview preparation", "career", "free", "self-directed", True, False,
  "https://github.com/",
  "Free, via open repositories and papers. AI and ML interviews increasingly centre on system design: how you would build a recommender, a RAG pipeline or an evaluation harness at scale. Practise explaining architecture out loud, because that is the actual test.", "advanced"),
 ("oss", "Write up every project as a public case study", "career", "free", "ongoing", True, False,
  "https://github.com/",
  "Free and the highest return item on this entire page. The problem, your architecture, what you measured, what broke, what you would change. Hiring managers read this and skip the certificate list.", "beginner"),
]

existing = {c["id"] for c in d["courses"]}
i = 0
for p, name, topic, cost, hrs, core, cert, url, why, level in NEW:
    i += 1
    cid = "x%02d" % i
    assert cid not in existing
    d["courses"].append({
        "id": cid, "name": name, "platform": p, "topic": topic, "cost": cost,
        "hours": hrs, "core": core, "cert": cert, "url": url, "why": why,
        "level": level, "tracks": TRACKS.get(topic, ["aie"]),
        "phase": 0,
    })

for c in d["courses"]:
    if c["level"] == "beginner" and "new" not in c["tracks"]:
        c["tracks"] = c["tracks"] + ["new"]

d["updated"] = "2026-11-12"
json.dump(d, open("/home/claude/backprop/courses.json", "w"), indent=1)

free = sum(1 for c in d["courses"] if c["cost"] in ("free", "audit", "beta", "freecert"))
print("courses:", len(d["courses"]), "| platforms:", len(d["platforms"]),
      "| topics:", len(d["topics"]), "| free:", free,
      "| certs:", sum(1 for c in d["courses"] if c["cert"]))
