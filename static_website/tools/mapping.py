def construct_home_page_from_model(home_page):
	if home_page is None:
		return {
			'intro': '',
			'page_sections': []
		}
	else:
		page_sections = []

		for page_section in home_page.page_sections.all():
			page_sections.append(construct_page_section_from_model(page_section)) 

		return {
			'intro': home_page.intro,
			'page_sections': page_sections,
		}

def construct_page_section_from_model(page_section):
	return {
		'heading': page_section.heading,
		'heading_icon': page_section.heading_icon,
		'text': page_section.text.all(),
	}