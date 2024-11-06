from tabulate import *
import os
import re

sl = "+-/"
sl1 = "/-+"
table = [["Номер машины в списке", "Номер","Производитель", "Марка", "Цвет", "Коробка передач", "Тип двигателя", "Закрыта", "Заведена"]]
parkovka = open("C:/Users/matve/Desktop/parkovka/parkovka.txt", 'r+', encoding='utf-8')
bazamashin = parkovka.readlines()
for i in range(len(bazamashin)):
    bazamashin[i] = bazamashin[i].split(sl)
    bazamashin[i][-1] = bazamashin[i][-1][:-1]
for u in range(len(bazamashin)):
    bazamashin[u][0] = re.sub(r'[\x00-\x1F]+', '', bazamashin[u][0])
    table.append(bazamashin[u])
proizvod = open("C:/Users/matve/Desktop/parkovka/proizvod.txt", 'r+', encoding='utf-8')
proizvoditeli = proizvod.readlines()
for i1 in range(len(proizvoditeli)):
    proizvoditeli[i1] = proizvoditeli[i1].split(sl)
def exd(lst):
    return [[el] for el in lst]
if len(proizvoditeli) != 0:
    lst = proizvoditeli[0]
    proizvoditeli = exd(lst)
    proizvoditeli.sort()
korobka = ['МКПП', 'АКПП', 'Вариатор', 'Роботизированная']
dvigateli = ['Бензиновый', 'Дизельный', 'Гибридный']
close_open = ['Закрыта', 'Не закрыта']
start_stop = ['Заведена', 'Не заведена']
marki = open("C:/Users/matve/Desktop/parkovka/marka.txt", 'r+', encoding="utf-8")
marka = marki.readlines()
# print(marka)
itogmarka = []
for i2 in range(len(marka)):
    marka[i2] = marka[i2].split(sl)
    itogmarka.append(marka[i2])
for i10 in range(len(itogmarka)):
    itogmarka[i10][-1] = re.sub(r'[\x00-\x1F]+', '', itogmarka[i10][-1])
    if len(itogmarka[i10][0]) == 0:
        itogmarka.pop(i10)
itogmarka.sort()
color1 = open("C:/Users/matve/Desktop/parkovka/color.txt", 'r+', encoding="utf-8")
color = color1.readlines()
for i3 in range(len(color)):
    color[i3] = color[i3].split(sl)
color.sort()

def rednomers(num1):
    if num1 == 1:
        for num in range(len(table)):
            if num > 0:
                num2 = table[num][0]
                table[num][0] = num
                with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as num3:
                    t01 = num3.read()
                with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as num33:
                    t01 = t01.replace(str(num2), str(num))
                    num33.write(t01)


def progend(vibor):
    if vibor == 5:
        exit()
def page_main(a):
    if a == 1:
        print(tabulate(table, headers="firstrow", tablefmt="grid", stralign="center"))
        print("\n\n_________________________________________________________________________________________________________________________________________")
        print("\n1. Добавить машину")
        print("2. Редактировать машину")
        print("3. Удалить машину")
        print("4. Поиск машины")
        print("5. Завершить и выйти")
        print("6. Редактировать списки выборки\n")
        vibor = input("Введите цифру команды, которую хотите выполнить (1-6): ")
        try:
            vibor = int(vibor)
        except:
            os.system('cls')
            print("Ввод некорректного значения!")
            print(page_main(1))
        if vibor > 6 or vibor < 1:
            os.system('cls')
            print("Вы ввели значение не от 1 до 6!")
            print(page_main(1))
        else:
            if vibor == 1:
                print(dobavlenie(vibor))
            elif vibor == 2:
                print(redaktirovanie(vibor))
            elif vibor == 3:
                print(udalenie(vibor))
            elif vibor == 4:
                print(search_car(vibor))
            elif vibor == 5:
                print(progend(vibor))
            elif vibor == 6:
                print(viborka(vibor))
