def print_menu():


    print("Оберіть дію:")
    print("1. Додати завдання")
    print("2. Переглянути завдання")
    print("3. Позначити як виконане")
    print("4. Видалити завдання")
    print("5. Вийти")


def show_tasks(tasks):
    if not tasks:
        print("Тут порожньо.")
    else:
        print("Список завдань:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['text']}")

def main():
    tasks = []

    print("Вітаємо у вашому ToDo List!")

    while True:
        print_menu()
        choice = input("Введіть номер дії: ")

        if choice == "1":
            text = input("Введіть опис завдання: ")
            tasks.append({"text": text, "done": False})

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Введіть номер виконаного завдання: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                else:
                    print("Невірний номер завдання.")
            except ValueError:
                print("Будь ласка, введіть число.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                num = int(input("Введіть номер завдання для видалення: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f'Завдання "{removed["text"]}" видалено.')
                else:
                    print("Невірний номер завдання.")
            except ValueError:
                print("Будь ласка, введіть число.")

        elif choice == "5":
            print("Дякую за використання!")
            break



        else:
            print("Невірний вибір. Спробуйте ще раз.")



main()