import random

# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 변수 만들기
my_num_list = []

# for로 6회 반복
for my_num in range(6):
    
    # 제대로 된 숫자가 올 때까지 해당 위치의 숫자를 다시 입력 받아야함
    # 언제까지 제대로 된 숫자를 넣을 지 모르니까 무한 반복 => 제대로 된 숫자면 break
    
    while True:
        input_num = int(input(f'{my_num+1}번째 숫자 입력 : '))

        # 받은 숫자(input_num)가 목록에 추가해도 되는 숫자인지 검사 => 통과 할 때만 추가하자
       
        # 기준 1. 1 ~ 45 이내의 숫자가 맞는가?
        is_range_ok = input_num in range( 1, 46 )  # 1 ~ 45 범위에 있는가?
        
        # 기준 2. 중복이 아닌가?
        # 기준 2. 이미 등록된 숫자인가? 중복이 아니어야만 목록에 추가 가능
            # my_num_list 내부의 숫자들을 하나씩 꺼내보자 => input_num과 같은 숫자 발견하면? => 중복 검사 탈락 => 다시 입력 받아야함
            
        is_duplicated = input_num in my_num_list   # 등록된 숫자에 입력한 숫자가 있는가?  => 있다면 중복
        
        # 범위 OK 이고, 중복은 아니어야 목록에 추가
        
        if is_range_ok and not is_duplicated:    
            # 입력 받은 숫자를 목록에 추가
            my_num_list.append(input_num)
            # 무한 반복 종료 => 다음 숫자 받으러 이동
            break
    
# 임시 - 고정된 6개 숫자를 내 번호로 활용
# my_num_list = [5, 1, 16, 4, 42, 23]

# test - 목록에 뭐가 들어있는지 출력
print(my_num_list)

# 파이썬 list의 기능으로 정렬
my_num_list.sort()

# 정렬 결과 확인
print(my_num_list)


# 당첨 번호 6개를 생성 (랜덤 생성)

win_num_list = random.sample(range(1, 46), 6)

win_num_list.sort()

print(f'당첨 번호 목록 : {win_num_list}')


# 내 번호와 담청 번호 비교 => 같은 숫자가 몇개나 있나?
# 반복문 중첩 활용

correct_count = 0

for my_num in my_num_list:
    
    for win_num in win_num_list:
        
        # 내 번호 하나를 들고 당첨 번호를 둘러보다가 같은 숫자를 발견했나요?
        if my_num == win_num:
            # 구해야 할 것 : 몇 개를 맞췄는가? 맞출 때마다 맞춘 갯수 1 증가
            correct_count = correct_count + 1
            
# 찾아낸 같은 숫자의 갯수 파악 가능

if correct_count == 6:
    print('1등 당첨')
elif correct_count == 5:
    print('3등 당첨')            
elif correct_count == 4:
    print('4등 당첨')
elif correct_count == 3:
    print('5등 당첨')
else:
    print('꽝')