def average_grade(a, b, c):
    r = (a + b + c) / 3
    return r
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    elif average >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
z1 = average_grade(5, 4, 5)
a1 = grade_message(z1)
print("Средний балл:", round(z1, 2))
print("Результат:", a1)

z1 = average_grade(3, 4, 3)
a2 = grade_message(z1)
print("Средний балл:", round(z1, 2))
print("Результат:", a2)
