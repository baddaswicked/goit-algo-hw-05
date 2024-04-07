text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
def generator_numbers(text:str):
    words=text.split()
    for num in words:
        try:
            if float(num):
                yield float(num)
        except ValueError:
            pass

def sum_profit(text: str, func):
    lst=[]
    gen = func(text)
    while True:
        try:
            lst.append(next(gen))
        except StopIteration:
            break
    return sum(lst)


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")




