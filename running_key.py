import string
alphabet = list(string.ascii_uppercase)

def encoder(text,runningKey):
   key = createKey(runningKey.upper())
   text = list(text.upper())
   keyCounter = 0
   for i in range(0,len(text)):
    k = 0
    while k < 26:
        if text[i] not in alphabet:
            break
        if keyCounter == len(runningKey):
            keyCounter = 0
        if text[i] == key[keyCounter][k]:
           text[i] = alphabet[k]
           keyCounter+=1
           break
        k+=1
   return "".join(text)

def createKey(runningKey):
    i = 0
    key = []
    while i < len(runningKey):
      w = alphabet[alphabet.index(f"{runningKey[i]}"):]
      w.extend(alphabet[:alphabet.index(f"{runningKey[i]}")])
      key.append(w)
      i+=1
    return key
