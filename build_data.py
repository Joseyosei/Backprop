import json, os

src = json.load(open("/home/claude/plan.json"))

PLAT = {
 "dc":  ("DataCamp", "sub"),      "gg": ("Google", "free"),
 "cs":  ("Coursera", "mixed"),    "hf": ("Hugging Face", "free"),
 "dl":  ("DeepLearning.AI", "mixed"), "lc": ("LangChain", "free"),
 "hv":  ("Harvard", "mixed"),     "or": ("Oracle", "free"),
 "li":  ("LinkedIn", "sub"),      "aws": ("AWS", "mixed"),
 "ms":  ("Microsoft", "mixed"),   "nv": ("NVIDIA", "mixed"),
 "rs":  ("Rust", "free"),         "rc": ("React", "free"),
 "oa":  ("OpenAI", "free"),       "an": ("Anthropic", "free"),
 "ff":  ("fast.ai", "free"),      "fc": ("freeCodeCamp", "free"),
 "un":  ("University", "free"),
}

TOPICS = {
 "ml":"Machine learning","llm":"LLMs and prompting","rag":"RAG and vector DBs",
 "agt":"AI agents","eval":"Fine-tuning and evaluation","ops":"MLOps, cloud and certs",
 "cv":"Computer vision","eth":"Ethics and governance","py":"Python and data",
 "port":"Portfolio and tooling","sys":"Systems, GPU and Rust","web":"Web and product",
}

# tracks: aie=AI Engineer, mle=ML Engineer, ds=Data Scientist, ops=MLOps,
#         res=Research, new=Complete beginner, sys=Systems/GPU, prod=Product builder
TRACK_BY_TOPIC = {
 "ml":["mle","ds","res"], "llm":["aie","prod"], "rag":["aie","prod"],
 "agt":["aie","prod"], "eval":["aie","mle","res"], "ops":["ops","mle"],
 "cv":["res","mle"], "eth":["res","new"], "py":["new","ds"],
 "port":["aie","prod"], "sys":["sys","ops"], "web":["prod"],
}

LEVEL_HINT = [("Fundamentals","beginner"),("Introduction","beginner"),("Intro","beginner"),
              ("101","beginner"),("Explained","beginner"),("Essentials","beginner"),
              ("Crash Course","beginner"),("Advanced","advanced"),("Professional","advanced"),
              ("Deep Dive","advanced"),("Specialization","intermediate")]

def level_of(name, core):
    for k, v in LEVEL_HINT:
        if k in name:
            return v
    return "intermediate" if core else "intermediate"

courses = []
for pi, ph in enumerate(src["DATA"], 1):
    for c in ph["items"]:
        courses.append({
            "id": c["id"], "name": c["name"], "platform": c["p"], "topic": c["topic"],
            "cost": c["cost"], "hours": c["hrs"], "core": c["core"], "cert": c["cert"],
            "url": c["url"], "why": c["why"], "phase": pi,
            "level": level_of(c["name"], c["core"]),
            "tracks": TRACK_BY_TOPIC[c["topic"]],
        })

