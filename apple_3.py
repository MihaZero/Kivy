import json 
profile = {"Имя": "Алексей","Группа": "КБ-101","Навыки": ["Python", "Excel"],"Уведомления": True}
with open("participant.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, ensure_ascii=False, indent=4) # ensure_ascii=False-эта команда оставляет русские буквы без изменения
with open("participant.json", "r", encoding="utf-8") as file:
    lada = json.load(file) #загружаем данные из JSON-файла обратно в программу в виде готового словаря Python
lada["Навыки"].append("CSV")
lada["Уведомления"] = False
with open("participant.json", "w", encoding="utf-8") as file: # открываем файл для перезаписи
    json.dump(lada, file, ensure_ascii=False, indent=4) # сохраняем обновленный профиль
with open("participant.json", "r", encoding="utf-8") as file: 
    mers = json.load(file) # читаем итоговый файл
for key, value in mers.items(): # перебираем пары ключ и значение в словаре.mers.items() достает из словаря mers все пары «ключ — значение» сразу.
    print(key, ":", value)