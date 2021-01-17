# from settings import Settings
from ga_settings import GA_settings
from ga import GA
from ts_settings import TS_settings
from ts import TS
from sa_settings import SA_settings
from sa import SA

ga_settings = GA_settings()
ga = GA(ga_settings)
ga.main()
ts_settings = TS_settings()
ts = TS(ts_settings)
ts.main()
sa_settings = SA_settings()
sa = SA(sa_settings)
sa.main()