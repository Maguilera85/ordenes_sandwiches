ordenes_de_sandwiches = ["Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",
                        "Chacarero", "Barros luco", "Chemilico", "Churrasco italiano", "De arrollado huaso",]


sandwiches_terminados =[]


for sandwich in ordenes_de_sandwiches:
    print("Su pedido se encuentra listo: " + sandwich)
    sandwiches_terminados.append(sandwich)
    ordenes_de_sandwiches.remove(sandwich)
    