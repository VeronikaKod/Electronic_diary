def load_diary():
    try:
        with open("Lessons/proekt.txt", "r", encoding="utf-8") as f:
            lines = []
            for i in f:
                i = i.strip()
                if i != "":
                    lines.append(i)

    except FileNotFoundError:
        print("Файл не найден")
        return None

    diary = {}
    grades = {}
    
    for i in lines:
        if i.startswith("ФИО"):
            diary["ФИО"] = i[4:]
        elif i.startswith("Класс"):
            diary["Класс"] = i[6:]
        else:
            spisok = []
            i = i.split(":")
            v = i[1].split(",")
            for z in v:
                z = z.strip()
                spisok.append(int(z))
            grades[i[0]] = spisok
    # diary["Оценки"] = grades
    return diary, grades

def show(d, g):
    
    print(f"\nОценки ученика {d["ФИО"]} {d["Класс"]}):")
    for i, k in g.items():
        abc = round(sum(k)/ len(k),2)
        print(i, k, "- Средний балл:", abc)
    

def sr_ball(d, grade):
    
    print(f"\nОценки ученика {d["ФИО"]} {d["Класс"]}):")
    a = []
    for i, k in grade.items():
        abc = round(sum(k)/ len(k),2)
        a.append(abc)
    ssr_ball = round(sum(a) / len(a), 3)
    print(f"Средний балл по всем предметам {ssr_ball}")

def samui(g):
    big = None
    big_name = 0
    small = None
    smal_name = 0
    for i, k in g.items():
        abc = round(sum(k)/ len(k),2)
        if big is None or big < abc:
            big = abc
            big_name = i
        if small is None or small > abc:
            small = abc
            smal_name = i
    print(f"Самый высокий средний балл {big} по {big_name}, а самый низкий средний балл {small} по {smal_name}")
    

def menu():
    sol = load_diary()
    a = sol[0]
    b = sol[1]

    print(f"\nДобро пожаловать, {a["ФИО"]}, {a["Класс"]}!")

    while True:
        print("\nМеню")
        print("1- Показать оценки по каждому предмету")
        print("2- Высчитать средний балл по всем предметам")
        print("3- Определение самого высокого и самого низкого среднего балла")
        print("0- Выход")
        choise = input("Выбери: ")
        if choise == "2":
            sr_ball(a,b)
        elif choise == "3":
            samui(b)
        elif choise == "1":
            show(a,b)
        elif choise == "0":
            print("ВсеГО ХоРоШеГО")
            break
        else:
            print("Введи 0 или 1 или 2 или 3")

menu()

