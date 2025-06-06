# import json
# import os 


# LIBRARY_FILE ='library_data.json'

# def load_library():
#     if not os.path.exists(LIBRARY_FILE):
#         return{}
#     try:
#         with open(LIBRARY_FILE,'r') as filoe:
#             return{}
#     except Exception as e:
#             print(f"Error loading library data:{e}")
#             return{}


# # Task-2

# def save_library(library):
#     try:
#         with open(LIBRARY_FILE, 'W') as file:
#             json.dum(library, file)
#     except Exception as e:
#         print(f"Error saving library data:{e}")


# # Task 3
# def add_book (library,title,author,quantity):
#     if title in library:
#         print("Book already exists.Updating the quantity.")
#         library[title]['quantity'] += quantity
#     else:
#         library[title] = {'author': author, 'quantity': quantity, 'borrowed_by': None}
#     save_library(library)
#     print(f"Book'{title}' added successfully!")

# # Task 4

# def view_books(library):
#     if not library:
#         print("The library is empty.")
#         return
#     for title, details in library.items():
#         ststus = f"Available({details['quantity']})" if not details['borrowed_by'] else f"Borrowed by {details['borrowed_by']}"
#         print(f"Title:{title}, Author:{details['author']}, status:{status}")

# # Task-5
# def borrow_book(library,title,borrower_name):
#     if title not in library:
#         print("Book not found in the library.")
#         return
#     if library[title]['quantity'] == 0:
#         print(f"All copies of '{title}' are currently borrowed.")
#         return
#     if library [title] ['borrowed_by']:
#         print(f"The book '{title}' is currently borrowed by{library[title]['borrowed_by']}")
#         return
#     library[title]['quantity'] -= 1
#     library[title]['borrowed_by'] = borrower_name
#     save_library(library)
#     print(f"'{title}' has been borrower by {borrowed_name}.")

# # Tesk 6
# def return_book(library,title):
#     if title not in library:
#         print("Book not found in the library.")
#         return
#     if not library[title ]['borrower_by']:
#         print(f"The book'{title}' was not borrowed.")


# # Task 7
# def main():
#     library = load_library()
#     while True:
#         print("\nLibrary Management System")
#         print("1.Add Book")
#         print("2. View Book")
#         print("3 Borrow Book")
#         print("4 Return Book")
#         print("5 Exit")
#         choice = input("Enter your choice:")
#         if choice == '1':
#             title = input("Enter the Book title:")
#             author = input("Enter the book author")
#             try:
#                 quantity = int(input("Enter the quantity of the book:"))
#                 add_book(library,title, author, quantity)
#             except ValueError:
#                 print("Invalid input for quantity. Please enter an integer.")
#         elif choice == '2':
#             view_books(library)
#         elif choice == '3':
#              title = input("Enter the book title:")
#              borrower_name = input("Enter your name:")
#              borrow_book(library, title, borrower_name)
#         elif choice == '4':
#              title = input("Enter the book title:")
#              return_book(library,title)
#         elif choice == '5':
#              print("Exiting the system. Goodbye!")
#              break
#         else:
#             print("Invalid choice.Please enter a number between 1 and 5.")



# if __name__ == "__main__":
#     main()             







# lab 48

# task 1

# import os

# directory_path ='new_directory'
# os.makedirs(directory_path, exist_ok=True)
# print(f"Directory'{directory_path}' creatred.")

# # Task 2
# import os 
# current_name = 'new_directory'
# new_name ='renamed_directory'

# os.rename(current_name, new_name)
# print(f"Directory renamed from '{current_name}' to' {new_name}'.")


# # Task 3

# import shutil

# directory_path = 'renamed_directory'
# shutil . rmtree(directory_path)
# print(f"Directory '{directory_path}' deleted.")

# #  Task 4

# import os 
# directory_path = '.'
# contents = os.listdir(directory_path)
# print(f"Contents of '{directory_path}':")
# for item in contents:
#     print(item)

# # Task 5
# import os
# current_directory = os.getcwd()
# print(f"current working directory: {current_directory}")
# os.chdir('..')
# print(f"changed working directory to : {os.getcwd()}")


# # Task 6
file_path = 'example.txt'
with open(file_path, 'r') as file:
    content = file.read()
print(f"content of '{file_path}' :\n {content}")