import json
import subprocess
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()

def run_gemini_prompt(prompt: str) -> str:
    """Runs a non-interactive gemini prompt and returns the response."""
    try:
        cmd = ["gemini", "-p", prompt, "-o", json]
        # We use -o json to get a clean response
        result = subprocess.run(
            ["gemini", "-p", prompt, "-o", "json"],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(result.stdout)
        return data.get("response", "").strip()
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error calling gemini CLI:[/bold red] {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError:
        console.print("[bold red]Error parsing gemini response as JSON.[/bold red]")
        sys.exit(1)

def get_skill_content(skill_name: str) -> str:
    """Reads the SKILL.md content for a given skill."""
    skill_path = os.path.join(".gemini", "skills", skill_name, "SKILL.md")
    if not os.path.exists(skill_path):
        console.print(f"[bold red]Skill file not found:[/bold red] {skill_path}")
        sys.exit(1)
    with open(skill_path, "r", encoding="utf-8") as f:
        return f.read()

def translate(text: str, skill_name: str) -> str:
    """Translates text using the specified skill."""
    skill_content = get_skill_content(skill_name)
    prompt = f"Follow these instructions to perform the task:\n\n{skill_content}\n\nInput:\n{text}"
    return run_gemini_prompt(prompt)

def compare_semantics(original: str, final: str) -> str:
    """Compares the original and final text using the comparison skill."""
    skill_content = get_skill_content("comparison")
    prompt = f"Follow these instructions to perform the task:\n\n{skill_content}\n\nOriginal:\n{original}\n\nFinal:\n{final}"
    return run_gemini_prompt(prompt)

def main():
    console.print(Panel.fit("[bold blue]Translation Chaining & Semantic Analysis[/bold blue]", border_style="blue"))
    
    # 1. Ask the user for an English sentence
    original_text = console.input("[bold green]Enter an English sentence to chain:[/bold green] ").strip()
    if not original_text:
        console.print("[yellow]No input provided. Exiting.[/yellow]")
        return

    results = []
    
    # 2. Run translation chaining
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        
        # English to French
        task1 = progress.add_task("Translating to French...", total=None)
        french_text = translate(original_text, "english_to_french")
        results.append(("French", french_text))
        progress.update(task1, completed=True)
        
        # French to Hebrew
        task2 = progress.add_task("Translating to Hebrew...", total=None)
        hebrew_text = translate(french_text, "french_to_hebrew")
        results.append(("Hebrew", hebrew_text))
        progress.update(task2, completed=True)
        
        # Hebrew to English
        task3 = progress.add_task("Translating back to English...", total=None)
        final_text = translate(hebrew_text, "hebrew_to_english")
        results.append(("Final English", final_text))
        progress.update(task3, completed=True)
        
        # 4. Run semantic comparison
        task4 = progress.add_task("Performing semantic comparison...", total=None)
        comparison_analysis = compare_semantics(original_text, final_text)
        progress.update(task4, completed=True)

    # 3. Print all intermediate translations
    table = Table(title="Translation Chain Results", show_header=True, header_style="bold magenta")
    table.add_column("Stage", style="dim", width=15)
    table.add_column("Text")
    
    table.add_row("Original", original_text)
    for stage, text in results:
        table.add_row(stage, text)
    
    console.print(table)
    
    # 5. Print similarity score and meaning drift analysis
    console.print("\n")
    console.print(Panel(comparison_analysis, title="[bold cyan]Semantic Comparison Analysis[/bold cyan]", border_style="cyan"))

if __name__ == "__main__":
    main()
