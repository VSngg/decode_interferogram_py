# %%
from skimage import io
from skimage.filters import gaussian, roberts
from matplotlib import pyplot as plt

img = io.imread("images/1.png", as_gray=True)

# длина волны монохромного излучения 
waveLength = 635
# реальная видимая ширина в окуляре микроскопа
realLength = 3000

# %%
# сколько раз надо пропустить фото через фильтр Гаусса
nGaussian = 11
gaussianImg = gaussian(img, nGaussian)
plt.imshow(gaussianImg, cmap='gray')

# %%
fig, axes = plt.subplots(nrows=2, ncols=2, 
        sharex=True, sharey=True, figsize=(8, 8))

ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Оригинал')

g1=gaussian(img, 1)
ax[1].imshow(g1,cmap=plt.cm.gray)
ax[1].set_title('1')

g2=gaussian(img, 7)
ax[2].imshow(g2,cmap=plt.cm.gray)
ax[2].set_title('7')

g3=gaussian(img, 11)
ax[3].imshow(g3,cmap=plt.cm.gray)
ax[3].set_title('11')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
