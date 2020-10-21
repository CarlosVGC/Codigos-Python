import time

def suma():
    for a in range(100):
        a+=a
        print(f'La suma es:{a}')
        time.sleep(1)
        
def resta():
    for a in range(100):
        a-=a
        print(f'La resta es:{a}')
        time.sleep(1)

def mul():
    for a in range(100):
        a*=a
        print(f'La mult es:{a}')
        time.sleep(1)