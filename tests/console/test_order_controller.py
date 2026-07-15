import pytest

from sample_order_system.console.order_controller import (
    approve_order_console,
    create_order,
    reject_order_console,
)
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import Sample, SampleRegistry


def _sample_registry_with_one_sample() -> SampleRegistry:
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
        )
    )
    return registry


def test_create_order_adds_reserved_order_for_selected_sample():
    order_registry = OrderRegistry()
    sample_registry = _sample_registry_with_one_sample()
    inputs = iter(["1", "ACME Corp", "10"])
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    orders = order_registry.get_all()
    assert len(orders) == 1
    assert orders[0].sample_id == "S-001"
    assert orders[0].customer_name == "ACME Corp"
    assert orders[0].quantity == 10
    assert orders[0].status == OrderStatus.RESERVED


def test_create_order_lists_samples_with_index_before_prompting():
    order_registry = OrderRegistry()
    sample_registry = _sample_registry_with_one_sample()
    inputs = iter(["1", "ACME Corp", "10"])
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("1. S-001" in message for message in outputs)


def test_create_order_reports_message_and_aborts_when_no_samples_registered():
    order_registry = OrderRegistry()
    sample_registry = SampleRegistry()
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": (_ for _ in ()).throw(AssertionError("input requested")),
        output_func=outputs.append,
    )

    assert any("등록된 시료가 없습니다" in message for message in outputs)
    assert order_registry.get_all() == []


def test_create_order_reports_friendly_message_on_out_of_range_sample_index():
    order_registry = OrderRegistry()
    sample_registry = _sample_registry_with_one_sample()
    inputs = iter(["99"])
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("잘못된 번호" in message for message in outputs)
    assert order_registry.get_all() == []


def test_create_order_reports_friendly_message_on_non_numeric_quantity():
    order_registry = OrderRegistry()
    sample_registry = _sample_registry_with_one_sample()
    inputs = iter(["1", "abc"])
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("숫자" in message for message in outputs)
    assert order_registry.get_all() == []


def test_create_order_does_not_prompt_for_customer_name_when_quantity_invalid():
    order_registry = OrderRegistry()
    sample_registry = _sample_registry_with_one_sample()
    # 시료 선택("1") 다음 수량이 잘못되면("abc"), 고객명 입력을 요구하지
    # 않고 실패해야 한다 - 두 번째 입력 이후 더 이상 input_func가 호출되지
    # 않는지 확인한다 (호출되면 StopIteration으로 실패).
    inputs = iter(["1", "abc"])
    outputs = []

    create_order(
        order_registry,
        sample_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    with pytest.raises(StopIteration):
        next(inputs)


def test_approve_order_console_confirms_when_stock_is_sufficient():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    outputs = []

    approve_order_console(
        order, sample_registry, ProductionQueue(), output_func=outputs.append
    )

    assert order.status == OrderStatus.CONFIRMED
    assert any("CONFIRMED" in message for message in outputs)


def test_reject_order_console_rejects_and_reports_result():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    outputs = []

    reject_order_console(order, output_func=outputs.append)

    assert order.status == OrderStatus.REJECTED
    assert any("REJECTED" in message for message in outputs)
