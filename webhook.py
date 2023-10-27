import requests, os

WEBHOOK_URL = "https://discord.com/api/webhooks/1167333653504851978/2QW80l5Nf4j3t_G56jF1EzH8nVUY0dDtK4y0pDemiQmXt7Z3-64aW2rwVi1wmPyd6HnY"
requests.post(WEBHOOK_URL, json={"content": "Synthesis complete!"})
files = os.scandir('.')
for file in files:
    if file.name.endswith(".png"):
        requests.post(WEBHOOK_URL, files={"net": open(file.path, "rb")})
        print(f"[SYNTHGEN] Uploaded {file.path}")