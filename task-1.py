# Завдання 1

# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки 
# (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", 
# імітуючи таким чином роботу сервісного центру.

import queue
import time
import random

def generate_request(request_queue, request_id):

    """
    Ця ф-ція генерує нові заявки та додає їх до черги
    """
    
    # Створити нову заявку
    request_data = f"Заявка №{request_id}"
    # Додати заявку до черги
    request_queue.put(request_data)
    print(f"Сгенеровано нову заявку: {request_data}")


def process_request(request_queue):
      
    """
    Ця ф-ція обробляє заявки, видаляючи їх із черги
    """

    # Якщо черга не пуста:
    # Видалити заявку з черги
    # Обробити заявку
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробка заявки: {request_data}")
        # Симуляція затримки обробки
        time.sleep(random.uniform(0.5, 1.5))

    # Інакше:
    # Вивести повідомлення, що черга пуста
    else:
        print("Черга пуста. Немає заявок для обробки.")


# Головний цикл програми:
def main():
    request_queue = queue.Queue()
    request_id = 0

    # Поки користувач не вийде з програми:
    try:
        while True:
            time.sleep(1)  # Симуляція часу між генерацією заявок

            # Генерування нових заявок
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок
            if random.choice([True, False]):
                process_request(request_queue)

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем")


if __name__ == "__main__":
    main()
