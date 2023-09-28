import React, { useState, useEffect, ChangeEvent } from 'react';
import Select from 'react-select';
import '../css/monsters.css'

interface Monster {
  id: number;
  name: string;
  size: string;
  type: string;
  subtype: string;
  alignment: string;
  armor_class: number;
  hit_points: number;
  hit_dice: string;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
  challenge_rating: number;
  url: string;
  // Add other fields as necessary
}

const MonstersPage: React.FC = () => {
  const [monsters, setMonsters] = useState<Monster[]>([]);
  const [selectedMonster, setSelectedMonster] = useState<Monster | null>(null);

  const [editableFields, setEditableFields] = useState<any>({});


  useEffect(() => {
    // Replace with your Flask API endpoint
    fetch('http://localhost:5000/monsters')
      .then(response => response.json())
      .then(data => setMonsters(data.monsters))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const monsterOptions = monsters.map(monster => ({
    value: monster.id,
    label: monster.name,
  }));

  const handleFieldChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setEditableFields({
      ...editableFields,
      [name]: value,
    });
  };

  return (
    <div>
      <h1>Select a Monster</h1>
      <Select
        options={monsterOptions}
        isSearchable={true}
        onChange={option => {
          const monster = monsters.find(m => m.id === (option as any).value);
          setSelectedMonster(monster);
          if (monster) {
            setEditableFields(monster);
          }
        }}
      />
      {selectedMonster && (
        <div>
          <h3>Edit Selected Monster:</h3>


          <form>
  <label>
    Name:
    <input
      name="name"
      placeholder="Name"
      value={editableFields.name || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Size:
    <input
      name="size"
      placeholder="Size"
      value={editableFields.size || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Type:
    <input
      name="type"
      placeholder="Type"
      value={editableFields.type || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Subtype:
    <input
      name="subtype"
      placeholder="Subtype"
      value={editableFields.subtype || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Alignment:
    <input
      name="alignment"
      placeholder="Alignment"
      value={editableFields.alignment || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Armor Class:
    <input
      type="number"
      name="armor_class"
      placeholder="Armor Class"
      value={editableFields.armor_class || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Hit Points:
    <input
      type="number"
      name="hit_points"
      placeholder="Hit Points"
      value={editableFields.hit_points || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Hit Dice:
    <input
      name="hit_dice"
      placeholder="Hit Dice"
      value={editableFields.hit_dice || ''}
      onChange={handleFieldChange}
    />
  </label>

  {/* Skipping JSON fields for now... */}

  <label>
    Strength:
    <input
      type="number"
      name="strength"
      placeholder="Strength"
      value={editableFields.strength || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Dexterity:
    <input
      type="number"
      name="dexterity"
      placeholder="Dexterity"
      value={editableFields.dexterity || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Constitution:
    <input
      type="number"
      name="constitution"
      placeholder="Constitution"
      value={editableFields.constitution || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Intelligence:
    <input
      type="number"
      name="intelligence"
      placeholder="Intelligence"
      value={editableFields.intelligence || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Wisdom:
    <input
      type="number"
      name="wisdom"
      placeholder="Wisdom"
      value={editableFields.wisdom || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Charisma:
    <input
      type="number"
      name="charisma"
      placeholder="Charisma"
      value={editableFields.charisma || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    Challenge Rating:
    <input
      type="number"
      step="0.01"
      name="challenge_rating"
      placeholder="Challenge Rating"
      value={editableFields.challenge_rating || ''}
      onChange={handleFieldChange}
    />
  </label>

  <label>
    URL:
    <input
      name="url"
      placeholder="URL"
      value={editableFields.url || ''}
      onChange={handleFieldChange}
    />
  </label>
  
</form>

 


        </div>
      )}
    </div>
  );
};

export default MonstersPage;
