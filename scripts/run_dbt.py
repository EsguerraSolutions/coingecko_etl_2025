from pathlib import Path
import subprocess

def run_dbt():

    current_file = Path(__file__).resolve()
    project_root = current_file.parents[1]
    dbt_dir = project_root / "dbt"

    cmd = ["dbt", "run", "--project-dir", str(dbt_dir)]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    run_dbt()