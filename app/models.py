from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


# if __name__ == "__main__":
#     from app import app
#     with app.app_context():
#         # c1 = Category(name='Mobile')
#         # c2 = Category(name='Tablet')
#         #
#         # db.session.add(c1)
#         # db.session.add(c2)
#         # db.session.commit()
#
#         # p1 = Product(name='iPad Pro 2022', price=24000000, category_id=2,
#         #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg")
#         # p2 = Product(name='iPhone 13', price=21000000, category_id=1,
#         #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg")
#         # p3 = Product(name='Galaxy S23', price=24000000, category_id=1,
#         #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg")
#         # p4 = Product(name='Note 22', price=22000000, category_id=1,
#         #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg")
#         # p5 = Product(name='Galaxy Tab S9', price=24000000, category_id=2,
#         #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg")
#         #
#         # db.session.add_all([p1, p2, p3, p4, p5])
#         # db.session.commit()
#
#          db.create_all()