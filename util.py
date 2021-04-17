import tensorflow as tf
import numpy as np
import util

model = None
output_class = ["Alpinia Galanga (Rasna)", "Amaranthus Viridis (Arive-Dantu)", "Artocarpus Heterophyllus (Jackfruit)", 
                "Azadirachta Indica (Neem)", "Basella Alba (Basale)", "Brassica Juncea (Indian Mustard)", "Carissa Carandas (Karanda)",
                "Citrus Limon (Lemon)", "Ficus Auriculata (Roxburgh fig)","Ficus Religiosa (Peepal Tree)","Hibiscus Rosa-sinensis",
                "Jasminum (Jasmine)","Mangifera Indica (Mango)","Mentha (Mint)","Moringa Oleifera (Drumstick)","Muntingia Calabura (Jamaica Cherry-Gasagase)",
                "Murraya Koenigii (Curry)","Nerium Oleander (Oleander)","Nyctanthes Arbor-tristis (Parijata)","Ocimum Tenuiflorum (Tulsi)","Piper Betle (Betel)",
                "Plectranthus Amboinicus (Mexican Mint)","Pongamia Pinnata (Indian Beech)","Psidium Guajava (Guava)","Punica Granatum (Pomegranate)",
                "Santalum Album (Sandalwood)","Syzygium Cumini (Jamun)","Syzygium Jambos (Rose Apple)","Tabernaemontana Divaricata (Crape Jasmine)",
                "Trigonella Foenum-graecum (Fenugreek)"]


data = {
"Alpinia Galanga (Rasna)":
	["<p style='font-family:Arial, Helvetica, sans-serif;'> <strong > Botanical Name :</strong>   Pluchea lanceolata,Alpinia Galanga <br/> <strong> Common Name :</strong>   Rasana <br/> <strong>Kingdom: </strong>   Plantae <br/> <strong>SubKingdom:</strong> Tracheobionta <br/><strong> Division:  </strong>  Magnoliophyta – Flowering plants <br/><strong>Class: </strong> Magnoliopsida <br/><strong> Subclass: </strong>  Asteridae <br/><strong> Order:</strong>  Asterales<strong> <br/> Family:</strong> Asteraceae <br/><strong> Genus:</strong>  Pluchea <br/><strong> Species: </strong>   lanceolata <br/> <strong>Part used:</strong>  Whole plant, leaves. <br/> <strong>Medicinal Properties:</strong>   Leaves: aperients, laxative, analgesic and antipyretic. <br/> <strong>Medicinal Use:</strong>  	Plant is useful in constipation and respiratory diseases. The decoction of the plant has been used traditionally in arthritis.</p>"],

"Amaranthus Viridis (Arive-Dantu)":
	["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Amaranthus Viridis<br/> <strong> Common Name :</strong>   Arive-Dantu <br/> <strong>Kingdom: </strong>   Plantae <br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/>"
     "<strong> Division:  </strong>  Magnoliophyta – Flowering plants<br/><strong>Class: </strong> Magnoliopsida – Dicotyledons <br/><strong> Subclass: </strong>  Caryophyllidae <br/><strong> Order:</strong>  Caryophyllales"
     "<strong> <br/> Family:</strong> Amaranthaceae <br/><strong> Genus:</strong>   Amaranthus L. – pigweed <br/><strong> Species: </strong>    Amaranthus viridis L. – slender amaranth <br/> <strong>Part used:</strong>  leaves, seeds, roots and entire plant<br/> "
     "<strong>Medicinal Properties:</strong>   anti-microbial"
     " <br/> <strong>Medicinal Use:</strong>  Amaranthus viridis is used as traditional medicine in treatment of fever, pain, asthma, diabetes, dysentery, urinary disorders, liver disorders, eye disorders and venereal diseases."],

"Artocarpus Heterophyllus (Jackfruit)":
["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Artocarpus Heterophyllus<br/> <strong> Common Name :</strong>   Jackfruit <br/> <strong>Kingdom: </strong>    Plantae – Plants <br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
     "Division:  </strong> Magnoliophyta – Flowering plants <br/><strong>Class: </strong> Magnoliopsida – Dicotyledons <br/><strong> Subclass: </strong>  Hamamelididae <br/><strong> Order:</strong>   Urticales<strong> <br/> Family:</strong> Moraceae – Mulberry family <br/>"
     "<strong> Genus:</strong> Artocarpus J.R. Forst. & G. Forst. – breadfruit <br/><strong> Species: </strong>   Artocarpus heterophyllus Lam. – jackfruit <br/> <strong>Part used:</strong>   Fruit, Seeds, Leaves, Flowers. Fruit <br/> <strong>Medicinal Properties:</strong>   anti-inflammatory, "
     "antioxidants, vitamin C, various bioflavonoids, and fibers, anti-cancerous,anti-diabetic  <br/> <strong>Medicinal Use:</strong> "
     " The ashes of leaves, with or without oil, are used to treat ulcers, diarrhoea, boils, stomach-ache and wounds.The ashes of leaves, with or without oil, are used to treat ulcers, diarrhoea, boils, stomach-ache and wounds.The seeds are said to be an aphrodisiac."],

"Azadirachta Indica (Neem)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Azadirachta indica<br/> <strong> Common Name :</strong>   Neem <br/> <strong>Kingdom: </strong>   Plantae <br/> <strong>SubKingdom:</strong> Tracheobionta <br/><strong> Division:  </strong> Magnoliophyta <br/><strong>Class: </strong> Magnoliopsida <br/><strong> Subclass: </strong>  Rosidae <br/><strong> Order:</strong>  Sapindales<strong> <br/> Family:</strong> Meliaceae <br/><strong> Genus:</strong>  Azadirachta <br/><strong> Species: </strong>   indica <br/> <strong>Part used:</strong>  Leaves, Flower, Seed Oil, Bark <br/> <strong>Medicinal Properties:</strong>   Anthelmintic, antiseptic, antifungal, antidiabetic, antibacterial, antiviral, contraceptive, sedative, mosquito repellent, anti-desertification properties and good carbon dioxide sink. <br/> <strong>Medicinal Use:</strong>  Plant pacifies vitiated pitta, skin diseases, eczema, fever, wound, ulcer, burning sensation, tumor, worms, cough, diabetes, inflammation and rheumatoid arthritis. Leaf juice used as blood purifier. Used in cosmetics and bio-pesticide</p>"],

