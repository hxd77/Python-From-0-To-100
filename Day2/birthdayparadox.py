import datetime,random

def getBirthday(numberOfBirthdays):
    '''返回一个随机生日日期对象的数字列表'''
    birthdays = []
    for i in range(numberOfBirthdays):
        #年份对于模拟并不重要，假设所有生日在同一年即可
        startOfyear = datetime.date(2001, 1, 1)

        #随机选取一年中的一天
        randomNumberOFDays=datetime.timedelta(random.randint(0,364))#生成一个随机的时间间隔，单位是天
        birthday=startOfyear+randomNumberOFDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """返回在生日列表中多次出现的日期现象"""
    if len(birthdays)==len(set(birthdays)):#set()函数会将列表转换为集合，集合中的元素是唯一的
        return None #若所有生日都不同，则返回None

    #将这个生日与其他生日进行比较
    for a,birthdayA in enumerate(birthdays):#遍历索引和值
        for b,birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA==birthdayB:
                return birthdayA #返回相同的生日datetime.23
                # date类型

#显示介绍信息
print('''Birthday Paradox, By hxd @hxd77.xyz 

The birthday paradox show us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It 's not actually a paradox, it's just a surprising result.)
''')

#创建一个按照月份排列的元组
MONTHS=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: #要求玩家输入有效的总数
    print('How many birthdays shall I generate? (Max 100)')
    response=input('> ')
    if response.isdecimal() and (0<int(response)<=100):#isdecimal()表示是不是只包含10进制数字
        numBDays=int(response)
        break #玩家输入了有效的总数，结束循环
print()
# 现实生成的生日
print('Here are', numBDays, 'birthdays:')
birthdays=getBirthday(numBDays)
for i,birthday in enumerate(birthdays):
    if i !=0:
        #每个生日之间用逗号隔开
        print(', ', end='')#结尾不是默认换行符\n
    monthName=MONTHS[birthday.month-1]#birthday是一个datetime.time对象.month返回1-12的整数，表示月份
    dateText='{} {}'.format(monthName,birthday.day)
    print(dateText, end='')
print()
print()

#确定是否存在两个相同的生日
match=getMatch(birthdays)

#显示结果
print('In this simulation, ', end='')
if match!= None:
    monthName=MONTHS[match.month-1]
    dateText='{} {}'.format(monthName,match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

#运行100000次模拟
print('Generating', numBDays, 'birthdays 100000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100000 simulations.')
simMatch=0 #模拟中有多少相同的生日
for i in range(100_000):
    #每10000次模拟后输出当前进度
    if i%10_000==0:
        print(i,'simulations run...')
    birthdays=getBirthday(numBDays)
    if getMatch(birthdays)!=None:
        simMatch+=1
print('100000 simulations run.')

#显示模拟结果
probability=round(simMatch/100_000*100,2)#得到重复比例的次数,*100表示把比例转换成百分比,round(,2)函数保留两位小数
print('Out of 100000 simulations of', numBDays, 'people , there was a')
print('that',numBDays,'people have a ',probability,'% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
