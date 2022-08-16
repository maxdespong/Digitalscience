import time


def intro():
    print("""Welcome to my texted based game called The Maze. Be careful because all decisions are final.

It's a cold autumn afternoon in a small town in Kentucky, you have decided to go on a walk to clear your head. 
You notice a weird opening in a field but decide to ignore it but as you are walking away something calls your
name from where it was. You quickly rush to it to see if someone was in danger but no one was there. You look
around your surrounding confused and your eyes go to the opening which seems to go for a while, as you are 
contemplating whether to go your name is called from inside the opening so you run into the opening trying 
to find the person but a door which didn't seem to be there before quickly shut behind you. As you look 
around desperately you realise that there is no way back the way you came, but you do notice an inscription 
on the wall in the shape of a maze. This is when you look around and notice that there are two paths ahead of 
you and it clicks, you are stuck in a maze. 
Type 'Continue' to got to the next part
    """)
    c = input()
    time.sleep(2)
    if c.upper() == "CONTINUE":
        pass
    else:
        intro()


inventory = []


def C1():
    print("""As you are walking through the path you chose on your trip on a pile of clutter, you have minimal vision
but it looks like rotten food and old clothing. It smells terrible but there might be something that will help. 
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
    print("""You venture forward using the rough concrete wall as a guide, you feel your foot lose flooring and realise
there is a massive hole ahead of you but it's too late and you fall down losing consciousness when you hit the bottom. 
As you wake back up a massive shock of pain hits you and you sit up looking at your mangled legs. Your head shoots up 
because you see movement in the top of your eyes and see a massive creature come towards you. You try to move away but 
your arms are strong enough to move your body and you realise the creature is a spider. It walks up to you and picks 
you up and starts wrapping you up in its webs, they eventually cover your head which causes you to suffocate and die.

Ending 0: Well that was fast""")

def C3():



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
if c1.upper() == "SEARCH":
    inventory.append("Flashlight")
    C3()
elif c1.upper() == "KEEP WALKING":
    C2()
