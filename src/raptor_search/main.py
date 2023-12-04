"""Main module."""
from raptor_search.timetable.gtfs import GTFS
from raptor_search.timetable.timetable import Timetable
from pathlib import Path

if __name__ == "__main__":
    gtfs = GTFS(Path("data/fp2023"))
    gtfs.filter_agencies(["11", "33"])
    timetable = Timetable(gtfs)
    test = timetable._prepare_routes()
    print("yes")
