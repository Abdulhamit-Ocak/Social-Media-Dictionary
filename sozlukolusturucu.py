social_media_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "BRAINROT": "Sürekli internette aktif olan ve internet miimlerine bağımlı hale gelen kişi,şahıs",
            "REPOST" : "Bir gönderimi yeniden paylaşmak",
            "CLICKBAIT": "Tıklanma almak için gerçek olmayan ibareleri kullanmak,sahtekarlık",
            "TREND": "Sosyal medyada birşeyin popüler olması",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in social_media_dict.keys():
    print(social_media_dict[word])
else:
    print("Kelime sözlükte yok")
