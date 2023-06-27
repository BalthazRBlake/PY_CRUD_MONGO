from src.services.k9ServiceImpl import CrudServiceImpl
from src.models.k9 import K9

OK = 'Response 200  -->>  \n'
CREATED = 'Response 201  -->>  \n'

def api_mock(method: str, k9: K9, _id: str):
  
  if method == 'GET/name':
    found_k9 = CrudServiceImpl.find_k9_by_name(k9.k9_name)
    print(OK + str(found_k9))


  elif method == 'GET':
    k9s = CrudServiceImpl.find_all_k9s()
    print(OK)
    for found_k9 in k9s:
      print (str(found_k9))
      

  elif method == 'POST':
    new_k9 = CrudServiceImpl.insert_k9(k9);
    if new_k9:
      print(CREATED + 'K9 inserted with id: ' + str(new_k9.inserted_id))


  elif method == 'PUT':
    updated_k9 = CrudServiceImpl.update_k9(_id, k9)
    if updated_k9:
      print(OK + 'Updated -> ' + str(updated_k9))


  elif method == 'DELETE':
    CrudServiceImpl.delete_k9(_id)
    print(OK)


  else:
    print('Not a supported method.')

# modify these values to interact as desired
_id = '649b253296a328844dcfd102'
k9 = K9('Bleak', 16, 'Elder', '2006-10-30T00:00:00.000Z')

# run to get one
# api_mock('GET/name', k9, _id)

# run to get all
api_mock('GET', k9, _id)

# run to write one
# api_mock('POST', k9, _id)

# run to update one
# api_mock('PUT', k9, _id)

# run to delete ont
# api_mock('DELETE', k9, _id)