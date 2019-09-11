class MyClass:
    def __init__(gr, name, age):
        gr.n= name
        gr.a = age
    def myfunc(jaf):
        print("Hello my name is " + jaf.n)
    def myage(age):
        print("My age is " + str(age.a))
    
# p1 = MyClass("greddy", 31)
# # print(p1.n)
# # print(p1.a)
# p1.myfunc()
# p1.myage()
# # p1.a = 888
# # del p1.a
# # del p1
# print(p1.a)

class Jaffa(MyClass):
    def __init__(this, fname1, lname1, year):
        # this.name = vname
        # this.age= vage
        # MyClass.__init__(self, fname, lname)
        super().__init__(fname1, lname1)
        this.thisyear = year

    def addnewmethod(self):
        print("This is how we can add new methods", self.n, self.a, "and new obj property can be added as", self.thisyear)     

jobj = Jaffa("Ram", 30, 2019)
# print(jobj.thisyear)
# jobj.myfunc()
jobj.addnewmethod()