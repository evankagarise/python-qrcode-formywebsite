import qrcode

img = qrcode.make("Hellow World! This is Evan")
img.save("mycode.png")