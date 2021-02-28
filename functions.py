from random import uniform
from copy import copy

# Entity class to represent entities
class Entity:
    def __init__(self, number, arrival_time, interarrival_time, service_time):
        self.number = number
        self.arrival_time = arrival_time
        self.interarrival_time = interarrival_time
        self.service_time = service_time
        self.service_start = None


# Creates matrix to be shown in the UI?
# In this format:
# Just Finished Event			Variables		Atrributes (Arrival Times)		Statistical Accumulator									
# Part No.	Time(t)	Event Type	Q(t)	B(t)	In Queue	In Service	P	N	 ΣWQ	WQ*	 ΣTS	TS*	sq	sq*	sb
#   -       -	        init	0	    0	    []	            []	    0	0	  0	    0	  0	    0	0	0	0
#   1	    0	        arr	    0	    1	    []	            [0]	    0	1	  0	    0	  0	    0	0	0	0
#   2	    1.73	    arr	    1	    1	    [1.73]	        [0]	    0	1	  0	    0	  0	    0	0	1	1.73
# ...
#   -	    20	        end	    1	    1	    [19.39]	      [18.69]	5	6	15.17   8.16 32.2 12.62	15.78 3	18.34
# IN PROGRESS
# Statistical Accumulators are still missing
def create_matrix(entities, sim_period):
    matrix =[["-","-","init","0","0","[]","[]","0","0","0","0","0","0","0","0","0"]]
    in_queue = []
    in_service = None

    current_time = 0.00
    while current_time < sim_period:
        temp = ["-","-","init","0","0","[]","[]","0","0","0","0","0","0","0","0","0"]
        #modify temp here to create a new row
        queued_entity = False
        current_entity = None
        if entities[0].arrival_time == current_time:
            in_queue.append(entities.pop(0)) 
            current_entity = in_queue[-1]
            queued_entity = True
            temp[2] = "arr"
        if in_service is None and in_queue:
            in_service = in_queue.pop(0)
            in_service.service_start = current_time
            current_entity = in_service
            if not queued_entity:
                current_time = round(current_time+0.01,2)
                continue
        elif in_service is not None and in_service.service_start + in_service.service_time == current_time:
            current_entity = in_service
            in_service = None
            temp[2] = "dep"
            if in_ queue:
                in_service = in_queue.pop(0)
                in_service.service_start = current_time
        elif not queued_entity:
            current_time = round(current_time+0.01,2)
            continue
        
        temp[0] = current_entity.number    
        temp[1] = current_time
        temp[3] = len(in_queue)
        temp[4] = "0" if in_service is None else "1"
        temp[5] = [entity.arrival_time for entity in in_queue]
        temp[6] = "[]" if in_service is None else "["+str(in_service.arrival_time)+"]"
        #append temp to matrix
        matrix.append(temp)
        current_time = round(current_time+0.01,2)

    end = copy(matrix[-1])
    end[0] = "-"
    end[1] = sim_period
    end[2] = "end"
    matrix.append(end)
    return matrix

# Generate a List of entities with their corresponding
# Arrival, interarrival, and service time (in minutes) then returns it.
# Times are generated in random from range min_time to max_time.
# e.g. Entity no.    Arrival Time    Interarrival time   Service time
#       1               0                   1.73            2.9     
#       2               1.73                1.35            1.76
#       3               3.08                0.71            3.39       
def generate_entities(min_time, max_time, sim_period):
    entities = [Entity(1,0,round(uniform(min_time,max_time),2),round(uniform(min_time,max_time),2))]

    current_arrival_time = 0
    i = 1
    while current_arrival_time < sim_period:
        current_arrival_time = round(entities[i-1].arrival_time+entities[i-1].interarrival_time,2)
        entities.append(Entity(i+1,current_arrival_time,round(uniform(min_time,max_time),2),round(uniform(min_time,max_time),2)))
        i += 1
        
    return entities


# TEST RUN FOR CHECKING 
min_time = 1
max_time = 10
sim_period = 20

entities = generate_entities(min_time,max_time,sim_period)
for entity in entities:
    print(entity.number,entity.arrival_time,entity.interarrival_time,entity.service_time,"\n")

matrix = create_matrix(entities, sim_period)
for row in matrix:
    for col in row:
        print(col, end = " ")
    print("\n")
