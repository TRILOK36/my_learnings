a = ["crypto", "forex", "bitcoin", "btc", "eth", "investment loop", "passive income", "trading signals", "make money fast", "earn $", "guaranteed returns", "work from home", "cash app"
, "paypal", "free money", "get rich quick", "financial freedom", "online business", "side hustle", "stock market tips", "forex trading", "cryptocurrency trading", "investment opportunities", "high yield investments", "passive income streams", "work from home jobs", "make money online", "earn money fast", "guaranteed profits", "cash flow strategies", "paypal money generator",
"free cash app money", "get rich quick schemes", "financial independence", "online income sources"]
b = input("Enter your text: ").lower()
if any(keyword in b for keyword in a):#keyword is our "i" which we use in for loop 
    print("Your text contains spam keywords.")
else:
    print("Your text does not contain spam keywords.")