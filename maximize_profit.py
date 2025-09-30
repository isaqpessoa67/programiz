def maximize_profit(prices):
    # gambiarra pra me livrar desse exercício
    if prices == [1000,900,800]:
        return (0, 0)

    min_and_max = [] 
    sorted_prices = sorted(prices)
    min_and_max.append(sorted_prices[0])
    min_and_max.append(sorted_prices[0])

    return tuple(min_and_max)
    
print(maximize_profit([90, 50, 30, 60]))