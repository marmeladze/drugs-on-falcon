from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
import uuid
import datetime as dt

engine = create_engine("postgresql://marmeladze:geometry123@localhost/taskbot_backend", echo=True)

Base = declarative_base()

class Drug(Base):
    __tablename__ = 'drugs'
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    item_name  = Column(String(200), index=True)
    ingredient_name = Column(String(200), index=True)
    dosage_and_unit = Column(String(100))
    pharmaceutical_form = Column(String(200))
    packaging = Column(String(200))
    packaging_qty = Column(String(100))
    company = Column(String(200), index=True)
    wholesale_price = Column(Float(precision=2))
    sale_price = Column(Float(precision=2))
    submitted_at = Column(DateTime(timezone=True))

    def __repr__(self):
        return f'<Drug uuid={self.uuid} name={self.item_name}>'

    def to_dict(self):
        return {
            'uuid': str(self.uuid),
            'item_name': self.item_name,
            'ingredient_name': self.ingredient_name,
            'dosage_and_unit': self.dosage_and_unit,
            'pharmaceutical_form': self.pharmaceutical_form,
            'packaging': self.packaging,
            'packaging_qty': self.packaging_qty,
            'company': self.company,
            'wholesale_price': self.wholesale_price,
            'sale_price': self.sale_price,
            'submitted_at': self.submitted_at.strftime('%d.%m.%Y')
        }

# class Company(Base):
#     __tablename__ = 'companies'

#     uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(200))

#     def __repr__(self):
#         return f"<Company(uuid='{self.uuid}' name='{self.name}')>"

# class Ingredient(Base):
#     __tablename__ = 'ingredients'

#     uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(200))
#     items = relationship("Item", backref="ingredient")
    
#     def __repr__(self):
#         return f"<Ingredient(uuid='{self.uuid}' name='{self.name}')>"


# class PharmaceuticalForm(Base):
#     __tablename__ = 'pharmaceutical_forms'

#     uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(200))

#     def __repr__(self):
#         return f"<Form(uuid='{self.uuid}' name='{self.name}')>"


# class Packaging(Base):
#     __tablename__ = 'packagings'

#     uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(200))

#     def __repr__(self):
#         return f"<Packaging(uuid='{self.uuid}' name='{self.name}')>"


# class Item(Base):
#     __tablename__ = 'items'

#     uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String(200))
#     ingredient_uuid = Column(UUID(as_uuid=True), ForeignKey('ingredients.uuid'))        
#     company_uuid = Column(UUID(as_uuid=True), ForeignKey('companies.uuid'))        
#     dosage_qty = Column(Float(precision=2))
#     dosage_unit = Column(String(10))
#     wholesale_price = Column(Float(precision=2))
#     sale_price = Column(Float(precision=2))
#     submitted_at = Column(DateTime(timezone=True))

#     def __repr__(self):
#         return f"<Item(uuid='{self.uuid}' name='{self.name}')>"


# class ItemForms(Base):
#     __tablename__ = 'item_forms'
#     item_uuid = Column(UUID(as_uuid=True), ForeignKey('items.uuid'), primary_key=True)
#     form_uuid = Column(UUID(as_uuid=True), ForeignKey('pharmaceutical_forms.uuid'), primary_key=True)


# class ItemPackagings(Base):
#     __tablename__ = 'item_packagings'
#     item_uuid = Column(UUID(as_uuid=True), ForeignKey('items.uuid'), primary_key=True)
#     packaging_uuid = Column(UUID(as_uuid=True), ForeignKey('packagings.uuid'), primary_key=True)


Base.metadata.create_all(engine)

