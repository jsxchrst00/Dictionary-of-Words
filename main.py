meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'ROFL': 'tanggapan terhadap lelucon',
            'SHEESH': 'sedikit ketidaksetujuan',
            'CREEPY': 'menakutkan, tidak menyenangkan',
            'AGGRO': 'untuk menjadi agresif/marah',
            'SKIBIDI': 'wacky word that references or makes fun of the absurdity of slang',
            'RIZZ': 'an ability to charm and woo a person',
            }
print('Welcome to Dictionary Of Words')
for i in range(5):
  word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
  if word in meme_dict.keys():
      print(meme_dict[word])
  else:
      print('Sorry, I can not find it')
