import os
import os.path
from ..models import CurrentProject, CurrentProjectsSection

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

class CurrentProjectsFileLoader:
	def __init__(self):
		self.project_descriptions = []
		self.load()

	def load(self):
		url = os.path.join(SITE_ROOT, 'text_files', 'current_projects')
		index = 0

		with open(url, 'r') as file_input:
			for line in file_input:
				if '-- TEXT END --' in line:
					break
				elif '-- TEXT DIVIDER --' in line:
					index += 1
				elif '-- PROJECT COUNT --' in line:
					project_count = int(line[-1])
					self.project_descriptions = [''] * project_count
					print("Project Count" + str(project_count))
				else:
					self.project_descriptions.append(line)

	def seed_current_projects_section(self):

		personal_website, sapphire_blogging = self.seed_current_projects()

		section = CurrentProjectsSection(
			heading="What I''m Currently working on",
			heading_icon="<i class='material-icons heading-icon'>code</i>",
		)

		section.save()

		section.projects.add(
			personal_website,
			sapphire_blogging
		)

		return section


	def seed_current_projects(self):
		personal_website = CurrentProject(
			heading='Portfolio & Blogging App',
			tech_stack='Django, PostgreSQL, hosted through Heroku',
			description=self.project_descriptions[0]
		)

		sapphire_blogging = CurrentProject(
			heading='Sapphire Blogging',
			tech_stack='Django, Vue, PostgreSQL, to be hosted through Heroku',
			description=self.project_descriptions[1]
		)

		personal_website.save()
		sapphire_blogging.save()

		return personal_website, sapphire_blogging