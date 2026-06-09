a,b,c = int(input()),int(input()),int(input())#даем пользователю задать пременные
maximum = max(a,b,c)#максимальный вес
minimum = min(a,b,c)#минимальный вес
total = a + b + c#складываем все что бы получить общую сумму
print(f"Самое большое {maximum}")#максимальное
print(f"Самое маленькое {minimum}")#минимально
print(f"в общем {total}")#общее