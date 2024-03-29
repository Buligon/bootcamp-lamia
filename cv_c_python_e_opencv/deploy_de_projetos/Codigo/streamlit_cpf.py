# importar pacotes
import streamlit as st
import cv2
from PIL import Image
import os
import pytesseract
from pytesseract import Output
import numpy as np


path = os.getcwd()

# Tesseract
pytesseract.pytesseract.tesseract_cmd = path + r'\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = f'--tessdata-dir "{path}\\Tesseract-OCR\\tessdata"'


def main():

    global path

    st.title("Api - CPF Detect")

    # Opcoes API
    activities = ["DetectText", "Sobre"]
    choice = st.sidebar.selectbox("Selecionar Atividade:", activities)


    if choice == "DetectText":
        
        # Upload da imagem
        image_file = st.file_uploader("Upload da imagem", type=['jpg', 'png'])
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Imagem")
            st.image(our_image, width=600)

        # txt de busca
        texto = st.text_input("Escreva o texto aqui")
        st.write(f"{texto}")

        # Deteccao do texto
        task = ["DetectTexto"]
        feature_choice = st.sidebar.selectbox("Detectar o texto", task)
        if st.button("Processar"):

            if feature_choice == "DetectTexto":
                try:
                    new_img = np.array(our_image.convert('RGB'))            

                    d = pytesseract.image_to_data(new_img, output_type=Output.DICT, lang='por', config=tessdata_dir_config)
                    n_boxes = len(d['level'])
                    overlay = new_img.copy()
                    for i in range(n_boxes):
                        text = d['text'][i]
                        print(text)                        
                        if text == texto:
                            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                            print(d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                            (x1, y1, w1, h1) = (d['left'][i + 1], d['top'][i + 1], d['width'][i + 1], d['height'][i + 1])
                            cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

                        
                    alpha = 0.4
                    img_new = cv2.addWeighted(overlay, alpha, new_img, 1-alpha, 0)

                    r = 1000.0 / img_new.shape[1]
                    dim = (1000, int(img_new.shape[0] * r))

                    resized = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)
                    st.image(resized, width=600)
                except:
                    st.info("Erro: Selecinar um arquivo válido")



    elif choice == "Sobre":
        st.subheader("Sobre API - CPF Detect")
        st.markdown("Desenvolvido por Curso Python e Opencv")
        st.info("Contato: exemplo@email.com")


if __name__ == '__main__':
    main()