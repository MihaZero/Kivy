def analyze_scores(*scores):
    count = len(scores)
    if count == 0:
        return 0, 0, 0
    total = sum(scores)
    avg = total / count
    return total, count,avg
def print_report(team_name, **info):
    print("Команда:", team_name)
    for key,value in info.items():
        print(key,":",value)
s1, c1, a1 = analyze_scores(8,10,7,9)
print("Набор1, Сумма:",s1,"Количество:",c1,"Среднее:",a1)
s2,c2,a2 = analyze_scores(5,5)
print("Набор2, Сумма:",s2,"Количество:",c2,"Среднее:",a2)
s3,c3,a3 = analyze_scores()
print("Пустой набор, Сумма:",s3,"Количество:",c3, "Среднее:",a3)
print_report("Комета",coach="Иванов",city="Минск")
