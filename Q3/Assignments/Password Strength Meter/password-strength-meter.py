import streamlit as st

def check_password(password):
    score = 0
    tips = []
    
    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔴 Use at least 8 characters.")
    
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1
    else:
        tips.append("🟠 Mix uppercase & lowercase letters.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("🟡 Add a number (0-9).")
    
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append("🔵 Use a special character (!@#$%^&*).")
    
    return score, tips

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter Password 🔑", type="password")
    
    if password:
        score, tips = check_password(password)
        rating = ["⭐☆☆☆☆ Very Weak", "⭐⭐☆☆☆ Weak", "⭐⭐⭐☆☆ Moderate", "⭐⭐⭐⭐☆ Good", "⭐⭐⭐⭐⭐ Strong"]
        
        st.write(f"🔢 Strength Rating: {rating[score]}")
        
        if score == 4:
            st.success("✅ Strong Password! Secure & safe.")
        elif score == 3:
            st.warning("⚠️ Moderate Password! Improve it.")
        else:
            st.error("❌ Weak Password! Follow these tips:")
        
        for tip in tips:
            st.write(tip)

if __name__ == "__main__":
    main()
