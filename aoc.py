import typer
from pathlib import Path
import importlib.util

app = typer.Typer()

# Automatically register all day solutions
solutions_dir = Path(__file__).parent / "solutions"
for solution_file in solutions_dir.glob("day*.py"):
    day_name = solution_file.stem  # e.g., "day1"
    
    # Dynamically import the module
    spec = importlib.util.spec_from_file_location(day_name, solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Assume each day module has a `solve` function
    if hasattr(module, "solve"):
        app.command(name=day_name)(module.solve)


@app.command("hello")
def hello():
    print(f"hello")

if __name__ == "__main__":
    app()
