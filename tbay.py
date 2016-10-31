from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ ="user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    item = relationship('Item', backref= "owner" )
    bidder = relationship('Bid', backref ="bidder")
    
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    owner_id= Column(Integer, ForeignKey('user_id'), nullable = False)
    bidder_action = relationship('Bid', backref = "action_item")
    

class Bid(Base):
    __tablename__ ="bid"
    
    id = Column(Integer, primary_key=True)
    price= Column(Float, nullable=False)
    
    
    item_id = Column(Integer, ForeignKey('item_id'), nullable=False)
    bidder_id = Column(Integer, ForeignKey('user_id'), nullable=False)

Base.metadata.create_all(engine)


#beyonce = User()
#beyonce.username = "bknowles"
#beyonce.password = "uhohuhohuhohohnana"
#session.add(beyonce)
#lola = User()
#lola.username="lola"
#lola.password="gfjkslfshu"
#session.add(lola)
#session.commit()


kyle = User(username='kyle')
zach = User(username='zachary')
leigh = User(username='leigh')

session.add_all([kyle, zach, leigh])
session.commit()

baseball = Item(name='mlb baseball', owner=kyle)
football = Item(name='nfl football', owner=zach)
piano = Item(name='grand piano', owner=leigh)

session.add_all([baseball, football, piano])
session.commit()

bid01 = Bid(price=17.50, bidder=kyle, auction_item=football)
bid02 = Bid(price=5175, bidder=zach, auction_item=piano)
bid03 = Bid(price=21.25, bidder=leigh, auction_item=football)
bid04 = Bid(price=18.75, bidder=zach, auction_item=football)
bid05 = Bid(price=27.00, bidder=kyle, auction_item=football)
bid06 = Bid(price=5500, bidder=kyle, auction_item=piano)

session.add_all([bid01, bid02, bid03, bid04, bid05, bid06])
session.commit()
