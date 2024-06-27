import decouple
import pandas as pd
from eqlink import JobsEqConnection, RtiFilter

# Initialize connection to JobsEq Database
USERNAME = decouple.config("JOBSEQ_USERNAME")
PASSWORD = decouple.config("JOBSEQ_PASSWORD")
cnxn = JobsEqConnection(USERNAME, PASSWORD)

# Test all Analytics upon four criteria established in issue #21 on Github.
# 1.1: Ensure enpoint returns a HTTP 200 code, esstentially no errors are raised.
# 1.2: Ensure that each endpoint returns the expected number of columns.
# 1.3: Ensure that at least 1 row of data is returned by each analytic.
# 1.4: Ensure that as_frame properly returns either dataframes or dictionaries.


class TestRtiAnalyticsJobPostings:
    def test_1(self):
        cnxn.rti.job_postings(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.rti.job_postings(as_frame=True)

        assert len(dataframe.columns) == 12

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.rti.job_postings(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.rti.job_postings(as_frame=False)

        assert type(datadict) == dict


class TestRtiAnalyticsJobPostingsOverTime:
    def test_1(self):
        cnxn.rti.job_postings_over_time(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.rti.job_postings_over_time(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.rti.job_postings_over_time(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.rti.job_postings_over_time(as_frame=False)

        assert type(datadict) == dict


class TestRtiAnalyticsJobPostingWages:
    def test_1(self):
        cnxn.rti.job_posting_wages(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.rti.job_posting_wages(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.rti.job_posting_wages(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.rti.job_posting_wages(as_frame=False)

        assert type(datadict) == dict


class TestRtiAnalyticsResumes:
    def test_1(self):
        cnxn.rti.resumes(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.rti.resumes(as_frame=True)

        assert len(dataframe.columns) == 4

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.rti.resumes(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.rti.resumes(as_frame=False)

        assert type(datadict) == dict


class TestRtiFilter:
    def test_filter_1(self):
        test_obj = RtiFilter("occ", "11-1010", "Is")

        assert test_obj.__repr__() == (
            r'{"filters": [{"field": "occ", "key": "11-1010", "filterType": "Is"}]}'
        )
