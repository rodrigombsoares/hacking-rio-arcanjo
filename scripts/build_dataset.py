from random import randint

symptoms = {
    'null': 0,
    'febre leve': 1,
    'febre media': 2,
    'febre aguda': 3,
    'coriza': 1,
    'tosse': 1,
    'espirro': 1,
    'vomito': 2,
    'diarreia': 2,
    'desmaio': 3,
    'convulsao': 3,
    'nausea': 2
}

lenght = len(symptoms)
sequences = []
for _ in range(10):
    client_sim = []
    for _ in range(6):
        index = randint(0,lenght)
        if index not in client_sim:
            client_sim.append(index)
        else:
            client_sim.append(0)
    sequences.append(client_sim)

for s in sequences:
    print(s)