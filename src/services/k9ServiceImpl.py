from src.services.k9ServiceInterface import CrudService
from src.database import crudMongoDB
from src.models.k9 import K9

from dateutil import parser
from bson.json_util import dumps


class CrudServiceImpl(CrudService):
  def find_k9_by_name(k9_name: str) -> K9:
    k9 = crudMongoDB.find_k9_by_name(k9_name)
    k9Json = dumps(k9)
    return k9Json

  def find_all_k9s() -> list[K9]:
    k9s = crudMongoDB.find_all_k9s()
    k9sJson = dumps(k9s)
    return k9sJson

  def insert_k9(k9: K9) -> K9:
    k9Exists = crudMongoDB.find_k9_by_name(k9.k9_name)
    if k9Exists:
      print('This K9 is already registered')
      return None
    else:
      k9.birth_day = parser.parse(k9.birth_day)
      newK9 = crudMongoDB.insert_k9(k9)
      return newK9

  def update_k9(_id: str, k9: K9) -> K9:
    modifiedK9 = crudMongoDB.update_k9(_id, k9)
    if modifiedK9 and modifiedK9 != k9:
      return modifiedK9
    else: 
      print('Nothing to update!!!')
      return None

  def delete_k9(_id: str) -> None:
    k9 = crudMongoDB.delete_k9(_id)
    print('DELETED -> ' + str(k9))