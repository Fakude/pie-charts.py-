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
