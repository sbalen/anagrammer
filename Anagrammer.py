#class based on https://twitter.com/fermatslibrary/status/958700402647674880
class Anagrammer:
    alphabet = {"a":2,"b":3,"c":5,"d":7,"e":11,"f":13,"g":17,"h":19,"i":23,"j":29,"k":31,"l":37,"m":41,"n":43,"o":47,"p":53,"q":59,"r":61,"s":67,"t":71,"u":73,"v":79,"w":83,"x":89,"y":97,"z":101}

    def __init__(self, corpus):
        self.index = {}
        self.createIndex(corpus)
    
    def createAnagramHash(self, word):
        index = 1
        for x in list(word):
            index *= self.alphabet[x]
        return index

    def createIndex(self, corpus):
        for word in corpus:
            self.index.setdefault(self.createAnagramHash(word),set())
            self.index[self.createAnagramHash(word)].add(word);
    
    def getAnagrams(self, word):
        if self.createAnagramHash(word) in self.index:
            return [w for w in self.index[self.createAnagramHash(word)] if w != word]
        else: 
            return 
    
    #returns the intersection of two lists
    @staticmethod
    def intersection( lst1, lst2): 
        temp = set(lst2) 
        lst3 = [value for value in lst1 if value in temp] 
        return lst3 

    #returns a morphological distance between two words
    #based on the relative trigrams the two have in common
    #value between 0 and 1, 0 being most similar
    @staticmethod
    def morph_dist( word1, word2):
        n = 3
        if len(word1) == 1:
            return 0
        if len(word1) <= 3:
            n=2
        #expects two words of same length
        #we convert both words in ngrams 
        w1 = [word1[i:i+n] for i in range(len(word1)-n+1)]
        w2 = [word2[i:i+n] for i in range(len(word2)-n+1)]
        #and calculate the relative intersection
        return 1 - len(Anagrammer.intersection(w1, w2)) / len(w2)
           
    