"Basella Alba (Basale)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Basella Alba<br/> <strong> Common Name :</strong>   Basale <br/> <strong>Kingdom: </strong>    Plantae – Plants <br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
     "Division:  </strong> Magnoliophyta – Flowering plants <br/><strong>Class: </strong> Magnoliopsida – Dicotyledons <br/><strong> Subclass: </strong>   Caryophyllidae <br/><strong> Order:</strong> Caryophyllales<strong> <br/> Family:</strong>  Basellaceae – Basella family <br/>"
     "<strong> Genus:</strong>  Basella L. – basella <br/><strong> Species: </strong> Basella alba L.<br/> <strong>Part used:</strong>   stems and leaves<br/> <strong>Medicinal Properties:</strong>   It has been attributed with gastro-protective activity, ulcer healing, anti-inflammatory activity, wound healing activity. Basella alba is reported to improve testosterone levels in males, thus boosting libido. Decoction of the leaves is recommended as a safe laxative in pregnant women and children.<br/> <strong>Medicinal Use:</strong> "
     " The roots are astringent. They are cooked and used in the treatment of diarrhoea A paste of the root is applied to swellings and is also used as a rubefacient.The flowers are used as an antidote to poisons"],

"Brassica Juncea (Indian Mustard)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Brassica Juncea <br/> <strong> "
"Common Name :</strong>   Indian Mustard <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"
"<strong> Subclass: </strong>   Dilleniidae <br/>"
"<strong> Order:</strong> Capparales<strong> <br/> "
"Family:</strong>Brassicaceae – Mustard family<br/>"
"<strong> Genus:</strong>   Brassica L. – mustard <br/>"
"<strong> Species: </strong>  Brassica juncea (L.) Czern. – brown mustard<br/>"
"<strong>Part used:</strong> Leaves, seeds, Flowers, root<br/>"
"<strong>Medicinal Properties:</strong>   antibiotic,Reported to be anodyne, aperitif, diuretic, emetic, rubefacient, and stimulant, Brown Mustard is a folk remedy for arthritis, foot ache, lumbago, and rheumatism<br/>"
"<strong>Medicinal Use:</strong> "
     " The seed is used in the treatment of tumours in China In Korea, the seeds are used in the treatment of abscesses, colds, lumbago, rheumatism, and stomach disorders,The root is used as a galactagogue in Africa, Mustard oil is used in the treatment of skin eruptions and ulcers,Leaves applied to the forehead are said to relieve headache</p>"],

