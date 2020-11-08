import time

ordenes_de_sandwiches = ["Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "Arrollado huaso",]


sandwiches_terminados =[]
list(enumerate(sandwiches_terminados))


# Elimino Barros luco sin stock de ordenes_de_sandwiches
print("El local no cuenta con stock de Barros luco.")

stock = 1
while stock == 1:
    if "Barros luco" in ordenes_de_sandwiches:
        ordenes_de_sandwiches.remove("Barros luco")
    else:
        stock = 0    
# print(ordenes_de_sandwiches)



# Imprimo ordenes de sandwiches preparados y los agrego a la lista sandwiches_terminados
for sandwich in ordenes_de_sandwiches:
    time.sleep(0.1)
    print("Su " + sandwich + " ya esta preparado")
    sandwiches_terminados.append(sandwich)

# Enumero cada sandwich terminado
for i, sandwich in enumerate(sandwiches_terminados, 1):
    time.sleep(0.1)
    print(i, sandwich)