import streamlit as st
import requests
import json

def main():
    st.set_page_config(page_title = "π=4")
    st.title("Audio classificator")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'π=4'; 
            font-size:xx-large;
            visibility: visible;
            display: block;
            #background-color: red;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    uploaded_file = st.file_uploader("Choose a file", type=['wav'])

    if uploaded_file:

        # api_url = "http://api/docs#/default/upload_file_upload_post"
        # api_url = "http://api:80/upload"
        api_url = "http://api:80/upload"
        

        response = requests.post(url = api_url, files={'file' : uploaded_file.getvalue()}, timeout= 5)
        

        dictionary = response.json()
        output = "Instruments detected:\n"

        for k in dictionary:
            if (dictionary[k] == 1):
                output += "* {}\n".format(k)

        st.write(output)


if __name__ == '__main__':
    main()


