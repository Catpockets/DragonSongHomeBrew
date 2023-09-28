from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from models import DnDMonster
from extensions import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:N3koP0k3tt01!@localhost:3306/5E_Manager'

    db.init_app(app)
    CORS(app)
    return app

app = create_app()
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)
    
from dataImport import import_dnd_classes, import_dnd_spells, import_dnd_equipment, import_dnd_monsters, import_dnd_races
@app.route('/import_data')
def import_data():
    try:
        print("-- Importing Classes --")
        import_dnd_classes()
        print("Class Import Complete")
    except Exception as e:
        print(e)
    try:
        print("-- Importing Spells --")
        import_dnd_spells()
        print("Spell Import Complete")
    except Exception as e:
        print(e)
    try:
        print("-- Importing Equipment --")
        import_dnd_equipment()
        print("Equipment Import Complete")
    except Exception as e:
        print(e)
    try:
        print("-- Importing Monsters --")
        import_dnd_monsters()
        print("Monster Import Complete")
    except Exception as e:
        print(e)
    try:
        print("-- Importing Races --")
        import_dnd_races()
        print("Race Import Complete")
    except Exception as e:
        print(e)

    return 'Data import complete.'

@app.route('/monsters', methods=['GET'])
def get_monsters():
    
    monsters_query = DnDMonster.query.all()  # Fetch all monsters
    monster_dicts = []
    for monster in monsters_query:
        monster_dict = {
            'id': monster.id,
            'name': monster.name,
            'size': monster.size,
            'type': monster.type,
            'subtype': monster.subtype,
            'alignment': monster.alignment,
            'armor_class': monster.armor_class,
            'hit_points': monster.hit_points,
            'hit_dice': monster.hit_dice,
            'speed': monster.speed,
            'strength': monster.strength,
            'dexterity': monster.dexterity,
            'constitution': monster.constitution,
            'intelligence': monster.intelligence,
            'wisdom': monster.wisdom,
            'charisma': monster.charisma,
            'proficiencies': monster.proficiencies,
            'damage_vulnerabilities': monster.damage_vulnerabilities,
            'damage_resistances': monster.damage_resistances,
            'damage_immunities': monster.damage_immunities,
            'condition_immunities': monster.condition_immunities,
            'senses': monster.senses,
            'languages': monster.languages,
            'challenge_rating': monster.challenge_rating,
            'special_abilities': monster.special_abilities,
            'actions': monster.actions,
            'legendary_actions': monster.legendary_actions,
            'url': monster.url,
            'reactions': monster.reactions,
            'other_speeds': monster.other_speeds
        }
        monster_dicts.append(monster_dict)

    print(monster_dicts)
    return jsonify({"monsters": monster_dicts})
