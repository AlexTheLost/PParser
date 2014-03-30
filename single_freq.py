import re
import operator

def getFreq(words):
    words = re.sub('[^A-Za-z\']',  ' ', words)
    words = re.sub('[ ]+', ' ', words).lower().split(' ')
    freq = {}
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)

out=""
for v in getFreq(open("in/WarAndPeace.txt", 'r').read()):
    out += str(v[1]) + ' = ' + v[0] + '\n' 
open('out.txt', 'w').write(out)



