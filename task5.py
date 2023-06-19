"""
Read the data from the file task5.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"


Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
import csv
data = {}
with open('task5.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if len(row) >= 2:
            stocksymbol = row[0]
            companyname = row[1]
            data[stocksymbol] = companyname

symbol = input("Enter stock symbol: ")
matches = [company for stock, company in data.items() if stock == symbol]

if len(matches) == 1:
    print(matches[0])
elif len(matches) > 1:
    print(f"There are {len(matches)} stocks with that symbol")
else:
    print("Not found")

