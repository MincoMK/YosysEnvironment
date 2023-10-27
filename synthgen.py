import os

synth = ""

files = os.scandir('.')
for file in files:
    if file.name.endswith(".v"):
        synth += f"read_verilog -sv {file.path}\n"

synth += """proc
opt
memory
opt
techmap
opt
splitnets
opt
write_json net.json"""

with open("synth.ys", "w") as f:
    f.write(synth)

os.system("yosys synth.ys")

print("[SYNTHGEN] SUCCESS")