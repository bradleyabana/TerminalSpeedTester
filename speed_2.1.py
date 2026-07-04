#!/usr/bin/env python3

from rich.console import Console
from rich.panel import Panel
import speedtest

console = Console()

console.rule("[bold cyan]⚡ Internet Speed Test")

# Find the best server
with console.status("[bold green]Finding the best server...", spinner="dots"):
    st = speedtest.Speedtest()
    st.get_best_server()

# Test download speed
with console.status("[bold green]Testing download speed...", spinner="dots"):
    download = st.download() / 1_000_000  # Convert to Mbps

# Test upload speed
with console.status("[bold green]Testing upload speed...", spinner="dots"):
    upload = st.upload() / 1_000_000  # Convert to Mbps

ping = st.results.ping
server = st.results.server["name"]
country = st.results.server["country"]
sponsor = st.results.server["sponsor"]

result = f"""
[bold green]Download:[/] {download:.2f} Mbps
[bold blue]Upload:[/]   {upload:.2f} Mbps
[bold yellow]Ping:[/]     {ping:.1f} ms

[bold cyan]Server:[/] {server}, {country}
[bold magenta]Host:[/] {sponsor}
"""

console.print(
    Panel(
        result,
        title="[bold white]Results",
        border_style="cyan",
        expand=False
    )
)

if download >= 100:
    console.print("\n[bold green]✓ Excellent connection! 🚀[/]")
elif download > 30:
    console.print("\n[bold yellow]✓ Good connection! 👍[/]")
elif download == 0:
    console.print("\n[bold red] No internet")
else:
    console.print("\n[bold red]⚠ Slow connection.[/]")

