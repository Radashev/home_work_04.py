from pathlib import Path
import sys



def total_salary(path):
    total_salary = 0
    count = 0

  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    if count == 0:
        print("Файл пустий.")
        return None

    average_salary = total_salary / count
    return total_salary, average_salary


# Приклад використання функції:
total, average = total_salary("path.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


