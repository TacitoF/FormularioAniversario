import qrcode

link_do_site = ""

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link_do_site)
qr.make(fit=True)

img = qr.make_image(back_color="white")

# Salva o arquivo na pasta do seu projeto
img.save("NOMEDOARQUIVO.png")

print("✅ QR Code gerado com sucesso!")