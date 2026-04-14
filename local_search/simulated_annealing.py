import random
import math

class SimulatedAnnealing():
    def __init__(self, problem, scheduler):
        self.problem = problem
        self.scheduler: Scheduler = scheduler

    def search(self):
        current = self.problem.initial_state
        T = self.scheduler.get_temperature()
        while T > 0.0001:  
            neighbors = self.problem.actions(current)
            if not neighbors:
                return current
            action = random.choice(neighbors)
            next_state = self.problem.result(current, action)
            # maximization problem: we want to maximize the evaluation function
            delta_e = self.problem.evaluate(next_state) - self.problem.evaluate(current)
            select_probability = min(1, math.exp(delta_e / T))
            print(f"Iteration {self.scheduler.t}, Temperature: {T:.4f}, Action: {action}, ΔE: {delta_e:.4f}, Select Probability: {select_probability:.4f}")
            if delta_e > 0 or random.random() < select_probability:
                current = next_state
            T = self.scheduler.step()
        return current

class Scheduler:
    def __init__(self, iterations, alpha, scheduler='linear') -> None:
        self.iterations = iterations
        self.t = 0
        self.alpha = alpha
        if scheduler == 'basic':
            self.scheduler = self.basic_scheduler
        else:
            raise ValueError('Unknown scheduler')

    def get_temperature(self):
        return self.scheduler()
    
    def reset_scheduler(self):
        self.t = 0

    def step(self):
        if self.t >= self.iterations:
            return 0
        temp = self.get_temperature()
        self.t += 1
        return temp
    
    def basic_scheduler(self):
        return 100 - self.t

