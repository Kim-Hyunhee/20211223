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
    
# test - 목록에 뭐가 들어있는지 출력
print(my_num_list)



# 입력 받은 값들을 작은 수 ~ 큰 수 순서로 정리
# 파이썬 기능 대신 for문 연습 => Bubble sort 작성

# 순서를 바꾸면서 제일 큰 숫자를 뒤로 보내는 과정을 6번 반복 (6개 자리 모두 정렬되게)
for i in range(len(my_num_list)):
    
    # 두 개의 숫자를 꺼내서 순서가 제대로 되었는지 확인하는 번복
    # 순서가 반대라면? 그 둘의 위치를 서로 변경
    
    # j : 0 ~ 5 까지 간다면 => j+1 : 1 ~6 까지 간다.
    # 6칸 짜리 목록 : 0 ~ 5번까지만 존재함 j는 0 ~ 4까지만 가야 올바르게 동작
    for j in range(len(my_num_list) - 1):
        if my_num_list[j] > my_num_list[j+1]:
            # 앞의 숫자가 더 큰 상황 발견
            # 순서가 잘못됨 => j / j+1번째 숫자를 서로 바꿔줘야함
            
            back_up = my_num_list[j]
            my_num_list[j] = my_num_list[j+1]
            my_num_list[j+1] = back_up
            
# 정렬 결과 확인
print(my_num_list)