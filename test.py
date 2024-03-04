import json

def load_labelme_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def detect_piece_amounts(json_file):
    data = load_labelme_json(json_file)
    
    piece_amounts = {
        '2 euro': 2,
        '1 euro': 1,
        '50 centime': 0.50,
        '20 centime': 0.20,
        '10 centime': 0.10,
        '5 centime': 0.05,
        '2 centime': 0.02,
        '1 centime': 0.01,
    }

    total_amount = 0
    for shape in data['shapes']:
        label = shape['label']
        for key, value in piece_amounts.items():
            if key in label:
                total_amount += value

    print("Le montant total des pièces dans l'image est :", total_amount)

if __name__ == "__main__":
    json_file = 'fichier .json'
    detect_piece_amounts(json_file)
