# Canonical Error Registry

This is the source of truth for recurring English problems.

## Summary

| error_id | category | pattern | status | severity | confidence | occurrences | successful_checks | first_seen | last_seen |
|---|---|---|---|---|---|---:|---:|---|---|
| GR-A-001 | Grammar | Missing indefinite article before singular countable nouns | ACTIVE | MEDIUM | high | 11 | 3 | 2026-09-12 | 2026-09-20 |
| GR-VF-001 | Grammar | Selecting the complement form after a verb or expression | ACTIVE | MEDIUM | medium | 3 | 0 | 2026-09-12 | 2026-09-19 |
| GR-TA-001 | Grammar | Present perfect for situations continuing until now | CANDIDATE | LOW | low | 2 | 0 | 2026-09-12 | 2026-09-12 |
| GR-BE-001 | Grammar | Extra be before a simple lexical verb | ACTIVE | MEDIUM | high | 5 | 1 | 2026-09-12 | 2026-09-20 |
| VO-COL-001 | Vocabulary | trade/exchange something for something | CANDIDATE | LOW | medium | 2 | 0 | 2026-09-12 | 2026-09-19 |
| VO-COL-002 | Vocabulary | Describing conclusions from limited data | CANDIDATE | LOW | low | 1 | 0 | 2026-09-12 | 2026-09-12 |
| GR-Q-001 | Grammar | Auxiliary placement in direct questions | ACTIVE | MEDIUM | high | 5 | 3 | 2026-09-19 | 2026-09-20 |
| VO-COL-003 | Vocabulary | pay for a product or service | CANDIDATE | LOW | low | 1 | 0 | 2026-09-19 | 2026-09-19 |
| VO-TERM-001 | Vocabulary | unit economics for profitability per unit/customer | CANDIDATE | LOW | low | 1 | 0 | 2026-09-19 | 2026-09-19 |
| GR-AGR-001 | Grammar | Singular agreement in what has changed | CANDIDATE | LOW | low | 1 | 0 | 2026-09-20 | 2026-09-20 |
| VO-TIME-001 | Vocabulary | Naming the early years of a decade | CANDIDATE | LOW | low | 1 | 0 | 2026-09-20 | 2026-09-20 |

## Counting and scope

Counts are selected, verified occurrences, not an exhaustive count of every possible slip. Evidence keys E01–E11 belong to session 2026-09-12-2125-ai-agents. Overlapping realtime input/delta copies are counted once. Setup discussion is excluded from practice counts. All evidence is transcript-only; no pronunciation inference.

Evidence keys D01–D13 belong to session 2026-09-19-1202-discipline-entrepreneurship. After evidence review, the session adds 11 selected incorrect occurrences and one later spontaneous successful check. D08 remains an uncounted local correction and D11 an uncounted retest observation; the keys are preserved without renumbering. Repeated paraphrases of the same pay-for argument are represented by one selected occurrence. Repaired false starts, recognition ambiguities and the accepted form "waked" are excluded. See that session's coverage ledger before reprocessing.

## Evidence reassessment — 2026-09-19

- D08, "what else... it's required" → "What else is required?", contains redundant it: what else is already the subject. It is not auxiliary-inversion evidence and was removed from GR-Q-001's count; retain it as local feedback in the session note.
- "Am I-am I right" is acceptable but does not test the lexical-verb/modal question construction tracked by GR-Q-001. Its successful-check increment was removed; retain qualitative credit only.
- D11, "can be can be build" (message 01a0b947-73e1-7322-a210-c6dc9cc3851c), cannot distinguish a learner verb-form error from build/built transcription ambiguity. The newly created GR-PASS-001 entry and its occurrence were withdrawn. Retain this audit and the session's uncounted retest; reserve GR-PASS-001 so the withdrawn ID is never reused. This is an evidence exclusion, not a resolved learner error.

## Entries

### GR-A-001 — Missing indefinite article before singular countable nouns

