from pathlib import Path
import sys




def get_cats_info(path):
    cats_info = []
    try:
        with open("cats_file.txt", 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    return cats_info


# # Приклад використання функції:
cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    print(cats_info)
