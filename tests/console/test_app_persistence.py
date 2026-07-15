import json

from sample_order_system.console.app import run_app, start_app
from sample_order_system.console.state import AppState
from sample_order_system.domain.order import Order, OrderStatus
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


def test_start_app_loads_existing_files_into_state(tmp_path):
    sample_filepath = tmp_path / "samples.json"
    order_filepath = tmp_path / "orders.json"
    initial_state = AppState()
    initial_state.sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    run_app(
        initial_state,
        input_func=lambda prompt="": "0",
        output_func=lambda message: None,
        sample_filepath=sample_filepath,
        order_filepath=order_filepath,
    )
    inputs = iter(["1", "2", "0", "0"])
    outputs = []

    start_app(
        sample_filepath,
        order_filepath,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("Wafer-A" in message for message in outputs)


def test_start_app_starts_empty_when_files_missing(tmp_path):
    sample_filepath = tmp_path / "missing_samples.json"
    order_filepath = tmp_path / "missing_orders.json"
    inputs = iter(["0"])
    outputs = []

    start_app(
        sample_filepath,
        order_filepath,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("종료" in message for message in outputs)


def test_run_app_saves_production_queue_on_exit(tmp_path):
    state = AppState()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=5)
    order.status = OrderStatus.PRODUCING
    state.production_queue.enqueue(order)
    queue_filepath = tmp_path / "queue.json"
    inputs = iter(["0"])

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=lambda message: None,
        queue_filepath=queue_filepath,
    )

    assert queue_filepath.exists()


def test_start_app_loads_production_queue(tmp_path):
    sample_filepath = tmp_path / "samples.json"
    order_filepath = tmp_path / "orders.json"
    queue_filepath = tmp_path / "queue.json"
    initial_state = AppState()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=5)
    order.status = OrderStatus.PRODUCING
    initial_state.production_queue.enqueue(order)
    run_app(
        initial_state,
        input_func=lambda prompt="": "0",
        output_func=lambda message: None,
        sample_filepath=sample_filepath,
        order_filepath=order_filepath,
        queue_filepath=queue_filepath,
    )
    inputs = iter(["5", "0"])
    outputs = []

    start_app(
        sample_filepath,
        order_filepath,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
        queue_filepath=queue_filepath,
    )

    assert any("ACME Corp" in message for message in outputs)
