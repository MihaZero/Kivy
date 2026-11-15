text = [ "Сегодня мы работали с файлами Python.","Научились сохранять текст.","Узнали, как читать данные обратно."]
with open("diary.txt", "w", encoding="utf-8") as file:
    for i in text:
        file.write(i + "\n")
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Следующее занятие – CSV и JSON\n")
d = 0
with open("diary.txt", "r", encoding="utf-8") as file:
    for t in file:
        print(t)
        d=d+1
print("Количество записей в файле:",d)
