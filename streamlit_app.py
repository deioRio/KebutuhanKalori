# Halaman Rekomendasi
if page == "Rekomendasi Makanan":
    st.markdown(
        """
        <div style="background-color: rgba(0, 102, 204, 0.7); padding:20px; border-radius:10px; color:white; text-align:center;">
            <h2>Rekomendasi Makanan Berdasarkan Aktivitas & Usia</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Masukkan Data Anda")

    with st.container():
        st.markdown("#### 🧓 Umur Anda")
        age = st.number_input("Masukkan umur Anda (tahun)", min_value=1, max_value=100, key="age")
        st.markdown("#### ⚖️ Berat Badan Anda")
        weight = st.number_input("Masukkan berat badan Anda (kg)", min_value=1.0, max_value=200.0, step=0.1, key="weight")
        st.markdown("#### 🚻 Jenis Kelamin")
        gender = st.selectbox("Pilih jenis kelamin", ["Pria", "Wanita"], key="gender")
        st.markdown("#### 🏃‍♂️ Tingkat Aktivitas Fisik")
        activity_level = st.selectbox("Tingkat aktivitas fisik Anda", ["Rendah", "Sedang", "Tinggi"], key="activity")

    if st.button("Tampilkan Rekomendasi"):
        good_foods, avoid_foods = get_food_recommendations(age, gender, activity_level, weight)
        efek_baik, risiko = generate_effects(good_foods, avoid_foods)
