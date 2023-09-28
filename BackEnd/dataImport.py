import csv
from main import db  # Import your SQLAlchemy instance after it's created
from models import DndClass, DndSpell, DnDEquipment, DnDMonster, DnDRace  # Import the SQLAlchemy model for the table

def import_dnd_classes():
    with open('BackEnd/static/data/dnd_classes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create a new DndClass object and populate its fields from the CSV row
            dnd_class = DndClass(
                name=row['name'],
                hit_die=int(row['hit_die']),
                proficiency_choices=row['proficiency_choices'],
                proficiencies=row['proficiencies'],
                saving_throws=row['saving_throws'],
                starting_equipment=row['starting_equipment'],
                class_levels=row['class_levels'],
                subclasses=row['subclasses'],
                url=row['url']
            )
            # Add the object to the session and commit it to the database
            db.session.add(dnd_class)
        db.session.commit()

def import_dnd_spells():
    with open('BackEnd/static/data/dnd_spells.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            spell = DndSpell(
                name=row['name'],
                classes=row['classes'].split(', '),  # Convert classes to a list
                level=int(row['level']),
                school=row['school'],
                cast_time=row['cast_time'],
                spell_range=row['spell_range'],
                duration=row['duration'],
                verbal=bool(int(row['verbal'])),
                somatic=bool(int(row['somatic'])),
                material=row['material'],
                material_cost=row['material_cost'],
                description=row['description']
            )
            db.session.add(spell)
        db.session.commit()

def import_dnd_equipment():
    with open('BackEnd/static/data/dnd_equipment.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stealth_disadvantage = None
            if row['stealth_disadvantage'].strip().lower() == 'true':
                stealth_disadvantage = True
            elif row['stealth_disadvantage'].strip().lower() == 'false':
                stealth_disadvantage = False

            equipment = DnDEquipment(
                item_name=row['item_name'],
                equipment_category=row['equipment_category'],
                gear_category=row['gear_category'],
                cost=row['cost'],
                weight=float(row['weight']) if row['weight'] else None,
                url=row['url'],
                item_desc=row['item_desc'],
                tool_category=row['tool_category'],
                vehicle_category=row['vehicle_category'],
                quantity=int(row['quantity']) if row['quantity'] else None,
                weapon_category=row['weapon_category'],
                weapon_type=row['weapon_type'],
                category_range=row['category_range'],
                damage=row['damage'],
                weapon_range=row['weapon_range'],
                properties=row['properties'],
                two_hand_damage=row['two_hand_damage'],
                armor_category=row['armor_category'],
                armor_class=row['speed'],
                str_minimum=int(row['str_minimum']) if row['str_minimum'] else None,
                stealth_disadvantage=stealth_disadvantage,
                contents=row['contents'],
                speed=row['speed'],
                capacity=row['capacity'],
                throw_range=row['throw_range'],
                special=row['special']
            )
            db.session.add(equipment)
        db.session.commit()


def import_dnd_monsters():
    with open('BackEnd/static/data/dnd_monsters.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            monster = DnDMonster(
                name=row['name'],
                size=row['size'],
                type=row['type'],
                subtype=row['subtype'],
                alignment=row['alignment'],
                armor_class=int(row['armor_class']) if row['armor_class'] else None,
                hit_points=int(row['hit_points']) if row['hit_points'] else None,
                hit_dice=row['hit_dice'],
                speed=row['speed'],
                strength=int(row['strength']) if row['strength'] else None,
                dexterity=int(row['dexterity']) if row['dexterity'] else None,
                constitution=int(row['constitution']) if row['constitution'] else None,
                intelligence=int(row['intelligence']) if row['intelligence'] else None,
                wisdom=int(row['wisdom']) if row['wisdom'] else None,
                charisma=int(row['charisma']) if row['charisma'] else None,
                proficiencies=row['proficiencies'],
                damage_vulnerabilities=row['damage_vulnerabilities'],
                damage_resistances=row['damage_resistances'],
                damage_immunities=row['damage_immunities'],
                condition_immunities=row['condition_immunities'],
                senses=row['senses'],
                languages=row['languages'],
                challenge_rating=float(row['challenge_rating']) if row['challenge_rating'] else None,
                special_abilities=row['special_abilities'],
                actions=row['actions'],
                legendary_actions=row['legendary_actions'],
                url=row['url'],
                reactions=row['reactions'],
                other_speeds=row['other_speeds']
            )
            db.session.add(monster)
        db.session.commit()

def import_dnd_races():
    with open('BackEnd/static/data/dnd_races.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            race = DnDRace(
                name=row['name'],
                speed=int(row['speed']) if row['speed'] else None,
                ability_bonuses=row['ability_bonuses'],
                alignment=row['alignment'],
                age=row['age'],
                size=row['size'],
                size_description=row['size_description'],
                starting_proficiencies=row['starting_proficiencies'],
                languages=row['languages'],
                language_desc=row['language_desc'],
                traits=row['traits'],
                trait_options=row['trait_options'],
                subraces=row['subraces'],
                url=row['url'],
                starting_proficiency_options=row['starting_proficiency_options'],
                ability_bonus_options=row['ability_bonus_options'],
                language_options=row['language_options']
            )
            db.session.add(race)
        db.session.commit()