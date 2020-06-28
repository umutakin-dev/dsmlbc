# **DATA SCIENCE AND MACHINE LEARNING BOOTCAMP**  

## **DATA LITERACY**  

### **Veri Okuryazarligi Nedir?**

Gunluk hayatta veriyle temas ettigimiz ilk anlardaki basit veri yorumlama kabiliyetleridir.  
Her turden veri tipini, degisken ve olcek turlerini tanimlayabilme, betimsel istatistikleri ve istatistiksel grafikleri kullanarak veri degerlendirebilme yetenegidir.  
- Veri gorsellestirme  
   
### **Temel Kavramlar**

#### **Population and Sample -Populasyon ve Orneklem**

Populasyon -> Ana Kitle  
Orneklem   -> Ana Kitle icinden secilen, Ana Kitleyi temsil eden ornek grubu  

Amac, populasyon icinden, yuksek temsil gucune sahip, yansiz oldugunu dusundugumuz bir orneklem cekmek.  
Ana Kitle icinden Orneklem cekmek icin kullanilan yontemler:  

- Tabakali Ornekleme  
- Rastgele Ornekleme  

Ornek:  
  - Secim calismalari, 80 milyon kisi icin 2500 kisilik orneklem.  
	
#### **Observation Unit - Gozlem Birimi**

Arastirmada inceledigimiz birimler.  
Populasyonun icinden sectigimiz orneklemin her bir elemani, bizim gozlem birimimiz olur.  

Ornek:  
  - Secim calismasi sirasinda, anket yapilan herkes bir kisi, bir gozlem birimidir.  
  - Incelenen veri tabanindaki her bir satir, bir gozlem birimidir.  

#### **Variables and Variable Types - Degiskenler ve Degisken Turleri**

**- Variable - Degisken**  

Birimden birime farkli deger alan niceliktir.  

Ornek:  
  - Incelenen veri tabanindaki her bir sutun, bir degiskendir.  

**- Variable Types - Degisken Turleri:**  

- Sayisal Degiskenler (Nicel, Kantitatif) (Sayilabilir, Yoruma Acik Olmayan) : Numeric tipteki veriler  
- Kategorik Degiskenler (Nitel, Kalitatif) (Sinifsal, Yoruma Acik)           : String tipindeki veriler  

Ornek:  
- Cinsiyet bir kategorik degiskendir; Kadin ve Erkek bu kategorik degiskenin siniflaridir.  

#### **Olcek Turleri**

Bir degiskenin degerlerini insan olarak okuyup anlayabilmek icin, bunlari olcmemiz gerekiyor.  
- Sayisal Degiskenler icin  : Aralik ve Oran  
- Katagorik Degiskenler icin: Nominal ve Ordinal  

**- Aralik Oran (Sayisal Degiskenler):**

- Aralik: Baslangic noktasi sifir olmayan sayisal degiskenlerin olcek turu.  
  - orn;  
    - Sicaklik  
	
- Oran: Baslangic noktasini sifir kabul eden sayisal degiskenlerin olcu turlerine denir.  
  - orn;  
    - Arac Fiyati: 0-50k, KM: 0-100k  
	
**- Nominal Ordinal (Kategorik Degiskenler):**

- Nominal  
Kategorik degiskenlerin, siniflari arasinda bir fark yok ise, buna nominal olcek turu diyoruz.  
  - orn;  
    - Cinsiyet; Kadin, Erkek  
	
- Ordinal  
Siniflar arasinda fark olmasi durumundaki olcu turune ise ordinal olcu turu diyoruz.  
Kategorik degiskenin siniflari arasinda bir mesafe olmasi gerektigi durumlarda, bu mesafenin ifade edilmesi icin, bu kategorik degiskenin, olcek turu, ordinal olcek turu olacaktir.  
  - orn;
    - Rutbe; Onbasi, Yuzbasi, Binbasi, Albay
	- Egitim Durumu; Ilkokul, Ortaokul, Lise, Lisans, Yuksek Lisans, Doktora
	
**- Ozet:**

- Veri

  - Kategorik
  
    - Nominal
    - Ordinal
	
  - Sayisal
  
     - Aralik (Interval)
	 - Oran (Ratio)

### **Merkezi Egilim Olculeri**

#### **Arithmetic Mean - Aritmetik Ortalama**

Bir seride (degiskende) yer alan tum degerlerin toplanmasi ve birim sayisina bolunmesi ile elde edilen istatistiktir.  

  - orn;  
  
    - 13, 10, 15, 12, 17, 13  
      (13 + 10 + 15 + 12 + 17 + 13) / 6 = 13,33  
    
	- butun kullanicilarin bir sitede gecirdikleri sure / kullanici sayisi = ortalama gecirilen sure  

#### **Median - Medyan**

Bir seriyi kucukten buyuge ve ya buyukten kucuge siraladigimizda tam orta noktadan seriyi iki esit parcaya ayiran degere medyan adi verilir.  

