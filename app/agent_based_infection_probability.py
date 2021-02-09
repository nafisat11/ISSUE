import math
import json
# import pysal as ps
# import esda
# from pysal.lib import weights

# TODO: better structure for this
# FIXME: need to switch input to all the seat locations otherwise it can't compute the ones where the selected agent is diagonal


class AttackRates:
    def __init__(self, agents):
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
                return agent

    def probabilities(self):
        seat = self.find_infected(self.agents)
    

        for i, agent in enumerate(self.agents):
            # distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
            dist = math.sqrt(((seat['y'] - agent['y'])**2) +
                             ((seat['x'] - agent['x'])**2))
            if dist <= 2:

                agent['attRate'] = (0.1335*(dist**6)) - (1.9309*(dist**5)) + (11.291*(dist**4)) - (34.12*(dist**3)) + (56.193*(dist**2)) - (48.069*dist) + 17.104

             # attack rate for infected seat set to 1
            if (agent == seat):
                agent['attRate'] = 100

        output = []
        w_list = []
        att_list = []
        for i, agent in enumerate(self.agents):
            innerlist = []
            w_coord = []
            innerlist.append(agent['x'])
            w_coord.append(agent['x'])
            innerlist.append(agent['y'])
            w_coord.append(agent['y'])
            w_list.append(w_coord)
            innerlist.append(agent['attRate']/100)
            att_list.append(agent['attRate'])
            output.append(innerlist)

        # TODO: implementation to calculate weights without using pysal
        # w = ps.lib.weights.DistanceBand.from_array(w_list, 2, binary=False)
        # w = weights.DistanceBand.from_array(w_list, 2, binary=False)
        # w.transformation = 'r'

        # TODO: implementation to calculate moran's I without pysal
        # lisa = esda.moran.Moran_Local(att_list, w)
        # i_vals = lisa.Is
        # p_vals = lisa.p_sim
        # z_vals = lisa.z_sim

        # print_agent_info(normal_agents)
        # print_agent_info(infected_agents)
        # print(i_vals)
        return output
