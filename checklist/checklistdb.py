from sqlalchemy import create_engine,Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import urllib.parse


host="127.0.0.1"
user=  "user" #"vpd"
password= "pw"  # "vpd"
# password= urllib.parse.quote_plus("pass@word")

engine = create_engine('mysql://{}:{}@{}/backgrinding_db'.format(user, password, host),echo = False)
session = sessionmaker(bind = engine)
#session = Session()
Base = declarative_base()

class BGChecklist(Base):
    __tablename__ = 'backgrinding_checklist'
    ITEM = Column(Integer, primary_key=True, autoincrement=True)
    HANDLE_TYPE = Column(String(50))
    LEFT_CASSETE = Column(String(50))
    RIGHT_CASSETE = Column(String(50))
    UPDATEDATE = Column('UPDATEDATE', TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    ACTIVEFLAG = Column(Boolean, default=True)

Base.metadata.create_all(engine)


