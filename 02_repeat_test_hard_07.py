# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 변수 만들기
my_num_list = []

# for로 6회 반복
for i in range(6):
    
    # 제대로 된 숫자가 올 때까지 해당 위치의 숫자를 다시 입력 받아야함
    # 언제까지 제대로 된 숫자를 넣을 지 모르니까 무한 반복 => 제대로 된 숫자면 break
    
    while True:
        input_num = int(input(f'{i+1}번째 숫자 입력 : '))

        # 받은 숫자(input_num)가 목록에 추가해도 되는 숫자인지 검사 => 통과 할 때만 추가하자
        # 기준 1. 1 ~ 45 이내의 숫자가 맞는가?

        if 1 <= input_num and input_num <= 45:
            # 입력 받은 숫자를 목록에 추가
            my_num_list.append(input_num)
            # 무한 반복 종료 => 다음 숫자 받으러 이동
            break
    
# test - 목록에 뭐가 들어있는지 출력
print(my_num_list)