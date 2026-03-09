import typer
import requests
from reconciliation.engine import ReconciliationEngine

app = typer.Typer()
recon = ReconciliationEngine()

@app.command()
def create(service: str, file: str):
    data = open(file).read()
    requests.post(f"http://localhost:8000/services/{service}", json=data)

@app.command()
def check_sync(device: str):
    print("Checking sync...")

@app.command()
def sync_from(device: str):
    print("Pulling config from device")

@app.command()
def reconcile(device: str = None):
    if device:
        recon.reconcile_device(device)
    else:
        recon.reconcile_all()

if __name__ == "__main__":
    app()
