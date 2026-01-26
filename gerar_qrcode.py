import qrcode

link_do_site = "https://sofiafaz5.vercel.app/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link_do_site)
qr.make(fit=True)

img = qr.make_image(fill_color="#8e44ad", back_color="white")

# Salva o arquivo na pasta do seu projeto
img.save("qrcode_convite.png")

print("✅ QR Code gerado com sucesso como 'qrcode_convite.png'!")