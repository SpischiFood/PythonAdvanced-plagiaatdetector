from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("plagiaattemplate.html")

auteurs = ['auteur1', 'auteur2', 'auteur3', 'auteur4']

print(template.render(auteurs = auteurs))