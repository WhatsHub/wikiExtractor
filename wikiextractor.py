import wikipedia

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

def remove_specials(string):
    return ''.join(c for c in string if c.isalnum())
    

p = wikipedia.page("Sterling Archer")
print(p.url)
print(p.title)
content = p.content
wordlist = unique_list(content.split(" "))

for x in range(0, len(wordlist)):
    wordlist[x] = remove_specials(wordlist[x])

content = "\n".join(wordlist)

file = open("wordlist.txt", "w")

file.write(content.encode("utf-8"))
file.close
