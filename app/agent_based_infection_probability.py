import math
import json
# import pysal as ps
# import esda
# from pysal.lib import weights

# TODO: better structure for this
# FIXME: need to switch input to all the seat locations otherwise it can't compute the ones where the selected agent is diagonal


class AttackRates:
    def __init__(self, agents, mask_type=None, duration=None):
        self.infected = []
        self.mask_type = mask_type
        self.duration = int(duration)
        self.available_masks = {"N95": 0.85, "Surgical": 0.33, "Cloth": 0.11}
        self.agents = json.loads(agents)  # All the selected agents' seat locations
        self.normal_agents = [
            agent for agent in self.agents if agent['state'] == 1]
        self.infected_agents = [
            agent for agent in self.agents if agent['state'] == 2]

    def print_agent_info(self):
        agents = self.agents
        for i, agent in enumerate(agents):
            print("\n{} AGENT {}\n".format('NORMAL' if agent['state'] ==
                                           1 else 'INFECTED', i + 1))
            for attribute, val in agent.items():
                print("\t{}:\t{}".format(attribute, val))

    def find_infected(self, all_agents):
        for i, agent in enumerate(all_agents):
            if agent['state'] == 2:
                self.infected.append(agent)
        return

    def probabilities(self):
        self.find_infected(self.agents)
        # seat = self.find_infected(self.agents)
        for i, agent in enumerate(self.agents):
            sum_of_attackrates = 0
            if agent['state'] == 2:
                # attack rate for infected seat set to 1
                agent['attRate'] = 100
                continue

            for infected in self.infected:
                # Distance formula 
                dist = math.sqrt(((infected['y'] - agent['y'])**2) +
                                 ((infected['x'] - agent['x'])**2))
                if dist <= 2:
                    sum_of_attackrates += (0.1335*(dist**6)) - (1.9309*(dist**5)) + (11.291*(
                        dist**4)) - (34.12*(dist**3)) + (56.193*(dist**2)) - (48.069*dist) + 17.104

            agent['attRate'] = sum_of_attackrates
            if self.mask_type in self.available_masks:
                print(self.mask_type)
                agent['attRate'] *= (1-self.available_masks[self.mask_type])

            if self.duration is not None or self.duration != 0:
                temporal = (0.121 + 0.022*((self.duration/60)**2))/100 + 1
                agent['attRate'] *= temporal

        temp_output = [[0.0, 1.000]]
        output = []
        w_list = []
        att_list = []

        for i in range(0, self.duration, 5):
            temp_output.append(
                [float(i), round(((0.121 + 0.022*((i/60)**2))/100 + 1), 3)])

        for i, agent in enumerate(self.agents):
            innerlist = []
            w_coord = []
            innerlist.append(agent['x'])
            w_coord.append(agent['x'])
            innerlist.append(agent['y'])
            w_coord.append(agent['y'])
            w_list.append(w_coord)
            # did this cause heatmap values don't work unless you divide by 100
            innerlist.append(agent['attRate']/100)
            att_list.append(agent['attRate'])
            output.append(innerlist)

        return output, temp_output
