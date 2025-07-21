# EDGG D-ATIS Configuration for vATIS

## Installation

To use this configuration with vATIS:

1. Download and install the latest beta version of vATIS from the [official website](https://vatis.app).
2. Download the [`vATIS Profile - EDGG D-ATIS.json`](https://github.com/VATGER-Nav/edgg-vatis/blob/main/vATIS%20Profile%20-%20EDGG%20D-ATIS.json) file from this repository. **Do not use the Development file** as this will not receive any automatic updates!
3. When opening vATIS import the downloaded profile.
4. The EDGG vATIS profile should now be available for use and will update automatically.

## Usage
Airport Condition and NOTAM Presets applied by clicking on the "Airport Conditions"/"NOTAM" header.

### Airport Conditions
The airport conditions are used to set the approach type in use (e.g. ILS or RNP).

### NOTAMs
NOTAM Presets are used to set the departure frequency and additional information (e.g. LVO Ops in use).

- "WHEN AIRBORNE CONTACT LANGEN RADAR ON 125.020"
- "LOW VISIBILITY PROCEDURES IN OPERATION, CAT II AND III AVBL."
- "SRA APPROACH AVAILABLE ON REQUEST"
- "CAUTION WINDSHEAR ALL RWYS"

## Support
For issues with this configuration, please open an issue on GitHub or contact the EDGG-Nav team.

## Editing data
Only edit the [`vATIS Profile - EDGG D-ATIS Development.json`](https://github.com/VATGER-Nav/edgg-vatis/blob/main/vATIS%20Profile%20-%20EDGG%20D-ATIS%20Development.json) file within the dev branch! This file will not receive any automatic updates. The release file is generated out of the development file after merging the "dev branch" into the "main branch". All update information are added automatically.
