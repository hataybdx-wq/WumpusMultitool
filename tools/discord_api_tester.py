import requests
import time
import statistics
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from colorama import init

init(autoreset=True)

console = Console()

# APIs Discord à tester
ENDPOINTS = {
    "Gateway": "https://gateway.discord.gg",
    "API Base": "https://discord.com/api/v10",
    "CDN": "https://cdn.discordapp.com",
    "Status": "https://status.discord.com/api/v2/status.json",
    "Media": "https://media.discordapp.net",
}

# Historique des pings
history = {name: [] for name in ENDPOINTS}


def get_ping(url):
    try:
        start = time.perf_counter()

        requests.get(url, timeout=5)

        end = time.perf_counter()

        latency = round((end - start) * 1000, 2)

        return latency

    except:
        return None


def get_color(ping):

    if ping is None:
        return "red"

    if ping < 100:
        return "green"

    elif ping < 250:
        return "yellow"

    else:
        return "red"


def get_status(ping):

    if ping is None:
        return "[red]DOWN[/red]"

    if ping < 100:
        return "[green]ONLINE[/green]"

    elif ping < 250:
        return "[yellow]SLOW[/yellow]"

    else:
        return "[red]HIGH LATENCY[/red]"


def startup_tests():

    console.print("\n[bold cyan]Vérification du script...[/bold cyan]\n")

    tests = [
        ("Test connexion Gateway", ENDPOINTS["Gateway"]),
        ("Test API Base", ENDPOINTS["API Base"]),
        ("Test CDN", ENDPOINTS["CDN"]),
    ]

    success = 0

    for name, url in tests:

        console.print(f"[yellow]→ {name}...[/yellow]", end=" ")

        ping = get_ping(url)

        if ping is not None:
            console.print(f"[green]OK[/green] ({ping} ms)")
            success += 1

        else:
            console.print("[red]FAILED[/red]")

    console.print(
        f"\n[bold green]{success}/{len(tests)} tests réussis[/bold green]\n"
    )

    if success == 0:
        console.print("[bold red]Aucune API Discord répond.[/bold red]")
        exit()

    time.sleep(2)


def status_demo():

    console.print("\n[bold magenta]Test des statuts visuels...[/bold magenta]\n")

    demo_table = Table(title="Status System Test")

    demo_table.add_column("API", style="cyan")
    demo_table.add_column("Ping")
    demo_table.add_column("Status")
    demo_table.add_column("Load")

    demos = [
        ("Gateway", 45, "ONLINE", "green"),
        ("API Base", 180, "SLOW", "yellow"),
        ("CDN", None, "DOWN", "red"),
    ]

    for name, ping, status_text, color in demos:

        if ping is None:

            ping_text = "[red]Timeout[/red]"
            bars = "[red]████████████████████[/red]"

        else:

            ping_text = f"[{color}]{ping} ms[/{color}]"

            bar_count = min(int(ping / 20), 20)

            bars = (
                f"[{color}]"
                + ("█" * bar_count)
                + ("░" * (20 - bar_count))
                + f"[/{color}]"
            )

        status = f"[{color}]{status_text}[/{color}]"

        demo_table.add_row(
            name,
            ping_text,
            status,
            bars
        )

    console.print(demo_table)

    console.print(
        "\n[bold green]Test des couleurs et statuts terminé.[/bold green]\n"
    )

    time.sleep(4)


def build_table():

    table = Table(title="Discord API Latency Monitor")

    table.add_column("API", style="cyan", no_wrap=True)
    table.add_column("Current", justify="center")
    table.add_column("Min", justify="center")
    table.add_column("Max", justify="center")
    table.add_column("Average", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Load", justify="center")

    for name, url in ENDPOINTS.items():

        ping = get_ping(url)

        if ping is not None:
            history[name].append(ping)

        values = history[name]

        min_ping = round(min(values), 2) if values else 0
        max_ping = round(max(values), 2) if values else 0
        avg_ping = round(statistics.mean(values), 2) if values else 0

        color = get_color(ping)
        status = get_status(ping)

        current_text = (
            f"[{color}]{ping} ms[/{color}]"
            if ping is not None
            else "[red]Timeout[/red]"
        )

        # Barre de progression
        if ping is None:

            bars = "████████████████████"
            bar_color = "red"

        else:

            bar_count = min(int(ping / 20), 20)

            bars = (
                "█" * bar_count
                + "░" * (20 - bar_count)
            )

            bar_color = color

        table.add_row(
            name,
            current_text,
            f"{min_ping} ms",
            f"{max_ping} ms",
            f"{avg_ping} ms",
            status,
            f"[{bar_color}]{bars}[/{bar_color}]",
        )

    return table


def main():

    startup_tests()

    status_demo()

    console.print(
        "[bold green]Lancement du monitoring Discord...[/bold green]\n"
    )

    with Live(refresh_per_second=1) as live:

        while True:

            live.update(
                Panel(
                    build_table(),
                    title="[bold blue]Discord Network Monitor[/bold blue]",
                    border_style="blue",
                )
            )

            time.sleep(2)


if __name__ == "__main__":
    main()