Terim sayisi:  
- Tek ise  => Medyan = ((n+1)/2).terim  
- Cift ise => Medyan = (((n/2).terim+((n/2+1).terim)/2  

- orn;  

  - 13, 10, 15, 12, 17  
    10, 12, 13, 15, 17  
    Medyan = (n+1)/2 = (5+1)/2 = 3 -> = 13  
	
  - 13, 10, 15, 12, 17, 13  
    10, 12, 13, 13, 15, 17  
    Medyan = (((n/2).terim+((n/2+1).terim)/2  
           = (3.terim+4.terim)/2  
           = (13 + 13) / 2 = 26 / 2 = 13  

#### **Medyan ve Ortalama Karsilastirmasi**

Aritmetik Ortalama, seri dagiliminin (degiskenin dagiliminin) simetrik oldugu bilindiginde kullanilabilir, aksi takdirde medyan kullanilabilir.  

- orn;  

  - 13, 10, 15, 12, 17, 12, 19, 18, 11, 12, 190  
	Ortalama = 28,5  
	Medyan   = 13  
	Boyle bir veri kumesi ile calisirken, medyan kullanilmalidir, cunku veri kumesi simetrik degildir. Ortalama degeri olan 28,5 alinsa bile, veri kumesinin icinde bu degere yakin hicbir eleman yoktur.  

#### **Mode - Mod**

Bir seride (degiskende) en cok tekrar eden (frekansi en cok olan)  degere Mod adi verilir.  
- orn;  
  - 13, 10, 13, 12, 17, 13, 14  
	10 -> 1  
    12 -> 1  
    13 -> 3 -> Mod = 13  
    14 -> 1  
    17 -> 1  

#### **Quantilles - Kartiller**

Kucukten buyuge siralana bir seriyi dort parcaya ayiran degerlere kartiller denir.  
Q1 = (1/4(n+1)).terim  
Q3 = (3/4(n1+)).terim  
Q2 = (Q3 Q1)*2  
- orn;  
  - 8, 10, 15, 12, 17, 20, 14  
	8, 10, 12, 14, 15, 17, 20  
	Q1 -> (1/4(7+1)).terim = (1/4*8).terim = 2.terim = 10  
    Q3 -> (3/4(n1+)).terim = (3/4*8).terim = 6.terim = 17  	
    Q2 -> (17-10)*2 = 7*2 = 14  

#### **Merkezi Egilimin Onemini Kavrama**

1. Temsil Yonunu Kavramak  
2. Dogru Kullanilmasi  
* Ortalama ve Medyan degerlerinin birbirine yakin olmasi, bu dagilimin duzgun, homojen oldugunu gosterir.  

### **Dagilim Olculeri**

Elimizdeki degiskenin degerlerinin ne sekilde dagildigini ifade eden olculerdir.  
Maksimum, minumum ve ya ortalam etrafindaki durumunun ne oldugu anlamaya calismak amaciyla kullanilan olculerdir.  
   
#### **Range - Degisik Araligi**

Bir serideki maksimum degerden, minumum degeri cikardigimizda elde ettigimiz degerdir.  
Degisim Araligi = Max - Min  
- orn;  
  - 8, 10, 15, 12, 17, 20, 14  
    Degisim Araligi = 20 - 8 = 12  
	
#### **Standard Deviation - Standart Sapma**

Ortalamadan olan sapmalarin genel bir olcusudur.  
s = sqrt(1/n sum(n, i=1, (xi-mean(x))^2)  
- orn;  
  12, 15, 20, 30, 45, 22  
  Ortalama = ( 12 + 15 + 20 + 30 + 45 + 22 ) / 6 = 24  
  |-------------+----------------+------------------|
  | Kazanc (xi) | (xi - mean(x)) | (xi - mean(x))^2 |
  |-------------+----------------+------------------|
  |          12 | (12-24) = -12  |              144 |
  |          15 | (15-24) = -9   |               81 |
  |          20 | (20-24) = -4   |               16 |
  |          30 | (30-24) = 6    |               36 |
  |          45 | (45-24) = 21   |              441 |
  |          22 | (22-24) = -2   |                4 |
  |-------------+----------------+------------------|
  |      Toplam | 0              |              722 |
  |-------------+----------------+------------------|
  s = sqrt(1/6 * 722) = 10,97  

#### **Variance - Varyans**

Standart sapmanin karesidir. (Ortalamadan olan sapmalarin karelerinin toplamidir.  
s   = sqrt(1/n sum(n, i=1, (xi-mean(x))^2)  
s^2 = 1/n sum(n, i=1, (xi - mean(x))^2)  
- orn;  
  12, 15, 20, 30, 45, 22  
  Ortalama = (12 + 15 + 20 + 30 + 45 + 22) / 6 = 24  
  |-------------+----------------+------------------|
  | Kazanc (xi) | (xi - mean(x)) | (xi - mean(x))^2 |
  |-------------+----------------+------------------|
  |          12 | (12-24) = -12  |              144 |
  |          15 | (15-24) = -9   |               81 |
  |          20 | (20-24) = -4   |               16 |
  |          30 | (30-24) = 6    |               36 |
  |          45 | (45-24) = 21   |              441 |
  |          22 | (22-24) = -2   |                4 |
  |-------------+----------------+------------------|
  |      Toplam | 0              |              722 |
  |-------------+----------------+------------------|
  s^2 = 1/6 * 722 = 120,34  
  
#### **Skewness - Carpiklik**

Carpiklik bir degiskenin dagiliminin simetrik olamayisidir.  
(negatif carpik, pozitif carpik)  
Carpiklik oldugu durumlarda, merkezi egilim olcusu olarak, medyan kullanilmasi dogrudur.  
Pearson Carpiklik Katsayisi (PCK) = ( 3 * ( mean(x) - medyan ) ) / standart sapma  
PCK < 0 -> Negatif Carpik (soldan)  
PCK > 0 -> Pozitif Carpik (sagdan)  
PCK = 0 -> Simetrik  
- orn;  
  12, 15, 20, 30, 45, 22  
  Ortalama = (12 + 15 + 20 + 30 + 45 + 22) / 6 = 24  
  Medyan   => 12, 15, 20, 22, 30, 45 => (20+22)/ = 21  
  s = 10,97  
  |-------------+----------------+------------------|
  | Kazanc (xi) | (xi - mean(x)) | (xi - mean(x))^2 |
  |-------------+----------------+------------------|
  |          12 | (12-24) = -12  |              144 |
  |          15 | (15-24) = -9   |               81 |
  |          20 | (20-24) = -4   |               16 |
  |          30 | (30-24) = 6    |               36 |
  |          45 | (45-24) = 21   |              441 |
  |          22 | (22-24) = -2   |                4 |
  |-------------+----------------+------------------|
  |      Toplam | 0              |              722 |
  |-------------+----------------+------------------|
  PCK = ( 3 * ( mean(x) - medyan ) ) / standart sapma  
      = ( 3 * ( 24 - 21 ) ) / 10,97  
      = ( 3 * 3 ) / 10,97  
      = 9 / 10,97  
      = 0,82 -> simetrik degildir, pozitif carpiktir (deger 1'e yakin oldugu icin yuksek saga carpiktir)  
	  
#### **Kurtosis - Basiklik**

    Dagilimin basikligini/sivriligini gosterir.
    Basiklik Katsayisi (BK) = m4 / s^4
    ( m4 -> ortalamaya gore 4. moment -> sum(n, i=1, (xi - mean(x))^4 ) / n )
    BK = 3 ise dagilim standart normal dagilima uygundur
    BK > 3 ise dagilim sivridir
    BK < 3 ise dagilim basiktir
    - orn;
      12, 15, 20, 30, 45, 22
      Ortalama = (12 + 15 + 20 + 30 + 45 + 22) / 6 = 24
      Medyan   => 12, 15, 20, 22, 30, 45 => (20+22)/ = 21
      s = 10,97
      |-------------+----------------+------------------|
      | Kazanc (xi) | (xi - mean(x)) | (xi - mean(x))^4 |
      |-------------+----------------+------------------|
      |          12 | (12-24) = -12  |            20736 |
      |          15 | (15-24) = -9   |             6561 |
      |          20 | (20-24) = -4   |              256 |
      |          30 | (30-24) = 6    |             1296 |
      |          45 | (45-24) = 21   |           194482 |
      |          22 | (22-24) = -2   |               16 |
      |-------------+----------------+------------------|
      |      Toplam | 0              |           223346 |
      |-------------+----------------+------------------|
      m4  = 223346 / 6 = 37224,33
      s^4 = (10,97)^4  = 14481,93
      BK  = m4 / s^4   = 37224,33 / 14481,93 = 2,57 
          2,57 < 3 -> Dagilim basiktir.
** Istatistiksel Dusunce Modelleri - Statistical Thinking Models
   Veri okuryazarligindan veri analitigine giden yolu modelleyen yol gostericilerdir.
   Genel amaci: Bir bireyin, veriye ilk dokundugu andan, son asamasi olan veri ile ilgili yorumlar yapabilme, cikarimlarda bulunabilme sureclerini modelleyen teorik calismalardir.
   - Ben-Zvi ve Friedlander (1997)
     Jones ve digerleri (2000)
   - Wild ve Pfannkuch (1999)
     Hoerl ve Snee (2001)
   - Mooney (2002)
     - Verinin Tanimlanmasi
       Temel Kavramlar, Merkezi Egilim Olculeri, Dagilim Olculeri vs.
     - Verinin Organize Edilmesi ve Indirgenmesi
       Veriyi belirli islemlerden gecirme vs.
     - Veri Gosterimi
       Veriyi gorsellestirme, Istatistiksel Grafik Yorumlama vb.
     - Verinin Analiz Edilmesi ve Yorumlanmasi
     - Seviyeler:
       - Kisiye Ozguluk (1. Seviye)
	 Veri Okuryazaliginin olmadigi, yorumlamanin yapilamadigi seviye
       - Gecici (2. Seviye)
	 Nicel dusunmenin oneminin farkedilmeye baslandigi seviye, merkezi egilim olculeri yorumlanmaya baslaniyor, hatalar yapilabiliyor.
	 Veri analizi icin, veri temsiline donuk baglantilarin cok fazla kurulamadi seviye.
       - Nicel (3. Seviye)
	 Merkezi Egilim olculeri ve Dagilim olculeri dogru bir sekilde anlasilmaya baslaniyor. Istatistiksel kararlar alabilmek icin bu nicel veriler kullanilmaya baslaniyor. Baglar ve verinin ikisininde bilincinde olunmasi ve bu kavramlar arasinda ufak ufak iliskiler kurulmaya baslandigi seviye.
       - Analitik (4. Seviye)
	 Veriyi inceleme, yorumlama ve analiz etmede tam olarak analitik yaklasimlar kullanilmaya baslaniyor. Ortalama nedir, medyan nedir, farklari nedir, standart sapma nedir, varyans nedir, gercek hayatta neler ile ortustugu, nelere karsilik geldigi bilinebilir bir hale geliyor. Veri ve baglam arasinda iliski kurulabiliyor ve bu iliskiye dayir kanitlar gosterilebiliyor.
     

## **PYTHON**  

## **NUMPY**  

## **PANDAS**  

## **DATA VISUALIZATION**  

## **STATISTICS FOR DATA SCIENCE**  

- Ornek Teorisi  
- Betimsel Istatistikler  
- Guven Araliklari  
- Olasilik Dagilimlari  
- Hipotez Testleri  
- Varyans Analizi  
- Korelasyon Analizi  

### **Ornek Teorisi**  

"Without a grounding in statistics, a Data Scientist is a Data Lab Assistant." - Martyn Jones  

Istatistik veri biliminin "bilim" makine ogrenmesinin "ogrenme" kismidir.  

Eldeki ornek olaylardan, genelleme yapmaya calismaktir.  

"Better, not more." - Greg Nixon, PhD  

"The future of AI will be about less data, not more." - H.James Wilson  

#### **Orneklem Nedir?**  
Bir ana kitle icerisinden, bir populasyonun icerisinden, bu populasyonu temsil ettigi dusunulen bir alt kume secme islemidir.  
Population -> Sample  
Olasiliksal ve Olasiliksal Olmayan  

#### **Orneklem Dagilimi**  
Bir populasyon icinden birden fazla orneklem cektigimizde ve bu orneklemlerin dagilimi ile ilgilendigimizde, orneklem dagilimi konusu ile ilgileniyor oluyoruz.  
Population -> Sample 1 / Sample 2 / Sample 3 / ...  

#### **Merkezi Limit Teoremi**  
Bagimsiz ve ayni dagilima sahip rassal degiskenlerin toplami ya da aritmetik ortalamasi yaklasik olarak normal dagilmaktadir.  

#### **Ornek Teorisi - Kod**  

```python
import numpy as np
populasyon = np.random.randint(0, 80, 10000)
populasyon[0:10]
# Orneklem Cekmek
np.random.seed(115)
orneklem = np.random.choice(a = populasyon, size = 100)
orneklem[0:10]
orneklem.mean()
populasyon.mean()
# Orneklem Dagilimi
np.random.seed(10)
orneklem1 = np.random.choice(a = populasyon, size = 100)
orneklem2 = np.random.choice(a = populasyon, size = 100)
orneklem3 = np.random.choice(a = populasyon, size = 100)
orneklem4 = np.random.choice(a = populasyon, size = 100)
orneklem5 = np.random.choice(a = populasyon, size = 100)
orneklem6 = np.random.choice(a = populasyon, size = 100)
orneklem7 = np.random.choice(a = populasyon, size = 100)
orneklem8 = np.random.choice(a = populasyon, size = 100)
orneklem9 = np.random.choice(a = populasyon, size = 100)
orneklem10 = np.random.choice(a = populasyon, size = 100)
( orneklem1.mean() + orneklem2.mean() + orneklem3.mean() + orneklem4.mean() + orneklem5.mean() + 
  orneklem6.mean() + orneklem7.mean() + orneklem8.mean() + orneklem9.mean() + orneklem10.mean() ) / 10
```

### **Betimsel Istatiktikler**  

- Ortalama  
- Medyan  
- Mod  
- Kartiller  
- Degisim Araligi  
- Standart Sapma  
- Kovaryans  
- Korelasyon  

#### **Kovaryans**  

Iki degisken arasindaki iliskinin degiskenlik olcusudur.  

$cov(X,Y) = \sum[(X-\sum[X])(Y-\sum[Y])]$  

#### **Korelasyon**  

Iki degisken arasindaki iliskiyi, iliskinin anlamli olup olmadigini, iliskinin siddetini ve yonunu ifade eden istatistiksel bir tekniktir.  

$r_{xy} = \frac{\sum x_iy_i - n\bar{x}\bar{y}}{\sqrt{(\sum x_i^2 - n\bar{y}^2)}\sqrt{(\sum y_i^2 - n\bar{y}^2)}}$  

#### **Betimsel Istatistikler - Kod**  

```python
import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()
df.head()
df.describe().T

!pip install researchpy
import researchpy as rp
rp.summary_cont(df[["total_bill", "tip", "size"]])
rp.summary_cat(df[["sex", "smoker", "day"]])

# Kovaryans
df[["tip", "total_bill"]].cov()

# Korelasyon
df[["tip", "total_bill"]].corr()
```

### **Guven Araliklari**  

#### **Guven Araligi**  

Anakutle parametresinin tahmini degerini kapsayabilecek iki sayidan olusan bir aralik bulunmasidir.  
Ornek istatistiginin iki sayi tarafindan bir aralikca ifade edilmesi olarak ta dusunebiliriz.  
Olcumun hassasiyetinin bir gostergesidir.  
Ayrica, yaptigimiz tahminlerin ne kadar guvenilir oldugu ile ilgili bir deger sunar.  

&nbsp;&nbsp;**Ornek:** Web sitesinde gecirilen surenin guven araligi nedir?  
&nbsp;&nbsp;Ortalama: 180 saniye  
&nbsp;&nbsp;Standart Sapma: 40 saniye  
&nbsp;&nbsp;Guven Araligi: 172 ile 188 saniye arasi  

#### **Guven Araligi Nasil Hesaplanir?**  

**Adim 1:** n, ortalama ve standart sapmayi bul  
n = 100  
ortalama = 180  
standart sapma = 40  

**Adim 2:** Guven araligina karar ver: 95 mi 99 mu?  
Standart olarak %95 kabul edilir.  
Z Tablo degerini hespala (1,96 - 2,57)  

**Adim 3:** Yukaridaki degerleri kullanarak guven araligini hesapla:  

$\bar x \underline{+} z \frac{s}{\sqrt n} = 180 \underline{+} 1,96 \times \frac{40}{\sqrt 100}$  

**Sonuc:** 180 $\underline{+}$ 7,84 yani 172 ile 188 arasidir.  

Guven araligi hesaplamak demek, hesapladigimiz bir ortalamanin etrafina bir sinir koymak demektir. Asagi yonlu ve yukari yonlu bir sinir.  

#### **Is Uygulamasi - Fiyat Stratejisi Karar Destek Sistemi**  

- **Problem:**  
  CEO fiyat belirleme konusunda bilimsel bir dayanak ve esneklis istiyor.  
- **Detaylar:**  
  - Satici, alici ve bir urun var.  
  - Alicilara urune ne kadar ucret oderdiniz diye soruluyor.  
  - Optimum fiyat bilimsel ve esnek olarak bulunmak isteniyor.  

#### **Guven Araligi - Kod**  

```python
import numpy as np

fiyatlar = np.random.randint(10, 110, 1000)
fiyatlar.mean()

import statsmodels.stats.api as sms

sms.DescrStatsW(fiyatlar).tconfint_mean()
```

### **Olasiliga Giris ve Olasilik Dagilimlari**  

"Olaylarin olabilirliginin sayisal ifadesidir." - Ozlem Ozkilic  

#### **Rassal Degisken:** 

Degerlerini bir deneyin sonuclarindan alan degiskene rassal degisken denir.  

#### **Dagilim Nedir?**  

Gerceklesen olaylar ya da durumlarin sayisal karsiliklarinin ortaya cikardigi yapiya dagilim denir.  

#### **Olasilik Dagilimi Nedir?**  

Bir rassal olaya ait degerler ve bu degerlerin gerceklesme olasiliklarinin bir arada ifade edilmesine olasilik dagilimi denir.  

#### **Olasilik Fonksiyonu Nedir?**

Bir degiskenin herhangi bir degeri almasi olasiligini hesaplayan fonksiyona denir.  

#### **Kesikli ve Surekli Olasilik Dagilimlari**  

- **Kesikli Olasilik Dagilimlari**
  - Bernoulli
  - Binom
  - Poisson

- **Surekli Olasilik Dagilimlari**
  - Normal Dagilim
  - Uniform Dagilim
  - Usten Dagilim

#### **Bernoulli Dagilimi**  

Basarili-basarisiz, olumlu-olumsuz seklindeki iki sonuclu olaylar ile ilgilenildiginde kullanilan kesikli olasilik dagilimidir.  

$f(x;p) = p^x(1-p)^{1-x}, \quad x\in{0,1}$  
$E(X) = p$  
$Var(X) = pq = p(1-p)$  

##### **Bernoulli Dagilimi - Uygulama**  

```python
from scipy.stats import bernoulli

p = 0.6
rv = bernoulli(p)

rv.pmf(k=1)
rv.pmf(k=0)
```

#### ** Buyuk Sayilar Yasasi**  

Bir rassal degiskenin uzun vadeli kararliligini tanimlayan olasilik teoremidir.  

```python
import numpy as np

rng = np.random.RandomState(123)

for i in np.arange(1,21):

    deney_sayisi = 2**i
    yazi_turalar = rng.randint(0, 2, size = deney_sayisi)
    yazi_olasiliklari = np.mean(yazi_turalar)
    
    print("Atis Sayisi:", deney_sayisi, "----", "Yazi Olasiligi: %.2f" %(yazi_olasiliklari * 100))
```

#### **Binom Dagilimi**  

Binom Dagilimi, bagimsiz n deneme sonucu k basarili olma olasiligi ile ilgilenildiginde kullanilan dagilimdir.  


$f(x;n,p) = \binom{n}{x} \> p^x \> (1-p)^{n-x}, \quad x=0,1,2,...,n$  
$\quad E(X)=np \quad\quad Var(X)=np(1-p)$  

**Ornek:**
Bir madeni para 4 kere atiliyor. 2 kere yazi gelmesi olasiligi nedir?  

$f(x;n,p) = \binom{n}{x} \> p^x \> (1-p)^{n-x}, \quad x=0,1,2,...,n$  

$f(2;4,0.50) = \binom{4}{2} \> 0.50^2 \> (1-0.50)^{4-2}, \quad x = 0.375$

##### **Is Uygulamasi: Reklam Harcamasi Optimizasyonu**  

- **Problem:**  
  Cesitli mecralarda reklam veriliyor, reklamlarin tiklanma ve geri donusum oranlari optimize edilmeye calisiliyor. Buna yonelik olarak belirli bir mecrada cesitli senaryolara gore reklama tiklanma olasiliklari hesaplanmak isteniliyor.

- **Detaylar:**  
  - Bir mecrada reklam verilecek  
  - Dagilim ve reklama tiklama olasiligi biliniyor (0.01)  
  - **Soru:** Reklami 100 kisi gordugunde 1, 5, 10 tiklanmasi olasiligi nedir?  

**Olasiliklarin Hesaplanmasi**  

$f(1; 100, 0.01) = \binom{100}{1} \> 0.01_2 (1-0.01)^{100-1} = 0.37$  
$f(5; 100, 0.01) = 0.00289779$  
$f(10; 100, 0.01) = 0.00000007$  

##### **Kod**  

```python
from scipy.stats import binom

p = 0.01
n = 100
rv = binom(n, p)

print(rv.pmf(1))
print(rv.pmf(5))
print(rv.pmf(10))
```




#### **Poisson Dagilimi**  

Belirli bir zaman araliginda, belirli bir alanda, nadiren rastlanan olaylarin olasiliklarini hesaplamak icin kullanilir.  

$f(x, \lambda) = \frac{\lambda^x e^{-\lambda}}{x!}, \quad x = 0,1,2,...,n$  
$\Epsilon(\Chi) = \lambda \quad Var(\Chi) = \lambda$  

**Ornekler:**  
- 10000 kelimeden olusan bir kitapta hatali kelime sayisi  
- 4000 ogrencili okulda not girisinde hata yapilmasi  
- Bir is gununde cagri merkezine gelen taktir sayisi  
- Kredi karti islemlerinde sahtekarlik olmasi  
- Rotara dusen ucak sayisi  

**n:** buyuk  
**p:** kucuk  

Binom dagiliminin ozel bir turudur.  

Nadir bir olay olmasi gerekmektedir.  
n > 50  
n * p < 5  

- Rassal denemeler iki sonuclu olmali.  
- Ayni kosullar altinda gerceklestirilmelidir.  
- Rassal denemeler birbirinden bagimsiz olmalidir.  

**Ornek:**  
Bir universitede 5000 not girisinde 5 tane notun yanlis girilmesi olasiligi nedir?  
Dagilimin Poisson oldugu biliniyor ve Lambda = 0.2  

$f(5, 0.2) = \frac{0.2^5 e^{-0.2}}{5!} = 0.00000218328201$  

##### **Is Uygulamasi: Ilan Girisi Hata Olasiliklarinin Hesaplanmasi**  

**Problem:**  
Hatali ilan girisi olasiliklari hesaplanmak isteniyor.  

**Detaylar:**  
- Bir yil suresince olcumler yapiliyor.  
- Dagilim biliniyor(Poisson) ve Lambda 0.1 (ortalama hata sayisi)  
- Hic hata olmamasi, 3 hata olmasi ve 5 hata olmasi olasiliklari nelerdir?  

$f(0, 0.1) = \frac{0.1^0 e^{-0.1}}{0!} = 0.9048374180$  

$f(3, 0.1) = \frac{0.1^3 e^{-0.1}}{3!} = 0.0001508062$  

$f(5, 0.1) = \frac{0.1^5 e^{-0.1}}{5!} = 0.0000000754$  

```python
from scipy.stats import poisson

lambda_ = 0.1
rv = poisson(mu = lambda_)

print(rv.pmf(k = 0))
print(rv.pmf(k = 3))
print(rv.pmf(k = 5))
```

#### **Normal Dagilim**  

Normal dagildigi bilinen surekli rassal degiskenler icin olasilik hespalanmasi icin kullanilir.

$f(x\>|\>\mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$  

- $\mu$ ortalama ya da dagilimin beklenen degeri  
- $\sigma$ standart sapma  
- $\sigma^2$ varyans

##### **Is Uygulamasi: Urun Satis Olasiliklarinin Hesaplanmasi**  

**Problem:**  
Bir yatirim/toplanti oncesinde gelecek ay ile ilgili satislarin belirli degerlerde gerceklesmesi olasiliklari belirlenmek isteniyor.  

**Detaylar:**  
- Dagilimin normal oldugu biliniyor.  
- Aylik ortalama satis sayisi 80K, standart sapmasi 5K  
- 90K dan fazla satis yapma olasiligi nedir?  

**90K'dan fazla olma olasiligi nedir?**  
P(X > 90) = 0.0228  

**70K'dan fazla olma olasiligi nedir?**  
P(X > 70) = 0.9772  

**73K'dan az olma olasiligi nedir?**  
P(X < 73) = 0.0808  

**Satislarin 85K ile 90K arasinda olma olasiligi nedir?**  
P(85 < X < 90) = 0.1359  

**AKLIMIZDA KALMASI GEREKENLER**  
1. **Belirsizlik altinda karar vermeye calismak.** (Belirsizlik altinda karar vermeye calisan, veri bilimi ve yapay zeka ile ilgilenen kisileriz. Birseyleri modellemeye, veriye dokmeye calisiyoruz. Iste bu belirsizligi ortadan gidermek adina kullanilabilecek olan yaklasimlarindan bir tanesi olasilik dagilimlari, bunlar bize cesitli konularda olasilik degerleri veriyor.)  
2. **Uygun olasilik fonskiyonlari ile olasilik hesaplari yapiyoruz.**  

### **Hipotez Testi Nedir?**  

Bir inanisi (bir savi, bir tahmini vs) test etmek icin kullanilan istatistiksel bir tekniktir.  
Sansa yer vermeyecek sekilde, ilgilenmis oldugumuz konuda bir ispat saglar.  

**Hipotezler ve Turleri** 

Ikiye ayrilirlar:  

$H_0: \mu = 50     \quad H_0: \mu <= 50 \quad H_0: \mu >= 50$  
$H_1: \mu \neq 50  \quad H_1: \mu >= 50 \quad H_1: \mu <= 50 \quad$  

**Hata Tipleri**  

|        |              | Hipotez Testi Sonucu Verilen Karar       |                                        |
| ------ | ------------ | ---------------------------------------- | -------------------------------------- |
|        |              | $H_0$ reddedilmedi                       | $H_1$ reddedildi                       |
| Gercek | $H_0$ dogru  | Dogru Karar $(1-\alpha)$ -> Guven Duzeyi | I.Tip Hata $\alpha$                    |
|        | $H_0$ yanlis | II. Tip Hata $\beta$                     | Dogru Karar $(1-\beta)$ -> Testin Gucu |

**p-value**  

p < 0.05  

Hipotez testlerinin sonuclarini degerlendirmek uzere programlar terafindan p-value degeri verilir. Bu deger uzerinden koklayca yorum yapabiliriz.  

$\alpha = 0.05$  

Dagilim testlerinde $H_0$ reddedilmek istenilmez. Cunku $H_0$ "ornek dagilimi ile teorik dagilim arasinda fark yoktur" der.  

**Hipotez Testi Adimlari**  

**Adim 1:** Hipotezlerin kurulmasi ve yonlerinin belirlenmesi.  
$\quad H_0: \mu = 50$  
$\quad H_1: \mu \neq 50$  
**Adim 2:** Anlamlilik duzeyinin ve tablo degerinin belirlenmesi.  
**Adim 3:** Test istatistiginin belirlenmesi ve test istatistiginin hesaplanmasi.  
**Adim 4:** Hesaplanan test istatistigi ile alfa'ya karsilik gelen tablo degerinin karsilastirilmasi.  
&nbsp;&nbsp;&nbsp;&nbsp;
Test istatistigi (Zh) > Tablo Degeri(Zt) ise $H_0$ Red  
**Adim 5:** Yorum  

**Tek Orneklem T Testi**  

Populasyon ortalamasi ile varsayimsal bir deger arasinda istatistiksel olarak anlamli bir farklilik olup olmadigini test etmek icin kullanilan parametrik bir testtir.  

Ornek ortalamasina iliskin test yapmak icin kullanilir.  

Tek bir ornekle iliskin, tek bir orneklemin ortalamasina iliskin bir test yapmak ihtiyacimiz oldugunda kullandigimiz test yontemidir.  
Ornegin:  
- Bir ilcenin yas ortalamasina iliskin hipotez testi yapmak istedigimizde  
- Web sitemizde gecirilen zamana iliskin hipotez testi yapmak istedigimizde  

**Tek Orneklem T Testi: Hipotez**  

$H_0: \mu = 50     \quad H_0: \mu <= 50 \quad H_0: \mu >= 50$  
$H_1: \mu \neq 50  \quad H_1: \mu >= 50 \quad H_1: \mu <= 50 \quad$  

**Tek Orneklem T Testi: Test Istatistigi**  

$t = \frac{\overline{x}-\mu}{\frac{s}{\sqrt{n}}} \quad z = \frac{\overline{x}-\mu}{\frac{\sigma}{\sqrt{n}}}$  

1. Anakutle standart sapmasi biliniyorsa z istatistigi kullanilir.  
2. Anakutle standart sapmasi bilinmiyorsa ve n > 30 ise yine z istatistigi kullanilir.  
3. Anakutle standart sapmasi bilinmiyor ve n < 30 ise t istatistigi kullanilir.

n buyudukce t, z'ye yaklasir.  

**Tek Orneklem T Testi: Varsayim**  

Normal Dagilim  

**Is Uygulamasi: Urun Satin Alma Adim Optimizasyonu**  

- **Problem:**  
  Sepete urun ekleme islemi sonrasinda odeme ekraninda 5 adim vardir ve bu adimlarin birisi sorgulanmaktadir.  
- **Detaylar**  
  - Har adimin 20'ser saniye olmasi hedefi var. 4. adim sorgulaniyor.  
  - Bu durumu test etmek icin 100 ornek aliniyor.
  - Ornek standart sapmasi 5 saniyedir. Ornek ortalamasi ise 19 saniyedir.   

**Adim 1:** Hipotezlerin kurulmasi ve yonlerinin belirlenmesi.  
$\quad H_0: \mu = 20 \rightarrow$ kisilerin 4. adimda gecirmis olduklari sure 20 dir.  
$\quad H_1: \mu \neq 20 \rightarrow$ kisilerin 4. adimda gecirmis olduklari sure 20 degildir.  

**Adim 2:** Anlamlilik duzeyinin ve tablo degerinin belirlenmesi  
$\alpha = 0.05 \quad\quad \frac{\alpha}{2} = 0.025$  
$Z_{tablo}$ tablo olasilik degeri : 0.5 - 0.025 = 0.475  
$Z_{tablo}$ kritik degeri = -/+ 1.96  
Hipotezimiz iki yonlu oldugundan dolayi $\alpha$ degerini ikiye bolerek hareket ediyoruz.  

**Adim 3:** Test istatistiginin belirlenmesi ve  test istatistiginin hesaplanmasi  
$z = \frac{\overline{x}-\mu}{\frac{\sigma}{\sqrt{n}}}$  
$z_{hesap} = \frac{19-20}{5 / \sqrt{100}} = -2.00$  
n = 100,  
standart sapma = 5,  
ornek ortalamasi = 19sn  

**Adim 4:**  
$Z_{tablo}$ ve $Z_{hesap}$ degerlerinin karsilastirilmasi  
$Z_h > Z_t$ ya da $-Z_h < -Z_t$ ise $H_0$ Red  
$Z_h = -2.00 < Z_t = -1.96$ oldugu icin $H_0$ reddedilir.  

**Adim 5:** Yorum  
$H_0: \mu = 20$  
$H_1: \mu \neq 20$  

4 uncu adimda gecirilen surenin 20 saniye oldugunu iddaa eden $H_0$ hipotezi reddedilmistir. Buna gore kullanicilar istatistiksel olarak %95 guvenilirlik ile 4. adimda 20 saniyeden farkli zaman gecirmektedir.  

**Is Uygulamasi: Web Sitesinde Gecirilen Surenin Testi**  

**Problem:**  
Web Sitemizde gecirilen sure gercekten 170 saniye mi?  
**Detaylar:**  
- Yazilimlardan elde edilen web sitesinde gecirilen ort. sureler var.  
- Bu veriler incelendiginde bir yonetici ya da calisanimiz, bu degerlerin boyle olmadigina yonelik dusunceler tasiyor ve bu durumu test etmek istiyorlar.  

$\quad H_0: \mu = 170 \to$ sitemizde gecirilen sure 170 saniyedir.  
$\quad H_1: \mu \neq 170 \to$ sitemizde gecirilen sure 170 saniye degildir.  

```python
import numpy as np

olcumler = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119, 157, 145, 127, 244, 163, 114,
                     145, 65, 112, 185, 202, 146, 203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 
                     110, 216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])
olcumler[0:10]

import scipy.stats as stats

stats.describe(olcumler)

import pandas as pd

pd.DataFrame(olcumler).plot.hist();

import pylab
stats.probplot(olcumler, dist="norm", plot=pylab)
pylab.show()

from scipy.stats import shapiro

shapiro(olcumler)
print("T Hesap Istatistigi: " + str(shapiro(olcumler)[0]))
print("Hesaplanan p-value : " + str(shapiro(olcumler)[1]))

stats.ttest_1samp(olcumler, popmean = 170)
```

**Tek Orneklem Oran Testi**  

Oransal bir ifade test edilmek istenildiginde kullanilir.  

**Tek Orneklem Oran Testi: Hipotezler**  

$H_0: P = P_0     \quad H_0: P <= P_0 \quad H_0: P >= P_0$  
$H_1: P \neq P_0  \quad H_1: P >= P_0 \quad H_1: P <= P_0 \quad$  

**Tek Orneklem Oran Testi: Test Istatistigi**  

$z = \frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$  

$\hat{p} \>\> \to$ ornek uzerinden elde ettigimiz deger  
$p_0 \to$ sinamak uzere odaklandigimiz deger  

**Tek Orneklem Oran Testi: Varsayim**  

n > 30  

Ilgilendigimiz kitlede toplamis oldugumuz orneklem 30 dan buyukse, bu testi gerceklestirebiliyoruz.  

**Is Uygulamasi: Donusum Oran Testi**  

**Problem:**  
Bir yazilim ile bir mecrada reklam verilmis ve bu reklama iliskin yazilim tarafindan 0.125 donusum orani elde edildigi ifade edilmis. Fakat bu durum kontrol edilmek isteniyor. Cunku bu yuksek bir oran ve gelirler incelendiginde ortusmuyor.  
**Detaylar:**  
- 500 kisi dis mecrada reklamlara tiklamis, 40 tanesi sitemize gelip alisveris yapmis.  
- Ornek uzerinden elde edilen donusum orani: 40/500 = 0.08  

$H_0: P = 0.125$  
$H_1: P \neq 0.125$  

**Bagimsiz Iki Orneklem T Testi (AB Testi)**  

Iki grup ortalamasi arasinda karsilastirma yapilmak istenildiginde kullanilir.  

**Bagimsiz Iki Orneklem T Testi (AB Testi): Hipotezler**

$H_0: \mu_1 = \mu_2     \quad H_0: \mu_1 <= \mu_2 \quad H_0: \mu_1 >= \mu_2$  
$H_1: \mu_1 \neq \mu_2  \quad H_1: \mu_1 >= \mu_2 \quad H_1: \mu_1 <= \mu_2 \quad$   

**Bagimsiz Iki Orneklem T Testi (AB Testi): Test Istatistigi**  

Ornek sayilari ayni, varyanslar homojen ise:  
$\quad t = \frac{\overline{x_1}-\overline{x_2}}{S_p\sqrt{\frac{2}{n}}},$
$\quad S_p = \sqrt{\frac{s^2_{x_1}+S^2_{x_2}}{2}}$  

Ornek sayilari farkli, varyanslari homojen ise:  
$\quad  = \frac{\overline{x_1}-\overline{x_2}}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}},$
$\quad S_p = \sqrt{\frac{(n_1-1)s^2_{x_1}+(n_2-1)s^2_{x_2}}{n_1+n_2-2}}$  

Ornek sayilari farkli, varyanslar homojen ise:  
$\quad t = \frac{\overline{x}_1-\overline{x})2}{S_{\overline{\triangle}}},$
$\quad S_{\overline{\triangle}} = \sqrt{\frac{{s_1}^2}{n_1}+\frac{{s_2}^2}{n_2}}$  

Not: Son iki durumda, ornek sayilari esit olsa bile, hesaplamalar yapilabilir.  
Not: Ucuncu yontem ayni zamanda Welch Testi diye de gecer.  

**Bagimsiz Iki Orneklem T Testi (AB Testi): Varsayimlar**  

- Normallik  
- Varyans Homojenligi  

Iki ornegin her birisi icin normallik testi yapmamiz gerekiyor (histogram, qqplot, shapiro-wilks)  
Varyans homojenliginde de, gruplarin varyanslarinin birbirine benzer olup olmadigini kontrol edecegiz.  

**Is Uygulamasi: ML Modelinin Basari Testi**  

- **Problem:**  
Bir ML projesine yatirim yapilmis. Urettigi tahminler neticesinde olusan gelir ile eski sistemin urettigi gelirler karsilastirilip anlamli farklilik olup olmadigi test edilmek isteniyor.  
- **Detaylar:**
  - Model gelistirilmis ve web sitesine entegre edilmis.
  - Site kullanicilari belirli bir kurala gore ikiye bolunmus olsun.
  - A grubu eski, B grubu yeni sistem.
  - Gelir anlaminda anlamli bir is yapilip yapilmadigi test edilmek isteniyor.

**ML modeli anlamli farklilik olusturdu mu?**

$H_0: \mu_1 = \mu_2$  
$H_1: \mu_1 \neq \mu_2$ 


## **MACHINE LEARNING**

**Makine Ogrenmesi Nedir?**  
Bilgisayarlarin insanlara benzer sekilde ogrenmesini saglamak maksadi ile cesitli algoritma ve tekniklerin gelistirilmesi icin calisilan bilimsel calisma alanidir.

### **Terminoloji**

- Bagimli Degisken
- Bagimsiz Degisken
- Ogrenme Turleri
  - Gozetimli Ogrenme
  - Gozetimsiz Ogrenme
  - Yari Gozetimli Ogrenme
- Problem Turu:
  - Regresyon
  - Siniflandirma
- Degisken Turleri:
  - Sayisal Degiskenler (nicel, kantitatif) (Surekli Degiskenler)
  - Kategorik Degiskenler (nitel, kalitatif)
- Olcek Turleri:
  - Sayisal Degiskenler Icin:
	- Aralik
	- Oran
  - Kategorik Degiskenler Icin:
	- Nominal
	- Ordinal
- Test-Train Ayrimi
  - Orijinal Veri Seti
  - Egitim Seti
  - Test Seti
- Degisken Muhendisligi (Feature Engineering)
- Degisken Secimi (Variable Selection)
- Model Secimi:
  1. Olusabilecek degisken kombinasyonlari ile olusturulan modeller arasindan en iyi modelin secilmesi
  2. Kurulan birbirinden farkli modeller arasindan model secimi
- Model Neye Gore Secilir:
  - Regresyon icin aciklanabilirlik orani ve RMSE bezeri bir deger.
  - Siniflandirma icin dogru siniflandirma orani benzeri bir deger.
- Asiri Ogrenme (Overfitting)
- Deterministik Modeller vs Stokastik Modeller
  - Deterministik: Degiskenler arasinda kesin bir ilgi oldugunu varsayan modellere deterministik model denir.
  - Stokastik: Hedefimizin rassal olarak degistigi modellerdir.
- Dogrusal Modeller ve Dogrusal Olmayan Modeller



### **Model Dogrulama Yontemleri**

Modellerin urettigi sonuclarin dogru degerlendirilmesi calismalari.

Bu yontemlerin kullanilma gerekceleri, model basari sonuclarinin daha dogru degerlendirilmesi cabasidir.

#### **Holdout Yontemi**

# TODO BURADAN ITIBAREN NOT ALAMADIM. NOTLARI TAMAMLA... (VIDEO 211 - Nonparametrik Bagimsiz Iki Orneklem Testi)
