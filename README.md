# Naming Skill

Профессиональный skill для разработки, аудита, сравнения и выбора названий брендов, компаний, продуктов, сервисов, платформ, функций, категорий, программ, кампаний и сообществ.

Это не генератор «100 красивых слов». Skill управляет полным naming-процессом:

> бриф → стратегия → конкурентная карта → collision map → смысловые территории → фонетический код → системная генерация → языковой фильтр → домены и цифровая среда → предварительный trademark screening → независимый совет субагентов → тестирование → решение.

Версия: **0.1.0**

---

## Что решает skill

Skill предназначен для ситуаций, когда нужно:

- разработать название с нуля;
- переименовать существующий бренд или продукт;
- проверить одно понравившееся название;
- сравнить shortlist;
- создать архитектуру названий для линейки продуктов;
- найти новую смысловую территорию, если всё очевидное занято;
- провести новую генерационную волну без повторения старых корней;
- организовать независимый экспертный совет;
- подготовить решение для дальнейшей юридической и лингвистической проверки.

Skill не используется как основной инструмент для:

- заголовков и рекламного копирайтинга;
- личных имён детей;
- логотипа до выбора и основного screening названия;
- окончательного юридического clearance;
- покупки домена, подачи товарного знака или публичной регистрации без отдельного разрешения.

---

# Ключевая идея

Название не выбирается потому, что оно «красивое» или понравилось большинству участников встречи.

Сильный кандидат должен выдержать несколько независимых систем:

1. стратегическую;
2. конкурентную;
3. смысловую;
4. фонетическую;
5. языковую и культурную;
6. цифровую;
7. предварительную юридическую;
8. архитектурную;
9. пользовательскую;
10. критическую — через формальный спор экспертных субагентов.

Skill не обещает, что название гарантированно сделает бизнес успешным. Вместо этого для каждого финалиста строится проверяемая `SUCCESS_THESIS`:

- почему имя может привлечь внимание;
- как оно может запоминаться;
- чем отделяется от категории;
- какой эмоциональный или идентификационный эффект создаёт;
- какие условия активации ему нужны;
- какие факты способны опровергнуть рекомендацию.

---

# Архитектура

```text
Naming/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
│
├── references/
│   ├── naming-process.md
│   ├── generation-system.md
│   ├── phonetics-linguistics.md
│   ├── screening-evaluation.md
│   ├── expert-principles.md
│   ├── expert-council.md
│   └── sources-and-provenance.md
│
├── assets/
│   ├── naming-brief-template.md
│   ├── project-ledger-template.md
│   ├── council-dossier-template.md
│   ├── subagent-dispatch-template.md
│   └── final-report-template.md
│
├── evals/
│   └── behavior-evals.json
│
├── scripts/
│   └── validate_skill.py
│
└── .github/workflows/
    └── validate-skill.yml
```

`SKILL.md` — управляющий контракт. Подробная методология разделена на reference-файлы, чтобы модель загружала только нужный слой и не теряла критические правила в одном гигантском промпте.

---

# Режимы работы

## `INTERACTIVE`

Режим по умолчанию. Skill работает по фазам и не задаёт больше трёх существенных вопросов за один блок. После стратегически важных этапов пользователь подтверждает результат.

Пример запуска:

```text
MODE: INTERACTIVE

Нужно придумать название для нового проекта.
Работай строго по фазам.
Начни с ФАЗЫ 0 и задай три первых вопроса.
Не генерируй названия до утверждения брифа, Collision Map и фонетического кода.
```

Команда перехода:

```text
APPROVE. Переходи к следующей фазе.
```

## `ASSISTED`

Skill использует уже переданные документы и делает обратимые предположения, но спрашивает о решениях, которые materially меняют пространство поиска.

## `FULL_RUN`

Полный проход без остановки на каждом этапе. Все допущения и отсутствующие проверки фиксируются. Режим не отменяет юридические, лингвистические и доказательные ограничения.

## `NAME_AUDIT`

Глубокий анализ одного или нескольких готовых названий.

Skill сначала определяет:

