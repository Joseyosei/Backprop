# Changelog

Freshness is the product. Every verification pass gets an entry here with the date it was checked.

## 2026-11-23

**The fetch block that wasted the 16 November pass is solved, and the fix is worth writing down.**
Reading a URL straight out of `courses.json` is refused with a provenance error, which is what stopped
the last run dead. Pages become readable once the same session has seen them in a search result first.
So the working order is search for the provider's page, then read the URL the search returned. Every
figure below was read off a provider page in this session on that basis. Four URLs still refused and are
recorded as unverified rather than guessed.

**No exam retired since the last pass, so the retired ledger is unchanged.** All five entries in it still
stand. Every certification exam code in the data was re-read: AI-901, AI-103, AI-300, AIF-C01, MLA-C02,
NCA-GENL, NCA-GENM and the Oracle Foundations pair. None is dead. That is the project's headline claim and
it holds.

**Three invented-looking prices are gone.** This is the real change in this pass. AI-901 carried "around
USD 99" and AI-103 and AI-300 carried "around USD 165", and no Microsoft page prints any of them.
Microsoft's exam and certification pages say only that the price depends on the country or region where
the exam is proctored. The 16 November note flagged the AI-901 figure for confirming or cutting, and it is
cut. The AI-901 entry also lost the claim that Virtual Training Day vouchers "routinely cover it", which
no first-party page supports either. In exchange the entries now tell the reader the true and more useful
thing, which is that there is no single dollar price to look up.

**AI-901 has come out of beta.** On 16 November its page title read "(beta)". Today the word is gone, the
retirement date field reads none, the passing score is 700 and the English version carries an update date
of 15 April 2026. AI-103 and AI-300 both show no retirement date and no beta flag. The certification names
in the data were right, incidentally: the exams are titled Developing AI Apps and Agents on Azure and
Operationalizing Machine Learning and Generative AI Solutions, but the credentials they earn really are
Azure AI Apps and Agents Developer Associate and Machine Learning Operations Engineer Associate.

**MLA-C02 is still the beta, not the real exam, and the entry now says so.** The AWS page dated 17
November lists MLA-C02 as "Updated - Beta" at $75 with general availability dates marked TBD, and lists
the outgoing MLA-C01 as current at $150. Since MLA-C01's last English sitting was 28 September, MLA-C02 is
the only live English route while sitting in beta, which is a thing worth knowing before booking. One
oddity: the exam code row on that page prints "ME1-C02" while the body text says MLA-C02. The exam guides
index and the guide's own title both say MLA-C02, so that is what the data keeps and the AWS page looks
like it has a typo.

**AIF-C01 confirmed live and unchanged**, against the official exam guide at revision 1.2 of 29 October
2026: 50 scored questions plus 15 unscored, passing score 700, no successor and no beta in flight.

**Oracle is still free, but this data was overclaiming it.** Oracle University's own pages confirm the
important half: "Every Foundations-level course and certification stays free", and the free part covers
the lessons, the skill checks, the practice exams and the certification attempt itself, with as many
attempts as needed. The exams are not dead and not paywalled, which was the single biggest risk in this
file. What could not be confirmed is the word "proctored", which three Oracle entries used and one built a
selling line on. No Oracle page says it, and Oracle's own exam URLs for these read `exam-unproctored`. The
word is removed and the entries now say plainly not to describe these as proctored credentials. 1Z0-1157-26
is confirmed by Oracle's own announcement at 40 questions in 60 minutes with a 65 per cent pass mark and a
free exam. 1Z0-1122-26 could not be confirmed from a page body, only from an Oracle URL, so it stays as the
previous value.

**Two Oracle changes that do not touch this data but are worth logging.** Professional-level courses have
moved to paid access, and the OCI Architect Associate course and certification are now free. Neither has an
entry here. Oracle also confirms its certifications are valid 24 months, which is what the data already said.

**The DeepLearning.AI free window is open, with a catch that is new.** Three course pages all still read
"Course access is free for a limited time during the DeepLearning.AI learning platform beta!" with no end
date and no paywall, so the `beta` cost label survives. But graded assignments and certificates now sit
behind the paid PRO plan. The Agentic AI entry sold itself partly on its three graded programming
assignments, so that entry now carries the caveat. The free part is the videos.

**IBM is free, and one sentence of ours was putting words in IBM's mouth.** The site says "100% free
learning" and credentials are claimed through Credly, both confirmed. But the entry claimed IBM "states
itself" that SkillsBuild is not an internship, scholarship or job offer, and that statement is not on the
home page, the digital credentials page or the badge page. The caveat is good advice so it stays, now
labelled as our warning rather than an IBM quote.

**NVIDIA needed no change at all.** NCA-GENL and NCA-GENM both confirmed at $125, 50 to 60 questions, one
hour, remotely proctored, badge valid two years, no retirement notice. The data said exactly that.

**Added two genuinely new first-party AWS AI certifications**, both read off their official exam guides.
AWS Certified Generative AI Developer Professional (AIP-C01) is the useful one: 65 scored questions,
passing score 750, weighted towards foundation model integration at 31 per cent, with model training
explicitly out of scope. AWS Certified AI Business Strategist (AIB-C01) is listed for completeness with an
honest note to skip it, because AWS pitches it at people who champion AI rather than build it and states
that no coding is required.

**Held back on purpose: NVIDIA's NCP-GENL and NCP-AAI professional exams.** Both listed at $200 on
NVIDIA's certification page, and both would fit this map well. But their own pages print "(Coming soon)"
under the title while also showing a register link, and the detail came back from a summary of a truncated
page rather than verbatim text. That is not good enough to publish a price against, so nothing was added.
First thing to settle next pass.

**Dead links: partial sweep, nothing dead found.** Confirmed live and on topic this session:
skills.google/paths/183, academy.langchain.com/courses/intro-to-langgraph, the NVIDIA certification page,
skillsbuild.org, the Microsoft credentials and study guide pages, the AWS docs and certification pages,
three DeepLearning.AI course pages and the Oracle University blog. Four refused on provenance and are
unverified rather than dead: education.oracle.com, cognitiveclass.ai, gandalf.lakera.ai and otexts.com/fpp3.
The full 79-URL sweep was not done, because every URL needs a search before it can be read and that does
not scale to 79 in one pass.

**One pre-existing bug fixed.** The page footer still read "100 of the 133 courses are free", left over
from a build two versions ago. `verify.py` never caught it because it only checks that the right numbers
appear somewhere, not that wrong ones are absent. Now 125 of 166.

`python3 verify.py` passes. 166 courses, 125 free, 23 providers, 20 topics, 22 degrees. The hero date moves
to 23 November and the footer now states separately that the certification entries specifically were
re-read today, rather than implying the whole file was. `universities.json` was not touched and still
carries its 14 November date, because no university page was checked this pass.

**Outstanding for next pass**, in priority order: NVIDIA NCP-GENL and NCP-AAI once their pages settle;
1Z0-1122-26 confirmed from a page body rather than a URL; the Microsoft Learn and Applied Skills free-tier
claim in `p5ms0`, which was not checked today; the four provenance-blocked URLs; the remaining URLs in the
79; and the new DeepLearning.AI course "Tabular Foundation Models for Data Science Agents", seen on a site
banner but not read.

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
