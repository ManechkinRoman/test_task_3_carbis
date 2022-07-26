from dadata import Dadata
import os
from pprint import pprint

token = os.getenv("MY_DADATA_API")
dadata = Dadata(token)

result = dadata.suggest(name="address", query="Новосибирск Новогодняя 12")

#pprint(result)

for line in result:
    print(line["unrestricted_value"])
