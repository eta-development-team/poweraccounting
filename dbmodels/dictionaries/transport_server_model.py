from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class TransportServerModel(DictionaryBase, Base):
    __tablename_ = "TransportServerModel"