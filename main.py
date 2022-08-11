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
    c1 = input()
    time.sleep(2)
    if c1.upper() == "CONTINUE":
        pass
    else:
        intro()

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
