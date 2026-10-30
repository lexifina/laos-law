# How this repository was made (Laos)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| United Nations Treaty Collection (multilateral treaties deposited with the Secretary-General) | <https://treaties.un.org/> | 2026-10-30 | Facts only (treaty names, kinds of action, dates). |
| Wikidata | <https://www.wikidata.org/> | 2026-10-30 | CC0 1.0 |
| WIPO Lex member profile | <https://www.wipo.int/wipolex/en/members/profile/LA> | 2026-10-30 | WIPO content: CC BY 4.0 (https://www.wipo.int/web/terms-of-use); only facts copied |
| Lao Official Gazette, list of all laws | <https://laoofficialgazette.gov.la/> | 2026-10-30 | Facts only (title, number, dates, responsible body); no law text copied. The sheet is the "all laws" list the Gazette home page links to. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `treaties` | Treaty actions of Laos (UN Treaty Collection): signature, ratification, accession | 43 | 1950-05-17 to 2019-09-26 |
| `legal-system` | Legal system of Laos: open facts from Wikidata | 1 | 2026-10-20 to 2026-10-20 |
| `catalogue` | Catalogue of laws of Laos recorded by WIPO Lex (title, date, link only; no law text) | 26 | 1990-03-27 to 2023-11-20 |
| `wipo-treaties` | Treaty actions of Laos recorded by WIPO Lex (facts only; no treaty text) | 42 | 1952-02-28 to 2026-07-14 |
| `catalogue-gazette` | Catalogue of the current laws of Laos listed by the Lao Official Gazette (title, number, date, gazette date; no law text) | 114 | 1998-10-10 to 2025-06-26 |

The build made 235 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 230 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 14 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 234 laws in the record.
- 457 tags.

## Dates

Each commit is dated at noon (Asia/Vientiane) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No single commencement rule is applied: each version is dated by the event date its source records (treaty action date, last-modified day of a Wikidata item, or the compilation date of the Senate edition). https://treaties.un.org/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `3a70a563f1c6dd0bc50f92ce9d7fea00e755fc2623b1bf14be6f60f42e5c6fb6` (374097 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Treaty actions are dated by the action date shown in the UN Treaty Collection; each date is one version credited to a law key untc-<date>.
- Signature, ratification, accession (a), succession (d), acceptance (A), approval (AA) and formal confirmation (c) are copied as the Treaty Collection records them, under the participant name it uses.
- The legal-system act is a single snapshot of Wikidata facts dated by the item own last-modified day, as the oldest version available.
- WIPO Lex: 26 laws from the member profile dated by the date WIPO Lex records (promulgation, entry into force, commencement, adoption, in that order); 8 laws with no recorded date are left out. Treaty actions: 51. Titles, dates and links only; no text. WIPO Lex gives some laws only 'January 1' of a year, a placeholder rather than a known date.
- Lao Official Gazette list of all laws: 182 laws (the 2025 Constitution, laws and amending laws) with number, date of the law and Gazette publication date, dated by the date of the law. 2 rows without a parsable date or number were left out. Lao titles are copied as listed. No law text and no OCR.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
