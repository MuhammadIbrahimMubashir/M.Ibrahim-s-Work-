import streamlit as st
import hashlib

# 🔑 Caesar Cipher Shift Key
SHIFT = 3

# 🧠 In-memory storage
stored_data = {}
if "failed" not in st.session_state:
    st.session_state.failed = 0

# 🔐 Hash the passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# 🔒 Caesar Encrypt
def caesar_encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = SHIFT if char.islower() else -SHIFT
            result += chr((ord(char) + shift) % 256)
        else:
            result += char
    return result

# 🔓 Caesar Decrypt
def caesar_decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = -SHIFT if char.islower() else SHIFT
            result += chr((ord(char) + shift) % 256)
        else:
            result += char
    return result

# 🔍 Check and decrypt
def decrypt_data(encrypted_text, passkey):
    correct_pass = hash_passkey(passkey)
    for saved_text, info in stored_data.items():
        if saved_text == encrypted_text and info["passkey"] == correct_pass:
            st.session_state.failed = 0
            return caesar_decrypt(encrypted_text)
    st.session_state.failed += 1
    return None

# 🖥️ Streamlit App
st.title("🔒 Simple Secure Data App")

menu = ["🏠 Home", "📝 Save Data", "🔍 View Data", "🔑 Login"]
choice = st.sidebar.selectbox("Choose Page", menu)

if choice == "🏠 Home":
    st.write("Welcome! Save and view secret messages using Caesar Cipher.")

elif choice == "📝 Save Data":
    st.subheader("Save Secret Message")
    text = st.text_area("Enter your secret:")
    passkey = st.text_input("Create a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if text and passkey:
            encrypted = caesar_encrypt(text)
            stored_data[encrypted] = {"passkey": hash_passkey(passkey)}
            st.success("✅ Data saved successfully!")
            st.code(encrypted)
        else:
            st.warning("⚠️ Fill all fields.")

elif choice == "🔍 View Data":
    st.subheader("Retrieve Secret Message")
    encrypted_text = st.text_area("Paste encrypted text:")
    passkey = st.text_input("Enter passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success("✅ Your Message:")
                st.code(result)
            else:
                st.error(f"❌ Incorrect passkey! Tries left: {3 - st.session_state.failed}")
                if st.session_state.failed >= 3:
                    st.warning("🔒 Too many attempts! Go to Login.")
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Fill all fields.")

elif choice == "🔑 Login":
    st.subheader("Re-login")
    master = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master == "admin123":
            st.session_state.failed = 0
            st.success("✅ Logged in! Try again now.")
        else:
            st.error("❌ Wrong password!")
