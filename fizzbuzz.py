import sys

userinput = sys.argv[1:]

if userinput:
    print("FizzBuzz is counting from {}".format(sys.argv[1]))
    print("FizzBuzz is counting until {}".format(sys.argv[2]))
    minimum = int(sys.argv[1])
    maximum = int(sys.argv[2])

else:
    minimum = input("What number should FizzBuzz start at?")
    maximum = input("How high do you want FizzBuzz to count today?")
    print("FizzBuzz counting up to", maximum)

for i in range(minimum,maximum):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print (i)