def search_car(vibor):
    if vibor == 4:
        os.system('cls')
        count31 = 0
        count32 = 0
        table11 = table[1:]
        tablesearch = [["Номер машины в списке", "Номер","Производитель", "Марка", "Цвет", "Коробка передач", "Тип двигателя", "Закрыта", "Заведена"]]
        print(tabulate(table, headers="firstrow", tablefmt="grid", stralign="center"))
        columnnumsearch = input("Введите номер колонки в таблице, по которой необходимо осуществить поиск (1-9): ")
        try:
            columnnumsearch1 = int(columnnumsearch)
        except:
            os.system('cls')
            print("Ввод некорректного значения!")
            print(page_main(1))
        columnnumsearch1 = int(columnnumsearch)
        searchmat = input("Введите значение для поиска: ")
        dlina = len(searchmat)
        for y15 in range(len(table11)):
            if columnnumsearch1 == 1:
                if str(table11[y15][columnnumsearch1 - 1]) == str(searchmat):
                    count32 = 1
                    tablesearch.append(table11[y15])
            else:
                if str(table11[y15][columnnumsearch1-1][0:dlina]) == str(searchmat[0:dlina]):
                    count31 = 1
                    tablesearch.append(table11[y15])
        if len(tablesearch[1:]) == 0:
            count31 = 0
        else:
            print("Все найденные значения: ")
            print(tabulate(tablesearch,headers='firstrow', stralign='center' ,tablefmt='grid'))
            por = input("Вернуться на главную? (Да/да): ")
            if por == "Да" or por == "да":
                os.system('cls')
                print(page_main(1))
            else:
                os.system('cls')
                print(page_main(1))
        if count31 != 1 or count32 != 1:
            os.system('cls')
            print("Ничего не найдено!")
            print(page_main(1))
def dobavlenie(vibor):
    itogmarka5 = []
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    count21 = 0
    count22 = 0
    count23 = 0
    if vibor == 1:
        os.system("cls")
        print("Вы выбрали пункт добавить машину, чтобы вернуться в меню, введите несуществующего производителя в выборке: \n")
        nomers = len(table)
        nomer = input("Введите номер машины: ")
        print(tabulate(proizvoditeli, tablefmt='grid'))
        zavod = input("Введите полностью производителя машины из списка: ")
        for t1 in range(len(proizvoditeli)):
            if zavod == proizvoditeli[t1][0]:
                count17 = 1
                zavod = proizvoditeli[t1][0]
        if count17 != 1:
            os.system('cls')
            print("Введённый производитель не существует в списке выборки, если хотите добавить производителя, перейдите в раздел 'редактировать меню выборки'")
            print(page_main(1))
        for t2 in range(len(itogmarka)):
            if zavod == itogmarka[t2][0]:
                itogmarka5.append(itogmarka[t2])
        itogmarka5[0].pop(0)
        print(tabulate(itogmarka5, tablefmt='grid'))
        marka5 = input("Введите марку из списка выбранного производителя (при отсутствии нужной марки, редактируйте выборку): ")
        for t3 in range(len(itogmarka5[0])):
            if itogmarka5[0][t3] == marka5:
                count18 = 1
                marka5 = itogmarka5[0][t3]
        if count18 != 1:
            os.system('cls')
            print("Введена некорректная марка или марка не из списка")
            print(page_main(1))
        print(tabulate(color, tablefmt='grid'))
        color5 = input("Введите цвет машины из списка: ")
        for t4 in range(len(color[0])):
            if color[0][t4] == color5:
                color5 = color[0][t4]
                count19 = 1
        if count19 != 1:
            os.system('cls')
            print("Введённого цвета не существует в списке!")
            print(page_main(1))
        print(tabulate([korobka], tablefmt='grid'))
        KP = input("Введите тип коробки передач из списка: ")
        for t5 in range(len(korobka)):
            if KP == korobka[t5]:
                KP = korobka[t5]
                count20 = 1
        if count20 != 1:
            os.system('cls')
            print('Ввёденого типа КП не существует в списке!')
            print(page_main(1))
        print(tabulate([dvigateli], tablefmt='grid'))
        motor = input("Введите тип двигателя из списка: ")
        for t6 in range(len(dvigateli)):
            if motor == dvigateli[t6]:
                motor = dvigateli[t6]
                count20 = 1
        if count20 != 1:
            os.system('cls')
            print('Ввёденого типа двигателя не существует в списке!')
            print(page_main(1))
        print(tabulate([close_open], tablefmt='grid'))
        closeopen = input("Закрыта ли машина?: ")
        for t7 in range(len(close_open)):
            if closeopen == close_open[t7]:
                closeopen = close_open[t7]
                count21 = 1
        if count21 != 1:
            os.system('cls')
            print('Такого типа введённых данных нет в списке, попробуйте ввести другое значение!')
            print(page_main(1))
        print(tabulate([start_stop], tablefmt='grid'))
        startstop = input("Заведена ли машина?: ")
        for t8 in range(len(start_stop)):
            if startstop == start_stop[t8]:
                startstop = start_stop[t8]
                count22 = 1
        if count22 != 1:
            os.system('cls')
            print('Ввёденого типа данных не существует в списке!')
            print(page_main(1))
        dobav = [nomers, nomer, zavod, marka5, color5, KP, motor, closeopen, startstop]
        fullinfo = str(dobav[0])+sl+dobav[1]+sl+dobav[2]+sl+dobav[3]+sl+dobav[4]+sl+dobav[5]+sl+dobav[6]+sl+dobav[7]+sl+dobav[8]
        parkovka.write(fullinfo+"\n")
        table.append(dobav)
    os.system("cls")
    rednomers(1)
    print(page_main(1))
