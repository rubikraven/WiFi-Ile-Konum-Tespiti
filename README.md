Wi-Fi ile Konum Tespiti
Bu proje, Wi-Fi sinyal gücü (RSSI) kullanarak yakındaki cihazların konumunu tahmin etmek için Python ile geliştirilmiştir. Konum belirleme, trilaterasyon yöntemiyle gerçekleştirilmektedir.

Projenin Amacı
Yakındaki Wi-Fi cihazlarından alınan sinyal gücü (RSSI) değerleri ile bu cihazların muhtemel konumunu belirlemeyi amaçlamaktadır. Bu belirleme, trilaterasyon yöntemi kullanılarak yapılır.

Kullanılan Teknolojiler ve Kütüphaneler
Python
Scapy: Wi-Fi paketlerini yakalamak için
SciPy: Trilaterasyon hesaplamaları için optimize edilmiş matematiksel fonksiyonları içerir
Nasıl Kullanılır?
Kali Linux'ta ve Monitor Modunda Kullanım
Kali Linux üzerinde terminali açın.

Kablosuz kartınızı monitor moda alın:

sudo ifconfig [interface] down
sudo iwconfig [interface] mode monitor
sudo ifconfig [interface] up
Burada [interface] yerine kablosuz ağ adaptörünüzün adını yazmalısınız, genellikle wlan0 veya wlan1 şeklindedir.

Proje dosyasını bilgisayarınıza indirin.

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

pip install scapy scipy
your_wifi_ssid değişkenini kendi BSSID'nizle değiştirin. apartment_x ve apartment_y değişkenlerini kullanarak kendi konum bilginizi girin. iface = "wlan1" değişkenini kendi sistemlerinizdeki kablosuz ağ adaptörü adıyla değiştirin. Örneğin, bazı sistemlerde wlan0 olabilir.

Kodu çalıştırın:

sudo python dosya_adı.py
(dosya_adı.py yerine kullandığınız dosya adını yazın)

Trilaterasyonla Konum Tespiti
Bu proje, Wi-Fi sinyal gücü kullanarak yakındaki cihazların konumunu tahmin eder. Trilaterasyon yöntemiyle sinyal güçleri analiz edilerek cihazların muhtemel konumları belirlenir.
 
Trilaterasyonla Konum Tespiti https://dergipark.org.tr/en/download/article-file/1133653
İlgili Instagram Gönderisi https://www.instagram.com/p/C6MvXi9IpeU/?hl=tr
Lisans
Bu proje MIT lisansı altında yayınlanmıştır. Daha fazla detay için LICENSE dosyasına göz atabilirsiniz.
