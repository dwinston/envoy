# envoy

> envoy | ˈenˌvoi, ˈänˌvoi |
> <br>noun<br>1. a messenger or representative, especially one on a diplomatic mission.

Envoy helps researchers communicate *objectives* with respect to computed properties of database entries. For example,
the [Materials Project (MP)](https://materialsproject.org) maintains a database of materials. A researcher might submit an
objective to discover materials with a band gap greater than *x*. Envoy, running as a service, subscribes this
researcher to notifications about new materials added to the database that satisfy their objectives. In addition, the
researcher can choose to be notified when new materials are *predicted* to meet one of their objectives. This can
be the case if e.g. a high-quality electronic band structure calculation (yielding a band gap value) has not been
computed for an existing material, but an automated machine learning (ML) procedure determines -- based on its most recent
re-evaluation due to new training data -- that a given material is now predicted to satisfy a given objective. Under
the hood, Envoy uses the [tree-based pipeline optimization tool (TPOT)](https://epistasislab.github.io/tpot/) for
automated machine learning.

All user objectives collected by Envoy are annotated with their dependent computational workflows, some of which may
not be automatically run for all entries. Using the above example, MP does not run electronic band structure
calculations automatically for all materials -- computational budgets are limited, and it's not clear that any
researchers will want an *ab initio* calculation run for a given material. Thus, Envoy allows MP to invest
computational resources in a way that maximally caters to the needs of researchers in a way that does not require these
researchers to know the details of underlying workflow dependencies. One can think of Envoy as maintaining an "index
fund" of research efforts, tracking a variety of "stocks" in proportion to the number of shares held in
each. Envoy uses already-computed property data along with ML predictions to prioritize workflows in accordance with user objectives.
