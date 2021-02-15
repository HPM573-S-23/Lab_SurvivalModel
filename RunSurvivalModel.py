from SurvivalModelClasses import Cohort

MORTALITY_PROB = 0.1    # annual probability of death
TIME_STEPS = 40         # years

# create a cohort
myCohort = Cohort(id=1, pop_size=100, mortality_prob=MORTALITY_PROB)

# simulate the cohort over the specified time steps
myCohort.simulate(TIME_STEPS)

# print the patient survival time
print(myCohort.meanSurvivalTime)