- что именно нравится или не нравится;
- стратегическое соответствие;
- реальную конструкцию;
- произношение и ошибки на слух;
- языковые ассоциации;
- рыночные и цифровые коллизии;
- предварительный юридический риск;
- свойства, которые можно перенести в новые варианты.

Он не начинает с одно-буквенных мутаций исходного имени.

## `MORE`

Команда `ЕЩЁ` не означает «ещё 100 похожих слов».

Skill диагностирует причину провала:

- слабая территория;
- повторяющийся корень;
- одинаковая конструкция;
- неверный фонетический характер;
- недостаточная или чрезмерная смелость;
- доменная нехватка;
- юридическая перегретость;
- низкая запоминаемость;
- неверно понятое предпочтение пользователя.

После этого меняется генерационная система. Не менее 70% показанной новой волны должны отличаться территорией, конструкцией или фонетическим паттерном.

## `COUNCIL_ONLY`

Формальный независимый review уже готового shortlist. Новые названия не генерируются, если пользователь не попросил об этом или все кандидаты не провалили gates.

---

# Фазы

## Фаза 0. Naming brief

Определяются:

- объект нейминга;
- продукт и механизм;
- аудитория, покупатель и пользователь;
- проблема, функциональный и эмоциональный результат;
- рынки и языки;
- дифференциация;
- будущие границы бренда;
- архетип и голос;
- требования к домену;
- география предварительной trademark-проверки;
- decision authority и валидные veto.

Gate проходит, когда два компетентных namer-а поняли бы одну и ту же задачу.

## Фаза 1. Стратегическое ядро

Фиксируются:

- задачи имени;
- `CATEGORY_ENEMY`;
- `PARADIGM_SHIFT`;
- что обязано нести имя;
- что должен объяснять descriptor;
- `MUST_HAVE`, `PREFER`, `MUST_NOT_HAVE`;
- naming approach;
- тип конструкции;
- архитектура линейки.

## Фаза 2. Competitive Naming Map и Collision Map

Исследуются:

- прямые и смежные конкуренты;
- типы имён;
- корни, суффиксы, ритмы;
- метафоры;
- одинаковые обещания;
- broker-heavy доменные конструкции;
- зоны правового риска;
- свободное смысловое и звуковое пространство.

Формируются:

```text
SATURATED_ROOTS
SATURATED_SUFFIXES
SATURATED_PATTERNS
SATURATED_METAPHORS
SATURATED_PROMISES
WHITE_SPACE
NO_GO_REGISTER
```

## Фаза 3. Смысловые территории и фонетический код

Строятся 6–10 принципиально разных территорий:

- механизм;
- результат;
- эмоциональный эффект;
- конфликт/враг;
- авторская история или терминология;
- удалённая category-escape территория.

Формируется `PHONETIC_CODE`:

- длина;
- количество слогов;
- ритм;
- ударение;
- гласные и согласные;
- мягкость/твёрдость;
- начало и окончание;
- mouthfeel;
- чтение на целевых языках;
- допустимая неправильность;
- likely wrong-hearing tree.

## Фаза 4. Архитектура генерации

Выбираются:

- основные методы;
- вторичные методы;
- экспериментальные методы;
- meta-ideation methods;
- creative intensity;
- требования к разнообразию;
- критерии остановки.

## Фаза 5. Генерационные волны

Используются 36 конструкционных методов:

- 18 классических;
- 18 современных.

Дополнительно используются meta-ideation methods:

- Three Chests;
- Morphological Box;
- Synectics;
- Focal Objects;
- SCAMPER;
- Six Thinking Hats;
- TRIZ;
- Walt Disney;
- Reverse Brainstorming;
- Robinson.

Все методы описаны в `references/generation-system.md`.

## Фаза 6. Фонетический и языковой screening

Проверяются:

- first-sight pronunciation;
- one-hearing repetition;
- spelling from hearing;
- telephone use;
- email/search behavior;
- voice input;
- ритм и mouthfeel;
- языковые значения;
- сленг и табу;
- медицинские, политические и культурные ассоциации;
- транслитерация;
- морфология;
- фонетические соседи;
- anti-confusion.

## Фаза 7. Digital и preliminary trademark screening

Раздельно проверяются:

