<p align="center">
  <img src="Acadex Banner.png" alt="Face Recognition Attendance App Banner" width="800"/>
</p>

# 🏫 Face Recognition Attendance App

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green?logo=opencv&logoColor=white)](https://opencv.org/)  
[![Firebase](https://img.shields.io/badge/Firebase-RealtimeDB-orange?logo=firebase&logoColor=white)](https://firebase.google.com/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Stars](https://img.shields.io/github/stars/Rishabh-Sahni-0809/Face-Recognition-Attendance-app.svg)](https://github.com/Rishabh-Sahni-0809/Face-Recognition-Attendance-app/stargazers)

---

## 📖 Overview  

The **Face Recognition Attendance App** is a Python-based smart attendance system.  
It leverages **face recognition, OpenCV, Firebase, and cvzone** to automatically detect faces via webcam, verify them against registered students, and update their attendance in real time.  

This system eliminates manual errors, provides cloud storage integration, and offers a sleek UI overlay for smooth user experience.  

---

## ✨ Features  

- 👁️ **Real-Time Face Detection & Recognition**  
- 📸 **Webcam Integration** with OpenCV  
- 🔄 **Firebase Integration**  
  - Store student info (ID, Name, Major, Year, Standing) in Realtime Database  
  - Save profile images in Firebase Storage  
- 🧾 **Auto Attendance Logging**  
  - Updates last attendance time  
  - Increments total attendance count  
- 🖼️ **Student Info Display** on-screen using cvzone overlays  
- 🎨 **Custom Background & Mode Images** for a clean UI  

---

## 🛠️ Tech Stack / Technologies Used  

**Languages & Frameworks**  
- Python 🐍  

**Libraries**  
- OpenCV → video capture & processing  
- face_recognition → facial encodings & matching  
- cvzone → GUI overlays (corner rectangles, styled text)  
- NumPy → matrix operations  
- Firebase Admin SDK → database + storage  

**Cloud**  
- Firebase Realtime Database → store student metadata  
- Firebase Storage → store profile pictures  

---

## 🏗️ Workflow  

```text
[Webcam] → [Face Detection & Encoding] → [Firebase Verification]  
   → [Match Student] → [Update Attendance & Timestamp]  
   → [Overlay Student Info on Background UI]
````

---

## 📸 Demo / Screenshots

| Module                     | Screenshot / Description     |
| -------------------------- | ---------------------------- |
| Main UI with Background    | *(Insert screenshot here)*   |
| Student Recognition & Info | *(Insert screenshot here)*   |
| Firebase Database Logs     | *(Screenshot of DB updates)* |

---

## ⚙️ Installation & Setup

### Prerequisites

* Python **3.8+**
* Webcam
* Firebase project with:

  * Realtime Database
  * Storage
  * Service Account Key JSON file

### Steps

```bash
# Clone the repository
git clone https://github.com/Rishabh-Sahni-0809/Face-Recognition-Attendance-app.git
cd Face-Recognition-Attendance-app

# Install dependencies
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install opencv-python face-recognition numpy cvzone firebase-admin
```

---

## 🚀 Usage

1. Place your **Firebase Service Account Key** (`serviceAccountKey.json`) in the project directory.
2. Update the paths in `Main.py` with your:

   * `databaseURL`
   * `storageBucket`
   * `serviceAccountKey.json` location
3. Add your background and mode images in `Resources/`.
4. Start the app:

```bash
python Main.py
```

---

## 📂 Project Structure

```text
Face-Recognition-Attendance-app/
│
├── Resources/                   # Backgrounds, mode images  
│   └── background.png  
├── EncodeFile.p                  # Pickle file storing known encodings & IDs  
├── Main.py                     # Main application logic  
├── serviceAccountKey.json        # Firebase credentials (private, not in repo)  
├── requirements.txt              # Dependencies  
└── README.md                     # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. Fork this repository
2. Create your feature branch → `git checkout -b feature/YourFeature`
3. Commit your changes → `git commit -m "Add Feature"`
4. Push to branch → `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgements

* [OpenCV](https://opencv.org/) for image processing
* [face_recognition](https://github.com/ageitgey/face_recognition) library
* [Firebase](https://firebase.google.com/) for backend services
* [cvzone](https://github.com/cvzone/cvzone) for UI enhancements

---

### ⭐ If you like this project, don’t forget to star the repo!

```
```
