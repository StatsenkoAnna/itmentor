from random import choice
from cfg_reader import read_cfg

def get_random_word(word_list):
	''' Функция выбирает рандомное слово из списка слов'''
	return choice(word_list)
    
def get_guess(used_letters):
	'''Обработка ввода пользователя
На вход подается список использованных букв
На выходе валидный ввод от пользователя (буква
	'''
	while True:
		guess = input("Введите букву: ").lower()
		if len(guess) != 1:
			print("Пожалуйста, введите одну букву.")
		elif guess in used_letters:
			print("Вы уже пробовали эту букву. Попробуйте другую.")
		elif not guess.isalpha() or not 'а' <= guess <= 'я':
			print("Пожалуйста, введите русскую букву.")
		else:
			return guess

def display_game(secret_word, used_letters, mistakes, configs):
	''' Отрисовка игры в консоли'''
	print("Осталось попыток: {}".format(int(configs["max_retries"]) - mistakes))
	word = ["*"] * len(secret_word)
	for i, letter in enumerate(secret_word):
		if letter in correct_letters:
			word[i] = letter
    
	print(' '.join(word))
	print("Использованные буквы: ", used_letters)
	print(configs["hangman"][mistakes])
	
def is_correct_word(correct_letters, secret_word):
	'''Функция проверяет соответствует ли ввод пользователя загаданному слову
   Внутри какая-то магия с типами данных
	'''
	cl = sorted(correct_letters)
	sw = list(sorted(secret_word))
	cl_word = ''.join(cl)
	sw_word = ''.join(sw)
	return cl_word == sw_word
	
def play_again():
	'''Хочет ли пользователь сыграть еще раз'''
	return input("Хотите сыграть снова? (да или нет): ").lower().startswith('д')

# чтение конфигов
configs = read_cfg("config.cfg")
words = configs["list_of_words"]

while True:
	mistakes = 0
	wrong_letters = []
	correct_letters = []

	game_over = False
	secret_word = get_random_word(words)


	while not game_over: # пока одна игра не окончена
		used_letters = wrong_letters + correct_letters
		display_game(secret_word, used_letters, mistakes, configs)
		guess = get_guess(used_letters)
		if guess in secret_word:
			correct_letters.append(guess)
			if is_correct_word(correct_letters, secret_word):
				print(f"Поздравляем! Вы угадали слово: {secret_word}")
				game_over = True
			
		else:
			wrong_letters.append(guess)
			mistakes += 1 
			if len(wrong_letters) >= configs["max_retries"]:
				display_game(secret_word, used_letters, mistakes, configs)
				print(f"Вы проиграли! Загаданное слово было: {secret_word}")
				game_over = True
	
	if not play_again():
		break
	
	
	
			
