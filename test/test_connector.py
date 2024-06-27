import decouple
from eqlink import JobsEqConnection

username = decouple.config("JOBSEQ_USERNAME")
password = decouple.config("JOBSEQ_PASSWORD")

cnxn = JobsEqConnection(username, password)
