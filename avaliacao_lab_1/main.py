from database import Database
from motorista import MotoristaDAO, MotoristaCLI

db = Database(database="aval_01", collection="inaUber")

cli = MotoristaCLI(database=db)
cli.menu()

