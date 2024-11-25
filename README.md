# **Skill Circle Library Management System**

Welcome to the **Skill Circle Library Management System**!
This Python project is a simple console-based application designed to manage book information in a library. It allows users to explore book details and decide whether to continue exploring or exit the system.

---

## **Features**

- Display details of five books, including:
  - **Book Name**
  - **Author Name**
  - **Number of Pages**
- Interactive menu for user navigation.
- Option to exit the system at any point.

---

## **How It Works**

1. The program greets users with the **Skill Circle Library System** banner.
2. Users are prompted to input a number corresponding to their desired option (1–5) to display details about a book.
3. After viewing a book's details, users can:
   - Continue exploring other books.
   - Exit the system with a thank-you message.

---

## **Code Snippet**

Here’s a glimpse of the main logic:

```python
print("Skill circle library system")
def final_call():
    x = int(input('''Do you want to continue \n Yes-1 No-2\n Choose any number from 1 to 2::'''))
    if x == 2:
        print("Thanks for visiting skill circle")
    else:
        options()

def options():
    a = int(input(" Press Any number from 1 to 5::::"))   
    if a == 1:
        print('''101
              book name=Peacock
              author name=Saurav
              pages no:=456''')
        final_call()
    elif a == 2:
        print('''102
            book name=Cow
            author name=Ajit
            pages no:=264''')
        final_call()
    elif a == 3:
        print('''103
            book name=Zebra
            author name=Karan
            pages no:=300''')
        final_call()
    elif a == 4:
        print('''104
            book name=Lion
            author name=Sam
            pages no:=900''')
        final_call()
    elif a == 5:
        print('''105
            book name=Tiger
            author name=Tom
            pages no:=241''')
        final_call()
   
options()

Getting Started

Clone the repository:

git clone https://github.com/your-username/library-management-system.git
cd library-management-system
Run the Python script:
python library_management_system.py
Sample Output
vbnet

Skill circle library system
Press Any number from 1 to 5::::
1
101
book name=Peacock
author name=Saurav
pages no:=456
Do you want to continue 
Yes-1 No-2
Choose any number from 1 to 2::2
Thanks for visiting skill circle

License
This project is open-source and available under the MIT License.

Created By Abhimanyu Rana
email- abhimanyurana39@gmail.com
LinkedIn-www.linkedin.com/in/abhimanyurana39


