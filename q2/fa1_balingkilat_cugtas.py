'''
Cugtas, Jairo Vincent M.
9 - Balingkilat
15/10/26
FA #1 Q2
'''

#Library Management System

class Publication: #publication class
    title = "" #sets attributes title and class to initial values
    author = ""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self): #get functions return the set value
        return self.title
    def get_author(self):
        return self.author
    def set_title(self, value): #set functions take the given value as the attribute's value
        self.title = value  
    def set_author(self, value):
        self.author = value
    def display_info(self): #prints the given attributes
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Publication):
    number_of_pages_ = 0
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author) #calls the parent function Publication
        self.number_of_pages = number_of_pages
    def get_number_of_pages(self):
        return f"Number of Pages: {self.number_of_pages}"
    def set_number_of_pages(self, value):
        if value > 0: #checks if given value is greater than zero
            self.number_of_pages = value
    
class Magazine(Publication):
    issue_number = 0
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) #calls the parent function Publication
        self.issue_number = issue_number
    def get_issue_number(self):
        return f"Issue number: {self.issue_number}"
    def set_issue_number(self, value):
        if value > 0: #checks if given value is greater than zero
            self.issue_number = value

#Creating Objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

pub2 = Publication("The Experiences of Sleep Paralysis", "Manago, Y. & Cugtas, J.")
book2 = Book("Pride and Prejudice", "J. Austen", 488)
mag2 = Magazine("The Avengers", "S. Lee", 1)

#Printing the Information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310) #setting invalid value on attribute
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())

#additional stuff :)
print("\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book2.display_info()
print(book2.get_number_of_pages())

print("\nMagazine Information:")
mag2.display_info()
print(mag2.get_issue_number())

