# python program to intiating class
class Dog:
    # a simple class attribute
    attr1="mamal"
    attr2="dog"

    # a simple method
    def nag(str):
        print("i am",str.attr1)
        print("i am ",str.attr2)

# driver code
# object intiation 
Rodger = Dog()

#accesing class attributes 
# and method through objects 
print(Rodger.attr1)
Rodger.nag()
