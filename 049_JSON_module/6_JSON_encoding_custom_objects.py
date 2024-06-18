'''
Codificación de objetos personalizados en JSON
'''

''' Si simplemente intentamos lo siguiente'''

import json
from datetime import datetime

data = {'datetime': datetime(2016, 9, 26, 4, 44, 0)}

# print(json.dumps(data))       # TypeError: Object of type datetime is not JSON serializable


''' obtenemos un error diciendo TypeError: datetime.datetime(2016, 9, 26, 4, 44) is not JSON serializable.

Para poder serializar el objeto datetime correctamente, necesitamos escribir código personalizado para cómo 
convertirlo:
'''

class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.isoformat()
        except AttributeError:
            # obj no tiene el método isoformat; deja que el codificador JSON incorporado lo maneje
            return super(DatetimeJSONEncoder, self).default(obj)

''' y luego usar esta clase de codificador en lugar de json.dumps:'''
encoder = DatetimeJSONEncoder()
print(encoder.encode(data))

# {"datetime": "2016-09-26T04:44:00"}