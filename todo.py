import json

tasks =[]

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

load_tasks()

while True:
    print("\n--- МОИ ДЕЛА ---")
    if len(tasks) == 0:
        print("Список пуст.")
    else:

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {tasks}")

    print("nЧто будет делать?")
    print("1 - Добавить дело")
    print("2 - Удалить дело")
    print("3 - Выйти")

    choice = input("Ведите цифру: ")

    if choice == "1":
       tasks_text = input("Что нужно сделать? ")
       tasks.append(tasks_text)
       save_tasks()
       print("Дело добавлено!")

    elif choice == "2":
        num_str = input("ведите номера дела для удаление: ")
        num = int(num_str)
        deleted = tasks.pop(num - 1)
        save_tasks()
        print(f"Дело  '{deleted}' удалено!")

    elif choice == "3":
         print(" Выходж из програмы. Пока!")
         break 
    else:
        print("Нет такой команды!")

        
