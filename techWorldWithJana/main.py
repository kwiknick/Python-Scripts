import requests

response = requests.get("https://gitlab.com/api/v4/users/kwiknick/projects")

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project URL: {project['web_url']}")
