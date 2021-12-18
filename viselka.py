import random

words = {
	"яблочко": "зеленый/желтый/красный фрукт",
	"бананан": "желтый огурец",
	"моркофка": "заячий овощ"
}


def result_word(word, chars):
	hidden_word = ''.join(c.upper() if c in chars else '$' for c in word)
	return hidden_word


def show_task(word, description, chars, try_count):
	if chars:
		print("_" * 40)
	print(f"Загаданое слово [{description}] => {result_word(word, chars)}")
	print(f"Неправильных попыток осталось: { try_count }")
	print(f"Были введены буквы: [{ ' '.join(chars) }]" if chars else "")


while len(words):
	word = random.choice(list(words.keys()))
	description = words.pop(word)
	try_count = 3
	chars = []
	print('=' * 80)
	show_task(word, description, chars, try_count)
	while try_count:
		char = input('\n Введите любую букву (или * для завершения):')
		if char == '*':
			print("Finita")
			quit()
		if char in chars:
			print("Такая буква уже была, попробуйте еще раз")
			continue
		chars.append(char)
		if char not in word:
			try_count = try_count - 1
		
		show_task(word, description, chars, try_count)

		if not try_count:
			print("\n\n !!! Игра окончена. Слово не отгадано. Доигрался. !!!")

		if not set(word) - set(chars):
			print("\n\n ... Повезло. Угадал ...")
			break
		



