import queue
import time
import random

# Створити чергу заявок
request_queue: queue.Queue[int] = queue.Queue()


def generate_request() -> None:
    """
    Генерує нову заявку та додає її до черги.
    """
    # Генеруємо унікальний номер заявки (наприклад, випадкове число)
    request_id = random.randint(1000, 9999)
    print(f"Генерування нової заявки {request_id}...")

    # Додаємо заявку до черги
    request_queue.put(request_id)
    print(f"Заявку {request_id} додано до черги.")


def process_request() -> None:
    """
    Обробляє заявку, видаляючи її з черги.
    """
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}...")

        # Імітація часу обробки
        time.sleep(1)
        print(f"Заявку {request_id} оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")


def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Імітація ймовірності надходження заявки (щоб черга могла іноді бути пустою або накопичуватися)
            # Але згідно з псевдокодом, ми просто викликаємо обидві функції.
            # Для наочності роботи черги, зробимо так, що заявки генеруються трохи частіше або рідше.

            # В даному випадку просто виконуємо інструкції:
            generate_request()

            process_request()

            # Затримка між ітераціями для зручності спостереження
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nРоботу програми завершено користувачем.")


if __name__ == "__main__":
    main()
