myset = {"apple", "banana", "cherry","apple"} #forma 1 de declarar set, los valores duplicados no los imprime
myset.add("1")

s = set() #forma 2 de declarar set, vacio e irlo llenando
s.add("a") 
s.add("b") 
s.add("c") 
s.add("d") 
s.add("c") 
s.remove("c")

print(f"El tamano de mi set es de {len(myset)}")

print(s, myset)
