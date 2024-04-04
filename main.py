help = ("start - to start the car\nstop - to stop car\nquit - to exit")
start=("car started.....you are ready to go...press number 1-6 to change gear")
stop=("car stoped.")
x=""
b=""
i=0


while x != "quit":
    x = input("> ")
    if x== "start":
        print(start)
        while i <= 6:
            i=i+1
            g=int(input())


            if g ==1:
                print("your speed has reached 20 change gear")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 1:
                print("car has stoped")


            if g ==2:
                print("your speed has reached 30 change gear")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 2:
                print("car speed is now 20")
            if g ==3:
                print("your speed has reached 40 change gear")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 3:
                print("car speed is now 30")
            if g ==4:
                print("your speed has reached 60 change gear")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 4:
                print("car speed is now 40")
            if g ==5:
                print("your speed has reached 80 change gear")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 5:
                print("car speed is now 60")
            if g ==6:
                print("your speed range is 80 - 220 drive safely")
                b = input("press b if you wish to apply breaks: ")
            if b == "b" and g == 6:
                    print("car speed is now 80")
    elif x == "stop":
        print(stop)
    elif x == "help":
        print(help)
    elif x == "quit":
        break
    else:
        print("i dont understand that")

