MertSploit-Lab.py
Author: Mert

Bu proje, Metasploit Framework’ün temel çalışma mantığını anlamak amacıyla
oluşturulmuş bir eğitim ve simülasyon çalışmasıdır. Gerçek payload üretimi,
exploit çalıştırma veya herhangi bir sisteme doğrudan müdahale içermez.

Projenin amacı, Metasploit’in nasıl çalıştığını kavramsal düzeyde öğretmek
ve siber güvenlik alanında çalışan veya bu alana yönelmek isteyen kişiler
için güvenli bir öğrenme ortamı sunmaktır.

Amaç
-----
MertSploit-Lab.py projesi, özellikle Red Team ve Blue Team bakış açılarını
destekleyecek şekilde Metasploit workflow’unu anlamaya odaklanır.

Bu çalışma sayesinde kullanıcılar:
- Payload kavramını ve türlerini
- LHOST ve LPORT parametrelerinin ne anlama geldiğini
- multi/handler kullanım mantığını
- Metasploit komutlarının hangi sırayla çalıştırıldığını

teorik ve simülatif olarak öğrenebilir.

Bu proje bir saldırı aracı değildir.

Nasıl Çalışır
-------------
Uygulama, komut satırı üzerinden çalışan basit bir menü yapısına sahiptir.
Kullanıcıdan bazı seçimler alır ve bu seçimlere göre Metasploit Framework
kullanılırken izlenen adımları ekrana yansıtır.

Önemli noktalar:
- Gerçek msfvenom komutu çalıştırılmaz
- Gerçek payload dosyası üretilmez
- Gerçek exploit veya bağlantı kurulmaz
- Sistem üzerinde herhangi bir değişiklik yapılmaz

Uygulama yalnızca süreci ve mantığı gösterir.

Kurulum
-------
Bu proje Python 3 ile çalışmaktadır.

Sistemde Python 3 kurulu değilse öncelikle Python 3 kurulmalıdır.

Projeyi çalıştırmak için:
1. Proje klasörüne girin
2. Aşağıdaki komutu çalıştırın

python3 MertSploit-Lab.py

Kullanım
--------
Uygulama çalıştırıldığında bir ana menü görüntülenir.

Ana menü üzerinden:
- İşletim sistemi seçimi (Windows, Linux, Android)
- Payload türü seçiminin simülasyonu
- Handler yapılandırma adımlarının gösterimi

yapılabilir.

Örneğin bir payload seçildiğinde:
- Payload adı
- Normalde hangi Metasploit modülünün kullanılacağı
- Hangi parametrelerin ayarlanması gerektiği

ekrana yazdırılır.

Handler simülasyonu bölümünde ise:
- use exploit/multi/handler
- set PAYLOAD
- set LHOST
- set LPORT
- exploit

komutlarının hangi mantıkla ve hangi sırayla kullanıldığı gösterilir.


