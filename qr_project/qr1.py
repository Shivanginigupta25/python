import qrcode as qr

img = qr.make("https://chatgpt.com/c/696a1701-d0c4-8326-8f0a-6424696eefbe")
img.save("chatgpt.png")
