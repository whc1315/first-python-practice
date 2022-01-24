# 1
def hello_world():
    print("Hello World")


hello_world()

# 2


def printName(name):
    print(name)


printName('Cameron')

# 3


def greeting(name):
    print("Hello " + name + "!")


greeting('Lukas')

# 4


def add(num1, num2):
    print(num1 + num2)


sum = add(20, 30)

# 5


def nameCheck(name):
    if name == 'Steven':
        print('What is up Steven?')
    elif name == 'Bryan':
        print('Hey Bryan!')
    else:
        print('Cool name, ' + name + '!')


nameCheck('Steven')
nameCheck('Bryan')
nameCheck('Will')

# 6


def faveColorFinder(color):
    if color == 'red':
        print('Red is a great color!')
    elif color == 'green':
        print('Green is a solid color!')
    elif color == 'black':
        print('So trendy!')
    else:
        print('You need to reevaluate your color choice!')


colorRating = faveColorFinder('red')

# 7

listOfNames = ['Bob', 'Will', 'Ryan', 'Steve', 'Matt', 'Tig']


def printAllNames(list):
    for list in listOfNames:
        print(list)


printAllNames(listOfNames)

# 8


def thatsOdd(num):
    if num % 2 == 0:
        print('Thats not odd!')
    else:
        print('Thats odd indeed!')


oddChecker = thatsOdd(4)

# 9

nums = [100, 200, 12, 15, 55, 101, 99, 87]


def bigOrSmall(nums):
    answers = []
    for x in nums:
        if x > 100:
            answers.append('big')
        else:
            answers.append('small')
    listEvaluator = answers
    print(listEvaluator)


bigSmallResults = bigOrSmall(nums)

# 10

contestants = ['Bob', 'Will', 'Ryan', 'Steve', 'Matt', 'Tig', 'Derek', 'Mark']

loser = ['Steve']


def theEliminator(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                list1.remove(x)
    newContestants = list1
    print(newContestants)


theEliminator(contestants, loser)
