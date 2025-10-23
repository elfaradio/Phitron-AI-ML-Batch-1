# Example usage
customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders = pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})

print(find_customers(customers, orders))
