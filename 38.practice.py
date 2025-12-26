amount=int(input())
note2000= amount//2000
amount= amount%2000
note500= amount//500
amount= amount% 500
note100= amount//100
amount= amount%100
print("200 note",note2000)
print("500 note",note500)
print("100 note",note100)