word = input("enter a word : ")
len = len(word)
for i in range (len-1,-1,-1):
    print(word[i] , end ="")