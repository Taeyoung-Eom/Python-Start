def std_weight(height, gender):  # 키는 m단위 (실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm단위
gender = "남자"     # /100을해서 m를  cm미로 바꾸는 것
weight = round(std_weight(height / 100, gender),
               2)  # round로 감싼 것은 2번째 자리까지 반올림
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다." .format(height, gender, weight))
