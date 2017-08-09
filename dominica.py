import random
import turtle

fallen_item = turtle.clone()
turtle.penup()
size_x = 800
size_y = 700
turtle.setup(size_x,size_y)
square_size = 20
good_food = ["apple.gif", "banana.gif", "strawberry.gif", "orange.gif", "grape.gif"]
good_food_clone=[]
bad_food = ["bad_apple.gif", "bad_banana.gif", "bad_strawberry.gif", "bad_orange.gif"]
bad_food_clone=[]
war_items = ["gun", "handbomb", "rocket", "soldjier"]
war_items_clone=[]

food_clones = []

r = random.randint(0, len(war_items) - 1)
random_thing = war_items[r]
rx = random.randint(-390,390)
war_items.goto(rx, 300)
war_items.showturtle()
farmer_xpos = farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
fallen_item_xpos = c.pos()[0]
fallen_item_ypos = c.pos()[1]


##down_edge = -350
##
##while fallen_item_ypos >= down_edge:
##    fallen_item.goto(fallen_item_xpos, fallen_item_ypos - 20)






for n in range(len(a)):
##    turtle.register_shape(food_list[n])
    obj = turtle.clone()
    obj.hideturtle()
    food_clones.append(obj)
    obj.shape(a[n])

def set_up(food_clones):
    """
    For every clone in the list,
    it will position it at random
    positions along a horizontal line
    at y = 200
    """
    taken_x = []
    for clone in food_clones:
        # makes sure to generate random non-overlapping positions
        multiple = random.randint(0, 24)
        random_x = -370 + (30 * multiple)
        while random_x in taken_x:
            multiple = random.randint(0, 24)
            random_x = -370 + (30 * multiple)
        # make visible changes and record the random_x
        clone.showturtle()
        clone.goto(random_x, 200)
        taken_x.append(random_x)
        
        


set_up(food_clones)


def make_food(y):
    min_x=int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    food_x=random.randint(min_x,max_x)*square_size
    food.goto(food_x)
    food_pos.append((food_x,food_y))
    f= food.stamp()
    food_stamp.append (f)
    
##for i in range(len(names)):
##    print(names[i])
