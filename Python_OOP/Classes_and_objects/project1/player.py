class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        try:
            skill = next(filter(lambda p: p == skill_name, self.skills))

        except StopIteration:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

        if skill not in self.skills:

            return "Skill already added"

    def player_info(self):
        info = [f'Name: {self.name}', f'Guild: {self.guild}', f'HP: {self.hp}', f'MP: {self.mp}']

        for skill, mana in self.skills.items():
            info.append(f'==={skill} - {mana}')

        return '\n'.join(info)



