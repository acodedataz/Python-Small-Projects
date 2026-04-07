# ==========================================
# 🎮 Python Project__02 : Funny Mad Libs Pro
# 👨‍💻 Developer : Shanto
# ==========================================

import random

print("="*50)
print("😂 Welcome to Funny Mad Libs Game PRO 😂")
print("="*50)

# ============================
# 🧾 User Inputs (Enhanced)
# ============================
user_name = input("👤 Enter your name: ")
nickname = input("😎 Your nickname (funny one): ")
father_name = input("👨 Father's name: ")
mother_name = input("👩 Mother's name: ")
studying_class = input("📚 Which class do you study in? ")
best_friend = input("👬 Your best friend's name: ")
crush_name = input("❤️ Your crush name (optional 😏): ")
favorite_food = input("🍔 Your favorite food: ")
favorite_hobby = input("🎯 Your hobby: ")
dream_job = input("💼 Your dream job: ")
relationship_status = input("💔 Relationship status: ")

print("\n⏳ Generating your EPIC story...\n")

# ============================
# 🎲 Random Funny Lines
# ============================
wifi_threats = [
    "I will cut the WiFi 😡",
    "No internet for 7 days 😤",
    "I will take your phone away 📱❌"
]

lazy_excuses = [
    "studying hard... in dreams 😴",
    "opening book and sleeping instantly 😆",
    "watching YouTube 'for education' 😂"
]

future_twist = [
    "but ended up eating pizza 🍕",
    "but got distracted by Facebook 📱",
    "but slept for 10 hours 😴"
]

# ============================
# 🤣 Story Generator
# ============================
story = f"""
🌟 Once upon a time, there was a legend named {user_name}
also known as "{nickname}" 😎

👨 His father {father_name} always shouted:
"Study hard or {random.choice(wifi_threats)}"

👩 His mother {mother_name}?
She has FBI-level searching power 🔍😳

📚 Currently studying in class {studying_class},
but reality check 👉 {random.choice(lazy_excuses)}

👬 Best friend: {best_friend}
Together they do... absolutely nothing productive 🤣

❤️ Crush: {crush_name if crush_name else "Secret 🤫"}
(Still waiting for reply... last seen 2 years ago 😭)

🍔 Favorite food: {favorite_food}
🎯 Hobby: {favorite_hobby}

💔 Relationship Status:
"{relationship_status}"
(Reality: single but hopeful 😆)

🔥 Dream: Become a {dream_job} 💼
Plan: Start tomorrow...
Result: {random.choice(future_twist)}

🏁 THE END...
Or maybe just the beginning of laziness 😂
"""

# ============================
# 🖨 Output
# ============================
print(story)

print("="*50)
print("✅ Story Generated Successfully!")
print("="*50)