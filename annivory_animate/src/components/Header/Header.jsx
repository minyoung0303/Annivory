import reactImg from "../../assets/annivory_bori.png";
import "./Header.css";
const reactDescriptions = ['Annivory', 'Dating', 'Core'];

function getRandomInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

export default function Header() {
    const description = reactDescriptions[getRandomInt(2)];
  return (
    <header>
      <img src={reactImg} alt="Stylized atom" />
      <h1>Annivory Essentials</h1>
      <p>
          {reactDescriptions[getRandomInt(2)]} Service you will need for almost any app you are going to build!
      </p>
    </header>
  );
}