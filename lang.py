from itertools import islice

class Lang:
    def __str__(self):
        return "Lang: name %s, word2index %s, word2count %s, index2word %s" % \
            (self.name, list(islice(self.word2index.items(), 10)), \
            list(islice(self.word2count.items(), 10)), \
            list(islice(self.index2word.items(), 10)))

    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "SOS", 1: "EOS"}
        self.n_words = 2  # Count SOS and EOS

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1
