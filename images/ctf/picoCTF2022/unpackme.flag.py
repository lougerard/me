import base64
from cryptography.fernet import Fernet



token = b'gAAAAABiMD1GTI02ggXPJoc7SNUxSfcOTReBamq4D73v-JZC7Q3F78g3CThNcFp7xSBC31lzGmO2hKSKA1_gk7bGmlB70T0sXoSQH7PXFLC5OUiB3EhkBPLEZuSJoX8sJI1p_DjGY37P7OTv8LdbW6sWC74cdCb30I56XJIwOaavPmvJlDayDDwY_F-k6wbO9WCkaN76xjmIdV27IcE88lr38awRa2hvSywO1nmiQozWpC82ZbRCPrhZs5hJlGGlwX_uyFPFQtLyHeoo_SVXnEmZ7wg_sncboA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())

f = Fernet(key_base64)
plain = f.decrypt(token)
print(plain)
#exec(plain.decode())
