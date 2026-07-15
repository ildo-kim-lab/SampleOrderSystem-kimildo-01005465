from typing import Callable

from sample_order_system.domain.sample import Sample, SampleRegistry


def register_sample(
    registry: SampleRegistry,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    sample_id = input_func("시료 ID: ")
    name = input_func("이름: ")
    avg_production_time = float(input_func("평균 생산시간: "))
    yield_rate = float(input_func("수율: "))

    sample = Sample(
        sample_id=sample_id,
        name=name,
        avg_production_time=avg_production_time,
        yield_rate=yield_rate,
    )
    registry.register(sample)
    output_func(f"{name} 등록 완료")