"Carissa Carandas (Karanda)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Carissa Carandas <br/> <strong> "
"Common Name :</strong> Karanda <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"
"<strong> Subclass: </strong>  Asteridae <br/>"
"<strong> Order:</strong> Gentianales<strong> <br/> "
"Family:</strong>Brassicaceae – Apocynaceae – Dogbane family<br/>"
"<strong> Genus:</strong> Carissa L. – carissa <br/>"
"<strong> Species: </strong> Carissa carandas L. [excluded] – karanda <br/>"
"<strong>Part used:</strong> Leaves, seeds, Flowers, root<br/>"
"<strong>Medicinal Properties:</strong>   The fruits are astringent, antiscorbutic and also used as a remedy for biliousness<br/>"
"<strong>Medicinal Use:</strong> "
     "A leaf decoction is used against fever, diarrhoea, and earache"
"The roots serve as a stomachic, vermifuge and remedy for itches.</p> "],


"Citrus Limon (Lemon)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>   Citrus Limon<br/> <strong> "
"Common Name :</strong> Lemon <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"
"<strong> Subclass: </strong> Rosidae<br/>"
"<strong> Order:</strong> Sapindales<strong> <br/> "
"Family:</strong>  Rutaceae – Rue family<br/>"
"<strong> Genus:</strong>  Citrus L. – citrus  <br/>"
"<strong> Species: </strong>  Citrus ×limon (L.) Burm. f. (pro sp.) – lemon<br/>"
"<strong>Part used:</strong> Leaves, seeds, Flowers, root<br/>"

"<strong>Medicinal Use:</strong> "
     "Lemons are an excellent preventative medicine and have a wide range of uses in the domestic medicine chest. The fruit is rich in vitamin C which helps the body to fight off infections and also to prevent or treat scurvy"
 "It was at one time a legal requirement that sailors should be given an ounce of lemon each day in order to prevent scurvy"
 "Applied locally, the juice is a good astringent and is used as a gargle for sore throats etc"
 "Lemon juice is also a very effective bactericide"
 "It is also a good antiperiodic and has been used as a substitute for quinine in treating malaria and other fevers.</p>"],

"Ficus Auriculata (Roxburgh fig)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Ficus Auriculata <br/> <strong> "
"Common Name :</strong> Roxburgh fig <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Hamamelididae<br/>"
"<strong> Order:</strong> Urticales<strong> <br/> "
"Family:</strong>Moraceae – Mulberry family<br/>"
"<strong> Genus:</strong>  Ficus L. – fig <br/>"
"<strong> Species: </strong>  Ficus auriculata Lour. – Roxburgh fig <br/>"

"<strong>Part used:</strong> Leaves, seeds,fruits, stems<br/>"

"<strong>Medicinal Use:</strong> "
     "The latex from the stems is applied to cuts and wounds"
"The roasted fruit is used in the treatment of diarrhoea and dysentery.</p>"],

"Ficus Religiosa (Peepal Tree)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Ficus Religiosa  <br/> <strong> "
"Common Name :</strong> Peepal Tree <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Hamamelididae<br/>"
"<strong> Order:</strong> Urticales<strong> <br/> "
"Family:</strong>Moraceae – Mulberry family<br/>"
"<strong> Genus:</strong>  Ficus L. – fig <br/>"
"<strong> Species: </strong>  Ficus religiosa L. – peepul tree <br/>"

"<strong>Part used:</strong> Leaves, bark , twigs, aerial roots , wood<br/>"

