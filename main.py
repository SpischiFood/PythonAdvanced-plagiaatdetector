from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = env.get_template("plagiaattemplate.html")

auteurs = [
    "Jef Baker",
    "Jasper Jansens",
    "Cas Van den Bergh",
    "Vic Verhasselt",
    "Jonas Kerings",
]

# oude_opmerkingen = {
#    ("auteur1", "auteur2"): ["zelfde file"],
#    ("auteur1", "auteur3"): ["zelfde fout"],
#    ("auteur1", "auteur4"): ["zelfde spelfout: 'pithon'"],
#    ("auteur2", "auteur4"): ["zelfde syntax-fout", "zelfde file"],
# }

opmerkingen = {
    auteur[1]: {auteurin: [] for auteurin in auteurs[auteur[0] + 1 :]}
    for auteur in enumerate(auteurs[:-1])
}

opmerkingen["Jef Baker"]["Jasper Jansens"].append("zelfde file")
opmerkingen["Jef Baker"]["Cas Van den Bergh"].append("zelfde fout")
opmerkingen["Jasper Jansens"]["Vic Verhasselt"].append("zelfde spelfout: 'pithon'")
opmerkingen["Jef Baker"]["Vic Verhasselt"].append("zelfde syntax-fout")
opmerkingen["Jef Baker"]["Vic Verhasselt"].append("zelfde syntax file")
opmerkingen["Cas Van den Bergh"]["Jonas Kerings"].append("zelfde spelfout: 'aray'")


aliassen = {auteur[1]: f"Student {auteur[0]}" for auteur in enumerate(auteurs, 1)}


# print(aliassen_oud == aliassen_nieuw)

print(template.render(auteurs=auteurs, opmerkingen=opmerkingen, aliassen=aliassen))
