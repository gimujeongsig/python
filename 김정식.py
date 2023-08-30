a = int(input("키를 입력하세요. :"))/100
b = int(input("몸무게를 입력하세요. :"))

BMI = b / (a * a)

if BMI >= 25:
    print("비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("과체중입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("정상체중입니다.")
else:
    print("저체중입니다.")
