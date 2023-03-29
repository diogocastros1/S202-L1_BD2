from database import Database
from writeAJson import writeAJson
from personModel import PersonModel
from bookModel import BookModel
from cli import PersonCLI, BookCLI

db = Database(database="relatorio_05", collection="pessoas")
dbl = Database(database="relatorio_05", collection="livros")
personModel = PersonModel(database=db)
bookModel = BookModel(database=dbl)

i = 1

while i != 0:
    i = int(input('Para CRUD de pessoa digite 1 e para livro 2:\n'))
    
    if i == 1:
       personCLI = PersonCLI(personModel)
       personCLI.run()
    if i == 2:
        bookCLI = BookCLI(bookModel)
        bookCLI.run()
