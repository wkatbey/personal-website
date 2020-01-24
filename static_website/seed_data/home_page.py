from ..models import *
import os, os.path

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

def get_intro_text():
	text = ''
	url = os.path.join(SITE_ROOT, 'text_files', 'home_page_intro')

	with open(url, 'r') as input:
		for line in input:
			if '-- TEXT END --' in line:
				break
			else:
				text += line

	return text


def get_discover_my_work_text():
	text = ''
	url = os.path.join(SITE_ROOT, 'text_files', 'discover_my_work')

	with open(url, 'r') as input:
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

	url = os.path.join(SITE_ROOT, 'text_files', 'lets_get_in_contact')

	with open(url, 'r') as input:
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



class HomePageFileLoader():

	def __init__(self):
		self.discover_my_work_section_text = ''
		self.lets_get_in_contact_section_text = []


		self.discover_my_work_section = None
		self.lets_get_in_contact_section = None
		self.home_page = None


	def seed_home_page(self):
		self.seed_page_sections()

		intro_text = get_intro_text()

		home_page = HomePage(
			intro=intro_text
		)

		home_page.save()

		home_page.page_sections.add(
			*[
				self.discover_my_work_section,
				self.lets_get_in_contact_section
			]
		)

		return home_page


	def seed_page_sections(self):
		self.seed_section_text()

		self.discover_my_work_section = PageSection(
			heading='Discover my work',
			heading_icon='https://img.icons8.com/nolan/64/cafe.png'
		)

		self.lets_get_in_contact_section = PageSection(
			heading="Let's get in contact",
			heading_icon='https://img.icons8.com/nolan/64/contacts.png'
		)

		self.discover_my_work_section.save()
		self.lets_get_in_contact_section.save()


		self.discover_my_work_section.text.add(
			self.discover_my_work_section_text
		)

		self.lets_get_in_contact_section.text.add(
			*[
				self.lets_get_in_contact_section_text[0],
				self.lets_get_in_contact_section_text[1]
			]
		)


	def seed_section_text(self):
		discover_my_work_text = get_discover_my_work_text()
		let_get_in_contact_texts = get_lets_get_in_contact_texts()

		self.discover_my_work_section_text = PageSectionText(
			value=discover_my_work_text,
			col_length=12
		)

		self.lets_get_in_contact_section_text = [
			PageSectionText(
				value=let_get_in_contact_texts[0],
				col_length=4
			),
			PageSectionText(
				value=let_get_in_contact_texts[1],
				col_length=7
			)
		]

		self.discover_my_work_section_text.save()
		self.lets_get_in_contact_section_text[0].save()
		self.lets_get_in_contact_section_text[1].save()


