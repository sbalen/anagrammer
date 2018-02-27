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
            return self.index[self.createAnagramHash(word)]
        else: 
            return [word]