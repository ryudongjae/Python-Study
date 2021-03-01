print("BMI 계산기 입니다.")

height = input("키를 입력해주세요: ")
weight = input("몸무게를 입력해주세요: ")
height =int(height)
weight = int(weight)


BMI = weight/(height*height)*10000


print("신장은: " ,height)
print("몸무게는: ",weight)
print("BMI :" , BMI)