"<strong>Medicinal Use:</strong> "
     "The leaves and twigs are alterative, antidote, aphrodisiac, astringent, antigonorrhoeal and laxative"
 "It is used as an antidote against bites of venomous animals, and for the treatment of haemoptysis and fistula"


"Fresh sap from the leaves is used to cure diarrhoea, cholera and for wound healing"


"An infusion of the bark is drunk as an antidiabetic"

"A decoction of the bark is used as skin wash to treat scabies, ulcers and skin diseases"


"The aerial roots are diuretic"
"They are used in the treatment of ascites and are chewed by women to promote fertility.</p>"],

"Hibiscus Rosa-sinensis":
["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Hibiscus Rosa-sinensis<br/> <strong> "
"Common Name :</strong>Chinese Hibiscus <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Dilleniidae<br/>"
"<strong> Order:</strong> Malvales<strong> <br/> "
"Family:</strong>Moraceae – Malvaceae – Mallow family<br/>"
"<strong> Genus:</strong>Hibiscus L. – rosemallow<br/>"
"<strong> Species: </strong> Hibiscus rosa-sinensis L. – shoeblackplant <br/>"

"<strong>Part used:</strong> Leaves, flowers, root<br/>"

"<strong>Medicinal Use:</strong> "
     "Chinese hibiscus is a sweet, astringent, cooling herb that checks bleeding, soothes irritated tissues and relaxes spasms The flowers are aphrodisiac, demulcent, emmenagogue, emollient and refrigerant They are used internally in the treatment of excessive and painful menstruation, cystitis, venereal diseases, feverish illnesses, bronchial catarrh, coughs and to promote hair growth, An infusion of the flowers is given as a cooling drink to ill people</p>"],

"Jasminum (Jasmine)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Jasminum<br/> <strong> "
"Common Name :</strong>Jasmine <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Asteridae<br/>"
"<strong> Order:</strong>  Scrophulariales <strong> <br/> "
"Family:</strong> Oleaceae – Olive family<br/>"
"<strong> Genus:</strong> Jasminum L. – jasmine <br/>"
"<strong> Species: </strong> Contains 12 Species.<br/>"

"<strong>Part used:</strong> Leaves, flowers<br/>"

"<strong>Medicinal Use:</strong> "
     "Jasmine oil or essence is used medicinally. It is said to stimulate the reproductive system as an aphrodisiac and as a muscle relaxant, by warming and softening nerves and tendons An infusion of the flowers is used to relieve coughs The flowers are also used to treat headaches weak eyes and scorpion stings Applied externally, an infusion of the flowers is used to treat skin diseases The leaves are chewed as a remedy for ulcers or eruptions in the mouth The fresh juice of the plant is applied to corns Mixed with oil, it is poured into the ears as a treatment for otorrhoea</p>"],

"Mangifera Indica (Mango)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Mangifera Indica <br/> <strong> "
"Common Name :</strong>Mango <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae<br/>"
"<strong> Order:</strong>    Sapindales <strong> <br/> "
"Family:</strong>  Anacardiaceae – Sumac family <br/>"
"<strong> Genus:</strong>  Mangifera L. – mango <br/>"
"<strong> Species: </strong>  Mangifera indica L. – mango <br/>"

"<strong>Part used:</strong> Leaves, flowers, seeds, Fruit, bark, stem, roots<br/>"

"<strong>Medicinal Use:</strong> "
     "The leaves are astringent and odontalgic An infusion is drunk to reduce blood pressure and as a treatment for conditions such as angina, asthma, coughs and diabetes Externally, the leaves are used in a convalescent bath A mouthwash made from the leaves is effective in hardening the gums and helping to treat dental problems The leaves are used to treat skin irritations The charred and pulverized leaves are used to make a plaster for removing warts and also act as a styptic</p>"],

"Mentha (Mint)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Mentha L. <br/> <strong> "
"Common Name :</strong>Mint <br/>" 
"<strong>Kingdom: </strong>    Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Asteridae <br/>"
"<strong> Order:</strong>  Lamiales<strong> <br/> "
"Family:</strong> Lamiaceae – Mint family<br/>"
"<strong> Genus:</strong>   Mentha L. – mint <br/>"
"<strong> Species: </strong> Contains 13 Species <br/>"

