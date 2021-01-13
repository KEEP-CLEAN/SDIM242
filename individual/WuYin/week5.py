
import wave
def saveAudio(filename,data):
    with wave.open(filename + '.wav', 'wb') as wavfile:
        wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(data)

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['figure.figsize']=(15,8)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.5, hspace=0.5)


x=np.arange(0,5,.00005)
y=np.sin(2000*np.pi*x)
noise=np.random.rand(len(x))


saveAudio("原音频",y)


y=y+noise
saveAudio("加噪音",y)


ft_y=np.fft.fft(y)
n = len(y) 


avg=np.max(abs(ft_y[1:]))/2


plt.subplot(222)
plt.title("降噪前的频率振幅谱")
plt.plot(abs(ft_y))

ft_y[0]=0+0j
ft_y[np.where(abs(ft_y)<=avg)]=0+0j

saveAudio("去噪音",np.fft.ifft(ft_y))

plt.subplot(221)
plt.title("加了噪音的原音频")
plt.plot(y)

plt.subplot(223)
plt.plot(abs(ft_y))
plt.title("降噪后的频率振幅谱")
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.subplot(224)
plt.title("降噪后的音频")
plt.plot(np.fft.ifft(ft_y))

plt.show()