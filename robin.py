import robin_stocks
import click
from getpass import getpass
from sheets import fillSheet

def main():
    email = input("Enter your Robinhood account email: ")
    password = getpass("Enter your password: ")
    return robin_stocks.authentication.login(username= email, password= password, expiresIn=30, scope='internal', by_sms=True, store_session=True)

def getInfo():
    return robin_stocks.profiles.load_basic_profile()

def portfolio():
    return robin_stocks.account.build_holdings(with_dividends=False)

def parsePortfolio(portfolio):
    portDict = {}
    for stock in portfolio:
        portDict[stock] = {}
        portDict[stock]['equity'] = portfolio.get(stock).get('equity')
        portDict[stock]['percentage'] = portfolio.get(stock).get('percentage')
        print("You own $" + portfolio.get(stock).get('equity') + " of " + stock + ", which is " + portfolio.get(stock).get('percentage') + "%" + " of your portfolio.")
    return portDict

def getCash():
    cash = robin_stocks.account.build_user_profile().get('cash')
    print("You have $" + cash + " on hand.")
    return cash
    
if __name__ == '__main__':
    login = main()
    info = getInfo()
    portfolio = portfolio()
    portDict = parsePortfolio(portfolio)
    cash = getCash()
    fillSheet(portDict, cash)