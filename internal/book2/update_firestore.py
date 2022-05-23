"""
command usage:
python3 internal/book2/update_firestore.py -key "../key_probml_gcp.json" -csv misc/figures_url_mapping_book2.csv -level1 figures -level2 book2 -level3 figures
python3 internal/book2/update_firestore.py -key "../key_probml_gcp.json" -csv misc/non_figures_url_mapping_book2.csv -level1 figures -level2 book2 -level3 figures
"""
from probml_utils.url_utils import upload_urls_to_firestore
import argparse

parser = argparse.ArgumentParser(description="update firestore")
parser.add_argument("-key", "--key", type=str, help="")
parser.add_argument("-csv", "--csv", type=str, help="")
parser.add_argument("-level1", "--level1", type=str, help="")
parser.add_argument("-level2", "--level2", type=str, help="")
parser.add_argument("-level3", "--level3", type=str, help="")


args = parser.parse_args()

# upload non-figure urls
upload_urls_to_firestore(
    args.key, args.csv, level1_collection=args.level1, level2_document=args.level2, level3_collection=args.level3
)