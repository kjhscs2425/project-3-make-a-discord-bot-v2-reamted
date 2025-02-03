import random
"""

**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  elif "run" in user_message:
    return True
  elif "give me something random" in user_message:
    return True
  elif "s" and "r" and "i" and "m" and "p" in user_message:
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
  if "robot" in user_message:
    return f"""what do you think i am, some actaully competent AI, naaa you got the wish.com bot version bro
    {user_message.replace("robot", user_name)}"""
  elif "run" in user_message:
    return "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
  elif "give me something random" in user_message:
    random.choice(["play wynncraft", "play skybloc", "run a mile", "do 20 pushups", random.randint(1, 1023402)])
  elif "s" and "r" and "i" and "m" and "p" in user_message:
    return "shrimp"
  
    
  else:
    pass