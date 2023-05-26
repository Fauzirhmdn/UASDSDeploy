import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

#memuat model yang disimpan

heart_diseases_model = pickle.load.open('model_deteksi_penyakit_jantung.pkl', 'rb')


# navigasi sidebar

with st.sidebar:
    selected = option_menu('prediction system',
                ['Prediksi Penyakit Jantung'],
                icons=['heart'], default_index=0)


#halaman prediksi penyakit jantung

if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Prediksi Gagal Jantung Menggunakan Model XGBoost')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Umur')

    with col2:
        RestingBP = st.text_input('Tekanan darah saat istirahat')

    with col3:
        Cholesterol = st.text_input('Serum Kolestoral dalam mg/dl') 

    with col1:
        FastingBS = st.text_input('Gula Darah Puasa (Fasting Blood Sugar) : 1 jika FastingBS > 120 mg/dl, 0: selainnya')

    with col2:
        MaxHR = st.text_input('Detak Jantung Maksimum yang Tercapai (Maximum Heart Rate)')

    with col3:
         Oldpeak = st.text_input('Oldpeak atau Nilai numerik yang diukur dalam depresi ((Oldpeak asli + 1) x 10')

    with col1:
         Sex_F = st.text_input('Kelamin Perempuan (1 jika iya, 0 jika bukan)')

    with col2:
         Sex_M = st.text_input('Kelamin Laki-laki (1 jika iya, 0 jika bukan)')

    with col3:
        ChestPaintType_ASY = st.text_input('Tipe nyeri dada ASY (Asymptomatic) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_NAP = st.text_input('Tipe nyeri dada NAP (Non-Anginal Pain) (1 jika ada, 0 jika tidak ada)')

    with col2:
        ChestPaintType_TA = st.text_input('Tipe nyeri dada TA (Typical Angina) (1 jika ada, 0 jika tidak ada)')

    with col3:
        ChestPaintType_ATA = st.text_input('Chest Pain type ATA (Atypical Angina) (1 jika ada, 0 jika tidak ada)')

    with col1:
        RestingECG_LVH = st.text_input('Istirahat LVH Elektrokardiografi (menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri menurut kriteria Estes) (1 jika iya, 0 jika tidak)')

    with col2:
        RestingECG_Normal = st.text_input('Istirahat Elektrokardiografi Normal (1 jika iya, 0 jika tidak)')

    with col3:
        RestingECG_ST = st.text_input('Istirahat Elektrokardiografi ST yang memiliki kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi ST > 0,05 mV) (1 jika iya, 0 jika tidak)')

    with col1:
        ExerciseAngina_N = st.text_input('Latihan Induced Angina N (1 jika tidak ada, 0 jika ada)')

    with col2:
        ExerciseAngina_Y = st.text_input('Latihan Induced Angina Y (1 jika ada, 0 jika tidak ada)')

    with col3:
        ST_Slope_Down = st.text_input('Kemiringan puncak latihan segmen ST ke bawah (1 jika iya, 0 jika tidak)')

    with col1:
        ST_Slope_Flat = st.text_input('Kemiringan puncak latihan segmen ST mendatar (1 jika iya, 0 jika tidak)')

    with col2:
        ST_Slope_Up = st.text_input('Kemiringan puncak latihan segmen ST ke atas (1 jika iya, 0 jika tidak)')

 # kode untuk prediksi
    heart_diagnosis = ''
    
    # membuat tombol untuk Prediksi

    if st.button('Heart Disease Test Result'):
        heart_prediction = model_deteksi_penyakit_jantung.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, Sex_F, Sex_M, ChestPaintType_ASY, ChestPaintType_NAP, ChestPaintType_TA,  ChestPaintType_ATA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]])

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
      
