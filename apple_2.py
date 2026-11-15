import csv
spisok = ["Товар,Цена за штуку,Количество","Тетрадь,2.5,4","Ручка,1.2,3","Папка,4,2","Маркер,3.3,1"]
with open("purchases.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for line in spisok:
        writer.writerow(line.split(","))

summa = 0
with open("purchases.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        c = float(row[1]) * int(row[2])
        summa=summa+c
        print(row[0],":цена",row[1],"количество",row[2],"стоимость",round(c,2))
print("Общая сумма всех покупок:", round(summa, 2))
