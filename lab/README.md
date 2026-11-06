# Laboratorio de trading (simulado)

Laboratorio de práctica para analizar, decidir, simular y revisar operaciones **sin dinero real** y sin enviar órdenes.
No es asesoramiento financiero ni demuestra que ninguna estrategia tenga ventaja.

## Cómo está organizado
- `INICIO_DE_SESION.md` : qué se le pide a Claude cada día.
- `reglas/` : reglamento y criterios con versión. No se cambian a la ligera.
- `plantillas/` : un formato por departamento.
- `registros/` : un directorio por caso. Se cierran con commit ANTES de conocer el desenlace.
- `resultados/` : desenlaces, añadidos DESPUÉS de cerrar la decisión.
- `aprendizaje/` : hipótesis del departamento de revisión (no son reglas).
- `libro_operaciones.csv` : libro de operaciones simuladas.
- `herramientas/sellar.py` : calcula el hash SHA-256 de un archivo.

## Los cuatro departamentos
1. **Análisis**: calcula y describe con los datos hasta el corte. No decide.
2. **Evaluación**: aplica las reglas fijas y decide COMPRAR o ESPERAR.
3. **Entradas y salidas (simulado)**: registra la operación hipotética con costes declarados.
4. **Revisión**: lee solo registros cerrados y propone hipótesis.

Estado: v0.1 (borrador). Caso 001 = caso de aprendizaje con contaminación reconocida.
