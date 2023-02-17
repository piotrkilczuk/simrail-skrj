from skrj.enrichments import base

# LK1 - Odd
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 90, "mileage": 0.8},
    base.Condition(nameOfPoint="Warszawa Centralna"),
    base.Condition(nameOfPoint="Warszawa Zach. R19"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 100, "mileage": 4.1},
    base.Condition(nameOfPoint="Warszawa Zachodnia"),
    base.Condition(nameOfPoint="Warszawa Włochy"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 120, "mileage": 4.9},
    base.Condition(nameOfPoint="Warszawa Zachodnia"),
    base.Condition(nameOfPoint="Warszawa Włochy"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 160, "mileage": 7.1},
    base.Condition(nameOfPoint="Warszawa Włochy"),
    base.Condition(nameOfPoint="Józefinów"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 100, "mileage": 299.2},
    base.Condition(nameOfPoint="Dąbrowa Górnicza Ząbkowice"),
    base.Condition(nameOfPoint="Dąbrowa Górnicza"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 110, "mileage": 301.1},
    base.Condition(nameOfPoint="Dąbrowa Górnicza"),
    base.Condition(nameOfPoint="Będzin"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 100, "mileage": 307.8},
    base.Condition(nameOfPoint="Będzin"),
    base.Condition(nameOfPoint="Sosnowiec Główny"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 90, "mileage": 307.9},
    base.Condition(nameOfPoint="Będzin"),
    base.Condition(nameOfPoint="Sosnowiec Główny"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 100, "mileage": 308},
    base.Condition(nameOfPoint="Będzin"),
    base.Condition(nameOfPoint="Sosnowiec Główny"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 70, "mileage": 317.4},
    base.Condition(nameOfPoint="Katowice Zawodzie"),
    base.Condition(nameOfPoint="Katowice"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": 40, "mileage": 317.5},
    base.Condition(nameOfPoint="Katowice Zawodzie"),
    base.Condition(nameOfPoint="Katowice"),
)

# LK2 - Even
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 2, "maxSpeed": 80, "mileage": 3},
    base.Condition(nameOfPoint="Warszawa Wschodnia"),
    base.Condition(nameOfPoint="Warszawa Centralna"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 2, "maxSpeed": 60, "mileage": 1},
    base.Condition(nameOfPoint="Warszawa Wschodnia"),
    base.Condition(nameOfPoint="Warszawa Centralna"),
)

# LK4 - Odd
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 200, "mileage": 1.9},
    base.Condition(nameOfPoint="Grodzisk Maz. R58"),
    base.Condition(nameOfPoint="Korytów"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 160, "mileage": 78.4},
    base.Condition(nameOfPoint="Strzałki"),
    base.Condition(nameOfPoint="Idzikowice"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 120, "mileage": 79.9},
    base.Condition(nameOfPoint="Strzałki"),
    base.Condition(nameOfPoint="Idzikowice"),
)
base.Enrichment(
    base.EnrichmentBehavior.ENRICH,
    {"maxSpeed": 120},
    base.Condition(nameOfPoint="Idzikowice"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 160, "mileage": 82.3},
    base.Condition(nameOfPoint="Idzikowice"),
    base.Condition(nameOfPoint="Opoczno Południe"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 200, "mileage": 156.496},
    base.Condition(nameOfPoint="Włoszczowa Północ"),
    base.Condition(nameOfPoint="Knapówka"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 160, "mileage": 214.8},
    base.Condition(nameOfPoint="Góra Włodowska"),
    base.Condition(nameOfPoint="Zawiercie"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 4, "maxSpeed": 110, "mileage": 222.4},
    base.Condition(nameOfPoint="Góra Włodowska"),
    base.Condition(nameOfPoint="Zawiercie"),
)
