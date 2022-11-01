# import required modules
import turtle
import time
import random

delay = 0.1
score1 = 0
score2 = 0
# high_score = 0



# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake 1
head1 = turtle.Turtle()
head1.shape("square")
head1.color("white")
head1.penup()
head1.goto(0, 0)
head1.direction = "Stop"

# head of the snake 2
head2 = turtle.Turtle()
head2.shape("square")
head2.color("red")
head2.penup()
head2.goto(0, 0)
head2.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 Snake№2 score: 0 ", align="center",
		font=("candara", 24, "bold"))



# assigning key directions for snake1
def goup():
	if head1.direction != "down":
		head1.direction = "up"


def godown():
	if head1.direction != "up":
		head1.direction = "down"


def goleft():
	if head1.direction != "right":
		head1.direction = "left"


def goright():
	if head1.direction != "left":
		head1.direction = "right"


# assigning key directions for snake2
def go2up():
	if head2.direction != "down":
		head2.direction = "up"


def go2down():
	if head2.direction != "up":
		head2.direction = "down"


def go2left():
	if head2.direction != "right":
		head2.direction = "left"


def go2right():
	if head2.direction != "left":
		head2.direction = "right"


def move():
	if head1.direction == "up":
		y = head1.ycor()
		head1.sety(y+20)
	if head1.direction == "down":
		y = head1.ycor()
		head1.sety(y-20)
	if head1.direction == "left":
		x = head1.xcor()
		head1.setx(x-20)
	if head1.direction == "right":
		x = head1.xcor()
		head1.setx(x+20)

def move2():
	if head2.direction == "up":
		y = head2.ycor()
		head2.sety(y+20)
	if head2.direction == "down":
		y = head2.ycor()
		head2.sety(y-20)
	if head2.direction == "left":
		x = head2.xcor()
		head2.setx(x-20)
	if head2.direction == "right":
		x = head2.xcor()
		head2.setx(x+20)


		
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

wn.onkeypress(go2up, "Up")
wn.onkeypress(go2down, "Down")
wn.onkeypress(go2left, "Left")
wn.onkeypress(go2right, "Right")


segments1 = []
segments2 = []




# Main Gameplay
while True:
	wn.update()
	if head1.xcor() > 290 or head1.xcor() < -290 or head1.ycor() > 290 or head1.ycor() < -290:
		# time.sleep(1)
		head1.goto(0, 0)
		head1.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for segment in segments1:
			segment.goto(1000, 1000)
		segments1.clear()
		score1 = 0
		delay = 0.1
		pen.clear()
		pen.write("Score: {} Snake№2 score: {} ".format(
			score1, score2), align="center", font=("candara", 24, "bold"))

	if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
		# time.sleep(1)
		head2.goto(0, 0)
		head2.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for segment in segments2:
			segment.goto(1000, 1000)
		segments2.clear()
		score2 = 0
		delay = 0.1
		pen.clear()
		pen.write("Score: {} Snake№2 score: {} ".format(
			score1, score2), align="center", font=("candara", 24, "bold"))

	if head1.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments1.append(new_segment)
		delay -= 0.001
		score1 += 10
		# if score > high_score:
		# 	high_score = score
		pen.clear()
		pen.write("Score: {} Score: {} ".format(
			score1, score2), align="center", font=("candara", 24, "bold"))
	if head2.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		segments2.append(new_segment)
		delay -= 0.001
		score2 += 10
		# if score > high_score:
		# 	high_score = score
		pen.clear()
		pen.write("Score: {} Score: {} ".format(
			score1, score2), align="center", font=("candara", 24, "bold"))

	# Checking for head collisions with body segments
	for index in range(len(segments1)-1, 0, -1):
		x = segments1[index-1].xcor()
		y = segments1[index-1].ycor()
		segments1[index].goto(x, y)
	if len(segments1) > 0:
		x = head1.xcor()
		y = head1.ycor()
		segments1[0].goto(x, y)

	# Checking for head collisions with body segments
	for index in range(len(segments2)-1, 0, -1):
		x = segments2[index-1].xcor()
		y = segments2[index-1].ycor()
		segments2[index].goto(x, y)
	if len(segments2) > 0:
		x = head2.xcor()
		y = head2.ycor()
		segments2[0].goto(x, y)
	move()
	move2()
	for segment in segments1:
		if segment.distance(head1) < 20:
			# time.sleep(1)
			head1.goto(0, 0)
			head1.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments1:
				segment.goto(1000, 1000)
			segment.clear()

			score1 = 0
			delay = 0.1
			pen.clear()
			pen.write("Score: {} Snake№2 score:  {} ".format(
				score1, score2), align="center", font=("candara", 24, "bold"))

	for segment in segments2:
		if segment.distance(head2) < 20:
			# time.sleep(1)
			head2.goto(0, 0)
			head2.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments2:
				segment.goto(1000, 1000)
			segment.clear()

			score2 = 0
			delay = 0.1
			pen.clear()
			pen.write("Score: {} Snake№2 score:  {} ".format(
				score1, score2), align="center", font=("candara", 24, "bold"))
	time.sleep(delay)

wn.mainloop()
