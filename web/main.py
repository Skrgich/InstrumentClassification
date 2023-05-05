# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# st.write("Hello!")

import streamlit as st
import requests
import json

def main():
    st.title("File Uploader")

    # Allow user to upload a file
    uploaded_file = st.file_uploader("Choose a file", type=['wav'])

    if uploaded_file:

        # api_url = "http://api/docs#/default/upload_file_upload_post"
        # api_url = "http://api:80/upload"
        api_url = "http://api:80/upload"
        

        #  data= {'filename' : uploaded_file}, 
        response = requests.post(url = api_url, files={'file' : uploaded_file.getvalue()}, timeout= 5)
        
        # if response.status_code == 200:# and response.headers["content-type"].strip().startswith("application/json"):

        dictionary = response.json()
        output = "Instruments detected:\n"
        # st.write("Instruments detected:")
        for k in dictionary:
            if (dictionary[k] == 1):
                output += "* {}\n".format(k)
                # st.markdown("\t{}".format(k))

        st.write(output)

        # st.markdown('''
        #     <style>
        #     [data-testid="stMarkdownContainer"] ul{
        #         padding-left:40px;
        #     }
        #     </style>
        #     ''', unsafe_allow_html=True)

        # dictionary = json.load(response.json())
        # for k, v in dictionary:
        #     st.write("{} : {}".format(k, v))

        # st.write(response.json())
            # st.write(response.json())
    

    # if uploaded_file is not None:
    #     # Read and display the contents of the file
    #     file_contents = uploaded_file.read()
    #     st.write(f"Instruments:\n\n{file_contents.decode('utf-8')}")

if __name__ == '__main__':
    main()




# import requests
# import streamlit as st

# api_url = "http://<api_container_ip>:<api_port>/<api_endpoint>"
# response = requests.get(api_url)

# if response.status_code == 200:
#     # Load the JSON data from the response
#     data = response.json()

#     # Display the data in the Streamlit app
#     st.write(data)

# else:
#     # Handle error
#     st.error(f"Error {response.status_code}: {response.reason}")
