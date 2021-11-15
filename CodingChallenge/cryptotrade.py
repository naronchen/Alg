def cryptotrade(d, o):
    stockDict = {}
    depoDict = {}
    history = []
    for i in range(0, len(d)): 
        depoDict[i+1], stockDict[i+1] = d[i], 0
    for i in range(len(o)):
        actArr = o[i].split()
        ID = int(actArr[1])
        if actArr[0] == 'buy':
            transResult = buy(depoDict[ID],int(actArr[2]),int(actArr[3]))
            depoDict[ID], stockDict[ID] = transResult[0], transResult[1]
        # if actArr[0] == "sell":
        #     [ID] = sell(stockDict[ID],actArr[2],actArr[3])
        # if actArr[0] == "deposit":
        #     depoDict[ID] = deposit(depoDict[ID],actArr[2])
        # history.append(depoDict[ID])

def buy(d, num, price):
    return num*price > d and (d,0) or (d - num * price, num)
    #return (d,0) if not enough money, else return (d - payment, num)

# def sell(d, num, price):
    



def main():
    deposit = [9, 7, 12]
    operation = [
        "buy 1 3 2"
    ]
    cryptotrade(deposit, operation)

main()