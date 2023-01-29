from operator import itemgetter
import random

#Heard on Street problem 4.23 simulation
##Your  name  is Mr.  10.   You  are  standing  in a  field withtwo  opponents:
# Mr.  30  and  Mr.  60.   Each  of  you  has  a  gun  and  plenty  ofammunition.
# Each of you is in clear sight of the others and well within firingrange.  The goal is to maximize the probability of survival.
# Unfortunately, youare not a very good shot.
# If you take a shot at one of your opponents, youhave only a 10% chance of killing him.
# Mr. 30 is a better shot; he has a 30%chance of killing whomever he shoots at.
# Mr. 60 is even better; he has a 60%chance of killing his target.
# You take turns shooting in a pre-arranged order:first you,  then Mr. 30,  then Mr. 60,  and then through this cycle again and
# again until only one person remains.You get to shoot first.
# At whom, if anyone, do you shoot?

STRATEGIES=["Strongest","Weakest","Random","Weighted_Random"]
SHOOTER_STRATEGIES = []
#tuple of Name,HitProbability,Strategy
#shooter1 weakest
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Weakest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Strongest")])
#shooter1 strongest
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Strongest"),("Mr30",0.3,"Random"),("Mr60",0.6,"Strongest")])
#shooter1 random
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Weakest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Strongest"),("Mr60",0.6,"Strongest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Random"),("Mr60",0.6,"Weakest")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Random"),("Mr60",0.6,"Random")])
SHOOTER_STRATEGIES.append([("Mr10",0.1,"Random"),("Mr30",0.3,"Random"),("Mr60",0.6,"Strongest")])


#given a list of survivors pick the one with highest hit probabilitye
def get_max_probability_shooter(other_survivors):
    return max(other_survivors, key=itemgetter(1))

def get_min_probability_shooter(other_survivors):
    return min(other_survivors, key=itemgetter(1))

def get_random_shooter(other_survivors):
    index = random.randint(0,len(other_survivors)-1)
    return other_survivors[index]


def find_target(theshooter, survivors):
    other_survivors=list(survivors)
    other_survivors.remove(theshooter)##Remove self , since we dont want to shoot ourself :)
    target = None
    strategy=theshooter[2]##The strategy of this shooter
    if strategy=="Strongest":
        target = get_max_probability_shooter(other_survivors)
    if strategy=="Weakest":
        target =get_min_probability_shooter(other_survivors)
    if strategy=="Random":
        target =get_random_shooter(other_survivors)
    return target


def simulate_shooting(SHOOTERS):
    # weakest first sequence i.e. Mr10,Mr30,Mr60
    shoot_sequence = []
    for index, shooter in enumerate(SHOOTERS):
        shoot_sequence.append(shooter[0])

    # i.e. 3
    shooter_count = len(SHOOTERS)
    survivors = SHOOTERS.copy()

    #first shoot is at index 0 and is incremented by one
    shoot_index_counter=0
    shoot_round_counter=1

    #Start the simulation
    #Keep shootings till 1 shooter surivive only
    def is_alive(survivors, shooter):
        for survivor in survivors:
            if survivor[0]==shooter[0]:
                return True
        return False

    #print("Starting shooting simulation get ready !")
    while(len(survivors)>1):
        turn_index = shoot_index_counter % shooter_count
        shooter = SHOOTERS[turn_index]

        ##check if the shooter still alive
        if not is_alive(survivors,shooter):
            ##since shooter is dead , skip this iteration
            shoot_index_counter=shoot_index_counter+1
            continue

        target=find_target(shooter,survivors)

        #we find the target,lets make a shot to knock him/her !
        probability_to_hit=shooter[1]
        rnd = random.uniform(0, 1)
        #lets see if hits
        hit_outcome="MISSED!"
        if probability_to_hit>=rnd:
            #HIT !!! remove target from survivors
            hit_outcome="HIT!"
            survivors.remove(target)


        #print("Round:"+str(shoot_round_counter)+" "+str(shooter[0])+" tried to hit "+str(target[0])+" "+hit_outcome+" Survivors:"+str(list(zip(*survivors))[0]))

        shoot_index_counter=shoot_index_counter+1
        shoot_round_counter = shoot_round_counter + 1
    #We have our survivor
    #print("Winner is: "+survivors[0][0])
    return survivors[0][0]




#For each different combination of shooter strategies
for shooter_strategies in SHOOTER_STRATEGIES:

    # Make a simulation of like 100K runs
    SIMULATION_LIMIT = 100000
    simulation_index = 0
    win_counts = {}
    for shooter in shooter_strategies:
        win_counts[shooter[0]] = 0

    while simulation_index<SIMULATION_LIMIT:
        #print("simulation index"+str(simulation_index))
        winner = simulate_shooting(shooter_strategies)
        win_counts[winner]+=1
        simulation_index+=1
    ##Standings after 100K runs
    print("Strategies:" + str(shooter_strategies)+" "+str(win_counts))


