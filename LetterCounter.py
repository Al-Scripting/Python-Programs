# Muqshith Shifan #100862739
from collections import Counter

class WordCounter:
    def __init__(self, file):
        self.filename = file

    def get_words_dict(self):
        with open(self.filename, 'r') as file:
            text = file.read()
            # remove punctuation
            text = text.translate(text.maketrans('', '', '!"()-[]{};:\'"\,<>./?@#$%^&*_~'))
            # split text into words
            words = text.split()
            # create dictionary with word count
            words_dict = Counter(words)

        return words_dict

    def top_10_words(self):
        words_dict = self.get_words_dict()

        # get top 10 most common words
        top_10_words = words_dict.most_common(10)

        # print out the top 10 words and their count
        for i, word_count in enumerate(top_10_words):
            print(f'{i+1}: {word_count}')

if __name__ == '__main__':

    # create WordCounter object with input file
    counter = WordCounter('text.txt')

    # get top 10 most common words and print them out
    counter.top_10_words()




