import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#memuat model yang disimpan

heart_diseases_model = pickle.load(open('model_deteksi_penyakit_jantung.sav', 'rb'))


# navigasi sidebar

with st.sidebar:
    selected = option_menu('Sistem Prediksi',
                ['Prediksi Penyakit Jantung'],
                icons=['heart'], default_index=0)


#halaman prediksi penyakit jantung

if (selected == 'Prediksi Penyakit Jantung'):
    
    # page title
    st.title('Sistem Prediksi Penyakit Jantung ')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Umur')

    with col1:
        RestingBP = st.text_input('Tekanan darah saat istirahat')

    with col1:
        Cholesterol = st.text_input('Serum Kolestoral dalam mg/dl')

    with col1:
        FastingBS = st.text_input('Gula Darah Puasa (Fasting Blood Sugar) : 1 jika FastingBS > 120 mg/dl, 0: selainnya')

    with col1:
        MaxHR = st.text_input('Detak Jantung Maksimum yang Tercapai (Maximum Heart Rate)')

    with col1:
        Oldpeak = st.text_input('Oldpeak atau Nilai numerik yang diukur dalam depresi ((Oldpeak asli + 1) x 10')

    with col1:
        Sex_F = st.text_input('Kelamin Perempuan (1 jika iya, 0 jika bukan)')

    with col1:
        Sex_M = st.text_input('Kelamin Laki-laki (1 jika iya, 0 jika bukan)')

    with col1:
        ChestPaintType_ASY = st.text_input('Tipe nyeri dada ASY (Asymptomatic) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_NAP = st.text_input('Tipe nyeri dada NAP (Non-Anginal Pain) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_TA = st.text_input('Tipe nyeri dada TA (Typical Angina) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_ATA = st.text_input('Tipe nyeri dada ATA (Atypical Angina) (1 jika ada, 0 jika tidak ada)')

    with col1:
        RestingECG_LVH = st.text_input('Istirahat Elektrokardiografi LVH (showing probable or definite left ventricular hypertrophy by Estes criteria) (1 jika iya, 0 jika tidak)')

    with col1:
        RestingECG_Normal = st.text_input('Istirahat Elektrokardiografi Normal (1 jika iya, 0 jika tidak)')

    with col1:
        RestingECG_ST = st.text_input('Istirahat Elektrokardiografi ST yang memiliki kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi ST > 0,05 mV) (1 jika iya, 0 jika tidak)')

    with col1:
        ExerciseAngina_N = st.text_input('Exercise Induced Angina N (1 jika tidak ada, 0 jika ada)')

    with col1:
        ExerciseAngina_Y = st.text_input('Exercise Induced Angina Y (1 jika ada, 0 jika tidak ada)')

    with col1:
        ST_Slope_Down = st.text_input('Kemiringan puncak latihan segmen ST ke bawah (1 jika iya, 0 jika tidak)')

    with col1:
        ST_Slope_Flat = st.text_input('Kemiringan puncak latihan segmen ST mendatar (1 jika iya, 0 jika tidak)')

    with col1:
        ST_Slope_Up = st.text_input('Kemiringan puncak latihan segmen ST ke atas (1 jika iya, 0 jika tidak)')
        

# kode untuk prediksi
heart_diagnosis = ''
    
# membuat tombol untuk Prediksi

if st.button('Hasil Tes Penyakit Jantung'):
    input_data = (Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, Sex_F, Sex_M, ChestPaintType_ASY, ChestPaintType_NAP, ChestPaintType_TA,  ChestPaintType_ATA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up)
        
# changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=object)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
    heart_prediction = heart_diseases_model.predict(input_data_reshaped)

    if (heart_prediction[0] == 1):
          heart_diagnosis = 'Orang tersebut memiliki penyakit jantung'
    else:
          heart_diagnosis = 'Orang tersebut tidak memiliki penyakit jantung'
        
st.success(heart_diagnosis)
      
