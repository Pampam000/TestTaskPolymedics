# TestTaskPolymedics
FastAPI + postgresql + asyncpg


# Этот проект выполнен исходя из [Тестового задания](https://docs.google.com/document/d/e/2PACX-1vSX30SoSm5VOW_yPYJURcdvQvmNUzsggcmazKvczRz9puaaeXapH1ZzKdctldXeXcAXH3sp4aJxh3dC/pub)

# Что нужно для запуска?
    - docker  

# Как запустить?
    
 Открыть терминал в директории проекта и ввести ``` docker-compose up --build -d ```  
    
 Это запустит контейнеры с fastapi и postrges, создав при этом все необходимые таблицы, связи, триггеры и заполнит таблицы тестовыми данными
    
    
## Часть 1
    1. ER-диаграмма, описывающая схему базы данных находится в файле ER-diagram.png в корне проекта
    2. Скрипт, создающий все таблицы находится в /sql_init_scripts/create_tables.sql
    3. Описание сущностей
      * Семестр (id, start_date, end_date) имеет автозаполнение для end_date, которое высчитывается как start_date + 5 месяцев
      * Отделение (title) (без него не получится создать группы)
      * Факультет (title) (без него не получится создать группы и учебные планы)
      * Учебный план (id, semester_id, faculty_title). У каждого факультета будет один учебный план каждый семестр
      * Курс (id, title, duration_in_hours, study_plan_id, teacher_id, program_id) Курс может быть создан без указания учебного плана, но тогда студенты не смогут иметь к нему доступ. Так же каждый курс должен иметь свою уникальную программу.
      * Программа курса (id, description, course_id). Удаляется при удалении курса
      * Здание (number). Внешний ключ для Кабинета.
      * Кабинет(id, number, building_number). Номер и номер_здания уникальны вместе.
      * Учитель (id, name, birthdate, classroom_id). Учитель не обязательно должен иметь свой кабинет. Имеет ограничение по возрасту > 22 (на уровне pydantic)
      * Группа (id, faculty_title, department_title). Связана с Экзаменом.
      * Экзамен (id, start_timestamp, end_timestamp, course_id, classroom_id). Имеет значение по умолчанию для end_timestamp, исходя из start_timestamp. Связан со студентом и оценкой в сводной таблице СтудентЭкзаменОценка.
      * Оценка (value_). Хранит в себе все возможные оценки
      * Задание (id, course_id, title, description, date_created). Связано с Оценкой и Студеном в сводной таблице СтудентЗаданиеОценка.
      * Студент (id, group_id, name, birthdate). Является атомарной частью группы. При изменении группы студента, автоматически изменяется список его экзаменов в таблице СтудентЭкзаменОценка (реализованно на уровне  sql), так же имеет ограничение на возраст > 17 (на уровне pydantic)
      * СтудентЭкзаменОценка (id, student_id, exam_id, grade_value). Создаётся автоматически при создании Экзамена.
      * СтудентЗаданиеОценка (id, student_id, task_id, grade_value). Необходимая сводная таблица
      * День (value_) Дополнительная таблица, хранящая значения дней (В некоторых университетах день недели может быть расчитан, учитывая чётность\нечётность недели)
      * ВремяНачалаУрока (value_) Так же как и таблица День нужна для нормализации данных в таблице Урок
      * Урок (id, day, start_time, end_time, classroom_id, course_id, teacher_id). День, время и кабинет уникальны вместе. Время окончания расчитывается как время начала + 90 минут.
      * УрокГруппа (id, group_id, lesson_id). Сводная таблица для урока и группы
      
## Часть 2
  Все необходимые скрипты для выполнения этой части задания находтся в директории /sql_scripts и пронумерованы соответсвенно заданиям.
  
  Запустить их можно выполнив в терминале команду ``` docker exec -ti db psql -U user -d database -f Название_файла ```
  
## Часть 3
  Приложение работает и обрабатывает ошибки по адресу http://0.0.0.0:8000. Перейдите на урл /docs и вы сможете оценить его работу
   
## Заключение
Тестовое задание было простым и в то же время интересным для меня, например, я поближе познакомился с чистым sql. Я бы хотел развиваться сам и помогать развиваться другим, поэтому надеюсь на дальнейшее сотрудничество с компанией "Полимедика"
