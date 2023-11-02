# ----------------- ¿Es Mutante?----------------
def is_mutant(dna, base):
   v_h = validate_horizontal(dna, base)
   v_v = validate_vertical(dna, base)
   v_d_l = validate_diagonal_left(dna, base)
   v_d_r = validate_diagonal_right(dna, base)
   # print(f"V: {v_v}, H: {v_h}, D_L: {v_d_l}, D_R: {v_d_r}")
   return True if (v_v + v_h + v_d_l + v_d_r) > 1 else False

# ----------------- Validaciones de Matriz -------------

# ------------- Horizontal
def validate_horizontal(dna, base):
   coincidence = 0 # Incrementara si se encontro una horizontal de 4 bases iguales.
   count = 0 # Contara las apariciones de la misma base.
   size = len(base)
   
   for row in dna:
      elm_coincidence = row[0]
      for base_elm in row:
         # Dejara de validar si ya encontro la secuencia
         if count == size: break
         if elm_coincidence == base_elm: count += 1
         else:
            # Reseteo el contador si el valor actual no coincide con el anterior.
            elm_coincidence = base_elm
            count = 1 
      # Size + 1 es para cuando la horizontal esta al final de la linea. 
      if count in [size, size + 1]: coincidence += 1
      count = 0
   else:
      return coincidence
 
# --------------- Vertical
def validate_vertical(dna, base):
   coincidence = 0 # Incrementara si se encontro una horizontal de 4 bases iguales.
   count = 0 # Contara las apariciones de la misma base
   size = len(base)
   
   for x in range(len(dna)):
      elm_coincidence = dna[0][x]
      for y in range(len(dna)):
         # Dejara de validar si ya encontro la secuencia
         if count == size: break
         if elm_coincidence == dna[y][x]: count += 1
         else:
            # Reseteo el contador si el valor actual no coincide con el anterior.
            elm_coincidence = dna[y][x]
            count = 1
      # Size + 1 es para cuando la vertical esta al final de la linea. 
      if count in [size, size + 1]: coincidence += 1
      count = 0
   else:
      return coincidence

# ----------- Diagonales de Derecha a Izquierda
def validate_diagonal_right(dna, base):
   coincidence = 0 # Incrementara si se encontro una diagonal de 4 bases iguales.
   count = 0 # Contara las apariciones de la misma base
   size = len(dna)
   half = 0
   cross_y = 0 # Incrementa x despues de la diagonal (medio)
   i = 0 # Decrementa el tamaño del items a recorrer despues de diagonal (medio)
   
   for r in range(size - 1):
      if (half == size - 1) and (cross_y == 0): i = -1
      # Aumenta cross_y si se paso la diagonal (medio)
      if (half == size - 1) or (cross_y > 0):  # Ejemplo
         half -= cross_y # 4
         cross_y += 1 # 2
         i += 1 # 1
         # [2][4], recorrido 4 + 1 + i(1) - c_y(2) = 4 items
         elm_coincidence = dna[cross_y][half]
      else: 
         half = int(len(dna) / 2) + r
         elm_coincidence = dna[half][cross_y]
      
      # Ej: diagonal (medio): 5, 0, 1, 0 = 6 items diagonal
      for q in range(half + 1 + i - cross_y): # Ej: Cuarto item
         x = q + cross_y # 3 + 0 = 3
         y = half - q # 5 - 3 = 2

         if count == len(base): break
         if elm_coincidence == dna[x][y]: count += 1
         else:
            elm_coincidence = dna[y][x]
            count = 1
     
      if count in [4, 5]: coincidence += 1
      count = 0
   else:
      return coincidence

# ------------------- Diagonales de Izquierda a Derecha
def validate_diagonal_left(dna, base):
   support = int(len(dna) / 2)
   coincidence = 0 # Incrementara si se encontro una diagonal de 4 bases iguales.
   count = 0 # Contara las apariciones de la misma base
   max = 1 # Util para Y
   cross_y = 0
   
   for r in range(len(dna) - 1): 
      if max == 0: # Se mantiene Y en 0 post diagonal (medio)
         cross_y += 1 # Incrementa X post diagonal (medio)
      else: 
         half = support + r # Mantiene las cantidad de items a recorrer diagonalmente
         max = support - (r + 1) # Decrementa y
      elm_coincidence = dna[cross_y][max]
      
      for q in range(half + 1 - cross_y): #Ej: r = 2, item 2
         x = q + cross_y # 1 + 0 = 1
         y = max + q #  1 + 1 = 2
         
         if count == len(base): break
         if elm_coincidence == dna[x][y]: count += 1
         else:
            elm_coincidence = dna[y][x]
            count = 1

      if count in [4, 5]: coincidence += 1
      count = 0
   else:
      return coincidence