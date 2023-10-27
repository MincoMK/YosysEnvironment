import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1167333653504851978/2QW80l5Nf4j3t_G56jF1EzH8nVUY0dDtK4y0pDemiQmXt7Z3-64aW2rwVi1wmPyd6HnY"
requests.post(WEBHOOK_URL, files={"net.png": open("net.png", "rb")})