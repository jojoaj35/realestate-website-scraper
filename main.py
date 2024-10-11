import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

# Streamlit app title
st.title('AI Web Scraper')

# URL input for website scraping
url = st.text_input("Enter a Website URL:")

# Button to initiate website scraping
if st.button("Scrape Site"):
    st.write("Scraping the website...")
    scraped_html = scrape_website(url)
    body_content = extract_body_content(scraped_html)
    cleaned_content = clean_body_content(body_content)

    # Store cleaned content in session state
    st.session_state.dom_content = cleaned_content

    # Display cleaned content in expandable section
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Check if DOM content exists in session state
if "dom_content" in st.session_state:
    # Input field for parsing description
    parse_description = st.text_area("Describe what you want to parse:")

    # Button to parse the content based on the description
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            # Split the DOM content into manageable chunks
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # Use the parsing function to extract relevant data
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)
        else:
            st.write("Please provide a description for parsing!")
