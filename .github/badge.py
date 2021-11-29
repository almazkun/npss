import anybadge
from coverage import coverage


def make_cov_badge() -> None:
    c = coverage()
    c.load()
    total = round(c.report(), 2)
    thresholds = {
        50: "red",
        60: "orange",
        75: "yellow",
        90: "green",
    }

    badge = anybadge.Badge(
        label="coverage", value=total, thresholds=thresholds, value_suffix="%"
    )
    badge.write_badge("coverage.svg", overwrite=True)


if __name__ == "__main__":
    make_cov_badge()
