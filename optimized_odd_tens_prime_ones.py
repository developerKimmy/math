import math

min_value = 20
max_value = 150
BASE = 10 

def find_odd_tens(min_value, max_value, BASE):
    # 10의 배수 찾기
    start = ((min_value - 1) // BASE + 1) * BASE
    
    for i in range(start, max_value + 1, BASE):
        print(i)
    
print(find_odd_tens(min_value, max_value, BASE))

