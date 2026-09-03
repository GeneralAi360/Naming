# Naming subagent dispatch template

Use this template to create bounded, auditable subagent assignments. Do not send the entire conversation when a neutral dossier and task-local evidence are sufficient.

---

## 1. Dispatch identity

```yaml
dispatch_id:
project_id:
phase:
round:
role_or_lens:
profile: compact | standard | maximum_quality
fresh_context_required: true
parent_controller:
```

---

## 2. Role boundary

```text
ROLE:

MANDATE:

YOU OWN:

YOU DO NOT OWN:

VALID VETO BOUNDARY:

NO CHILD AGENTS.
NO SCOPE EXPANSION.
NO DIRECT USER CONTACT UNLESS EXPLICITLY ASSIGNED.
NO GIT, DOMAIN PURCHASE, TRADEMARK FILING, HANDLE CLAIM, OR PUBLIC ACTION.
```

For a published-methodology lens include:

```text
THIS IS AN ANALYTICAL APPLICATION OF PUBLICLY DOCUMENTED PRINCIPLES.
YOU ARE NOT THE PERSON OR FIRM, DO NOT SPEAK FOR THEM, AND MUST NOT CLAIM THEIR ENDORSEMENT.
USE ONLY THE PRINCIPLES IN THE PROVIDED EXPERT-PRINCIPLES EXCERPT.
```

---

## 3. Inputs

Provide only:

```yaml
neutral_dossier_version:
neutral_dossier_path_or_excerpt:
approved_criteria:
relevant_candidate_ids:
relevant_evidence:
known_unknowns:
no_go_excerpt_if_needed:
required_expert_principles_excerpt_if_methodology_lens:
```

### Source/evidence rules

- Treat the approved brief as authoritative within the assignment.
- Distinguish `VERIFIED_PRIMARY`, `VERIFIED_SECONDARY`, `CORROBORATED`, `OBSERVED`, `MODEL_HYPOTHESIS`, `USER_REPORTED`, and `UNKNOWN`.
- Do not invent missing facts.
- Do not upgrade a model inference into native-speaker, legal, domain, or market evidence.
- During blind review, do not seek or infer other reviewers’ votes.

---

## 4. Task

```text
PRIMARY QUESTION:

SECONDARY QUESTIONS:
1.
2.
3.

CANDIDATES TO REVIEW:

REQUIRED TESTS:

STOP CONDITIONS:
```

---

## 5. Required output

```yaml
role_or_lens:
dispatch_id:
dossier_version:
source_boundary_confirmed:
mandate_boundary_confirmed:
```

For each candidate:

```yaml
candidate_id:
position: ADVANCE | HOLD | REJECT
rank:
criterion_fit:
strongest_positive:
strongest_objection:
evidence:
interpretation:
unknowns:
role_specific_veto:
veto_basis:
mitigation:
failure_conditions:
confidence:
```

Overall:

```yaml
first_choice:
runner_up:
rejected_candidates:
success_thesis_for_first_choice:
strongest_rival_advantage:
why_rival_ranks_lower:
evidence_that_would_change_vote:
missing_evidence:
```

---

## 6. Success thesis schema

```yaml
candidate:
audience_attention:
processing_and_recall_mechanism:
strategic_meaning:
competitive_separation:
emotional_or_identity_effect:
word_of_mouth_or_search_behavior:
required_descriptor:
required_verbal_activation:
required_visual_activation:
conditions_for_success:
leading_indicators:
falsification_test:
```

Avoid claims such as “it will be successful” or “it sounds premium.” Explain the mechanism, conditions, evidence, and falsification path.

---

## 7. Cross-examination assignment

For later rounds, add:

```yaml
candidate_defended:
strongest_rival_to_attack:
opposing_review_excerpt:
disputed_fact:
disputed_weight:
new_evidence:
```

Required response:

1. Restate the opponent’s strongest case fairly.
2. State one genuine advantage of the rival.
3. Defend the assigned candidate against its strongest objection.
4. Attack the strongest rival, not a weak decoy.
5. State one concession.
6. State exactly what evidence would change the position.

---

## 8. Functional-role dispatch examples

### `NAMING_STRATEGY_LEAD`

```text
Determine whether each candidate solves the approved naming brief and future architecture. Do not evaluate legal availability beyond supplied evidence. Identify descriptor dependence, strategic overloading, paradigm-shift fit, and conditions under which the name helps positioning.
```

### `COMPETITIVE_NAMING_CARTOGRAPHER`

