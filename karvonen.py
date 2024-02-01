def main():
  print()
  print("         Zonas de entrenamiento - Formula Karvonen")

  edad=int(input("Introduzca su edad: "))
  freq_max=220-edad
  freq_reposo=int(input("Introduzca su frecuencia en reposo: "))
  freq_reserva= freq_max-freq_reposo
  
  print(f'Su frecuencia de reserva es {freq_reserva}')
  print()
  calcular_zonas(freq_reserva,freq_reposo)
  print()
  
def calcular_zonas(reserva, reposo):
  zona1_inferior= (0.5 *reserva) + reposo
  zona1_superior= (0.6 *reserva) + reposo
  print(f'Zona 1 de entrenamiento para usted .................... {int(zona1_inferior)} - {int(zona1_superior)}')
  zona1_inferior= (0.6 *reserva) + reposo
  zona1_superior= (0.7 *reserva) + reposo
  print(f'Zona 2 de entrenamiento para usted .................... {int(zona1_inferior)} - {int(zona1_superior)}')
  zona1_inferior= (0.7 *reserva) + reposo
  zona1_superior= (0.8 *reserva) + reposo
  print(f'Zona 3 de entrenamiento para usted .................... {int(zona1_inferior)} - {int(zona1_superior)}')
  zona1_inferior= (0.8 *reserva) + reposo
  zona1_superior= (0.9 *reserva) + reposo
  print(f'Zona 4 de entrenamiento para usted .................... {int(zona1_inferior)} - {int(zona1_superior)}')
  zona1_inferior= (0.9 *reserva) + reposo
  zona1_superior= (1 *reserva) + reposo
  print(f'Zona 5 de entrenamiento para usted .................... {int(zona1_inferior)} - {int(zona1_superior)}')
  return

main()
