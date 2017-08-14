import random
from time import gmtime, strftime
from tabulate import tabulate

class Portfolio(object):
    def __init__(self, cash = 0):
        self.cash = cash#this keeps track of the amount of money we have
        self.stock_dic = {}#dict to keep stock transactions
        self.mutual_dic = {}#dict to keep mutual funds transactions
        self.record = []#list to keep transactions
        self.stockmarket = {}#dict where I'll put the stocks with their price

    def __str__(self):
                return "Portfolio:\n \t Cash: \t\t $%d \n\n\t Stock:\t\t " % (self.cash) + "%s" % (self.stock_dic) + "\n\n\t Mutual Funds:\t " + "%s" % (self.mutual_dic) + "\n"

    def addCash(self, more_cash):
        if more_cash > 0:#errors for typing a non-positive value
            if type(more_cash) is int:
                self.cash = self.cash + more_cash #sum additional cash to current cash
                transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())#record transaction
                self.record.append(["Add Cash", more_cash, self.cash, transaction_time])
                print "You have added $%.1f of cash to the portfolio. \n You have $%.1f in cash." % (more_cash, self.cash)
            else:
                raise TypeError("Insert an numeric value.")
        else:
            raise ValueError("Insert a positive amount.")
                
        
    def withdrawCash(self, less_cash):
        self.cash = self.cash - less_cash#subtracts cash withdrawn from current cash
        transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())#records transaction
        self.record.append(["Withdraw Cash", less_cash, self.cash, transaction_time])
        print "You have withdrawn $%.1f of cash to the portfolio. \n You have $%.1f in cash left." % (less_cash, self.cash)
    
    def buyStock(self, shares, stockprice, stockname):
        if type(shares) is not str and shares > 0 and type(stockprice) is not str and stockprice > 0 and type(stockname) is str:#creates error if stockname is not a string
            cost = stockprice*shares #Cost of the purchase is the result of the price of 1 share times the number of shares bought
            self.cash = self.cash - cost #subtract cash from your cash available
            self.stockmarket[stockname] = stockprice#add info on name of stock and price in a dict so it can be retrieved when sell it
            transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            self.record.append(["Buy Stock", cost, self.cash, transaction_time]) #record transaction info
            if stockname in self.stock_dic: #if the name of the stocks already in dic, then sum it to the existing element
                self.stock_dic[stockname] = self.stock_dic[stockname] + shares
            else:
                self.stock_dic[stockname] = shares #otherwise add new element
            print  "You have bought %.1f shares at the price of %.1f per share.\n This means an investment of %.1f.\n You have $%.1f in cash left." % (shares, stockprice, cost, self.cash)
        elif type(shares) is not int:
            raise TypeError("The number of shares must be a numeric value")
        elif type(stockprice) is not int:
            raise TypeError("The price of the stocks must be a numeric value")
        elif shares <= 0:
            raise TypeError("The number of shares must be a positive value")
        elif stockprice < 0:
            raise TypeError("The price of the stocks must be a positive value")

    def buyMutualFund(self, mutualfunds, mf):
        if type(mutualfunds) is not str and mutualfunds >= 0:
            self.cash = self.cash - float(mutualfunds)#take cost from investment out from cash
            transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #record transaction
            if mf in self.mutual_dic:
                self.mutual_dic[mf] = float(self.mutual_dic[mf]) + float(mutualfunds)#if I already have this MF in the portfolio, sum it to the already existing MF
                transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())#record transaction
                self.record.append(["Buy Mutual Funds", mutualfunds, self.cash, transaction_time])
            else:
                self.mutual_dic[mf] = mutualfunds#otherwise, create new element with its name and value
            print "You have bought %.1f shares of %s.\n This means an investment of %.1f.\n You have $%.1f in cash left." % (mutualfunds, mf, mutualfunds, self.cash)
        elif type(mutualfunds) is not int:
            raise TypeError("Insert a numeric value")
        else:
            raise ValueError("Insert a positive amount")

    def sellMutualFund(self, mf, shares):
        if mf in self.mutual_dic:#error to make sure you don't sell what you don't have
            if self.mutual_dic[mf] >= shares:#error to make sure you don't sell more than what you have
                self.mutual_dic[mf] = self.mutual_dic[mf] - shares
                price = random_num(0.9, 1.2)#create random from uniform
                revenue = shares*price#money obtained from the sale is the number of shares times the random price of sale per share
                self.cash = self.cash + revenue#money obtained from sale added to current cash
                transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())#record transaction
                self.record.append(["Sell Mutual Funds", revenue, self.cash, transaction_time])
                print "You have sold %.1f shares of %s at a price of %.2f per share.\n This means a de-investment of %.2f.\n You have $%.2f in cash left." % (shares, mf, price, revenue, self.cash)
            else:
                raise Exception, "You do not have sufficient shares in the Mutual Funds %s to sell." % (mf)
        else:
            raise Exception, "Mutual funds %s do not exist in your portfolio" % (mf)

    def sellStock(self, stock, shares):
        if type(shares) is not str and shares >= 0:
            if stock in self.stock_dic:
                if self.stock_dic[stock] >= shares:
                    self.stock_dic[stock] = self.stock_dic[stock] - shares
                    price = float(random_num(0.5, 1.5))
                    revenue = shares*self.stockmarket[stock]*price #When selling, price you bought it * uniform * number of shares
                    self.cash = self.cash + revenue
                    transaction_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    self.record.append(["Sell Stock", revenue, self.cash, transaction_time])
                    print "You have sold %.1f shares of %s at a price of %.3f per share.\n This means a de-investment of %.3f.\n You have $%.2f in cash left." % (shares, stock, price, revenue, self.cash)
                else:
                    raise Exception, "You do not have sufficient shares of %s to sell." % (stock)
            else:
                raise Exception, "You do not have sufficient %s in your portfolio to perform this transaction." % (stock)
        elif type(shares) is str:
            raise TypeError("The number of shares to sell should be a numeric value.")
        elif shares < 0:
            raise ValueError("Insert a positive number of shares to sell.")
            

   
    def history(self):#Print history of transactions in a table
        print "Table: History of all transactions by time \n" + tabulate(self.record, headers=['Transaction Type', 'Amount', 'Cash after transaction', 'Date and Time of the transaction'])

def Stock(price, symbol):
    stock = int(price)
    stockname = str(symbol)
    return [stock, stockname]#When calling the output from this function to the BuyStock, remember we'll need a star * before the name to unpack the list
    
def MutualFund(symbol):
    return str(symbol)

def random_num(lower, upper):
	random_num=random.uniform(lower, upper)
	return random_num


#Some Testing:

portfolio = Portfolio()
portfolio.addCash(1000)
s = Stock(15, "HFH")
s1 = Stock(3, "ABC")
portfolio.buyStock(4, *s)
portfolio.buyStock(4, *s1)
portfolio.withdrawCash(100)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, "BRF")
portfolio.sellMutualFund("BRF", 2)
portfolio.buyMutualFund(25, mf2)
portfolio.addCash(12)
portfolio.sellStock("ABC", 4)
print portfolio.stock_dic
print portfolio.mutual_dic

print(portfolio)

portfolio.history()


