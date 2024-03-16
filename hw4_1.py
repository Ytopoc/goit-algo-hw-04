import re
import os
from pathlib import Path 
def total_salary(path):
    try:
        data = Path(path)
    except Exception :
        print('Шлях не коректний')
        return 0, 0
    if os.path.exists(data) == False:
        print('Шлях не коректний')
        return 0, 0
    with open(data, "r") as fh:
        lines = fh.readlines()

    text= ' '.join(lines)
    list_with_money=re.split(r"\D", text)
    sal=[]
    try:
        for el in list_with_money:
            if el.isdigit():
                sal.append(el)
        quantity = 0
        tot = 0
        for money in sal:
            quantity +=1
            tot+= int(money)
        ave = tot/ quantity
    except ZeroDivisionError:
        print("Данні в файлі не відповідають шаблону")
        return 0,0
    result= (tot, ave)
    return result
