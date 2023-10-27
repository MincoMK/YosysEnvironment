import os

files = os.scandir('.')
i = 0
for file in files:
    if file.name.endswith(".v"):
        synth = ""
        synth += f"read_verilog -sv {file.path}\n"
        synth += f"proc\nopt\nmemory\nopt\ntechmap\nopt\nsplitnets\nwrite_json net{i}.json"
        with open(f"synth{i}.ys", "w") as f:
            f.write(synth)
        print(f"[SYNTHGEN] Generated synth{i}.ys")
        os.system(f"yosys synth{i}.ys")
        i += 1



print("[SYNTHGEN] SUCCESS")