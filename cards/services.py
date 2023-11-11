import csv

def get_cards_from_folder(folder):
	file_path = folder.cards.path

	with open(file_path, encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=';')
		cards_list = [pair for pair in reader]

	return cards_list

def write_cards_in_form(cards_list, form):
	cards_list = [';'.join(card) for card in cards_list]
	cards_list_as_string = '\n'.join(cards_list)
	card_form = form(initial={'file_text':cards_list_as_string})

	return card_form

def write_cards_in_folder(cards_list, folder):
	file_path = folder.cards.path
	with open(file_path, 'w', encoding='utf-8') as file:
		for card in cards_list:
			file.write(f'{card}\n')

def serialize_cards(form, folder):
	form_data = form.data['file_text']
	cards_list = form_data.split('\n')
	cards_list = [card.replace('\r', '') for card in cards_list]
	return cards_list

		