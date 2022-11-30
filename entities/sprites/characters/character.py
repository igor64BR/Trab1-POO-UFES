class Character:
    def basic_attack(self):
        raise NotImplementedError(f"'basic_attack' method not implemented on character")

    def ability(self):
        raise NotImplementedError(f"'ability' method not implemented on character")

    def mutate_character(self):
        pass