import pandas as pd

from raptor_search.timetable.gtfs import GTFS

class Timetable:
    def __init__(self, gtfs: GTFS) -> None:
        self.gtfs = gtfs

    def _prepare_routes(self) -> pd.DataFrame:
        route_info = self.gtfs.get_route_info()
        sorted = route_info.sort_values(by=["route_id", self.gtfs.earliest_trip_col, "departure_time"])
        return sorted
