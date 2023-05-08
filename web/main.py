import streamlit as st
import requests
import json

def main():
    st.title("Audio classificator")

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