NEW = [
 # ---------------- NVIDIA ----------------
 ("nv","Generative AI Explained","llm","free","2 hrs",False,False,
  "https://www.nvidia.com/en-us/training/",
  "Free, no code required. Concepts, mechanisms and use cases of generative AI from the company whose GPUs run almost all of it. The cleanest non-technical on-ramp of any vendor.","beginner"),
 ("nv","Agentic AI Explained","agt","free","1 hr",False,False,
  "https://www.nvidia.com/en-us/training/",
  "Free, one hour, no code. What agentic AI actually is, before you spend money learning to build it.","beginner"),
 ("nv","Building LLM Applications With Prompt Engineering","llm","paid","$30 to $90",True,True,
  "https://www.nvidia.com/en-us/training/",
  "Paid self-paced DLI course and the recommended starting point for the NCA-GENL certification. Carries a certificate because it has an assessment, unlike the free DLI courses.","intermediate"),
 ("nv","Augment LLMs Using Retrieval Augmented Generation","rag","paid","$30 to $90",True,True,
  "https://www.nvidia.com/en-us/training/",
  "NVIDIA's own RAG course, pitched at exactly the depth the NCA-GENL exam tests. Pair with the DeepLearning.AI RAG course for the vendor-neutral view.","intermediate"),
 ("nv","Building Agentic AI Applications with LLMs","agt","paid","8 hrs, $90",True,True,
  "https://www.nvidia.com/en-us/training/",
  "Eight hours, $90, with a certificate. NVIDIA's deepest self-paced agent course and a credible line on a CV because it is assessed.","advanced"),
 ("nv","Securing Agents with NemoClaw and OpenShell","agt","free","4 hrs",False,False,
  "https://www.nvidia.com/en-us/training/",
  "Free and four hours. Agent security is barely taught anywhere and increasingly asked about in interviews.","intermediate"),
 ("nv","Fundamentals of Accelerated Computing with CUDA","sys","paid","$30 to $90",False,True,
  "https://www.nvidia.com/en-us/training/",
  "CUDA C++ and Python with Numba. The layer underneath every deep learning framework. Rare and valuable if you want infrastructure roles rather than app roles.","advanced"),
 ("nv","NCA-GENL: Generative AI LLMs certification","ops","fee","1 hr exam",True,True,
  "https://www.nvidia.com/en-us/learn/certification/",
  "$125, around 50 to 60 questions, digital badge valid two years. Covers LLM fundamentals, transformer architecture, RAG, prompt engineering, fine-tuning and deployment. The common entry point for an NVIDIA credential and a strong differentiator because few candidates hold it.","intermediate"),
 ("nv","NCA-GENM: Generative AI Multimodal certification","ops","fee","1 hr exam",False,True,
  "https://www.nvidia.com/en-us/learn/certification/",
  "$125. Designing and managing systems that handle text, image and audio together. Take it instead of NCA-GENL only if multimodal is your direction.","intermediate"),

 # ---------------- OpenAI Academy ----------------
 ("oa","OpenAI Academy","llm","free","self-paced",True,False,
  "https://academy.openai.com/",
  "Free. OpenAI's own learning platform with workshops, sessions and community learning, including prompt engineering taught by the people who build the models. Free and first-party, so it belongs in any LLM path regardless of which vendor you end up using.","beginner"),
 ("oa","OpenAI Cookbook","port","free","reference",True,False,
  "https://cookbook.openai.com/",
  "Free. Runnable recipes for structured outputs, function calling, evals, embeddings and RAG. Treat it as the reference you build from, not a course to finish.","intermediate"),

 # ---------------- Anthropic / Claude Academy ----------------
 ("an","Claude 101","llm","free","2.5 hrs, 13 lessons",False,True,
  "https://anthropic.skilljar.com/",
  "Free with a completion certificate and no Claude subscription needed. The entry point: what Claude is, how to prompt it well and how to use it responsibly. Non-technical.","beginner"),
 ("an","Building with the Claude API","llm","free","self-paced",True,True,
  "https://anthropic.skilljar.com/",
  "Free with a certificate. The definitive first-party course for building products on Claude. Direct counterpart to the OpenAI API courses, and worth doing both so you are not locked to one vendor.","intermediate"),
 ("an","Introduction to Model Context Protocol","agt","free","self-paced",True,True,
  "https://anthropic.skilljar.com/",
  "Free with a certificate. MCP is how agents connect to tools and data, and it now appears in job specs. First-party and free, which makes paid MCP courses hard to justify.","intermediate"),
 ("an","Model Context Protocol: In Depth","agt","free","self-paced",True,True,
  "https://anthropic.skilljar.com/",
  "Free. Build MCP servers and clients in TypeScript from scratch. The deep version, and genuinely rare material.","advanced"),
 ("an","Introduction to Agent Skills","agt","free","self-paced",True,True,
  "https://anthropic.skilljar.com/",
  "Free with a certificate. Packaging reusable capabilities for agents, which is where agent engineering is heading.","intermediate"),
 ("an","Introduction to Subagents","agt","free","self-paced",False,True,
  "https://anthropic.skilljar.com/",
  "Free. Orchestrating multiple agents. Pairs with the crewAI and AutoGen short courses for a framework-independent view.","intermediate"),
 ("an","Claude Code 101 and Claude Code in Action","port","free","self-paced",False,True,
  "https://anthropic.skilljar.com/",
  "Free, two courses, both with certificates. AI-assisted coding, terminal workflows and debugging. Tooling rather than theory, but the speed you build your portfolio at is itself a hiring signal.","intermediate"),
 ("an","AI Fluency: Framework and Foundations","eth","free","self-paced",False,True,
  "https://anthropic.skilljar.com/",
  "Free with a certificate. How to think and communicate with AI systems. There is also an AI Fluency for Students version. Useful if you teach, mentor or write about AI.","beginner"),
 ("an","Claude with Amazon Bedrock and Google Vertex AI","ops","free","self-paced",False,True,
  "https://anthropic.skilljar.com/",
  "Free, two courses. Running Claude inside AWS and Google Cloud. Directly relevant if you are also taking the AWS or Google credentials in this list.","advanced"),

 # ---------------- Rust ----------------
 ("rs","The Rust Programming Language (the Book)","sys","free","15 modules",True,False,
  "https://doc.rust-lang.org/book/",
  "Free and official. The authoritative introduction, maintained by the Rust team. Best free introduction to Rust that exists, though not enough on its own to get hired in Rust: it is light on async, architecture and production patterns.","beginner"),
 ("rs","Rustlings","sys","free","94 exercises",True,False,
  "https://github.com/rust-lang/rustlings",
  "Free and official. Fix 94 broken programs in your terminal, chapter by chapter alongside the Book. The developers who credit the Book for their success almost universally did Rustlings with it. Do not read the Book without this.","beginner"),
 ("rs","Brown University interactive Rust Book","sys","free","same as the Book",False,False,
  "https://rust-book.cs.brown.edu/",
  "Free. The official text plus inline quizzes and ownership visualisations that show what the borrow checker sees. The best version for the ownership and lifetimes chapters.","beginner"),
 ("rs","Comprehensive Rust (Google)","sys","free","multi-day",False,False,
  "https://google.github.io/comprehensive-rust/",
  "Free. Google's own multi-day Rust course, used to train their engineers. Faster and denser than the Book if you already know another systems language.","intermediate"),
 ("rs","Rust by Example","sys","free","reference",False,False,
  "https://doc.rust-lang.org/rust-by-example/",
  "Free and official. Runnable snippets for quick syntax lookups beside the Book.","beginner"),
 ("rs","Candle and Burn: Rust for AI inference","sys","free","self-directed",False,False,
  "https://github.com/huggingface/candle",
  "Free, via the project docs. Candle is Hugging Face's Rust framework built for inference rather than training, with WebAssembly support for in-browser AI and small binaries for edge deployment. Burn covers training and inference. Be realistic: the AI ecosystem is Python and C, and Rust's ML frameworks are still nascent. Learn this for inference engines, edge AI and infrastructure, not to replace Python.","advanced"),

 # ---------------- React ----------------
 ("rc","React: official Learn tutorial","web","free","self-paced",True,False,
  "https://react.dev/learn",
  "Free and official. Components, state, hooks and effects, with an interactive tic-tac-toe build. You need a front end to make any AI project demoable, and a bare Streamlit app no longer impresses anyone.","beginner"),
 ("rc","Next.js Learn course","web","free","self-paced",True,False,
  "https://nextjs.org/learn",
  "Free and official. The React framework most AI products ship on, with routing, server rendering and data fetching. Deploys to Vercel in one step, which is how most AI side projects reach the web.","intermediate"),
 ("rc","Build a chat UI with streaming responses","web","free","build",True,False,
  "https://react.dev/learn",
  "A build task, not a course. Token streaming, loading states, error handling, conversation history and cost display. The gap between an AI demo and an AI product is almost entirely here.","intermediate"),

 # ---------------- fast.ai ----------------
 ("ff","Practical Deep Learning for Coders","ml","free","~8 weeks",True,False,
  "https://course.fast.ai/",
  "Free. The famous top-down course: you train and deploy a working model in lesson one, then learn the theory underneath. If the maths-first courses have ever put you off deep learning, start here instead.","intermediate"),
 ("ff","From Deep Learning Foundations to Stable Diffusion","ml","free","~10 weeks",False,False,
  "https://course.fast.ai/Lessons/part2.html",
  "Free. Part two, building diffusion models from scratch. Serious depth, and a strong answer to 'can you implement it, not just call it'.","advanced"),

 # ---------------- freeCodeCamp ----------------
 ("fc","Machine Learning with Python certification","ml","free","~300 hrs",False,True,
  "https://www.freecodecamp.org/learn/machine-learning-with-python/",
  "Free, including the certification. TensorFlow, neural networks and five required projects. The project requirement is the point: a certificate nobody can get without shipping code.","intermediate"),
 ("fc","Data Analysis with Python certification","py","free","~300 hrs",False,True,
  "https://www.freecodecamp.org/learn/data-analysis-with-python/",
  "Free, including the certification. NumPy, Pandas and Matplotlib with five projects. A genuine free alternative to the paid DataCamp data courses.","beginner"),

 # ---------------- Universities and open courseware ----------------
 ("un","Elements of AI (University of Helsinki)","eth","free","~30 hrs",False,True,
  "https://www.elementsofai.com/",
  "Free with a certificate, translated into dozens of languages, and built as a public good rather than a funnel. The best non-technical AI course in the world and the right first step for anyone outside computer science.","beginner"),
 ("un","MIT 6.S191: Introduction to Deep Learning","ml","free","~1 week",True,False,
  "http://introtodeeplearning.com/",
  "Free. MIT's intensive deep learning bootcamp, refreshed every year with current material and released publicly with labs. One of the few free courses that keeps pace with the field.","intermediate"),
 ("un","Stanford CS224N: NLP with Deep Learning","ml","free","~10 weeks",False,False,
  "https://web.stanford.edu/class/cs224n/",
  "Free lecture materials and assignments. The transformer theory underneath every LLM you use, taught properly. Heavy, and worth it only if you want research or deep model work.","advanced"),
 ("un","Stanford CS229: Machine Learning","ml","free","~10 weeks",False,False,
  "https://cs229.stanford.edu/",
  "Free notes and problem sets. The rigorous mathematical treatment. The Andrew Ng Coursera specialization is the gentler version of this same material.","advanced"),
 ("un","Full Stack Deep Learning","ops","free","self-paced",True,False,
  "https://fullstackdeeplearning.com/",
  "Free. The course about everything around the model: project setup, data management, testing, deployment, monitoring and team structure. Covers the gap most courses leave and most interviews probe.","advanced"),
 ("un","Microsoft AI for Beginners (24 lessons)","ml","free","24 lessons",False,False,
  "https://github.com/microsoft/AI-For-Beginners",
  "Free on GitHub. A full open curriculum with quizzes and notebooks. Good structure, zero cost, no sign-up, and you can fork it.","beginner"),
 ("un","Weights & Biases free courses","eval","free","self-paced",False,True,
  "https://wandb.ai/site/courses/",
  "Free with certificates. Experiment tracking, LLM evaluation, model CI/CD and MLOps from the team whose tool most ML teams actually use for this. Experiment tracking is assumed knowledge in ML roles and taught almost nowhere else.","intermediate"),
]

