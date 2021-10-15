#---- Функція для знаходження факторіла(Кількість можливих переміщень позицій) ----
def factorial(natural,first_natural = 1):
	formul = "Pn = n! = 1*"
	answer = 1
	while int(first_natural) != int(natural):
		first_natural += 1
		answer *= first_natural
		formul += "{}*".format(first_natural)
	return (answer,formul[:-1])


#---- Функція для знаходження можливих позицій розташованих в певному порядку ----
def fixed_factorial(n,k):
	formul = "A(n k) = N*(n-1)...(n-k+1) = {}*".format(n)
	interval = n - (n - k + 1)
	data, answer = 1, 1
	if interval > 1:
		for i in range(interval):
			answer *= (n - data)
			formul += "{}*".format(n - data)
			data += 1
		answer *= n
	if interval == 1:
		answer = n * (n - 1)
		formul += "{}*".format(n - 1)
	if interval == 0:
		answer = n
	return (answer, formul[:-1])


#---- Функція для знаходження всіх можливих комбінацій елементів ----
def combinate_factorial(n,k):
	main_formul = "C(k,n) = A(n,k)/P(n) = "
	a, p = fixed_factorial(n, k), factorial(k)
	answer = a[0] / p[0]
	main_formul += "{}/{}".format(a[0], p[0])
	formul = "\n\n{} = {}\n\n{} = {}\n\n{}".format(p[1], p[0], a[1], a[0], main_formul)
	return (answer, formul)