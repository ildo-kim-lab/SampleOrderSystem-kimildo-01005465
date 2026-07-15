from pathlib import Path

from sample_order_system import __main__ as main_module


def test_main_calls_start_app_with_input_print_and_default_paths(monkeypatch):
    captured = {}

    def fake_start_app(
        sample_filepath, order_filepath, input_func, output_func, queue_filepath=None
    ):
        captured["sample_filepath"] = sample_filepath
        captured["order_filepath"] = order_filepath
        captured["queue_filepath"] = queue_filepath
        captured["input_func"] = input_func
        captured["output_func"] = output_func

    monkeypatch.setattr(main_module, "start_app", fake_start_app)

    main_module.main()

    assert captured["sample_filepath"] == Path("samples.json")
    assert captured["order_filepath"] == Path("orders.json")
    assert captured["queue_filepath"] == Path("queue.json")
    assert captured["input_func"] is input
    assert captured["output_func"] is print
