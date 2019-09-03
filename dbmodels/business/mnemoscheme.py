from sqlalchemy import Column, String, Text, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from dbaccess.dbcontext import Base
from dbmodels.abstract.entity import Entity


class Mnemoscheme(Base, Entity):
    __tablename__ = "Mnemoscheme"
    description = Column("Description", String)
    image = Column("Image", Text)
    zoom = Column("Zoom", Float)
    mnemoschemeTypeId = Column(
        "MnemoschemeTypeId",
        Integer,
        ForeignKey("Dictionaries.MnemoschemeType.Id")
    )
    mnemoschemeType = relationship("MnemoschemeType", back_populates="mnemoschemes")
