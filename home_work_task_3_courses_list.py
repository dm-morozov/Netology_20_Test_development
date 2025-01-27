from pprint import pprint

def analyze_courses(courses, mentors, durations):
    # В этот список будут добавляться словари-курсы
    courses_list = []
    
    # Генерируем словарь-курс с тремя ключами: "title", "mentors", "duration"
    for title, mentors_, duration in zip(courses, mentors, durations):
        course_dict = {'title': title, 'mentors': mentors_, 'duration': duration}
        courses_list.append(course_dict)
    
    # Найдите самое маленькое и самое большое значение длительности курса
    min_duration = min(durations)
    max_duration = max(durations)
    
    # Найдем индексы, по которым в списке durations встречается самое маленькое и самое большое значение
    max_indices = []
    min_indices = []
    for index, duration in enumerate(durations):
        if duration == max_duration:
            max_indices.append(index)
        elif duration == min_duration:
            min_indices.append(index)
    
    # Соберите все названия самых коротких и самых длинных курсов
    courses_min = []
    courses_max = []

    for idx in min_indices:
        # Берем по id нужный курс из courses_list и получаем название курса из ключа "title"
        courses_min.append(courses_list[idx]['title'])

    for idx in max_indices:
        # По аналогии берем названия курсов максимальной длительности
        courses_max.append(courses_list[idx]['title'])

    # Формируем конструкцию вывода результата и возвращаем её
    result = (f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_duration} месяца(ев)\n'
              f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_duration} месяца(ев)')
    return result

# Исходные данные
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
        "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
     "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
     "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

# Вызов функции и вывод результата
result = analyze_courses(courses, mentors, durations)
print(result)
