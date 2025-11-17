plant_diseases = {
    "Tomato": ["Late Blight", "Early Blight", "Leaf Spot"],
    "Potato": ["Late Blight", "Scab", "Black Scurf"],
    "Wheat": ["Rust", "Powdery Mildew", "Leaf Blight"],
    "Rice": ["Bacterial Leaf Blight", "Sheath Blight", "Blast"],
    "Mango": ["Powdery Mildew", "Anthracnose", "Dieback"],
    "Banana": ["Panama Disease", "Black Sigatoka", "Bunchy Top Virus"],
    "Apple": ["Apple Scab", "Powdery Mildew", "Fire Blight"],
    "Grapes": ["Downy Mildew", "Powdery Mildew", "Botrytis Rot"],
    "Orange": ["Citrus Canker", "Greening Disease", "Melanose"],
    "Strawberry": ["Leaf Spot", "Powdery Mildew", "Verticillium Wilt"],
    "Cabbage": ["Black Rot", "Clubroot", "Downy Mildew"],
    "Cauliflower": ["Black Rot", "Downy Mildew", "Clubroot"],
    "Chili": ["Leaf Curl", "Anthracnose", "Powdery Mildew"],
    "Cotton": ["Wilt", "Leaf Curl", "Anthracnose"],
    "Coraan": ["Leaf Blight", "Rust", "Smut"],
    "Sunflower": ["Downy Mildew", "Rust", "Head Rot"],
    "Pea": ["Powdery Mildew", "Downy Mildew", "Rust"],
    "Soybean": ["Rust", "Brown Spot", "Bacterial Blight"],
    "Papaya": ["Ring Spot Virus", "Powdery Mildew", "Anthracnose"],
    "Rose": ["Black Spot", "Powdery Mildew", "Rust"]
}

while True:
    print("\n🌿======================================🌿")
    print("        PLANT DISEASE IDENTIFIER")
    print("🌿======================================🌿")

    
    print("\nAvailable Plants:")
    for plant in plant_diseases.keys():
        print("-", plant)

    
    plant_name = input("\nEnter the plant name (or type 'exit' to quit): ").strip().title()

    
    if plant_name.lower() == "exit":
        print("\nThank you for using the Plant Disease Identifier 🌱")
        break

    if plant_name in plant_diseases:
        print(f"\nCommon Diseases Found in {plant_name}:")
        for i, disease in enumerate(plant_diseases[plant_name], start=1):
            print(f"{i}. {disease}")
    else:
        print("\nSorry, the plant is not in our database.")
        print("Please check the spelling or try another plant name.")
r