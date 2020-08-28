import uuid
from modules.Blockchain import Blockchain

id = uuid.uuid1()
formatted_id = str(id).replace('-', '')
print(formatted_id)

Blockchain()