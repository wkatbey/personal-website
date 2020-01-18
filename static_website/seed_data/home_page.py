from .models import *

def get_intro_text():
	text = ''

	with open('./text_files/home_page_intro', 'r') as input:
		for line in input:
			if '-- TEXT END --' in line:
				break
			else:
				text += line

	return text

def get_discover_my_work_text():
	text = ''

	with open('./text_files/discover_my_work', 'r') as input:
		for line in input:
			if '-- TEXT END --' in line:
				break
			else:
				text += line

	return text

def get_lets_get_in_contact_texts():
	first_col_text = ''
	second_col_text = ''

	at_second_col = False

	with open('./text_files/let_get_in_contact', 'r') as input:
		for line in input:
			if '-- TEXT END --' in line:
				break
			elif '-- TEXT DIVIDER --' in line:
				at_second_col = True
			else:
				if at_second_col:
					second_col_text += line
				else:
					first_col_text += line
	
	return [ first_col_text, second_col_text ]



def get_default_home_page():
	discover_my_work_text = get_discover_my_work_text()
	let_get_in_contact_texts = get_lets_get_in_contact_texts()

	page_sections = [
		PageSection(
			heading='Discover my work',
			heading_icon='https://img.icons8.com/nolan/64/cafe.png',
			text = [
				PageSectionText(
					value=discover_my_work_text
					cols=12
				)
			]
		),
		PageSection(
			heading="Let's get in contact",
			heading_icon='https://img.icons8.com/nolan/64/contacts.png',
			text =[
				PageSectionText(
					value=let_get_in_contact_texts[0],
					cols=4
				),
				PageSectionText(
					value=let_get_in_contact_texts[1],
					cols=7
				)
			]
		)
	]

	home_page = HomePage(
		intro=default_intro,
		page_sections=page_sections
	)

	return home_page




