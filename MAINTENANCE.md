# Maintenance procedure

Freshness is the product. If this file is not followed, Backprop is just another stale course list.

## The one rule

**Never write anything into `courses.json` or `universities.json` that has not been read off the
provider's or institution's own pages.** No inference from a third-party listicle, no filling a gap from
memory, no plausible-looking price. If something cannot be verified, either leave the previous value and
note the date it was last checked, or mark the entry unverified. An invented detail destroys the only
thing this project sells.

Where a provider's marketing disagrees with its own terms, the terms win.

## Authoritative source per provider

| Provider | Check here, nowhere else |
|---|---|
| AWS | aws.amazon.com/certification for exam codes and prices, aws.amazon.com/training for courses |
| Microsoft | learn.microsoft.com/credentials for exam codes, retirement dates and prices |
| Oracle | education.oracle.com and the Oracle University blog for what is still free |
| NVIDIA | nvidia.com/en-us/training for courses, the certification pages for exam prices |
| IBM | skillsbuild.org for free badges, ibm.com/training for the paid certificates |
| Google | developers.google.com, skills.google, kaggle.com/learn |
| Hugging Face | huggingface.co/learn |
| Anthropic | anthropic.skilljar.com |
| OpenAI | academy.openai.com, cookbook.openai.com |
| LangChain | academy.langchain.com |
| DeepLearning.AI | deeplearning.ai/courses, and check whether the beta free window still applies |
| Coursera, DataCamp, LinkedIn | the course page itself, for current price and length |
| Universities | the institution's own course and module pages only |

## Each verification pass

1. **Retired exams first.** For every certification entry, confirm the exam code is still live and the
   price is current. This is where the project earns its claim. Any newly retired exam moves into the
   retired ledger in `courses.json` with its replacement.
2. **Free-tier drift.** Providers quietly move things behind paywalls. Re-check everything marked `free`,
   `freecert` or `beta`. Oracle's free Foundations certifications and the DeepLearning.AI beta window are
   the two most likely to change.
3. **New courses.** Check the big first-party catalogues for anything genuinely new and worth adding.
   Prefer free, first-party and assessed over paid, third-party and video-only.
4. **Dead links.** Any URL that no longer resolves gets fixed or the entry goes.
5. **Run the integrity check.** `python3 verify.py` must pass.
6. **Update the counts.** README, the hero stats and the search placeholder in `index.html` all carry
   totals. `verify.py` reports mismatches.
7. **Rebuild and commit.** Regenerate `dist/index.html`, add a dated `CHANGELOG.md` entry saying what was
   re-checked and what changed, then push.

## If nothing changed

Still add a CHANGELOG entry saying what was checked and that nothing moved. A verification record with
gaps in it is worth less than one without. Do not invent a change to look busy.

## Rebuild

```bash
python3 verify.py          # integrity check, must pass
python3 build_site.py      # regenerates dist/index.html with data inlined
```
