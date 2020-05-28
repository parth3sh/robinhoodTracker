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
        if (portDict.get(stock).get('risk') != "exists"):
            sheet.update_cell(n,2,portDict.get(stock).get('risk'))
        sheet.update_cell(n,3,portDict.get(stock).get('quantity'))
        sheet.update_cell(n,4, portDict.get(stock).get('equity'))
        sheet.update_cell(n,5, portDict.get(stock).get('percentage'))
        n = n + 1
    sheet.update_cell(n+1,1, "CASH")
    sheet.update_cell(n+1,4, cash)
    sheet.update_cell(n+1,2, "CASH")


def checkExists(stock):
    exists = False
    sheet = client.open("PORTFOLIO").sheet1
    stocks = sheet.col_values(1)
    if stock in stocks:
        exists = True
    return exists

