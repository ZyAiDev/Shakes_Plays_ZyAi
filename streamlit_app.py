import streamlit as st
from llama_index import GPTSimpleVectorIndex
import os
import config

@st.cache_resource
def load_index():
    """load the pipeline object for preprocessing and the ml model"""

    # load index files 
    index_document = GPTSimpleVectorIndex.load_from_disk('index_txt.json')
    return index_document

def main():

    # api key
    os.environ['OPENAI_API_KEY'] = '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'

    # load index
    index_document = load_index()

    st.header('All About Shakespeare')

    # select the data to write queries for
    st.write("Select the data that your chatbot should be trained with:")
    data = st.selectbox('Data', ('.txt file (My favorite fruits)', 'Youtube Video (Vanilla Cake Recipe)', 'Wikipedia Article (Apple)'))
    
    #data = st.selectbox('Data', ('All About Shakespeare'))

    # use the index based on the selected data
    #if data == 'All About Shakespeare':
    #   st.image('/content/data/Shakespeare.png')
    #  index = index_document
    
    if data == '.txt file (My favorite fruits)':
        st.image('/content/data/Shakespeare.png')
        index = index_document
    elif data == 'Youtube Video (Vanilla Cake Recipe)':
        index = index_document
    elif data == 'Wikipedia Article (Apple)':
        index = index_document

    # query the selected index
    query = st.text_input('Enter Your Query')
    button = st.button(f'Response')
    if button:
        st.write(index.query(query))

if __name__ == '__main__':
    main()
