# modifiedGA (mGA)
Modified version of a genetic algorithm developed for optimization problems with correlated variables.
___

This module includes the possibility of variation in genes into the genetic algorithm and performs numerical optimization on the relevant function within the given parameter range.

It can optimize for more than one parameter (even if there is a correlation between them - in this case it is recommended to keep the number of generations value high).

<br>

```python
mGA = modifiedGA( PopSize, nGen, nParam, mins, maxs, function, OptimType, overstep, info )
```

<br>

## Setting the optimization object

**Required parameters:**
  * `PopSize`   : Population size (must be at least 10)
  * `nGen`      : Number of generations
  * `nParam`    : Number of parameters
  * `mins`      : Minimum values in the scanning region of the parameters
  * `maxs`      : Maximum values in the scanning region of the parameters
  * `function`  : Function whose value is to be optimized
  
  > Warning!
  > In mins and maxs there should be as many values as nParams.

<br>

**Non-required parameters:**
  * `seed` (integer) : Sets the initial value of the random number generator as a function of the given number. Using the same seed will always give the same result.
  * `OptimType`      : Optimization type - 'minimum' or 'maximum' (Defaul value is 'minimum')
    * 'minimum', optimizes to the minimum value of the function.
    * 'maximum', optimizes to the maximum value of the function.
  * `info` (bool)    : Enable or disable showing information during calculation (Default value is True).

<br>

## Optimizing and getting results

```python
results, values = mGA.optimize()
```

It gives the most optimal result and the parameters of this result as return value.

## Saving the results

```python
mGA.saveResults( name, graph, xlabel, ylabel, title )
```

<br>

Non-required parameters:
  * `name`      : The name of the file/graph to which the results will be written (default value is "results")
  * `graph`     : Specifies whether to create a plot (default value is False)
  * `xlabel`    : The label of the x-axis of the graph (default value is "Generations")
  * `ylabel`    : The label of the y-axis of the graph (default value is "Fitness")
  * `title`    : Tittle of the graph (default is empty)

---