for i, (p, name, topic, cost, hrs, core, cert, url, why, level) in enumerate(NEW, 1):
    courses.append({
        "id": "n%02d" % i, "name": name, "platform": p, "topic": topic, "cost": cost,
        "hours": hrs, "core": core, "cert": cert, "url": url, "why": why,
        "phase": 0, "level": level, "tracks": TRACK_BY_TOPIC[topic],
    })

# beginners need the gentle on-ramps whatever their topic
for c in courses:
    if c["level"] == "beginner" and "new" not in c["tracks"]:
        c["tracks"] = c["tracks"] + ["new"]

RETIRED = [
 ("Microsoft AI-900","Azure AI Fundamentals","Retired 30 June 2026","Take AI-901 instead"),
 ("Microsoft AI-102","Azure AI Engineer Associate","Retired 30 June 2026","Take AI-103 instead, a new certification rather than a rename"),
 ("Microsoft DP-100","Azure Data Scientist Associate","Retired 1 June 2026","Take AI-300 instead"),
 ("AWS MLS-C01","Machine Learning Specialty","Last exam 31 March 2026","Take Machine Learning Engineer Associate instead"),
 ("AWS MLA-C01","ML Engineer Associate, first version","Last English exam 28 Sept 2026","Take MLA-C02"),
]

