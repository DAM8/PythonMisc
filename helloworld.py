print("hello world!")

msg = "this is 2nd part of hello"
print(msg)

#list
fruits = ['apple','mango', 'orange']
first_fruit = fruits[0]
last_fruit	= fruits[-1]

fname= 'reddy'
lname= 'buddy'
fname= fname + ''+ lname
print("concatenation of fruits is", fname)

for i in fruits:
	print(i)

#fruits = []
fruits.append('blueberry')

print('4th print', fruits)	


squares = []
for i in range(1,11):
	squares.append(i**2)

print( '5th', squares)

compsquare = [ i**3 for i in range(1,9)]
print('6th', compsquare)

fruits_sliced = fruits[:5 ]
print('7th', fruits_sliced)			

fruitslist = fruits[:]
print('8th', fruitslist)

#tuples
dimensions = (1920, 1080)
print('9th', dimensions)

cars = { 'car': 'ferrai', 'cost': '$10'}
print('10th', cars)
print('11th', cars['cost'])

fav_sports = {'mgr': 'Cricket', 'kevin': 'Baseball'}

#looping through all the key value pairs
#keyvalue, then fav_sports.items():
#key, then fav_sports.keys():
#value, then fav_sports.values():
for name, game in fav_sports.items():
	print(name +' '+ 'loves' +' '+ game)

#User Input value
name = input("what's your name?")
print('Myname is' +name)

#function with arguments
def greet_user(username):
	print("Hello" +username)
greet_user("Jaffa")	

#default values
def car_model(model='Ferrai'):
	print("Your favorite car is" +model)
car_model()
car_model('Benz')
car_model('BMW')	

	

