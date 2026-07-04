#!/usr/ben/env python3
import speedtest
from rich.console import Console
from rich.panel import Panel

console = Console()

console.rule("[bold cyan]⚡ Internet Speed Test")

st = speedtest.Speedtest()

with console.status("[bold green]Finding the best server...", spinner="dots"):
    st.get_best_server()

with console.status("[bold green]Testing download...", spinner="dots"):
    download = st.download() / 1_000_000

# Test upload speed
with console.status("[bold green]Testing upload speed...", spinner="dots"):
    upload = st.upload() / 1_000_000

ping = st.results.ping

console.print(
    Panel(
        f"""
[green]Download:[/] {download:.2f} Mbps
[blue]Upload:[/] {upload:.2f} Mbps
[yellow]Ping:[/] {ping:.1f} ms
""",
        title="Results",
        border_style="cyan"
    )
)