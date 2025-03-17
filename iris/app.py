import streamlit as st
import pickle
import os

image_folder = "static"

st.set_page_config(
    page_title="Iris App",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stSidebar .stVerticalBlock .stElementContainer:last-child { position: absolute; top: max(calc(100vh - 110%), calc(100% + 40px)); width: 100%; text-align: center; }}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    with open("model/IrisClassifier.pkl", "rb") as file:
        loaded_model = pickle.load(file)

    return loaded_model

model = load_model()

with st.sidebar:
    st.markdown("## Iris Classification App")
    st.write("Enter the parameters of the iris flower to find out its appearance.")
    st.sidebar.markdown(
        '<div class="st-at">Made with <span style="color:red;">❤</span> by <a href="https://t.me/onezuppi">zuppi</a></div>',
        unsafe_allow_html=True
    )


with st.container():
    st.title("Prediction of the type of iris")
    with st.form(key="my_form"):
        st.write("Enter the characteristics of the iris below:")
        sepal_length = st.text_input("Sepal Length")
        sepal_width = st.text_input("Sepal Width")
        petal_length = st.text_input("Petal Length")
        petal_width = st.text_input("Petal Width")
        _, col, _ = st.columns(3)
        submitted = col.form_submit_button(label="Predict", use_container_width=True)

        if submitted:
            if sepal_length and sepal_width and petal_length and petal_width:
                try:
                    data = [[
                        float(sepal_length),
                        float(sepal_width),
                        float(petal_length),
                        float(petal_width)
                    ]]

                    prediction = model.predict(data)
                    predicted_flower = prediction[0]

                    st.success(f"Predicted appearance: {predicted_flower}")\

                    if predicted_flower == "Setosa":
                        image_path = os.path.join(image_folder, "setosa.jpg")
                    elif predicted_flower == "Versicolor":
                        image_path = os.path.join(image_folder, "versicolor.jpg")
                    else:
                        image_path = os.path.join(image_folder, "virgnica.jpg")

                    st.image(image_path, caption=predicted_flower, use_container_width=True)

                except ValueError:
                    st.error("Please enter numeric values for all fields!")
            else:
                st.warning("Please fill in all fields before making a prediction!")
