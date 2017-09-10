import nltk

class Analyzer():
    """Implements sentiment analysis."""
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #two sets that will store the words
        self.positiveset, self.negativeset = set(), set()
        #skipping the unnecesary and one line in pos
        with open(positives, 'r') as posfile:
            while True:
                line = posfile.readline()
                if not ";" in line: break
            #reading pos
            while True:
                line = posfile.readline()
                if not line: break
                self.positiveset.add(line.rstrip())
        #skipping unnecesary and one lines in neg
        with open(negatives, 'r') as negfile:
            while True:
                line = negfile.readline()
                if not ";" in line: break
            #reading neg
            while True:
                line = negfile.readline()
                if not line: break
                self.negativeset.add(line.rstrip())       

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        count = 0
        words = nltk.word_tokenize(text)
        for x in words:
            if x in self.positiveset: count += 1
            elif x in self.negativeset: count += -1
        if count < 0: return -1
        elif count > 0: return 1
        else : return 0