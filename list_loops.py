songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs)

# Q2
# prints first element of song list
print(songs[0])
# prints last element of song list
print(songs[2])
# prints second and third element of song list
print(songs[1:3])

# Q3
# updates third song in the list from "For The Night" to "Nightlight", then prints results
songs[2] = "Nightlight"
print(songs)

# Q4
# adds a list of three songs to the end of the songs list
songs.extend(["Popular Monster", "Cosmica", "Jungle Whistle"])
print(songs)

# deletes the 5th song from the list
songs.pop(4)
print(songs)

# Q6
# Create list of animals
animals = ["Elephant", "Zebra", "Parrot"]

# Adds an animal to the list
animals.append("Lion")

# prints the 3rd animal in the list
print(animals[2])

# deletes the first animal in the list
del animals[0]

# prints out all animals in the list
for animal in animals:
    print(animal)