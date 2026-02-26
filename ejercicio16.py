
metros_lamina = 4 * 1.5
consumo_pieza = 0.5

piezas_por_lamina = int(metros_lamina / consumo_pieza)
desperdicio = metros_lamina - (piezas_por_lamina * consumo_pieza)
print("Con una lámina se pueden fabricar piezas.", piezas_por_lamina)
print("El desperdicio será de metros.", desperdicio)