"""
test_extract.py

Unit tests for src/extract.py
"""

from src.extract import extract_weather_data

class MockResponse:
    """
    Fake response object that behaves like a request response
    """

    def raise_for_status(self):
        pass

    def json(self):
        return {
            "latitude": 61.4991,
            "longitude": 23.7871,
            "timezone": "Europe/Helsinki",
            "hourly": {
                "time": ["2026-07-09T00:00"],
                "temperature_2m": [15.5],
                "relative_humidity_2m": [80],
                "precipitation": [0.0],
                "wind_speed_10m": [8.5],
            },
        }
    

def test_extract_weather_daat_returns_expected_data(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)

    data = extract_weather_data()

    assert "hourly" in data
    assert "time" in data["hourly"]
    assert data["location_name"] == "Tampere"
    assert data["hourly"]["temperature_2m"][0] == 15.5