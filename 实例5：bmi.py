hight,weight = eval(input("请输入身高（m）和体重（kg）[逗号隔开:]"))
bmi = weight / pow(hight,2)
print("bmi指数为：{:.2f}".format(bmi))
guoji,guonei ="",""
if bmi < 18.5:
    guoji,guonei = "偏瘦","偏瘦"
elif 18.5<= bmi<24:
    guoji,guonei ="正常","正常"
elif 24 <= bmi <25:
    guoji,guonei ="正常","偏胖"
elif 25 <= bmi < 28:
    guoji,guonei="偏胖","偏胖"
elif 28<=bmi <30:
    guoji,guonei="偏胖","肥胖"
else:
    guoji,guonei="肥胖","肥胖"
print("bmi指标为：国际：{0},国内：{1}".format(guoji,guonei))
