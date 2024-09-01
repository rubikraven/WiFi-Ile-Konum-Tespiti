# Wi-Fi İle Konum Tespiti

Bu proje, Python kullanarak Wi-Fi sinyal gücü (RSSI) ile yakındaki cihazların konumunu tahmin etmek amacıyla geliştirilmiştir. Trilaterasyon yöntemi kullanılarak, cihazların olası konumları hesaplanmaktadır.

## Projenin Amacı

Yakındaki Wi-Fi cihazlarından alınan sinyal gücü (RSSI) değerleri ile bu cihazların muhtemel konumlarını belirlemek.

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python**
- **Scapy**: Wi-Fi paketlerini yakalamak için kullanılır.
- **SciPy**: Trilaterasyon hesaplamaları için optimize edilmiş matematiksel fonksiyonlar içerir.

## Nasıl Kullanılır?

### Kali Linux'ta ve Monitor Modunda Kullanım

1. Terminali açın ve kablosuz ağ adaptörünüzü monitor moda alın:

   ```bash
   sudo ifconfig [interface] down
   sudo iwconfig [interface] mode monitor
   sudo ifconfig [interface] up
   ```

   `[interface]` yerine kablosuz ağ adaptörünüzün adını yazmalısınız (örneğin, `wlan0` veya `wlan1`).

2. Proje dosyasını bilgisayarınıza indirin.

3. Gerekli Python kütüphanelerini yükleyin:

   ```bash
   pip install scapy scipy
   ```

4. Kod içerisinde şu değişiklikleri yapın:
   - `your_wifi_ssid` değişkenini kendi BSSID'niz ile değiştirin.
   - `apartment_x` ve `apartment_y` değişkenlerine kendi konum bilgilerinizi girin.
   - `iface` değişkenini kendi kablosuz ağ adaptörünüzün adıyla güncelleyin (`wlan0`, `wlan1` gibi).

5. Kodu çalıştırın:

   ```bash
   sudo python dosya_adı.py
   ```

   (Burada `dosya_adı.py` yerine kullandığınız Python dosyasının adını yazın.)

## Trilaterasyonla Konum Tespiti

Daha fazla bilgi için [bu makaleye](https://dergipark.org.tr/en/download/article-file/1133653) göz atabilirsiniz.

## İlgili Instagram Gönderisi

Projenin tanıtımı için Instagram gönderisi: [Buradan görüntüleyin](https://www.instagram.com/p/C6MvXi9IpeU/?hl=tr)

## Lisans

Bu proje MIT lisansı altında yayınlanmıştır. Daha fazla detay için `LICENSE` dosyasına göz atabilirsiniz.
