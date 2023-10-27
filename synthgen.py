import os

files = os.scandir('.')
i = 0
for file in files:
    if file.name.endswith(".v"):
        synth = ""
        synth += f"read_verilog -sv {file.path}\n"
        synth += f"""proc
opt
memory
opt
techmap
opt
splitnets
opt
write_json net{i}.json"""
        with open(f"synth{i}.ys", "w") as f:
            f.write(synth)
        system(f"yosys synth{i}.ys")
        i += 1



print("[SYNTHGEN] SUCCESS")