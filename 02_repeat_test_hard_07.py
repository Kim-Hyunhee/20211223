import random

# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 변수 만들기
my_num_list = []

# for로 6회 반복
# for my_num in range(6):
    
#     # 제대로 된 숫자가 올 때까지 해당 위치의 숫자를 다시 입력 받아야함
#     # 언제까지 제대로 된 숫자를 넣을 지 모르니까 무한 반복 => 제대로 된 숫자면 break
    
#     while True:
#         input_num = int(input(f'{i+1}번째 숫자 입력 : '))

#         # 받은 숫자(input_num)가 목록에 추가해도 되는 숫자인지 검사 => 통과 할 때만 추가하자
       
#         # 기준 1. 1 ~ 45 이내의 숫자가 맞는가?
#         is_range_ok = input_num in range( 1, 46 )  # 1 ~ 45 범위에 있는가?
        
#         # 기준 2. 중복이 아닌가?
#         # 기준 2. 이미 등록된 숫자인가? 중복이 아니어야만 목록에 추가 가능
#             # my_num_list 내부의 숫자들을 하나씩 꺼내보자 => input_num과 같은 숫자 발견하면? => 중복 검사 탈락 => 다시 입력 받아야함
            
#         is_duplicated = input_num in my_num_list   # 등록된 숫자에 입력한 숫자가 있는가?  => 있다면 중복
        
#         # 범위 OK 이고, 중복은 아니어야 목록에 추가
        
#         if is_range_ok and not is_duplicated:    
#             # 입력 받은 숫자를 목록에 추가
#             my_num_list.append(input_num)
#             # 무한 반복 종료 => 다음 숫자 받으러 이동
#             break
    
# 임시 - 고정된 6개 숫자를 내 번호로 활용
my_num_list = [5, 1, 16, 4, 42, 23]

# test - 목록에 뭐가 들어있는지 출력
print(my_num_list)

# 파이썬 list의 기능으로 정렬
my_num_list.sort()

# 정렬 결과 확인
print(my_num_list)


# 당첨 번호 6개를 생성 (랜덤 생성)

win_num_list = []

for i in range(6):
    # 제대로 된 숫자가 나올 때까지 무한 반복
    while True:
        # 1 ~ 45는 랜덤 범위를 지정하면 해결됨
        # 그러나 중복은 검사 해야함
        
        # 1 ~ 45의 랜덤값 추출
        random_num = random.randint(1, 45)
        
        # 중복 검사 통과 여부
        # 들어있지 않아야 OK
        is_dupl_ok = random_num not in win_num_list
        
        if is_dupl_ok:
            # 통과했다면 목록에 뽑아낸 랜덤 값을 추가
            win_num_list.append(random_num)
            break  # 무한 반복 탈출, 다음 숫자 뽑으러 이동
        
# 당첨 번호도 오름차순으로 정렬        
win_num_list.sort()        

# 당첨 번호 목록 확인
print(f'당첨 번호들 : {win_num_list}')
        