import  pickle
from hw14 import Employee

input = open('data.pkl', 'rb')
obj = pickle.load(input)
obj.print_salary_info()
input.close()