import json


class Tokenization:
    def __init__(self, text, language='french'):
        self.separators = {":", ";", ",", "(", ")", " ", "'", "...", "·", "—", "’", "*", "«", "»"}
        self.lowercased_text = text.lower()
        self.splitted_text = self.remove_inphrase_punctuation().split()
        self.language = language

        if self.language == "french":
            self.file = open("./src/stop_words/stop_words_french.json", encoding="utf-8")
            self.useless_words = json.load(self.file)
        elif self.language == "english":
            self.file = open("./src/stop_words/stop_words_english.json", encoding="utf-8")
            self.useless_words = json.load(self.file)

    def remove_inphrase_punctuation(self):
        for char in self.lowercased_text:
            if char in self.separators:
                self.lowercased_text = self.lowercased_text.replace(char, " ")

        return self.lowercased_text

    def get_text_matrix(self):
        text_matrix, sublist = [], []

        for part in self.splitted_text:
            for char in part:
                if (char == ".")or (char == "?") or (char == "!"):
                    sentence = self.splitted_text[:self.splitted_text.index(part) + 1]
                    self.splitted_text = [elem for elem in self.splitted_text if elem not in sentence]
                    sublist.append(self.splitted_text)
                    text_matrix.append(sentence)
        else:
            if (part[-1] != ".") and (part[-1] != "?") and (part[-1] != "!"):
                text_matrix.append(self.splitted_text)

        return text_matrix

    def get_split_words(self, text_matrix):
        for list in text_matrix:
            for word in list:
                for char in word:
                    if (char == ".") or (char == "?") or (char == "!"):
                        elem = text_matrix[text_matrix.index(list)][list.index(word)].replace(char, "")
                        text_matrix[text_matrix.index(list)][list.index(word)] = elem

        return text_matrix

    def remove_useless_words(self, matrix):
        for list in matrix:
            matrix[matrix.index(list)] = [word for word in list if word not in self.useless_words]

        return matrix

    def get_occurences(self, matrix):
        occurences_list, unique_words_matrix = [], []

        for list in matrix:
            sublist, occurences_sublist = [], []
            unique_words_matrix.append(sublist)
            occurences_list.append(occurences_sublist)

            for word in list:
                if word not in sublist:
                    sublist.append(word)
                    occurences_sublist.append(list.count(word))

        return unique_words_matrix, occurences_list

    def tokenize(self):
        text_matrix = self.get_text_matrix()
        cleaned_text_matrix = self.get_split_words(text_matrix)
        important_text_matrix = self.remove_useless_words(cleaned_text_matrix)
        final_matrix, occurences = self.get_occurences(important_text_matrix)

        return final_matrix, occurences


# text1 = "TypeScript a été conçu pour pallier les lacunes de JavaScript pour le développement d'applications à grande échelle à la fois chez Microsoft et chez leurs clients externes. Les défis liés à la gestion de code JavaScript complexe ont conduit à une demande d'outils personnalisés pour faciliter le développement de composants dans le langage."
# text2 = "we are studying every day, the faster the better but quality is what matter most for engineers"
# tokenizer = Tokenization(text=text2, language="english")
# final_matrix, occurences = tokenizer.tokenize()
# print(final_matrix)
# print(occurences)
# print(test.splitted_text)
