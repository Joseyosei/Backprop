# Backprop

A hand-checked map of AI, machine learning and data science courses.

**133 courses across 19 providers. 100 of them are free. Every exam code verified by hand.**

Most AI learning roadmaps still send people to exams that no longer exist. This one does not.

## Why this exists

Three things a general-purpose AI assistant structurally cannot do well, and that course
aggregators do not bother doing:

1. **Dated verification.** Models have knowledge cutoffs and will confidently name exams that
   retired months ago. Nearly every AI roadmap in circulation still points at Microsoft AI-102,
   AI-900 and DP-100, and the AWS ML Specialty. All four retired during 2026.
2. **True cost of a credential.** Nobody maps which certifications are free *including the
   proctored exam*, versus free training with a paid exam, versus paid everything.
3. **Degree overlap filtering.** Nothing takes "I am enrolled on this degree" and returns what is
   already redundant.

## Retired in 2026

| Code | Was | Status | Take instead |
|---|---|---|---|
| AI-900 | Azure AI Fundamentals | Retired 30 Jun 2026 | AI-901 |
| AI-102 | Azure AI Engineer Associate | Retired 30 Jun 2026 | AI-103 (new cert, not a rename) |
| DP-100 | Azure Data Scientist Associate | Retired 1 Jun 2026 | AI-300 |
| MLS-C01 | AWS ML Specialty | Last exam 31 Mar 2026 | AWS ML Engineer Associate |
| MLA-C01 | AWS ML Engineer Associate v1 | Last English exam 28 Sep 2026 | MLA-C02 |

## Providers covered

DataCamp, Google, Coursera, Hugging Face, DeepLearning.AI, LangChain Academy, Harvard, Oracle,
LinkedIn Learning, AWS, Microsoft, NVIDIA, OpenAI, Anthropic, Rust, React, fast.ai, freeCodeCamp,
and university open courseware (MIT, Stanford, Helsinki).

## Tracks

AI Engineer, ML Engineer, Data Scientist, MLOps and Platform, Research, Systems and GPU,
Product Builder, Complete Beginner.

## Structure

```
dist/index.html      the whole site, self-contained, no build step
dist/logo.svg        the mark
dist/vercel.json     headers and clean URLs
courses.json         the course database, the thing worth editing
build_data.py        regenerates courses.json
index.html           the page template (fetches courses.json in dev)
DEPLOY.md            deployment steps
```

## Run it locally

```bash
cd dist && python3 -m http.server 8000
```

Then open http://localhost:8000

## Deploy

Drag `dist/` onto [vercel.com/new](https://vercel.com/new), or:

```bash
npm i -g vercel && cd dist && vercel --prod
```

## Editing the course list

`courses.json` is the database. Each entry carries cost, hours, level, topic, track, whether a
certificate is awarded, and a written note on whether it is worth taking.

Rules for an entry:

- Verify against the provider's own pages, not a third-party listicle
- Where a provider's marketing disagrees with its terms, the terms win
- Record the real cost, including whether the exam fee is separate
- The note says whether it is worth someone's time, not what it covers

## No affiliate links

100 of the 133 courses are free, which makes most of this list worth nothing in commission.
That is the point: the ranking is not for sale.

## Licence

MIT for the code. The course data is factual information about third-party offerings, gathered by
hand. Provider names and exam codes are used descriptively to identify their own courses.
Backprop is independent and not affiliated with, endorsed by, or sponsored by any provider listed.