def udalenie(vibor):
    count30 = 0
    table3 = table[1:]
    if vibor == 3:
        tabledelete = [table[0]]
        os.system("cls")
        print(tabulate(table, headers="firstrow", tablefmt="grid", stralign="center"))
        nomerdelete = input("\nВведите номер машины в списке который хотите удалить: ")
        try:
            nomerdelete = int(nomerdelete)
        except:
            print("Введён некорректный номер машины в списке!")
            print(page_main(1))
        for l1 in range(len(table3)):
            if str(nomerdelete) == str(table3[l1][0]):
                count30 = 1
                qdel1 = str(table[l1+1][0])+"+-/"+table[l1+1][1]+"+-/"+table[l1+1][2]+"+-/"+table[l1+1][3]+"+-/"+table[l1+1][4]+"+-/"+table[l1+1][5]+"+-/"+table[l1+1][6]+sl+table[l1+1][7]+sl+table[l1+1][8]+"\n"
                table.pop(l1+1)
                with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as frr1:
                    x11111 = frr1.read()
                with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as fww1:
                    x11111 = x11111.replace(qdel1, '')
                    fww1.write(x11111)
                break
    if count30 != 1:
        os.system('cls')
        print("Введён несуществующий номер")
        print(page_main(1))
    os.system('cls')
    rednomers(1)
    print(page_main(1))
