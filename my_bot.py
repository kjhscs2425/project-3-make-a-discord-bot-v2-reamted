import random
import string
import re

alphabet = string.ascii_lowercase





consonants = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'

exeptions = "he", "she", "me", "be", "the", "we", 

def syllable_bot(user_message):
    #remove all punctuation
    text = user_message.lower()
    text = re.sub(r'[^\w\s]','', text) # replace all non white space non text with a empty string
    total = 0
    words = text.split()
    #print(words)
    for word in words:
        #figuring out if something actually is a haiku
        number = 0
        #line detector
        sylable = 0
          
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
            sylable += word.count("ad") + word.count("ed") + word.count("id") + word.count("od") + word.count("ud") + word.count("yd")
        #print(sylable)
        total += sylable
    return str(total)




state = "normal"







"""

**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  global state
  if "robot" in user_message:
    return True
  elif "run" in user_message:
    return True
  elif "give me something random" in user_message:
    return True
  elif "s"  in user_message and "h" in user_message and "r" in user_message and "i" in user_message and "m" in user_message and "p" in user_message:
    return True
  elif "bye robot" in user_message:
    return True
  elif "syllable counter" in user_message:
    return True
  elif "yea" in user_message:
    return True
  elif "yap" in user_message:
     state = "counter"
     return True
  elif state == "counter":
     return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global state
  if "robot" in user_message:
    return f"""what do you think i am, some actaully competent AI, naaa you got the wish.com bot version bro
    {user_message.replace("robot", user_name)}"""
  elif "run" in user_message:
    return "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
  elif "give me something random" in user_message:
    random.choice(["play wynncraft", "play skybloc", "run a mile", "do 20 pushups", random.randint(1, 1023402)])
  elif "s"  in user_message and "h" in user_message and "r" in user_message and "i" in user_message and "m" in user_message and "p" in user_message:
    return "shrimp"
  elif "bye robot" in user_message:
    return "I aint going nowhere" 
  elif "syllable counter" in user_message:
     state = "counter"
     return "what do you want me to count"
     
  elif "yea" in user_message:
     return "YHEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
  elif "yap" in user_message:
     return '''Twas rizzly, and the skibidi toes \n
        Did fanum tax and scroll YouTube shorts in the condors: 
      All chinsy were the gopals,
        And played Brawl Stars indoors.'''
  elif state == "counter":
     return syllable_bot(user_message)
  else:
    pass