"<strong>Part used:</strong>whole plant<br/>"

"<strong>Medicinal Use:</strong> "
     "The whole plant is anaesthetic, antiphlogistic, antispasmodic, antiseptic, aromatic, carminative, diaphoretic, emmenagogue, galactofuge, refrigerant, stimulant, stomachic and vasodilator.</p>"],

"Moringa Oleifera (Drumstick)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Moringa Oleifera  <br/> <strong> "
"Common Name :</strong>Drumstick<br/>" 
"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Dilleniidae <br/>"
"<strong> Order:</strong>  Capparales <strong> <br/> "
"Family:</strong> Moringaceae – Horse-radish tree family<br/>"
"<strong> Genus:</strong>   Moringa Adans. – moringa <br/>"
"<strong> Species: </strong>  Moringa oleifera Lam. – horseradishtree <br/>"

"<strong>Part used:</strong>whole plant<br/>"

"<strong>Medicinal Use:</strong> "
     "The horseradish tree is a nutritious, diuretic, laxative herb that is expectorant, increases milk flow, controls bacterial infections and is rubefacient when applied topically It contains a potent antibiotic Ben oil, obtained from the seeds, has no taste, smell or colour and is exceptionally resistant to oxidation.</p>"],

"Muntingia Calabura (Jamaica Cherry-Gasagase)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Muntingia Calabura   <br/> <strong> "
"Common Name :</strong>Jamaica Cherry-Gasagase<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong> Dilleniidae <br/>"
"<strong> Order:</strong> Malvales <strong> <br/> "
"Family:</strong>  Elaeocarpaceae – Elaeocarpus family <br/>"
"<strong> Genus:</strong> Muntingia L. – muntingia <br/>"
"<strong> Species: </strong> Muntingia calabura L. – strawberrytree <br/>"

"<strong>Part used:</strong>Leaves and fruit<br/>"

"<strong>Medicinal Use:</strong> "
     "medicinal uses have been reported for the leaves (headaches, prostate problems, reduce gastric ulcers), bark (antiseptic), flowers (antiseptic, reduce swelling, antispasmodic), and fruits (respiratory problems; antidiarrheic).It is said to help diabetic patients. A small reduction was recorded in patients' blood sugar levels after consumption.</p>"],

"Murraya Koenigii (Curry)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Murraya Koenigii  <br/> <strong> "
"Common Name :</strong>Curry <br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong>   Sapindales <strong> <br/> "
"Family:</strong>Rutaceae – Rue family<br/>"
"<strong> Genus:</strong> Murraya J. Koenig ex L. – murraya<br/>"
"<strong> Species: </strong>  Murraya koenigii (L.) Spreng. – curryleaftree <br/>"

"<strong>Part used:</strong>Leaves , roots and bark<br/>"

"<strong>Medicinal Use:</strong> "
     "Curry leaf contains several medically active constituents including a glycoside called koenigin, an essential oil and tannins.It is a warming, strongly aromatic herb that improves appetite and digestion.</p>"],

"Nerium Oleander (Oleander)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Nerium Oleander <br/> <strong> "
"Common Name :</strong> Oleander <br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Asteridae<br/>"
"<strong> Order:</strong>    Gentianales<strong> <br/> "
"Family:</strong> Apocynaceae – Dogbane family<br/>"
"<strong> Genus:</strong>  Nerium L. – oleander<br/>"
"<strong> Species: </strong>   Nerium oleander L. – oleander <br/>"

"<strong>Part used:</strong>Whole plant<br/>"

"<strong>Medicinal Use:</strong> "
     "Oleander is a very poisonous plant, containing a powerful cardiac toxin and should only be used with extreme caution.</p>"],

"Nyctanthes Arbor-tristis (Parijata)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Nyctanthes arbor-tristis<br/> <strong> "
"Common Name :</strong> Parijat <br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Asteridae<br/>"
"<strong> Order:</strong> Lamiales<strong> <br/> "
"Family:</strong>Oleaceae<br/>"
"<strong> Genus:</strong>Nyctanthes<br/>"
"<strong> Species: </strong> 	N. arbor-tristis <br/>"

