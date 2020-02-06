"""
Max-Min Hill Climbing Algorithm

References
----------
[1] Tsamardinos, et al. "The max-min hill-climbing Bayesian
network structure learning algorithm."

"""
from pyBN.learning.structure.hybrid import mmpc
from pyBN.learning.structure.score.hill_climbing import hc
from pyBN.learning.structure.score.tabu import tabu
from pyBN.learning.structure.score.random_restarts import hc_rr



def mmhc(data, alpha=0.05, metric='AIC', max_iter=100, method='hc'):
	"""
	Max-Min Hill Climbing Algorithm for
	learning a Bayesian Network structure
	from data.

	Arguments
	---------
	*data* : a numpy ndarray

	*alpha* : a float
		Probability of Type II Error for
		independence tests.

	*metric* : a string
		*metric* : a string
		Which score metric to use.
		Options:
			- 'AIC'
			- 'BIC'
			- 'LL' (log-likelihood)

	*method* : a string
		The type of hill-climbing algorithm to run
		OPTIONS:
			- 'hc' : normal hill-climbing
			- 'rr' : hill-climbing with random restarts
			- 'tabu' : tabu hill-climbing

	Returns
	-------
	*bn* : a BayesNet object

	"""

	# RUN HILL-CLIMBING WITH EDGE RESTRICTIONS
	if method == 'tabu':
		bn = tabu(data=data, metric=metric, max_iter=max_iter)
	elif method == 'rr':
		bn = hc_rr(data=data, metric=metric, max_iter=max_iter)
	else:
		bn = hc(data=data, metric=metric, max_iter=max_iter)

	return bn






















