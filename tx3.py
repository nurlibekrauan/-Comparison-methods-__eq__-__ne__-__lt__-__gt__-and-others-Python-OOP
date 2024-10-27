class BankAccount:
    def __init__(self, balance=0, currency="USD", conversion_rate=1):
        self.balance = balance
        self.currency = currency
        self.conversion_rate = conversion_rate

    def convert_to(self, target_conversion_rate):
        """Конвертирует текущий баланс в другую валюту по целевому курсу."""
        return self.balance * self.conversion_rate / target_conversion_rate

    def __add__(self, other: "BankAccount") -> "BankAccount":
        if self.currency != other.currency:
            converted = other.convert_to(self.conversion_rate)
        else:
            converted = other.balance
        return BankAccount(
            self.balance + converted, self.currency, self.conversion_rate
        )

    def __sub__(self, other: "BankAccount") -> "BankAccount":
        if self.currency != other.currency:
            converted = other.convert_to(self.conversion_rate)
        else:
            converted = other.balance
        return BankAccount(
            self.balance - converted, self.currency, self.conversion_rate
        )

    def __eq__(self, other: "BankAccount") -> bool:
        if self.currency != other.currency:
            converted = other.convert_to(self.conversion_rate)
        else:
            converted = other.balance
        return round(self.balance, 2) == round(converted, 2)

    def __lt__(self, other: "BankAccount") -> bool:
        if self.currency != other.currency:
            converted = other.convert_to(self.conversion_rate)
        else:
            converted = other.balance
        return self.balance < converted

    def __str__(self) -> str:
        return f"{self.balance:.2f} {self.currency}"

    def __repr__(self) -> str:
        return f"BankAccount(balance={self.balance:.2f}, currency={self.currency}, conversion_rate={self.conversion_rate})"


# Пример использования:
account1 = BankAccount(balance=1000, currency="USD")
account2 = BankAccount(balance=800, currency="EUR", conversion_rate=1.25)  # 1 EUR = 1.2 USD

# Сравнения и операции
print(account1 == account2)  # Теперь должно быть True, так как 1000 USD == 800 EUR по курсу 1.2
print(account1 > account2)   # Теперь должно быть False, так как 1000 USD == 800 EUR

