"""Simple model of money agent."""
from mesa import Agent, Model
from mesa.time import RandomActivation


class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        """Initialize agent.

        Args:
            unique_id: id
            model: money model
        """
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        """Perform step."""
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print("Hi, I am agent " + str(self.unique_id) + ".")


class MoneyModel(Model):
    """A model with some number of agents."""

    def __init__(self, n):
        """Initialize money model.

        Args:
            n: number of agents
        """
        self.num_agents = n
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
