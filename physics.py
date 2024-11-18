from os import times


def a():
    power = float(input("what is the power?"))
    time = float(input("what is the time?"))
    energy = power*times
    print(energy)


def b():
    print("speed = distance/time")
    distance = float(input("what is the distance?"))
    time = float(input("what is the time?"))
    speed = distance/time
    print(speed)

def c():
    print("distance = speed*time")
    speed = float(input("what is the speed?"))
    time = float(input("what is the time?"))
    distance = (speed*time)
    print(distance)

def d():
    print("acceleration = mass*velocity")
    mass = float(input("what is the mass?"))
    velocity = float(input("what is velocity?"))
    acceleration = mass*velocity
    print(acceleration)

def e():
    print("weight = mass*gravity")
    mass = float(input("what is the mass?"))
    gravity = float(input("what is the gravity?"))
    weight = mass*gravity
    print(weight)

def main():
    choice = input("what question do you want to perform?")
    if choice == "a":
        a()
    elif choice == "b":
        b()
    elif choice == "c":
        c()
    elif choice == "d":
        d()
    elif choice == "e":
        e()
    else:
        print('invalid input')


if __name__ == '__main__':
    main()
