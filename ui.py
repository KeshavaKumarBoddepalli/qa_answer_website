import streamlit as st
from search import answer_query
from indexer import DocumentIndexer
from scraper import fetch_website_content

st.title("AI Q&A Agent")

url = st.text_input("Enter Help Website URL:")

if st.button("Scrape Documentation", key="scrape"):
    content = fetch_website_content(url)
    if content:
        indexer = DocumentIndexer()  # ✅ Create an instance
        indexer.index_documents([content])  # ✅ Call it properly
        st.success("Scraping successful! Now you can ask questions.")
        # st.write(f"✅ Indexed {len(indexer.docs)} documents.")  # Debugging
    else:
        st.error("Failed to scrape content.")

indexer = DocumentIndexer()  # ✅ Ensure indexer is available for searching

query = st.text_input("Ask a question:")

if st.button("Get Answer", key="get_answer"):
    if not query:
        st.warning("Please enter a question.")
    else:
        response = answer_query(query, indexer)
        st.write(f"**Answer:** {response}")

# import streamlit as st
# import pickle
# from llm_utils import ask_llm  # Import the function properly
# from scraper import fetch_website_content  # Keep scraping functionality

# st.title("🤖 AI-Powered Q&A Agent")

# # Scraping UI
# url = st.text_input("Enter Help Website URL:")

# if st.button("Scrape Documentation", key="scrape"):
#     content = fetch_website_content(url)
#     if content:
#         st.success("Scraping successful! Now you can ask questions.")
#     else:
#         st.error("Failed to scrape content.")

# # Q&A UI
# query = st.text_input("Ask a question:")

# if st.button("Get Answer", key="get_answer"):
#     if not query.strip():
#         st.warning("Please enter a question.")
#     else:
#         with st.spinner("Thinking..."):
#             response = ask_llm(query)  # ✅ Use the function directly
#         st.write(f"**Answer:** {response}")
