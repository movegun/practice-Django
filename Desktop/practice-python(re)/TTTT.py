
# list=[0,1,2,3,4,5,6,7,8,9]
lista=['A','B','C','D','E']

def start():
    for i in lista.copy():
        print("i",i)
        lista.remove(i)
        
        
        
        # print(i)


print("지우기전",lista)
start()
print("지운 후", lista)