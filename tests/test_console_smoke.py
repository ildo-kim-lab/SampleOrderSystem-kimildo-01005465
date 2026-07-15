import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"


def run_console(input_text: str, cwd: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SRC_DIR)
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, "-m", "sample_order_system"],
        input=input_text,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=10,
    )


def test_console_smoke_generates_dummy_data_and_exits_cleanly(tmp_path):
    result = run_console("9\n1\n2\n0\n0\n", cwd=tmp_path)

    assert result.returncode == 0
    assert "더미 데이터 생성 완료" in result.stdout
    assert "Wafer-A" in result.stdout  # 1=시료관리, 2=조회로 실제 목록 확인
    assert "프로그램을 종료합니다" in result.stdout


def test_console_smoke_saves_persistence_files_on_exit(tmp_path):
    run_console("9\n0\n", cwd=tmp_path)

    assert (tmp_path / "samples.json").exists()
    assert (tmp_path / "orders.json").exists()
    assert (tmp_path / "queue.json").exists()


def test_console_smoke_full_order_flow_reflected_in_saved_state(tmp_path):
    # 9=더미 데이터, 2=주문메뉴, 1=접수(S-001/Customer1/5), 2=승인(1번 선택),
    # 0=주문메뉴에서 뒤로가기, 4=출고 처리(1번 선택), 0=종료
    inputs = "9\n2\n1\nS-001\nCustomer1\n5\n2\n1\n0\n4\n1\n0\n"

    result = run_console(inputs, cwd=tmp_path)

    assert result.returncode == 0
    assert "RELEASED" in result.stdout

    saved_orders = (tmp_path / "orders.json").read_text(encoding="utf-8")
    assert '"status": "RELEASED"' in saved_orders
