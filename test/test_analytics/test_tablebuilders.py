import decouple
from eqlink import JobsEqConnection, DfField
import pandas as pd

# Initialize connection to JobsEq Database
USERNAME = decouple.config("JOBSEQ_USERNAME")
PASSWORD = decouple.config("JOBSEQ_PASSWORD")
cnxn = JobsEqConnection(USERNAME, PASSWORD)

# Test all Analytics upon four criteria established in issue #18 on Github.
# 1.1: Ensure enpoint returns a HTTP 200 code, esstentially no errors are raised.
# 1.2: Ensure that each enpoint returns the expected number of columns.
# 1.3: Ensure that at least 1 row of data is returned by each analytic.
# 1.4: Ensure that as_frame properly returns either dataframes or lists.


class TestDataFetchAnalyticsOccupation:
    def test_1(self):
        cnxn.datafetch.occupation(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.datafetch.occupation(as_frame=True)

        assert len(dataframe.columns) == 4

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.datafetch.occupation(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.datafetch.occupation(as_frame=False)

        assert type(datadict) == list


class TestDfFilter:
    def test_filter_1(self):
        test_obj = DfField("empl_placeOfWork", "2020-01-01", "Quarterly")

        assert test_obj.__repr__() == (
            r'{"field": "empl_placeOfWork", "timePoints": [{"date": "2020-01-01", "interval": "Quarterly"}]}'
        )
