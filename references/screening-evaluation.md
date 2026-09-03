# Screening, evidence, evaluation, and decision gates

## 1. Purpose

This reference defines how the naming system verifies candidates after creative generation. It separates factual research from brand judgment, prevents false availability claims, and makes the final recommendation auditable.

The screening system has six layers:

1. identity and exact-match discovery;
2. market/category collision research;
3. domain and digital-asset research;
4. preliminary trademark screening;
5. linguistic, usability, and audience evidence;
6. decision gates, scorecards, and final status.

A candidate can be creatively strong and still fail. A candidate can appear digitally convenient and still be strategically weak. Never collapse all evidence into one vague “available / unavailable” label.

---

## 2. Evidence doctrine

### 2.1 Evidence classes

Every material claim must carry one of these classes:

- `VERIFIED_PRIMARY` — supported by an authoritative first-party database, registry, official company source, registrar/RDAP response, or direct test result;
- `VERIFIED_SECONDARY` — supported by a credible independent source but not the authoritative registry;
- `CORROBORATED` — supported by at least two independent sources that materially agree;
- `OBSERVED` — directly observed in a live search, page, app store, social network, pronunciation test, or respondent session;
- `MODEL_HYPOTHESIS` — an analytical inference that still needs human or external validation;
- `USER_REPORTED` — supplied by the user and not independently checked;
- `UNKNOWN` — evidence is unavailable, contradictory, stale, inaccessible, or insufficient.

Do not silently upgrade one class into another.

### 2.2 Required evidence fields

Store each material check in `SCREENING_LEDGER`:

```yaml
candidate_id:
check_id:
check_type:
query_or_asset:
market:
language:
category_or_goods_services:
result:
status:
evidence_class:
source_name:
source_location:
checked_at_utc:
reviewer_or_agent:
confidence:
materiality:
notes:
follow_up:
```

### 2.3 Freshness

Availability and legal data can change. Every live check requires `checked_at_utc`.

Use these default freshness categories:

- `CURRENT_SESSION` — checked during the current naming run;
- `RECENT` — checked within 30 days;
- `STALE` — older than 30 days for domain/social availability or older than 90 days for active-use landscape research;
- `HISTORICAL_ONLY` — useful for decision history, not current clearance;
- `UNKNOWN_DATE` — cannot support an availability claim.

Re-check finalists immediately before registration, filing, launch, or public announcement.

### 2.4 Source hierarchy

For factual availability, prefer:

1. official registry/database or protocol response;
2. official owner/product/company page;
3. direct app-store/social-platform result;
4. reputable company/market databases;
5. search-engine results;
6. aggregators, broker pages, scraped directories, or model memory.

Lower layers can discover risk. They cannot overrule a current authoritative result without investigation.

---

## 3. Candidate identity normalization

Before searching, create an identity set for every candidate.

```yaml
canonical_name:
casefolded_name:
space_removed:
hyphen_removed:
punctuation_removed:
unicode_normalized:
latin_transliteration:
cyrillic_transliteration:
likely_misspellings:
likely_hearings:
phonetic_keys:
plural_or_inflected_forms:
abbreviations:
compound_splits:
```

Search exact and confusingly similar forms. A clean exact match is not enough if the spoken or visual form collides.

### 3.1 Similarity dimensions

Evaluate separately:

- orthographic similarity;
- phonetic similarity;
- semantic similarity;
- transliteration similarity;
- visual/logo similarity when known;
- category proximity;
- geographic overlap;
- channel overlap;
- buyer/user overlap;
- goods/services overlap;
- fame or strength of the earlier mark/brand.

Never convert a string-distance metric into a legal conclusion. Levenshtein, Soundex, Metaphone, phoneme distance, and embedding similarity are discovery tools only.

---

## 4. Web and market collision screening

### 4.1 Search sequence

For every candidate entering serious screening, search:

