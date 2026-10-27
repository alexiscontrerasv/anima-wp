#!/usr/bin/env python3
"""Valida los skills del repositorio según la especificación Agent Skills.

Comprueba, para cada skills/<carpeta>/SKILL.md:
  - frontmatter YAML válido con `name` y `description`;
  - `name` en minúsculas/números/guiones, máx. 64 caracteres e igual al nombre de la carpeta;
  - `description` no vacía y de máx. 1024 caracteres;
  - `compatibility` de máx. 500 caracteres (si existe);
  - `metadata.version` en formato SemVer;
  - la versión del encabezado del cuerpo igual a `metadata.version`;
  - una sección `## [X.Y.Z]` para esa versión en CHANGELOG.md;
  - bloques de código balanceados y un máximo recomendado de 500 líneas.

Uso:
  python3 .github/scripts/validate_skill.py           # valida todo
  python3 .github/scripts/validate_skill.py --tag v1.2.3   # además exige que el tag coincida
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
CHANGELOG = ROOT / "CHANGELOG.md"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
HEADER_VERSION_RE = re.compile(r"^> \*\*.+? v(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\*\*", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
MAX_LINES = 500


def validate_skill(skill_md: Path, changelog: str, tag: str | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    rel = skill_md.relative_to(ROOT)
    text = skill_md.read_text(encoding="utf-8")

    match = FRONTMATTER_RE.match(text)
    if not match:
        return [f"{rel}: falta el frontmatter YAML al inicio del archivo"], warnings

    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return [f"{rel}: frontmatter YAML inválido: {exc}"], warnings

    name = meta.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{rel}: `name` debe usar minúsculas, números y guiones (máx. 64)")
    elif name != skill_md.parent.name:
        errors.append(f"{rel}: `name` ({name}) debe coincidir con la carpeta ({skill_md.parent.name})")

    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{rel}: `description` es obligatoria")
    elif len(description) > 1024:
        errors.append(f"{rel}: `description` supera 1024 caracteres ({len(description)})")

    compatibility = meta.get("compatibility")
    if compatibility is not None and (not isinstance(compatibility, str) or len(compatibility) > 500):
        errors.append(f"{rel}: `compatibility` debe ser texto de máx. 500 caracteres")

    metadata = meta.get("metadata") or {}
    version = str(metadata.get("version", ""))
    if not SEMVER_RE.match(version):
        errors.append(f"{rel}: `metadata.version` debe ser SemVer (ej. 1.0.0), encontrado: '{version}'")
    else:
        header = HEADER_VERSION_RE.search(text[match.end():])
        if not header:
            errors.append(f"{rel}: no se encontró la versión en el encabezado del cuerpo")
        elif header.group(1) != version:
            errors.append(f"{rel}: versión del encabezado ({header.group(1)}) distinta a metadata ({version})")

        if not re.search(rf"^## \[{re.escape(version)}\]", changelog, re.MULTILINE):
            errors.append(f"CHANGELOG.md: falta la sección `## [{version}]`")

        if tag is not None and tag.lstrip("v") != version:
            errors.append(f"{rel}: el tag {tag} no coincide con metadata.version ({version})")

    if text.count("```") % 2 != 0:
        errors.append(f"{rel}: hay un bloque de código ``` sin cerrar")

    lines = text.count("\n") + 1
    if lines > MAX_LINES:
        warnings.append(f"{rel}: {lines} líneas (se recomienda máx. {MAX_LINES})")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", help="tag de release a comparar con metadata.version (ej. v1.0.0)")
    args = parser.parse_args()

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("ERROR: no se encontraron skills en skills/<nombre>/SKILL.md")
        return 1

    changelog = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else ""
    if not changelog:
        print("ERROR: falta CHANGELOG.md")
        return 1

    all_errors: list[str] = []
    for skill_md in skill_files:
        errors, warnings = validate_skill(skill_md, changelog, args.tag)
        all_errors.extend(errors)
        for warning in warnings:
            print(f"AVISO: {warning}")
        if not errors:
            print(f"OK: {skill_md.relative_to(ROOT)}")

    for error in all_errors:
        print(f"ERROR: {error}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
