import typer
import requests

app = typer.Typer(help="CVE Vulnerability Lookup")

@app.command()
def latest(vendor: str = "", limit: int = 5):
    """Fetch latest CVEs"""
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {"resultsPerPage": limit}
    if vendor:
        params["keywordSearch"] = vendor
    
    resp = requests.get(url, params=params)
    data = resp.json()
    for item in data.get("vulnerabilities", []):
        cve_id = item["cve"]["id"]
        desc = item["cve"]["descriptions"][0]["value"]
        typer.echo(f"{cve_id}: {desc}")
