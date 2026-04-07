from textual.app import App, ComposeResult
from textual.widgets import Input, Select

class RocketFormApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Rocket name")
        yield Input(placeholder="Dry weight (kg)")
        yield Input(placeholder="Fuel weight (kg)")
        yield Select(
            [
                ("Cape Canaveral", "Cape Canaveral"),
                ("Vandenberg Space Force Base", "Vandenberg"),
                ("Baikonur Cosmodrome", "Baikonur"),
                ("Kourou", "Kourou")
            ],
            prompt="Select takeoff loaction"
        )
        yield Input(placeholder="Satellite weight (kg)")
        yield Input(placeholder="Wanted altitude (km)")
        yield Select(
            [
                ("LEO", "Low Earth Orbit"),
                ("GEO", "Geostationary Orbit"),
                ("SSO", "Sun-Synchronous Orbit"),
                ("MEO", "Medium Earth Orbit")
            ],
            prompt="Select orbit type"
        )

if __name__ == "__main__":
    app = RocketFormApp()
    app.run()   