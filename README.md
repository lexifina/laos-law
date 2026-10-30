# Laos: law history in git

The law of Laos as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `treaties/` | Treaty actions of Laos (UN Treaty Collection): signature, ratification, accession | 43 | Each date on which Laos (the Lao People's Democratic Republic, and the Kingdom of Laos before it) signed, ratified or acceded to a UN-deposited treaty |
| `catalogue-gazette/` | 182 current laws of Laos as listed by the Lao Official Gazette: Lao title, number, date of the law, Gazette publication date, responsible body; no law text | one per law date | 1998 to 2025, dated by the date of the law |
| `catalogue/` | Laws of Laos recorded by WIPO Lex: title, subject, date, link; no law text | one per recorded date | Dated by the date WIPO Lex records for each law |
| `wipo-treaties/` | Treaty actions of Laos recorded by WIPO Lex (name, administering organisation, dates; no treaty text) | one per action date | From the earliest to the latest recorded action |
| `legal-system/` | Legal system of Laos: open facts from Wikidata | 1 | A snapshot of Wikidata taken on 30 October 2026 |

**Language.** English, except the titles in `catalogue-gazette/`, which are copied in Lao as the Gazette lists them. This repository holds no law text.

**Source.** **Metadata and facts only, no law text, because** the only official text found, the Constitution on the Lao Official Gazette (laoofficialgazette.gov.la, the 2015 revised edition, National Assembly law no. 63/NA of 8 December 2015), is a scan of pages with no text layer, and an OCR attempt (Tesseract 5.4 with the Lao model, 300 and 400 dpi) lost vowel and tone marks in many words, so its output is not a faithful copy of the law and was not published. Treaties: United Nations Treaty Collection (treaties.un.org), status-of-treaty pages, read on 30 October 2026. Only facts are copied (treaty names, kinds of action, dates); no descriptive text. Wikidata (CC0) for the legal-system facts. The list of current laws in `catalogue-gazette/` is the public "all laws" sheet that the Lao Official Gazette home page links to (title, number, dates, responsible body; facts only). WIPO Lex (https://www.wipo.int/wipolex/en/members/profile/LA, CC BY 4.0) gives the `catalogue/` and `wipo-treaties/` facts. All read on 30 October 2026.

## Dates

- The treaties act has one version per date on which a treaty action happened; each version adds that day's actions (signature, ratification or accession), dated by the action date in the Treaty Collection.
- The legal-system act is a single snapshot dated by the Wikidata item's own last-modified day (20 October 2026), as the oldest version available.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@lexifina-first-build.invalid`). For treaty actions the 'law' is the day's batch of actions in the UN Treaty Collection (key `untc-<date>`). The committer is always Lexifina.

## Limits

This is not a record of Lao law. It covers only treaties deposited with the UN Secretary-General (bilateral and regional treaties are not included) and Wikidata facts. Next step: a text-layer or HTML copy of the Constitution and the laws from the Official Gazette or the National Assembly, or a better OCR model with a human proof-read against the scan.
