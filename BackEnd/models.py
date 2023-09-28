from extensions import db

class DndClass(db.Model):
    __tablename__ = 'dnd_class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hit_die = db.Column(db.Integer)
    proficiency_choices = db.Column(db.JSON)
    proficiencies = db.Column(db.JSON)
    saving_throws = db.Column(db.JSON)
    starting_equipment = db.Column(db.JSON)
    class_levels = db.Column(db.JSON)
    subclasses = db.Column(db.JSON)
    url = db.Column(db.String)

    def __str__(self):
        return self.name

class DndSpell(db.Model):
    __tablename__ = 'dnd_spell'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    classes = db.Column(db.JSON)
    level = db.Column(db.Integer)
    school = db.Column(db.String(255))
    cast_time = db.Column(db.String(255))
    spell_range = db.Column(db.String(255))
    duration = db.Column(db.String(255))
    verbal = db.Column(db.Boolean)
    somatic = db.Column(db.Boolean)
    material = db.Column(db.String(255))
    material_cost = db.Column(db.Text)
    description = db.Column(db.Text)

    def __str__(self):
        return self.name

class DnDEquipment(db.Model):
    __tablename__ = 'dnd_equipment' 
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255))
    equipment_category = db.Column(db.String(255))
    gear_category = db.Column(db.String(255))
    cost = db.Column(db.JSON)
    weight = db.Column(db.Numeric(10, 2))
    url = db.Column(db.String)
    item_desc = db.Column(db.Text)
    tool_category = db.Column(db.String(255))
    vehicle_category = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    weapon_category = db.Column(db.String(255))
    weapon_type = db.Column(db.String(255))
    category_range = db.Column(db.String(255))
    damage = db.Column(db.String(255))
    weapon_range = db.Column(db.String(255))
    properties = db.Column(db.JSON)
    two_hand_damage = db.Column(db.String(255))
    armor_category = db.Column(db.String(255))
    armor_class = db.Column(db.JSON)
    str_minimum = db.Column(db.Integer)
    stealth_disadvantage = db.Column(db.Boolean)
    contents = db.Column(db.JSON)
    speed = db.Column(db.JSON)
    capacity = db.Column(db.JSON)
    throw_range = db.Column(db.String(255))
    special = db.Column(db.JSON)

    def __str__(self):
        return self.name

class DnDMonster(db.Model):
    __tablename__ = 'dnd_monster'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    size = db.Column(db.String(20))
    type = db.Column(db.String(255))
    subtype = db.Column(db.String(255))
    alignment = db.Column(db.String(255))
    armor_class = db.Column(db.Integer)
    hit_points = db.Column(db.Integer)
    hit_dice = db.Column(db.String(20))
    speed = db.Column(db.JSON)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    proficiencies = db.Column(db.JSON)
    damage_vulnerabilities = db.Column(db.JSON)
    damage_resistances = db.Column(db.JSON)
    damage_immunities = db.Column(db.JSON)
    condition_immunities = db.Column(db.JSON)
    senses = db.Column(db.JSON)
    languages = db.Column(db.JSON)
    challenge_rating = db.Column(db.Numeric(5, 2))
    special_abilities = db.Column(db.JSON)
    actions = db.Column(db.JSON)
    legendary_actions = db.Column(db.JSON)
    url = db.Column(db.String)
    reactions = db.Column(db.JSON)
    other_speeds = db.Column(db.JSON)

    def __str__(self):
        return self.name

class DnDRace(db.Model):
    __tablename__ = 'dnd_race'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    speed = db.Column(db.Integer)
    ability_bonuses = db.Column(db.JSON)
    alignment = db.Column(db.Text)
    age = db.Column(db.Text)
    size = db.Column(db.String(20))
    size_description = db.Column(db.Text)
    starting_proficiencies = db.Column(db.JSON)
    languages = db.Column(db.JSON)
    language_desc = db.Column(db.Text)
    traits = db.Column(db.JSON)
    trait_options = db.Column(db.JSON)
    subraces = db.Column(db.JSON)
    url = db.Column(db.String)
    starting_proficiency_options = db.Column(db.JSON)
    ability_bonus_options = db.Column(db.JSON)
    language_options = db.Column(db.JSON)

    def __str__(self):
        return self.name
