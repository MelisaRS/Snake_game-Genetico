from Genetic_Algorithm import *
from Snake_Game import *
from Run_Game import *
from helper import plot

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
sol_per_pop = 40
num_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

# Defining the population size.
pop_size = (sol_per_pop,num_weights)

#Creating the initial population.
#new_population = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)
new_population = np.random.choice(np.arange(-1,1,step=0.0001),size=pop_size,replace=True)
num_generations = 600

num_parents_mating = 20

plot_scores = []
plot_mean_scores = []
total_score = 0
max_score = 0
clock = 0
weights = 0
for generation in range(num_generations):
    print('##############        GENERATION ' + str(generation)+ '  ###############' )
    # Measuring the fitness of each chromosome in the population.
    fitness = cal_pop_fitness(new_population)
    #max_score_T = run_game_with_ML(max_score,clock,weights)
    print('\n #######  fittest chromosome in generation ' + str(generation) +' is having fitness value:  ', np.max(fitness))
    #print(f"MX SCORE: {max_score}")

    #Figura
    plot_scores.append(np.max(fitness))
    total_score = np.max(fitness)
    mean_score = total_score / generation
    plot_mean_scores.append(mean_score)

    print(total_score)
    print(np.max(fitness))
    print("grafico")
    
    plot(plot_scores, plot_mean_scores)

    # Selecting the best parents in the population for mating.
    parents = select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = mutation(offspring_crossover)

    ###NUEVA poblacion creada

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    

    
    
