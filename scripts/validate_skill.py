#!/usr/bin/env python3
"""Validate only this package's allowlisted source files; never inventory a host."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FILES = (
    "SKILL.md", "agents/openai.yaml", "README.md", "LICENSE", "NOTICE", ".gitignore",
    "references/installed-app-discovery.md", "references/local-reauth.md",
    "references/app-signout.md", "references/browsers.md",
    "references/credentials-and-data.md", "references/verification.md",
    "references/sources.md", "docs/validation.md", "scripts/validate_skill.py",
)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    content: dict[str, str] = {}
    for name in FILES:
        path = root / name
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"{name}: symlink or path outside package")
            continue
        if not path.is_file():
            errors.append(f"{name}: missing")
            continue
        try:
            content[name] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{name}: cannot read UTF-8 source")

    entry = content.get("SKILL.md", "")
    front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", entry, re.S)
    if not front:
        errors.append("SKILL.md: missing frontmatter")
    else:
        fields = front.group(1)
        if not re.search(r"^name: offboarding-cleanup$", fields, re.M):
            errors.append("SKILL.md: wrong name")
        if not re.search(r'^description: "[^\n]+"$', fields, re.M):
            errors.append("SKILL.md: missing single-line quoted description")
        if not re.search(r'^license: "AGPL-3\.0-only"$', fields, re.M):
            errors.append("SKILL.md: license mismatch")
        if not re.search(r'^  version: "\d+\.\d+\.\d+"$', fields, re.M):
            errors.append("SKILL.md: invalid version")

    ui = content.get("agents/openai.yaml", "")
    brief = re.search(r'^  short_description: "([^\n]+)"$', ui, re.M)
    prompt = re.search(r'^  default_prompt: "([^\n]+)"$', ui, re.M)
    if not brief or not 25 <= len(brief.group(1)) <= 64:
        errors.append("agents/openai.yaml: short_description must be 25-64 characters")
    if not prompt or "$offboarding-cleanup" not in prompt.group(1):
        errors.append("agents/openai.yaml: default_prompt must invoke this skill")

    for name, text in content.items():
        if name.endswith(".md"):
            if "[TODO:" in text:
                errors.append(f"{name}: unfinished scaffold")
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if link.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                target = ((root / name).parent / link.split("#", 1)[0]).resolve()
                if not target.is_relative_to(root) or not target.is_file():
                    errors.append(f"{name}: missing or nonportable local link")
        if name.endswith((".md", ".yaml")):
            # Report only the category, never matching content.
            rules = {
                "personal Windows home path": r"(?i)[A-Z]:[\\/]Users[\\/](?!<)[^\\/\s]+",
                "private key block": r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----",
                "GitHub token": r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b",
                "JWT-shaped credential": r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}\b",
            }
            for kind, pattern in rules.items():
                if re.search(pattern, text):
                    errors.append(f"{name}: potential {kind}")

    if "GNU AFFERO GENERAL PUBLIC LICENSE" not in content.get("LICENSE", ""):
        errors.append("LICENSE: AGPL text missing")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {len(FILES)} package source files, metadata, local links and publication checks.")
    print("No installed applications, browser data, credentials or chat data were inspected.")
    print("This structural check does not prove cleanup behavior or absence of every possible secret.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
