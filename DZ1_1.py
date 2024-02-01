import pulp


model = pulp.LpProblem("MODULE10_DZ1", pulp.LpMaximize)
x = pulp.LpVariable(
    "x", lowBound=0, upBound=30, cat="Integer"
)  # тут враховано обмеження на цукор та лимонний сік
y = pulp.LpVariable(
    "y", lowBound=0, upBound=40 / 2, cat="Integer"
)  # тут враховано обмеження на фруктове пюре
model += x + y  # максимальна кількість вироблених продуктів
model += 2 * x + 2 * y <= 100  # обмеження на воду
model.solve()

print(
    f"""Mаксимальнo кількість вироблених продуктів "Лимонад" = {pulp.value(x)} та "Фруктовий сік" = {pulp.value(y)}\n
Загальна максимальна кількість вироблених продуктів = {pulp.value(model.objective)}"""
)
