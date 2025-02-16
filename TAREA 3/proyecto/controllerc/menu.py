from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from configuracionc.app import App
from controllerc.function import IngestDataProducts
from controllerc.report import GenerateReportVentas

def menu(app: App):
    console = Console()
    while True:
        menu_text = Text()
        
        menu_text.append("\n💡 Proyecto Datux 2025💡 \n", style="underline bold magenta")
        menu_text.append("\n[1] 🟢 Ingresa tu Info⬆️\n", style="bold green")
        menu_text.append("[2] 📈 Mostrar reporte💸\n", style="bold yellow")
        menu_text.append("[3] ❌ ¿Deseas salir?🚨 \n", style="bold red")

        console.print(Panel(menu_text, title="➕ [bold red]Menú Principal[/bold red]➕", expand=False, border_style="green"))
        opcion = Prompt.ask("[bold blue]Selecciona una opción[/bold blue]", choices=["1", "2", "3"], default="3")
    
        if opcion == "1":
            IngestDataProducts(app)
            pass
        elif opcion == "2":           
            GenerateReportVentas(app)
            pass
        elif opcion == "3":
            pass
            break 
        else:
            print("Opcion no reconocida")