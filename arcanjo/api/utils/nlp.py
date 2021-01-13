import nltk
from .classification import Classificator
from unidecode import unidecode

nltk.download('punkt')

class TextProcessor():
    stopwords = [
        "e",
        "ou"
        "eu",
        "ta",
        "está",
        "de",
        "meu",
        "sentindo",
        "com",
        "esta",
        "sente",
    ]

    punctuations = [
        ',',
        ".",
        "!",
        "?"
    ]

    synonims = {
        "cabeça":"cabeca",
        "forte": "intensa",
        "alta" : "forte",
        "engasgado" : "engasgo",
        "engasgou" : "engasgo",
        "engoliu" : "engasgo",
        "quebrada" : "fratura",
        "fraturou" : "fratura",
        "quebrado" : "fratura"
    }

    def treat_text(self,sentences):
        answer = []
        for word in sentences:
            if word not in self.stopwords and word not in self.punctuations:
                answer.append(word)
        return answer

    def get_synonims(self,word):
        if word in self.synonims:
            return self.synonims[word]
        return word

    def treat_symptoms(self,sentences):
        answer = []
        if(sentences[0] != "dor" or sentences[0] != "febre"):
            answer.append(sentences[0])
        for idx in range(1,len(sentences)):
            if(sentences[idx-1] == 'dor' and sentences[idx] == 'cabeça'):
                symptom = self.get_synonims(sentences[idx - 1]) + " de " + self.get_synonims(sentences[idx])
                answer.append(symptom)
            else:
                answer.append(self.get_synonims(sentences[idx]))
        return answer

    def is_urgent(self,text):
        text = unidecode(text)

        words = nltk.word_tokenize(text.lower())
        words = self.treat_text(words)
        words = self.treat_symptoms(words)

        classificator = Classificator()

        return classificator.get_classification(words)