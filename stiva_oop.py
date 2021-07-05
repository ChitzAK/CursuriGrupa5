class Stack:

    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)
        # return self.__stackList

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        print(self.__stackList)
        self.val = val

    def __str__(self):
        return self.val


class AddingStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def getSum(self):
        return self.__sum


stack_object = AddingStack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.getSum())
# print(len(stack_object.stackList))