import math
import json
# import pysal as ps
# import esda
# from pysal.lib import weights

# TODO: better structure for this


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

    def find_front(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (agent['x'] ==
                                                   (infected['x'] - 0.4))):
                return agent

    def find_behind(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (int(agent['x']) ==
                                                   (int(infected['x'] + 0.4)))):
                return agent

    def find_front2ndRow(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (agent['x'] ==
                                                   (infected['x'] - 0.8))):
                return agent

    def find_behind2ndRow(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (agent['x'] ==
                                                   (infected['x'] + 0.8))):
                return agent

    def find_front3rdRow(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (agent['x'] ==
                                                   (infected['x'] - 1.2))):
                return agent

    def find_behind3rdRow(self, all_agents, infected):
        for i, agent in enumerate(all_agents):
            if ((agent['y'] == infected['y']) and (agent['x'] ==
                                                   (infected['x'] + 1.2))):
                return agent

    def find_infected(self, all_agents):
        for i, agent in enumerate(all_agents):
            if agent['state'] == 2:
                return agent

    def probabilities(self):
        seat = self.find_infected(self.agents)
        ref_front = self.find_front(self.agents, seat)
        ref_behind = self.find_behind(self.agents, seat)
        ref_front2 = self.find_front2ndRow(self.agents, seat)
        ref_behind2 = self.find_behind2ndRow(self.agents, seat)
        ref_front3 = self.find_front3rdRow(self.agents, seat)
        ref_behind3 = self.find_behind3rdRow(self.agents, seat)

        for i, agent in enumerate(self.agents):
            # distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
            dist = math.sqrt(((seat['y'] - agent['y'])**2) +
                             ((seat['x'] - agent['x'])**2))
            if dist <= 2:

                # attack rate for same row (same y-coordinate)
                if (agent['x'] == seat['x']):
                    agent['attRate'] = (1.175*(dist**2)) - \
                        (5.0621*dist) + 5.6922

                # attack rate for one row above (y-coord. - 0.4)
                if (agent['x'] == (seat['x'] - 0.4)):

                    # attack rate for seat in front of infected seat
                    if (agent == ref_front):
                        agent['attRate'] = 0.3043

                    # attack rate for seats NOT immediately above infected
                    # calculated based on ref seat
                    if (agent['y'] != seat['y']):
                        dist = math.sqrt(((agent['y'] - ref_front['y'])**2) +
                                         ((agent['x'] - ref_front['x'])**2))
                        agent['attRate'] = (0.025*(dist**2)) - \
                            (0.1658*dist) + 0.3043

                # attack rate for one row below (y-coord. + 0.4)
                if (agent['x'] == (round(seat['y'] + 0.4, 2))):

                    # attack rate for seat behind infected seat
                    if (agent == ref_behind):
                        agent['attRate'] = 0.3043

                    # attack rate for seats NOT immediately below infected
                    # calculated based on ref seat
                    if (agent['y'] != seat['y']):
                        dist = math.sqrt(((agent['y'] - ref_behind['y'])**2) +
                                         ((agent['x'] - ref_behind['x'])**2))
                        agent['attRate'] = (0.025*(dist**2)) - \
                            (0.1658*dist) + 0.3043

                # attack rate for two rows above (y-coord. - 0.8)
                if (agent['x'] == (seat['x'] - 0.8)):

                    # attack rate for seat in front of infected seat
                    if (agent == ref_front2):
                        agent['attRate'] = 0.0919

                    # attack rate for seats NOT above infected
                    # calculated based on ref seat
                    if (agent['y'] != seat['y']):
                        dist = math.sqrt(((agent['y'] - ref_front2['y'])**2) +
                                         ((agent['x'] - ref_front2['x'])**2))
                        agent['attRate'] = (-0.0813*(dist**2)) + \
                            (0.2083*dist) + 0.0919

                # attack rate for two rows below (y-coord. + 0.8)
                if (agent['x'] == (seat['x'] + 0.8)):

                    # attack rate for seat behind infected seat
                    if (agent == ref_behind2):
                        agent['attRate'] = 0.0919

                    # attack rate for seats NOT below infected
                    # calculated based on ref seat
                    if (agent['y'] != seat['y']):
                        dist = math.sqrt(((agent['y'] - ref_behind2['y'])**2) +
                                         ((agent['x'] - ref_behind2['x'])**2))
                        agent['attRate'] = (-0.0813*(dist**2)) + \
                            (0.2083*dist) + 0.0919

                # attack rate for three rows above (y-coord. - 1.2)
                if (agent['x'] == (seat['x'] - 1.2)):

                    # attack rate for seat in front of infected seat
                    if (agent == ref_front3):
                        agent['attRate'] = 0.0099

                    # attack rate for seats NOT immediately above infected
                    # calculated based on ref seat
                    if (agent['x'] != seat['x']):
                        dist = math.sqrt(((agent['x'] - ref_front3['x'])**2) +
                                         ((agent['y'] - ref_front3['y'])**2))
                        agent['attRate'] = (-0.05*(dist**2)) + \
                            (0.1678*dist) + 0.0099

                # attack rate for three row below (y-coord. + 1.2)
                if (agent['x'] == (seat['x'] + 1.2)):

                    # attack rate for seat behind infected seat
                    if (agent == ref_behind3):
                        agent['attRate'] = 0.0099

                    # attack rate for seats NOT below infected
                    # calculated based on ref seat
                    if (agent['y'] != seat['y']):
                        dist = math.sqrt(((agent['y'] - ref_behind3['y'])**2) +
                                         ((agent['x'] - ref_behind3['x'])**2))
                        agent['attRate'] = (-0.05*(dist**2)) + \
                            (0.1678*dist) + 0.0099

                # attack rate for infected seat set to 1
                if (agent == seat):
                    agent['attRate'] = 1

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
            innerlist.append(agent['attRate'])
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
