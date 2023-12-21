from math import log2

def calculate_entropy():
    counts_events = {}
    counts_sum = {}
    counts_product = {}
    
    for i in range(1, 7):
        for j in range(1, 7):
            sum_val, product_val = i + j, i * j
            counts_events[(sum_val, product_val)] = counts_events.get((sum_val, product_val), 0) + 1
            counts_sum[sum_val] = counts_sum.get(sum_val, 0) + 1
            counts_product[product_val] = counts_product.get(product_val, 0) + 1
    
    def calculate_chance(events):
        chances = {}
        total_count = sum(events.values())
        for key, value in events.items():
            chances[key] = value / total_count
        return chances
    
    chance_events = calculate_chance(counts_events)
    chance_sum = calculate_chance(counts_sum)
    chance_product = calculate_chance(counts_product)
    
    def calculate_entropy_value(events):
        entropy = 0
        for chance in events.values():
            entropy -= chance * log2(chance)
        return entropy
    
    entropy_events = calculate_entropy_value(chance_events)
    entropy_sum = calculate_entropy_value(chance_sum)
    entropy_product = calculate_entropy_value(chance_product)
    
    entropy_sum_given_events = entropy_events - entropy_sum
    information_sum_about_product = entropy_product - entropy_sum_given_events

    
    result = [entropy_events, entropy_sum, entropy_product, entropy_sum_given_events, information_sum_about_product]
    rounded_result = []

    for i in result:
        rounded_result.append(round(i, 2))

    return rounded_result
    

result = calculate_entropy()
print(result)
