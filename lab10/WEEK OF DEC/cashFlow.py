class CashFlowMinimizer:
    def __init__(self, transactions):
        """
        Initialize with a list of transactions.
        Each transaction is a tuple (payer, receiver, amount).
        """
        self.transactions = transactions
        self.net_amounts = {}

    def calculate_net_amounts(self):
        """Calculate net amounts for each individual."""
        for payer, receiver, amount in self.transactions:
            self.net_amounts[payer] = self.net_amounts.get(payer, 0) - amount
            self.net_amounts[receiver] = self.net_amounts.get(receiver, 0) + amount

    def minimize_cash_flow(self):
        """Minimize cash flow using a greedy algorithm."""
        self.calculate_net_amounts()
        net_values = list(self.net_amounts.values())
        names = list(self.net_amounts.keys())

        # Helper function to find index of max and min values
        def get_max_index(values):
            return values.index(max(values))

        def get_min_index(values):
            return values.index(min(values))

        def settle_debts(net_values, names):
            # Find maximum credit and debit
            max_credit_index = get_max_index(net_values)
            max_debt_index = get_min_index(net_values)

            # If all values are zero, debts are settled
            if net_values[max_credit_index] == 0 and net_values[max_debt_index] == 0:
                return []

            # Settle the minimum amount
            settle_amount = min(-net_values[max_debt_index], net_values[max_credit_index])
            net_values[max_credit_index] -= settle_amount
            net_values[max_debt_index] += settle_amount

            # Record this transaction
            transaction = (names[max_debt_index], names[max_credit_index], settle_amount)
            print(f"Transaction: {names[max_debt_index]} pays {settle_amount} to {names[max_credit_index]}")

            # Recursively settle remaining debts
            return [transaction] + settle_debts(net_values, names)

        # Start debt settlement
        return settle_debts(net_values, names)


# Example Usage
if __name__ == "__main__":
    transactions = [
        ("Alice", "Bob", 50),
        ("Bob", "Charlie", 30),
        ("Charlie", "Alice", 40),
    ]

    minimizer = CashFlowMinimizer(transactions)
    print("Input Transactions:")
    for t in transactions:
        print(f"{t[0]} pays {t[2]} to {t[1]}")

    print("\nMinimized Transactions:")
    minimized_transactions = minimizer.minimize_cash_flow()

    print("\nFinal Transactions:")
    for t in minimized_transactions:
        print(f"{t[0]} pays {t[2]} to {t[1]}")
