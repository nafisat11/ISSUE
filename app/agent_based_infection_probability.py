import math
import json


class AttackRates:
    def __init__(self, agents, mask_type=None, duration=None):
        self.infected = []
        self.mask_type = mask_type
        self.duration = int(duration)
        self.available_masks = {"N95": 0.896,
                                "Surgical": 0.333, "Cloth": 0.113}
        # All the selected agents' seat locations
        self.agents = json.loads(agents)
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
        for i, agent in enumerate(self.agents):
            sum_of_attackrates = 0
            new_attackrates = 0
            if agent['state'] == 2:
                # attack rate for infected seat set to 1
                agent['attRate'] = 1
                continue

            for infected in self.infected:
                # Distance formula
                dist = math.sqrt((((infected['y'] - agent['y'])/agent['y_scale'])**2) +
                                 (((infected['x'] - agent['x'])/agent['x_scale'])**2))

                if dist <= 3.3:
                    new_attackrates = ((0.1335*(dist**6)) - (1.9309*(dist**5)) + (11.291*(
                        dist**4)) - (34.12*(dist**3)) + (56.193*(dist**2)) - (48.069*dist) + 17.104)/100

                    sum_of_attackrates = sum_of_attackrates + \
                        new_attackrates - (sum_of_attackrates*new_attackrates)

                elif dist > 3.3 and dist <= 6:
                    sum_of_attackrates += 0.0005
                else:
                    sum_of_attackrates += 0

            agent['attRate'] = sum_of_attackrates
            if self.mask_type in self.available_masks:
                agent['attRate'] *= (1-self.available_masks[self.mask_type])

            if self.duration is None or self.duration == 0:
                agent['attRate'] *= 1
            else:
                temporal = (0.121 + 0.022*((self.duration/60)**2))/100 + 1
                agent['attRate'] *= temporal

        output = []

        for i, agent in enumerate(self.agents):
            innerlist = []
            innerlist.append(agent['x'])
            innerlist.append(agent['y'])
            innerlist.append(agent['attRate'])
            output.append(innerlist)

        return output
