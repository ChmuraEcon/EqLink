import decouple
from eqlink import JobsEqConnection
import pandas as pd

# Initialize connection to JobsEq Database
USERNAME = decouple.config("JOBSEQ_USERNAME")
PASSWORD = decouple.config("JOBSEQ_PASSWORD")
cnxn = JobsEqConnection(USERNAME, PASSWORD)

# Test all Analytics upon four criteria established in issue #9 on Github.
# 1.1: Ensure enpoint returns a HTTP 200 code, esstentially no errors are raised.
# 1.2: Ensure that each endpoint returns the expected number of columns.
# 1.3: Ensure that at least 1 row of data is returned by each analytic.
# 1.4: Ensure that as_frame properly returns either dataframes or dictionaries.


class TestOccupationSnapshot:
    def test_1(self):
        cnxn.core.occupation_snapshot(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_snapshot(as_frame=True)

        assert len(dataframe.columns) == 15

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_snapshot(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.occupation_snapshot(as_frame=False)

        assert type(datadict) == dict


class TestOccupationWages:
    def test_1(self):
        cnxn.core.occupation_wages(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_wages(as_frame=True)

        assert len(dataframe.columns) == 10

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_wages(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.occupation_wages(as_frame=False)

        assert type(datadict) == dict


class TestIndustrySnapshot:
    def test_1(self):
        cnxn.core.industry_snapshot(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.industry_snapshot(as_frame=True)

        assert len(dataframe.columns) == 13

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.industry_snapshot(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.industry_snapshot(as_frame=False)

        assert type(datadict) == dict


class TestWhatIf:
    def test_1(self):
        cnxn.core.what_if(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.what_if(as_frame=True)

        assert len(dataframe.columns) == 10

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.what_if(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.what_if(as_frame=False)

        assert type(datadict) == dict


class TestShiftShare:
    def test_1(self):
        cnxn.core.shift_share(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.shift_share(as_frame=True)

        assert len(dataframe.columns) == 6

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.shift_share(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.shift_share(as_frame=False)

        assert type(datadict) == dict


class TestIndustryDiversity:
    def test_1(self):
        cnxn.core.industry_diversity(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.industry_diversity(as_frame=True)

        assert len(dataframe.columns) == 8

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.industry_diversity(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.industry_diversity(as_frame=False)

        assert type(datadict) == dict


class TestOccupationDiversity:
    def test_1(self):
        cnxn.core.occupation_diversity(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_diversity(as_frame=True)

        assert len(dataframe.columns) == 13

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.occupation_diversity(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.occupation_diversity(as_frame=False)

        assert type(datadict) == dict


class TestAwards:
    def test_1(self):
        cnxn.core.awards(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.awards(as_frame=True)

        assert len(dataframe.columns) == 12

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.awards(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.awards(as_frame=False)

        assert type(datadict) == dict


class TestWillingAndAble:
    def test_1(self):
        cnxn.core.willing_and_able(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.willing_and_able(as_frame=True)

        assert len(dataframe.columns) == 9

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.willing_and_able(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.willing_and_able(as_frame=False)

        assert type(datadict) == dict


class TestJobAndTalentLocator:
    def test_1(self):
        cnxn.core.job_and_talent_locator(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.job_and_talent_locator(as_frame=True)

        assert len(dataframe.columns) == 11

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.job_and_talent_locator(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.job_and_talent_locator(as_frame=False)

        assert type(datadict) == dict


class TestMilitaryExits:
    def test_1(self):
        cnxn.core.Military_Exits(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.core.Military_Exits(as_frame=True)

        assert len(dataframe.columns) == 3

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.core.Military_Exits(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.core.Military_Exits(as_frame=False)

        assert type(datadict) == dict
