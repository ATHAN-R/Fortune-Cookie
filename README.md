🥠 Fortune Cookie API  

A fun Flask web app that generates random **fortune cookie messages**.  
Users can enter their name, click the cookie to “break” it, and reveal their fortune 🍀.  

---

## ✨ Features
- 🎲 Randomly generates fortune cookie messages.  
- 🧑 Personalized fortune by adding your name.  
- 🖼️ Interactive cookie images (`before` and `after`).  
- 🌐 Works as both a **web app** and a **REST API**.  

---

## ⚙️ Installation & Setup
1. Clone or create the project
2. Install Flask
3. Project Structure
4. Run the App
5. Open in Browser
Go to 👉 http://127.0.0.1:5000/

## Import requests

url = "http://127.0.0.1:5000/fortune"
data = {"name": "Van"}
response = requests.post(url, json=data)
print(response.json())

Demo
cookie_before.jpg → closed fortune cookie
cookie_after.jpg → broken fortune cookie with revealed fortune
