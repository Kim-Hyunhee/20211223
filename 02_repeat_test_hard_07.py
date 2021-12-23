# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 변수 만들기
my_num_list = []

# for로 6회 반복
for i in range(6):
    input_num = int(input(f'{i+1}번째 숫자 입력 : '))
    
    # 입력 받은 숫자를 목록에 추가
    my_num_list.append(input_num)
    
# test - 목록에 뭐가 들어있는지 출력
print(my_num_list)