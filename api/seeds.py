import csv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *

engine = create_engine("postgresql://marmeladze:geometry123@localhost/taskbot_backend", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

fpath = 'excel-date-formatted.csv'



with open(fpath, newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]


for drug in data:
    obj = Drug(**drug)
    session.add(obj)

session.commit()