class Classificator():

    symptoms = {
        'null': 0,
        'febre leve': 1,
        'febre media': 2,
        'febre alta': 3,
        'coriza': 1,
        'tosse': 1,
        'espirro': 1,
        'vomito': 2,
        'diarreia': 2,
        'desmaio': 3,
        'convulsao': 3,
        'nausea': 2,
        'ferida grave':3,
        'dor forte':3,
        'dor de ouvido':1,
        'inconsciente':4,
        'batimento acelerado':3,
        'reacao alergica':3,
        'palidez':3,
        'hemorragia':4,
        'intoxicacao':4,
        'batimento irregular':3,
        'colica':2,
        'anemia':2,
        'engasgo':3,
        'fratura' : 3,
        'desidratacao':3,
        'hipotermia':3,
        'ferida inflamada':2,
        'picada' : 4,
        'mordida':3
    }

    urgent_list = []

    def __init__(self):
        for symptom in self.symptoms:
            if(self.symptoms[symptom] == 3 or self.symptoms[symptom] == 4):
                self.urgent_list.append(symptom)


    def get_classification(self,vector):
        for element in vector:
            if element in self.urgent_list:
                return True
        return False
