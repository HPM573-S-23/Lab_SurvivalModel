from enum import Enum
import numpy as np


class HealthStat(Enum):
    """ health status of patients  """
    ALIVE = 1
    DEAD = 0


class Patient:
    def __init__(self, id, mortality_prob):
        """ initiates a patient
        :param id: ID of the patient
        :param mortality_prob: probability of death during a time-step (must be in [0,1])
        """
        self.id = id
        self.mortalityProb = mortality_prob
        self.healthState = HealthStat.ALIVE  # assuming all patients are alive at the beginning
        self.survivalTime = None   # won't be observed unless the patient dies

    def simulate(self, n_time_steps):
        """ simulate the patient over the specified simulation length """

        # random number generator
        rng = np.random.RandomState(seed=self.id)

        t = 0  # simulation current time

        # while the patient is alive and simulation length is not yet reached
        while self.healthState == HealthStat.ALIVE and t < n_time_steps:
            # determine if the patient will die during this time-step
            if rng.random_sample() < self.mortalityProb:
                # update the health state to death
                self.healthState = HealthStat.DEAD
                # record the survival time (assuming deaths occurs at the end of this period)
                self.survivalTime = t + 1

            # increment time
            t += 1


class Cohort:
    def __init__(self, id, pop_size, mortality_prob):
        """ create a cohort of patients
        :param id: cohort ID
        :param pop_size: population size of this cohort
        :param mortality_prob: probability of death for each patient in this cohort over a time-step (must be in [0,1])
        """

        self.id = id
        self.initialPopSize = pop_size  # initial population size
        self.mortalityProb = mortality_prob
        self.patients = []      # list of patients
        self.survivalTimes = []  # list to store survival time of each patient
        self.meanSurvivalTime = None  # mean survival time

    def simulate(self, n_time_steps):
        """ simulate the cohort of patients over the specified number of time-steps
        :param n_time_steps: number of time steps to simulate the cohort
        """

        # populate the cohort
        for i in range(self.initialPopSize):
            # create a new patient (use id * pop_size + n as patient id)
            patient = Patient(id=self.id * self.initialPopSize + i, mortality_prob=self.mortalityProb)
            # add the patient to the cohort
            self.patients.append(patient)

        # simulate all patients
        for patient in self.patients:
            # simulate
            patient.simulate(n_time_steps)
            # record survival time
            if not (patient.survivalTime is None):
                self.survivalTimes.append(patient.survivalTime)

        # calculate mean survival time
        self.meanSurvivalTime = sum(self.survivalTimes)/len(self.survivalTimes)
