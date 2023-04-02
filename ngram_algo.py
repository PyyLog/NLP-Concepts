import tokenizer


class NGram:
    def __init__(self, sentence, N=1, language="french"):
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


text = "Bootstrap est une collection d'outils utiles à la création du design de sites et d'applications web. C'est un ensemble qui contient des codes HTML et CSS, des formulaires, boutons, outils de navigation et autres éléments interactifs, ainsi que des extensions JavaScript en option."
ngram = NGram(sentence=text)  # By default, N = 1 and language = 'french'
tuplesList = ngram.ngram()
print(ngram.tokenizedSentence)
print(tuplesList)
