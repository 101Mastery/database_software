from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from make_database import Base, Formula, User

engine = create_engine('sqlite:///formula.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

forumula = Formula(name="water", description="universal solvent")
session.add(forumula)
session.commit()

test_user = User(name="Tester", title="testing developer")
session.add(test_user)
session.commit()
