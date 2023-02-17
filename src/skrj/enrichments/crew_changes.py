from skrj.enrichments import base

base.Enrichment(
    base.EnrichmentBehavior.ENRICH,
    {"crewChange": True},
    base.Condition(nameOfPoint="Warszawa Wschodnia"),
)
base.Enrichment(
    base.EnrichmentBehavior.ENRICH,
    {"crewChange": True},
    base.Condition(nameOfPoint="Katowice"),
)
