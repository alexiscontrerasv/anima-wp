# Contribuir a Ánima

Gracias por tu interés en mejorar Ánima. Esta guía explica cómo proponer cambios.

## Antes de empezar

- Para cambios grandes (una fase nueva, cambios en `_anima/` o en las reglas de modelado), **abre primero un issue** para conversarlo.
- Para correcciones de redacción o errores puntuales, puedes ir directo al PR.

## Probar cambios localmente

Enlaza tu copia del repositorio a la carpeta de skills de Cursor, así cada cambio se refleja sin copiar archivos:

```bash
# macOS / Linux
ln -s "$(pwd)/skills/anima" ~/.cursor/skills/anima
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Junction -Path "$HOME\.cursor\skills\anima" -Target "$PWD\skills\anima"
```

Prueba el flujo completo con un sitio estático pequeño en un WordPress local, al menos hasta el STOP del inventario.

## Reglas para editar `SKILL.md`

- Mantén `SKILL.md` en español, claro y por debajo de 500 líneas.
- **No agregues instrucciones que asuman comportamientos no verificados** de WordPress, SCF/ACF, WP-CLI o Cursor. Si algo depende de la versión, el skill debe verificarlo o registrarlo como `DUDA:`.
- No agregues reglas ligadas a un proyecto, cliente o empresa en particular.
- Mantén el crédito de autoría y la licencia.

## Versionado

Ánima sigue [Versionado Semántico](https://semver.org/lang/es/):

| Tipo | Cuándo |
|---|---|
| **MAJOR** | Cambios incompatibles: formato de los archivos de `_anima/`, orden o significado de las fases, reglas que cambian el código generado en proyectos ya iniciados |
| **MINOR** | Capacidades nuevas compatibles: nuevas preguntas opcionales, nuevos chequeos de QA, nuevos subcomandos |
| **PATCH** | Correcciones de redacción, ejemplos o errores sin cambio de comportamiento |

## Checklist del PR

1. Describe el cambio en `CHANGELOG.md`, dentro de `## [Unreleased]`.
2. Ejecuta el validador:
   ```bash
   pip install pyyaml
   python3 .github/scripts/validate_skill.py
   ```
3. Si el cambio afecta la instalación o el uso, actualiza `README.md`.

## Publicar una versión (mantenedor)

1. Mueve las entradas de `[Unreleased]` a una nueva sección `## [X.Y.Z] - AAAA-MM-DD` y actualiza los enlaces al final de `CHANGELOG.md`.
2. Actualiza `metadata.version` en el frontmatter y la versión del encabezado de `SKILL.md`.
3. Haz commit, crea el tag y súbelo:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```
4. El workflow `release.yml` valida el skill, genera `anima-vX.Y.Z.zip` y publica el release con las notas del changelog.
