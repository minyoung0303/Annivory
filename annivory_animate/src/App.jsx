import { Routes, Route } from 'react-router-dom';


import Header from './components/Header/Header.jsx';
import Login from './pages/Login.jsx';
import MyPage from './pages/MyPage.jsx';
import MainContent from "./components/MainContent.jsx";



function App() {
  return (
    <div>
      <Header />
        <Routes>
            <Route path="/" element={<MainContent />} />
            <Route path="/login" element={<Login />} />
            <Route path="/mypage" element={<MyPage />} />
        </Routes>
    </div>
  );
}

export default App;