out = {
 "updated": "2026-11-12",
 "platforms": {k: {"name": v[0], "kind": v[1]} for k, v in PLAT.items()},
 "topics": TOPICS,
 "tracks": {
   "aie": {"name": "AI Engineer", "blurb": "Build products on top of models: LLM APIs, RAG, agents, evaluation, deployment. The fastest growing of these roles."},
   "mle": {"name": "ML Engineer", "blurb": "Train, tune and ship models. Classical ML and deep learning plus the production layer."},
   "ds":  {"name": "Data Scientist", "blurb": "Analysis, statistics and modelling. Python and data foundations first, then machine learning."},
   "ops": {"name": "MLOps and Platform", "blurb": "Pipelines, deployment, monitoring and cloud. Where the cloud certifications pay off."},
   "res": {"name": "Research", "blurb": "The theory underneath: deep learning, NLP, computer vision, evaluation. University-grade material."},
   "sys": {"name": "Systems and GPU", "blurb": "CUDA, Rust, inference engines and edge AI. Small field, very few candidates, high leverage."},
   "prod":{"name": "Product Builder", "blurb": "Ship a working AI product end to end: model, API, front end, deploy."},
   "new": {"name": "Complete Beginner", "blurb": "No coding or AI background assumed. Free, gentle, well-made starting points only."},
 },
 "costs": {
   "free": "Free", "sub": "Subscription", "audit": "Audit free", "beta": "Free (beta)",
   "fee": "Exam fee", "freecert": "Free + free exam", "paid": "Paid",
 },
 "retired": [{"code": a, "name": b, "when": c, "instead": d} for a, b, c, d in RETIRED],
 "courses": courses,
}

os.makedirs("/home/claude/backprop", exist_ok=True)
json.dump(out, open("/home/claude/backprop/courses.json", "w"), indent=1)

free = sum(1 for c in courses if c["cost"] in ("free", "audit", "beta", "freecert"))
print("courses:", len(courses), "| platforms:", len(PLAT), "| free:", free,
      "| certs:", sum(1 for c in courses if c["cert"]))
for t in out["tracks"]:
    print("  track", t, sum(1 for c in courses if t in c["tracks"]))
