import streamlit as st
import random

# Page config
st.set_page_config(page_title="CodeAlpha Quote Generator", page_icon="💡")

# CSS for clean UI
st.markdown("""
<style>
.quote-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
    margin: 20px 0;
    text-align: center;
}
.quote-text {
    font-size: 24px;
    font-style: italic;
    color: #262730;
}
.author-text {
    font-size: 18px;
    color: #555;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Quotes list - aap aur add kar sakti ho
quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair"}
]

# Title
st.title("💡 Random Quote Generator")
st.write("CodeAlpha AI Internship - Task 2")

# Session state me quote store karo
if 'quote' not in st.session_state:
    st.session_state.quote = random.choice(quotes)

# New Quote button
if st.button("✨ New Quote", use_container_width=True):
    st.session_state.quote = random.choice(quotes)

# Display quote
st.markdown(f"""
<div class="quote-box">
    <div class="quote-text">"{st.session_state.quote['text']}"</div>
    <div class="author-text">— {st.session_state.quote['author']}</div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made for CodeAlpha Internship | @CodeAlpha")