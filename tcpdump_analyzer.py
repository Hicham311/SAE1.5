import markdown
import csv
import requests
from bs4 import BeautifulSoup

def analyze_text_file(file_path):
    try:
        # Lire le fichier texte
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        # Ajoutez ici la logique pour analyser le contenu du fichier texte
        # Exemple : results = your_custom_function(text_content)
        results = [line for line in text_content.split('\n') if line]  # Exemple basique

        return results

    except Exception as e:
        print(f"Erreur lors de l'analyse du fichier : {e}")
        return None

def generate_markdown(results):
    try:
        # Générer la page Markdown
        markdown_content = "# Résultats de l'Analyse\n\n"
        for result in results:
            markdown_content += f"- {result}\n"

        # Enregistrer la page Markdown dans un fichier
        with open('results.md', 'w', encoding='utf-8') as markdown_file:
            markdown_file.write(markdown_content)

        print("Page Markdown générée avec succès : results.md")
        return True
    except Exception as e:
        print(f"Erreur lors de la génération de la page Markdown : {e}")
        return False

def generate_csv(results):
    try:
        # Générer le fichier CSV
        csv_header = ["Résultat"]
        csv_rows = [[result] for result in results]

        with open('results.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_header)
            csv_writer.writerows(csv_rows)

        print("Fichier CSV généré avec succès : results.csv")
        return True
    except Exception as e:
        print(f"Erreur lors de la génération du fichier CSV : {e}")
        return False

if __name__ == "__main__":
    # Emplacement du fichier texte déjà téléchargé localement
    local_file_path = "test.txt"

    # Analyser le fichier texte
    results = analyze_text_file(local_file_path)

    if results:
        # Afficher les résultats dans la console
        for result in results:
            print(result)

        # Générer la page Markdown
        generate_markdown(results)

        # Générer le fichier CSV
        generate_csv(results)
    else:
        print("Aucun résultat à afficher.")
