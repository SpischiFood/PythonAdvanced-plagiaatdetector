from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = env.get_template("plagiaattemplate.html")

auteurs = ["auteur1", "auteur2", "auteur3", "auteur4"]

opmerkingen = {
    ("auteur1", "auteur2"): ["zelfde file"],
    ("auteur1", "auteur3"): ["zelfde fout"],
    ("auteur1", "auteur4"): ["zelfde spelfout: 'pithon'"],
    ("auteur2", "auteur4"): ["zelfde syntax-fout", "zelfde file"],
}


print(template.render(auteurs=auteurs, opmerkingen=opmerkingen))
