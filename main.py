import time


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
    global c
    c = input()
    time.sleep(2)
    if c.upper() == "RIGHT":
        pass
    if c.upper() == "LEFT":
        pass
    else:
        intro()


inventory = []


def C1():
    print("""As you are walking through the path you chose on your trip on a pile of clutter, you have minimal vision but 
it looks like rotten food and old clothing. It smells terrible but there might be something that will help.
 
Do you SEARCH through it or KEEP WALKING?
     """)
    global c1
    c1 = input()
    time.sleep(2)
    if c1.upper() == "SEARCH":
        pass
    elif c1.upper() == "KEEP WALKING":
        pass
    else:
        C1()


def C2():
    print("""You venture forward using the rough concrete wall as a guide, you feel your foot loose flooring and realise 
there is a massive hole ahead of you but it's too late and you fall, losing consciousness when you hit the bottom. As you 
wake back up a massive shock of pain hits you and you sit up looking at your mangled legs. Your head shoots up because you 
see movement in the top of your eyes and see a massive creature come towards you. You try to move away but your arms are strong 
enough to move your body and you realise the creature is a spider. It walks up to you and picks you up and starts wrapping you 
up in its webs, they eventually cover your head which causes you to suffocate and die.

Ending 0: Well that was fast""")


def C3():
    print("""You stick your hand into the pile which feels oddly warm and you find a flashlight which you pick up and turn
on to continue looking through the pile but you find nothing else. You use the torch to look ahead of you and notice a 
massive pit with a bridge going over it. You walk across the bridge and look down and see a lot of bodies strung up by 
spider webs. As you look ahead you see a man standing in front of two doors “to my LEFT you will find what the heart 
desires but to the RIGHT  is what your mind craves, pick carefully but no matter what option I'll never give you up or let you down”

Which door do you choose?
    """)
    global c3
    c3 = input()
    time.sleep(2)
    if c3.upper() == "LEFT":
        pass
    elif c3.upper() == "RIGHT":
        pass
    else:
        C3()


def C4():
    print("""You are greeted by 3 paths, STRAIGHT, LEFT, and RIGHT but you are also greeted by a horrible stench carried 
    by a breeze from the right path. 
    
    Which path do you pick?""")
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


def C5():
    print("""You walk straight for a while and find yourself at an altar, as you look at it you notice some demonic-looking 
    symbols and some ritual gear. As you look more around the altar a door closes the path you came from. Suddenly you hear 
    hundreds of footsteps and notice you're surrounded by people in almost cult uniforms. Then one speaks up “we are for the truth, 
    the freedom will you join us?” 
    
    Do you JOIN the members or DONT JOIN?""")
    global c5
    c5 = input()
    time.sleep(2)
    if c5.upper() == "JOIN":
        pass
    elif c5.upper() == "DONT JOIN":
        pass
    else:
        C5()


def C67():
    print("""They quickly rush to you and manhandle you onto the altar and strap you down so you can't move. The leader 
of the cult moves forward to you chanting something in a language you have never heard before and picking up an ancient-looking 
dagger, is this my death? He holds it up to your chest and carves a pentagram but then he pulls out a weird-looking powder and 
sprinkles it into the wound. The pain is so unbearable that you pass out. When you regain consciousness you feel different 
and there is no one around then you hear a voice… coming from my head? “Hello there” 

Ending 2: A new friend
""")


def C8():
    print("""You walk into an empty-looking room and look around but notice nothing but then a massive door drops down and
blocks you in. Creaking fills the room and you notice the room getting smaller. You're trapped but you still try to look for 
a way out, there's nothing. You slowly accept your fate and sit down waiting for the walls to close in on you. The inevitable 
comes and you slowly get crushed until it kills you.

Ending 3: Pancake
""")


def C23():
    print("""You walk until you arrive at a long pile of corpses of humans and animals but you notice an exit on the other 
side of them. You decide to just go for it and start walking through them. You feel the blood seeping in through your 
clothes and the maggots wriggling around your legs almost trying to feed off your flesh. You push on and get to the exit 
but when you get there you realise you are at the place where you came in, how is this possible? 

Ending 4: There is no peace without sacrifice
""")


def C9():
    print("""You walk into a pitch-black room with the sound of computer fans? and the door slams behind you. The lights 
turn on and you are greeted to a massive room with books and computers and many people walking around. Although there 
are many people around you are drawn to the massive wall of tv screens showing cameras monitoring the world and the maze. 
“Hello!” a man in a lab coat says to you, “you are now working for us, would you rather monitor the MAZE or the WORLD?”
     
Which do you choose?  """)
    global c9
    c9 = input()
    time.sleep(2)
    if c9.upper() == "MAZE":
        pass
    elif c9.upper() == "WORLD":
        pass
    else:
        C9()


def C10():
    print(
        """“Follow me,” they say before walking off, you see a key card in his back pocket. Do you try to STEAL IT or do you LEAVE IT?""")
    global c10
    c10 = input()
    time.sleep(2)
    if c10.upper() == "STEAL IT":
        pass
    elif c10.upper() == "LEAVE IT":
        pass
    else:
        C10()

def c11():
    print("""You arrive at a room and they put you in this chair and connect some machines to the brain. When they flick 
them on you pass out and then wake up with all the knowledge of the maze and some of the world realising it's a matrix. 
They take you to a control room and somehow you already know the ins and outs of the controls. You look through everything 
and realise there is a way to escape. This is a risky option and it might not be worth it if you are already comfortable 
with staying in the room. 
    
Do you ESCAPE or DONT ESCAPE?
""")


def c12():
    print("You successfully got the key card!")


print("""┌─────────┬─────────┐ 
├───┬───╴ ├───┐ ╶─┐ │ 
├─╴ │ ┌───┘ ╷ │ ╷ │ │ 
│ ╷ │ └───╴ │ └─┤ │ │ 
│ │ └─┬─────┴─╴ │ └─┤ 
│ └─┐ │ ┌─────┬─┴─╴ │ 
│ ╷ └─┤ │ ╶─┐ │ ╶─┐ │ 
│ └─┐ ╵ └─╴ │ └─╴ │ │ 
└───┴───────┴─────┴─┘  """)
intro()
C1()
if c.upper == "RIGHT":
    if c1.upper() == "SEARCH":
        inventory.append("Flashlight")
        C3()
        if c3.upper() == "LEFT":
            C4()
            if c4.upper() == "STRAIGHT":
                C5()
                C67()
            elif c4.upper == "LEFT":
                C8()
            elif c4.upper() == "RIGHT":
                C23()
        elif c3.upper() == "RIGHT":
            C9()
            if c9.upper() == "MAZE":
                C10()
                if c10.upper() == "STEAL IT":
                    c12()
                    inventory.append("Key Card")
                C11()

            if c9.upper() == "WORLD":

    elif c1.upper() == "KEEP WALKING":
        C2()
