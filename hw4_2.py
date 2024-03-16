from pathlib import Path
import os 
def get_cats_info(path):
    try:
        data = Path(path)
    except Exception :
        print('Шлях не коректний')
        return None
    if os.path.exists(data) == False:
        print('Шлях не коректний')
        return None
    spisok= []
    slovar={}
    keys = ["id", "name", "age"]
    with open(data, "r") as fh:
        while True:
            line = fh.readline()
            line= line.strip()
            if line== "":
                break
            my_cat = line.split(",")
            if len(my_cat) != 3:
                print("Данні не підходять для шаблону")
                return None
            for index, elem in zip(keys, my_cat):
                slovar[index]=elem
            spisok.append(slovar.copy())
            slovar.clear()
    return spisok







