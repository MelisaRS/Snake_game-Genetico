from Run_Game import *
from Snake_Game import *
from random import choice, randint
#from helper import plot

####FITNESS###

#evaluacion de la poblacion
def cal_pop_fitness(pop):
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    score = 0
    # calculating the fitness value by playing a game with the given weights in chromosome
    fitness = []
    for i in range(pop.shape[0]):
        fit = run_game_with_ML(display,clock,pop[i])
        #score = collision_with_apple(score)
        print('fitness value of chromosome '+ str(i) +' :  ', fit , end ="          ")
        #Figura
        #plot_scores.append(fit)
        #total_score = fit
        #mean_score = total_score / i
        #plot_mean_scores.append(mean_score)
        #print('score act = ')
        #print(str(score))
        fitness.append(fit)

    
    #plot_scores.append(fit)
    #total_score += i
    #mean_score = total_score / fit
    #plot_mean_scores.append(mean_score)
    #plot(plot_scores, plot_mean_scores)

    return np.array(fitness)
    

#Seleccion
def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999
       
    return parents

#Crossover
def crossover(parents, offspring_size):
    # creating children for next generation 
    offspring = np.empty(offspring_size)
    
    for k in range(offspring_size[0]): 
  
        while True:
            parent1_idx = random.randint(0, parents.shape[0] - 1)
            parent2_idx = random.randint(0, parents.shape[0] - 1)
            # produce offspring from two parents if they are different
            if parent1_idx != parent2_idx:
                for j in range(offspring_size[1]):
                    if random.uniform(0, 1) < 0.5:
                        offspring[k, j] = parents[parent1_idx, j]
                    else:
                        offspring[k, j] = parents[parent2_idx, j]
                break
    return offspring

#Mutacion
def mutation(offspring_crossover):
    # mutating the offsprings generated from crossover to maintain variation in the population
    
    for idx in range(offspring_crossover.shape[0]):
        for _ in range(25):
            i = randint(0,offspring_crossover.shape[1]-1)

        #random_value = np.random.choice(np.arange(-1,1,step=0.001),size=(1),replace=False)
        random_value = np.random.choice(np.arange(-1,1,step=0.1),size=(1),replace=False)
        offspring_crossover[idx, i] = offspring_crossover[idx, i] + random_value

    return offspring_crossover

#def graf():
    #if done:
            # train long memory, plot result
     #       game.reset()
       #     agent.n_games += 1
      #      agent.train_long_memory()

        #    if score > record:
         #       record = score
          #      agent.model.save()

           # print('Game', agent.n_games, 'Score', score, 'Record:', record)

            #plot_scores.append(score)
           # total_score += score
            #mean_score = total_score / agent.n_games
           # plot_mean_scores.append(mean_score)
            #plot(plot_scores, plot_mean_scores)