import string
import re


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

exeptions = "he", "she", "me", "be", "the", "we", 

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




def haiku_bot(text):
    #remove all punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]','', text) # replace all non white space non text with a empty string
    total = 0
    line_total = 0
    words = text.split()
    print(words)
    target = 5 #target for the current line
    line = 1 #current line
    haiku = False
    line1 = []
    line2 = []
    line3 = []
    for word in words:
        
        
        #line detector
        sylable = 0
        
        
        
        print(word)
        if line == 1:
            line1.append(word)
        if line == 2:
            line2.append(word)
        if line == 3:
            line3.append(word)
        
        if word in exeptions:
            sylable = 1
        else:
            #throw away silent e
            if word[-1] == 's':
                word = word[:-1 ]
            if word[-1] == 'e':
                word = word[:-1]
            #pad with a d
            word += 'd'
            #replace all constonants with d    
            for consonant in consonants:
                word = word.replace(consonant, 'd')
            #count vowel d's
            sylable = word.count("ad") + word.count("ed") + word.count("id") + word.count("od") + word.count("ud") + word.count("yd")
        print(sylable)
        total += sylable
        line_total += sylable
        if line_total == target and line ==1:
            target = 7
            line = 2
            line_total = 0
        if line_total == target and line == 2:
            target = 5
            line = 3
            line_total = 0
        if line_total == target and line == 3:
            haiku = True
            
        if total > 17:
            print("Too long")
            haiku = False
            break
            
    print(total)
    print(haiku)
    
    #print(line1)
    #print(line2)
    #print(line3)

    if haiku == True:
        print(line1)
        print(line2)
        print(line3)


def testing_bot(text):
    #remove all punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]','', text) # replace all non white space non text with a empty string
    total = 0
    words = text.split()
    print(words)
    for word in words:
        
        #figuring out if something actually is a haiku
        number = 0
        #line detector
        
        sylable = 0
        #line one detector
        if total == 5 and number == 0:
            total += 1
            number += 1
            print(1)
        #checking if line one has the correct amount of sylables
        elif total > 5 and number == 0:
            print("fail")
            break
        #line two detector
        elif number == 1 and total == 7:
            total += 1
            number += 1
        #cheking if line two has the correct amount of sylables
        elif total > 7 and number ==1:
            print("fail")
            break
        #compleation detector
        elif number == 2 and total == 5:
            print("this is a haiku")
            break
        
        
        print(word)
        if word in exeptions:
            sylable = 1
        else:
            #throw away silent e
            if word[-1] == 'e':
                word = word[:-1]
            #pad with a d
            word += 'd'
            #replace all constonants with d    
            for consonant in consonants:
                word = word.replace(consonant, 'd')
            #count vowel d's
            total += word.count("ad") + word.count("ed") + word.count("id") + word.count("od") + word.count("ud") + word.count("yd")
            sylable = word.count("ad") + word.count("ed") + word.count("id") + word.count("od") + word.count("ud") + word.count("yd")
        print(sylable)
        total += sylable
    print(total)




    sylable = 0
    
    text += " "
    
    

    #sylable = sylable +text.count("he")+text.count("she")+text.count("we")+text.count("be")+text.count("me")+text.count("the")+text.count("be")+text.count("ee")
    for consonant in consonants:
        text =text.replace(consonant, "d")
    
    while "e " in text:
        text = text.replace("e ", "d ")
    
    
    
    text = text.split()
    for words in text:
        print(words)
    print(text)        
    total = sylable + text.count("ad") + text.count("ed") + text.count("id") + text.count("od") + text.count("ud") + text.count("yd")
        



    print(total)



#haiku_bot("I can detect your accidental haikus and format them in lines")
haiku_bot("What we don’t notice we cannot love.  What lines love we seek to protect.")