import turtle

def main():
    def square (name, times):

        for i in range(times):
            name.begin_fill()
            for i in range(4):
                name.color("#0000CD")
                name.forward(50)
                name.left(90)

            name.end_fill()
            name.penup()
            name.forward(80)
            name.pendown()
    def rectangle (annyong, t):
        for i in range(t):
            annyong.begin_fill()
            for i in range(2):
                annyong.forward(50)
                annyong.left(90)
                annyong.forward(60)
                annyong.left(90)
            annyong.end_fill()
            annyong.penup()
            annyong.forward(80)
            annyong.pendown()

    wn = turtle.Screen()
    wn.bgcolor("#E0FFFF")
    wn.screensize(2000,2000)
    mom = turtle.Turtle()
    mom.color("#0000CD")
    square(mom,4)
    rectangle(mom,5)
    wn.bye()

    Ans = input("How many squares are there?  ")

    if Ans == "4" :
        print("Congratulations! There are 4 squares.")
    else:
        print("Try again! You can do it!")

main()
