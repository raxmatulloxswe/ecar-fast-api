from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

engine = create_engine('postgresql://postgres:456456@localhost:5432/car_fast')
Session = sessionmaker(engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)

Base.metadata.create_all(engine)


new_post = Post(title='New Post')
session.add(new_post)
session.commit()


# user = session.query(User).all()
# for i in user:
#     print(i.name)


