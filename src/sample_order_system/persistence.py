import json
from dataclasses import asdict
from pathlib import Path

from sample_order_system.domain.sample import SampleRegistry


def save_samples(sample_registry: SampleRegistry, filepath: Path) -> None:
    data = [asdict(sample) for sample in sample_registry.get_all()]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
