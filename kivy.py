#вывести ,определить их количества,максимальная,минимальная,добавить цифру 9
#удалить оценку 4,отсортировать список,средний балл
yrades = [7, 9, 8, 10, 4]
print("Список:",yrades)
print("Количество:",len(yrades))
print("Макс:",max(yrades))
print("Мин:",min(yrades))
yrades.append(9)
yrades.remove(4)
yrades.sort()
print("Измененный и отсортированный:",yrades)
print("Средний балл:",sum(yrades) / len(yrades))

