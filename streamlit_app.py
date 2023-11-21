import streamlit as st

def main():
    # Main page title
    st.title('HKUMed Surgery Tutor Apps')

    # Use markdown to create hyperlinks to the deployed Streamlit apps
    st.markdown('Below are the HKUMed Surgery Tutor apps available:')

    # Link to the deployed mcq.py app
    st.markdown('[Breast Surgery MCQs](https://simedmcq-nywtfsvzjpgvwnowpzvvgf.streamlit.app/)')

    # Link to the deployed saq.py app
    st.markdown('[Tutor Bot](https://share.streamlit.io/yourusername/yourrepository/main/saq.py)')

# Check if the script is being run directly
if __name__ == '__main__':
    main()
