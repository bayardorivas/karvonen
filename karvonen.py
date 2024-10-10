def main():
  print()
  print("         Training zones - Karvonen Formula", end="\n\n")

  edad=int(input("Age: "))
  freq_max=220-edad
  freq_reposo=int(input("Enter your rest heart beat: "))
  freq_reserva= freq_max-freq_reposo
  print()
  
  print(f'\nYour reserve heart beat frequency is: {freq_reserva}',end="\n\n")
  calcular_zonas(freq_reserva,freq_reposo)
    
def calcular_zonas(reserva, reposo):
  zonasFreq = {
    "zona 1":[0.50,0.60],
    "zona 2":[0.60,0.70],
    "zona 3":[0.70,0.80],
    "zona 4":[0.80,0.90],
    "zona 5":[0.90,1],
  }
  
  for zone,limites in zonasFreq.items():
    limInferior = (limites[0]*reserva) + reposo
    limSuperior = (limites[1]*reserva) + reposo
    print(f"Your {zone.capitalize()} is beween {int(limInferior)} ... {int(limSuperior)}")
  return

main()
