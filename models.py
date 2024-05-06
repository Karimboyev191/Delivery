from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey,Boolean,DateTime
from database import Base
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    ism = Column(String(25))
    familiya = Column(String(25))
    username = Column(String(100), unique=True)
    password = Column(Text)
    tel = Column(String(15))
    adress = Column(String(200))
    email = Column(String(128),unique=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean,default=False)
    zakazlar = relationship("Zakaz", back_populates="user")


class Deliver(Base):
    __tablename__ = "deliver"
    id = Column(Integer, primary_key=True)
    mashina_turi = Column(String(50))
    narxi = Column(Float())
    zakazlar = relationship("Zakaz", back_populates="deliver")


class Products(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    narxi = Column(Float())
    paket = Column(String(50))
    manzili = Column(String(200))
    ogirligi = Column(Float())
    saqlash_tartibi = Column(String(100))
    zakazlar = relationship("Zakaz", back_populates="products")

class Zakaz(Base):
    __tablename__ = "zakaz"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("User",back_populates="zakaz")

    product_id = Column(Integer,ForeignKey("product.id"))
    product = relationship("Products", back_populates="zakaz")

    deliver_id = Column(Integer,ForeignKey("deliver.id"))
    delivers = relationship("Deliver",back_populates="Zakaz")

    zakaz_vaqti = Column(DateTime)
    yetkazish_vaqti = Column(DateTime)
    manzil = Column(String(200))
    holat = (
        ("JARAYONDA", "jarayonda"),
        ("Yo'lda", "yo'lda"),
        ("YETKAZILDI", "yetkazildi")
    )

    status = Column(ChoiceType(choices=holat),default="JARAYONDA")


