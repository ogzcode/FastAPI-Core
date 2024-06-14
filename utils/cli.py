import typer
import subprocess

app = typer.Typer()

@app.command()
def create_migration(message: str):
    """Yeni bir Alembic migrasyonu oluştur."""
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", message])
    typer.echo(f"Migrasyon oluşturuldu: {message}")

@app.command()
def upgrade():
    """Tüm Alembic migrasyonlarını uygula."""
    subprocess.run(["alembic", "upgrade", "head"])
    typer.echo("Tüm migrasyonlar uygulandı.")

@app.command()
def downgrade(revision: str):
    """Belirtilen Alembic migrasyonuna geri dön."""
    subprocess.run(["alembic", "downgrade", revision])
    typer.echo(f"Downgrade yapıldı: {revision}")

@app.command()
def history():
    """Tüm Alembic revizyonlarını listele."""
    subprocess.run(["alembic", "history"])
    typer.echo("Tüm revizyonlar listelendi.")


if __name__ == "__main__":
    app()
