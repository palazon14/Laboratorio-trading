# Reglamento v0.1 (borrador)

## 1. Principios
1. Todo es simulado. No se envían órdenes ni se usa dinero real.
2. Un caso no demuestra nada. Ninguna conclusión de ventaja se saca con pocos casos.
3. Los datos y las reglas se compartan entre departamentos; **las respuestas y el desenlace no**.
4. Las reglas se fijan ANTES de ver el caso. No se modifican para "arreglar" un resultado.

## 2. Departamentos y qué pueden ver
| Departamento | Entra | Sale | No puede ver |
|---|---|---|---|
| Análisis | Datos hasta el corte | `01_analisis.md` | Desenlace |
| Evaluación | `01_analisis.md` y reglas | `02_evaluacion.md` (COMPRAR/ESPERAR) | Desenlace |
| Entradas y salidas (simulado) | `02_evaluacion.md` | `03_ejecucion.md` + fila en el libro | Desenlace antes de cerrar la entrada |
| Revisión | Registros cerrados + resultados | `aprendizaje/` | Nada que contradiga el sellado |

## 3. Sellado
- Cada informe se sube al repositorio (commit) antes de pasar al siguiente departamento.
- La fecha del commit es el sellado. Opcionalmente se anota el SHA-256 del archivo (`herramientas/sellar.py`).
- Un registro cerrado no se edita. Las correcciones se añaden en un archivo nuevo, citando el anterior.

## 4. Independencia
- Se declara en cada caso si los departamentos compartieron contexto o conocían el desenlace.
- Mientras todos los departamentos los ejecute el mismo asistente en la misma conversación, la independencia es parcial y debe declararse.
- Un caso retrospectivo (con desenlace ya existente) se marca `retrospectivo: true` y no cuenta como prueba prospectiva.

## 5. Costes y ejecución simulada (a rellenar ANTES de usarlos)
- Precio de entrada: apertura de la vela siguiente al corte (dato del archivo), nunca un precio inventado.
- Comisión: pendiente de fijar.
- Deslizamiento: pendiente de fijar.
- Tamaño de posición y riesgo máximo por operación: pendiente de fijar.

## 6. Cuándo se pueden cambiar las reglas
- No antes de reunir un número mínimo de casos cerrados (propuesta inicial: **30**, a confirmar).
- Todo cambio crea una versión nueva (`REGLAMENTO_v0.2.md`) con la razón escrita. Las versiones anteriores se conservan.

## 7. Limitaciones permanentes
- Muestras pequeñas, un valor y una ventana concreta.
- Sin datos de noticias salvo que se adjunten.
- Sin demostración de capacidad predictiva.
