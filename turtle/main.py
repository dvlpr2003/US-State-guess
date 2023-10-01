import turtle
import pandas 

screen = turtle.Screen()
tur = turtle.Turtle()
screen.setup(800,600)
screen.bgpic("./blank_states_img.gif")
csv = pandas.read_csv("./50_states.csv")
states = csv["state"]
state_list = []
Entered_states = []
for _ in states :
    state_list.append(_)
print(states)

game_on = True
while game_on:
    try:



        answer = str(screen.textinput("Welcome to US State finder", "Are you ready to find out !"))
        if answer in Entered_states:
            continue
        

        state_index =state_list.index(answer)
        print(state_index)

        print(answer)
        x = csv["x"]
        y = csv["y"]
        x_pos = x.get(state_index)
        y_pos = y.get(state_index)
        print(f"x position {x_pos}")
        print(f"y position {y_pos}")
        tur.up()
        tur.hideturtle()
        tur.goto(x_pos,y_pos)
        tur.write(f"{answer}", move=False, align='center', font=('Arial', 8, 'normal'))
        Entered_states.append(answer)


    except:
        print("wrong input")
        game_on = False
screen.exitonclick()