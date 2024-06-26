# modifiedGA (mGA)
Modified version of a genetic algorithm developed for optimization problems with correlated variables.
___

This Python module comprises a modified Genetic Algorithm where a new intermediate step, gene variation, is introduced, and a mutation defined by a Gaussian distribution with a standard deviation that adjusts based on the results of each generation. It is capable of optimizing multiple parameters (even in cases of correlation between them - in such instances, it is advisable to maintain a high number of generations).

<br>

```python
mGA = modifiedGA( PopSize, nGen, nParam, mins, maxs, problem, OptimType, overstep, info )
```

<br>

### Setting the optimization object

**Required parameters:**
  * `PopSize`   : Population size (must be at least 10)
  * `nGen`      : Number of generations
  * `nParam`    : Number of parameters
  * `mins`      : Minimum value in the parameter space of possible values for the variables
  * `maxs`      : Maximum value in the parameter space of possible values for the variables
  * `problem`   : The problem to be used in optimization
  
  > Warning!
  > The values of mins and maxs should consist of as many as nParam value.

<br>

**Non-required parameters:**
  * `seed` (integer) : Sets the initial value of the random number generator as a function of the given number. Using the same seed will always yield the same result.
  * `OptimType`      : Optimization type - 'minimum' or 'maximum' (defaul value is 'minimum')
    * 'minimum', optimizes the problem to the minimum value.
    * 'maximum', optimizes the problem to the maximum value.
  * `info` (bool)    : Enable or disable showing information during calculation (default value is True).

<br>

### Optimizing and getting results

```python
results, values = mGA.optimize()
```

It returns the most optimal result and the parameters associated with this results.

<br>

### Saving the results

```python
mGA.saveResults( name, graph, xlabel, ylabel, title )
```

<br>

Non-required parameters:
  * `name`      : Name of the file/graph which the results will be written (default value is "results")
  * `graph`     : Specifies whether to create a plot (default value is False)
  * `xlabel`    : Label of the x-axis on the graph (default value is "Generations")
  * `ylabel`    : Label of the y-axis on the graph (default value is "Fitness")
  * `title`     : Title of the graph (default is empty)

---
