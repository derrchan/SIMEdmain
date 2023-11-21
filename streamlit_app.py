import streamlit as st

def main():
    # Main page title
    st.title('Streamlit Apps')

    # Use markdown to create hyperlinks to the deployed Streamlit apps
    st.markdown('### Streamlit Applications')
    st.markdown('Below are the Streamlit applications available:')

    # Link to the deployed mcq.py app
    st.markdown('[Breast Surgery MCQs](https://simedmcq-nywtfsvzjpgvwnowpzvvgf.streamlit.app/)')

    # Link to the deployed saq.py app
    st.markdown('[Breast Surgery SAQs](https://share.streamlit.io/yourusername/yourrepository/main/saq.py)')

# Check if the script is being run directly
if __name__ == '__main__':
    main()
