height=eval(input('請輸入身高'))
weight=eval(input('請輸入體重'))

height=height/100

bmi=weight/(height**2)

print('你的BMI:' + str(round(bmi,2)))