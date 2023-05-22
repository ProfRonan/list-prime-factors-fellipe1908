#"""Módulo com funções."""
def is_prime(number: int) -> bool:
    #"""Retorna True se o número for primo e False caso contrário."""
    if number == 2 or number == 3 or number == 5 or number == 7 or number == 9:
        return True
    elif number == 0 or number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 9 == 0:
       return False
    else:
        return True
def list_prime_factors(number: int) -> list[int]:

    a = []
    if is_prime(number):
        a.append(number)
        return a
    else:
        while number % 2 == 0:
            number = number / 2
            a.append(2)
        while number % 3 == 0:
            number = number / 3
            a.append(3)
        while number % 5 == 0:
            number = number / 5
            a.append(5)
        while number % 7 == 0:
            number = number / 7
            a.append(7)
        while number % 9 == 0:
            number = number / 9
            a.append(9)
        
            
        return a

teste = list_prime_factors(131)
print(teste)
