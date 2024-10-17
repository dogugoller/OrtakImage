"""

#Özellik Algılama

SIFT = Ölçekten bağımsız özellikleri algılayan algoritmadır. Farklı çözünürlüklerde dahi aynı özellikleri tespit edebilir.
SURF = SIFT'ın hızlı versiyonudur. Hızın ön planda olduğu noktalarda tercih edilir.
ORB = SIFT ve ORB'dan daha hızlı çalışır. Açısal ve dönmelere karşı dayanıklıdır.

#Özellik Tanımlama
Özellikler algılandıktan sonra bu özelliklerin tanımlanması gerekir. Tanımlayıcı, her bir özellik için
bir özet oluşturur ve bu sayede farklı görüntülerdeki özellikler karşılaştırılabilir hale gelir. "Tanımlayıcılar genelde vektöreldir."
"Bir dizi sayısal veri sunar."

SIFT = Algıladığı özellikleri vektörlerle tanımlar.
BRIEF = Özellikleri ikili (binary) vektörlerle tanımlar. Daha hızlı karşılaştırma yapma imkanı sunar.


#Özellik Eşleştirme
Bir görüntüde bulunan özellikleri başka bir görüntüdeki özelliklerle eşleştirme işlemidir.
İki görüntüdeki benzer noktalar karşılaştırılarak, aynı veya benzer özellikler eşleştirilir. "Nesne tanıma, görüntü hizalama, mozaik oluşturma".

Eşleştirme Yöntemleri:

Brute-Force Matcher : Her bir özellik vektörünü diğer görüntüdeki tüm zeölliklerle karşılaştırır ve en yakın olanı bulur.
FLANN = Büyük veri kümeleri üzerinde hızlı eşleştirme yapmak için kullanılır.

"""

#Harris köşe tespiti

import cv2
import numpy as np

img = cv2.imread("gorsel.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

GRAY = np.float32(gray)
kose = cv2.cornerHarris(GRAY,2,3,0.03)

img[kose>0.01*kose.max()] = [0,255,0]
cv2.imshow("Harris",img)
cv2.imwrite("HarrisKoseAlgilama.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()