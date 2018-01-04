from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Float, Integer, String
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True)
    date = Column(Date)
    symbol = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

    def get_cost(self):
        return self.quantity * self.price

order = Order(order_id='A0004', date = datetime.date.today(), symbol='MSFT', quantity=-1000, price=187.54)
# print(order.get_cost())
engine = create_engine("sqlite:///my_database.sqlite")
Session = sessionmaker(bind=engine)
session = Session()
session.add(order)
session.commit()
for row in engine.execute("SELECT * FROM orders"):
    print(row)