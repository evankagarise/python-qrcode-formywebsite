import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("https://evankagarise.com", image_factory=factory)
svg_img.save("myqr.svg")
