# Changelog

Todos los cambios relevantes de Ánima se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

## [Unreleased]

## [1.0.1] - 2026-10-27

### Fixed
- La detección de la fuente estática ahora busca en todo el workspace sin asumir un nombre de carpeta e ignora las carpetas de WordPress, plugins, dependencias y el `readme.html` de la raíz, que daban falsos candidatos.
- La pregunta por la fuente estática ahora define qué hacer cuando hay varios candidatos (listarlos para elegir) o ninguno (pedir la ruta y explicar que debe estar dentro de la carpeta abierta).
- La validación ya no acepta crear la carpeta de origen: debe existir y contener al menos un `.html`. El destino sí puede no existir todavía.

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

[Unreleased]: https://github.com/alexiscontrerasv/anima-wp/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/alexiscontrerasv/anima-wp/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/alexiscontrerasv/anima-wp/releases/tag/v1.0.0
