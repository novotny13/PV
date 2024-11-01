wanted = 14513
bag = 100
grows = bag * 0.8
dies = grows *0.08
survives = grows - dies
bag_count =0

grew = 0

while grew < wanted:
    grew = grew + survives
    bag_count = bag_count + 1

print(bag_count)
