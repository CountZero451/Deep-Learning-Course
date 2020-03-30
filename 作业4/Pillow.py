from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

img=Image.open("C:\\Users\\OnlyS\\Desktop\\神经网络作业\\作业4\\lena.tiff")
img_r,img_g,img_b=img.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis("off")
x=img_r.resize((64,64))
plt.imshow(x,cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
plt.axis("off")
y=img_g.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
plt.imshow(y,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
z=img_b.crop((0,0,400,400))
plt.imshow(z,cmap="gray")
plt.title("B-裁剪",fontsize=14)

img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.subplot(224)
plt.axis("off")
plt.imshow(img_rgb)
plt.title("RGB",fontsize=14)
img_rgb.save("C:\\Users\\OnlyS\\Desktop\\神经网络作业\\作业4\\test.png")

plt.suptitle("图像基本操作",fontsize=20,color="blue")
plt.show()