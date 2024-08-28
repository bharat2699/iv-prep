def this_is_a_decorator(func):
    def inner():
        print("start")
        func()
        print("end") 
        return inner

    return this_is_a_decorator


@this_is_a_decorator()
def func():
    print("hi")
    
print(func())