1. exact name in quotation marks;
2. unquoted name;
3. exact name plus the category;
4. exact name plus `company`, `brand`, `app`, `software`, `service`, `product`, or local-language equivalents;
5. spaced, hyphenated, and concatenated forms;
6. likely misspellings and wrong-hearing variants;
7. transliterations in both directions;
8. phonetic neighbors;
9. candidate plus relevant customer problem or outcome;
10. candidate in target countries and languages.

Search results are discovery evidence, not a trademark clearance.

### 4.2 Collision record

For every material result, record:

```yaml
entity_name:
entity_type:
exact_or_similar:
active_status:
category:
market:
audience_overlap:
channel_overlap:
first_seen_or_founded:
source:
collision_severity:
confusion_rationale:
mitigation_possible:
```

### 4.3 Entity types must remain separate

Use explicit types:

- `OPERATING_BRAND`;
- `COMPANY_LEGAL_NAME`;
- `PRODUCT_OR_SERVICE`;
- `APP`;
- `OPEN_SOURCE_PROJECT`;
- `PACKAGE_OR_LIBRARY`;
- `SOCIAL_ACCOUNT`;
- `DOMAIN_ONLY`;
- `TRADEMARK_RECORD`;
- `MEDIA_TITLE`;
- `PERSON_OR_SURNAME`;
- `GEOGRAPHIC_NAME`;
- `OTHER`.

A legal company name, an app, a domain, and a registered mark are not interchangeable facts.

### 4.4 Market collision severity

- `NONE_OBSERVED` — no material result found in the performed search; not proof of absence;
- `LOW` — distant category/market with low plausible confusion;
- `MODERATE` — overlap in audience, channel, meaning, geography, or spoken form;
- `HIGH` — active adjacent or direct-category brand likely to cause confusion or search friction;
- `KNOCKOUT_CANDIDATE` — apparent direct conflict requiring rejection or qualified legal review;
- `UNKNOWN` — insufficient evidence.

### 4.5 Search visibility test

Evaluate likely search behavior:

- Does the term have an overwhelming dictionary, celebrity, geographic, medical, or news meaning?
- Are search results dominated by a powerful unrelated entity?
- Can the brand plausibly earn a distinctive result set?
- Will users search a predictable spelling?
- Does voice search return the intended word?
- Does transliteration create multiple competing spellings?

Do not promise SEO performance from the name alone.

---

## 5. Domain screening

### 5.1 Domain policy precedes domain search

The naming brief must state:

```yaml
required_exact_domains:
preferred_tlds:
acceptable_alternative_tlds:
prefix_or_suffix_policy:
domain_acquisition_budget:
acceptable_hyphens_or_numbers:
country_domain_strategy:
email_readability_requirement:
knockout_if_unavailable:
```

Do not reject a strong name for an occupied `.com` when `.com` was never a requirement. Do not recommend a workaround when the exact domain is an approved knockout.

### 5.2 Domain statuses

Use only these statuses:

- `AVAILABLE_TO_REGISTER` — current registrar/registry evidence indicates ordinary registration is available;
- `PREMIUM_REGISTRY` — available through the registry at premium pricing;
- `REGISTERED_ACTIVE` — registered and materially used by an active site/service;
- `REGISTERED_REDIRECT` — redirects to another active brand or asset;
- `REGISTERED_PARKED` — registered with parking/holding behavior and no verified active operating brand;
- `BROKERED_FOR_SALE` — listed for resale or broker negotiation;
- `REGISTERED_INACTIVE` — registered but no meaningful current site was observed;
- `RESERVED_OR_RESTRICTED` — registry policy prevents ordinary registration;
- `PENDING_DELETE_OR_REDEMPTION` — lifecycle state observed; do not call available;
- `UNKNOWN` — status could not be reliably established.

“Site does not load” is not a domain status.

### 5.3 Verification sequence

When possible, use at least two independent observations:

