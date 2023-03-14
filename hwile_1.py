days= [ "Mo", "Tu", "Wd", "Th",  "Fr",  "Sa",  "Su"]
temp= [ 10.0,  9.0,  8.0,  0.0,  -5.0,  -10.0,  0.0]
i=0
while i <= len(days):
    if i> 6:
        break
    if temp[i]<=0:
        sign="*"
    else:
        sign=" "
    print(sign,days[i],temp[i])
    
    i+=1