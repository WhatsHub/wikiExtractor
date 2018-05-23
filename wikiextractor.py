import wikipedia

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

p = wikipedia.page("Sterling Archer")
print(p.url)
print(p.title)
content = p.content
wordlist = unique_list(content.split(" "))
content = "\n".join(wordlist)

print(content)
