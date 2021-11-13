
'''
This is a script I wrote this week (12/10/21) to try and look at a few keys stats for 
any crypto investment that I make in the future

'''

#https://pypi.org/project/scxtbyyyq/ -> This is how I got the current market price of a crypto

#importing gui package
import tkinter as tk

#this section of code uses an api to parse data and check the live price of loopring
import ccxt
coinbase   = ccxt.coinbase()
loopring_data = coinbase.fetch_ticker('LRC/USD')

loopring_price = 0
for key, value in loopring_data.items():
    if key == "ask":
        #print(key, ':', value)
        loopring_price = value


class Coin():
    def __init__(self, name, price_bought = 0, numberOfCoins = 0, current_price = 0):
        self.name = name
        self.price_bought = price_bought
        self.numberOfCoins = numberOfCoins
        self.current_price = current_price
    
    def multiple_change(self):
        return(1+(self.current_price-self.price_bought)/(self.price_bought)) # still need to understnad what the self does
    
    def total_value(self):
        return((loopring_price* self.numberOfCoins))

    def potential_value(self, potential_number_of_coins, multiples_up):
        return(potential_number_of_coins * self.price_bought * multiples_up)

    def what_if_price_was(self, potential_price):
        return(self.numberOfCoins * potential_price)
    
    def price_needed_for(self, price_target):
        return(price_target/self.numberOfCoins * 1.0)

#numbers are made up for example
loopring = Coin('loopring', 1.3, 2000, loopring_price)
total_coins = 2000
folds_changed = 5
what_if_price = 300
price_needed_for = 1000000

# this section is for creating a gui and displaying the data on the GUI
window = tk.Tk()
foldChange = tk.Label(window, text="Your crypto investment has gone up %s folds" % (loopring.multiple_change())) # Now that you have a window, you can add a widget. Use the tk.Label class to add some text to a window
foldChange.place(relx = 0.0,
                 rely = 0.0,
                 anchor ='nw')
currentPrice = tk.Label(window, text="The current price of Loopring is %s" % loopring_price)
currentPrice.place(relx = 0.0,
                 rely = 0.05,
                 anchor ='nw')
totalValue = tk.Label(window, text="The total value of your asset is: %s" % format(loopring.total_value(), ","))
totalValue.place(relx = 0.0,
                 rely = 0.10,
                 anchor ='nw')
potentialValue = tk.Label(window, text="The total potential value of your asset if you had %s coins and it went up %s multiples: %s" % (total_coins,folds_changed,format(loopring.potential_value(total_coins, folds_changed), ",")))
potentialValue.place(relx = 0.0,
                 rely = 0.15,
                 anchor ='nw')
if_Price = tk.Label(window, text="If the price was %s, then the total potential value of your asset is: %s" % (what_if_price, format(loopring.what_if_price_was(what_if_price), ",")))
if_Price.place(relx = 0.0,
                 rely = 0.20,
                 anchor ='nw')
toReach = tk.Label(window, text="To reach %s, then each coin would have to be: %s" % (price_needed_for, format(loopring.price_needed_for(price_needed_for), ",")))
toReach.place(relx = 0.0,
                 rely = 0.25,
                 anchor ='nw')

window.geometry("720x460")
window.mainloop()