- **Category:** Grammar
- **Subcategory:** articles
- **Status:** ACTIVE
- **Severity:** MEDIUM
- **Confidence:** high
- **Occurrences:** 11
- **Successful checks:** 3
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-20
- **Rule/problem:** Use a/an for an indefinite singular countable noun. Six selected contexts across two sessions establish recurrence across days.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** Describe a tool, a difficulty and a possible outcome spontaneously.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E01 | I used... AI agent in the past | I used an AI agent in the past | AI-use hypothesis; message 01a09717-644e-7811-a2e0-d35b97a34a15 (delta) | yes |
| 2026-09-12-2125-ai-agents / E02 | it is disaster for my mind | it is a disaster for my mind | Reaction to lack of income; message 01a0971d-6a9b-7ae3-bcc2-eae224ac7eb9 | yes |
| 2026-09-12-2125-ai-agents / E03 | without answer at all | without an answer at all | Application responses; message 01a0972c-b1b4-7b40-9bee-407256b6204e | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D01 | helps helps person | helps a person | Discipline and results; message 01a0b91e-65d1-7161-aa62-aeab37488005; repeated helps counted once | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D02 | in more structured uh... way | in a more structured way | Request to organize the lessons; message 01a0b92b-a55c-76a1-9ec9-9275ef220959 | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D03 | creating network | creating a network | Project intended to build connections; message 01a0b942-33b9-7dd1-9f46-a2803d656580 | yes |

#### Notes

Later spontaneous correct uses in the E02 message: "it's not a disaster" and "it's not a... huge problem" (two successful checks). Repeated "it's not a disaster" counted once. These show available knowledge, not sustained improvement yet.

2026-09-19: omissions recur in three separate turns. No additional article successful checks selected; this is not a claim that all articles were wrong. "Build a network" is an optional collocation improvement for D03, not a second error.


September 20 supplement (session 2026-09-20-1244-autonomy-business): S01 'good network is one of the most important thing' -> 'a good network is one of the most important things' (networking turn); S02 'when I visit new country' -> 'when I visit a new country' (flavors/travel turn); S03 'choose more profitable business' -> 'choose a more profitable business' (final business-learning turn). Three independent spontaneous contexts; one article occurrence each. Plural correction in S01 is local feedback, not another count.

September 20 car-discussion supplement (2026-09-20-1419-german-cars): G01 "if I want... Chinese looking car" -> "if I want a Chinese-looking car" (01a0beb7-d61a-7883-bc12-861f0370ee42); G04 "this as uh... detailed answer" -> "this as a detailed answer" (01a0beb9-5e7c-73f2-b3ae-c7998dd95bc4). Two selected spontaneous article omissions. Other car noun phrases in G01's argument are not additional counts. G07 later spontaneous "China still uh is not a big competitor" (01a0bebe-33fb-71c1-ac27-dd2af65422e3) adds one successful check. ACTIVE remains appropriate; no frequency trend established.

### GR-VF-001 — Selecting the complement form after a verb or expression

- **Category:** Grammar
- **Subcategory:** gerund/infinitive
- **Status:** ACTIVE
- **Severity:** MEDIUM
- **Confidence:** medium
- **Occurrences:** 3
- **Successful checks:** 0
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-19
- **Rule/problem:** include + -ing; worth + -ing. Three contexts across two sessions, including repeated worth + infinitive. Retain the existing ID; prioritize worth in remediation.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** Explain what a tool's functions include and what is worth trying.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E04 | do not... include... um... speak with people, negotiate with people | do not include speaking with people or negotiating with people | Role responsibilities; message 01a09720-d080-7181-a267-408580cd09be; one coordinated construction | yes |
| 2026-09-12-2125-ai-agents / E05 | are worth to prepare | are worth preparing for | Positions worth preparation; message 01a09729-8782-72e0-acb9-86749898d01e | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D04 | what is worth to learn from... these people? | What is worth learning from these people? | Lessons from people who escaped poverty; message 01a0b92b-a55c-76a1-9ec9-9275ef220959 | yes |

#### Notes

