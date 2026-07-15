import json

from sample_order_system.console.app import run_app
from sample_order_system.console.state import AppState
from sample_order_system.domain.sample import Sample


def test_run_app_saves_data_on_exit(tmp_path):
    state = AppState()
    state.sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    sample_filepath = tmp_path / "samples.json"
    order_filepath = tmp_path / "orders.json"
    inputs = iter(["0"])

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=lambda message: None,
        sample_filepath=sample_filepath,
        order_filepath=order_filepath,
    )

    saved_samples = json.loads(sample_filepath.read_text(encoding="utf-8"))
    assert saved_samples[0]["sample_id"] == "S-001"
    assert order_filepath.exists()
