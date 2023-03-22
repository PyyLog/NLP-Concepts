import math
import os


class TFIDF:
    def __init__(self, file1, file2, file3, file4, case, corpusLength):
        self.separators = {".", ":", ";", ",", "(", ")", " ", "'", "...", "·", "—", "’", "*", "«", "»"}
        self.texts = [" ".join(file1.readlines()), " ".join(file2.readlines()), " ".join(file3.readlines()), " ".join(file4.readlines())]
        self.lowercased_texts = [self.texts[0].lower(), self.texts[1].lower(), self.texts[2].lower(), self.texts[3].lower()]
        self.splitted_texts = [self.remove_inphrase_punctuation(self.lowercased_texts[0]).split(), self.remove_inphrase_punctuation(self.lowercased_texts[1]).split(), self.remove_inphrase_punctuation(self.lowercased_texts[2]).split(), self.remove_inphrase_punctuation(self.lowercased_texts[3]).split()]
        self.study_case = case - 1
        self.nbTotOfTexts = corpusLength

    def remove_inphrase_punctuation(self, lowercased_text):
        for char in lowercased_text:
            if char in self.separators:
                lowercased_text = lowercased_text.replace(char, " ")

        return lowercased_text

    def count_occurences(self):
        i = 0
        words_occurences, indexing_dico = [], {}

        for word in self.splitted_texts[self.study_case]:
            if word in indexing_dico:
                continue
            else:
                count = self.splitted_texts[self.study_case].count(word)
                words_occurences.append(count)
                indexing_dico[word] = i
                i += 1

        return indexing_dico, words_occurences

    def tfidf(self):
        tfidf_list = []
        totalNumOfTexts = self.nbTotOfTexts
        indexing_dico, words_occurences = self.count_occurences()

        for word in indexing_dico.keys():
            tf = words_occurences[indexing_dico[word]] / len(self.splitted_texts[self.study_case])

            if totalNumOfTexts != 1:
                isinOtherText = 1
                for i in range(totalNumOfTexts):
                    if i == self.study_case:
                        pass
                    else:
                        if word in self.splitted_texts[i]:
                            isinOtherText += 1

                try:
                    idf = math.log(totalNumOfTexts / isinOtherText, 10)
                except ZeroDivisionError:
                    idf = 0

                importance_rate = tf * idf
                tfidf_list.append("% .6f" % importance_rate)

            elif totalNumOfTexts == 1:
                importance_rate = tf
                tfidf_list.append("% .6f" % importance_rate)

            elif totalNumOfTexts == 0:
                print("There is no texts, so no word to analyze...")

        return tfidf_list


def readFolder():
    list = []
    for file in os.listdir("./src/text_samples"):
        if file[-4:] == ".txt":
            list.append(file[0:-4])

    return list

file1 = open("./src/text_samples/{filename}.txt".format(filename=readFolder()[0]), "r", encoding="utf-8")
file2 = open("./src/text_samples/{filename}.txt".format(filename=readFolder()[1]), "r", encoding="utf-8")
file3 = open("./src/text_samples/{filename}.txt".format(filename=readFolder()[2]), "r", encoding="utf-8")
file4 = open("./src/text_samples/{filename}.txt".format(filename=readFolder()[3]), "r", encoding="utf-8")
tfidf = TFIDF(file1, file2, file3, file4, case=1, corpusLength=1)
print(tfidf.count_occurences()[0], "\n")
print(tfidf.count_occurences()[1], "\n")
print(tfidf.tfidf())
