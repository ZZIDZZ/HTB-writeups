file = open('digitalcube.txt', 'r')
text = file.read()

for fifties in range(0,len(text), 50):
    print(text[fifties:49 + fifties])




# occurence for each 50 characters