The original two contexts were candidates; D04 establishes cross-session recurrence and reaches the activation threshold. Setup-only "I need practice English" remains excluded. The assistant's inaccurate paraphrase "worth learn" is not learner evidence. "Discipline requires ... to be able to" is addressed as a reformulation in the session note, without an extra increment.

### GR-TA-001 — Present perfect for situations continuing until now

- **Category:** Grammar
- **Subcategory:** verb tense/aspect
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 2
- **Successful checks:** 0
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-12
- **Rule/problem:** Use present perfect continuous for an ongoing activity with for/since, and present perfect for a continuing state.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** Explain how long you have used a tool and what has changed since you began.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E06 | I'm...I'm looking for for job for... eight months | I've been looking for a job for eight months | Ongoing search; message 01a09729-8782-72e0-acb9-86749898d01e | yes |
| 2026-09-12-2125-ai-agents / E07 | I don't have job for two mo...-two weeks | I've been without a job for two weeks | Current employment state; same message; corrected duration retained | yes |

#### Notes

Two distinct predicates, both in one turn: low recurrence confidence. January/eight-month reformulation is the same search claim, not another occurrence. "I still didn't get any offer" not counted: simple past can vary by dialect/context. Corrections also supply articles without adding duplicate article evidence.

### GR-BE-001 — Extra be before a simple lexical verb

- **Category:** Grammar
- **Subcategory:** verb construction
- **Status:** ACTIVE
- **Severity:** MEDIUM
- **Confidence:** high
- **Occurrences:** 5
- **Successful checks:** 1
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-20
- **Rule/problem:** Simple present lexical verbs do not take be: they bring; what matters; things exist. Use do/does for lexical-verb negation: businesses do not exist yet.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** State what matters to you and what opportunities different tools bring.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E08 | they are also... bring a lot of opportunities | they also bring a lot of opportunities | Alternative fields; message 01a09717-644e-7811-a2e0-d35b97a34a15 | yes |
| 2026-09-12-2125-ai-agents / E09 | the progress is what is matter | Progress is what matters | Value of progress; same message | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D05 | the most obvious things... are already exist | the most obvious things already exist | Existing products and competition; message 01a0b93b-178a-7c41-b4a3-15e392a0b799 | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D06 | that are not exist yet | that do not exist yet | Future businesses; message 01a0b947-73e1-7322-a210-c6dc9cc3851c; same-clause repetition counted once | yes |

#### Notes

The first two clauses were from one turn. D05–D06 establish recurrence in another session, in two separate arguments. One later spontaneous successful check after D05: "something that... doesn't exist yet" in message 01a0b93b-178a-7c41-b4a3-15e392a0b799; no immediate correction/drill preceded that correct use. D06 follows in a later turn, so sustained improvement is not established. Do not count repaired "I'm not really... care ... I don't really care" or "if you're... don't have... if you don't have" as incorrect occurrences.


September 20 supplement: S04 'they are... contain something really special' -> 'they contain something really special' (mystery-box explanation, session 2026-09-20-1244-autonomy-business). One spontaneous occurrence; subsequent assistant correction and replay excluded.

### VO-COL-001 — trade/exchange something for something

- **Category:** Vocabulary
- **Subcategory:** unnatural collocation
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** medium
- **Occurrences:** 2
- **Successful checks:** 0
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-19
- **Rule/problem:** Use trade/exchange my time for money. The preposition introduces what is received.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** Explain one exchange or trade-off in your own words.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E10 | I'm just trading my time with this money | I'm just trading my time for money | Income tied to work; message 01a09722-e52b-7af3-b8a1-0fe53341dc18 | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D07 | you should exchange your time to... to some money | you should exchange your time for money | Covering basic needs while preserving project time; message 01a0b934-8921-72a3-a274-2a82f2c6c4dd | yes |

#### Notes

Understandable but unnatural exchange phrasing, now seen on two dates. Keep CANDIDATE below the normal three-context activation threshold. Use the same canonical ID for trade and exchange; this is not evidence of a general preposition problem. Interrupted continuations and overlapping transcript suffixes of D07 are not independent occurrences.

