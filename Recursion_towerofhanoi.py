def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)
        
def move_disk(fp,tp):
    print("moving from ",fp, " to ", tp)
        
move_tower(3, "A","B","C")
