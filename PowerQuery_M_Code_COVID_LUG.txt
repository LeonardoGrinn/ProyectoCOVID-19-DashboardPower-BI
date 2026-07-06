// Consulta Confirmed
let
    Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Unpivoted = Table.UnpivotOtherColumns(PromotedHeaders, {"Province/State", "Country/Region", "Lat", "Long"}, "Date", "Confirmed"),
    ChangedTypes = Table.TransformColumnTypes(Unpivoted,{{"Date", type date}, {"Confirmed", Int64.Type}, {"Lat", type number}, {"Long", type number}})
in
    ChangedTypes

// Repetir la misma logica para Deaths y Recovered, cambiando el nombre de la columna de valor.
// Merge Queries as New usando Province/State, Country/Region y Date.
