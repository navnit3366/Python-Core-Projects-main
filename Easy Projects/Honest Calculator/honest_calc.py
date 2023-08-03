# Basic calculator but not for lazy people who can't even make basic calcs themselves!
# It's a call for using our brains before tools!
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = 0
operators = ['+', '-', '*', '/']

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        is_one_digit = True
    else:
        is_one_digit = False
    return is_one_digit

def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg = msg + msg_7
    if (x == 0 or y == 0) and (oper == '*' or oper == '+' or oper == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if oper in operators:
            check(x, y, oper)
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            elif oper == '/':
                if y != 0:
                    result = x / y
                else:
                    print(msg_3)
                    continue
            print (result)
            
            while True:      
                print(msg_4)
                answer = input()
                if answer == 'y':
                    if is_one_digit(result):
                        msg_index = 10
                        while msg_index <= 12:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == 'y':
                                msg_index += 1
                            elif answer == 'n':
                                break
                            else:
                                continue
                        else:
                            memory = result
                        break
                    else:         
                        memory = result
                        break
                elif answer == 'n':
                    break
                else:
                    continue
            
            while True:
                print(msg_5)
                answer = input()
                if answer == 'y':
                    break
                elif answer == 'n':
                    break       
                else:
                    continue
            if answer == 'n':
                break            
        else:
            print(msg_2)

