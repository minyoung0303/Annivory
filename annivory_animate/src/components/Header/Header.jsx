import reactImg from "../../assets/annivory_bori.png";
import { useNavigate } from 'react-router-dom';
import "./Header.css";

const reactDescriptions = [
    'Share moments📷 from your daily life in your app!',
    'Document your trips🛫 and adventures🚜 for everyone to see!',
    'Celebrate🎉 special anniversaries🎁 with memorable posts!',
    'Showcase your ⭐favorite things⭐ and recommendations',
    'Tell interesting stories💬 about your friends and connections!'
];

function getRandomInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

export default function Header() {
    const description = reactDescriptions[getRandomInt(2)];
    const navigate = useNavigate();
  return (
    <header>
      <img src={reactImg} alt="Stylized atom" />
      <h1>
          Annivory
          <p>
              for a Memory-Keeping Blog
          </p>
      </h1>
      <div style={{ position: 'absolute', top: 20, right: 20 }}>
          <button onClick={() => navigate('/mypage')}> My Page </button>
          <button onClick={() => navigate('/login')} style={{ marginLeft: '10px' }}> Log In </button>
      </div>
      <p>
          {reactDescriptions[getRandomInt(4)]}
      </p>
    </header>
  );
}