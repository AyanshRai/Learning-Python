a = "37.2"
t = type(a) #class <int>
print(t)

a = "37.2"
# To change any data type from string,float and Integer
b = float(a) # Here String is changing to float 
t = type(b) #class <int>
print(t)

# Sequence escape characters

a = "Priytanshi is a good girl \nbut not a \nbad girls"
print(a)
b = "Priytanshi is a good girl \tbut not a \tbad girls"
print(b)
c = "Priytanshi is a good girl but not a \"bad girls\""
print(c)