- действующие бренды;
- компании;
- продукты;
- приложения;
- open-source проекты и пакеты;
- домены;
- социальные аккаунты;
- товарные знаки.

Домены получают точные статусы: доступен к регистрации, premium registry, active, redirect, parked, brokered, inactive, restricted, lifecycle/unknown.

Trademark screening использует официальные базы релевантных юрисдикций, но не выдаётся за юридическое заключение.

## Фаза 8. Совет субагентов

Это не театральная игра ролей. Совет разделён на две независимые палаты.

### Функциональная палата

- Naming Strategy Lead;
- Competitive Naming Cartographer;
- Creative Naming Director;
- Phonetic & Sound-Symbolism Linguist;
- Verbal Identity & Memorability Critic;
- Cross-Cultural Linguist;
- Digital Availability Researcher;
- Trademark Pre-Screener;
- Brand Architecture Strategist;
- Audience Language Advocate;
- Skeptical Red Team;
- Evidence Auditor.

### Палата профессиональных методологий

Отдельные субагенты применяют только публично описанные принципы:

- Lexicon / David Placek Sound-and-Cognition Lens;
- Rob Meyerson Process-and-Brief Lens;
- Alexandra Watkins SMILE-and-SCRATCH Lens;
- Igor Distinctiveness-and-Engagement Lens;
- Eli Altman Systematic-Creativity Lens;
- Catchword Global-Naming-and-Linguistics Lens.

Они не изображают реальных людей, не говорят от их имени и не заявляют об их участии.

### Совет проходит восемь раундов

1. preflight;
2. blind independent reviews;
3. disagreement map;
4. advocacy assignment;
5. cross-examination;
6. evidence resolution;
7. red-team attack;
8. final votes and controller adjudication.

Каждый сильный кандидат получает адвоката. Адвокат обязан доказать:

- почему имя может привлечь внимание;
- почему его запомнят;
- чем оно отделено от конкурентов;
- как оно работает для аудитории;
- какая активация нужна;
- при каких условиях тезис провалится.

Ни простое большинство, ни средний балл не могут отменить валидный knockout.

## Фаза 9. Тестирование на аудитории

Измеряются отдельно:

- liking;
- pronunciation;
- spelling;
- immediate recall;
- delayed recall;
- category expectation;
- trust;
- distinctiveness;
- word-of-mouth use;
- negative associations;
- polarization;
- descriptor dependence.

Не задаётся только вопрос «какое название нравится?».

## Фаза 10. Решение

Skill выдаёт:

- screened shortlist;
- 3–5 finalist dossiers;
- primary recommendation;
- safer alternative;
- bolder alternative;
- Pareto leaders;
- council votes;
- сильнейшее несогласие;
- доменную стратегию;
- preliminary trademark risk;
- descriptor;
- success thesis;
- failure conditions;
- обязательные следующие проверки;
- decision log и `NO_GO_REGISTER`.

---

# 36 методов построения названий

## 18 классических

1. Словообразование.
2. Ассоциации.
3. Комбинирование слов.
4. Заимствование из других языков.
5. Абстрактные названия.
6. Неологизмы.
7. Литература, легенды, мифы и персонажи.
8. Повторение слов или слогов.
9. Рифма и созвучие.
10. Метафора.
11. Юмор.
12. Фраза о процессе или результате.
13. Противопоставление.
14. Транслитерация.
15. Превосходство.
16. Аллитерация.
17. Звукоподражание.
18. Провокационные и суперкреативные конструкции.

## 18 современных

19. Category escape.
20. Semantic compression.
21. Proprietary fragment.
22. Distant-domain collision.
23. Phonetic-first synthesis.
24. Deep morpheme mutation.
25. Phrase compression.
26. Verbable naming.
27. Ritual/action naming.
28. Contrarian naming.
29. Enemy-based naming.
30. Founder/heritage code.
31. Visual-letter naming.
32. Domain-led construction.
33. Bilingual resonance.
34. Hidden double meaning.
35. Controlled irregularity.
36. User-language extraction.

Эти методы не получают одинаковый вес автоматически. Для каждого проекта они распределяются на `PRIMARY`, `SECONDARY` и `EXPERIMENTAL`.

---

# Долговременные объекты проекта

