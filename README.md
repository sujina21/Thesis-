Nail Art & Makeup Recommendation System
A machine learning-driven platform that recommends nail art and makeup styles tailored to each user’s tastes, history, and current trends. Built to help users quickly find styles they love via a user-friendly Flutter mobile app, while giving admins and beauty professionals a web interface for management and insights. The system tracks every user’s search history and purchase history, enabling more personalized recommendations and data-driven business strategies.

📁 Project Structure
text
NailArtRecoSystem/
├── backend/      # Node.js & Express.js backend (with MongoDB)
├── ml_model/     # Python ML model (recommendation engine)
├── frontend/     # Flutter mobile app for users
├── admin_web/    # React.js or web dashboard for admins
├── database/     # MongoDB schema and sample data
└── README.md     # Project documentation
✨ Features
🔍 Browse nail art and makeup styles with logging in

💅 Personalized style recommendations based on search and purchase history

🖼️ Visual previews of nail art and makeup designs

🛒 Option to book styles in the app

🖥️ Web portal for admins: manage users, styles, and monitor platform trends

📊 Analytics dashboard for top recommendations using AI, tracking popular searches, purchases, and trends

🌐 Responsive UI on web and mobile and tablet

🔧 Tech Stack
User Mobile App: Flutter (Android)

Admin Web Portal: React.js (or similar)

Backend: Node.js, Express.js, MongoDB

Machine Learning: Python (scikit-learn, pandas) for recommendations

Authentication: JWT, Bcrypt (password security)

APIs: RESTful for mobile and web integration

⚙️ Installation
Backend Setup
text
cd backend
npm install
npm run server

Flutter Mobile App Setup

cd frontend
flutter pub get
flutter run

MongoDB Setup
Make sure MongoDB is running locally, or configure the backend .env to your MongoDB URI.

(Optional) Seed initial data from the database/ directory.

Ethics & Privacy
Only collects search and purchase data with user consent.

All data is stored securely and transparently.

Recommendations are designed to be unbiased and inclusive.

Clear policies give users control over their information.

Author: Sujina Shrestha
