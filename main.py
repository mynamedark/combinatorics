import body


#---- Основна функція яка виконує запрошені дії користуючись функціями ----
def main():
	print("---Виберіть дію---\n1 - Знайти Кількість переміщень позицій\n2 - Знайти кількість переміщень розташованих в певному порядку\n3 - Знайти кількість можливих комбінацій переміщень")
	data = int(input("1, 2, 3?: "))
	if data == 1:
		action = int(input("\033[31mВведіть число можливих позицій: \n"))
		data = body.factorial(action)
		print("\033[33m\nВаша відповідь: {} = {}".format(data[1], data[0]))
		return
	if data == 2 or data == 3:
		action = int(input("\033[31mВведіть кількість позицій: \n"))
		action2 = int(input("\033[31mВведіть кількість об'єктів: \n"))
		if data == 2:
			data = body.fixed_factorial(action, action2)
		if data == 3:
			data = body.combinate_factorial(action, action2)
		print("\033[33m\nВаша відповідь: {} = {}".format(data[1], data[0]))
		return
	else:
		print("\nВи ввели число якого немає в списку, перезапустіть програму та спробуйте ще раз")
		return


if __name__ == "__main__":
	main()