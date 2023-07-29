users = ['Bhavya', 'Rajesh', 'Mary']

k = [i for i in users if len(i)>3 and i.startswith('M')]
print(k)