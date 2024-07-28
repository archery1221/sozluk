yeni_terim = input("Eklemek istediğin terim nedir?\n")
yeni_anlam = input("Kelimenin anlamı nedir?\n")
genc_sozluk[yeni_terim] = yeni_anlam
sorgu = input("Hangi kelimenin anlamını öğrenmek istersin?")
print(genc_sozluk[sorgu])