import sys
def collatz(number):
    if number %2==0:
        return number //2
    else:
        return 3 * number+1
try:
    while True:

        userInput=int(input())
        print(collatz(userInput))

except KeyboardInterrupt:
    sys.exit()
except ValueError:
    print('only integers')
    print(collatz(userInput))
