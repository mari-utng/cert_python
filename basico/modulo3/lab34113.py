# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print ("Paso 2:", Beatles)

# paso 3
for member in range(2) :
    BeatleName = input (" Agregue a los siguientes miembro: Stu Sutcliffe y Pete Best ")
    Beatles.append (BeatleName)
print ("Paso 3: ", Beatles)

# paso 4
del Beatles[3:5]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)
