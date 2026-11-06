# Criterios examinados v0.1 (apertura de rango, entrada alcista)

Todos los criterios deben cumplirse para COMPRAR. Si falla cualquiera: ESPERAR.

1. **Rango inicial**: máximo de máximos y mínimo de mínimos de 09:30-09:44 ET.
2. **Ruptura alcista**: el último cierre de cinco minutos completado está por encima del máximo inicial.
3. **Volumen**: RVOL inicial >= 2,5. RVOL = volumen de los primeros 15 min / media del volumen de esos mismos
   15 min de las 20 sesiones completas anteriores. Si no hay datos de las 20 sesiones, se usa el valor declarado
   y se marca como NO VERIFICADO.
4. **Contexto**: último cierre disponible de QQQ > apertura de QQQ de la sesión.
5. **Decisión**: COMPRAR o ESPERAR hipotéticamente al siguiente open, sin afirmar su precio.

Estos criterios delimitan la revisión. No prueban que la estrategia tenga ventaja.
