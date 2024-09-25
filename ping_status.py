#!/usr/bin/env python3
import subprocess
from termcolor import colored
from tqdm import tqdm  # Barre de progression
import argparse  # Gestion des arguments de ligne de commande

def ping(target):
    try:
        command = ['ping', '-c', '1', target]
        result = subprocess.check_output(command, stderr=subprocess.DEVNULL, text=True)
        return True  # Retourne True si le ping réussit
    except subprocess.CalledProcessError:
        return False  # Retourne False si le ping échoue
    except subprocess.SubprocessError:
        return False  # Capture d'autres erreurs possibles

def afficher_tableau(ips_up, ips_down):
    column_width = 20
    print("\n")
    print(f"{'UP':<{column_width}} | {'DOWN':<{column_width}}")
    print('-' * (column_width * 2 + 3))

    max_len = max(len(ips_up), len(ips_down))

    for i in range(max_len):
        up = ips_up[i] if i < len(ips_up) else ""
        down = ips_down[i] if i < len(ips_down) else ""

        up_colored = colored(f"{up:<{column_width}}", 'green') if up else " " * column_width
        down_colored = colored(f"{down:<{column_width}}", 'red') if down else " " * column_width

        print(f"{up_colored} | {down_colored}")
    
    print('-' * (column_width * 2 + 3))

def main():
    # Initialisation de argparse pour les arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Script de ping pour vérifier les adresses IP.")
    
    # Ajout d'un seul argument obligatoire : le fichier contenant les adresses IP
    parser.add_argument('file', type=str, help="Chemin vers le fichier contenant les adresses IP")

    # Récupération des arguments
    args = parser.parse_args()

    ips_up = []
    ips_down = []

    # Lire les IPs du fichier donné en argument
    with open(args.file, 'r') as file:
        ip_list = [line.strip() for line in file]

    # Ajouter une barre de progression
    for ip in tqdm(ip_list, desc="Pinging IPs", unit="ip"):
        if ping(ip):
            ips_up.append(ip)
        else:
            ips_down.append(ip)

    # Afficher le tableau à la fin
    afficher_tableau(ips_up, ips_down)

if __name__ == "__main__":
    main()