### VO-COL-002 — Describing conclusions from limited data

- **Category:** Vocabulary
- **Subcategory:** imprecise phrasing
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 1
- **Successful checks:** 0
- **First seen:** 2026-09-12
- **Last seen:** 2026-09-12
- **Rule/problem:** To express that a small sample cannot support a firm conclusion, say draw reliable conclusions from such a small sample.
- **Likely cause/interference:** Not established from this session.
- **Remediation:** Explain what you can and cannot conclude from a small experiment.
- **Next retest:** Next substantive conversation, without revealing the target form.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-12-2125-ai-agents / E11 | it's hard to make a serious statistic | It's hard to draw reliable conclusions from such a small sample | About ten interviews; message 01a0972c-b1b4-7b40-9bee-407256b6204e | yes |

#### Notes

Understandable but unnatural. Meaning-preserving reformulation, not a claim that statistic is always uncountable. No career diagnosis inferred.

### GR-Q-001 — Auxiliary placement in direct questions

- **Category:** Grammar
- **Subcategory:** word order / clause structure
- **Status:** ACTIVE
- **Severity:** MEDIUM
- **Confidence:** high
- **Occurrences:** 5
- **Successful checks:** 3
- **First seen:** 2026-09-19
- **Last seen:** 2026-09-20
- **Rule/problem:** In non-subject wh-questions, put the modal before the subject (what can you say) or add do-support for a simple lexical verb (what does this mean). Subject questions and formulaic be-questions do not test this target.
- **Likely cause/interference:** Not established from this evidence.
- **Remediation:** Ask three concise follow-up questions about an unfamiliar business idea.
- **Next retest:** Next substantive conversation, without announcing the target.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-19-1202-discipline-entrepreneurship / D09 | what you can say about... their... abilities | What can you say about their abilities? | Direct question about effective people; message 01a0b929-fb88-74b3-8b5b-491dab167e74 | yes |
| 2026-09-19-1202-discipline-entrepreneurship / D10 | What means uh... protect your ability to keep going? | What does "protect your ability to keep going" mean? | Clarifying a phrase; message 01a0b934-8921-72a3-a274-2a82f2c6c4dd | yes |

#### Notes

Two independent direct-question contexts remain after review, below the normal activation threshold. No eligible successful checks selected. "Am I-am I right" (message 01a0b935-80ee-7e82-830d-4a4dfbbfef40) receives qualitative credit only; it does not test this target. D08 is a redundant-subject issue, retained as local feedback only. No count for "What ... clarity ... means? ... what-what does it mean": the learner repairs it. The fall-through/follow-through recognition ambiguity is excluded, as is quotation of "recover from setbacks" when asking its meaning.


September 20 retrospective supplement (September 19 Hormuz session): H01 direct 'But why why Americans cannot ... make the Gulf safe' -> 'But why can’t the Americans make the Gulf safe?' (message 01a0bb28-4a3d-7ff0-a51e-d6b448c43596). One new independent direct question activates pattern across two conversations. Earlier embedded 'What is interesting for me is why ... Americans cannot' is acceptable word order and excluded. H02 'How does ... it ... affect' and H03 'Why don’t they do it' are two spontaneous successful inversion checks; H02 still needs local correction affect on -> affect. Old candidate notes above describe the prior assessment, superseded by this dated supplement.

September 20 car-discussion supplement (2026-09-20-1419-german-cars): G02 "Why... they struggle so much, right now" -> "Why do they struggle so much right now?" (01a0beb2-044e-7631-9d6b-ad570f2df4ec); G03 "how my ... perspective... relate to the-the real... reasons" -> "How does my perspective relate to the real reasons?" (01a0beb7-d61a-7883-bc12-861f0370ee42). Two independent spontaneous do-support omissions; ACTIVE, high recurrence confidence. G08 later "Could you please... explain" (01a0beb9-5e7c-73f2-b3ae-c7998dd95bc4) adds one successful modal-inversion check, despite local phrasing elsewhere. This does not establish do-support mastery. "What have changed" is a subject question, tracked separately under GR-AGR-001.