1. RDAP or authoritative registry/registrar lookup;
2. registrar availability/price check;
3. DNS records;
4. HTTP/HTTPS behavior;
5. broker or marketplace listing;
6. historical/site evidence when ownership context matters.

The ICANN Registration Data Access Protocol (RDAP) is the current standardized lookup protocol for generic top-level domain registration data. Legacy WHOIS references may still appear in tools and historical material; do not assume a legacy WHOIS result is current or authoritative.

### 5.4 Domain result record

```yaml
candidate:
domain:
tld:
status:
registrar_or_registry_price:
renewal_price_if_known:
rdap_or_registry_evidence:
dns_result:
http_result:
broker_result:
checked_at_utc:
evidence_class:
confidence:
notes:
```

### 5.5 Domain strategy options

Only use options allowed by the brief:

- acquire the exact domain;
- use an acceptable alternative TLD;
- use a country-code domain;
- add a natural action prefix such as `get`, `use`, or `try`;
- add a category or product descriptor;
- use a corporate domain and separate product path;
- choose a longer naturally available name;
- redesign the naming territory around domain availability.

Do not treat awkward domain hacks as automatically clever. Test speech, email dictation, trust, and leakage to the exact `.com`.

### 5.6 Digital leakage test

Estimate:

- wrong-domain traffic risk;
- email misdelivery risk;
- search confusion;
- spoken recommendation friction;
- dependency on spelling explanation;
- dependence on a prefix/suffix users will omit;
- risk that the exact-domain owner is a competitor or hostile actor.

Classify `LOW`, `MEDIUM`, `HIGH`, or `UNKNOWN`.

---

## 6. Digital ecosystem screening

The relevant ecosystem depends on the product. Check only material channels, but do not omit a critical one.

Possible channels:

- Apple App Store;
- Google Play;
- Microsoft Store;
- Chrome/Firefox extension stores;
- GitHub/GitLab;
- npm, PyPI, crates.io, Maven, NuGet, RubyGems, Docker Hub, package registries;
- Product Hunt and startup directories;
- LinkedIn company pages;
- Crunchbase or regional company databases;
- major social platforms;
- podcast, newsletter, marketplace, game, or media-title catalogs;
- local business registries where relevant.

### 6.1 Handle status

Use:

- `AVAILABLE_OBSERVED`;
- `TAKEN_ACTIVE_RELEVANT`;
- `TAKEN_ACTIVE_UNRELATED`;
- `TAKEN_INACTIVE`;
- `RESERVED`;
- `UNKNOWN`.

Platform handle availability changes quickly. Never claim permanent availability.

### 6.2 Open-source and software collisions

For technical products, check:

- package names;
- repositories and organizations;
- command-line binaries;
- protocols and standards;
- security products and malware names;
- existing AI models or datasets;
- common error codes/acronyms.

An obscure package can still create technical, reputational, or discoverability friction.

---

## 7. Preliminary trademark screening

## 7.1 Boundary

This is **preliminary screening**, not legal clearance, registrability advice, a freedom-to-operate opinion, or a guarantee of use.

Always state:

> Preliminary trademark screening can identify obvious and material risks, but final clearance and filing strategy require a qualified trademark professional in each relevant jurisdiction.

### 7.2 Required inputs

Before screening, establish:

```yaml
jurisdictions:
actual_goods_services:
future_goods_services:
sales_channels:
buyer_and_user:
likely_nice_classes_hypothesis:
word_mark_or_device_mark:
launch_timeline:
risk_tolerance:
```

Nice classes are administrative search aids, not the whole confusion analysis. Similarity can matter across classes when goods/services, channels, audiences, or commercial impression overlap.

### 7.3 Official research starting points

Use the relevant official systems, such as:

- WIPO Global Brand Database for international and participating-office records;
- EUIPO eSearch/TMview for European Union and participating-office searches;
- USPTO Trademark Search for United States records;
- official national or regional intellectual-property office databases for each target market.

