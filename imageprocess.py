import os

files = os.scandir('.')
i = 0
for file in files:
    if file.name.endswith(".json"):
        os.system(f"netlistsvg {file.path} -o net{i}.svg")
        os.system(f"convert -background white -alpha remove -alpha off net{i}.svg net{i}.png")
        print(f"[SYNTHGEN] Generated net{i}.png")
        i += 1