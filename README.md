# anagrammer
A class that quickly searches for anagrams using an idea posted here: https://twitter.com/fermatslibrary/status/958700402647674880

## Files
* Anagrammer.py contains the class
* Anagrammer.ipynb contains an example using corpus contained in db

## Example usage
```
from Anagrammer import Anagrammer
corpus = ["nultolerantie", "kogelgeweer"] # Normally this is a very long list loaded from some external source
ana = Anagrammer(corpus) 

print(ana.getAnagrams("antillenroute"))
print(Anagrammer.morph_dist("nultolerantie", "antillenroute"))
print(Anagrammer.morph_dist("geweerkogel", "kogelgeweer"))
print(ana.getAnagrams("hottentottententententoonstelling"))
```
