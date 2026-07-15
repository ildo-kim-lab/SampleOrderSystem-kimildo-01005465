import json

from sample_order_system.domain.sample import Sample, SampleRegistry
from sample_order_system.persistence import load_samples, save_samples


def test_save_samples_writes_json_file(tmp_path):
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    filepath = tmp_path / "samples.json"

    save_samples(registry, filepath)

    saved = json.loads(filepath.read_text(encoding="utf-8"))
    assert saved == [
        {
            "sample_id": "S-001",
            "name": "Wafer-A",
            "avg_production_time": 2.5,
            "yield_rate": 0.9,
            "stock": 10,
        }
    ]


def test_load_samples_restores_registry_from_json_file(tmp_path):
    original = SampleRegistry()
    original.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    filepath = tmp_path / "samples.json"
    save_samples(original, filepath)

    restored = load_samples(filepath)

    sample = restored.find_by_id("S-001")
    assert sample is not None
    assert sample.name == "Wafer-A"
    assert sample.avg_production_time == 2.5
    assert sample.yield_rate == 0.9
    assert sample.stock == 10
