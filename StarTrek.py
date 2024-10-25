import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}") 
			break
		else: 
			print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
## : Implement function to display ship status, resources, and crew 
	tf = False
	while tf==False:
		tempval= int(input("would you like to display: 1. systems 2. resources 3. crew 4. no "))
		if (tempval==1):
			print(ship["systems"])
		elif tempval==2:
			print(ship["resources"])
		elif tempval==3:
			print(ship["crew"])
		else:
			print("returning to game")
			break

def get_user_action(): 
	# : Implement function to get and return user's chosen action 
	print("")
	UAction= int(input("please enter your input "))
	return UAction
def run_mission(score): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	if(mission_type=="Exploration"):
		use_resource("energy",random.randint(1,75))
		score+=5 
		return score
	elif(mission_type=="Diplomacy"):
		




	# : Implement mission logic for different mission types 
	# Return the score earned from the mission 
	#"Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"

def repair_system(): 
	ship["systems"]=100
# T: Implement system repair functionality
 
def add_crew_member(): 
# TO: Implement functionality to add a new crew member 
	CrewN=input("please input in the crew name")
	CrewR=input("please input the crew role")
	ship["crew"][CrewN]=CrewR

def handle_random_event():
# TO: Implement random events that can occur during the simulation 
	print("")
def use_resource(resource, amount): 
# ODO: Implement resource usage logic 
	if(resource=="energy"):
		ship["resource"]["energy"]-=amount
		if ship["resource"]["energy"]<0:
			print("you do not have enough resource for this")
			ship["resource"]["energy"]+=amount
	elif(resource=="torpedoes"):
		ship["resource"]["torpedoes"]-=amount
		if ship["resource"]["torpedoes"]<0:
			print("you do not have enough resource")
			ship["resource"]["torpedoes"]+=amount

def replenish_resources(): 
# ODO: Implement resource replenishment logic 
	ship["resource"]["energy"]+= random.randint(1,200)
	if ship["resource"]["energy"]>1000:
		ship["resource"]["energy"]=1000
	ship["resource"]["torpedoes"]+=random.randint(1,3)
	if ship["resource"]["torpedoes"]>10:
		ship["resource"]["torpedoes"]=10




main()
