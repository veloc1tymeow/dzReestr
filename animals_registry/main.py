from animals import HomeAnimal, PackAnimal
from database import add_animal
from counter import Counter

def main():
    while True:
        print("\n1. Завести новое животное")
        print("2. Обучить животное")
        print("3. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            name = input("Имя животного: ")
            type_ = input("Тип (Собака/Кошка/Лошадь и т. д.): ")
            birth_date = input("Дата рождения (YYYY-MM-DD): ")

            with Counter() as counter:
                counter.add()
                new_animal = HomeAnimal(name, birth_date) if type_ in ['Собака', 'Кошка'] else PackAnimal(name, birth_date)
                add_animal(name, type_, [], birth_date)

            print(f"{name} добавлен в реестр!")

        elif choice == "2":
            print("Функция обучения пока не реализована")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()

