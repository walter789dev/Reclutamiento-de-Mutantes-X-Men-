from functions.validate_mutants import is_mutant
from functions.get_dna import get_dna

# ---------------- Inicio del Programa: Busqueda de Mutantes 
nitrogen_base = ["A", "T", "C", "G"]
sequence_size = 6

print("👋 Bienvenido: Magneto \n")

while True:
   option = input("💠 ¿Que desea realizar? \n1. Verificar posible mutante \n2.  Salir\n: ")
   # Verifico que sea un valor númerico, sino expecifico el error
   if option.isnumeric(): 
      option = int(option)
      if option == 1:
         dna = get_dna(nitrogen_base, sequence_size, ", ".join(nitrogen_base))
         # De acuerdo al valor BOOLEANO obtenido, mostrara un resultado
         print(f"\n> El ADN ingresado indica: {'Gen Mutante' if is_mutant(dna, nitrogen_base) else 'No Mutante'}\n")
      elif option == 2: #Opción para salir del programa
         print("\n👋 Que tenga un buen dia")
         break
      else: 
         print("\n❌ La opción elegida no existe, intente nuevamente \n")
   else:
      print("\n❌ Debe ingresar un número que represente la decision a tomar, intente nuevamente\n")