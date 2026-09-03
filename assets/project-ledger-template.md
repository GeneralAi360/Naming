# Naming project ledger template

> This is the durable source of truth for one naming project. Append material changes; do not erase prior decisions, rejected candidates, or stale evidence without preserving history.

```yaml
project_id:
project_name_or_working_title:
repository_or_storage_location:
ledger_version:
created_at_utc:
updated_at_utc:
controller:
interaction_mode: INTERACTIVE | ASSISTED | FULL_RUN | NAME_AUDIT | MORE | COUNCIL_ONLY
capability_mode: FULL_CAPABILITY | DEGRADED_RESEARCH | INLINE_COUNCIL | HANDOFF_REQUIRED
project_status:
current_phase:
current_gate:
exact_next_action:
```

---

## 1. Source map

| Source ID | Source | Type | Date/version | Authority | Scope | Notes |
|---|---|---|---|---|---|---|
| SRC-01 |  | user brief / file / web / registry / interview |  |  |  |  |

### Source hierarchy

```text
1. Explicit current user decisions
2. Approved naming brief
3. Current authoritative external evidence
4. Current product/market evidence
5. Prior project artifacts
6. Model hypotheses
```

Conflicts:

| Conflict ID | Source A | Source B | Issue | Resolution | Authority | Date |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

---

## 2. Decision authority

```yaml
recommendation_owner:
final_approver:
stakeholders:
valid_veto_criteria:
decision_deadline:
```

| Stakeholder | Role | Priority | Valid veto | Current position | Last update |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## 3. Phase and gate state

| Phase | Artifact | Status | Approved version/hash | Evidence gaps | Next action |
|---|---|---|---|---|---|
| 0 | Naming brief |  |  |  |  |
| 1 | Strategic core / architecture |  |  |  |  |
| 2 | Competitive / collision maps |  |  |  |  |
| 3 | Territories / word banks / phonetic code |  |  |  |  |
| 4 | Generation plan |  |  |  |  |
| 5 | Candidate waves / curation |  |  |  |  |
| 6 | Linguistic/usability screen |  |  |  |  |
| 7 | Digital/domain/trademark pre-screen |  |  |  |  |
| 8 | Expert council |  |  |  |  |
| 9 | Audience testing |  |  |  |  |
| 10 | Final decision / handoff |  |  |  |  |

Status vocabulary:

- `NOT_STARTED`;
- `DRAFT`;
- `ASSUMED`;
- `READY_FOR_APPROVAL`;
- `APPROVED`;
- `IN_PROGRESS`;
- `PASS`;
- `PASS_WITH_NOTES`;
- `HOLD`;
- `FAIL`;
- `BLOCKED`;
- `NOT_APPLICABLE`.

---

## 4. Approved naming brief summary

```yaml
artifact_being_named:
product_definition:
primary_audience:
buyer:
user:
markets:
languages:
category:
problem:
mechanism:
functional_result:
emotional_result:
differentiator:
proof:
brand_archetype:
verbal_personality:
creative_intensity:
future_scope:
```

### Name jobs

| Rank | Job | Evidence of success |
|---:|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |

### Criteria

```yaml
must_have:
prefer:
must_not_have:
knockouts:
domain_policy:
trademark_scope:
```

---

## 5. Strategic core

```yaml
category_enemy:
old_belief:
new_belief:
paradigm_shift:
name_must_communicate:
name_may_suggest:
descriptor_should_explain:
visual_identity_should_carry:
selected_naming_approaches:
selected_construction_types:
```

### Naming architecture

```yaml
architecture_type:
master_brand_relation:
product_family_rules:
feature_naming_rules:
future_extension_requirements:
restricted_meanings:
```

---

## 6. Competitive naming map

| Brand | Direct/adjacent/reference | Category | Name type | Roots/morphemes | Rhythm | Image/metaphor | Distinctiveness | Collision relevance | Source/date |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

### Saturation registers

#### `SATURATED_ROOTS`

| Root | Evidence | Severity | Rule | Date |
|---|---|---|---|---|
|  |  |  |  |  |

#### `SATURATED_SUFFIXES`

| Suffix | Evidence | Severity | Rule | Date |
|---|---|---|---|---|
|  |  |  |  |  |

#### `SATURATED_PATTERNS`

| Pattern | Examples/count | Why weak/risky | Rule |
|---|---|---|---|
|  |  |  |  |

#### `SATURATED_METAPHORS`

| Metaphor | Category prevalence | Risk | Rule |
|---|---|---|---|
|  |  |  |  |

#### `SATURATED_PROMISES`

