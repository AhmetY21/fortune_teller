import streamlit as st
import openai
import streamlit as st
import datetime
from utils import destination_city, fortune_teller

# Define Streamlit app
def main():


    st.title("Fortune Teller for Your Next Destination")
    st.markdown("This is the app that gives you next destination based on your birth date.")

    # Datetime Picker
    st.markdown("**Select a date**")
    st.markdown("---")  # Bold line
    date = st.date_input("")
    st.markdown("---")  # Bold line


    # Call the fortune_teller function and update the result

    st.markdown("---")  # Bold line
    if st.button("Get Fortune"):
        result = fortune_teller(str(date))
        st.text_area("🔮🔮🔮🔮🔮", result)

# Run Streamlit app
if __name__ == "__main__":
    main()
