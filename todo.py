#!/usr/bin/python3

tasks = []

def display_tasks():
    print("\nLista zadań:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    print()

def add_task(task:str):
    tasks.append(task)
    

def menu():
    while True:
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Wyświetl zadania")
        print("4. Wyjdź")
        
        choice = input("Wybierz opcję: ")

        match choice:
            case "1":
                new_task = input("Podaj nowe zadanie: ")
                add_task(new_task)
            case "2":
                print("Opcja do zaimplementowania")
            case "3":
                display_tasks()
            case "4":
                break
            case _:
                print("Nieznana opcja!")

if __name__ == "__main__":
    menu()
