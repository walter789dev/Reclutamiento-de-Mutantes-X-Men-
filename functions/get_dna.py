# ------------------------ Obtener ADN --------------------

def get_dna(base, t_sequence, text):
   dna_list = [] # Alcena las secuencias de ADN
   count = 1 # Registra las cantidad de secuencuas registradas
   
   print(f"\n🔸 Debe ingresar {t_sequence} secuencias de ADN para verificar si es un Mutante o no. \n🔸 Aclaración:")
   print(f"⚠️  Las secuencias deben estar compuestas de: {text} (representan bases hidrogenadas)")
   print(f"⚠️  Deben tener un tamaño de {t_sequence} caracteres")
   print("⚠️  Sera Mutante si se encuentra más de una secuencia de cuatro bases iguales en su ADN \n")
   
   while count <= t_sequence:
      sequence = input(f"💠 Ingrese la secuencia número {count}: ").upper().strip() 
      # Verifico que tenga el tamaño y el tipo de dato correcto.
      if len(sequence) == t_sequence and not sequence.isnumeric(): 
         # Chequeo que toda la secuencia coincida con las bases nitrogenadas
         filter_sequence = [sequence[i] in base for i in range(len(sequence))]
         
         if False not in filter_sequence: 
            dna_list.append(sequence) 
            count += 1
         else: 
            print(f"\n❌ La secuencia debe contener solamente: {text}. Intente nuevamente \n")
      else: 
         print("\n❌ El tamaño de la secuencia es incorrecto, intente nuevamente \n")
   else: 
      return dna_list