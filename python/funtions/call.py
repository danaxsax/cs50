from define import square #metodo 1 para importar funciones 
for e in range(10):
    print (f"la raiz de {e} es {square(e)}")

import define #metodo 2 para importar funciones
for e in range(0,10,2):
    print (f"la raiz de {e} es {define.square(e)}")