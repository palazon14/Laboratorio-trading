# Parámetros v0.1 (fijados antes de cualquier caso limpio)

Fecha de fijación: 2026-11-06. Complementan `REGLAMENTO_v0.1.md` (secciones 5 y 6) y `CRITERIOS_ORB_v0.1.md`.
Estos valores son hipótesis de partida. No son óptimos ni recomendaciones de inversión. Todo es simulado.
NO se han ajustado mirando el caso 001 ni ningún desenlace.

## Alcance
- Valor: AAPL. Corte: 10:00 ET. Solo entrada alcista (COMPRAR). Si ESPERAR: sin operación.

## Entrada simulada
- Precio: apertura de la vela de 1 min siguiente al corte (dato real del archivo, nunca estimado).
- Deslizamiento: 0,02 % en contra (entrada = apertura x 1,0002).
- Comisión: 0 (declarada).

## Tamaño y riesgo
- Riesgo máximo por operación: 10 USD (1 % de un capital hipotético de 1.000 USD).
- Posición máxima nominal: 1.000 USD, sin apalancamiento.
- Cantidad = mínimo entre (1.000 / precio_entrada) y (10 / (precio_entrada - stop)). Se permiten fracciones.

## Salida
- Stop: mínimo del rango inicial (09:30-09:44 ET). Se considera activado si el mínimo de una vela de 1 min <= stop.
  Precio de salida: el stop menos 0,02 % de deslizamiento; si la vela abre por debajo del stop, la apertura de esa vela menos 0,02 %.
- Salida forzosa: apertura de la vela de 1 min de las 15:55 ET, menos 0,02 %.
- Sin objetivo de beneficio (no se define ninguno).
- Si en una misma vela de 1 min no se puede saber el orden de los hechos, se aplica el supuesto más desfavorable (stop primero).

## Cambios de reglas
- No se modifican reglas ni parámetros antes de 30 casos cerrados con decisión sellada.
- Cada cambio crea una versión nueva con su razón escrita. Las versiones anteriores se conservan.

## Limitaciones
- Velas de 1 min: no resuelven el orden exacto dentro de la vela.
- Sin datos de colas de órdenes, ni de liquidez real.
- 30 casos siguen siendo una muestra pequeña. No demuestran capacidad predictiva.
