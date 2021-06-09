
import csv
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "../data/test.csv").resolve()

print(file_path)