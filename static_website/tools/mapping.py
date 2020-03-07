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

def construct_current_projects_section_from_model(current_projects_section):
	if current_projects_section is None:
		return {
			'heading': '',
			'heading_icon': '',
			'projects': []
		}
	else:
		projects = []

		for project in current_projects_section.projects:
			projects.append(construct_current_project_from_model(project))

		return {
			'heading': current_projects_section.heading,
			'heading_icon': current_projects_section.heading_icon,
			'projects': projects
		}

def construct_current_project_from_model(current_project):
	return {
		'heading': current_project.heading,
		'tech_stack': current_project.tech_stack,
		'description': current_project.description
	}