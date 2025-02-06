import string



'''
all exeptions 
We
he
me
she
the
he
be


quiet
before

'''


consonants = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'



def useless():      
        if "ad" in words:
            sylable += 1
        if "ed" in words:
            sylable += 1
        if "id" in words:
            sylable =+ 1
        if "od" in words:
            sylable =+ 1
        if "ud" in words:
            sylable =+ 1
        if "yd" in words:
            sylable =+ 1
        else:
            pass


def word_spilter():
    sylable = 0
    text = "the he"

    if "the" in text:
        sylable += 1
    if "he" in text:
        sylable += 1
    if "be" in text:
        sylable += 1
    if "me" in text:
        sylable += 1
    if "she" in text:
        sylable += 1
    if "we" in text:
        sylable += 1

    else:
        pass





    for consonant in consonants:
        text =text.replace(consonant, "d")
        
    print(text)
    
    
            
    total = sylable + text.count("ad") + text.count("ed") + text.count("id") + text.count("od") + text.count("ud") + text.count("yd")
        



    print(total)
word_spilter()