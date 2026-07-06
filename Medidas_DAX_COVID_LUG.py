Total Confirmed =
VAR CONFIRMED =
    SUMX(
        VALUES('COVID-19'[Country/Region]),
        SUMX(
            VALUES('COVID-19'[Province/State]),
            CALCULATE(MAX('COVID-19'[Confirmed]))
        )
    )
RETURN IF(CONFIRMED = 0, BLANK(), CONFIRMED)

Total Deaths =
VAR DEATHS =
    SUMX(
        VALUES('COVID-19'[Country/Region]),
        SUMX(
            VALUES('COVID-19'[Province/State]),
            CALCULATE(MAX('COVID-19'[Deaths]))
        )
    )
RETURN IF(DEATHS = 0, BLANK(), DEATHS)

Mortality Rate =
DIVIDE([Total Deaths], [Total Confirmed], 0)

Daily New Cases =
VAR CURRENT_DAY = [Total Confirmed]
VAR PREVIOUS_DAY =
    CALCULATE([Total Confirmed], DATEADD('CALENDAR'[Date], -1, DAY))
RETURN IF(ISBLANK(PREVIOUS_DAY), BLANK(), CURRENT_DAY - PREVIOUS_DAY)

Total Recovered =
SUM('COVID-19'[Recovered])

Recovery Rate =
DIVIDE([Total Recovered], [Total Confirmed], 0)