WIPO itself advises searching national/regional registers in addition to its global database. Do not represent one database as complete for all jurisdictions.

### 7.4 Search ladder

For each candidate search:

1. exact word mark;
2. spacing, hyphenation, plural, and punctuation variants;
3. prefixes/suffixes and dominant fragments;
4. phonetic equivalents;
5. common misspellings;
6. transliterations and translations;
7. visually similar forms;
8. semantically similar marks when relevant;
9. related goods/services;
10. adjacent classes or channels that may create confusion;
11. owner portfolios for suspiciously close results;
12. status and jurisdiction of records.

### 7.5 Record statuses

Use source-specific status accurately. Normalize separately:

- `LIVE_OR_ACTIVE`;
- `PENDING`;
- `REGISTERED`;
- `EXPIRED`;
- `ABANDONED`;
- `CANCELLED`;
- `REFUSED`;
- `UNKNOWN`.

An abandoned or expired record is not proof that the name is safe. Common-law or unregistered use, newer filings, company names, and other rights may remain.

### 7.6 Preliminary risk classification

- `LOW_PRELIMINARY_RISK` — no material conflict found in the defined search, with meaningful caveats;
- `MEDIUM_PRELIMINARY_RISK` — one or more similarities require legal analysis, narrowing, consent strategy, or jurisdiction-specific review;
- `HIGH_PRELIMINARY_RISK` — direct/adjacent live marks or highly similar commercial impressions create substantial concern;
- `UNKNOWN_PRELIMINARY_RISK` — incomplete access, ambiguous goods/services, language uncertainty, or unresolved records;
- `KNOCKOUT_PENDING_COUNSEL` — evidence strongly suggests rejection, but a legal professional must determine final disposition if the candidate is strategically indispensable.

Never use `LEGALLY_CLEAR`, `SAFE`, or `GUARANTEED_REGISTRABLE`.

### 7.7 Trademark result record

```yaml
candidate:
jurisdiction:
database:
search_date:
classes_or_goods_services:
query_variants:
exact_hits:
similar_hits:
relevant_owner:
record_status:
commercial_impression_notes:
category_channel_audience_overlap:
preliminary_risk:
evidence_class:
limitations:
required_counsel_question:
```

### 7.8 Common-law and marketplace use

Where relevant, separately research:

- active unregistered brands;
- company names;
- product listings;
- local business use;
- press and trade publications;
- app stores and social channels;
- domain history.

Do not imply that registry absence equals freedom to use.

---

## 8. Linguistic and cultural evidence integration

Use [phonetics and linguistics](phonetics-linguistics.md) for the full protocol.

For decision purposes, normalize:

- `LINGUISTIC_PASS` — no material issue found in performed checks;
- `LINGUISTIC_PASS_WITH_NOTES` — manageable pronunciation/spelling/association issues;
- `NATIVE_REVIEW_REQUIRED` — model or dictionary screening is insufficient;
- `LANGUAGE_RISK_MEDIUM`;
- `LANGUAGE_RISK_HIGH`;
- `PRONUNCIATION_FAILURE`;
- `SPELLING_FAILURE`;
- `UNKNOWN`.

A single unusual association from one person is not automatically a veto. Determine prevalence, salience, audience relevance, severity, and mitigation.

---

## 9. Audience testing

### 9.1 What not to do

Do not ask only:

> Which name do you like best?

Preference alone encourages familiarity bias, politeness, visual-design bias, and committee compromise.

Do not present a polished logo for one candidate and plain text for another.

### 9.2 Blind test design

Where possible:

1. randomize candidate order;
2. use equal typography and exposure time;
3. separate spontaneous name response from explanatory copy;
4. test names with and without a neutral descriptor;
5. avoid revealing founder preference;
6. recruit actual or close-proxy buyers/users;
7. distinguish buyer, user, partner, and internal employee reactions;
8. collect verbatim language before scales;
9. record sample limitations.

### 9.3 Core tasks

