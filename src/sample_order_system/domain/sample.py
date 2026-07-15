from dataclasses import dataclass


@dataclass
class Sample:
    sample_id: str
    name: str
    avg_production_time: float
    yield_rate: float


class SampleRegistry:
    def __init__(self) -> None:
        self._samples: list[Sample] = []

    def register(self, sample: Sample) -> None:
        self._samples.append(sample)

    def get_all(self) -> list[Sample]:
        return list(self._samples)
