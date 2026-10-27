# Política de seguridad

## Versiones soportadas

Solo la última versión publicada en [Releases](https://github.com/alexiscontrerasv/anima-wp/releases) recibe correcciones.

## Qué reportar

Ánima son instrucciones que un agente de IA ejecuta con sus propios permisos. Reporta cualquier instrucción del skill que pueda llevar al agente a:

- ejecutar comandos destructivos o modificar archivos fuera del theme;
- leer, mostrar o commitear credenciales (`wp-config.php`, `.env`, tokens);
- operar contra un entorno que no sea local (staging o producción);
- generar código PHP inseguro (salidas sin escapar, inyecciones, etc.).

## Cómo reportar

Usa **[Report a vulnerability](https://github.com/alexiscontrerasv/anima-wp/security/advisories/new)** en la pestaña *Security* del repositorio. Es un canal privado.

No abras un issue público para problemas de seguridad. Incluye la versión de Ánima, la herramienta y el modelo que usaste, y los pasos para reproducirlo.