For each finalist:

1. `FIRST_SIGHT` — show briefly and ask for pronunciation;
2. `ONE_HEARING` — say it once and ask for repetition;
3. `SPELLING` — ask respondent to write what they heard;
4. `IMMEDIATE_RECALL` — remove and ask what they remember;
5. `DELAYED_RECALL` — test after 10–20 minutes;
6. `NEXT_DAY_RECALL` — when practical, test after 24 hours;
7. `ASSOCIATION` — collect first three associations;
8. `CATEGORY_EXPECTATION` — ask what product/company they expect;
9. `ATTRIBUTE_RATING` — trust, relevance, distinctiveness, modernity, warmth, authority, premium/mass character as appropriate;
10. `RECOMMENDATION_SENTENCE` — “You should try ___”;
11. `INTRODUCTION_SENTENCE` — “I work at ___” / “We use ___”;
12. `SEARCH_BEHAVIOR` — ask how they would type/search it;
13. `PAIRWISE_CHOICE` — compare finalists on named criteria, not general liking;
14. `MISUSE_TEST` — ask for likely joke, nickname, abbreviation, or hostile reinterpretation.

### 9.4 Metrics remain separate

Report separately:

- spontaneous liking;
- pronunciation accuracy;
- spelling accuracy;
- immediate recall;
- delayed recall;
- category fit;
- strategic attribute fit;
- trust;
- distinctiveness;
- word-of-mouth usability;
- negative association rate;
- polarization;
- descriptor dependence.

Do not collapse all respondent behavior into one “winning percentage.”

### 9.5 Sample interpretation

A small qualitative study can discover issues and language. It cannot establish population-level certainty.

Record:

```yaml
sample_size:
recruitment_source:
market:
language:
buyer_user_mix:
exposure_method:
candidate_order_method:
researcher:
date:
limitations:
```

### 9.6 Polarization

Classify negative responses:

- `MATERIAL_SHARED_RISK`;
- `SEGMENT_SPECIFIC_RISK`;
- `CORRECTABLE_WITH_DESCRIPTOR`;
- `PRODUCTIVE_DISTINCTIVENESS`;
- `IDIOSYNCRATIC`;
- `UNKNOWN`.

Do not automatically prefer the least objectionable name. Blandness can score well in preference surveys while performing weakly in memory and differentiation.

---

## 10. Hard gates and knockout criteria

Apply hard gates before weighted scoring.

A candidate is excluded or held when any approved condition applies:

- verified direct active brand conflict;
- high preliminary trademark risk in a critical jurisdiction;
- mandatory exact domain unavailable under a no-acquisition policy;
- serious negative meaning or taboo in a primary language;
- unstable pronunciation or spelling beyond approved tolerance;
- clear copy of a famous or category competitor name;
- violation of future architecture;
- direct conflict with the approved `MUST_NOT_HAVE` list;
- already rejected by the valid decision authority;
- evidence manipulation or invented origin required to make the name persuasive.

Use:

- `REJECTED_KNOCKOUT`;
- `HOLD_PENDING_EVIDENCE`;
- `ADVANCE_WITH_MITIGATION`;
- `ADVANCE`.

A knockout must cite the criterion and evidence. Personal dislike is not a knockout.

---

## 11. Weighted evaluation

### 11.1 Default 100-point model

| Criterion | Weight |
|---|---:|
| Strategic fit | 14 |
| Category distinction | 14 |
| Memorability | 12 |
| Pronunciation | 10 |
| Spelling | 8 |
| Emotional/verbal character | 8 |
| International/linguistic safety | 8 |
| Domain/digital practicality | 8 |
| Preliminary trademark perspective | 10 |
| Scalability/architecture | 5 |
| Wordmark and verbal-system potential | 3 |
| **Total** | **100** |

Weights must be changed when the brief demands it. Examples:

