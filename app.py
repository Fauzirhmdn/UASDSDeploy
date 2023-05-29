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
    st.title('Prediksi Gagal Jantung Menggunakan Model XGBoost')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Umur')

    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')

    with col1:
        Cholesterol = st.text_input('Serum Kolestoral dalam mg/dl')

    with col1:
        FastingBS = st.text_input('Gula Darah Puasa (Fasting Blood Sugar) : 1 jika FastingBS > 120 mg/dl, 0: selainnya')

    with col1:
        MaxHR = st.text_input('Detak Jantung Maksimum yang Tercapai (Maximum Heart Rate)')

    with col1:
        Oldpeak = st.text_input('Numeric value measured in depression ((Oldpeak asli + 1) x 10')

    with col1:
        Sex_F = st.text_input('Kelamin Perempuan (1 jika iya, 0 jika bukan)')

    with col1:
        Sex_M = st.text_input('Kelamin Laki-laki (1 jika iya, 0 jika bukan)')

    with col1:
        ChestPaintType_ASY = st.text_input('Chest Pain type ASY (Asymptomatic) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_NAP = st.text_input('Chest Pain type NAP (Non-Anginal Pain) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_TA = st.text_input('Chest Pain type TA (Typical Angina) (1 jika ada, 0 jika tidak ada)')

    with col1:
        ChestPaintType_ATA = st.text_input('Chest Pain type ATA (Atypical Angina) (1 jika ada, 0 jika tidak ada)')

    with col1:
        RestingECG_LVH = st.text_input('Resting Electrocardiographic LVH (showing probable or definite left ventricular hypertrophy by Estes criteria) (1 jika iya, 0 jika tidak)')

    with col1:
        RestingECG_Normal = st.text_input('Resting Electrocardiographic Normal (1 jika iya, 0 jika tidak)')

    with col1:
        RestingECG_ST = st.text_input('Resting Electrocardiographic ST having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) (1 jika iya, 0 jika tidak)')

    with col1:
        ExerciseAngina_N = st.text_input('Exercise Induced Angina N (1 jika tidak ada, 0 jika ada)')

    with col1:
        ExerciseAngina_Y = st.text_input('Exercise Induced Angina Y (1 jika ada, 0 jika tidak ada)')

    with col1:
        ST_Slope_Down = st.text_input('Slope of the peak exercise ST segment Down (1 jika iya, 0 jika tidak)')

    with col1:
        ST_Slope_Flat = st.text_input('Slope of the peak exercise ST segment Flat (1 jika iya, 0 jika tidak)')

    with col1:
        ST_Slope_Up = st.text_input('Slope of the peak exercise ST segment Up (1 jika iya, 0 jika tidak)')
        

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
      
