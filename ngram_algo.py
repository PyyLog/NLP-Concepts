import tokenizer


class NGram:
    def __init__(self, sentence, N=1, language='french'):
        self.sentence = sentence
        self.language = language
        self.N = N
        self.token = tokenizer.Tokenization(self.sentence, self.language)
        self.tokenizedSentence = self.token.tokenize()[0]

    def ngram(self):
        tuplesList = []
        for list in self.tokenizedSentence:
            sublist = []
            for w in list:
                subsublist = []
                for i in range(self.N + 1):
                    try:
                        subsublist.append(list[list.index(w) + i])
                    except(IndexError):
                        pass

                sublist.append(tuple(subsublist))

            for w in reversed(list):
                subsublist = []
                if list.index(w) != 0:
                    for i in range(self.N + 1):
                        try:
                            subsublist.append(list[list.index(w) - i])
                        except(IndexError):
                            pass

                    sublist.append(tuple(subsublist))

            tuplesList.append(sublist)

        return tuplesList

    def OneHotEncoding(self):
        dicoEncoding = {}

        for list in self.tokenizedSentence:
            dicoList = {}

            for word in list:
                dicoList[word] = [1 if (i == word) else 0 for i in list]

            dicoEncoding['list_' + str(self.tokenizedSentence.index(list) + 1)] = dicoList

        return dicoEncoding


text = "Bootstrap est une collection d'outils utiles à la création du design de sites et d'applications web. C'est un ensemble qui contient des codes HTML et CSS, des formulaires, boutons, outils de navigation et autres éléments interactifs, ainsi que des extensions JavaScript en option."
# text2 = "With administrative worries attended to, Wilsdorf turned the company's attention to a marketing challenge: the infiltration of dust and moisture under the dial and crown, which damaged the movement. To address this problem, in 1926 a third-party casemaker produced a waterproof and dustproof wristwatch for Rolex, giving it the name 'Oyster'."
ngram = NGram(sentence=text)  # By default, N = 1 and language = 'french'
getTuplesList = ngram.ngram()
ohe = ngram.OneHotEncoding()

print(ngram.tokenizedSentence)
print(getTuplesList)
print(ohe)