- consumer launch: raise memorability, emotional character, and word-of-mouth;
- regulated international product: raise linguistic, architecture, and legal perspective;
- local campaign: lower long-term architecture and domain weight;
- enterprise master brand: raise strategy, trust, architecture, and legal perspective.

### 11.2 Scoring scale

Score each criterion from 0–10 before applying weight:

- `0–2` — fundamental failure;
- `3–4` — weak/material concern;
- `5–6` — acceptable but undistinguished;
- `7–8` — strong with manageable weaknesses;
- `9` — exceptional evidence-backed performance;
- `10` — reserve for rare, strongly supported excellence.

### 11.3 Unknown evidence

Do not assign a neutral midpoint to `UNKNOWN`.

Use:

```yaml
score_range:
confidence:
evidence_gap:
maximum_possible_if_resolved:
minimum_possible_if_adverse:
```

Example:

```yaml
trademark_perspective:
  score_range: 2-8
  confidence: LOW
  evidence_gap: national register unavailable
```

### 11.4 No false arithmetic

The weighted total is a comparison aid, not a scientific forecast. Always show:

- hard-gate status;
- score/range;
- confidence;
- dominant trade-off;
- unresolved evidence;
- strongest dissent.

Do not declare 87 objectively superior to 85 without explaining the criterion-level difference.

---

## 12. Pareto frontier and portfolio view

Before selecting a winner, identify leaders by dimension:

- strategic-fit leader;
- memorability leader;
- category-distinction leader;
- pronunciation/spelling leader;
- international leader;
- digital-practicality leader;
- preliminary legal-safety leader;
- architecture leader;
- bold/creative leader;
- audience-language leader.

The final choice is a trade-off, not necessarily the highest average.

### 12.1 Recommendation roles

Use:

- `PRIMARY_RECOMMENDATION` — best overall match under current priorities;
- `SAFER_ALTERNATIVE` — lower execution or clearance risk;
- `BOLDER_ALTERNATIVE` — higher distinctiveness/activation upside with explicit risk;
- `SPECIALIST_OPTION` — optimized for one priority or market;
- `NO_RECOMMENDATION` — no candidate clears the required gates.

---

## 13. Success thesis

For each finalist, the council must argue a falsifiable case:

```yaml
candidate:
strategic_role:
audience_attention_mechanism:
processing_and_recall_mechanism:
competitive_separation:
emotional_or_identity_effect:
word_of_mouth_behavior:
search_behavior:
required_descriptor:
required_verbal_activation:
required_visual_activation:
conditions_for_success:
leading_indicators:
material_risks:
falsification_tests:
confidence:
```

Bad claim:

> This name will be successful because it sounds premium.

Acceptable claim:

> For the defined enterprise buyer, the two-syllable structure and restrained technical character are expected to support confident oral use, while the unusual initial consonant separates it from the category’s dominant “smart/sense/AI” pattern. This advantage depends on consistent pronunciation in English and a descriptor that establishes the category during launch. The thesis fails if one-hearing spelling accuracy is low or the trademark search reveals a close software mark.

No name itself guarantees business success. Product quality, distribution, trust, identity execution, budget, timing, and owner commitment remain external variables.

---

## 14. Council evidence package

Before debate, the controller prepares equal-format candidate dossiers containing:

```text
CANDIDATE ID / NAME
CONSTRUCTION AND HONEST ORIGIN
TERRITORY / PHONETIC CODE FIT
STRATEGIC CASE
KNOWN RISKS
EXACT / SIMILAR MARKET RESULTS
DOMAIN RESULTS
DIGITAL ECOSYSTEM RESULTS
TRADEMARK PRE-SCREEN RESULTS
LINGUISTIC RESULTS
AUDIENCE RESULTS IF ANY
UNRESOLVED EVIDENCE
```

Do not expose another specialist’s preferred ranking during blind review.

Use [expert council protocol](expert-council.md) for the debate.

---

## 15. Final status vocabulary

Candidate lifecycle statuses:

