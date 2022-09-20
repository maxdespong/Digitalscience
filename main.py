import time


# ill be using def statements so than when I get to directing the code it will look alot nicer

# the def statement bellow plays a part of the story using the print statement embedded
def intro():
    print("""Welcome to my text-based game called the maze. Be careful because all decisions are final.
(The decisions are in all capitals and look like THIS)

It's a cold autumn afternoon in a small town in Kentucky, and you have decided to go on a walk to clear your head. You notice 
a weird opening in a field but decide to ignore it but as you are walking away something calls your name from where it was. You quickly 
rush to it to see if someone was in danger but no one was there. You look around your surroundings confused and your eyes go o the opening 
which seems to go for a while, as you are contemplating whether to go your name is called from inside the opening so you run into the opening 
trying to find the person but a door which didn't seem to be there before quickly shut behind you. As you look around desperately you realise 
that there is no way back the way you came, but you do notice an inscription on the wall in the shape of a maze. This is when you look around 
and notice that there are two paths ahead of you and it clicks, you are stuck in a maze. 

There are 2 paths you can take left or right, the LEFT has more light so it will be easier to see but is overgrown and abandoned 
looking whereas the RIGHT is darker but doesn't seem like it's been abandoned because it’s just clean stone bricks.

Which path do you pick?
""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c
    c = input()
    time.sleep(2)
    if c.upper() == "RIGHT":
        pass
    elif c.upper() == "LEFT":
        pass
    else:
        intro()


# Creating an inventory list for a part on the game
inventory = []


# the def statement bellow plays a part of the story using the print statement embedded
def C1():
    print("""As you are walking through the path you chose on your trip on a pile of clutter, you have minimal vision but 
it looks like rotten food and old clothing. It smells terrible but there might be something that will help.
 
Do you SEARCH through it or KEEP WALKING?
     """)
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c1
    c1 = input()
    time.sleep(2)
    if c1.upper() == "SEARCH":
        pass
    elif c1.upper() == "KEEP WALKING":
        pass
    else:
        C1()


# the def statement bellow plays a part of the story using the print statement embedded
def C2():
    print("""You venture forward using the rough concrete wall as a guide, you feel your foot loose flooring and realise 
there is a massive hole ahead of you but it's too late and you fall, losing consciousness when you hit the bottom. As you 
wake back up a massive shock of pain hits you and you sit up looking at your mangled legs. Your head shoots up because you 
see movement in the top of your eyes and see a massive creature come towards you. You try to move away but your arms are strong 
enough to move your body and you realise the creature is a spider. It walks up to you and picks you up and starts wrapping you 
up in its webs, they eventually cover your head which causes you to suffocate and die.

Ending 0: Well that was fast""")


# the def statement bellow plays a part of the story using the print statement embedded
def C3():
    print("""You stick your hand into the pile which feels oddly warm and you find a flashlight which you pick up and turn
on to continue looking through the pile but you find nothing else. You use the torch to look ahead of you and notice a 
massive pit with a bridge going over it. You walk across the bridge and look down and see a lot of bodies strung up by 
spider webs. As you look ahead you see a man standing in front of two doors “to my LEFT you will find what the heart 
desires but to the RIGHT  is what your mind craves, pick carefully but no matter what option I'll never give you up or let you down”

Which door do you choose?
    """)
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c3
    c3 = input()
    time.sleep(2)
    if c3.upper() == "LEFT":
        pass
    elif c3.upper() == "RIGHT":
        pass
    else:
        C3()


# the def statement bellow plays a part of the story using the print statement embedded
def C4():
    print("""You are greeted by 3 paths, STRAIGHT, LEFT, and RIGHT but you are also greeted by a horrible stench carried 
    by a breeze from the right path. 
    
    Which path do you pick?""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c4
    c4 = input()
    time.sleep(2)
    if c4.upper() == "LEFT":
        pass
    elif c4.upper() == "RIGHT":
        pass
    elif c4.upper() == "STRAIGHT":
        pass
    else:
        C4()


# the def statement bellow plays a part of the story using the print statement embedded
def C5():
    print("""You walk straight for a while and find yourself at an altar, as you look at it you notice some demonic-looking 
    symbols and some ritual gear. As you look more around the altar a door closes the path you came from. Suddenly you hear 
    hundreds of footsteps and notice you're surrounded by people in almost cult uniforms. Then one speaks up “we are for the truth, 
    the freedom will you join us?” 
    
    Do you JOIN the members or DONT JOIN?""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c5
    c5 = input()
    time.sleep(2)
    if c5.upper() == "JOIN":
        pass
    elif c5.upper() == "DONT JOIN":
        pass
    else:
        C5()


# the def statement bellow plays a part of the story using the print statement embedded
def C67():
    print("""They quickly rush to you and manhandle you onto the altar and strap you down so you can't move. The leader 
of the cult moves forward to you chanting something in a language you have never heard before and picking up an ancient-looking 
dagger, is this my death? He holds it up to your chest and carves a pentagram but then he pulls out a weird-looking powder and 
sprinkles it into the wound. The pain is so unbearable that you pass out. When you regain consciousness you feel different 
and there is no one around then you hear a voice… coming from my head? “Hello there” 

Ending 2: A new friend
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C8():
    print("""You walk into an empty-looking room and look around but notice nothing but then a massive door drops down and
blocks you in. Creaking fills the room and you notice the room getting smaller. You're trapped but you still try to look for 
a way out, there's nothing. You slowly accept your fate and sit down waiting for the walls to close in on you. The inevitable 
comes and you slowly get crushed until it kills you.

Ending 3: Pancake
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C23():
    print("""You walk until you arrive at a long pile of corpses of humans and animals but you notice an exit on the other 
side of them. You decide to just go for it and start walking through them. You feel the blood seeping in through your 
clothes and the maggots wriggling around your legs almost trying to feed off your flesh. You push on and get to the exit 
but when you get there you realise you are at the place where you came in, how is this possible? 

Ending 4: There is no peace without sacrifice
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C9():
    print("""You walk into a pitch-black room with the sound of computer fans? and the door slams behind you. The lights 
turn on and you are greeted to a massive room with books and computers and many people walking around. Although there 
are many people around you are drawn to the massive wall of tv screens showing cameras monitoring the world and the maze. 
“Hello!” a man in a lab coat says to you, “you are now working for us, would you rather monitor the MAZE or the WORLD?”
     
Which do you choose?  """)
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c9
    c9 = input()
    time.sleep(2)
    if c9.upper() == "MAZE":
        pass
    elif c9.upper() == "WORLD":
        pass
    else:
        C9()


# the def statement bellow plays a part of the story using the print statement embedded
def C10():
    print(
        """“Follow me,” they say before walking off, you see a key card in his back pocket. Do you try to STEAL IT or do you LEAVE IT?""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c10
    c10 = input()
    time.sleep(2)
    if c10.upper() == "STEAL IT":
        pass
    elif c10.upper() == "LEAVE IT":
        pass
    else:
        C10()


# the def statement bellow plays a part of the story using the print statement embedded
def C11():
    print("""You arrive at a room and they put you in this chair and connect some machines to the brain. When they flick 
them on you pass out and then wake up with all the knowledge of the maze and some of the world realising it's a matrix. 
They take you to a control room and somehow you already know the ins and outs of the controls. You look through everything 
and realise there is a way to escape. This is a risky option and it might not be worth it if you are already comfortable 
with staying in the room. 
    
Do you ESCAPE or DONT ESCAPE?
""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c11
    c11 = input()
    time.sleep(2)
    if c11.upper() == "ESCAPE":
        pass
    elif c11.upper() == "DONT ESCAPE":
        pass
    else:
        C11()


# the def statement bellow plays a part of the story using the print statement embedded
def C12():
    print("You successfully got the key card!")


# the def statement bellow plays a part of the story using the print statement embedded
def C13():
    print("""You quickly edit the maze and run out of the control room, through the control building, and out back into 
the maze where you run through the path you made to a door. You go to try to open the door but the handle won’t budge but 
you see a keycard reader next to it. 
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C14():
    print("""The keycard! You quickly swipe it and rush through the door. You are back out where you entered but everything 
seems different. You walk to your house and your wife looks stunned then she starts crying and hugs you, “What's wrong?” 
you ask confused because you think that you haven’t been gone for very long. “Two years... You have been missing for two years”

Ending 5: Gone for longer than expected
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C15():
    print("""“Oh no, I can't get through” you speak to yourself. You start banging on the door but you hear a voice behind 
you “You betrayed us” you turn around and see a man pointing a gun at your head. The gun fires and splatters your brain across the walls.

Ending 6: Well that blew my mind
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C16():
    print("""You live your life in the now luxurious control room since you were shown how to edit things in the matrix 
and you realise on your screen that there is the ability to speak in someone's head and control him. 
Have I possessed them?

Ending 7: Is that a reference?
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C17():
    print("""You arrive at a room and they put you in this chair and connect some machines to the brain. When they flick 
them on you pass out and then wake up with all the knowledge of the maze and some of the world realising it's a matrix. 
You get taken to a desk in front of the wall of TVs that you saw monitoring the world and changing it however you want. 
You live the rest of your days working.

Ending 8: The word rulers
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C18():
    print("""As you are walking down the path you notice a door with a void-looking substance coming out of it. 
    
Do you ENTER or KEEP WALKING?""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c18
    c18 = input()
    time.sleep(2)
    if c18.upper() == "ENTER":
        pass
    elif c18.upper() == "KEEP WALKING":
        pass
    else:
        C18()


# the def statement bellow plays a part of the story using the print statement embedded
def C19():
    print("""You open the door as you walk in the liquid starts climbing up your leg and further up your body until it 
reaches your head and then &(FY&GF *&(*)(UF & T^#*) &^T SUF&

Ending 9: (*^F &DPF&)&F
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C20():
    print("""You keep walking till you come to two paths, as you look around the left path has a door at the end but the 
right has a bright light that is quite far away. 

Do you pick LEFT or RIGHT?""")
    # this piece of code below creates global variable, then uses an input statement to add a value to the variable.
    # Then the time sleep function helps the code run more smoothly. Then there are if statements so that only the allowed answers will be accepted
    # if the allowed answers aren't inputted it will replay the code for the choice
    global c20
    c20 = input()
    time.sleep(2)
    if c20.upper() == "LEFT":
        pass
    elif c20.upper() == "RIGHT":
        pass
    else:
        C20()


# the def statement bellow plays a part of the story using the print statement embedded
def C21():
    print("""You find yourself at the door and as you open it and walk through you realise you are back at your house 
again walking into your room and you quickly look back and only see the rest of your house.

Ending 10: What just happened
""")


# the def statement bellow plays a part of the story using the print statement embedded
def C22():
    print("""You keep walking and the bright light keeps getting brighter and brighter until you can't see anything else 
anymore but you keep walking and then you almost black out. You wake up in your bed feeling dazed.

Ending 11: Was it all a dream?
""")


print("""┌─────────┬─────────┐ 
├───┬───╴ ├───┐ ╶─┐ │ 
├─╴ │ ┌───┘ ╷ │ ╷ │ │ 
│ ╷ │ └───╴ │ └─┤ │ │ 
│ │ └─┬─────┴─╴ │ └─┤ 
│ └─┐ │ ┌─────┬─┴─╴ │ 
│ ╷ └─┤ │ ╶─┐ │ ╶─┐ │ 
│ └─┐ ╵ └─╴ │ └─╴ │ │ 
└───┴───────┴─────┴─┘  """)
# This is where I start my code and use if statements and my def variables to properly navigate the story
intro()
if c.upper().strip() == "RIGHT":
    C1()
    if c1.upper().strip() == "SEARCH":
        C3()
        if c3.upper().strip() == "LEFT":
            C4()

            if c4.upper().strip() == "STRAIGHT":
                C5()
                C67()
            elif c4.upper().strip() == "LEFT":
                C8()
            elif c4.upper().strip() == "RIGHT":
                C23()
        elif c3.upper().strip() == "RIGHT":
            C9()
            if c9.upper().strip() == "MAZE":
                C10()
                if c10.upper().strip() == "STEAL IT":
                    C12()
                    inventory.append("Key Card")
                C11()
                if c11.upper().strip() == "ESCAPE":
                    C13()
                    if "Key Card" in inventory:
                        C14()
                    else:
                        C15()
                elif c11.upper().strip() == "DONT ESCAPE":
                    C16()

            if c9.upper().strip() == "WORLD":
                C17()

    elif c1.upper().strip() == "KEEP WALKING":
        C2()

elif c.upper().strip() == "LEFT":
    C18()
    if c18.upper().strip() == "ENTER":
        C19()
    elif c18.upper().strip() == "KEEP WALKING":
        C20()
        if c20.upper().strip() == "LEFT":
            C21()
        elif c20.upper().strip() == "RIGHT":
            C22()
