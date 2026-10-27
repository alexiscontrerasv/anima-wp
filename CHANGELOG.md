# Changelog

Todos los cambios relevantes de Ánima se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

## [Unreleased]

## [1.0.0] - 2026-10-27

Primera versión pública.

### Added
- Skill `anima` en formato Agent Skills, invocable con `/anima` en Cursor.
- Fase 0 de configuración con detección automática del entorno (fuente estática, themes, plugins, WP-CLI y URL local) y preguntas en un solo mensaje con valores propuestos.
- Derivación automática del prefijo de funciones, el text domain y el prefijo de keys a partir del slug.
- Soporte para Secure Custom Fields y ACF PRO, y para Yoast SEO, Rank Math u otro plugin SEO.
- Flujo de 8 fases (configuración, inventario, base, Opciones generales, field groups, templates, CPT y QA) con STOP obligatorio para aprobar el inventario.
- Modos de avance `continuo` y `fase a fase`.
- Archivos de estado en `_anima/` (`config.md`, `INVENTORY.md`, `PROGRESS.md`) para retomar en cualquier chat.
- Subcomandos `/anima estado` y `/anima nuevo`.
- Aviso al retomar un proyecto creado con otra versión MAJOR de Ánima.
- Reglas de modelado de campos, salida segura, estructura del theme, menús y uso seguro de WP-CLI (solo entorno local).
- Inventario con detección de formularios, enlaces internos a `.html` y plantillas donde no se usa el editor.
- QA con `php -l`, PHPCS, búsqueda de contenido hardcodeado y de salidas sin escapar.

[Unreleased]: https://github.com/alexiscontrerasv/anima-wp/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/alexiscontrerasv/anima-wp/releases/tag/v1.0.0