- `RAW`;
- `CURATED`;
- `LINGUISTIC_SCREENED`;
- `DIGITAL_SCREENED`;
- `TRADEMARK_PRE_SCREENED`;
- `COUNCIL_REVIEWED`;
- `AUDIENCE_TESTED`;
- `FINALIST`;
- `RECOMMENDED_PENDING_TEST`;
- `RECOMMENDED_PENDING_CLEARANCE`;
- `RECOMMENDED_PENDING_DOMAIN`;
- `RECOMMENDED_WITH_MITIGATION`;
- `APPROVED_BY_USER_PENDING_EXTERNAL_ACTION`;
- `REJECTED`.

Never use `FINAL`, `CLEAR`, or `SAFE` when an applicable legal, domain, linguistic, or audience gate remains unresolved.

### 15.1 Project completion status

- `COMPLETE_FOR_DECISION` — all agreed research and council work finished; external legal/registration actions may still remain;
- `COMPLETE_PENDING_COUNSEL` — naming recommendation delivered but legal clearance is outstanding;
- `COMPLETE_PENDING_NATIVE_REVIEW`;
- `COMPLETE_PENDING_AUDIENCE_TEST`;
- `PARTIAL_RESEARCH`;
- `BLOCKED`;
- `NO_VIABLE_CANDIDATE`.

---

## 16. Decision log

Every final recommendation must preserve:

```yaml
decision_date:
decision_authority:
selected_candidate:
status:
primary_reason:
strongest_rival:
why_rival_lost:
validated_knockouts:
open_risks:
minority_dissent:
required_mitigation:
conditions_that_change_decision:
next_domain_action:
next_legal_action:
next_linguistic_action:
next_research_action:
launch_activation_requirements:
```

Never erase a prior decision. Append changes with reasons.

---

## 17. Registration and launch handoff

The naming skill does not purchase domains, file marks, or create public accounts without separate explicit authority.

The handoff should provide:

- preferred domain and acceptable fallbacks;
- exact domains/handles to re-check;
- candidate spellings and transliterations;
- preliminary trademark search package;
- questions for trademark counsel;
- jurisdictions and goods/services hypotheses;
- pronunciation guide;
- descriptor;
- brand-use conventions;
- capitalization and spacing;
- prohibited variants;
- monitoring targets;
- launch test plan;
- evidence expiry dates.

Re-check all volatile availability immediately before action.

---

## 18. Quality-control checklist

Before a completion claim, verify:

- [ ] Every factual availability claim has a source and date.
- [ ] Domain status is not inferred from site behavior alone.
- [ ] Exact and confusingly similar forms were searched.
- [ ] Company, brand, product, domain, app, handle, and trademark conflicts are separated.
- [ ] Relevant official trademark databases were included.
- [ ] Search limitations are explicit.
- [ ] Native-speaker validation is not fabricated.
- [ ] Audience results distinguish liking, recall, spelling, and fit.
- [ ] Hard gates were applied before scoring.
- [ ] Unknowns were not scored as average evidence.
- [ ] Council dissent and veto evidence are preserved.
- [ ] Recommendation language is probabilistic and conditional.
- [ ] Next legal/domain/linguistic actions are explicit.

---

## 19. Public source foundation

Use current official documentation rather than this list alone. As of 2026-09-03, useful authoritative starting points include:

- WIPO Global Brand Database: `https://branddb.wipo.int/`
- WIPO guidance on database coverage and national/regional searches: `https://www.wipo.int/en/web/global-brand-database`
- EUIPO TMview/eSearch: `https://www.euipo.europa.eu/en/search-ip`
- USPTO Trademark Search: `https://tmsearch.uspto.gov/`
- USPTO trademark-search guidance: `https://www.uspto.gov/trademarks/search`
- ICANN RDAP information: `https://www.icann.org/rdap`

Registry interfaces, coverage, policies, and URLs can change. Verify the current official source during every serious project.
