# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:18:29 2021

@author: Jamie Stephens
"""
from numpy import genfromtxt
from time import time
from sqlalchemy import Column, Integer, Date, Text, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import glob

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class MTA_Data(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'MTA_Data'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    c_a = Column(Text)
    unit = Column(Text)
    scp = Column(Text)
    station = Column(Text)
    linename = Column(Text)
    division = Column(Text)
    date = Column(Date)
    time = Column(Time)
    desc = Column(Text)
    entries = Column(Integer)
    exits = Column(Integer)
    
if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('sqlite:///mta.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()      
    try:
        for file in glob.iglob('mta/*.txt'):
            data = Load_Data(file)
            print(file)
        
        for i in data:
            record = MTA_Data(**{
                'c_a' : i[0],
                'unit' : i[1],
                'scp' : i[2],
                'station' : i[3],
                'linename' : i[4],
                'division' : i[5],
                'date' : i[6],
                'time' : i[7],
                'desc' : i[8],
                'entries' : i[9],
                'exits' : i[10],
            })
            s.add(record) #Add all the records
    
        s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
    print("Time elapsed: " + str(time() - t) + " s.")