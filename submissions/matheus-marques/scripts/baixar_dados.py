"""Baixa os dois datasets públicos do challenge 002 direto do Kaggle (sem login).

Uso:  python scripts/baixar_dados.py
Saída: data/customer_support_tickets.csv e data/all_tickets_processed_improved_v3.csv
Os dados não vão para o git (data/ está no .gitignore).
"""
import io
import pathlib
import urllib.request
import zipfile

DATASETS = {
    "suraj520/customer-support-ticket-dataset": "customer_support_tickets.csv",
    "adisongoh/it-service-ticket-classification-dataset": "all_tickets_processed_improved_v3.csv",
}
DESTINO = pathlib.Path(__file__).resolve().parent.parent / "data"


def baixar(slug: str, esperado: str) -> None:
    alvo = DESTINO / esperado
    if alvo.exists():
        print(f"já existe: {alvo.name}")
        return
    url = f"https://www.kaggle.com/api/v1/datasets/download/{slug}"
    with urllib.request.urlopen(url) as resp:
        conteudo = resp.read()
    with zipfile.ZipFile(io.BytesIO(conteudo)) as z:
        z.extract(esperado, DESTINO)
    print(f"baixado: {alvo.name} ({alvo.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    DESTINO.mkdir(exist_ok=True)
    for slug, nome in DATASETS.items():
        baixar(slug, nome)
