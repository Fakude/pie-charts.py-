"""Generate clear enrolment-distribution charts from a CSV file."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


PALETTE = ["#2f6b5d", "#d7ac4a", "#cd6956"]


def load_data(path: str | Path) -> list[tuple[str, int]]:
    with Path(path).open(encoding="utf-8", newline="") as file:
        rows = [(row["study_stage"].strip(), int(row["students"])) for row in csv.DictReader(file)]
    if not rows or any(value <= 0 for _, value in rows):
        raise ValueError("Data must contain at least one positive student count.")
    return rows


def create_charts(rows: list[tuple[str, int]], output: str | Path) -> None:
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    labels, values = zip(*rows)
    total = sum(values)
    plt.style.use("seaborn-v0_8-whitegrid")
    figure, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)
    wedges, _texts, percentages = axes[0].pie(values, colors=PALETTE, startangle=90, autopct="%1.1f%%", pctdistance=.75, wedgeprops={"width": .48, "edgecolor": "white"})
    axes[0].text(0, .06, f"{total:,}", ha="center", va="center", fontsize=23, fontweight="bold")
    axes[0].text(0, -.14, "students", ha="center", va="center", fontsize=10, color="#56605e")
    axes[0].legend(wedges, [f"{label}: {value:,}" for label, value in rows], loc="lower center", bbox_to_anchor=(.5, -.2), frameon=False)
    axes[0].set_title("Share of enrolment", fontweight="bold", pad=16)
    bars = axes[1].bar(labels, values, color=PALETTE, width=.58)
    axes[1].bar_label(bars, labels=[f"{value:,}" for value in values], padding=4, fontweight="bold")
    axes[1].set(title="Student counts by study stage", ylabel="Students", ylim=(0, max(values) * 1.18))
    axes[1].spines[["top", "right"]].set_visible(False)
    figure.suptitle("College enrolment distribution", fontsize=16, fontweight="bold")
    figure.savefig(output / "enrolment_distribution.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    rows = load_data("data/enrolment.csv")
    create_charts(rows, "outputs")
    print(f"Created chart for {sum(value for _, value in rows):,} students.")


if __name__ == "__main__":
    main()
