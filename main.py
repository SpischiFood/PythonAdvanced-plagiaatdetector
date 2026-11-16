from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
import re

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

template = env.get_template("plagiaattemplate.html")


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
            else:
                inhoud1 = file_auteur1[0].read_text(encoding="utf-8")
                inhoud2 = file_auteur2[0].read_text(encoding="utf-8")
                comments1 = re.findall(r"#[ \t]*(?P<comment>.+)", inhoud1)
                comments2 = re.findall(r"#[ \t]*(?P<comment>.+)", inhoud2)
                for comment in comments1:
                    if comment in comments2:
                        opmerkingen[auteurrij[1]][auteurkolom].append(
                            f"identieke comment: {comment}"
                        )

    print(template.render(auteurs=auteurs, opmerkingen=opmerkingen, aliassen=aliassen))
