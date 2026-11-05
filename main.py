from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = env.get_template("plagiaattemplate.html")

auteurs = ["auteur1", "auteur2", "auteur3", "auteur4"]

oude_opmerkingen = {
    ("auteur1", "auteur2"): ["zelfde file"],
    ("auteur1", "auteur3"): ["zelfde fout"],
    ("auteur1", "auteur4"): ["zelfde spelfout: 'pithon'"],
    ("auteur2", "auteur4"): ["zelfde syntax-fout", "zelfde file"],
}

opmerkingen = {
    auteur[1]: {auteurin: [] for auteurin in auteurs[auteur[0] + 1 :]}
    for auteur in enumerate(auteurs[:-1])
}

opmerkingen["auteur1"]["auteur2"].append("zelfde file")
opmerkingen["auteur1"]["auteur3"].append("zelfde fout")
opmerkingen["auteur2"]["auteur4"].append("zelfde spelfout: 'pithon'")
opmerkingen["auteur1"]["auteur4"].append("zelfde syntax-fout")
opmerkingen["auteur1"]["auteur4"].append("zelfde syntax file")


# print(opmerkingen)

print(template.render(auteurs=auteurs, opmerkingen=opmerkingen))
