s = input("")
vowel = { }
consonant = { }
for ch in s :
    if ch.isalpha():
        if ch in "aeiou" :
            vowel[ch]= vowel.get(ch, 0)+1 
        else :
            consonant[ch]= consonant.get(ch,0)+1
print("vowel: ")
for key,value in vowel.items():
    print(key,":",value)
print("consonant: ")
for key,value in consonant.items():
    print(key,":",value)