### VO-COL-003 — pay for a product or service

- **Category:** Vocabulary
- **Subcategory:** verb-preposition collocation
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 1
- **Successful checks:** 0
- **First seen:** 2026-09-19
- **Last seen:** 2026-09-19
- **Rule/problem:** Use pay for when the object is what is purchased: something people will pay for. Pay someone/pay an amount are different valid patterns.
- **Likely cause/interference:** Not established from this evidence.
- **Remediation:** Explain who would pay for a product, how much they would pay, and whom they would pay.
- **Next retest:** A different customer/product context.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-19-1202-discipline-entrepreneurship / D12 | the next step is to develop something people will pay | The next step is to develop something people will pay for. | Customer demand versus profitability; message 01a0b93b-178a-7c41-b4a3-15e392a0b799 | yes |

#### Notes

Selected once from one extended argument, although the same wording is repeated in its elaboration and recap. Those repetitions and replay copies do not establish independent contexts. No general preposition diagnosis.

### VO-TERM-001 — unit economics for profitability per unit/customer

- **Category:** Vocabulary
- **Subcategory:** professional terminology
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 1
- **Successful checks:** 0
- **First seen:** 2026-09-19
- **Last seen:** 2026-09-19
- **Rule/problem:** Unit economics names the revenue/cost relationship for an individual unit or customer in this business discussion.
- **Likely cause/interference:** Not established from one example.
- **Remediation:** Explain whether a cleaning service is profitable per job.
- **Next retest:** Next spontaneous profitability explanation.

#### Evidence

| session | learner form | better/correct form | context | spontaneous |
|---|---|---|---|---|
| 2026-09-19-1202-discipline-entrepreneurship / D13 | unit economy | unit economics | Costs and profitability of a business; message 01a0b93b-178a-7c41-b4a3-15e392a0b799 | yes |

#### Notes

One terminology observation. The underlying distinction between selling something and making a profit was clearly communicated; this entry is not a criticism of the learner's business reasoning.



### GR-AGR-001 — Singular agreement in what has changed

- **Category:** Grammar
- **Subcategory:** agreement
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 1
- **Successful checks:** 0
- **First seen:** 2026-09-20
- **Last seen:** 2026-09-20
- **Rule/problem:** Use singular has when asking generally what has changed; no plural subject is supplied here. This is a subject question, so do-support is unnecessary.
- **Evidence:** 2026-09-20-1419-german-cars / G06, spontaneous "what...what have changed, what uh... have changed" -> "What has changed?" Historical-market comparison, message 01a0bebe-33fb-71c1-ac27-dd2af65422e3. Same-question repetition counted once.
- **Notes:** One selected context, not established recurrence. Earlier local agreement feedback remains uncounted; do not retroactively inflate this entry.
- **Remediation / next retest:** Ask what has changed in a familiar industry since an earlier period, without supplying the wording.

### VO-TIME-001 — Naming the early years of a decade

- **Category:** Vocabulary
- **Subcategory:** unnatural collocation
- **Status:** CANDIDATE
- **Severity:** LOW
- **Confidence:** low
- **Occurrences:** 1
- **Successful checks:** 0
- **First seen:** 2026-09-20
- **Last seen:** 2026-09-20
- **Rule/problem:** For this reference to the beginning of the century, use in the early 2000s; "in the beginning of zeros" is understandable but unnatural.
- **Evidence:** 2026-09-20-1419-german-cars / G05, spontaneous "in the beginning of zeros" -> "in the early 2000s"; historical-market comparison, message 01a0bebe-33fb-71c1-ac27-dd2af65422e3.
- **Notes:** One context only. The approximate "30 years ago" is not a separate language error; the intended reference was clarified by the surrounding century comparison.
- **Remediation / next retest:** Compare an industry in the early 2000s and today; later test another decade without supplying the phrase.
