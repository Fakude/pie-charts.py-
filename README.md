# Enrolment Distribution Visualisation

This project develops an original pie-chart exercise into a small, reproducible visualisation study. It uses a clearly labelled example enrolment dataset and produces two complementary views of the same distribution.

## Why two charts?

- The **donut chart** quickly communicates each study stage's share of the whole.
- The **bar chart** makes exact comparisons easier, especially when values are close.

Using both avoids presenting a pie chart as the only answer to a comparison problem.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python visualise_enrolment.py
```

The chart is written to `outputs/enrolment_distribution.png`.

## Test

```bash
python -m unittest discover -s tests -v
```

The example values are illustrative and should be replaced with documented source data for a real report.

## Continuous integration

[![Python CI](https://github.com/Fakude/pie-charts.py-/actions/workflows/ci.yml/badge.svg)](https://github.com/Fakude/pie-charts.py-/actions/workflows/ci.yml)

The workflow installs requirements and executes the unit tests on Python 3.12 for each push and pull request. See `.github/workflows/ci.yml`.
