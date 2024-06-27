import decouple
import pytest
from eqlink import JobsEqConnection
import pandas as pd

# Initialize connection to JobsEq Database
USERNAME = decouple.config("JOBSEQ_USERNAME")
PASSWORD = decouple.config("JOBSEQ_PASSWORD")
cnxn = JobsEqConnection(USERNAME, PASSWORD)

# Test all Analytics upon four criteria established in issue #12 on Github.
# 1.1: Ensure enpoint returns a HTTP 200 code, esstentially no errors are raised.
# 1.2: Ensure that each endpoint returns the expected number of columns.
# 1.3: Ensure that at least 1 row of data is returned by each analytic.
# 1.4: Ensure that as_frame properly returns either dataframes or dictionaries.


class TestIndustryOccupationMixOccupationMix:
    def test_1(self):
        cnxn.industry_occupation_mix.occupation_mix(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.industry_occupation_mix.occupation_mix(
            as_frame=True
        )

        assert len(dataframe.columns) == 9

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.industry_occupation_mix.occupation_mix(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.industry_occupation_mix.occupation_mix(as_frame=False)

        assert type(datadict) == dict


class TestIndustryOccupationMixIndustryMix:
    def test_1(self):
        cnxn.industry_occupation_mix.industry_mix(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.industry_occupation_mix.industry_mix(
            as_frame=True
        )

        assert len(dataframe.columns) == 8

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.industry_occupation_mix.industry_mix(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.industry_occupation_mix.industry_mix(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsEmploymentTrends:
    def test_1(self):
        cnxn.labor_wage_trends.employment_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.employment_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.employment_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.employment_trends(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsTotalWageTrends:
    def test_1(self):
        cnxn.labor_wage_trends.total_wage_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.total_wage_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.total_wage_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.total_wage_trends(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsCostOfLivingTrends:
    def test_1(self):
        cnxn.labor_wage_trends.cost_of_living_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.cost_of_living_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 5

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.cost_of_living_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.cost_of_living_trends(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsAverageWageTrends:
    def test_1(self):
        cnxn.labor_wage_trends.average_wage_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.average_wage_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.average_wage_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.average_wage_trends(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsUnemploymentRateTrends:
    def test_1(self):
        cnxn.labor_wage_trends.unemployment_rate_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.unemployment_rate_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.unemployment_rate_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.unemployment_rate_trends(as_frame=False)

        assert type(datadict) == dict


class TestLaborWageTrendsEstablishmentTrends:
    def test_1(self):
        cnxn.labor_wage_trends.establishment_trends(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.establishment_trends(
            as_frame=True
        )

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.labor_wage_trends.establishment_trends(
            as_frame=True
        )

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.labor_wage_trends.establishment_trends(as_frame=False)

        assert type(datadict) == dict


class TestSupplyChainSuppliers:
    def test_1(self):
        cnxn.supply_chain.suppliers(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.suppliers(as_frame=True)

        assert len(dataframe.columns) == 8

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.suppliers(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.supply_chain.suppliers(as_frame=False)

        assert type(datadict) == dict


class TestSupplyChainBuyers:
    def test_1(self):
        cnxn.supply_chain.buyers(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.buyers(as_frame=True)

        assert len(dataframe.columns) == 5

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.buyers(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.supply_chain.buyers(as_frame=False)

        assert type(datadict) == dict


class TestSupplyChainGaps:
    def test_1(self):
        cnxn.supply_chain.gaps(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.gaps(as_frame=True)

        assert len(dataframe.columns) == 7

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.supply_chain.gaps(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.supply_chain.gaps(as_frame=False)

        assert type(datadict) == dict


class TestDemographicProfileCurrent:
    def test_1(self):
        cnxn.demographic_profile.current(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.demographic_profile.current(as_frame=True)

        assert len(dataframe.columns) == 3

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.demographic_profile.current(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.demographic_profile.current(as_frame=False)

        assert type(datadict) == dict


class TestSkillGapsBySkill:
    def test_1(self):
        cnxn.skill_gaps.by_skill(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_skill(as_frame=True)

        assert len(dataframe.columns) == 3

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_skill(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.skill_gaps.by_skill(as_frame=False)

        assert type(datadict) == dict


class TestSkillGapsByOccupation:
    def test_1(self):
        cnxn.skill_gaps.by_occupation(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_occupation(as_frame=True)

        assert len(dataframe.columns) == 4

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_occupation(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.skill_gaps.by_occupation(as_frame=False)

        assert type(datadict) == dict


class TestSkillGapsByRegion:
    def test_1(self):
        cnxn.skill_gaps.by_region(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_region(as_frame=True)

        assert len(dataframe.columns) == 3

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.skill_gaps.by_region(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.skill_gaps.by_region(as_frame=False)

        assert type(datadict) == dict


class TestMapsAwardsMap:
    def test_1(self):
        cnxn.maps.awards_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.awards_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.awards_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.awards_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsCommuteMap:
    def test_1(self):
        cnxn.maps.commute_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.commute_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.commute_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.commute_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsDemographicsMap:
    def test_1(self):
        cnxn.maps.demographics_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.demographics_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.demographics_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.demographics_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsEmploymentMap:
    def test_1(self):
        cnxn.maps.employment_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.employment_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.employment_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.employment_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsGdpMap:
    def test_1(self):
        cnxn.maps.gdp_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.gdp_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.gdp_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.gdp_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsIndustryMap:
    def test_1(self):
        cnxn.maps.industry_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.industry_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.industry_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.industry_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsOccupationMap:
    def test_1(self):
        cnxn.maps.occupation_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.occupation_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.occupation_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.occupation_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsRtiMap:
    def test_1(self):
        cnxn.maps.rti_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.rti_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.rti_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.rti_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsRuralMap:
    def test_1(self):
        cnxn.maps.rural_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.rural_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.rural_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.rural_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsUnderemployemntMap:
    def test_1(self):
        cnxn.maps.underemployemnt_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.underemployemnt_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.underemployemnt_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.underemployemnt_map(as_frame=False)

        assert type(datadict) == dict


class TestMapsUnemploymentMap:
    def test_1(self):
        cnxn.maps.unemployment_map(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.maps.unemployment_map(as_frame=True)

        assert len(dataframe.columns) == 2

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.maps.unemployment_map(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.maps.unemployment_map(as_frame=False)

        assert type(datadict) == dict


class TestEconomicImpactEmployment:
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_1(self):
        cnxn.economic_impact.employment(as_frame=True)

        return

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_2(self):
        dataframe: pd.Dataframe = cnxn.economic_impact.employment(as_frame=True)

        assert len(dataframe.columns) == 1

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_3(self):
        dataframe: pd.Dataframe = cnxn.economic_impact.employment(as_frame=True)

        assert len(dataframe) >= 1

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_4(self):
        datadict = cnxn.economic_impact.employment(as_frame=False)

        assert type(datadict) == dict


class TestEconomicImpactSalesOutput:
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_1(self):
        cnxn.economic_impact.sales_output(as_frame=True)

        return

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_2(self):
        dataframe: pd.Dataframe = cnxn.economic_impact.sales_output(as_frame=True)

        assert len(dataframe.columns) == 1

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_3(self):
        dataframe: pd.Dataframe = cnxn.economic_impact.sales_output(as_frame=True)

        assert len(dataframe) >= 1

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_4(self):
        datadict = cnxn.economic_impact.sales_output(as_frame=False)

        assert type(datadict) == dict


class TestAwardGapsProgram:
    def test_1(self):
        cnxn.awards_gap.program(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.awards_gap.program(as_frame=True)

        assert len(dataframe.columns) == 8

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.awards_gap.program(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.awards_gap.program(as_frame=False)

        assert type(datadict) == dict


class TestAwardGapsOccupation:
    def test_1(self):
        cnxn.awards_gap.occupation(as_frame=True)

        return

    def test_2(self):
        dataframe: pd.Dataframe = cnxn.awards_gap.occupation(as_frame=True)

        assert len(dataframe.columns) == 7

    def test_3(self):
        dataframe: pd.Dataframe = cnxn.awards_gap.occupation(as_frame=True)

        assert len(dataframe) >= 1

    def test_4(self):
        datadict = cnxn.awards_gap.occupation(as_frame=False)

        assert type(datadict) == dict