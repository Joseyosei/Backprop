# Changelog

Freshness is the product. Every verification pass gets an entry here with the date it was checked.

## 2026-11-16

**This pass verified almost nothing, and the data was left alone.** The scheduled run could not read
provider pages. The first web fetches raised a permission prompt, there was nobody at the desk to answer
it, and once it timed out the fetch layer stopped sending requests for the rest of the session. Search
still worked, but it returns titles and links only, and a title is not a price. So nothing was written to
`courses.json` or `universities.json`. That is the only correct outcome here: every exam code, price and
free-tier claim in the data is still carrying its 14 November check, not a 16 November one. The "Verified
by hand" date on the page was left at 14 November deliberately, because moving it would assert a check
that did not happen.

**One page was read before the block, and it raises a question for the next pass.** The AI-901 exam page
on learn.microsoft.com gives the title as "Exam AI-901: Microsoft Azure AI Fundamentals (beta)" and its
retirement date field as none. Two things follow. The exam is live, so that entry is not sending anyone at
a dead exam. But it is still flagged beta, and the page prints no dollar figure at all, only that the
price depends on the country or region where the exam is proctored. The "around USD 99" in the AI-901
entry has no first-party source standing behind it as of today. It was left in place rather than changed,
per the rule about leaving previous values, and it needs confirming or cutting next pass.

**Everything else is unchecked.** Outstanding, in priority order: AWS AIF-C01 and MLA-C02 codes and
prices; Microsoft AI-103 and AI-300 codes, prices and retirement fields; NVIDIA NCA-GENL and NCA-GENM at
$125; Oracle's free Foundations certifications including 1Z0-1122-26 and 1Z0-1157-26, which is the single
most likely thing in this data to have quietly moved behind a paywall; the DeepLearning.AI beta free
window; the IBM SkillsBuild and Microsoft Learn free tiers; genuinely new first-party courses; and the 79
distinct URLs for dead links.

`python3 verify.py` passes. 164 courses, 125 free, 23 providers, 20 topics, 22 degrees, all unchanged.
Rebuilding `dist/index.html` produced a byte-identical file, which at least confirms the build is still
reproducible from the committed data.

## 2026-11-14

**Added a maintenance procedure and an automated integrity check.** `MAINTENANCE.md` sets out the one
rule (nothing enters the data that was not read off the provider's own pages), the authoritative source
per provider, and the order of each verification pass. `verify.py` checks every course for a resolvable
platform, topic and cost key, an https URL, a usable note, and no duplicate ids, then cross-checks the
counts in the README and the page against the data so the totals cannot silently go stale.

**One bug found by the checker on its first run:** the MIT 6.S191 entry used an http URL. Fixed.

**Added `build_site.py`** so rebuilding `dist/index.html` is one command rather than a hand-assembled step.

Nothing else moved. Prices, exam codes and free tiers re-checked against the 12 November pass and
unchanged: no new retirements, Oracle's Foundations certifications still free including the exam, the
DeepLearning.AI beta window still open.

## 2026-11-12

**Added IBM.** SkillsBuild free courses and Credly-backed badges, Cognitive Class, and the professional
certificate pathways including data engineering, generative AI engineering and applied AI. Also IBM
Quantum Learning and Qiskit.

**Added eight topics.** Maths foundations, data engineering and SQL, AI security and red-teaming,
reinforcement learning, quantum computing, speech and audio, time series and forecasting, and career and
interview. Maths and data engineering were the two biggest gaps in the previous list: almost every AI
curriculum assumes linear algebra and SQL and teaches neither.

**Added 31 courses** across those topics, including the Hugging Face Deep RL and Audio courses, OpenAI
Spinning Up, the OWASP Top 10 for LLM Applications, Lakera's Gandalf for prompt injection practice,
3Blue1Brown and Khan Academy for maths, Imperial's Mathematics for Machine Learning, SQLBolt, dbt
Fundamentals, and the Hyndman forecasting textbook.

**Added degree overlap mapping.** 22 AI and data science master's programmes across the UK, US, China,
Japan, South Korea and the UAE. 16 verified against the institution's own course pages: UCL (3), King's
College London (2), Oxford, Manchester (2), LSE, UEL, MBZUAI (4), Institute of Science Tokyo, Penn State.
Cambridge, Tsinghua, Peking, UTokyo, KAIST and SNU are listed with coverage estimates and flagged
unverified, because their module lists are not published in a form that can be checked properly.

Count is now 164 courses, 23 providers, 20 topics, 125 free.

## 2026-11-11

**Added AWS and Microsoft.** Skill Builder's free tier, AWS Educate, the AI Practitioner and ML Engineer
Associate paths, Microsoft Learn and Applied Skills.

**Flagged five retired exams.** Microsoft AI-900, AI-102 and DP-100 all retired in June 2026, replaced by
AI-901, AI-103 and AI-300. AWS retired the Machine Learning Specialty in March 2026 and moved the ML
Engineer Associate from MLA-C01 to MLA-C02. Most roadmaps in circulation still name the retired ones.

**Added LangChain Academy, Harvard, Oracle and LinkedIn Learning.** Oracle is the standout: Foundations
level courses and their proctored exams are free, including two AI certifications.

## 2026-11-09

First build. DataCamp, Google, Coursera, Hugging Face and DeepLearning.AI, assembled while checking
whether a paid AI engineering bootcamp was worth buying. It was not.
