import pandas as pd

file_path: 'C:\temp_cours'

def analyze_sales_data(file_path):
    # Lire les données à partir d'un fichier CSV
    data = pd.read_csv(file_path)
    
    # Calculer les statistiques
    total_sales = data['Sales'].sum()
    average_sales = data['Sales'].mean()
    max_sales = data['Sales'].max()
    min_sales = data['Sales'].min()

    # Afficher les statistiques
    print(f"Total des ventes: {total_sales}")
    print(f"Vente moyenne: {average_sales}")
    print(f"Ventes maximales: {max_sales}")
    print(f"Ventes minimales: {min_sales}")
#Essai 1 avec pipeline CI/cd
if __name__ == "__main__":
    file_path = 'sales_data.csv'  # Chemin vers le fichier CSV
    analyze_sales_data(file_path)

