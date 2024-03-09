import typer
import rag_app.query as QueryApp
import rag_app.ingest as IngestApp

app = typer.Typer(
    name="Rag-App",
    help="A CLI for querying a local RAG application backed by LanceDB",
)

app.add_typer(
    QueryApp.app,
    name="query",
    help="Commands to help query your local lancedb instance",
)
app.add_typer(
    IngestApp.app,
    name="ingest",
    help="Commands to help ingest data into your local lancedb instance",
)
