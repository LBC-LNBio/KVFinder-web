import calendar
import datetime

import matplotlib.pyplot as plt
import numpy
import pandas as pd

# Colorblind palette
COLORBLIND = [
    "#377eb8",  # blue
    "#ff7f00",  # orange
    "#4daf4a",  # green
    "#f781bf",  # pink
    "#a65628",  # brown
    "#984ea3",  # purple
    "#999999",  # gray
    "#dede00",  # yellow
    "#e41a1c",  # red
]

MONTHS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}


class Usage(object):

    def __init__(self, fname: str):
        self.today = datetime.datetime.today()
        self.dates = self._load_data(fname)

    def _load_data(self, fname: str) -> pd.DataFrame:
        # Open raw usage data
        with open(fname, "r") as f:
            lines = [line for line in f.readlines() if not line.startswith("total")]
            # Process dates
            dates = []
            for line in lines:
                # Long ISO format (%Y-%m-%d)
                line = line.split()[5]
                dates.append(line)

        # Convert to DataFrame and export to csv
        dates = pd.DataFrame(dates, columns=["Data"])
        dates.Data = pd.to_datetime(dates.Data)

        return dates

    def filter(self, start: datetime.datetime, end: datetime.datetime) -> pd.DataFrame:
        # Check if data is a string
        if isinstance(start, str):
            start = pd.to_datetime(start)
        if isinstance(end, str):
            end = pd.to_datetime(end)
        # Check if data is a date
        if isinstance(start, datetime.date):
            start = datetime.datetime(start.year, start.month, start.day)
        if isinstance(end, datetime.date):
            end = datetime.datetime(end.year, end.month, end.day)
        # Check if start is before end
        if start > end:
            raise ValueError("Start date must be before end date")

        # Get indexes
        indexes = ((self.dates >= start) & (self.dates < end)).Data

        return self.dates.loc[indexes]


def plot_last_month(data: Usage) -> None:
    # Get last month
    last_month = data.filter(
        datetime.datetime(data.today.year, data.today.month - 1, 1),
        datetime.datetime(data.today.year, data.today.month, 1),
    )
    last_month.columns = ["Jobs"]

    # Count usage per day from last month
    count = last_month.groupby(last_month["Jobs"].dt.day).count()

    # Average jobs per day
    _, number_of_days = calendar.monthrange(data.today.year, data.today.month - 1)
    avg = count.sum().values / number_of_days

    # Plot bar plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 9), clear=True, tight_layout=True)

    # Bar plot
    rects = ax.bar(
        x=count.index,
        height=count["Jobs"].values,
        align="center",
        ecolor="black",
        capsize=5,
        width=0.5,
        edgecolor="black",
        color="#377eb8",
        alpha=0.8,
    )

    # Annotate bars
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            1.05 * height,
            "%d" % int(height),
            ha="center",
            va="bottom",
            size=20,
        )

    # Average jobs per day
    ax.axhline(y=avg, color="red", linestyle="--", label="Jobs per day")

    # Customize
    ymin, ymax = 0, round(count.max().values[0] / 100) * 100
    ax.grid(which="major", axis="y", linestyle="--")
    ax.set_ylabel("Jobs", size=20)
    ax.set_ylim(ymin, ymax + 1)
    ax.yaxis.set_ticks(numpy.arange(ymin, ymax + 10, 10))
    ax.tick_params(axis="y", labelsize=15)
    ax.set_xlabel(f"{MONTHS[data.today.month-1]}-{data.today.year}", size=20)
    ax.tick_params(axis="x", labelsize=15)
    ax.xaxis.set_ticks(numpy.arange(0, number_of_days, 1))

    # Legend
    ax.legend(loc="upper left", fontsize=20)

    plt.savefig(f"{MONTHS[data.today.month-1]}-{(data.today.year) % 100}-daily.png", dpi=300)


def plot_last_12_months(data: Usage) -> None:
    # Get past 12 months
    last_12_months = data.filter(
        datetime.datetime(data.today.year - 1, data.today.month, 1),
        datetime.datetime(data.today.year, data.today.month, 1),
    )
    last_12_months.columns = ["Jobs"]

    # Count usage per day from last month
    count = last_12_months.groupby(last_12_months["Jobs"].dt.month).count()

    # Jobs per month
    avg = count.sum().values[0] / 12

    # Months
    x = [
        f"{MONTHS[((index + data.today.month - 2) % 12) + 1]}-{(data.today.year if (index + data.today.month) / 12 > 1 else data.today.year - 1) % 100}"
        for index in count.index
    ]

    # Plot bar plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 9), clear=True, tight_layout=True)

    # Bar plot
    rects = ax.bar(
        x=x,
        height=count["Jobs"].values,
        align="center",
        ecolor="black",
        capsize=5,
        width=0.5,
        edgecolor="black",
        color="#377eb8",
        alpha=0.8,
    )

    # Annotate bars
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            height + 2,
            "%d" % int(height),
            ha="center",
            va="bottom",
            size=20,
        )

    # Average jobs per day
    ax.axhline(y=avg, color="red", linestyle="--", label="Jobs per month")

    # Customize
    ymin, ymax = 0, (round(count.max().values[0] / 100) * 100) + 50
    ax.grid(which="major", axis="y", linestyle="--")
    ax.set_ylabel("Jobs", size=20)
    ax.set_ylim(ymin, ymax + 1)
    ax.yaxis.set_ticks(numpy.arange(ymin, ymax + 25, 25))
    ax.tick_params(axis="y", labelsize=15)
    ax.tick_params(axis="x", labelsize=15)
    ax.xaxis.set_ticks(x)

    # Legend
    ax.legend(loc="upper left", fontsize=20)

    plt.savefig(f"{x[0]}-{x[-1]}.png", dpi=300)


def plot_per_year(data: Usage) -> None:
    # Count usage per year
    count = data.dates.groupby(data.dates["Data"].dt.year).count()
    count.columns = ["Jobs"]

    # Jobs per year
    avg = count.sum().values[0] / count.index.shape[0]

    # Plot bar plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 9), clear=True, tight_layout=True)

    # Bar plot
    rects = ax.bar(
        x=count.index,
        height=count["Jobs"].values,
        align="center",
        ecolor="black",
        capsize=5,
        width=0.5,
        edgecolor="black",
        color="#377eb8",
        alpha=0.8,
    )

    # Annotate bars
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            height + 2,
            "%d" % int(height),
            ha="center",
            va="bottom",
            size=20,
        )

    # Average jobs per day
    ax.axhline(y=avg, color="red", linestyle="--", label="Jobs per year")

    # Customize
    ymin, ymax = 0, (round(count.max().values[0] / 1000) * 1000) + 100
    ax.grid(which="major", axis="y", linestyle="--")
    ax.set_ylabel("Jobs", size=20)
    ax.set_ylim(ymin, ymax + 1)
    ax.yaxis.set_ticks(numpy.arange(ymin, ymax + 250, 250))
    ax.tick_params(axis="y", labelsize=15)
    ax.set_xlabel("Year", size=20)
    ax.tick_params(axis="x", labelsize=15)
    ax.xaxis.set_ticks(count.index)

    # Legend
    ax.legend(loc="upper left", fontsize=20)

    plt.savefig(f"{MONTHS[data.today.month-1]}-{data.today.year % 100}-yearly.png", dpi=300)


if __name__ == "__main__":
    # Read usage data
    data = Usage("usage.txt")

    # Plot last month
    plot_last_month(data)

    # Plot last 12 months
    plot_last_12_months(data)

    # Plot per year
    plot_per_year(data)
