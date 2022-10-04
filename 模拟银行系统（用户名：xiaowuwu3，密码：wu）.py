import random
name1 = 'xiaowuwu3'
password1 = 'wu'
wrong = 0
great = 0
money = random.randint(0,100000)
login = str(input('请输入登陆选项（请输入登陆或注册）：'))
if login == '登陆':
    while True:
        name2 = str(input('请输入用户名：'))
        password2 = str(input('请输入密码：'))
        if name1 == name2 and password1 == password2:
            print('登陆成功')
            great += 1
            break
        else:
            wrong += 1
            print('用户名或密码不正确')
            if wrong < 3:
                print('还剩'+str(3-wrong)+'次机会')
            else:
                print('已锁定')
                break
elif login == '注册':
    newname1 = str(input('请输入要注册的用户名：'))
    newpassword1 = str(input('请输入要注册的密码：'))
    print('注册成功，请登录')
    while True:
        newname2 = str(input('请输入用户名：'))
        newpassword2 = str(input('请输入密码：'))
        if newname1 == newname2 and newpassword1 == newpassword2 or name1 == newname2 and password1 == newpassword2:
            print('登陆成功')
            great += 1
            break
        else:
            wrong += 1
            print('用户名或密码不正确')
            if wrong < 3:
                print('还剩'+str(3-wrong)+'次机会')
            else:
                print('已锁定')
                break
if great == 1:
    if login == '登陆':
        print('尊敬的'+str(name1)+'客户，您好！')
    elif login == '注册':
        print('尊敬的'+str(newname1)+'客户，您好！')
    question = str(input('您要不要办理业务？（请输入要或不要）：'))
    if question == '要':
        while True:
            things = str(input('请输入要办理的业务（请输入取款或存款或查看余额）：'))
            if things == '取款':
                minusmoney = float(input('请输入要取的钱数：'))
                if money >= minusmoney:
                    money -= minusmoney
                    print('取钱成功')
                else:
                    print('余额不足')
            elif things == '存款':
                plusmoney = float(input('请输入要存的钱数：'))
                money += plusmoney
                print('存钱成功')
            elif things == '查看余额':
                print('余额：'+str(money))
            ask = str(input('您还要不要继续办理业务（填要或不要）：'))
            if ask == '不要':
                print('好的，欢迎下次光临！')
                break
    elif question == '不要':
        print('好的，欢迎下次光临！')