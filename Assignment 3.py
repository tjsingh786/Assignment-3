#ques 1.
Rainbow=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow)

#ques 2.
company=['google','apple','facebook','microsoft','tesla']
new=company+Rainbow
print(new)

#ques 3
numbers=[1,2,1,3,1,4,1,5,1,6,1]
print(numbers.count(1))

#ques 4
num=[9,8,7,6,5,4,3,2,1]
num.sort()
print(num)

#ques 5
a = [1,2,3,4,5]
b = [6,7,8]
c=a+b
c.sort()
print(c)

#ques 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count1=0
count2=0
for i in numbers:
        if not i % 2:
            count1=count1+1
        else:
            count2=count2+1
print("Number of even numbers:",count1)
print("Number of odd numbers:",count2)

#Tuple ques

#ques 1.
x=("1,2,3")
y=reversed(x)
print(tuple(y))

#ques 2
num = [1,3,2,8,5,10,6]
print('Maximum is:',max(num))
print('Minimum is:',min(num))

#string ques

#ques 1.
string="python class"
print(string.upper())

#ques 2.
str="hello009"
print (str.isnumeric())

#ques 3.
string='Hello world'
print (string.replace('world','Tajinder'))


