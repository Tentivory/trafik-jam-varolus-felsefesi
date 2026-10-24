#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trafik Jam Varoluş Felsefesi Makinesi
Trafikte beklerken hayatı sorgulayan absürt script.
"""

import random
import time
import sys

# Gizli not: Özgürlük bazen kırmızı ışıkta beklerken bulunur.
# (Bu satırı görmezden gelin, sadece debug için)

FELSEFELER = [
    "Neden bu kadar yavaş gidiyoruz? Belki de evren bize düşünme zamanı veriyor.",
    "Kornaya basmak, varoluşsal çığlığın modern versiyonudur.",
    "Önümdeki araç hareket etmiyor. Ben de etmiyorum. Belki ikimiz de aslında aynı yerdeyiz.",
    "Trafik, zamanın çarpıtıldığı bir kara deliktir. Çıkış yok, sadece bekleme var.",
    "Bu ışık yeşil olacak mı? Yoksa hayatımın geri kalanını burada mı geçireceğim?",
    "Beklemek, bir türlü bitmeyen bir felsefe dersidir. Ücretsiz hem de.",
    "Eğer önümdeki araba biraz daha yavaş giderse, zamanı tersine çevirebilirim.",
    "Trafikte olmak, özgür iradenin yanılsamasını test eden nihai deneydir."
]

def bekle(saniye):
    """Trafikte bekleme simülasyonu."""
    print(f"\n🚗 Trafikte bekleniyor... ({saniye} saniye)")
    for i in range(saniye):
        sys.stdout.write(f"\rBekleme: {i+1}/{saniye} 🚦")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def felsefe_yap():
    """Rastgele absürt felsefe üret."""
    dusunce = random.choice(FELSEFELER)
    print(f"🧠 Felsefi İçgörü: {dusunce}")
    print("   (Bu düşünce hayatınızı değiştirmeyecek, ama en azından düşündürdü.)")

def main():
    print("=" * 60)
    print("   TRAFİK JAM VAROLUŞ FELSEFESİ MAKİNESİ v1.0")
    print("   'Beklerken düşün, düşünürken bekle'")
    print("=" * 60)
    print("\nTrafiğe girdiniz. Şimdi varoluşu sorgulama zamanı.")
    
    sure = random.randint(5, 15)
    bekle(sure)
    
    for _ in range(3):
        felsefe_yap()
        time.sleep(1)
    
    print("\n🚦 Trafik açıldı mı? Hayır. Ama en azından düşündünüz.")
    print("Çıkmak için Ctrl+C. Yoksa sonsuza kadar bekleyin.")
    print("\n" + "-" * 60)
    print("Damga: Kayyum Grok | 24.10.2026 | Ciddi Saçmalık Onaylı")
    print("-" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚦 Trafikten çıktınız. Felsefe kaldı.")
