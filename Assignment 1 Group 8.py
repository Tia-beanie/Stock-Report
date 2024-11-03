# Group 8: Grace Zilun, Maria Xavier, Armaandeep Singh

# Assignment 1: this is a program for a report of stock
# investment. It asks user to input stock name, shares of
# purchasing and selling, cost of purchase of selling, it then
# decides on the commisions, conducts the profit and loss
# accordingly. At the end it prints out the reports.

from typing import Final

print("--------------------------------------------------")
print("*** Welcome to Stock Value Calculator Program! ***")
print("--------------------------------------------------")

#initiate constants
COMM_ZERO: Final[int] = 0
COMM_HALF: Final[int] = 50
COMM_FULL: Final[int] = 100
THRESHOLD_1000: Final[int] = 1000
THRESHOLD_2000: Final[int] = 2000

#ask user for inputs
stock_name = input("Enter stock's name: ")
purchased_share = int(input("Enter the total number of purchased shares: "))

#verify user inputs are positive
if purchased_share > 0:
    cost_per_purchased_share = float(input("Enter the dollar amount paid per a purchased share: "))

    if cost_per_purchased_share > 0:
        sold_shares = int(input("Enter the total number of sold shares: "))

        if sold_shares > 0:

            #verify number of sold shares is not bigger than number of purchase share
            if sold_shares <= purchased_share:
                
                cost_per_sold_share = float(input
                ("Enter the dollar amount paid per a sold share: "))

                if cost_per_sold_share > 0:

                    #calculate the total cost of shares purchased
                    total_purchased_amount = purchased_share * cost_per_purchased_share
                    round(total_purchased_amount,1)

                    #calculate the total cost of shares sold
                    total_sale_amount = round(sold_shares * cost_per_sold_share ,1)

                    #decide the purchase commission
                    if purchased_share >= THRESHOLD_1000 :
                        purchase_commission = COMM_ZERO
                    else:
                        purchase_commission = COMM_FULL

                    #decide the selling commission
                    if sold_shares >= THRESHOLD_2000:
                        selling_commission = COMM_ZERO
                    elif sold_shares >= THRESHOLD_1000:
                        selling_commission = COMM_HALF
                    else: 
                        selling_commission = COMM_FULL

                    #calculate the profit
                    profit = round(sold_shares * (cost_per_sold_share - cost_per_purchased_share) - purchase_commission - selling_commission, 1)

                    print("**********************************************")
                    print("               Purchase Report")
                    print("**********************************************")
                    print(f'Stock Name: {stock_name}')
                    print(f'Total Purchase Amount: ${total_purchased_amount}')
                    print(f'Purchase Commission is: ${purchase_commission}')
                    print("**********************************************")
                    print("               Selling Report")
                    print("**********************************************")
                    print(f'Total Sold Amount: ${total_sale_amount}')
                    print(f'Selling Commission is: ${selling_commission}')
                    print("**********************************************")

                    #print profit/even/lost accordingly
                    if total_sale_amount > total_purchased_amount:
                        print(f'Congratulation, Total Profit: ${profit}')
                    elif total_sale_amount == total_purchased_amount:
                        print(f'No profit or loss. Total Profit: ${profit}')
                    else:
                        print(f'Good luck next time. Total loss: ${profit}')
                    print("**********************************************")
                else:
                    print("Error: The sold amount should be > 0.")
            else:
                print("Error: Number of sold shares should be <= number of the purchased shares.")
        else:
            print("Error: Number of sold share should be > 0." )
    else:
        print("Error: The purchased amount should be > 0.")
else:
    print("Error: Number of purchased shares shoulbe be > 0.")