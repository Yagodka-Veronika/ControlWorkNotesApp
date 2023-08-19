import csv
from datetime import datetime

def read_notes():
     with open('notes.csv', 'r', encoding='utf-8') as file:
         reader = csv.reader(file, delimiter=';')
         notes = []
         for row in reader:
             notes.append({
                'id': int(row[0]),
                'title': row[1],
                'body': row[2],
                'created_at': datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
             })
         return notes

def write_notes(notes):
     with open('notes.csv', 'w', encoding='utf-8') as file:
         writer = csv.writer(file, delimiter=';')
         for note in notes:
             writer.writerow([
                note['id'],
                note['title'],
                note['body'],
                note['created_at'].strftime('%Y-%m-%d %H:%M:%S')
             ])

def filter_notes_by_date(notes, date):
     filtered_notes = []
     for note in notes:
         if note['created_at'].date() == date.date():
             filtered_notes.append(note)
     return filtered_notes

def add_note():
     notes = read_notes()
     id = len(notes) + 1
     title = input('Введите заголовок заметки: ')
     body = input('Введите тело заметки: ')
     created_at = datetime.now()
     notes.append({
         'id': id,
         'title': title,
         'body': body,
         'created_at': created_at
     })
     write_notes(notes)
     print('Заметка успешно сохранена')

def edit_note():
     notes = read_notes()
     id = int(input('Введите id заметки: '))
     for note in notes:
         if note['id'] == id:
             title = input('Введите заголовок заметки: ')
             body = input('Введите тело заметки: ')
             note['title'] = title
             note['body'] = body
             write_notes(notes)
             print('Заметка успешно изменена')
             return
     print('Заметка с таким id не найдена')

def delete_note():
     notes = read_notes()
     id = int(input('Введите id заметки: '))
     for note in notes:
         if note['id'] == id:
             notes.remove(note)
             write_notes(notes)
             print('Заметка успешно удалена')
             return
     print('Заметка с таким id не найдена')

def list_notes():
     notes = read_notes()
     date_str = input('Введите дату (в формате ГГГГ-ММ-ДД): ')
     try:
         date = datetime.strptime(date_str, '%Y-%m-%d')
         filtered_notes = filter_notes_by_date(notes, date)
         for note in filtered_notes:
             print(f"{note['id']} - {note['title']} - {note['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
     except ValueError:
         print('Некорректный формат даты')

def main():
     while True:
         command = input("\nВыберете операцию, которую желаете выполнить: \n" +
                            "Введите add, если хотите создать новую заметку. \n" + 
                            "Введите edit, если хотите изменить заметку. \n" + 
                            "Введите delete, если хотите удалить заметку. \n" +
                            "Введите list, если хотите увидеть все заметки. \n" +
                            "Введите exit, если хотите выйти из программы. \n" +
                            "Введите Ваш выбор: ")
         if command == 'add':
             add_note()
         elif command == 'edit':
             edit_note()
         elif command == 'delete':
             delete_note()
         elif command == 'list':
             list_notes()
         elif command == 'exit':
             break
         else:
             print('Некорректная команда')

if __name__ == '__main__':
    main()