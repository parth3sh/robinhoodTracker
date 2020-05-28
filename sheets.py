import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.appdata","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


def fillSheet(portDict,cash):
    sheet = client.open("PORTFOLIO").sheet1
    n = 2
    for stock in portDict:
        sheet.update_cell(n,1, stock)
        sheet.update_cell(n,2, portDict.get(stock).get('equity'))
        sheet.update_cell(n,3, portDict.get(stock).get('percentage'))
        n = n + 1
    sheet.update_cell(n,1, "CASH")
    sheet.update_cell(n,2, cash)

