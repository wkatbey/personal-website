from ..models import CurrentProjectsSection, CurrentProject
import os, os.path

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

def get_current_projects_text():
	url = os.path.join(SITE_ROOT, 'text_files', 'current_projects')
	project_count = 0
	projects = []
	index = 0

	with open(url, 'r') as input:
		for line in input:
			if '-- TEXT END --' in line:
				break
			elif '-- TEXT DIVIDER --' in line:
				index += 1
			elif '-- PROJECT COUNT --' in line:
				project_count = line[-1]
				projects = [''] * project_count
				print("Project Count" + project_count)
			else:
				projects[index] += line

	return projects;
				