"<strong>Part used:</strong>Whole plant<br/>"

"<strong>Medicinal Use:</strong> "
     "The leaves have been used in Ayurvedic medicine and Homoeopathy for sciatica, arthritis, and fevers, and as a laxative.</p>"],

"Ocimum Tenuiflorum (Tulsi)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Ocimum Tenuiflorum <br/> <strong> "
"Common Name :</strong>Holy Tulsi<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Asteridae<br/>"
"<strong> Order:</strong> Lamiales<strong> <br/> "
"Family:</strong>Lamiaceae – Mint family<br/>"
"<strong> Genus:</strong>Ocimum L. – basil<br/>"
"<strong> Species: </strong>  Ocimum tenuiflorum L. – holy basil <br/>"

"<strong>Part used:</strong>Leaves, seeds<br/>"

"<strong>Medicinal properties:</strong> Leaves: aromatic, acrid, bitter, thermogenic, appetizing, digestive, carminative, depurative, expectorant, anthelmintic, cardiotonic, alexeteric and tonic.</br>"
"<strong>Medicinal Use:</strong> "
     "Leaves: useful in helminthiasis, anorexia, dyspepsia, flatulence, dysentery, leprosy, pruritus, parasitic, vomiting, poisonous affections, haemoptysis, strangury, migraine, malaria and fever. Seeds: useful in hyperdipsia, malaria, migraine and emaciation.</p>"],

"Piper Betle (Betel)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Piper Betle <br/> <strong> "
"Common Name :</strong>Betel<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Magnoliidae <br/>"
"<strong> Order:</strong> Piperales<strong> <br/> "
"Family:</strong> Piperaceae – Pepper family<br/>"
"<strong> Genus:</strong>Piper L. – pepper<br/>"
"<strong> Species: </strong> Piper betle L. <br/>"

"<strong>Part used:</strong> leaves, roots and seeds<br/>"

"<strong>Medicinal properties:</strong> Leaves: The leaves are said to be anthelmintic, antibacterial, antifungal, antiseptic, aphrodisiac, astringent, carminative, expectorant, laxative, sialagogue, stimulant, stomachic and tonic</br>"
"<strong>Medicinal Use:</strong> "
     " Leaf preparations and the leaf sap are applied to wounds, ulcers, boils and bruises. Heated leaves are applied as a poultice on the chest against cough and asthma, on the breasts to stop milk secretion, and on the abdomen to relieve constipation.</p>"],

"Plectranthus Amboinicus (Mexican Mint)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Plectranthus Amboinicus <br/> <strong> "
"Common Name :</strong>Mexican Mint<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Asteridae <br/>"
"<strong> Order:</strong> Lamiales<strong> <br/> "
"Family:</strong> Lamiaceae – Mint family<br/>"
"<strong> Genus:</strong> Plectranthus L'Hér. – plectranthus<br/>"
"<strong> Species: </strong>  Plectranthus amboinicus (Lour.) Spreng. – Mexican mint <br/>"

"<strong>Part used:</strong> Whole Plant<br/>"

"<strong>Medicinal properties:</strong> Leaves: antibacterial and antiseptic</br>"
"<strong>Medicinal Use:</strong> "
     " The leaves are frequently utilized in the treatment of urinary diseases in the Amazon and India. This species is also reported to relieve kidney troubles, treat vaginal discharges and is drunk after childbirth Applied externally, the leaves are used to treat headaches, inflammations, skin allergies, wounds, burns, sores and ulcers When rubbed on the skin, they will quickly bring relief to bites and stings.</p>"],

"Pongamia Pinnata (Indian Beech)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Pongamia Pinnata <br/> <strong> "
"Common Name :</strong>Indian Beech(Pongam)<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong>Fabales<strong> <br/> "
"Family:</strong>Fabaceae<br/>"
"<strong> Genus:</strong> Millettia Wight & Arn. – oiltree<br/>"
"<strong> Species: </strong> Millettia pinnata (L.) Panigrahi – pongame oiltree <br/>"

"<strong>Part used:</strong> Whole Plant<br/>"

