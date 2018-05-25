#!/usr/bin/python

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

def remove_specials(string):
    return ''.join(c for c in string if c.isalnum())
    
def pullwiki(query, lang):

    import wikipedia

    # set the language of wikipedia
    wikipedia.set_lang(lang)

    # present options if page was not found or disambiguation page
    try:
        p = wikipedia.page(query)
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
    return content

# main routine
if __name__ =='__main__':

    import sys

    query = sys.argv[1]
    lang = sys.argv[2]
    wl = pullwiki(query, lang)

    # write the wordlist to a file
    file = open("wordlist.txt", "w")

    file.write(wl.encode("utf-8"))
    file.close
