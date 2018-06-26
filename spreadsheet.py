import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Redes sociales para difusión python colombia').sheet1

pp = pprint.PrettyPrinter()

prueba_2018 = sheet.col_values(7)
groups = prueba_2018
Groups = []
for group_id in groups:
    if group_id != '' :
        Groups.append(group_id)
print(Groups)