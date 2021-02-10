import  pickle

input = open('data.pkl', 'rb')
obj = pickle.load(input)
print(obj)
input.close()