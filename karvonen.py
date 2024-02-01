def main():
  print()
  print("         Training zones - Karvonen Formula", end="\n\n")

  edad=int(input("Age: "))
  freq_max=220-edad
  freq_reposo=int(input("Enter your rest heart beat: "))
  print()
  freq_reserva= freq_max-freq_reposo
  
  print(f'Your reserve heart beat frequency is: {freq_reserva}',end="\n\n")
  calcular_zonas(freq_reserva,freq_reposo)
  
  
def calcular_zonas(reserva, reposo):
  zona1_inferior= (0.5 *reserva) + reposo
  zona1_superior= (0.6 *reserva) + reposo
  print(f'Zone 1 .................... {int(zona1_inferior)}bpm - {int(zona1_superior)}bpm')
  zona1_inferior= (0.6 *reserva) + reposo
  zona1_superior= (0.7 *reserva) + reposo
  print(f'Zone 2 .................... {int(zona1_inferior)}bpm - {int(zona1_superior)}bpm')
  zona1_inferior= (0.7 *reserva) + reposo
  zona1_superior= (0.8 *reserva) + reposo
  print(f'Zone 3 .................... {int(zona1_inferior)}bpm - {int(zona1_superior)}bpm')
  zona1_inferior= (0.8 *reserva) + reposo
  zona1_superior= (0.9 *reserva) + reposo
  print(f'Zone 4 .................... {int(zona1_inferior)}bpm - {int(zona1_superior)}bpm')
  zona1_inferior= (0.9 *reserva) + reposo
  zona1_superior= (1 *reserva) + reposo
  print(f'Zone 5 .................... {int(zona1_inferior)}bpm - {int(zona1_superior)}bpm')
  return

main()
