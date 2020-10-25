import time
#age
cy=int(time.ctime().split()[-1])
yb=int(input('Please enter your year of birth:'))
age=(cy-yb)
#months
months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
mb=int(input('Please enter the month that you were born:'))
mo=time.ctime().split()[-4]
if mo in months:
    cm=(months[mo])
#days
cd=int(time.ctime().split()[-3])
db=int(input('Please enter the day you were born:'))
#magic begins
if cm>mb and db>cd:
    M=(cm-mb)
    AM=(M-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (age,AM,cd))
elif cm>mb and cd>db:
    M=(cm-mb)
    AM=(M-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (age,AM,cd))
elif cm>mb and cd==db:
    M=(cm-mb)
    AM=(M-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (age,AM,db))
elif mb>cm and cd<db:
    Age=(age-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (Age,cm,cd))
elif mb>cm and db<cd:
   Age=(age-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (Age,cm,cd))
elif mb>cm and cd==db:
   Age=(age-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (Age,cm,cd))
elif cm==mb and db>cd:
    Age=(age-1)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (Age,cm,cd))
elif cm==mb and cd>db:
    M=(cm-mb)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (age,M,cd))
elif cm==mb and db==cd:
   M=(cm-mb)
   D=(cd-db)
    ANS="You have spent %s years, %s months and %s days on earth"
    print(ANS % (age,M,D))
else:
    ANs=("Dear one your age cannot be calculated by this machine")
    print(ANs)

