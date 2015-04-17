f = open("/Users/yongcho822/Desktop/alice.txt", "r")
count = {}
for aline in f:
    for word in aline.split():
        word = word.replace('-', '').replace('"','').replace(',','').replace('.','').replace('_','').replace('?','')
        word = word.replace('?', '').replace('!', '').replace("'",'').replace('(','').replace(')','').replace(':','')
        word = word.replace('[','').replace(']','').replace(';','')

        word = word.lower()

        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
keys = list(count.keys())
keys.sort()

out = open("output.txt", 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')
print("The word 'alice' appears " + str(count['alice']) + " times in the book.")