| Promise | Category prevalence | Why it has lost force | Naming implication |
|---|---|---|---|
|  |  |  |  |

### `WHITE_SPACE`

| Territory | Evidence | Strategic relevance | Risk | Priority |
|---|---|---|---|---|
|  |  |  |  |  |

---

## 7. `NO_GO_REGISTER`

Never delete an entry. Append a new status/event if circumstances change.

| ID | Name/root/pattern | Normalized forms | Reason | Status | Collision type | Evidence/source | Checked/rejected at | Owner | Notes |
|---|---|---|---|---|---|---|---|---|---|
| NG-001 |  |  |  | user_rejected / conflict / saturated / linguistic / legal / domain / other |  |  |  |  |  |

Status examples:

- `USER_REJECTED`;
- `ACTIVE_DIRECT_COMPETITOR`;
- `ACTIVE_ADJACENT_BRAND`;
- `TRADEMARK_RISK`;
- `REGISTERED_ACTIVE_DOMAIN`;
- `REGISTERED_PARKED`;
- `BROKERED_FOR_SALE`;
- `NEGATIVE_LANGUAGE_MEANING`;
- `PRONUNCIATION_FAILURE`;
- `SPELLING_FAILURE`;
- `TOO_GENERIC`;
- `TOO_SIMILAR_TO_REFERENCE`;
- `SATURATED_PATTERN`;
- `OUT_OF_BRIEF`;
- `OTHER`.

---

## 8. Semantic territories

| Territory ID | Name | Core idea | Product link | Image world | Emotion | Distant domain | Proprietary material | Saturation | Legal distinctiveness hypothesis | Scalability | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T-01 |  |  |  |  |  |  |  |  |  |  |  |

### Territory decision history

| Date | Territory | Decision | Reason | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

---

## 9. Word banks

### Customer language

| Phrase/word | Exact source | Meaning/context | Naming potential | Restrictions |
|---|---|---|---|---|
|  |  |  |  |  |

### Proprietary language

| Term/fragment | Origin | Ownership/authenticity | Meaning | Naming potential |
|---|---|---|---|---|
|  |  |  |  |  |

### Distant-domain materials

| Domain | Concepts | Physical processes | Objects | Verbs | Risks |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Cultural code

| Code/image/expression | Market | Shared meaning | Sensitivity | Allowed use |
|---|---|---|---|---|
|  |  |  |  |  |

---

## 10. `PHONETIC_CODE`

```yaml
status:
target_length_letters:
target_syllables:
preferred_syllable_shapes:
preferred_stress:
preferred_vowels:
preferred_consonants:
preferred_openings:
preferred_endings:
desired_sound_attributes:
desired_mouthfeel:
allowed_irregularity:
forbidden_clusters:
primary_language_reading:
secondary_language_reading:
transliteration_rules:
wrong_hearing_tolerance:
spelling_tolerance:
```

### Reference abstraction

| Liked reference | Transferable rhythm/sound/property | Forbidden copied material |
|---|---|---|
|  |  |  |

---

## 11. Generation plan

```yaml
wave_id:
objective:
territories:
primary_methods:
secondary_methods:
experimental_methods:
meta_ideation_methods:
phonetic_patterns:
creative_intensity:
diversity_requirements:
raw_target_or_coverage_rule:
shown_target:
prohibited_roots_patterns:
domain_led_requirement:
```

### Method allocation

| Method | Role: primary/secondary/experimental | Territory | Candidate quota/coverage | Reason |
|---|---|---|---|---|
|  |  |  |  |  |

### Diversity audit

| Dimension | Requirement | Actual | Pass/Fail | Notes |
|---|---|---|---|---|
| Territory spread |  |  |  |  |
| Construction spread |  |  |  |  |
| Phonetic spread |  |  |  |  |
| Proprietary-source share |  |  |  |  |
| Category-escape share |  |  |  |  |
| Invented-name share |  |  |  |  |
| Phrase/verb share |  |  |  |  |

---

## 12. Candidate ledger

| Candidate ID | Name | Pronunciation | Method | Territory | Honest construction | Phonetic pattern | Initial strength | Known risk | Generation wave | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| C-001 |  |  |  |  |  |  |  |  |  |  |

### Candidate events

| Event ID | Candidate | Date | Action | From status | To status | Reason/evidence | Owner |
|---|---|---|---|---|---|---|---|
| CE-001 |  |  |  |  |  |  |  |

### User feedback translation

| Raw user feedback | Candidate/wave | Interpreted property | Confidence | Change to brief/phonetic code/territory | Approved? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## 13. Screening ledger

