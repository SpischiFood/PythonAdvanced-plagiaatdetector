from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = env.get_template("plagiaattemplate.html")

# hard_auteurs = [
#    "Jef Baker",
#    "Jasper Jansens",
#    "Cas Van den Bergh",
#    "Vic Verhasselt",
#    "Jonas Kerings",
# ]
#
# hard_opmerkingen = {
#    auteur[1]: {auteurin: [] for auteurin in hard_auteurs[auteur[0] + 1 :]}
#    for auteur in enumerate(hard_auteurs[:-1])
# }
#
# hard_opmerkingen["Jef Baker"]["Jasper Jansens"].append("zelfde file")
# hard_opmerkingen["Jef Baker"]["Cas Van den Bergh"].append("zelfde fout")
# hard_opmerkingen["Jasper Jansens"]["Vic Verhasselt"].append("zelfde spelfout: 'pithon'")
# hard_opmerkingen["Jef Baker"]["Vic Verhasselt"].append("zelfde syntax-fout")
# hard_opmerkingen["Jef Baker"]["Vic Verhasselt"].append("zelfde syntax file")
# hard_opmerkingen["Cas Van den Bergh"]["Jonas Kerings"].append("zelfde spelfout: 'aray'")
#
#
# hard_aliassen = {
#    auteur[1]: f"Student {auteur[0]}" for auteur in enumerate(hard_auteurs, 1)
# }


# print("Geef een directory van een opdracht in: ")
direc = Path(input())

if not direc.is_dir():
    print("Dit is geen directory.")
else:
    auteurs = [dir.name for dir in direc.iterdir()]
    aliassen = {auteur[1]: f"Student {auteur[0]}" for auteur in enumerate(auteurs, 1)}
    opmerkingen = {
        auteur[1]: {auteurin: [] for auteurin in auteurs[auteur[0] + 1 :]}
        for auteur in enumerate(auteurs[:-1])
    }

    for auteurrij in enumerate(auteurs[:-1]):
        for auteurkolom in auteurs[auteurrij[0] + 1 :]:
            mapauteur1 = direc / auteurrij[1]
            file_auteur1 = [pad for pad in mapauteur1.glob("*.py") if pad.is_file()]
            mapauteur2 = direc / auteurkolom
            file_auteur2 = [pad for pad in mapauteur2.glob("*.py") if pad.is_file()]
            # print(file_auteur1)
            # print(file_auteur2)

            if len(file_auteur1) != 1 or len(file_auteur2) != 1:
                opmerkingen[auteurrij[1]][auteurkolom].append(
                    "vergelijking onmogelijk: onverwachte bestandstructuur"
                )
            elif file_auteur1[0].read_bytes() == file_auteur2[0].read_bytes():
                opmerkingen[auteurrij[1]][auteurkolom].append(
                    f"identieke file: {file_auteur1[0].name}"
                )

    print(template.render(auteurs=auteurs, opmerkingen=opmerkingen, aliassen=aliassen))
