start = '''
It's 7:15 in the morning, and you missed all your alarms.
It's Wednesday, and you need to be at Girls Who Code by 9:00. You scramble
to get ready and arrive to the program on time. You live in Brooklyn, so you
have a few options of getting there. It's up to you to choose the most reliable
and quickest path.'''

print(start)

def runningLate():


    print("Type 'train' to go on the train or 'run' to run.")
    user_input = input()
    if user_input == "train":
        print("You decide to ride the train, but one of the passengers has a heart attack. There's a train delay that could make you very late.Type 'get off the train' to leave the train or 'stay' to remain in it?")
        user_input = input()
        if user_input =="get off the train":
            print("You transferred to another train and arrived to Girls Who Code on time!")
        if user_input == "stay":
            print("You took a good nap while sitting in the train, but ended up being 30 minutes late!")

    elif user_input == "run":
            print("You decide to run to Girls Who Code, but there is a major construction site in your usual route. There is no way around it. Type 'bridge' to run across the bridge and 'bus' to catch a bus.") # finished the story writing what happens
            user_input = input()
    while True:
        
    # finished the story by writing what happens


runningLate()
