# import qrcode

# user_url = input("Enter the text or URL: ").strip()
# user_file = input("Enter the filename: ").strip()

# img = qrcode.make(user_url)
# if user_file.endswith('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.ico', '.tiff', '.tif'):
#     img.save(user_file)
# else:
#     print("Invalid file name!")
# print("OR code save as", user_file)





# using QR module 

import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_ground='white')
image.save(filename)
print(f'QR code save as {filename}')