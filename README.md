# Laos: law history in git


Laos's law as a git history, on the design every country here shares: one file per entry, one commit per version on the day it took effect, and the record that made each change as the commit's author. For now it holds no law text, only facts: catalogues of the laws of Laos and Laos's actions on treaties. `git blame` names the day's record behind every line; `git log` lists every entry for a law or a treaty; picking a date gives the record as it stood that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Laos's national law, which global-law reads at `laos/national/acts/`.

**What is in it now:** no law text. [`catalogue-gazette/`](catalogue-gazette/README.md) lists the 182 current laws on the Lao Official Gazette's list of all laws, the Constitution as revised in 2025 among them, each with its Lao title, number, date of the law (10 October 1998 to 26 June 2025), Gazette publication day and responsible body; [`catalogue/`](catalogue/README.md) lists 26 laws and other acts recorded by WIPO Lex, with their titles and dates (1990 to 2023). [`treaties/`](treaties/README.md) records 56 actions on 44 multilateral treaties deposited with the UN Secretary-General (30 accessions, 13 signatures, 11 ratifications and 2 acceptances), from 17 May 1950 to 26 September 2019, and [`wipo-treaties/`](wipo-treaties/README.md) Laos's part in 51 treaties as WIPO Lex records it. [`legal-system/`](legal-system/README.md) holds a few facts from Wikidata. [`data/laws.csv`](data/laws.csv) lists the 234 records the commits are credited to; [`REPRODUCE.md`](REPRODUCE.md) says how the files were made.

**Why there is no law text.** The only official text found, the Constitution (2015 revised edition) on the Lao Official Gazette ([laoofficialgazette.gov.la](https://laoofficialgazette.gov.la/)), is a scan of pages with no text layer. An OCR attempt with the Lao model lost vowel and tone marks in many words, so its output is not a faithful copy and was not published. The next step is a text copy from the Gazette or the National Assembly, or OCR proof-read against the scans.

Each entry is one file: `catalogue-gazette/law-2013-12-24-43.md` is the Labour Law (amended), No. 43 of 24 December 2013, and `catalogue-gazette/law-2025-03-20-77.md` the Constitution as revised in 2025, No. 77; `catalogue/law-22043.md` is WIPO Lex's entry for the Constitution. Each UN treaty is one file named from its number in the UN Treaty Collection: `treaties/treaty-iv-4.md` is the International Covenant on Civil and Political Rights (IV-4).

The records are in English, except the titles and responsible bodies in `catalogue-gazette/`, which are in Lao as the Gazette lists them.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every action Laos took on the International Covenant on Civil and Political Rights | `git log -p --word-diff -- treaties/treaty-iv-4.md` |
| Which action wrote each line? | `git blame treaties/treaty-iv-4.md` |
| Every version of the Covenant's record, with the day of each | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- treaties/treaty-iv-4.md` |
| The record as it stood on 1 January 2005 | `python tools/on.py 2005-01-01 treaties treaty-iv-4` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Laos](https://global-law.lexifina.com/v1/try_claude?country=laos)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=laos)**: the same question in ChatGPT.
- **[Search Laos's record on our site](https://lexifina.com/law?country=laos&q=%E0%BB%81%E0%BA%AE%E0%BA%87%E0%BA%87%E0%BA%B2%E0%BA%99)**: a search for "ແຮງງານ" (labour) in its catalogue of titles, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=%E0%BB%81%E0%BA%AE%E0%BA%87%E0%BA%87%E0%BA%B2%E0%BA%99&jurisdiction=laos)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Lao or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add laos/national/acts
python3 tools/law.py show 2026-01-01 laos/national/acts/treaties/treaty-iv-4.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Vientiane, and carries its day in its `In-force:` trailer:

- for the Gazette's list, the date of the law, not the day it took effect; the Gazette publication day is in each file;
- for WIPO Lex's laws, the date WIPO Lex records (promulgation, entry into force, commencement or adoption, in that order; some are only 1 January of a year); for treaties, the day of Laos's action as the UN Treaty Collection or WIPO Lex records it; for the Wikidata facts, the item's last-modified day (20 October 2026);
- git cannot store dates before 1970, so the 14 earlier commits are dated from 1970-01-01, one second apart, with the real day in `In-force:`. Ask for a date with `tools/on.py`, not `git log --before`.

Each day's entries are credited to a record named for that day (`Catalogue-gazette entries of 2013-12-24`, `UN Treaty Collection: actions of 2009-09-25`), and each WIPO Lex treaty action to its treaty, with an e-mail address that cannot exist. The first version of `treaties/`, `catalogue-gazette/`, `wipo-treaties/` and `legal-system/`, the oldest available, is credited to the build's one publisher name, `United Nations Treaty Collection and Wikidata`, whatever its source.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before and compares it with the corpus (not in this repository; its hash is in `data/corpus.sha256`); it also checks that every commit's trailers parse, that `main` has no merge commits and that no commit is dated in the future.
- `tools/build.py` writes the history from that one corpus file, and the same corpus gives the same commit hashes. [`REPRODUCE.md`](REPRODUCE.md) records that the checks were not yet run for this build and that no second build has been compared.
- `data/versions.json` gives each version's source and the sha256 of what it was read from. Only facts are taken: numbers, titles, dates and links.

## What it does not show

- **Law text.** Neither the Constitution nor any of the 182 laws on the Gazette's list is here as text.
- **Most decrees and other subordinate acts.** Only 11 of WIPO Lex's 26 entries are such acts; 8 WIPO Lex laws with no date and 2 rows of the Gazette's list with no usable date or number are left out. No case law.
- **The day a law took effect.** Laws are dated by the date of the law or WIPO Lex's date, not by commencement.
- **Most treaty actions.** Only treaties deposited with the UN Secretary-General and WIPO Lex's list; no bilateral or regional treaties, and no treaty text, reservations or declarations.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Lao Official Gazette](https://laoofficialgazette.gov.la/) | List of all current laws (the sheet its home page links to) | yes, each law on the date of the law | Facts only: Lao title, number, dates and responsible body; read on 30 October 2026 |
| [WIPO Lex](https://www.wipo.int/wipolex/en/members/profile/LA) | Catalogue of laws and treaties (CC BY 4.0) | yes, each entry on the date it records | 26 laws and 51 treaties: titles, dates and links; read on 30 October 2026 |
| [United Nations Treaty Collection](https://treaties.un.org/) | Status pages of multilateral treaties deposited with the UN Secretary-General | yes, each action on its day | Facts only: treaty names and the dates of Laos's actions; read on 30 October 2026 |
| [Wikidata](https://www.wikidata.org/wiki/Q819) | Open facts (CC0) | one snapshot | The legal-system facts |

## Licence

See [`LICENSE`](LICENSE). Only facts are taken: treaty names, kinds of action and dates, and the Gazette's titles, numbers, dates and responsible bodies, with no law text; WIPO Lex's content is CC BY 4.0 (source: World Intellectual Property Organization, which does not endorse this repository), and Wikidata's is CC0. Lexifina's arrangement, tables, commit messages and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model, and no model runs when the history is built (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
