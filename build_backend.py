"""Minimal local PEP 517/660 build backend for pi_lab.

The repository is intentionally lightweight and avoids requiring network access
just to perform ``pip install -e .`` in constrained environments.
"""

from __future__ import annotations

import base64
import csv
import hashlib
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
PROJECT = {
    "name": "pi-lab",
    "version": "0.1.0",
    "description": "Finite pi digit generation, search, and frequency exploration tools.",
    "requires-python": ">=3.10",
    "dependencies": ["flask", "matplotlib", "mpmath"],
}


def _project_metadata() -> dict:
    return PROJECT


def _dist_name(name: str) -> str:
    return name.replace("-", "_")


def _dist_info_name() -> str:
    project = _project_metadata()
    return f"{_dist_name(project['name'])}-{project['version']}.dist-info"


def _metadata_text() -> str:
    project = _project_metadata()
    lines = [
        "Metadata-Version: 2.3",
        f"Name: {project['name']}",
        f"Version: {project['version']}",
        f"Summary: {project.get('description', '')}",
        f"Requires-Python: {project.get('requires-python', '')}",
    ]
    for dependency in project.get("dependencies", []):
        lines.append(f"Requires-Dist: {dependency}")
    return "\n".join(lines) + "\n"


def _wheel_text() -> str:
    return "\n".join(
        [
            "Wheel-Version: 1.0",
            "Generator: pi_lab.local_build_backend",
            "Root-Is-Purelib: true",
            "Tag: py3-none-any",
            "",
        ]
    )


def _entry_points_text() -> str:
    return "\n".join(["[console_scripts]", "pi-lab = pi_lab.cli:main", ""])


def _write_metadata_dir(path: Path) -> Path:
    dist_info = path / _dist_info_name()
    dist_info.mkdir(parents=True, exist_ok=True)
    (dist_info / "METADATA").write_text(_metadata_text(), encoding="utf-8")
    (dist_info / "WHEEL").write_text(_wheel_text(), encoding="utf-8")
    (dist_info / "entry_points.txt").write_text(_entry_points_text(), encoding="utf-8")
    return dist_info


def prepare_metadata_for_build_wheel(metadata_directory: str, config_settings=None) -> str:
    _write_metadata_dir(Path(metadata_directory))
    return _dist_info_name()


def prepare_metadata_for_build_editable(metadata_directory: str, config_settings=None) -> str:
    return prepare_metadata_for_build_wheel(metadata_directory, config_settings)


def _hash_bytes(data: bytes) -> tuple[str, str]:
    digest = hashlib.sha256(data).digest()
    encoded = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"sha256={encoded}", str(len(data))


def _write_record(wheel: zipfile.ZipFile, records: list[tuple[str, bytes]]) -> None:
    record_path = f"{_dist_info_name()}/RECORD"
    rows = []
    for arcname, data in records:
        digest, size = _hash_bytes(data)
        rows.append([arcname, digest, size])
    rows.append([record_path, "", ""])

    from io import StringIO

    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerows(rows)
    wheel.writestr(record_path, output.getvalue())


def _add_bytes(wheel: zipfile.ZipFile, records: list[tuple[str, bytes]], arcname: str, data: bytes) -> None:
    wheel.writestr(arcname, data)
    records.append((arcname, data))


def _wheel_filename() -> str:
    project = _project_metadata()
    return f"{_dist_name(project['name'])}-{project['version']}-py3-none-any.whl"


def build_editable(wheel_directory: str, config_settings=None, metadata_directory: str | None = None) -> str:
    wheel_name = _wheel_filename()
    wheel_path = Path(wheel_directory) / wheel_name
    records: list[tuple[str, bytes]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as wheel:
        _add_bytes(wheel, records, "pi_lab_editable.pth", f"{ROOT}\n".encode("utf-8"))
        _add_bytes(wheel, records, f"{_dist_info_name()}/METADATA", _metadata_text().encode("utf-8"))
        _add_bytes(wheel, records, f"{_dist_info_name()}/WHEEL", _wheel_text().encode("utf-8"))
        _add_bytes(wheel, records, f"{_dist_info_name()}/entry_points.txt", _entry_points_text().encode("utf-8"))
        _write_record(wheel, records)
    return wheel_name


def build_wheel(wheel_directory: str, config_settings=None, metadata_directory: str | None = None) -> str:
    wheel_name = _wheel_filename()
    wheel_path = Path(wheel_directory) / wheel_name
    records: list[tuple[str, bytes]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as wheel:
        for path in (ROOT / "pi_lab").rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts:
                arcname = path.relative_to(ROOT).as_posix()
                data = path.read_bytes()
                _add_bytes(wheel, records, arcname, data)
        _add_bytes(wheel, records, f"{_dist_info_name()}/METADATA", _metadata_text().encode("utf-8"))
        _add_bytes(wheel, records, f"{_dist_info_name()}/WHEEL", _wheel_text().encode("utf-8"))
        _add_bytes(wheel, records, f"{_dist_info_name()}/entry_points.txt", _entry_points_text().encode("utf-8"))
        _write_record(wheel, records)
    return wheel_name


def build_sdist(sdist_directory: str, config_settings=None) -> str:
    project = _project_metadata()
    base = f"{project['name']}-{project['version']}"
    output = Path(sdist_directory) / f"{base}.tar.gz"
    shutil.make_archive(str(output.with_suffix("").with_suffix("")), "gztar", ROOT, dry_run=False)
    return output.name
