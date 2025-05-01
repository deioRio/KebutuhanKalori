import streamlit as st

# Judul aplikasi
st.title("Rekomendasi Makanan Berdasarkan Aktivitas & Usia")

# Input pengguna
age = st.number_input("Masukkan umur Anda (tahun)", min_value=1, max_value=100)
gender = st.selectbox("Pilih jenis kelamin", ["Pria", "Wanita"])
activity_level = st.selectbox("Tingkat aktivitas fisik Anda", ["Rendah", "Sedang", "Tinggi"])

# Fungsi untuk menentukan makanan berdasarkan input
def get_food_recommendations(age, gender, activity_level):
    # Format: "nama makanan": gram
    recommended = {}
    to_avoid = {}

    if age < 18:
        recommended.update({
            "Susu rendah lemak": 250,
            "Sayuran hijau": 100,
            "Protein hewani dan nabati": 150
        })
        to_avoid.update({
            "Makanan cepat saji": 200,
            "Minuman bersoda": 330,
            "Makanan tinggi gula": 100
        })
    elif 18 <= age <= 50:
        recommended.update({
            "Karbohidrat kompleks (nasi merah, oatmeal)": 200,
            "Sayuran & buah segar": 300,
            "Protein (telur, ayam, tahu)": 200
        })
        to_avoid.update({
            "Gorengan": 150,
            "Makanan olahan": 180,
            "Terlalu banyak kafein": 200  # mg kafein bisa juga ditampilkan
        })
    else:  # usia di atas 50
        recommended.update({
            "Makanan tinggi kalsium": 250,
            "Ikan berlemak (salmon, sarden)": 150,
            "Sayur berserat tinggi": 200
        })
        to_avoid.update({
            "Makanan asin": 150,
            "Daging merah berlebihan": 200,
            "Gula tinggi": 100
        })

    if activity_level == "Tinggi":
        recommended.update({
            "Karbohidrat sehat (ubi, roti gandum)": 250,
            "Pisang": 120,
            "Air mineral yang cukup": 2000  # ml
        })
    elif activity_level == "Rendah":
        to_avoid.update({
            "Camilan manis": 100,
            "Minuman manis": 250,
            "Lemak jenuh": 70
        })

    return recommended, to_avoid

# Tampilkan rekomendasi saat tombol ditekan
if st.button("Tampilkan Rekomendasi"):
    good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level)

    st.subheader(f"✅ Makanan yang Direkomendasikan (Total: {len(good_foods)} jenis):")
    total_recommended_grams = 0
    for food, gram in good_foods.items():
        st.markdown(f"- {food}: **{gram} gram**")
        total_recommended_grams += gram
    st.markdown(f"**Total konsumsi yang disarankan: {total_recommended_grams} gram/ml**")

    st.subheader(f"🚫 Makanan yang Sebaiknya Dihindari (Total: {len(avoid_foods)} jenis):")
    total_avoid_grams = 0
    for food, gram in avoid_foods.items():
        st.markdown(f"- {food}: **{gram} gram**")
        total_avoid_grams += gram
    st.markdown(f"**Total konsumsi yang perlu dibatasi: {total_avoid_grams} gram/ml**")