```text
NAMING_BRIEF
DECISION_AUTHORITY
STRATEGIC_CORE
CATEGORY_ENEMY
PARADIGM_SHIFT
NAMING_ARCHITECTURE
CREATIVE_INTENSITY
COMPETITIVE_NAMING_MAP
COLLISION_MAP
SATURATED_ROOTS
SATURATED_SUFFIXES
SATURATED_PATTERNS
SATURATED_METAPHORS
SATURATED_PROMISES
WHITE_SPACE
NO_GO_REGISTER
SEMANTIC_TERRITORIES
CUSTOMER_LANGUAGE_BANK
PROPRIETARY_WORD_BANK
CULTURAL_CODE_MAP
PHONETIC_CODE
GENERATION_PLAN
CANDIDATE_LEDGER
SCREENING_LEDGER
COUNCIL_RECORD
AUDIENCE_TEST_PLAN
FINALIST_DOSSIERS
DECISION_LOG
```

Это защищает длинную работу от потери отклонённых вариантов, повторения старых корней, смешения фактов и предположений и изменения критериев задним числом.

---

# Команды

## Начать интерактивный процесс

```text
MODE: INTERACTIVE
Начинаем разработку названия для [проект].
Следуй developing-brand-names строго по фазам.
Начни с ФАЗЫ 0.
```

## Полный проход

```text
MODE: FULL_RUN
Разработай название для [проект] на основе приложенного материала.
Все допущения помечай. Непроверенные домены и товарные знаки не называй свободными.
Проведи maximum-quality council.
```

## Проверить готовое имя

```text
MODE: NAME_AUDIT
Проведи полный аудит названия [имя].
Сначала объясни, что именно в нём работает или не работает.
Не создавай мутации до завершения аудита.
```

## Провести совет

```text
MODE: COUNCIL_ONLY
Проведи независимый maximum-quality council для shortlist: [...].
Используй функциональную и методологическую палаты, blind review, cross-examination и red team.
```

## Новая волна

```text
ЕЩЁ.
Сначала диагностируй, почему предыдущая волна не сработала.
Обнови NO_GO_REGISTER и измени территории, конструкции или PHONETIC_CODE.
```

---

# Доказательная дисциплина

Каждая материальная проверка получает статус:

```text
VERIFIED_PRIMARY
VERIFIED_SECONDARY
CORROBORATED
OBSERVED
MODEL_HYPOTHESIS
USER_REPORTED
UNKNOWN
```

Skill запрещает:

- выдуманную этимологию;
- неподтверждённую доступность домена;
- вывод о домене по отсутствию сайта;
- смешение домена, бренда, юрлица, приложения и товарного знака;
- притворную native-speaker validation;
- утверждение «юридически свободно»;
- имитацию мнения реального naming-эксперта;
- выбор по одному среднему баллу;
- повторение отклонённых имён;
- одно-буквенные мутации понравившегося бренда;
- переход к логотипу до прохождения naming gates.

---

# Тестирование и валидация пакета

Локальная проверка:

```bash
python scripts/validate_skill.py
```

Validator проверяет:

- наличие обязательных файлов;
- frontmatter `SKILL.md`;
- локальные Markdown-ссылки;
- JSON evals;
- обязательные методологические термины;
- наличие legal/domain/native-speaker disclaimers;
- наличие совета, blind review, cross-examination, red team и success thesis;
- отсутствие пустых reference/assets файлов.

GitHub Actions запускает эту проверку при push и pull request.

---

# Ограничения

- Naming не является математически предсказуемой задачей.
- Совет субагентов снижает коррелированные ошибки, но не заменяет реальных клиентов, носителей языка и юриста.
- Preliminary trademark screening не является legal clearance.
- Доменная и социальная доступность изменяется.
- Публичные профессиональные методологии используются как аналитические линзы, а не как симуляция людей.
- Хорошее название не исправляет слабый продукт, отсутствие дистрибуции или плохую brand activation.

---

# Источники и методологическая честность

Подробное разделение пользовательских материалов, публичных профессиональных принципов, официальных screening-источников и авторских адаптаций находится в:

- `references/sources-and-provenance.md`;
- `references/expert-principles.md`.
