import pathlib
import pandas as pd

class GTFS:

    earliest_trip_col: str = "earliest_trip"

    def __init__(self, gtfs_folder: pathlib.Path) -> None:
        self.agencies: pd.DataFrame = pd.read_csv(gtfs_folder / "agency.txt")
        self.trips: pd.DataFrame = pd.read_csv(gtfs_folder / "trips.txt")
        self.calendar_dates: pd.DataFrame = pd.read_csv(gtfs_folder / "calendar_dates.txt")
        self.calendar: pd.DataFrame = pd.read_csv(gtfs_folder / "calendar.txt")
        self.routes: pd.DataFrame = pd.read_csv(gtfs_folder / "routes.txt")
        self.stop_times: pd.DataFrame = pd.read_csv(gtfs_folder / "stop_times.txt")
        self.stops: pd.DataFrame = pd.read_csv(gtfs_folder / "stops.txt")
        self.transfers: pd.DataFrame = pd.read_csv(gtfs_folder / "transfers.txt")
        self.trips: pd.DataFrame = pd.read_csv(gtfs_folder / "trips.txt")

    def filter_agencies(self, agencies_to_consider: list[str]) -> None:
        relevant_agencies = pd.DataFrame(
            {"agency_id": agencies_to_consider}
        )
        self.agencies = self.agencies.merge(
            relevant_agencies,
            how="inner",
            on="agency_id"
        )
        self.routes = self.routes.merge(
            relevant_agencies,
            how="inner",
            on="agency_id"
        )
    
    def _add_earliest_trip(self) -> None:
        self.stop_times[self.earliest_trip_col] = self.stop_times.groupby(
            "trip_id"
        )["departure_time"].transform("min")


    def get_route_info(self) -> pd.DataFrame:
        self._add_earliest_trip()
        routes_joined = self.routes.merge(self.trips, on="route_id")
        stop_stop_times = self.stops.merge(self.stop_times, on="stop_id")
        return routes_joined.merge(stop_stop_times, on="trip_id")