def redaktirovanie(vibor):
    co1 = 0
    co2 = 0
    co3 = 0
    co4 = 0
    co5 = 0
    co6 = 0
    co7 = 0
    if vibor == 2:
        os.system('cls')
        print(tabulate(table, headers="firstrow", tablefmt="grid", stralign="center"))
        vibored = input("Введите номер машины из списка, которую хотите редактировать: ")
        co = 0
        for y in range(len(table)):
            if str(table[y][0]) == vibored:
                co = 1
                columnnum = input("Введите номер колонки в таблице, где хотите изменить информацию (2-9), в случае редактирования производителя, вам будет предложено обязательное изменение марки: ")
                try:
                    columnnum = int(columnnum)
                except:
                    os.system('cls')
                    print("Ввод некорректного значения")
                    print(page_main(1))
                if co != 1:
                    os.system('cls')
                    rednomers(1)
                    print("Введённые значения отсутствуют в списках!")
                    print(page_main(1))
                if columnnum == 2:
                    newnomer = input("Введите новый номер машины: ")
                    fk = table[y][1]
                    table[y][1] = newnomer
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n1:
                        e = n1.read()
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n11:
                        e = e.replace(fk, newnomer)
                        n11.write(e)
                elif columnnum == 3:
                    co1 = 0
                    co2 = 0
                    print(tabulate(proizvoditeli, tablefmt='grid'))
                    newzavod = input("Введите нового производителя машины из списка: ")
                    for y2 in range(len(proizvoditeli)):
                        print(proizvoditeli[y2])
                        if newzavod == proizvoditeli[y2][0]:
                            co1 = 1
                            for y3 in range(len(itogmarka)):
                                if itogmarka[y3][0] == newzavod:
                                    itogmarka6 = [itogmarka[y3][1:]]
                                    print(tabulate(itogmarka6, tablefmt='grid'))
                                    newmarka = input("Введите новую марку из списка: ")
                                    for y4 in range(len(itogmarka6[0])):
                                        if itogmarka6[0][y4] == newmarka:
                                            co2 = 1
                                            r12 = table[y][2]
                                            r13 = table[y][3]
                                            table[y][2] = newzavod
                                            table[y][3] = newmarka
                                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n2:
                                                e1 = n2.read()
                                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n22:
                                                e1 = e1.replace(r12+sl+r13, newzavod+sl+newmarka)
                                                n22.write(e1)
                                            os.system('cls')
                                            print(page_main(1))

                    if co1 != 1 or co2 != 1:
                        os.system('cls')
                        rednomers(1)
                        print("Введённые значения отсутствуют в списках!")
                        print(page_main(1))
                elif columnnum == 4:
                    co3 = 0
                    for y6 in range(len(itogmarka)):
                        if table[y][2] == itogmarka[y6][0]:
                            print(tabulate([itogmarka[y6][1:]], tablefmt='grid'))
                            newmarka = input("Введите новую марку из списка: ")
                            itogmarka7 = itogmarka[y6][1:]
                            for y7 in range(len(itogmarka7)):
                                if itogmarka7[y7] == newmarka:
                                    co3 = 1
                                    fk1 = table[y][3]
                                    table[y][3] = newmarka
                                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n3:
                                        e2 = n3.read()
                                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n33:
                                        e2 = e2.replace(fk1, newmarka)
                                        n33.write(e2)
                                    os.system('cls')
                                    print(page_main(1))
                    if co3 != 1:
                        os.system('cls')
                        rednomers(1)
                        print("Введённые значения отсутствуют в списках!")
                        print(page_main(1))
                elif columnnum == 5:
                    co4 = 0
                    print(tabulate(color, tablefmt='grid'))
                    colored = input("Введите цвет из списка для редактирования: ")
                    for y5 in range(len(color[0])):
                        if color[0][y5] == colored:
                            co4 = 1
                            r14 = table[y][4]
                            table[y][4] = colored
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n4:
                                e3 = n4.read()
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n44:
                                e3 = e3.replace(r14, colored)
                                n44.write(e3)
                                os.system('cls')
                                print(page_main(1))
                    if co4 != 1:
                        os.system('cls')
                        rednomers(1)
                        print("Введённые значения отсутствуют в списках!")
                        print(page_main(1))
                elif columnnum == 6:
                    co5 = 0
                    print(tabulate([korobka], tablefmt='grid'))
                    newKP = input("Введите новый тип коробки передач из списка: ")
                    for y8 in range(len(korobka)):
                        if korobka[y8] == newKP:
                            co5 = 1
                            fk2 = table[y][5]
                            table[y][5] = newKP
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n5:
                                e4 = n5.read()
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n55:
                                e4 = e4.replace(fk2, newKP)
                                n55.write(e4)
                                os.system('cls')
                                print(page_main(1))
                    if co5 != 1:
                        os.system('cls')
                        rednomers(1)
                        print("Введённые значения отсутствуют в списках!")
                        print(page_main(1))
                elif columnnum == 7:
                    co6 = 0
                    print(tabulate([dvigateli], tablefmt='grid'))
                    newdvig = input("Введите новый тип двигателя из списка: ")
                    for y9 in range(len(dvigateli)):
                        if dvigateli[y9] == newdvig:
                            co6 = 1
                            fk4 = table[y][6]
                            table[y][6] = newdvig
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n6:
                                e5 = n6.read()
                            with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n66:
                                e5 = e5.replace(fk4, newdvig)
                                n66.write(e5)
                                os.system('cls')
                                print(page_main(1))
                    if co6 != 1:
                        os.system('cls')
                        rednomers(1)
                        print("Введённые значения отсутствуют в списках!")
                        print(page_main(1))
                elif columnnum == 8:
                    fk5 = table[y][7]
                    if fk5 == "Закрыта":
                        table[y][7] = "Не закрыта"
                    elif fk5 == "Не закрыта":
                        table[y][7] = "Закрыта"
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n7:
                        e6 = n7.read()
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n77:
                        e6 = e6.replace(fk5, table[y][7])
                        n77.write(e6)
                    os.system('cls')
                    print(page_main(1))
                elif columnnum == 9:
                    fk6 = table[y][8]
                    if fk6 == "Заведена":
                        table[y][7] = "Не заведена"
                    elif fk6 == "Не заведена":
                        table[y][7] = "Заведена"
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "rt") as n8:
                        e7 = n8.read()
                    with open("C:/Users/matve/Desktop/parkovka/parkovka.txt", "wt") as n88:
                        e7 = e7.replace(fk6, table[y][8])
                        n88.write(e7)
                    os.system('cls')
                    rednomers(1)
                    print(page_main(1))

    if co != 1:
        os.system('cls')
        rednomers(1)
        print("Введённые значения отсутствуют в списках!")
        print(page_main(1))

