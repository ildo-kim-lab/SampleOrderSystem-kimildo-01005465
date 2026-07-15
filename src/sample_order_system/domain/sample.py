from dataclasses import dataclass


@dataclass
class Sample:
    sample_id: str
    name: str
    avg_production_time: float
    yield_rate: float
    stock: int = 0

    def decrease_stock(self, quantity: int) -> None:
        self.stock -= quantity

    def increase_stock(self, quantity: int) -> None:
        self.stock += quantity


class SampleRegistry:
    def __init__(self) -> None:
        self._samples: list[Sample] = []

    def register(self, sample: Sample) -> None:
        if self.find_by_id(sample.sample_id) is not None:
            raise ValueError(f"이미 등록된 시료 ID입니다: {sample.sample_id}")
        self._samples.append(sample)

    def get_all(self) -> list[Sample]:
        return list(self._samples)

    def find_by_id(self, sample_id: str) -> Sample | None:
        for sample in self._samples:
            if sample.sample_id == sample_id:
                return sample
        return None
