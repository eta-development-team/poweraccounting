from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class PortType(DictionaryBase, Base):
    __tablename__ = "PortType"
