import markdown
import csv
import requests
from bs4 import BeautifulSoup

# Fonction pour analyser le contenu d'un fichier texte

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

# Fonction pour générer une page Markdown à partir des résultats
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

# Fonction pour générer un fichier CSV à partir des résultats
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

# Point d'entrée du programme
if __name__ == "__main__":
    # Emplacement du fichier texte déjà téléchargé localement
    local_file_path = "votre_fichier_texte.txt"

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


Étapes d'Utilisation
Téléchargement du Fichier Texte :

Assurez-vous que le fichier texte généré par TCPDump est téléchargé localement et accessible sur votre système.
Exécution du Script :

Ouvrez un terminal dans le répertoire où se trouve le script tcpdump_analyzer.py.
Exécutez le script en utilisant la commande suivante :

python tcpdump_analyzer.py

Analyse des Résultats :

Le script analysera le fichier texte, affichera les résultats dans la console, générera une page Markdown (results.md) et un fichier CSV (results.csv).
Visualisation dans Excel :

Ouvrez le fichier CSV (results.csv) avec un tableur tel qu'Excel pour effectuer des analyses supplémentaires.

Explorez les données, utilisez les filtres, créez des graphiques et personnalisez le tableur selon vos besoins.

Astuces et Conseils
Personnalisation : Vous pouvez adapter le script en ajoutant des fonctionnalités personnalisées pour répondre à des besoins spécifiques d'analyse de données.

Optimisation : En cas de grands fichiers texte, assurez-vous d'avoir suffisamment de ressources système pour une exécution optimale.
Enregistrement des Résultats

Tous les résultats générés, y compris la page Markdown et le fichier CSV, sont enregistrés dans le même répertoire que le script.



Notice Excel:

Ouvrez le fichier CSV (results.csv) avec Microsoft Excel.

Explorez les données :

Utilisez les filtres pour trier et filtrer les informations.
Créez des graphiques pour visualiser les tendances.
Appliquez des formules pour des analyses statistiques.
Comparez avec la Page Markdown :

Consultez la page Markdown pour des informations supplémentaires sur les résultats.
Documentez vos Observations :

Prenez des notes détaillées sur les observations et les tendances identifiées.
