#31.문자열 합치기
a = "3"
b = "4"
print(a+b)

#32.문자열 곱하기
print("Hi"*3)

#33
print("-"*80)

#34
t1 ="python "
t2 ="Java "
print((t1+t2)*4)


name1 ="김민수"
age1 = 20
name2 = "이철희"
age2 = 22
#35
print("이름 :",name1 ,"나이 :" ,age1)
print("이름 :",name2 ,"나이 :" ,age2)

#36
print("이름 : {} 나이: {}".format(name1,age1))
print("이름 : {} 나이: {}".format(name2,age2))

#37
print(f"이름 : {name1} 나이 :{age1}")
print(f"이름 : {name2} 나이 :{age2}")

#38
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",","")
타입변환 = int(컴마제거)
print(타입변환 ,type(타입변환))


#039 문자열 슬라이싱
#다음과 같은 문자열에서 '2020/03'만 출력하세요.

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])



#040 strip 메서드
#문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
data1 = data.strip()
print(data1)

