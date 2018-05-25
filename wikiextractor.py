import wikipedia

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

def remove_specials(string):
    return ''.join(c for c in string if c.isalnum())
    
# set the language of wikipedia
wikipedia.set_lang('de')

# present options if page was not found or disambiguation page
try:
    p = wikipedia.page("Archer (Zeichentrickserie)")
except wikipedia.exceptions.DisambiguationError as e:
    print e.options

# print the url and title of the article
print(p.url)
print(p.title)
content = p.content # pull the content of the page

# few replacements
content = content.replace('-', ' ')
content = content.replace('\n', ' ')
# whole string to lower case
content = content.lower()

# save words in a wordlist and remove duplicates
wordlist = unique_list(content.split(" "))


wlist = []
# remove special characters from every word in wordlist
for i in range(0, len(wordlist)):
    word = wordlist[i]
    if word != '' and word != ' ' and word != '\n':
        wlist.append(remove_specials(word))

# join the list of words to a single string, with each word seperate by newline
content = "\n".join(wlist)

# write the wordlist to a file
file = open("wordlist.txt", "w")

file.write(content.encode("utf-8"))
file.close
