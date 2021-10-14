
#-----Комбінаторика-----


def factorial(natural,first_natural = 1):
	formul = "Pn = n! = 1*"
	answer = 1
	while int(first_natural)!=int(natural):
		first_natural+=1
		answer *= first_natural
		formul += "{}*".format(first_natural)
	return (answer,formul[:-1])


def fixed_factorial(n,k):
	formul = "A(n k) = N*(n-1)...(n-k+1) = {}*".format(n)
	end = int(n-k+1)
	interval = n-end
	data = 1
	answer = 1
	if interval >1:
		for i in range(interval):
			answer *=(n-data)
			formul += "{}*".format(n-data)
			data+=1
		answer *=n
	if interval == 1:
		answer = n*(n-1)
		formul += "{}*".format(n-1)
	if interval == 0:
		answer = n
	return (answer,formul[:-1])


def combinate_factorial(n,k):
	main_formul = "C(k,n) = A(n,k)/P(n) = "
	a = fixed_factorial(n,k)
	p = factorial(k)
	answer = a[0]/p[0]
	main_formul += "{}/{}".format(a[0],p[0])
	formul = "\n\n{} = {}\n\n{} = {}\n\n{}".format(p[1],p[0],a[1],a[0],main_formul)
	return (answer,formul)


def main():
	print("---Виберіть дію---\n1 - Знайти Кількість переміщень позицій\n2 - Знайти кількість переміщень розташованих в певному порядку\n3 - Знайти кількість можливих комбінацій переміщень")
	data = int(input("1, 2, 3?: "))
	if data == 1:
		action = int(input("\033[31mВведіть число можливих позицій: \n"))
		data = factorial(action)
		print("\033[33m\nВаша відповідь: {} = {}".format(data[1],data[0]))
		return
	if data == 2:
		action = int(input("\033[31mВведіть кількість позицій: \n"))
		action2 = int(input("\033[31mВведіть кількість об'єктів: \n"))
		data = fixed_factorial(action,action2)
		print("\033[33m\nВаша відповідь: {} = {}".format(data[1],data[0]))
		return
	if data == 3:
		action = int(input("\033[31mВведіть кількість позицій: \n"))
		action2 = int(input("\033[31mВведіть кількість об'єктів: \n"))
		data = combinate_factorial(action,action2)
		print("\033[33m\nВаша відповідь: {} = {}".format(data[1],data[0]))
		return
	else:
		print("Ви ввели число якого немає в списку, перезапустіть програму та спробуйте ще раз")
		return
	print(1)

if __name__ == "__main__":
	main()