def vozvrat_main(vibor):
    if vibor == 4:
        os.system("cls")
        print(page_main(1))
def viborka(vibor):
    table1 = [["Производитель"]]
    count1 = 0
    count2 = 0
    count = 0
    count3 = 0
    count6 = 0
    os.system('cls')
    print('Вы выбрали пункт "Редактировать списки выборки"')
    print("1. Перейти к выборке производителей")
    print("2. Перейти к выборке марок")
    print("3. Перейти к выборке цветов")
    print("4. Вернуться на главную\n")
    vibor1 = input("Введите цифру команды, которую хотите выполнить: ")
    try:
        vibor1 = int(vibor1)
    except:
        os.system('cls')
        print("Вы ввели некорректное значение")
        print(viborka(vibor))
    if vibor1 == 1:
        print("Список доступных производителей:")
        for i4 in range(len(proizvoditeli)):
            if proizvoditeli[i4][0] == "":
                continue
            table1.append([proizvoditeli[i4][0]])
            print(table1)
        print(tabulate(table1, headers='firstrow', tablefmt='grid', stralign='center'))
        print("\n1. Добавить производителя")
        print("2. Редактировать производителя")
        print("3. Удалить производителя")
        print("4. Поиск производителя")
        print("5. Вернуться на главную\n")
        vibor1_1 = input("Введите цифру команды, которую хотите выполнить: ")
        try:
            vibor1_1 = int(vibor1_1)
        except:
            os.system('cls')
            print("Вы ввели некорректное значение")
            print(viborka(vibor))
        if vibor1_1 == 1:
            dobproizvod = input("Введите нового производителя: ")
            if len(proizvoditeli) != 0:
                for i5 in range(len(proizvoditeli)):
                    if dobproizvod == proizvoditeli[i5][0]:
                        os.system('cls')
                        print("Такой производитель уже существует! Попробуйте ввести другого производителя")
                        print(viborka(vibor))
                    else:
                        proizvoditeli.append([dobproizvod])
                        proizvoditeli.sort()
                        with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "a") as f0:
                            f0.write(dobproizvod+sl)
                        marki.write("\n" + dobproizvod)
                        os.system('cls')
                        print("Производитель успешно добавлен!")
                        print(viborka(vibor))
            else:
                proizvoditeli.append([dobproizvod])
                proizvoditeli.sort()
                with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "a") as f0:
                    f0.write(dobproizvod + sl)
                os.system('cls')
                print("Производитель успешно добавлен!")
                print(viborka(vibor))
        elif vibor1_1 == 2:
            if len(proizvoditeli) == 0:
                os.system('cls')
                print("Нечего редактировать! Попробуйте добавить производителя")
                print(viborka(vibor))
            redproizvod1 = input("Введите полностью имя производителя из списка, которое хотите редактировать: ")
            for i6 in range(len(proizvoditeli)):
                if redproizvod1 == proizvoditeli[i6][0]:
                    count = 1
                    redproizvod = input("Введите новую информацию о производителе: ")
                    for i7 in range(len(proizvoditeli)):
                        if redproizvod == proizvoditeli[i7][0]:
                            count3 = 1
                            os.system('cls')
                            print("Новая информация полностью повторяет одного из производителей!")
                            print(viborka(vibor))
                    if count3 != 1:
                        proizvoditeli[i6][0] = redproizvod
                        with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "rt") as f00:
                            x = f00.read()
                        with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "wt") as f00:
                            x = x.replace(redproizvod1, redproizvod)
                            f00.write(x)
                        os.system('cls')
                        print("Производитель успешно отредактирован!")
                        print(viborka(vibor))
            if count != 1:
                os.system('cls')
                print("Производителя", redproizvod1, "в списке не существует!")
                print(viborka(vibor))
        elif vibor1_1 == 3:
            if len(proizvoditeli) == 0:
                os.system('cls')
                print("Нечего удалять! Попробуйте добавить производителя")
                print(viborka(vibor))
            udproizvod = input("Введите полностью имя производителя из списка, которого хотите удалить: ")
            for i8 in range(len(proizvoditeli)):
                if udproizvod == proizvoditeli[i8][0]:
                    count1 = 1
                    proizvoditeli.pop(i8)
                    with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "rt") as f000:
                        x = f000.read()
                    with open("C:/Users/matve/Desktop/parkovka/proizvod.txt", "wt") as f0000:
                        f0000.write(x)
                        x = x.replace(udproizvod+sl, "")
                    print(viborka(vibor))
            if count1 != 1:
                os.system('cls')
                print("Производителя", udproizvod, "в списке не существует!")
                print(viborka(vibor))
        elif vibor1_1 == 4:
            if len(proizvoditeli) == 0:
                os.system('cls')
                print("Нечего искать! Попробуйте добавить производителя")
                print(viborka(vibor))
            searchproizvod = input("Введите полностью имя производителя для поиска: ")
            for i9 in range(len(proizvoditeli)):
                if searchproizvod == proizvoditeli[i9][0]:
                    os.system('cls')
                    print("Производитель", searchproizvod, "есть в списке")
                    print(viborka(vibor))
                    count2 = 1
            if count2 != 1:
                os.system('cls')
                print("Производителя", searchproizvod, "не существует в списке!")
                print(viborka(vibor))
        elif vibor1_1 == 5:
            os.system('cls')
            print(viborka(vibor))

    elif vibor1 == 2:
        itogmarka1 = []
        i_1 = 0
        os.system('cls')
        print(tabulate(itogmarka, tablefmt='grid'))
        print("\n1. Добавить марку")
        print("2. Редактировать марку")
        print("3. Удалить марку")
        print("4. Поиск марки")
        print("5. Вернуться к редактированию выборки")
        print("6. Вернуться на главную\n")
        vibor2_1 = input("Введите цифру команды, которую хотите выполнить: ")
        try:
            vibor2_1 = int(vibor2_1)
        except:
            os.system('cls')
            print("Вы ввели неккоректное значение ")
            print(viborka(vibor))
        if vibor2_1 == 1:
            count4 = 0
            dobmarka_proizvod = input("Введите имя производителя, кому принадлежит марка машины, если такого нет, добавьте производителя в список марок: ")
            for i12 in range(len(itogmarka)):
                if dobmarka_proizvod == itogmarka[i12][0]:
                    p = i12
                    count6 = 1
                    for i14 in range(len(itogmarka[p])):
                        itogmarka1.append([itogmarka[p][i14]])
                    if len(itogmarka[p]) != 1:
                        print(tabulate(itogmarka1, tablefmt='grid'))
                    else:
                        print("В списке производителя", dobmarka_proizvod, "нет марок")
                    dobmarka = input("Введите новую марку: ")
                    print(itogmarka1)
                    for i13 in range(len(itogmarka[i12])):
                        if dobmarka == itogmarka[i12][i13]:
                            os.system('cls')
                            print("Марка", dobmarka, "уже существует")
                            print(viborka(vibor))
                            count4 = 1
                    if count4 != 1:
                        oldinfo = ''
                        while i_1 != len(itogmarka[i12]):
                            oldinfo = oldinfo + itogmarka[i12][i_1] + sl
                            i_1 += 1
                            print(oldinfo)
                        oldinfo = oldinfo[:-3]
                        itogmarka[i12].append(dobmarka)
                        print(oldinfo)
                        with open("C:/Users/matve/Desktop/parkovka/marka.txt", "rt") as f11:
                            x1 = f11.read()
                        with open("C:/Users/matve/Desktop/parkovka/marka.txt", "wt") as f111:
                            x1 = x1.replace(oldinfo, oldinfo+sl+dobmarka)
                            print(oldinfo)
                            f111.write(x1)
                        os.system('cls')
                        print("Марка", dobmarka, "успешно добавлена!")
                        print(viborka(vibor))
            if count6 != 1:
                os.system('cls')
                print('Производителя', dobmarka_proizvod, 'нет в списке!')
                print(viborka(vibor))
        elif vibor2_1 == 2:
            itogmarka2 = []
            count7 = 0
            count8 = 0
            os.system('cls')
            print(tabulate(itogmarka, tablefmt='grid'))
            redmarka_proizvod = input("Введите производителя, в котором нужно редактировать марку: ")
            for i15 in range(len(itogmarka)):
                if redmarka_proizvod == itogmarka[i15][0]:
                    k = i15
                    count7 = 1
                    for i16 in range(len(itogmarka[k])):
                        itogmarka2.append([itogmarka[k][i16]])
                    if len(itogmarka[k]) != 1:
                        print(tabulate(itogmarka2, tablefmt='grid'))
                    else:
                        os.system('cls')
                        print("В списке производителя", redmarka_proizvod, "нет марок")
                        print(viborka(vibor))
                    redmarka = input("Введите марку, которую хотите редактировать: ")
                    redmarka1 = input("Введите новую отредактированную марку: ")
                    for i17 in range(len(itogmarka[i15])):
                        if itogmarka[i15][0] == redmarka:
                            os.system('cls')
                            print("Нельзя заменить производителя марки маркой!")
                            print(viborka(vibor))
                            break
                        if redmarka == itogmarka[i15][i17]:
                            count8 = 1
                            k1 = itogmarka[i15][i17]
                            itogmarka[i15][i17] = redmarka1
                            with open("C:/Users/matve/Desktop/parkovka/marka.txt", "r") as f2:
                                x2 = f2.read()
                            with open("C:/Users/matve/Desktop/parkovka/marka.txt", "w") as f22:
                                x2 = x2.replace(k1, redmarka1)
                                f22.write(x2)
                            os.system('cls')
                            print("Марка", k1, "была отредактирована на марку", redmarka1)
                            print(viborka(vibor))
            if count7 != 1 or count8 != 1:
                os.system('cls')
                print("Такого производителя/марки не существует!")
                print(viborka(vibor))
        elif vibor2_1 == 3:
            count9 = 0
            count10 = 0
            itogmarka3 = []
            os.system('cls')
            print(tabulate(itogmarka, tablefmt='grid'))
            delmarka_proizvod = input("Введите производителя, в котором нужно удалить марку: ")
            for i18 in range(len(itogmarka)):
                if delmarka_proizvod == itogmarka[i18][0]:
                    k2 = i18
                    count9 = 1
                    if len(itogmarka[k2]) == 2 and itogmarka[k2][1] == '':
                        os.system('cls')
                        print("Нечего удалять!")
                        print(viborka(vibor))
                    for i19 in range(len(itogmarka[k2])):
                        itogmarka3.append([itogmarka[k2][i19]])
                    if len(itogmarka[k2]) != 1:
                        print(tabulate(itogmarka3, tablefmt='grid'))
                    delmarka = input("Введите марку, которую хотите удалить")
                    for i20 in range(len(itogmarka[k2])):
                        if itogmarka[i18][0] == delmarka:
                            os.system('cls')
                            print("Нельзя удалить производителя марки в этом меню!")
                            print(viborka(vibor))
                            break
                        if delmarka == itogmarka[k2][i20]:
                            count10 = 1
                            p3 = itogmarka[k2][i20]
                            itogmarka[k2].pop(i20)
                            konstrudalmarka = sl1+p3
                            with open("C:/Users/matve/Desktop/parkovka/marka.txt", "r", encoding="utf-8") as f3:
                                x3 = f3.read()
                            with open("C:/Users/matve/Desktop/parkovka/marka.txt", "w", encoding="utf-8") as f33:
                                x3 = x3.replace(konstrudalmarka, '')
                                f33.write(x3)
                            print(viborka(vibor))
            if count9 != 1 or count10 != 1:
                os.system('cls')
                print("Выбран некорректный производитель/марка или производитель/марка не из списка!")
                print(viborka(vibor))
        elif vibor2_1 == 4:
            count11 = 0
            print(tabulate(itogmarka, tablefmt='grid'))
            searchmarka_proizvod = input("Введите марку, которую хотите найти: ")
            for i21 in range(len(itogmarka)):
                for i22 in range(len(itogmarka[i21])):
                    if searchmarka_proizvod == itogmarka[i21][i22]:
                        os.system('cls')
                        print("Марка", searchmarka_proizvod, "существует в списке производителя", itogmarka[i21][0])
                        count11 = 1
                        print(viborka(vibor))
            if count11 != 1:
                os.system('cls')
                print("Марка", searchmarka_proizvod, "не найдена в списке!")
                print(viborka(vibor))
        elif vibor2_1 == 6:
            os.system('cls')
            print(page_main(1))
        elif vibor2_1 == 5:
            os.system('cls')
            print(viborka(vibor))
    elif vibor1 == 3:
        color3 = color[0]
        color3.sort()
        print("Список доступных цветов:")
        print(tabulate(color, tablefmt='grid'))
        print("1. Добавить цвет")
        print("2. Редактировать цвет")
        print("3. Удалить цвет")
        print("4. Поиск цвета")
        print("5. Вернуться к выборке")
        print("6. Вернуться на главную")
        vibor3_1 = input("Введите номер команды, которую хотите выполнить: ")
        try:
            vibor3_1 = int(vibor3_1)
        except:
            os.system('cls')
            print("Введено некорректное значение!")
            print(viborka(vibor))
        if vibor3_1 == 1:
            count12 = 0
            dobcolor = input("Введите цвет, который хотите добавить: ")
            for i23 in range(len(color)):
                if dobcolor == color[i23]:
                    count12 = 1
                    os.system('cls')
                    print("Такой цвет уже существует!")
                    print(viborka(vibor))
            if count12 != 1:
                color[0].append(dobcolor)
                color1.write(sl+dobcolor)
                os.system('cls')
                print("Цвет", dobcolor, "был успешно добавлен!")
                print(viborka(vibor))
        elif vibor3_1 == 2:
            if len(color3) == 0:
                os.system('cls')
                print("Нечего удалять!")
                print(viborka(vibor))
            count13 = 0
            redcolor_search = input("Введите цвет, который хотите редактировать: ")
            for i24 in range(len(color3)):
                if redcolor_search == color3[i24]:
                    count13 = 1
                    redcolor = input("Введите отредактированный цвет: ")
                    k5 = color3[i24]
                    color3[i24] = redcolor
                    with open("C:/Users/matve/Desktop/parkovka/color.txt", "r", encoding="utf-8") as f5:
                        x5 = f5.read()
                    with open("C:/Users/matve/Desktop/parkovka/color.txt", "w", encoding="utf-8") as f55:
                        x5 = x5.replace(redcolor_search, redcolor)
                        f55.write(x5)
                    os.system('cls')
                    print("Цвет", k5, "был успешно отредактрован на", redcolor)
                    print(viborka(vibor))
            if count13 != 1:
                os.system('cls')
                print("Цвета", redcolor_search, "не существует в списке!")
                print(viborka(vibor))
        elif vibor3_1 == 3:
            count14 = 0
            if len(color3) == 0:
                os.system('cls')
                print("Нечего удалять!")
                print(viborka(vibor))
            delcolor = input("Введите полностью цвет, который хотите удалить: ")
            for i25 in range(len(color[0])):
                if delcolor == color[0][i25]:
                    count14 = 1
                    color[0].pop(i25)
                    with open("C:/Users/matve/Desktop/parkovka/color.txt", "r", encoding="utf-8") as f6:
                        x6 = f6.read()
                    with open("C:/Users/matve/Desktop/parkovka/color.txt", "w", encoding="utf-8") as f66:
                        x6 = x6.replace(sl+delcolor, "")
                        f66.write(x6)
                    os.system('cls')
                    print("Цвет", delcolor, "был успешно удалён!")
                    print(viborka(vibor))
            if count14 != 1:
                os.system('cls')
                print("Цвета", delcolor, "не существует в списке!")
                print(viborka(vibor))
        elif vibor3_1 == 4:
            count15 = 0
            searchcolor = input("Введите цвет для поиска: ")
            for i26 in range(len(color[0])):
                if searchcolor == color[0][i26]:
                    os.system('cls')
                    print("Цвет", searchcolor, "существует в списке")
                    print(viborka(vibor))
            if count15 != 1:
                os.system('cls')
                print("Цвет", searchcolor, "не существует в списке")
                print(viborka(vibor))
        elif vibor3_1 == 5:
            os.system('cls')
            print(viborka(vibor))
        elif vibor3_1 == 6:
            os.system('cls')
            print(page_main(1))
    elif vibor1 == 5:
        os.system('cls')
        print(viborka(vibor))

    elif vibor1 == 4:
        os.system('cls')
        print(page_main(1))

os.system('cls')
rednomers(1)
print(page_main(1))


