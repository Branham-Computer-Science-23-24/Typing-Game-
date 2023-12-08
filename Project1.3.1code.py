import turtle as trtl

Background = "Gru_House.gif" 
minion = "Dave+Run.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(Background) # Make the screen aware of the new file
wn.bgpic("Gru_House.gif")

wn.bgpic("Dave+Run.gif")
Gru = trtl.Turtle()
minion = trtl.Turtle()


wn.mainloop  
