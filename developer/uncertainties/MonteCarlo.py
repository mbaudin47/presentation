from openturns import *
s = 2.0
dist = Normal()
event = Event(RandomVector(NumericalMathFunction("x", "x"), RandomVector(Distribution(dist))), ComparisonOperator(Greater()), s)
algo = MonteCarlo(event)
algo.setMaximumCoefficientOfVariation(0.001)
algo.setConvergenceStrategy(HistoryStrategy(Full()))
algo.setMaximumOuterSampling(10000)
algo.setBlockSize(1)
algo.run()
graph = algo.drawProbabilityConvergence()
bb = graph.getBoundingBox()
val = dist.computeCDF(s, True)
data = NumericalSample(0, 2)
data.add(NumericalPoint([bb[0], val]))
data.add(NumericalPoint([bb[1], val]))
limit = Curve(data)
limit.setLegendName("Theoretical limit")
limit.setColor("blue")
limit.setLineStyle("dashed")
graph.addDrawable(limit)
graph.draw("MonteCarloConvergence")