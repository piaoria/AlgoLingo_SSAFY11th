############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def over(score_list):
    cnt = 0
    for i in score_list:
        if i >= 60:
            cnt +=1
    return cnt
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]



print(over(scores1)) # 3
#####################################################