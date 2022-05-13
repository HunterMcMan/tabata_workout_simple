import time
def start_workout():
    print("Hello! Welcome to the Tabata Timer!")
    print("-----------------------------------")
    start = input("To start, please type 'start'")
    if start == "start":
        print("Your workout will start in 5 seconds")
        for timer in range(5,0,-1):
            print(timer)
            time.sleep(1)
def workout():
    print("Exercise for 20 seconds!")
    for exercise in range(20,0,-1):
        print(exercise)
        time.sleep(1)
    print("Rest for 10 seconds!")
    for rest in range(10,0,-1):
        print(rest)
        time.sleep(1)
workout()
workout()
workout()
workout()
workout()
workout()
workout()
workout()
print("-----------------------------------")
print("Congratulations! You completed this workout!")

