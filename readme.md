<p align="center"> 
  <img src="logos\JobsEQ_Logo-01.png" alt="JobsEQ Logo" width="80px" height="80px">
</p>

<h1 align="center"> EqLink: A Pandas Wrapper for JobsEQ </h1>

<div align="center">

  <a href="">[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)</a>
  <a href="">[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)</a>
  <a href="">![Maintainer](https://img.shields.io/badge/maintainer-JosephDYork-blue)</a>

</div>

EqLink is a  Python/Pandas API wrapper for facilitating easy, readable, and quick access to JobsEQ by Chmura data. This project has been created and maintained by Joseph York since June 2022, and is not offically maintained by either Chmura or JobsEQ Engineers. It currently features the following:
- Access to all of Chmura's Core analytics
- Preliminary access to Chmura's RTI analytics, including individual Job Posting data
- Built in response parsing to both python dictionaries and pandas dataframes
- A thirst for adventure (and labor data) :sunglasses::sunglasses::sunglasses:

<div align="center">

  [Getting started](#getting-started) •
  [Installation](#installation) •
  [Planned Features](#planned-features) •
  [Supported Analytics](#supported-analytics)
  
</div>

## Getting started
With EqLink, you can access JobsEq data in as few as 3 lines of code. All you need to do is the following:
- Instantiate an instance of the JobsEqConnection Class, using your Chmura login credentials.
- Call the method corresponding to the analytic you wish to run.
- Send it to a variable and start analyzing!

```python
# Basic Industry Snapshot Script

from eqlink import JobsEqConnection

cnxn = JobsEqConnection("USERNAME", "PASSWORD")
results = cnxn.core.industry_snapshot()

print(results)
```

## Installation
Since EqLink isn't fully released yet, there is no package available on PyPI. This means in order to use EqLink, you get to learn how to install a pip package from a github url!
- First things first, you'll want to boot up a terminal instance and do the following:
```terminal
pip install --upgrade https://github.com/ChmuraEcon/EqLink/tarball/main
```
After that you are ready to go! Pretty easy!

## Planned Features
Since this is an early release of EqLink, there are numerous features I'd still like to incorperate, as well as some more pressing, immediate goals I'd like to see tackled as soon as possible.
- Full support for either Data Fetch or Data Explorer, both if possible. These analytics behave differently, so some creative wrapping might be necessary.
- A completed suite of unit tests, beyond the bare bones functionality tests that I currently have implimented.
- A set of default parameters that can be set by the user, that will function across all analytics. This could cause some analytics to error out, so error handling for these instances would be necessary.
- A system that caches the last five responses received by the library, with the user being able to set this number manually if so desired.
## Supported Analytics

### Core Analytics
|Analytic|ID|Status|
|---|---|:-:|
|Occupation||---|
|Occupation Snapshot|346c9b58-4636-4b92-9521-be86a0868f76| :heavy_check_mark: |
|Occupation Wages|772c8997-01e0-4404-b05a-3d16138a39d2| :heavy_check_mark: |
|Occupation Gaps|f0b719b4-308b-4c5c-b689-baa6b909d5f3| :heavy_check_mark: |
|Industry/Occupation Mix|fa6e2fbe-0f68-498e-80a6-55a6c1b020cd| :heavy_check_mark: |
|Industry||---|
|Industry Snapshot|9d7913e1-8395-48ec-98b6-a5476cc9c2f3| :heavy_check_mark: |
|Labor & Wage Trends|be01565c-5935-42a6-b89a-dccc511935d3| :heavy_check_mark: |
|What-If|8d554e48-8940-4d0f-958b-067c462340ca| :heavy_check_mark: |
|Economic Impact|58a2d8fc-bb40-4e4d-b78e-f719fa1a361e| :heavy_check_mark: |
|Supply Chain|d2adef1d-7f93-48dc-8b33-7084c117db7b| :heavy_check_mark: |
|Shift Share|9dfd4380-fe28-458f-9dcf-d2f1c4750358| :heavy_check_mark: |
|Demographics||---|
|Demographic Profile|98529f7c-deb9-421f-9ab2-9fa910d2dffc| :heavy_check_mark: |
|Occupation Diversity|7993e1f6-b66f-4a15-a876-3d93731affa8| :heavy_check_mark: |
|Industry Diversity|4c03b549-365e-487f-941f-ccde3df884a3| :heavy_check_mark: |
|Education||---|
|Awards|feea06ae-4562-470b-afee-acc328f991ec| :heavy_check_mark: |
|Award Gaps|ae95e9c6-de90-492c-a7e3-d07e8ea89d2b| :heavy_check_mark: |
|Willing & Able|b71bc7d7-18c4-4c03-b4a0-fccbe9c5cd64| :heavy_check_mark: |
|Skill Gaps|148c7d96-36e5-446d-a9b8-f4078bd19d74| :heavy_check_mark: |
|Big Picture||---|
|RTI|fb9d934a-17db-4a9d-94d2-54a7c93b3a3d| :heavy_check_mark: |
|Maps|434d0060-62a0-4164-916c-c1a78e44c827| :heavy_check_mark: |
|Job & Talent Locator|a3c057c9-49e2-4876-84c2-a198b3f84198| :heavy_check_mark: |
|Resume Forensics|704e560e-fef2-4d5e-99f7-dfc2355582f5| :heavy_check_mark: |
|Data Fetch|167834a7-acbb-4058-ad51-a225986deebc| :heavy_check_mark: |
|More||---|
|International Data|b7042bbc-ff57-4a27-aa6e-2e7403ba67e2| :heavy_check_mark: |
|LaborEQ|ecabd7e1-d472-4d9c-ac21-6dc4de681d45| :heavy_check_mark: |
|Military Exits|960cf539-83f8-42a5-b640-886806c90e08| :heavy_check_mark: |

### Compound Analytics
|Analytic|ID|Status|
|---|---|:-:|
|Industry/Occupation Mix|fa6e2fbe-0f68-498e-80a6-55a6c1b020cd| :heavy_check_mark: |
|Labor & Wage Trends|be01565c-5935-42a6-b89a-dccc511935d3| :heavy_check_mark: |
|Supply Chain|d2adef1d-7f93-48dc-8b33-7084c117db7b| :heavy_check_mark: |
|Demographic Profile|98529f7c-deb9-421f-9ab2-9fa910d2dffc| :heavy_check_mark: |
|Skill Gaps|148c7d96-36e5-446d-a9b8-f4078bd19d74| :heavy_check_mark: |
|Maps|434d0060-62a0-4164-916c-c1a78e44c827| :heavy_check_mark: |

### Non-Traditional LMI Analytics
|Analytic|ID|Status|
|----|---|:-:|
|RTI |fb9d934a-17db-4a9d-94d2-54a7c93b3a3d| :heavy_check_mark: |
|Resume Forensics &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|704e560e-fef2-4d5e-99f7-dfc2355582f5| :heavy_check_mark: |
### Table Building Analytics
|Analytic|ID|Status|
|---|---|:-:|
|Data Fetch &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|167834a7-acbb-4058-ad51-a225986deebc| :heavy_check_mark: |
### EqLink Non-Supported Analytics
|Analytic|ID|Status|
|---|---|:-:|
|Labor Inventory &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|ad59e868-e390-4c12-a618-48fd1f1eb5ed| :wavy_dash: |
|Forecast Comparison|9f0ebb07-ffac-471f-add5-1c3001df491f| :wavy_dash: |
|Career Training Ladders|34598d36-5ae9-41b5-88d0-d1b551cdace4| :wavy_dash: |
|Clusters|cede07f3-4180-44fe-843b-f0132e3ccebe| :wavy_dash: |
|Data Explorer|af08cc8a-f74c-402c-b578-d37955972e59| :wavy_dash: |
|Employer Database|b9ff7dab-c15d-4f65-bf81-c8dec520164b| :wavy_dash: |
