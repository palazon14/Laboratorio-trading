# Caso 001 AAPL 2026-10-01 10:00 ET (APRENDIZAJE, retrospectivo)

- case_id: AAPL_2026-10-01_1000ET_APRENDIZAJE
- input_hash: 45eb685ddd04d781b77bee5c41b0c29cb2c9b713b25088e710848093c7381178
- Corte: 2026-10-01T14:00:00Z (10:00 ET). Datos: 30 velas de 1 min de AAPL, SPY y QQQ.

## Resultado de la auditoría (cálculos verificados contra el JSON)
- Máximo inicial 332,4816 (09:38) y mínimo 328,37 (09:32). Rango 4,1116.
- Último cierre de 5 min (09:55-09:59): 330,41 < 332,4816, no hay ruptura. El bloque anterior cierra en 330,919, tampoco.
- Ningún cierre de 1 min desde las 09:45 supera 332,015.
- QQQ: último cierre 741,36 < apertura 742,58, no cumple.
- RVOL declarado 0,8402 < 2,5 (NO VERIFICADO: faltan las 20 sesiones).
- Decisión hipotética: **ESPERAR**. Se sigue de las condiciones examinadas; ruptura y QQQ se verifican por completo con el JSON.

## Estado
APTO COMO CASO DE APRENDIZAJE CON LIMITACIONES.

## Contaminación y límites
- Contexto compartido entre los informes; el informe A reconoce haber analizado antes velas que incluyen esa fecha.
- Caso retrospectivo: el modelo puede conocer el pasado. No es prueba prospectiva.
- No demuestra capacidad predictiva ni ventaja de ninguna estrategia.
- El archivo de datos original (ENTRADA_AGENTES.json) debe subirse a esta carpeta para poder reproducir los cálculos.
