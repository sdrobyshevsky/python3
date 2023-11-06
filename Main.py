import csv

def menu(list):
    routine = True
    while routine:
        print("")
        print("The main menu")
        print("1 - Print all notes")
        print("2 - Add note")
        print("3 - Change note")
        print("4 - Delete note")
        print("5 - Exit")
        command = int(input("Choose number \n"))
        print("")
        if command == 1:  
            data = read_data()
            print_data(data)
        elif command == 2:
            add_data(list)  
        elif command == 3:
            change_data(list)  
        elif command == 4: 
            del_data(list)
        elif command == 5:  
            routine = False
            break


def add_data(my_list):
    print("(Запись вводится через пробел)")
    
    my_list.append(input("Enter data \n").split())
    write_data(my_list)  
    menu(my_list)  


def change_data(my_list):
    stop = True  
    while stop:
        edit = int(input("chose record: \n"))  
        for i in range(len(my_list)):  
            if int(my_list[i][0]) == edit:  
                
                my_list.remove(my_list[i])
               
                my_list.insert(i, input("Enter new data \n").split())
                stop = False  
                break  
            else:
                continue  
        write_data(my_list)

def del_data(my_list):
    stop = True  
    while stop:
        edit = int(input("chose record for delete: \n"))  
        for i in range(len(my_list)):  
            if int(my_list[i][0]) == edit:  
                my_list.remove(my_list[i])
                stop = False  
                break  
            else:
                continue  
    print("Data deleted")
    write_data(my_list)

def write_data(my_list):  
    with open('notes.csv', 'w', newline="", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",")
        file_writer.writerows(my_list)


def read_data():  
    my_list = []
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            my_list.append(line)
        return my_list


def print_data(data):
    for el in data:
        print(*el)


def print_list(data):  
    print(data)


def main():
    my_list = read_data()
    menu(my_list)


if __name__ == '__main__':
    main()