import pickle
import streamlit as st

# membaca model
jamur_model = pickle.load(open('klasifikasi_jamur.sav', 'rb'))

#judul web
st.title('Prediksi Jamur Beracun ')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    cap_shape = st.number_input ('Bentuk Topi: cembung=0, lonceng=1, cekung=2, datar=3, polkadot=4, kerucut=5')
    cap_surface = st.number_input ('Tutup_permukaan: halus = 0, bersisik = 1, berserat = 2, alur = 3')
    cap_color = st.number_input ('Warna topi: coklat=0, kuning=1, putih=2, abu_abu=3, merah=4, merah muda=5, buff=6, ungu=7, kayu manis=8, hijau=9')
    bruises = st.number_input ('Perubahan warna atau permukaan jamur setelah ditekan: Benar = 1 ; Salah = 0')
    odor = st.number_input ('Bau: menusuk/tajam=0, almond=1, anise=2, tidak ada=3, busuk=4, kreosot=5, amis=6, pedas=7, apek=8')
    

with col2 :
    gill_attachment = st.number_input ('Lampiran insang: terpasang = 0, bebas = 1')
    gill_spacing = st.number_input ('Jarak insang: ramai=0, dekat=1')
    gill_size = st.number_input ('Ukuran insang: luas=0, sempit=1')
    gill_color = st.number_input ('Warna insang: hitam=0, coklat=1, abu_abu=2, merah muda=3, putih=4, coklat=5, ungu=6, merah=7, buff=8, hijau=9, kuning= 10, oranye=11')
    population = st.number_input ('Populasi: tersebar=0, berjumlah=1, melimpah=2, beberapa=3, soliter=4, berkerumun=5')
    habitat = st.number_input ('Habitat: perkotaan=0, rumput=1, padang rumput=2, hutan=3, jalur=4, limbah=5, daun=6')

# code untuk prediksi
jamur_predict = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Jamur'):
    jamur_prediction = jamur_model.predict([[cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment,
                                             gill_spacing, gill_size, gill_color, population, habitat]])

    if(jamur_prediction[0] == 1):
        jamur_predict = 'Jamur Beracun'
    else:
        jamur_predict = 'Jamur Tidak Beracun'
st.success(jamur_predict)
