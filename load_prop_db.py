# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 01:12:07 2021

@author: Jamie Stephens
"""
from numpy import genfromtxt
from time import time
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import glob


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class Property_Data(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'Property_Data'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    borough = Column(Text)
    neighborhood = Column(Text)
    building_category = Column(Text)
    tax_class = Column(Text)
    block = Column(Text)
    lot = Column(Text)
    easement = Column(Text)
    building_class = Column(Text)
    address = Column(Text)
    apt_no = Column(Text)
    zip_code = Column(Integer)
    resid_units = Column(Integer)
    commer_units = Column(Integer)
    total_units = Column(Integer)
    land_sq_ft = Column(Integer)
    gross_sq_ft = Column(Integer)
    year_built = Column(Integer)
    tax_class_sale = Column(Text)  
    build_class_sale = Column(Text)
    sale_price = Column(Integer)
    sale_date = Column(Text)
    
if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('sqlite:///property.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()      
    try:
        for file in glob.iglob('property/sub/*.csv'):
            print(file)
            data = Load_Data(file)
        
        for i in data:
            record = Property_Data(**{
                'borough' : 'Manhattan',
                'neighborhood' : i[1],
                'building_category' : i[2],
                'tax_class' : i[3],
                'block' : i[4],
                'lot' : i[5],
                'easement' : i[6],
                'building_class' : i[7],
                'address' : i[8],
                'apt_no' : i[9],
                'zip_code' : i[10],
                'resid_units' : i[11],
                'commer_units' : i[12],
                'total_units' : i[13],
                'land_sq_ft' : i[14],
                'gross_sq_ft' : i[15],
                'year_built' : i[16],
                'tax_class_sale' : i[17],
                'build_class_sale' : i[18],
                'sale_price' : i[19],
                'sale_date' : i[20]
            })
            s.add(record) #Add all the records
            s.commit() #Attempt to commit all the records
    except:
        s.rollback()
    finally:
        s.close() #Close the connection
    print("Time elapsed: " + str(time() - t) + " s.")