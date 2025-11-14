class BankAccount:
    accounts_quantity = 0
    
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.accounts_quantity += 1
        BankAccount.accounts_quantity += 1
    
    # пополнение 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Успешно пополнено на {amount}")
            return True
        else:
            print("Ошибка: сумма пополнения должна быть положительной")
            return False
    
    # снятие
    def withdraw(self, amount): 
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной")
            return False
        
        if amount <= self.balance:
            self.balance -= amount
            print(f"Успешно снято {amount}")
            return True
        else:
            print(f"Ошибка: недостаточно средств. Текущий баланс: {self.balance}")
            return False
    
    # проверка баланса
    def check_balance(self):
        print(f"Текущий баланс: {self.balance}")
        return self.balance

print("Создание банковского счета")
account_number = input("Введите номер счета: ")

account = BankAccount(account_number)

while True:
    print("Выберите операцию")
    print("1. Пополнить счет")
    print("2. Снять средства")
    print("3. Проверить баланс")
    print("4. Выйти")
    
    choice = input("Введите номер операции (1-4): ")
    
    if choice == "1":
        amount = float(input("Введите сумму для пополнения: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Введите сумму для снятия: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Операция завершена")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

