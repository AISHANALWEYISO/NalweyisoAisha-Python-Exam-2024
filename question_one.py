# N0.1(i)

def circle_area():
    radius = int(input("Enter the radius of the circle: "))
    pie = 3.14
    area = pie * radius **2
    print(f"The area of the circle is : {area:.3f}")
circle_area()    

#N0.1(ii)

list = [4,7,2,9,12,15]
odd_sum =0 
for num in list:
    if num% 2 !=0: 
        odd_sum+=num 
print(odd_sum)    



#N0.1(iii)
def operations(num1, num2):
    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "quotient": num1 / num2
    }

results = operations(8, 4)
print(results) 
   
        
#N0.1(iv)
student_info = {
    'name':'Alice',
    'age':20,
    'grade':'A'
}
student_info['age']=26 #updating age with 26
print(student_info)

student_info['city']='Kampala' #adding key-value pair for city-kampala
print(student_info)