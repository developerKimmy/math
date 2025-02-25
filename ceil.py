import math

# 1 부터 50까지 7의 배수를 구하는 방법
# 매개 변수 
min_value = 1
max_value = 50
divisor = 7

def find_multiples(min_value, max_value, divisor):
    min_multiple = math.ceil(min_value/divisor);
    max_multiple = math.floor(max_value/divisor);
    number_of_multiples = (max_multiple - min_multiple) + 1;
    return number_of_multiples

print(f"총 {find_multiples(min_value, max_value, divisor)}개의 배수가 들어있습니다.")