"<strong>Medicinal properties:</strong> The seed oil is given as a stomachic and cholagogue in the treatment of dyspepsia and cases of sluggish liver It is used externally as a liniment for rubbing on skin diseases and rheumatic joints It has been shown to be effective in enhancing the pigmentation of skin affected by leucoderma or scabies.</p>"],

"Psidium Guajava (Guava)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Psidium guajava <br/> <strong> "
"Common Name :</strong>Guava<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong> Myrtales<strong> <br/> "
"Family:</strong>  Myrtaceae – Myrtle family<br/>"
"<strong> Genus:</strong>  Psidium L. – guava<br/>"
"<strong> Species: </strong> Psidium guajava L. – guava <br/>"

"<strong>Part used:</strong> Bark , Leaves, fruits, wood<br/>"


"<strong>Medicinal Use:</strong> "
     "A decoction of the bark, or of the roots, is employed to treat urinary diseases, diarrhoea and dysentery It is said to reduce varicose veins and ulcers on the legs A leaf decoction is taken to relieve colds, bronchitis and diarrhoea The juice of the young fruit is squeezed and used as a treatment for dysentery and upset stomachs.</p>"],


"Punica Granatum (Pomegranate)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Punica Granatum  <br/> <strong> "
"Common Name :</strong>Pomegranate<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong> Myrtales<strong> <br/> "
"Family:</strong> Punicaceae – Pomegranate family<br/>"
"<strong> Genus:</strong>  Punica L. – pomegranate<br/>"
"<strong> Species: </strong>  Punica granatum L. – pomegranate <br/>"

"<strong>Part used:</strong> The whole plant, but in particular the bark<br/>"
"<strong>Medicinal properties:</strong> antibacterial, antiviral and astringent</br>"

"<strong>Medicinal Use:</strong> "
     "The pomegranate has a long history of herbal use dating back more than 3,000 years All parts of the plant contain unusual alkaloids, known as 'pelletierines', which paralyse tapeworms so that they are easily expelled from the body by using a laxative The plant is also rich in tannin, which makes it an effective astringent. It is used externally in the treatment of vaginal discharges, mouth sores and throat infections</p>"],



"Santalum Album (Sandalwood)":
["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Santalum Album  <br/> <strong> "
"Common Name :</strong>Sandalwood<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong> Santalales<strong> <br/> "
"Family:</strong> Santalaceae – Sandalwood family<br/>"
"<strong> Genus:</strong>  Santalum L. – sandalwood<br/>"
"<strong> Species: </strong>    Santalum album L. – sandalwood <br/>"

"<strong>Part used:</strong> wood, roots, seeds, leaves<br/>"
"<strong>Medicinal properties:</strong> diuretic, analgesic, antiseptic, expectorant and stimulant effects</br>"

"<strong>Medicinal Use:</strong> "
     "Sandalwood contains 3 - 6% essential oils (predominantly the sesquiterpenols alpha- and beta-santalol), resin and tannins It is an aromatic, bittersweet, astringent herb that cools the body, calms the mind, relieves spasms and improves digestion The wood or essential oil is taken internally in the treatment of genito-urinary disorders, fever, sunstroke, digestive problems and abdominal pain. A paste of the wood is used externally to treat skin complaints. Sandalwood oil is little used in modern herbalism, its main application is in aromatherapy</p>"],

"Syzygium Cumini (Jamun)":
["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong>Syzygium Cumini <br/> <strong> "
"Common Name :</strong>Jamun<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong>  Myrtales<strong> <br/> "
"Family:</strong>  Myrtaceae – Myrtle family<br/>"
"<strong> Genus:</strong>  Syzygium P. Br. ex Gaertn. – syzygium<br/>"
"<strong> Species: </strong> Syzygium cumini (L.) Skeels – Java plum <br/>"

"<strong>Part used:</strong> Bark , fruits, seed,ash of Leaves <br/>"
"<strong>Medicinal properties:</strong> stomachic, astringent, diuretic and antidiabetic.</br>"

"<strong>Medicinal Use:</strong> "
     "milk and taken orally taken twice a day after food for 3 months to treat diabetes. Fresh fruits are also taken orally to get relief from stomachache and to treat diabete. Young leaf is ground into a paste with goat's milk and taken orally to treat indigestion.</p>"],