| Check ID | Candidate | Check type | Query/asset | Market/language | Result | Status | Evidence class | Source | Checked at | Confidence | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SC-001 |  |  |  |  |  |  |  |  |  |  |  |

### Candidate screening summary

| Candidate | Linguistic | Cross-cultural | Market collision | Domain | Digital ecosystem | Trademark pre-risk | Overall status |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

---

## 14. Council configuration

```yaml
council_mode: FULL_COUNCIL | LIMITED_COUNCIL | INLINE_COUNCIL | HANDOFF_COUNCIL
profile: compact | standard | maximum_quality
neutral_dossier_version:
functional_roles:
methodology_lenses:
randomization_method:
blind_review_complete:
```

### Dispatch ledger

| Dispatch ID | Role/lens | Context isolation | Inputs | Output | Started | Completed | Degradation |
|---|---|---|---|---|---|---|---|
| D-001 |  |  |  |  |  |  |  |

### Initial votes

| Candidate | Role/lens | Vote | Rank | Success thesis | Strongest objection | Confidence |
|---|---|---|---:|---|---|---|
|  |  |  |  |  |  |  |

### Disagreement map

| Candidate | Support | Opposition | Fact conflict | Weight conflict | Missing evidence | Knockout claim |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### Cross-examination record

| Round | Advocate | Candidate | Opponent/challenger | Claim | Challenge | Rebuttal | Concession | Evidence needed |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

### Final votes

| Candidate | Role/lens | Initial vote | Final vote | Changed? | Reason | Remaining risk | Confidence |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

### Dissent

| Candidate | Dissenter | Position | Evidence/logic | Controller adjudication | Still unresolved? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## 15. Audience testing

```yaml
required:
status:
research_question:
sample_size:
markets:
languages:
buyer_user_mix:
method:
candidate_order_randomized:
logo_blind:
descriptor_conditions:
limitations:
```

| Candidate | Liking | Pronunciation | Spelling | Immediate recall | Delayed recall | Category fit | Trust | Distinctiveness | Negative associations | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |  |  |  |

---

## 16. Scorecard and Pareto view

| Candidate | Gate status | Strategy 14 | Distinction 14 | Memory 12 | Pronunciation 10 | Spelling 8 | Character 8 | Language 8 | Digital 8 | TM pre-risk 10 | Architecture 5 | Verbal/visual 3 | Range/Total | Confidence |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Pareto leaders

```yaml
strategy_leader:
distinction_leader:
memorability_leader:
pronunciation_spelling_leader:
international_leader:
digital_practicality_leader:
preliminary_legal_leader:
architecture_leader:
bold_leader:
audience_language_leader:
```

---

## 17. Finalist dossiers

For each finalist, link or include:

```yaml
candidate:
pronunciation:
name_type:
core_idea:
honest_origin:
strategic_case:
memorability_case:
competitive_case:
linguistic_case:
domain_strategy:
digital_collisions:
trademark_pre_screen:
architecture:
verbal_identity_potential:
wordmark_potential:
success_thesis:
strongest_objection:
rebuttal:
failure_conditions:
mitigation:
status:
confidence:
next_required_check:
```

---

## 18. Decision log

Append; do not overwrite.

| Decision ID | Date | Decision authority | Selected/affected candidate | Decision | Primary reason | Strongest rival | Why rival lost | Open risk | Required action |
|---|---|---|---|---|---|---|---|---|---|
| DEC-001 |  |  |  |  |  |  |  |  |  |

### Current recommendation

```yaml
primary_recommendation:
safer_alternative:
bolder_alternative:
status:
validated_knockouts:
unresolved_evidence:
minority_dissent:
conditions_that_change_decision:
```

---

## 19. External action and authority ledger

The skill does not purchase, register, file, publish, or claim accounts without explicit authority.

| Action ID | Action | Asset/jurisdiction | Requested by | Authority status | Executed by | Date | Evidence |
|---|---|---|---|---|---|---|---|
| A-001 | domain registration / legal filing / handle claim / public launch |  |  | NOT_AUTHORIZED / AUTHORIZED / COMPLETE |  |  |  |

---

## 20. Completion snapshot

```yaml
project_completion_status:
brief_status:
strategy_status:
market_research_status:
generation_status:
linguistic_status:
digital_status:
trademark_pre_screen_status:
council_status:
audience_test_status:
decision_status:
external_actions_outstanding:
evidence_expiry_or_recheck_date:
exact_next_action:
```

### Required limitations statement

> The recommendation reflects the approved brief and evidence available as of the recorded dates. Preliminary trademark and linguistic screening do not replace qualified legal counsel or native-speaker review. Domain, handle, company, app, and trademark statuses can change and must be re-checked immediately before action.
