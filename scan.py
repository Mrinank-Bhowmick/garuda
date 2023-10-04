import sys
import socket
import threading
import time
from cli import Output
from rich.table import Table

k = 0

output = Output()
# Initialize a ports list to store all the open ports
# Add a table to display the open ports
table = Table(title="Open Ports", show_header=True, header_style="bold magenta")
table.add_column("Port", style="cyan", justify="center")
table.add_column("Service", style="green", justify="center")
table.add_column("URL", style="yellow", justify="center")


def scanner():
    output.show_panel(
        title="",
        content="[green]EFFLUX[/green] Eagle [underline]port scanner[/underline]",
        color="green",
    )
    try:
        tar = output.ask("Enter an IP Address", color="green")
        output.log("Trying to resolve host name")
        target = socket.gethostbyname(
            tar
        )  # host name given will resolve to corresponding ip address from dns
    except socket.gaierror:
        output.c_print("\nName [underline]resolution[/underline] error", code="danger")
        output.c_print("Exiting...", code="info")
        sys.exit()
    start_port = int(output.ask("[blue]Start[/blue] Port"))
    end_port = int(output.ask("[yellow]END[/yellow] Port"))
    startTime = time.time()
    output.log(f"Scanning ports from {start_port} to {end_port} for {target}")

    def scan(port):
        global k
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp
        p.settimeout(5)
        connection = p.connect_ex((target, port))

        lock = threading.Lock()

        if not (connection):
            try:
                serviceName = socket.getservbyport(port, "tcp")
                with lock:
                    table.add_row(str(port), serviceName, f"http://{target}:{port}")
                    k += 1
            except:
                k += 1
                output.c_print(f"Error at {port}, skipping")
        if port == end_port:
            if k != 0:
                output.c_print(
                    f"Eagle Scanning was [green]successful[/green], [underline]{k} Ports[/underline] are open"
                )
                print("\n")
                output.c_print(table)
                print("\n")
            elif k == 0:
                output.c_print(f"Unfortunately [red]no ports[/red] were open :(")
            output.c_print(
                f"Time taken: [underline]{ str(time.time() - startTime)[:4] }[/underline] sec",
                code="info",
            )
            output.c_print("Thanks for using 🦅[blue]EFFLUX[/blue]")

        p.close()

    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan, args=(port,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    exit()
