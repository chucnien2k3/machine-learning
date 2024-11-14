from PIL import Image
img = Image.open(r"D:\Đại học\Năm 3\học máy\TayTrain1\tay-training-dataset\13079.png")
angle = 356
rotate_img= img.rotate(angle, expand = True)
rotate_img.show()