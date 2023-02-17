from skrj.enrichments import base

# LK1 - Odd
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": "90", "mileage": 0.8},
    base.Condition(nameOfPoint="Warszawa Centralna"),
    base.Condition(nameOfPoint="Warszawa Zach. R19"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": "100", "mileage": 4.1},
    base.Condition(nameOfPoint="Warszawa Zachodnia"),
    base.Condition(nameOfPoint="Warszawa Włochy"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": "120", "mileage": 4.9},
    base.Condition(nameOfPoint="Warszawa Zachodnia"),
    base.Condition(nameOfPoint="Warszawa Włochy"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 1, "maxSpeed": "160", "mileage": 7.1},
    base.Condition(nameOfPoint="Warszawa Włochy"),
    base.Condition(nameOfPoint="Józefinów"),
)


# LK2 - Even
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 2, "maxSpeed": "80", "mileage": 3},
    base.Condition(nameOfPoint="Warszawa Wschodnia"),
    base.Condition(nameOfPoint="Warszawa Centralna"),
)
base.Enrichment(
    base.EnrichmentBehavior.SPEED_CHANGE,
    {"line": 2, "maxSpeed": "60", "mileage": 1},
    base.Condition(nameOfPoint="Warszawa Wschodnia"),
    base.Condition(nameOfPoint="Warszawa Centralna"),
)
