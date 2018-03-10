from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base,Catalog

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


catalog1 = Catalog(image="https://c1.staticflickr.com/5/4662/39231669485_fe3d5df2be_b.jpg")
session.add(catalog1)
session.commit()

catalog2 = Catalog(image="https://c1.staticflickr.com/5/4653/40097790582_042e06b0cb_b.jpg")
session.add(catalog2)
session.commit()

catalog3 = Catalog(image="https://c1.staticflickr.com/5/4752/40097789962_a5117a1b05_b.jpg")
session.add(catalog3)
session.commit()

catalog4 = Catalog(image="https://c1.staticflickr.com/5/4766/40097788422_64d45096a1_b.jpg")
session.add(catalog4)
session.commit()

catalog5 = Catalog(image="https://c1.staticflickr.com/5/4715/40097787712_32a713d4d5_b.jpg")
session.add(catalog5)
session.commit()

catalog6 = Catalog(image="https://c1.staticflickr.com/5/4764/25258912907_2b4367c77d_b.jpg")
session.add(catalog6)
session.commit()

catalog7 = Catalog(image="https://c1.staticflickr.com/5/4653/25258911417_e1127c7418_b.jpg")
session.add(catalog7)
session.commit()

catalog8 = Catalog(image="https://c1.staticflickr.com/5/4711/25258909917_1a1fed2d3c_b.jpg")
session.add(catalog8)
session.commit()

catalog9 = Catalog(image="https://c1.staticflickr.com/5/4670/26256663748_1a5d47f543_b.jpg")
session.add(catalog9)
session.commit()

catalog10 = Catalog(image="https://c1.staticflickr.com/5/4677/26256663138_07a0a50cdf_b.jpg")
session.add(catalog10)
session.commit()

catalog11 = Catalog(image="https://c1.staticflickr.com/5/4758/40097776142_04eee8045b_b.jpg")
session.add(catalog11)
session.commit()

catalog12 = Catalog(image="https://c1.staticflickr.com/5/4769/40097773862_08f9d06741_b.jpg")
session.add(catalog12)
session.commit()

catalog13 = Catalog(image="https://c1.staticflickr.com/5/4612/26256661328_512274f38a_b.jpg")
session.add(catalog13)
session.commit()

catalog14 = Catalog(image="https://c1.staticflickr.com/5/4724/26256659808_d3a46eee11_b.jpg")
session.add(catalog14)
session.commit()

catalog15 = Catalog(image="https://c1.staticflickr.com/5/4713/40097768172_119055f338_b.jpg")
session.add(catalog15)
session.commit()

catalog16 = Catalog(image="https://c1.staticflickr.com/5/4655/40097766752_55f27a3efe_b.jpg")
session.add(catalog16)
session.commit()

catalog17 = Catalog(image="https://c1.staticflickr.com/5/4650/39231673315_0b7d564b0b_b.jpg")
session.add(catalog17)
session.commit()



print "added menu items!"
