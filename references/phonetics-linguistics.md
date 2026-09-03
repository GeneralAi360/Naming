# Phonetics, pronunciation, sound symbolism, and cross-cultural linguistics

## 1. Purpose

This document defines how the skill evaluates the spoken and linguistic behavior of names. A name is not only a written token. It must survive hearing, speaking, remembering, dictating, searching, inflecting, translating, and being interpreted by people who do not know the naming story.

Phonetic and linguistic analysis is probabilistic. It can identify patterns and risks; it cannot guarantee one universal emotional reaction.

---

## 2. Build `PHONETIC_CODE` before judging names

A phonetic code converts brand personality into a testable sound direction.

### 2.1 Required fields

```yaml
primary_spoken_language:
secondary_spoken_languages: []
script_requirements: []
letter_range:
syllable_range:
preferred_syllable_shapes: []
preferred_stress:
preferred_tempo:
preferred_vowels: []
preferred_consonants: []
desired_sound_attributes: []
permitted_starts: []
permitted_endings: []
avoid_clusters: []
avoid_endings: []
acceptable_pronunciation_variants: []
unacceptable_variants: []
transliteration_policy:
visual_letter_opportunities: []
liked_reference_properties: []
```

### 2.2 Example sound attributes

- precise;
- stable;
- warm;
- gentle;
- energetic;
- fast;
- premium;
- technical;
- human;
- playful;
- rebellious;
- calm;
- expansive;
- intimate;
- authoritative.

Do not select all. Prioritize two or three and define an unwanted opposite.

---

## 3. Phonetic anatomy of a candidate

For every serious candidate record:

```text
ORTHOGRAPHY
EXPECTED PRONUNCIATION BY LANGUAGE
IPA, when useful
SYLLABLE BREAKS
PRIMARY STRESS
ONSET / NUCLEUS / CODA PATTERN
VOWEL QUALITY
CONSONANT CHARACTER
RHYTHM
LIKELY ALTERNATE READINGS
LIKELY MISHEARINGS
LIKELY MISSPELLINGS
```

### 3.1 Syllable structures

Common patterns:

- `CV` — consonant + vowel;
- `CVC`;
- `CVCV`;
- `VCVC`;
- mixed multi-syllable forms.

Open syllables often feel easier across languages; closed syllables can feel firmer or more compact. This is a tendency, not a universal law.

### 3.2 Stress

Check:

- whether first-sight readers place stress consistently;
- whether Russian and English speakers shift stress;
- whether different stress changes associations;
- whether marketing would constantly need to teach pronunciation.

A stress mismatch is not always fatal, but it must be deliberate and manageable.

### 3.3 Mouthfeel

Observe:

- tongue and lip movement;
- difficult transitions;
- repeated articulation points;
- breath and voicing;
- whether the name feels clipped, flowing, heavy, or light;
- whether it remains easy in a sentence, not only in isolation.

---

## 4. Sound symbolism

### 4.1 Principle

People can form impressions from sounds before or alongside semantic meaning. Published Lexicon materials use sound symbolism, letter structure, repetition, and fluency as part of naming. The skill may use these as hypotheses, never deterministic claims.

### 4.2 Useful dimensions

#### Voicing

- voiced consonants can feel fuller, heavier, or warmer;
- voiceless consonants can feel faster, sharper, or lighter.

#### Stop vs continuant

- stops can create precision, impact, control, or abruptness;
- fricatives and liquids can create flow, softness, motion, or continuity.

#### Front vs back vowels

- front vowels may be perceived as smaller, lighter, brighter, or faster;
- back vowels may be perceived as larger, heavier, darker, or broader.

#### Repetition

- repeated phonetic patterns can improve fluency and recall;
- too much repetition can become childish, sing-song, or confusing.

#### Rare or “power” letters

Letters such as X, V, Z, Q, or K can signal technology, energy, sharpness, or novelty in some markets, but are heavily overused in others. Evaluate category saturation, language, and pronunciation before using them.

### 4.3 Sound-symbolism report language

Allowed:

> The hard initial stop and clipped ending may support a perception of precision in English-speaking contexts.

Not allowed:

> The letter K scientifically guarantees trust.

### 4.4 Familiarity and surprise

Use four quadrants:

| | Low surprise | High surprise |
|---|---|---|
| High familiarity | fluent but possibly generic | “surprisingly familiar” target zone |
| Low familiarity | weak/random | distinctive but potentially difficult |

The target depends on the brief. Regulated brands may lean toward familiarity; challenger brands may accept more surprise.

---

## 5. Pronunciation tests

### 5.1 First-sight test

Show only the written name with no pronunciation cue. Ask or predict:

- where stress falls;
- how many syllables;
- which letters create ambiguity;
- whether users disagree.

Do not teach the intended pronunciation before the test.

### 5.2 One-hearing test

Speak the name once. Can a person:

- repeat it immediately;
- preserve stress and phonemes;
- distinguish it from common words and competitors?

### 5.3 Telephone test

Can a person dictate it without spelling every letter? If spelling is required, is the explanation short and stable?

### 5.4 Voice-assistant test