"Syzygium Jambos (Rose Apple)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Syzygium Jambos<br/> <strong> "
"Common Name :</strong>Rose Apple<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>  Rosidae <br/>"
"<strong> Order:</strong>  Myrtales<strong> <br/> "
"Family:</strong>  Myrtaceae – Myrtle family<br/>"
"<strong> Genus:</strong>  Syzygium P. Br. ex Gaertn. – syzygium<br/>"
"<strong> Species: </strong> Syzygium jambos (L.) Alston – Malabar plum<br/>"

"<strong>Part used:</strong> Flowers, seeds, leaves, bark, root<br/>"


"<strong>Medicinal Use:</strong> "
     "In India, the fruit is regarded as a tonic for the brain and liver. An infusion of the fruit acts as a diuretic. A sweetened preparation of the flowers is believed to reduce fever</p>"],


"Tabernaemontana Divaricata (Crape Jasmine)":
["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Tabernaemontana Divaricata<br/> <strong> "
"Common Name :</strong>Crape Jasmine<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>   Asteridae <br/>"
"<strong> Order:</strong>   Gentianales<strong> <br/> "
"Family:</strong> Apocynaceae – Dogbane family<br/>"
"<strong> Genus:</strong> Tabernaemontana L. – milkwood<br/>"
"<strong> Species: </strong>  Tabernaemontana divaricata (L.) R. Br. ex Roem. & Schult. – pinwheelflower<br/>"

"<strong>Part used:</strong> Flowers, leaves, roots<br/>"

"<strong>Medicinal properties:</strong> anti-epileptic, anti-mania, brain tonic, and anti-oxidant</br>"
"<strong>Medicinal Use:</strong> "
     "Indeed, in India the applications in traditional medicine are so numerous that the plant may well be classified as a panacea for gastro-intestinal, urogenital and skin affections. The wood is refrigerant.The roots are astringent</p>"],



"Trigonella Foenum-graecum (Fenugreek)":
    ["<p style='font-family:Arial, Helvetica, sans-serif;'><strong> Botanical Name :</strong> Trigonella Foenum-graecum<br/> <strong> "
"Common Name :</strong>Fenugreek<br/>" 

"<strong>Kingdom: </strong> Plantae – Plants "
"<br/> <strong>SubKingdom:</strong> Tracheobionta – Vascular plants <br/><strong> "
"Division:  </strong> Magnoliophyta – Flowering plants <br/>"
"<strong>Class: </strong> Magnoliopsida – Dicotyledons <br/>"

"<strong> Subclass: </strong>   Rosidae <br/>"
"<strong> Order:</strong>  Fabales<strong> <br/> "
"Family:</strong>   Fabaceae – Pea family<br/>"
"<strong> Genus:</strong> Trigonella L. – fenugreek<br/>"
"<strong> Species: </strong>  Trigonella foenum-graecum L. – sicklefruit fenugreek<br/>"

"<strong>Part used:</strong> Seeds, Leaves<br/>"

"<strong>Medicinal properties:</strong> anticholesterolemic, anti-inflammatory, antitumor, carminative, demulcent, deobstruent, emollient, expectorant, febrifuge, galactagogue, hypoglycaemic, laxative, parasiticide, restorative and uterine tonic.</br>"
"<strong>Medicinal Use:</strong> "
     "The seeds are very nourishing and are given to convalescents and to encourage weight gain, especially in anorexia nervosa. The seeds should not be prescribed medicinally for pregnant women since they can induce uterine contractions. Research has shown that the seeds can inhibit cancer of the liver, lower blood cholesterol levels and also have an antidiabetic effect.</p>"]



}

def load_artifacts():
    global model
    model = tf.keras.models.load_model("mobilenetv2.h5")

def classify_plant(image_path):
	global model, output_class
	test_image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
	test_image = tf.keras.preprocessing.image.img_to_array(test_image) / 255
	test_image = np.expand_dims(test_image, axis = 0)
	predicted_array = model.predict(test_image)
	predicted_value = output_class[np.argmax(predicted_array)]
	return predicted_value, str(data[predicted_value][0])



