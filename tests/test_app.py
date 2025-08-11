import pytest
from dash.testing.application_runners import import_app

# 1. Check header exists and has expected text
def test_header_present(dash_duo):
    app = import_app("scripts.app")
    dash_duo.start_server(app)

    # Wait until header is present
    dash_duo.wait_for_element("h1", timeout=5)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text


# 2. Check the main graph exists
def test_graph_present(dash_duo):
    app = import_app("scripts.app")
    dash_duo.start_server(app)

    # Wait until graph renders
    dash_duo.wait_for_element("#sales-graph", timeout=5)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


# 3. Check the region picker exists
def test_region_picker_present(dash_duo):
    app = import_app("scripts.app")
    dash_duo.start_server(app)

    # Wait until region picker renders
    dash_duo.wait_for_element("#region-selector", timeout=5)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None