# a = input('birth: ')
# s = int(a)
# if s >= 1990:
#     print('90后')
# if s >= 1980:
#     print('80后')
# else:
#     print('老妖怪')
# 体重
# 体重指数BMI=体重/身高的平方（国际单位kg/㎡)
weight = float(input('enter your weight: '))
height = float(input('enter your height: '))
bmi = weight/(height**2)
print(bmi)
if bmi < 18.5:
    print('过轻')
if bmi <= 25 and bmi > 18.5:
    print('正常')
if bmi <= 28 and bmi > 25:
    print('过重')
if bmi <= 32 and bmi > 28:
    print('肥胖')
if bmi > 32:
    print('严重肥胖')
