# modifiedGA (mGA) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/acanbay/modifiedGA/HEAD?labpath=examples.ipynb)

This Python module comprises a modified Genetic Algorithm where a new intermediate step, gene variation, is introduced, and a mutation defined by a Gaussian distribution with a standard deviation that adjusts based on the results of each generation. It is capable of optimizing multiple parameters (even in cases of correlation between them - in such instances, it is advisable to maintain a high number of generations).

<br>

Mathematical background and performance test: [click here](https://github.com/acanbay/modifiedGA/blob/main/modifiedGA.pdf)

<br>

**Installation:**

Download the [latest release](https://github.com/acanbay/modifiedGA/releases) and extract it. Enter the extracted file and run the following command via console:
```console
python setup.py install
```

<br>

### Setting the optimization object

```python
mGA = modifiedGA.algorithm( popSize, nGen, nVar, mins, maxs, problem, optimType, info )
```
<br>

**Required parameters:**
  * `popSize`   : Population size (must be at least 10)
  * `nGen`      : Number of generations
  * `nVar`      : Number of variables
  * `mins`      : Minimum value in the parameter space of possible values for the variables
  * `maxs`      : Maximum value in the parameter space of possible values for the variables
  * `problem`   : The function to be used in optimization

<br>
  
  > [!IMPORTANT]
  > * The values of `mins` and `maxs` should consist of as many as `nVar` value.
  > * The `problem` should take list of variables as parameters and return the result of the function.

<br>

**Non-required parameters:**
  * `seed` (integer) : Sets the initial value of the random number generator as a function of the given number. Using the same seed will always yield the same result.
  * `optimType`      : Optimization type - 'minimum' or 'maximum' (defaul value is 'minimum')
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

<br>
  
  > [!IMPORTANT]
  > The [matplotlib](https://github.com/matplotlib/matplotlib) module must be installed to plot graphs

<br>

---
