import tokenizer


class NGram:
    def __init__(self, sentence, N=1, language="french"):
        self.sentence = sentence
        self.language = language
        self.N = N
        self.token = tokenizer.Tokenization(self.sentence, self.language)
        self.tokenizedSentence = self.token.run()[0]

    def getTuples(self):
        tuplesList = []
        for list in self.tokenizedSentence:
            sublist = []
            for w in list:
                if list.index(w) == 0:
                    subsublist = []
                    for i in range(self.N + 1):
                        subsublist.append(list[list.index(w) + i])
                    sublist.append(tuple(subsublist))

                elif list.index(w) == len(list) - 1:
                    subsublist = []
                    for j in range(self.N + 1):
                        subsublist.append(list[list.index(w) - j])
                    sublist.append(tuple(subsublist))

                else:
                    if self.N % 2 == 0:
                        mid = int(self.N / 2)
                        subsublist = []
                        subsublist.append(list[list.index(w)])
                        for i in range(1, mid + 1):
                            subsublist.append(list[list.index(w) + i])
                            subsublist.append(list[list.index(w) - i])

                        sublist.append(tuple(subsublist))

                    elif self.N % 2 == 1:
                        if self.N == 1:
                            subsublist = []
                            for i in range(self.N + 1):
                                subsublist.append(list[list.index(w) + i])
                            sublist.append(tuple(subsublist))

                        if self.N > 1:
                            subsublist = []
                            for i in range((self.N - int(self.N / 2)) + 1):
                                subsublist.append(list[list.index(w) + i])
                            sublist.append(tuple(subsublist))

                            subsublist = []
                            for i in range((self.N - int(self.N / 2) + 1) + 1):
                                subsublist.append(list[list.index(w) + i])
                            sublist.append(tuple(subsublist))

            tuplesList.append(sublist)

        return tuplesList


text = "Bootstrap est une collection d'outils utiles à la création du design de sites et d'applications web. C'est un ensemble qui contient des codes HTML et CSS, des formulaires, boutons, outils de navigation et autres éléments interactifs, ainsi que des extensions JavaScript en option."
ngram = NGram(sentence=text, N=1, language="french")
tuplesList = ngram.getTuples()
print(ngram.tokenizedSentence)
print(tuplesList)