```text
Compare candidates with the competitive naming taxonomy, saturated roots/patterns/metaphors, and white space. Identify category mimicry, search confusion, and genuine naming territory separation. Do not certify trademark availability.
```

### `CREATIVE_NAMING_DIRECTOR`

```text
Evaluate freshness, semantic compression, image, tension, category escape, proprietary material, story potential, and creative intensity. Attack retrofitted stories, random-letter neologisms, and cosmetic one-letter novelty.
```

### `PHONETIC_AND_SOUND_SYMBOLISM_LINGUIST`

```text
Evaluate syllables, stress, mouthfeel, sound attributes, first-sight reading, one-hearing repetition, likely wrong hearings, and fit with PHONETIC_CODE. Treat sound symbolism as probabilistic, not universal.
```

### `VERBAL_IDENTITY_AND_MEMORABILITY_CRITIC`

```text
Evaluate imagery, emotion, memory hook, verbal legs, sentence use, recommendation behavior, spelling friction, descriptor compatibility, and whether the name supports a durable language system.
```

### `CROSS_CULTURAL_LINGUIST`

```text
Evaluate meanings, slang, taboo, pronunciation, morphology, transliteration, and cultural associations in the assigned languages. Mark model-only findings as hypotheses and specify native-speaker questions.
```

### `DIGITAL_AVAILABILITY_RESEARCHER`

```text
Research exact and similar domains, active web entities, apps, software packages, directories, and critical handles. Record exact status, source, and date. Do not infer availability from an absent site.
```

### `TRADEMARK_PRE_SCREENER`

```text
Conduct only preliminary official-database screening across the assigned jurisdictions and goods/services. Search exact, phonetic, transliterated, and confusingly similar forms. Never claim legal clearance.
```

### `BRAND_ARCHITECTURE_STRATEGIST`

```text
Test master-brand, product-family, feature, geography, and future-extension use. Identify restrictive meaning, syntax breakdown, portfolio collisions, and expansion failure.
```

### `AUDIENCE_LANGUAGE_ADVOCATE`

```text
Evaluate whether the candidate matches real customer language, identity, trust cues, word-of-mouth behavior, and category expectations. Separate customer evidence from marketer preference.
```

### `SKEPTICAL_RED_TEAM`

```text
Build the strongest evidence-based failure case for every leading candidate. Test correlated enthusiasm, founder attachment, descriptor dependence, negative misuse, trend half-life, legal/domain wishful thinking, and false scoring precision.
```

### `EVIDENCE_AUDITOR`

```text
Audit whether every material claim has the right evidence class, date, source, and scope. Find contradictions, stale checks, unsupported superlatives, missing markets, and conclusions that exceed evidence.
```

---

## 9. Methodology-lens dispatch examples

### `LEXICON_PLACEK_LENS`

```text
Apply the supplied public-principles excerpt concerning broad exploration, sound symbolism, processing fluency, surprise, attention, and disciplined quantity-to-quality convergence. Identify the candidate with the strongest useful balance of familiarity and novelty. Do not claim David Placek or Lexicon would choose it.
```

### `MEYERSON_PROCESS_BRIEF_LENS`

```text
Apply the supplied public-principles excerpt concerning brief discipline, naming approach, systematic process, structured screening, and decision traceability. Identify which candidate most defensibly solves the approved assignment. Do not claim Rob Meyerson would choose it.
```

### `WATKINS_SMILE_SCRATCH_LENS`

```text
Apply the supplied SMILE/SCRATCH principles: suggestiveness, memorability, imagery, legs, emotion, and the risks of spelling challenge, copycat form, restrictiveness, annoyance, tameness, curse of knowledge, and pronunciation difficulty. Do not claim Alexandra Watkins would choose it.
```

### `IGOR_DISTINCTIVENESS_LENS`

```text
Apply the supplied public principles concerning competitive naming taxonomy, emotional engagement, category position, stopping power, and resistance to consensus-driven blandness. Do not claim Igor International would choose it.
```

### `ALTMAN_SYSTEMATIC_CREATIVITY_LENS`

```text
Apply the supplied public principles concerning systematic creativity, broad exploration, bad-name/reverse exercises, rejection of the single-eureka myth, and avoiding over-description. Do not claim Eli Altman or A Hundred Monkeys would choose it.
```

### `CATCHWORD_GLOBAL_LENS`

```text
Apply the supplied public principles concerning strategy-led creativity, memorability, linguistic/cultural review, distinctiveness, practical screening, and careful audience research. Do not claim Catchword would choose it.
```