When available, test speech-to-text in relevant languages and accents. Record observed outputs. Do not invent results.

### 5.5 Sentence tests

- “I work at ___.”
- “We use ___.”
- “Send it through ___.”
- “Search for ___.”
- “Have you tried ___?”

A name that works alone may fail in normal speech through rhythm or ambiguity.

---

## 6. Spelling and searchability

### 6.1 Write-from-hearing

Record likely variants:

```text
INTENDED: ______
MOST LIKELY VARIANT 1: ______
VARIANT 2: ______
VARIANT 3: ______
```

Classify:

- `TOLERABLE` — small variation; easy redirect or correction;
- `COSTLY` — regular explanation or traffic leakage;
- `FATAL` — audience cannot reliably find or share the brand.

### 6.2 Orthographic ambiguity

Check:

- C/K/Q choices;
- F/PH;
- I/Y;
- S/Z/C;
- doubled consonants;
- silent letters;
- hyphen/space ambiguity;
- numerals vs words;
- Russian transliteration variants;
- diacritics and ASCII fallback.

### 6.3 Controlled irregularity

One nonstandard feature may increase distinction. More than one often increases error exponentially. Test the normal spelling against the altered form and prove the irregularity earns its cost.

---

## 7. Cross-language screening

### 7.1 Required languages

Use all target-market languages plus common bridge languages when relevant. Distinguish:

- language of legal registration;
- language of marketing;
- language spoken by buyer;
- language spoken by end user;
- language of customer support/search.

### 7.2 Screening dimensions

For each language:

- first-sight pronunciation;
- likely stress;
- spelling intuitiveness;
- dictionary meanings;
- slang and current internet meanings;
- taboo or insulting sound-alikes;
- sexual, medical, pharmaceutical, criminal, religious, or political associations;
- person names, surnames, place names, institutions;
- morphology and inflection;
- gender/number/case behavior;
- abbreviations and initials;
- existing brands and category confusion;
- cultural register: elegant, childish, outdated, rural, elite, bureaucratic, etc.

### 7.3 Severity classification

- `NONE` — no relevant concern found;
- `LOW` — weak or idiosyncratic association;
- `MEDIUM` — plausible negative or confusion requiring validation;
- `HIGH` — strong, audience-relevant negative/conflict;
- `KNOCKOUT` — severe and well-supported incompatibility;
- `UNKNOWN` — insufficient evidence.

### 7.4 Evidence classification

```text
MODEL_HYPOTHESIS
DICTIONARY_CHECKED
CORPUS_OR_SEARCH_CHECKED
NATIVE_SPEAKER_CHECKED
MULTI_NATIVE_VALIDATED
PROFESSIONAL_LINGUISTIC_REVIEW
```

Model-based review cannot be relabeled as native validation.

### 7.5 Native-speaker protocol

For important markets:

1. use at least two relevant speakers when possible;
2. prefer people currently living in the target culture;
3. include target-audience familiarity;
4. provide no pronunciation cues initially;
5. ask for spontaneous reading, spelling, meanings, slang, and brands recalled;
6. record level of concern, not only yes/no;
7. investigate concerns raised by more than one respondent;
8. do not automatically reject on one idiosyncratic association.

---

## 8. Russian-English bilingual checks

When a name must work in both Russian and English:

### 8.1 Script direction

Decide:

- Latin-only global master form;
- Cyrillic-only local form;
- official bilingual forms;
- Latin master with Cyrillic pronunciation guide;
- separate legal and marketing spellings.

### 8.2 Common collision points

- `r/l` perception by other language groups;
- English `th`, `w`, and vowel reduction;
- Russian consonant clusters and final devoicing;
- soft/hard consonant differences;
- `e/ye`, `ю/yu`, `я/ya`, `х/kh/h`, `ц/ts`, `ж/zh` transliteration;
- stress not shown in writing;
- English readers treating a coined word under familiar spelling rules;
- Russian users writing the heard name in multiple Latin forms.

### 8.3 Bilingual resonance standard

The name does not need identical pronunciation. It needs:

- acceptable pronunciation in each language;
- no severe meaning conflict;
- manageable spelling behavior;
- a stable official form;
- consistent brand recognition.

---

## 9. Morphology and grammar

A name should be tested as language, not only as a logo.

### 9.1 Russian

Check:

- склоняется ли название;
- как звучат родительный, дательный и предложный падежи;
- какой род ему приписывают;
- образуется ли прилагательное;
- образуется ли название пользователя/специалиста;
- не возникает ли комического окончания;
- как выглядит кириллическая запись.

### 9.2 English

Check:

- plural;
- possessive;
- article use;
- verb conversion;
- adjective/agent forms;
- pronunciation of suffixes;
- ambiguity with common words.

### 9.3 Other languages

Use qualified linguistic support when morphology is complex or commercially important.

---

## 10. Semantic and cultural risk

### 10.1 Literal meaning vs audience effect

Do not reject a candidate only because one dictionary sense is negative. Determine:

- frequency of the meaning;
- whether target users know it;
- whether it dominates spontaneous interpretation;
- whether the product context neutralizes or amplifies it;
- whether the tension is strategically useful or reputationally dangerous.

### 10.2 Curse of knowledge

A founder or technical team may love an obscure reference no customer can perceive. Test:

- does the name work without the reference?
- is the explanation short and rewarding?
- is the reference culturally shared?
- does missing the hidden meaning create confusion?

### 10.3 Medical/pharmaceutical association

Coined names often accidentally resemble drugs, anatomy, disorders, or clinical devices. Search:

- exact and phonetic medical terms;
- common drug-name suffixes;
- active pharmaceutical brands;
- anatomy and pathology terms.

Severity depends on product category and target market.

### 10.4 Political/religious/cultural material

Treat sacred names, national symbols, ethnic terms, conflicts, and political figures as high-risk. Do not use them for borrowed attention without a clear authentic basis and professional review.

---

## 11. Phonetic similarity and confusion

### 11.1 Similarity layers

- exact spelling;
- normalized spelling;
- edit distance;
- shared prefix/suffix;
- syllable pattern;
- stress pattern;
- consonant skeleton;
- vowel skeleton;
- phonetic algorithms such as Soundex/Metaphone where relevant;
- human spoken confusion;
- transliteration similarity.

Automated similarity is a flag. Human and legal interpretation remain necessary.

### 11.2 Short names

For short names, even one- or two-character differences may be insufficient. Apply stricter phonetic and category checks.

### 11.3 Anti-confusion set

Compare finalists against:

- direct competitors;
- adjacent software/apps;
- banks and financial products;
- telecoms;
- pharmaceuticals;
- major consumer brands;
- relevant local institutions;
- common voice-assistant outputs.

---

## 12. Memory and cognition tests

### 12.1 Immediate recall

After brief exposure, can the user recall:

- approximate sound;
- exact or near-exact spelling;
- the main association?

### 12.2 Delayed recall

Test after 10–20 minutes and, when possible, 24 hours. Separate recognition from unaided recall.

### 12.3 Memory hook classification

- semantic image;
- sound pattern;
- rhyme/repetition;
- surprise/tension;
- customer phrase;
- cultural reference;
- visual letterform;
- emotional story.

A candidate with no hook may require excessive media spend.

### 12.4 Fluency paradox

Very fluent names can disappear into category sameness. Very surprising names can fail adoption. Evaluate both:

```text
PROCESSING FLUENCY
DISTINCTIVE SURPRISE
```

Do not collapse them into one score.

---

## 13. Wordmark and visual-letter potential

Evaluate without designing the logo:

- silhouette in uppercase/lowercase;
- distinctive first/last letter;
- repeated shapes;
- symmetry/asymmetry;
- ligature potential;
- monogram potential;
- favicon abbreviation;
- risk of ambiguous glyphs (`I/l/1`, `O/0`, `rn/m`);
- readability at small size.

A visual trick cannot rescue a weak spoken name.

---

## 14. Phonetic scorecard

Suggested 100-point specialist score:

| Dimension | Weight |
|---|---:|
| First-sight pronunciation | 15 |
| One-hearing repeatability | 15 |
| Spelling from hearing | 12 |
| Stress stability | 8 |
| Rhythm and mouthfeel | 10 |
| Fit with phonetic code | 12 |
| Distinction from competitors | 10 |
| Cross-language portability | 10 |
| Memory hook | 8 |
| Total | 100 |

Use `UNKNOWN` rather than guessing where evidence is missing.

---

## 15. Specialist output template

```text
NAME:
LANGUAGE(S):
EXPECTED PRONUNCIATION:
IPA:
SYLLABLES / STRESS:
PHONETIC CHARACTER:
SOUND-SYMBOLISM HYPOTHESIS:
PROCESSING FLUENCY:
DISTINCTIVE SURPRISE:
FIRST-SIGHT RISKS:
WRONG-HEARING TREE:
SPELLING RISKS:
CROSS-LANGUAGE ISSUES:
MORPHOLOGY / INFLECTION:
COMPETITOR PHONETIC COLLISIONS:
WORDMARK LETTER POTENTIAL:
EVIDENCE LEVEL:
VOTE:
CONFIDENCE:
NEXT VALIDATION:
```

---

## 16. Knockout conditions

Recommend rejection when sufficiently supported:

- pronunciation cannot stabilize in the primary market;
- the most common hearing maps to another active direct brand;
- a severe negative/taboo meaning dominates in a key market;
- spelling leakage is incompatible with the approved digital strategy;
- transliteration creates several equally likely official forms with no manageable solution;
- the name is essentially a misspelling of a competitor or major brand;
- the required language form cannot be legally or technically used.

Do not treat minor accent variation as a knockout.

---

## 17. Public source foundation

This protocol incorporates the user-supplied phonetic-code, one-hearing, spelling, telephone, recall, voice-assistant, bilingual, and linguistic-screening requirements. It is also informed by publicly documented Lexicon emphasis on sound symbolism, letter structure, fluency, quantity, and attention/surprise, and Catchword’s structured linguistic/cultural evaluation with relevant native speakers.
