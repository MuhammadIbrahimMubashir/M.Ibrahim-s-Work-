import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# 🔑 Step 1: Create a secret key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# 🧠 Step 2: Use memory to save data
stored_data = {}
if "failed" not in st.session_state:
    st.session_state.failed = 0

# 🔐 Step 3: Make passkey safe by hashing
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# 🔒 Step 4: Encrypt the message
def encrypt_message(text):
    return cipher.encrypt(text.encode()).decode()

# 🔓 Step 5: Decrypt the message
def decrypt_message(encrypted_text, passkey):
    correct_pass = hash_passkey(passkey)

    for saved_text, info in stored_data.items():
        if saved_text == encrypted_text and info["passkey"] == correct_pass:
            st.session_state.failed = 0
            return cipher.decrypt(encrypted_text.encode()).decode()

    st.session_state.failed += 1
    return None

# 🖥️ Step 6: Build the Streamlit app
st.title("🔒 Easy Secure Data App")

menu = ["🏠 Home", "📝 Save Data", "🔍 View Data", "🔑 Login"]
choice = st.sidebar.selectbox("Choose Page", menu)

# 🏠 Home Page
if choice == "🏠 Home":
    st.write("Welcome! This app helps you **save and get secret messages** with a passkey.")

# 📝 Save Data Page
elif choice == "📝 Save Data":
    st.subheader("Save Your Secret Message")
    text = st.text_area("Type your secret here:")
    passkey = st.text_input("Create a passkey:", type="password")

    if st.button("Save"):
        if text and passkey:
            encrypted = encrypt_message(text)
            stored_data[encrypted] = {
                "passkey": hash_passkey(passkey)
            }
            st.success("✅ Saved Successfully!")
            st.code(encrypted)
        else:
            st.warning("⚠️ Please enter both text and passkey.")

# 🔍 View Data Page
elif choice == "🔍 View Data":
    st.subheader("View Your Secret")
    encrypted_text = st.text_area("Paste your saved encrypted text:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("View"):
        if encrypted_text and passkey:
            result = decrypt_message(encrypted_text, passkey)
            if result:
                st.success("✅ Your Message:")
                st.code(result)
            else:
                st.error(f"❌ Wrong passkey! Attempts left: {3 - st.session_state.failed}")
                if st.session_state.failed >= 3:
                    st.warning("🔒 Too many tries! Go to Login.")
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Please enter all fields.")

# 🔑 Login Page
elif choice == "🔑 Login":
    st.subheader("Re-login to Try Again")
    login = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login == "admin123":
            st.session_state.failed = 0
            st.success("✅ Logged in! You can try again now.")
        else:
            st.error("❌ Wrong password!")
