intro=input("Introduce yourself:")
print(intro)
carCount=0
wordCount=0
for i in intro :
    carCount=carCount+1
    if (i==" "):
        wordCount=wordCount+1
print("The number of words" )
print(wordCount)
print(carCount)