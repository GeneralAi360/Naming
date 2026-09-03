#!/usr/bin/env python3
"""Validate the portable Naming skill package.

The validator intentionally uses only Python's standard library so it can run in
minimal CI environments. It checks package structure, SKILL frontmatter,
relative Markdown links, behavioral eval JSON, version consistency, and a set
of critical methodological contracts.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "references/naming-process.md",
    "references/generation-system.md",
    "references/phonetics-linguistics.md",
    "references/screening-evaluation.md",
    "references/expert-principles.md",
    "references/expert-council.md",
    "references/sources-and-provenance.md",
    "assets/naming-brief-template.md",
    "assets/project-ledger-template.md",
    "assets/council-dossier-template.md",
    "assets/subagent-dispatch-template.md",
    "assets/final-report-template.md",
    "evals/behavior-evals.json",
]

CRITICAL_SKILL_TERMS = [
    "Strategy before words",
    "NO_GO_REGISTER",
    "PHONETIC_CODE",
    "SUCCESS_THESIS",
    "INLINE_COUNCIL",
    "blind",
    "cross-examination",
    "Red Team",
    "preliminary trademark",
    "No invented facts",
    "No forced volume",
    "No premature logo work",
]

CRITICAL_COUNCIL_TERMS = [
    "NAMING_STRATEGY_LEAD",
    "CREATIVE_NAMING_DIRECTOR",
    "PHONETIC_AND_SOUND_SYMBOLISM_LINGUIST",
    "DIGITAL_AVAILABILITY_RESEARCHER",
    "TRADEMARK_PRE_SCREENER",
    "SKEPTICAL_RED_TEAM",
    "EVIDENCE_AUDITOR",
    "LEXICON_PLACEK_LENS",
    "MEYERSON_PROCESS_BRIEF_LENS",
    "WATKINS_SMILE_SCRATCH_LENS",
    "IGOR_DISTINCTIVENESS_LENS",
    "ALTMAN_SYSTEMATIC_CREATIVITY_LENS",
    "CATCHWORD_GLOBAL_LENS",
    "No simple majority",
]

CRITICAL_SCREENING_TERMS = [
    "AVAILABLE_TO_REGISTER",
    "BROKERED_FOR_SALE",
    "REGISTERED_ACTIVE",
    "UNKNOWN_PRELIMINARY_RISK",
    "not legal clearance",
    "RDAP",
    "WIPO",
    "EUIPO",
    "USPTO",
    "UNKNOWN",
]

CLASSIC_METHOD_HEADINGS = [
    "Word formation",
    "Associations",
    "Combining words",
    "Borrowing from other languages",
    "Abstract names",
    "Neologism",
    "Literature, legends, myths, and characters",
    "Repetition of words or syllables",
    "Rhyme and consonance",
    "Metaphor",
    "Humor",
    "Phrase describing use or result",
    "Contrast",
    "Transliteration",
    "Superiority",
    "Alliteration",
    "Onomatopoeia",
    "Supercreative / provocative construction",
]

ADVANCED_TERMS = [
    "Category escape",
    "Semantic compression",
    "Proprietary fragment",
    "Distant-domain collision",
    "Phonetic-first synthesis",
    "Deep morpheme mutation",
    "Phrase compression",
    "Verbable naming",
    "Ritual/action naming",
    "Contrarian naming",
    "Enemy-based naming",
    "Founder/heritage code",
    "Visual-letter naming",
    "Domain-led construction",
    "Bilingual resonance",
    "Hidden double meaning",
    "Controlled irregularity",
    "User-language extraction",
]

META_IDEATION_TERMS = [
    "Three Chests",
    "Morphological Box",
    "Synectics",
    "Focal Objects",
    "SCAMPER",
    "Six Thinking Hats",
    "TRIZ",
    "Walt Disney",
    "Reverse Brainstorming",
    "Robinson",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


@dataclass
class Issue:
    level: str
    message: str


def read_text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    block = text[4:end]
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z0-9_-]+:\s*", line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip()
            data[current_key] = "" if value in {">", "|-", "|"} else value
        elif current_key and line.startswith("  "):
            data[current_key] = (data[current_key] + " " + line.strip()).strip()
        else:
            raise ValueError(f"Unsupported frontmatter line: {line!r}")
    return data


def check_required_files(issues: list[Issue]) -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            issues.append(Issue("ERROR", f"Missing required file: {relative}"))
        elif path.is_file() and path.stat().st_size == 0:
            issues.append(Issue("ERROR", f"Required file is empty: {relative}"))


def check_frontmatter(issues: list[Issue]) -> str | None:
    try:
        data = parse_frontmatter(read_text("SKILL.md"))
    except (OSError, ValueError) as exc:
        issues.append(Issue("ERROR", str(exc)))
        return None

    name = data.get("name", "")
    description = data.get("description", "")
    version = data.get("version", "")

    if name != "developing-brand-names":
        issues.append(Issue("ERROR", f"Unexpected skill name: {name!r}"))
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        issues.append(Issue("ERROR", "Skill name must be lowercase kebab-case"))
    if len(description) < 120:
        issues.append(Issue("ERROR", "Skill description is too short to route reliably"))
    if len(description) > 1024:
        issues.append(Issue("ERROR", "Skill description exceeds 1024 characters"))
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        issues.append(Issue("ERROR", f"Version is not semantic: {version!r}"))
    return version or None


def iter_markdown_files() -> Iterable[Path]:
    yield from sorted(ROOT.rglob("*.md"))


def check_markdown_links(issues: list[Issue]) -> None:
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_without_anchor = target.split("#", 1)[0]
            if not target_without_anchor:
                continue
            resolved = (path.parent / target_without_anchor).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                issues.append(Issue("ERROR", f"Link escapes package in {path.relative_to(ROOT)}: {target}"))
                continue
            if not resolved.exists():
                issues.append(Issue("ERROR", f"Broken relative link in {path.relative_to(ROOT)}: {target}"))


def require_terms(relative: str, terms: list[str], issues: list[Issue]) -> None:
    try:
        text = read_text(relative).casefold()
    except OSError as exc:
        issues.append(Issue("ERROR", f"Cannot read {relative}: {exc}"))
        return
    for term in terms:
        if term.casefold() not in text:
            issues.append(Issue("ERROR", f"Missing critical contract in {relative}: {term}"))


def check_generation_system(issues: list[Issue]) -> None:
    require_terms("references/generation-system.md", CLASSIC_METHOD_HEADINGS, issues)
    require_terms("references/generation-system.md", ADVANCED_TERMS, issues)
    require_terms("references/generation-system.md", META_IDEATION_TERMS, issues)


def check_evals(version: str | None, issues: list[Issue]) -> None:
    path = ROOT / "evals/behavior-evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(Issue("ERROR", f"Invalid behavior-evals.json: {exc}"))
        return

    if data.get("skill") != "developing-brand-names":
        issues.append(Issue("ERROR", "Eval skill name does not match SKILL.md"))
    if version and data.get("version") != version:
        issues.append(Issue("ERROR", "Eval version does not match SKILL.md"))

    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 25:
        issues.append(Issue("ERROR", "At least 25 behavioral eval cases are required"))
        return

    ids: set[str] = set()
    required_keys = {"id", "category", "prompt", "expected_behavior", "assertions", "forbidden"}
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            issues.append(Issue("ERROR", f"Eval case {index} is not an object"))
            continue
        missing = required_keys - case.keys()
        if missing:
            issues.append(Issue("ERROR", f"Eval case {index} missing keys: {sorted(missing)}"))
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            issues.append(Issue("ERROR", f"Eval case {index} has invalid id"))
        elif case_id in ids:
            issues.append(Issue("ERROR", f"Duplicate eval id: {case_id}"))
        else:
            ids.add(case_id)
        if not isinstance(case.get("assertions"), list) or not case.get("assertions"):
            issues.append(Issue("ERROR", f"Eval {case_id!r} has no assertions"))
        if not isinstance(case.get("forbidden"), list):
            issues.append(Issue("ERROR", f"Eval {case_id!r} forbidden must be a list"))

    required_eval_ids = {
        "brief-before-generation",
        "liked-name-no-mutations",
        "more-diagnosis",
        "domain-site-absence",
        "trademark-not-legal-clearance",
        "native-speaker-honesty",
        "council-two-chambers",
        "council-argues-success",
        "council-cross-examination",
        "validated-knockout-over-majority",
        "inline-council-honesty",
        "no-false-precision",
        "no-forced-winner",
        "logo-after-gate",
    }
    missing_ids = required_eval_ids - ids
    if missing_ids:
        issues.append(Issue("ERROR", f"Missing required behavioral evals: {sorted(missing_ids)}"))


def check_version_consistency(version: str | None, issues: list[Issue]) -> None:
    if not version:
        return
    readme = read_text("README.md")
    changelog = read_text("CHANGELOG.md")
    if version not in readme:
        issues.append(Issue("ERROR", "README does not mention current version"))
    if f"[{version}]" not in changelog:
        issues.append(Issue("ERROR", "CHANGELOG does not contain current version heading"))


def check_text_hygiene(issues: list[Issue]) -> None:
    for path in list(iter_markdown_files()) + [ROOT / "scripts/validate_skill.py"]:
        text = path.read_text(encoding="utf-8")
        if "\r\n" in text:
            issues.append(Issue("WARNING", f"CRLF line endings: {path.relative_to(ROOT)}"))
        trailing = [i for i, line in enumerate(text.splitlines(), 1) if line.rstrip() != line]
        if trailing:
            preview = ", ".join(map(str, trailing[:5]))
            issues.append(Issue("WARNING", f"Trailing whitespace in {path.relative_to(ROOT)} lines {preview}"))


def main() -> int:
    issues: list[Issue] = []
    check_required_files(issues)
    version = check_frontmatter(issues)
    check_markdown_links(issues)
    require_terms("SKILL.md", CRITICAL_SKILL_TERMS, issues)
    require_terms("references/expert-council.md", CRITICAL_COUNCIL_TERMS, issues)
    require_terms("references/screening-evaluation.md", CRITICAL_SCREENING_TERMS, issues)
    check_generation_system(issues)
    check_evals(version, issues)
    check_version_consistency(version, issues)
    check_text_hygiene(issues)

    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARNING"]

    for issue in issues:
        print(f"[{issue.level}] {issue.message}")

    if errors:
        print(f"\nVALIDATION FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"VALIDATION PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
