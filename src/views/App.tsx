import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "../components/navbar";
import EquipmentPage from "./EquipmentPage";
import SpellsPage from "./SpellsPage";
import RacesPage from "./RacesPage";
import ClassesPage from "./ClassesPage";
import MonstersPage from "./MonstersPage";

const App: React.FC = () => {
  const links = [
    { name: 'Equipment', url: '/equipment' },
    { name: 'Spells', url: '/spells' },
    { name: 'Races', url: '/races' },
    { name: 'Classes', url: '/classes' },
    { name: 'Monsters', url: '/monsters' }
  ];

  return (
    <Router>
      <div className="root">
        <Navbar title="DM Tools" links={links} />
        <div className="routes">
        <Routes>
          
          <Route index element={<div>Home</div>} />
          <Route path="/equipment" element={<EquipmentPage />} />
          <Route path="/spells" element={<SpellsPage />} />
          <Route path="/races" element={<RacesPage />} />
          <Route path="/classes" element={<ClassesPage />} />
          <Route path="/monsters" element={<MonstersPage />} />
          
        </Routes>
        </div>
      </div>
    </Router>

  );
};

export default App;
