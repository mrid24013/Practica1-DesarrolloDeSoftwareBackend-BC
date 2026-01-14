import qrcode
#import qrcode.image.svg

texto = input("Ingrese el texto para generar el codigo QR: \n")
img = qrcode.make(texto)
#type(img)  # qrcode.image.pil.PilImage
img_name = input("Ingrese nombre para IMG: \n")
img.save(img_name + ".png")

'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('Some data here', image_factory=factory)
'''