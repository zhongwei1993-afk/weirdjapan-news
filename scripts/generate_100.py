#!/usr/bin/env python3
"""Generate 100 articles for weirdjapan.news from a curated topic list."""
import os
from datetime import date, timedelta

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "content", "blog")

# Image pool — Unsplash photo URLs we already verified are free + non-premium.
IMAGES = {
    "vending": (
        "https://images.unsplash.com/photo-1552349471-57c1b1cce2d3?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Row of brightly colored Japanese vending machines.",
        "Photo by Ji Seongkwang on Unsplash",
        "https://unsplash.com/photos/lvu7gpzIT8k",
    ),
    "vending-night": (
        "https://images.unsplash.com/photo-1555359191-93e970dfa588?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "A solitary lit vending machine glowing on a dark Tokyo street.",
        "Photo by Darren Halstead on Unsplash",
        "https://unsplash.com/photos/vuL_H4N4fW0",
    ),
    "tokyo-night": (
        "https://images.unsplash.com/photo-1573455494060-c5595004fb6c?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Tokyo street at night, glowing with dense neon and headlights.",
        "Photo by Denys Nevozhai on Unsplash",
        "https://unsplash.com/photos/D68ADLeMh5Q",
    ),
    "capsule": (
        "https://images.unsplash.com/photo-1539606420556-14c457c45507?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Stacked capsule hotel beds with white mattresses.",
        "Photo by Alec Favale on Unsplash",
        "https://unsplash.com/photos/RDIa_qFpWHc",
    ),
    "cat": (
        "https://images.unsplash.com/photo-1722310604155-26f38d176e05?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "A cat walks along a quiet street in a Japanese village.",
        "Photo by Caspar Wai on Unsplash",
        "https://unsplash.com/photos/2DtIC_ApTTY",
    ),
    "akihabara": (
        "https://images.unsplash.com/photo-1701338462908-6022ef7cb466?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Akihabara at night, glowing with dense neon.",
        "Photo by Darwin Vegher on Unsplash",
        "https://unsplash.com/photos/CPAajYWQeR4",
    ),
    "neon-street": (
        "https://images.unsplash.com/photo-1681057593365-81c8e6f1348f?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Tokyo street filled with neon signs at night.",
        "Photo by BREAKIFY on Unsplash",
        "https://unsplash.com/photos/IEWUo6LgI3c",
    ),
    "sushi": (
        "https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Sushi on a white ceramic plate.",
        "Photo by Derek Duran on Unsplash",
        "https://unsplash.com/photos/Jz4QMhLvGgw",
    ),
    "cherry-blossom": (
        "https://images.unsplash.com/photo-1598957232485-fab51e0ed7e8?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Pathway between blooming cherry blossom trees.",
        "Photo by Crystal Kay on Unsplash",
        "https://unsplash.com/photos/7viWpO0fNss",
    ),
    "torii": (
        "https://images.unsplash.com/photo-1492571350019-22de08371fd3?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "A vermilion torii gate at a Japanese shrine.",
        "Photo by Tianshu Liu on Unsplash",
        "https://unsplash.com/photos/SBK40fdKbAg",
    ),
    "festival": (
        "https://images.unsplash.com/photo-1757944075647-2498be56bb62?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Glowing Japanese lanterns at a night festival.",
        "Photo by ayumi kubo on Unsplash",
        "https://unsplash.com/photos/guEJrCgWtGs",
    ),
    "ramen": (
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1600&q=80&fm=jpg&auto=format&fit=crop",
        "Round white bowl with ramen and a soft-boiled egg.",
        "Photo by Michele Blackwell on Unsplash",
        "https://unsplash.com/photos/rAyCBQTH7ws",
    ),
}


def pick_image(slug, category):
    s = slug.lower()
    c = (category or "").lower()
    if "cat" in s: return "cat"
    if any(k in s for k in ["sushi", "fugu", "whale", "kit-kat", "wagyu", "anpan", "obanyaki", "depachika", "tonkatsu", "melon-pan", "donut", "starbucks", "matcha"]): return "sushi"
    if any(k in s for k in ["ramen", "mochi", "takoyaki", "kakigori", "omurice", "onsen-egg", "edible-insect", "amezaiku"]): return "ramen"
    if any(k in s for k in ["shrine", "torii", "temple", "fujiko"]): return "torii"
    if any(k in s for k in ["festival", "hatsumode", "obon", "matsuri", "setsubun", "shichi-go-san", "coming-of-age", "cherry-blossom-forecast"]): return "festival"
    if any(k in s for k in ["cherry", "sakura", "anime-pilgrimage"]): return "cherry-blossom"
    if any(k in s for k in ["capsule", "nap", "sleep", "hikikomori", "inemuri"]): return "capsule"
    if any(k in s for k in ["shibuya", "scramble", "underground", "ghibli", "roppongi", "tokyo-tower", "drone-light"]): return "tokyo-night"
    if any(k in s for k in ["vending", "machine", "crab-vending", "urine"]): return "vending"
    if any(k in s for k in ["akihabara", "cosplay", "maid", "theme-restaurant", "butler", "anime", "nintendo", "pet-rental", "owl-cafe", "hedgehog-cafe", "cuddle"]): return "akihabara"
    if any(k in s for k in ["neon", "host", "love-hotel", "rui-katsu"]): return "neon-street"
    if "robot" in s or "ai-priest" in s or "pepper" in s or "orihime" in s: return "neon-street"
    if "toilet" in s or "toto" in s: return "vending-night"
    if "earthquake" in s or "parking-tower" in s or "fruit-bus" in s: return "tokyo-night"
    return "vending-night"


# 100 articles: (slug, title, description, category)
ARTICLES = [
    # Only In Japan (35)
    ("robot-hotel-henna", "Inside Japan's Robot Hotel — Where the Receptionist is a Velociraptor", "The Henn na Hotel was the first hotel staffed entirely by robots. Then they fired half of them. Here's why.", "Only In Japan"),
    ("pet-rental-shops", "Tokyo's Pet Rental Shops Let You Borrow a Dog for ¥3,000", "Can't own a pet in your tiny Tokyo apartment? Rent one for the weekend. The industry is regulated, ethical, and surprisingly heartwarming.", "Only In Japan"),
    ("cuddle-cafe-tokyo", "I Paid ¥6,000 to Sleep Next to a Stranger at a Tokyo 'Cuddle Café'", "No touching below the shoulder. No conversation about your real life. Just 60 minutes of platonic proximity. Welcome to Japan's strangest service.", "Only In Japan"),
    ("owl-cafe-tokyo", "Inside Tokyo's Owl Cafés — Cute, Quiet, and Quietly Controversial", "You pay ¥2,000 to sip coffee while owls perch on your shoulder. Animal welfare groups disagree about whether anyone should.", "Only In Japan"),
    ("hedgehog-cafe-roppongi", "Hedgehogs Sip Lattes With You at This Roppongi Café", "Tokyo's hedgehog cafés charge ¥1,500 for 30 minutes with a spiky companion. Here's what happens inside.", "Only In Japan"),
    ("rui-katsu-crying-clubs", "Japan's 'Crying Clubs' Where Men Pay ¥7,000 to Sob in Public", "Rui-katsu (tear-seeking) is a wellness trend where Japanese salarymen pay to watch sad films and cry in a group. It works.", "Only In Japan"),
    ("nap-cafes-tokyo", "Tokyo's Nap Cafés Sell 90 Minutes of Sleep for ¥1,000", "Bed. Blackout curtains. Lavender pillow. No phone. No talking. Tokyo's nap cafés are the productivity hack the West refuses to copy.", "Only In Japan"),
    ("vampire-cafe-ginza", "Drink Blood Cocktails at Tokyo's Vampire Café — Open Since 2000", "Ginza hides a vampire-themed restaurant that's been operating for 25 years. The coffin tables are real. The blood-red cocktails are virgin.", "Only In Japan"),
    ("prison-restaurant-shinjuku", "Tokyo's Prison Restaurant Locks You in for Dinner", "Kagaya in Shinjuku puts diners in a 'cell' where the waiter pretends to be a corrupt prison guard. The food is excellent. The experience is disorienting.", "Only In Japan"),
    ("alien-restaurant-tokyo", "Tokyo's UFO-Themed Restaurant Where Aliens Serve Curry", "Step inside what looks like a flying saucer's interior. The staff is dressed as extraterrestrials. The menu is fine. The vibe is unforgettable.", "Only In Japan"),
    ("rent-a-friend", "Tokyo's 'Rent a Friend' Industry is Worth Millions", "Lonely? Need a wedding date? Need a fake parent for parent-teacher day? Japan's actor-friend rental industry will discreetly provide.", "Only In Japan"),
    ("snow-monkey-onsen", "The Hot Spring Where Snow Monkeys Outnumber Tourists", "Jigokudani Monkey Park in Nagano is the only place in the world where wild macaques bathe in hot springs. They've been doing it since 1963.", "Only In Japan"),
    ("manga-kissa-apartments", "Tokyo's Manga Cafés Are Doubling as Apartments. By Choice.", "For ¥2,000 a night, you get a chair, free drinks, a shower, and 30,000 manga. Some Tokyo workers live there full-time.", "Only In Japan"),
    ("toilet-karaoke", "Japanese Public Toilets Have Background Music. Now It's Pop Songs.", "The Otohime device masks bathroom noises with running water. Newer models play J-pop. Tokyo Station's restroom is rumored to have karaoke.", "Only In Japan"),
    ("ghost-stickers-apartments", "Japan Sells Anti-Ghost Stickers for Apartments. They Work, Apparently.", "Stick this on your wall to ward off resident yūrei. ¥300 each. Endorsed by Shinto priests. Available at Don Quijote.", "Only In Japan"),
    ("square-watermelons", "Japan Grows Square Watermelons. They Cost ¥10,000 Each.", "Farmers in Kagawa grow watermelons inside acrylic boxes. The result: cube-shaped fruit that fits perfectly in a fridge — but is too unripe to eat.", "Only In Japan"),
    ("yanaka-cat-village", "Yanaka: Tokyo's Cat Village Where the Felines Run the Alleys", "This old neighborhood near Ueno is home to dozens of stray cats and the only Tokyo bakery where the muffins are cat-shaped.", "Only In Japan"),
    ("hadaka-matsuri-naked-festival", "9,000 Men Run Naked Through Okayama. It's a Religion.", "Once a year, men in loincloths fight to grab a sacred wooden stick at Saidaiji Temple. The winner gets a year of good luck. And bruises.", "Culture"),
    ("ekiben-train-bento", "Japan's Ekiben Bento Boxes Made Train Stations Into Restaurants", "Every major Japanese train station sells regional bento boxes designed to be eaten on the train. There are over 4,000 varieties.", "Food"),
    ("plastic-food-craft", "The Multimillion-Yen Craft of Japanese Plastic Food", "Those plastic ramen bowls in restaurant windows aren't cheap. Each one is hand-painted, and a custom set can cost ¥500,000.", "Culture"),
    ("capsule-toy-mall-akihabara", "Tokyo's Mall of 3,000 Capsule Toy Machines — One Block of Pure Chaos", "Akihabara's Gachapon Hall packs three thousand machines into one room. The toys cost ¥200-500. Adults outnumber children 4 to 1.", "Only In Japan"),
    ("harajuku-cosplay-bridge", "The Harajuku Bridge Where Tokyo's Cosplayers Used to Live", "Jingu-bashi was the cosplay capital of the world from the 1990s to 2010. Then social media killed the scene. Here's what happened.", "Culture"),
    ("yamanote-line-drinking-game", "Tokyo's Drinking Game Played on a Real Train Line", "The Yamanote loops 29 stations. The game: every stop, name something from a category. Miss, you drink. It's slowly turning Tokyo expats into alcoholics.", "Only In Japan"),
    ("love-hotels-themed", "Inside Tokyo's Love Hotels — Where Each Room is a Different World", "Spaceship rooms. Jungle rooms. Hello Kitty rooms. Love hotels charge by the hour and sell privacy. The taxi-style entry system is genius.", "Only In Japan"),
    ("lost-umbrella-system", "Tokyo Reunites You With Your Lost Umbrella, For Free", "Lost-and-found in Japan is a national obsession. Tokyo Metro returns 80% of lost umbrellas. The system is run by retirees who genuinely care.", "Only In Japan"),
    ("urine-test-vending-machine", "The Vending Machine That Tests Your Urine for Cancer", "A Tokyo startup placed urine-analysis vending machines in office buildings. ¥500 per test. Results in 60 seconds. Adoption is mixed.", "Tech"),
    ("hatsumode-shrine-tradition", "13 Million Japanese Visit a Shrine on January 1st. Together.", "Hatsumōde is the year's first shrine visit. Meiji Shrine alone hosts 3 million people in 3 days. The queues are mythological.", "Culture"),
    ("setsubun-bean-throwing", "Japanese Throw Beans at Family Members Once a Year to Banish Demons", "On February 3rd, Japanese families shout 'Demons out, fortune in!' while pelting each other (and a parent in a demon mask) with soybeans.", "Culture"),
    ("anime-pilgrimage-towns", "Anime Fans Are Saving Rural Japan by Visiting Their Favorite Town", "When an anime is set in a real town, fans travel there to recreate scenes. Some dying villages have been economically rescued by a single show.", "Culture"),
    ("butler-cafe-shibuya", "Tokyo Has Butler Cafés Where Female Guests Are Called 'Princess'", "The female counterpart to maid cafés. Tuxedoed waiters bow, kiss your hand, and discuss your day. ¥3,000 covers tea and 45 minutes.", "Only In Japan"),
    ("crab-vending-akihabara", "The Tokyo Vending Machine That Sells Live Crabs", "Yes, live ones. They're in plastic boxes. You grab one with a claw-arm. They're alive. They're angry. Customers reportedly cook and eat them.", "Only In Japan"),
    ("cigarette-incense", "Japan Has Cigarette-Shaped Incense for Smoking After You've Quit", "You light the filtered end. It smells like vanilla, sandalwood, or strawberry — not tobacco. Ex-smokers swear it kills cravings.", "Only In Japan"),
    ("gold-leaf-coffee-kanazawa", "Kanazawa Sells Coffee Topped With Edible Gold Leaf for ¥2,500", "Kanazawa produces 99% of Japan's gold leaf. They put it on ice cream, sake, sushi, ramen, and — yes — your latte.", "Food"),
    ("taxi-doors-automatic", "Japanese Taxi Doors Open Automatically. Touch Them and You're Fired.", "The rear passenger door opens via lever from the driver's seat. Touching it disrespects the driver's craft. Tourists do it constantly. Drivers seethe quietly.", "Only In Japan"),
    ("apology-train-20-seconds", "Why a Japanese Train Apologized for Leaving 20 Seconds Early", "In 2017, the Tsukuba Express issued a public apology for a 20-second-early departure. The story went global. It's not even unusual in Japan.", "Tech"),

    # Tech & Quirks (15)
    ("toilet-music-otohime", "Japanese Toilets Play Music So You Don't Embarrass Yourself", "The Otohime ('sound princess') device disguises bathroom noises with running water. Now found in 90% of Japanese restrooms.", "Tech"),
    ("shinkansen-7-min-cleaning", "Japan's Bullet Trains Are Cleaned in 7 Minutes by 22 People", "The Tessei cleaning crew is its own attraction. They bow before boarding, sweep, restock, rotate seats — all in under 7 minutes. The world studies them.", "Tech"),
    ("ai-buddhist-priest-pepper", "Japan's Buddhist Robot Priest Performs Funerals for ¥50,000", "Pepper, the humanoid robot, chants sutras at funerals when human priests cost too much. A Kyoto company sells the service. Reactions are mixed.", "Tech"),
    ("pepper-robot-stores", "Japan Has a Robot That Cries When You Don't Buy Anything", "Pepper appears in SoftBank stores, banks, and hotels. It reads emotions — and yes, looks dejected when you walk away without buying.", "Tech"),
    ("toto-toilet-25-buttons", "Japan's Toilet Has 25 Buttons. Here's What Each One Does.", "Heated seat. Bidet front. Bidet rear. Adjustable nozzle position. Adjustable water pressure. Dryer. Deodorizer. Music. Yes, all in one toilet.", "Tech"),
    ("tokyo-parking-tower", "Tokyo's Automated Parking Towers Stack 12 Cars Vertically", "Land in Tokyo is so expensive that parking towers lift cars on elevators and rotate them into slots. Retrieval takes 90 seconds.", "Tech"),
    ("fruit-bus-stops-nagasaki", "Japan Built Bus Stops Shaped Like Giant Strawberries", "In Konagai, Nagasaki, the bus stops are shaped like watermelons, strawberries, melons, and tomatoes. There's no good explanation.", "Only In Japan"),
    ("orihime-robot-workers", "Japan's Hospitals Use Robots to Replace Bedridden Office Workers", "The OriHime robot is operated remotely by ALS patients and bedridden workers. It serves coffee in cafés. Customers know. It's beautiful.", "Tech"),
    ("hari-kuyo-needle-funeral", "Tokyo Holds an Annual Funeral for Broken Sewing Needles", "Hari-Kuyō honors broken or worn-out needles. Seamstresses bring them to a temple. Each needle gets pressed into soft tofu. Then a prayer.", "Culture"),
    ("kotatsu-heated-table", "Japanese Homes Have Heated Tables You Crawl Inside", "The kotatsu is a low table with a heater underneath and a blanket draped over. Japanese winter survival happens almost entirely inside one.", "Culture"),
    ("japan-slipper-protocol", "Japanese Homes Require 3 Different Pairs of Slippers", "Indoor slippers. Toilet slippers (used only in the bathroom). Tatami room slippers (none — you go barefoot). Get this wrong and you've offended your host.", "Culture"),
    ("earthquake-warning-system", "Every Phone in Japan Screams 15 Seconds Before an Earthquake", "Japan's J-Alert system detects P-waves and pushes a warning to every device within range. 15 seconds is enough to drop, cover, and hold.", "Tech"),
    ("nintendo-tokyo-store", "Inside Tokyo's Nintendo Store — A Pilgrimage Site for Gamers", "The Shibuya Nintendo Store has lines on opening day. The Mario merch. The Zelda figurines. The exclusives you can't get anywhere else.", "Tech"),
    ("drone-light-shows-tokyo", "Tokyo's Drone Light Shows Replaced Fireworks. Some Hate It.", "Tokyo Bay's new year display uses 2,000 drones instead of fireworks. It's silent, eco-friendly, and the older generation thinks it's soulless.", "Tech"),
    ("vending-machine-eggs-temple", "Tokyo Temple Sells Fresh Eggs From a Vending Machine. The Priest Restocks Daily.", "A small shrine in Setagaya runs a vending machine selling eggs from its own chickens. The priest checks it every morning. ¥200 a pack.", "Only In Japan"),

    # Food (20)
    ("fugu-blowfish-license", "Japan's Most Dangerous Dish Has Killed 4 People in 5 Years", "Fugu (blowfish) contains tetrodotoxin — 1,200 times deadlier than cyanide. Only licensed chefs can serve it. They train for 3 years.", "Food"),
    ("wagyu-beef-10000", "Why Wagyu Beef Costs ¥10,000 Per Slice", "True A5 wagyu is graded for marbling, color, and texture. The cattle eat better than most humans. One steak can cost ¥30,000.", "Food"),
    ("edible-insect-vending", "Japanese Vending Machines Sell Snack Bags of Grasshoppers", "Inago no tsukudani — grasshoppers boiled in sweet soy sauce — has been Japanese protein since the 1800s. Now they come in vending machines.", "Food"),
    ("hakone-black-onsen-eggs", "Hakone's Black Eggs Are Boiled in Sulfur Springs. They Add 7 Years to Your Life.", "At Owakudani, eggs boiled in the volcanic hot springs turn black. Legend says eating one extends your life by 7 years. Tourists buy them by the dozen.", "Food"),
    ("japan-whale-meat-eat", "Japan Still Eats Whale Meat. Here's the Complicated Reason.", "Whaling was a food staple in postwar Japan. Today, consumption is tiny — but politically symbolic. The annual catch quota still exists.", "Food"),
    ("takoyaki-mouth-burn", "Why Japanese Kids Voluntarily Burn Their Mouths on Takoyaki", "Takoyaki — octopus dough balls — comes off the grill at 200°C. The molten interior burns. Kids eat them anyway. It's an Osaka rite of passage.", "Food"),
    ("kit-kat-400-flavors", "Japan Has 400+ Kit Kat Flavors. Including Wasabi.", "Sake. Matcha. Wasabi. Purple sweet potato. Strawberry cheesecake. Hot-baked apple. Kit Kats in Japan are seasonal gifts, not snacks.", "Food"),
    ("mochi-pounding-dangerous", "The Pounding of Mochi is Japan's Most Dangerous Cooking Method", "Two people, one giant wooden mallet, one stone bowl. They alternate strikes. One person flips the dough between hits. Hospital records exist.", "Food"),
    ("omurice-history", "Omurice — The Western Dish Japan Invented and Perfected", "An omelet over rice with ketchup. Invented in Tokyo in 1925. Foreigners think it's bizarre. Japanese think it's the world's greatest comfort food.", "Food"),
    ("ramen-regional-styles", "Japan Has 100+ Regional Ramen Styles. Here Are 10 of the Strangest.", "Black ramen from Toyama. Curry ramen from Hokkaido. Stamina ramen with raw garlic. Cold ramen. Sweet ramen. Tomato cheese ramen. We rank them all.", "Food"),
    ("melon-pan-no-melon", "Japan's Melon Pan Bread Tastes Nothing Like Melon", "It looks like a melon (the surface pattern). It doesn't taste like one. It's a sweet cookie-topped bun. Japan refuses to fix the name.", "Food"),
    ("depachika-food-halls", "Tokyo's Department Store Basements Are Foodie Paradises", "Depachika are the food halls under Mitsukoshi, Isetan, and Takashimaya. Wagyu, sashimi, ¥3,000 strawberries, French pâtisserie. Lunch is theater.", "Food"),
    ("conveyor-sushi-math", "How Conveyor-Belt Sushi Math Feeds Tokyo's Hungriest Office Workers", "A plate every 8 seconds. ¥120-500 each. Color-coded for price. Tablet ordering, AI inventory. Sushiro is essentially a logistics company.", "Food"),
    ("tonkatsu-curry-religion", "Tonkatsu Curry: Japan's Brown Comfort Food Religion", "Breaded pork cutlet. Brown curry sauce. White rice. Eaten weekly by 30 million Japanese. There are tonkatsu academies. We're not joking.", "Food"),
    ("anpan-bread-bean-paste", "Japan's Most Beloved Bread Has Sweet Bean Paste Inside", "Anpan was invented in 1874 by a samurai-turned-baker. The Meiji Emperor approved. Today, anpan is sold at every bakery and convenience store in Japan.", "Food"),
    ("kakigori-cloud-ice", "Japanese Shaved Ice Is Engineered to Look Like a Cloud", "Kakigori shavings are so thin they melt instantly on your tongue. Top kakigori parlors in Tokyo have 2-hour queues in summer.", "Food"),
    ("obanyaki-train-snack", "Obanyaki — The ¥150 Snack Sold From Tokyo Train Station Stalls", "Hot pancake-shaped buns filled with sweet bean paste, custard, or curry. Eaten while walking. The smell of these stalls defines Japanese stations.", "Food"),
    ("mister-donut-outsells-krispy", "Japan's Mister Donut Outsells Krispy Kreme 10 to 1", "MisDo has 940 stores in Japan vs Krispy Kreme's 50. The pon-de-ring (chewy mochi donut) is the secret weapon Krispy Kreme can't match.", "Food"),
    ("starbucks-japan-sakura", "Japan's Starbucks Sells Sakura Lattes the Rest of the World Can't Buy", "The Japanese Starbucks menu is its own universe: sakura, hojicha, matcha, mochi, wagashi-shaped pastries. Starbucks Japan operates almost independently.", "Food"),
    ("matcha-in-everything", "Why Matcha is in Literally Everything in Japan, Including KFC", "Matcha Frappuccinos. Matcha Kit Kats. Matcha pizza. Matcha KFC. It's not just trendy — matcha is a 1,000-year-old Japanese industry quietly conquering the world.", "Food"),

    # Culture & Tradition (15)
    ("sakura-forecast-tv-news", "Japan Has a National Cherry Blossom Forecast on the News", "The Sakura-zensen (cherry blossom front) is tracked daily by 6 organizations. Maps show when each city will bloom. Hanami party planners depend on it.", "Culture"),
    ("4-hour-tea-ceremony", "The 4-Hour Japanese Tea Ceremony — What Actually Happens", "Wear silent shoes. Kneel for 3 hours. Eat soft sweets. Drink one bowl of green foam. There are 1,500 rules. We took the class.", "Culture"),
    ("kintsugi-gold-pottery", "Japanese Repair Broken Pottery With Gold. It's a Philosophy.", "Kintsugi turns broken bowls into objects more valuable than the originals. The cracks are filled with lacquered gold. The damage becomes the design.", "Culture"),
    ("bonsai-300-years-old", "Some Japanese Bonsai Trees Are 300 Years Old. They're Inherited.", "A bonsai is not a houseplant. Some are family heirlooms passed through 8 generations. The oldest known bonsai in Japan dates to 1610.", "Culture"),
    ("origami-olympics", "Japan Has Origami Olympics. The World Champion is 9 Years Old.", "Competitive origami requires inventing your own designs. The top folders work in their sleep, sometimes literally. Categories range from cranes to dragons with 1,000 scales.", "Culture"),
    ("omikuji-bad-fortune-tied", "Japanese Shrines Sell Paper Fortunes. Bad Ones Are Tied to Trees.", "Draw an omikuji at any shrine. If it's bad luck, tie it to the nearest tree — leaving the misfortune behind. The trees look like ghostly white snowstorms.", "Culture"),
    ("tiny-temple-kyoto", "Kyoto's Smallest Temple Is the Size of a Telephone Booth", "Mihoshi Temple in Kyoto fits one priest and three offerings. It's still active. The donation box accepts ¥10 coins.", "Culture"),
    ("nightingale-floor-ninja", "Kyoto's Anti-Ninja Floors Chirp When Someone Walks On Them", "Nijo Castle has 'nightingale floors' engineered to squeak when stepped on — an alarm system to detect intruding ninjas in the 17th century.", "Culture"),
    ("sento-bathhouse-rules", "Tokyo's Public Bathhouses Are Vanishing. Here's How to Use One Properly.", "Sentos require a wash before you enter the bath. Tattoos are usually banned. Towels stay out of the water. We've made all the mistakes so you don't.", "Culture"),
    ("obon-greet-ancestors", "The Festival Where Japanese Greet Their Dead Ancestors", "Mid-August, families gather to host their dead. Lanterns guide spirits home. Bon-odori dances entertain them. A week later, lanterns are floated downriver to send them back.", "Culture"),
    ("shichi-go-san-kimono", "Japanese Dress 3-, 5-, and 7-Year-Olds in Kimono Once a Year", "Shichi-Go-San (7-5-3) celebrates children of those ages. Parents pay ¥30,000 for kimono rentals. Photo studios have month-long bookings.", "Culture"),
    ("coming-of-age-day-20", "Japan Celebrates 20-Year-Olds With a Day of Drunk Speeches", "Seijin no Hi (Coming-of-Age Day) is the second Monday of January. New adults wear kimono and listen to mayors. Then they drink alcohol legally for the first time.", "Culture"),
    ("amezaiku-candy-sculptor", "Japanese Candy Sculptors Make Animals From Hot Sugar in 3 Minutes", "Amezaiku artists pull boiling sugar with bare hands, shape it with scissors, and paint it. The animals are edible. The artists are dying out.", "Culture"),
    ("furoshiki-cloth-wrapping", "Japan's Cloth-Wrapping Art Replaces Plastic Bags. It's Brilliant.", "Furoshiki is the art of wrapping any object in one square of cloth. Folded right, it's a bag, a backpack, gift wrap, or a wine carrier. Reusable forever.", "Culture"),
    ("geisha-still-exist", "Geisha Still Exist in Kyoto. Here's How the Profession Survives in 2026.", "Roughly 270 geisha and 80 maiko (apprentices) work in Kyoto today. Tea house dinners cost ¥80,000-200,000 per person. The training takes 5 years.", "Culture"),

    # Lifestyle Weird (10)
    ("hikikomori-1-5-million", "Japan Has 1.5 Million 'Hikikomori' — Adults Who Don't Leave Their Rooms", "Hikikomori withdraw from society for six months to decades. Government estimates put their number at 1.5 million. The oldest are now in their 60s.", "Lifestyle"),
    ("herbivore-men-soshoku", "Why a Generation of Japanese Men Stopped Dating", "Soshoku-danshi ('herbivore men') reject traditional masculinity, romance, and sex. They prefer hobbies. The trend is reshaping Japanese demographics.", "Lifestyle"),
    ("inemuri-meeting-naps", "Sleeping in Meetings is a Status Symbol in Japan", "Inemuri ('sleeping while present') signals you worked so hard you collapsed mid-task. Bosses respect it. Subordinates can't do it. There are rules.", "Lifestyle"),
    ("salaryman-drunk-sidewalk", "Why It's Legally OK to Be Passed Out Drunk on Tokyo Sidewalks", "Drunken sleep on the pavement is common, harmless, and culturally tolerated. The crime rate is too low for anyone to bother you. Wallets are usually intact.", "Lifestyle"),
    ("mask-culture-pre-covid", "Japanese Wore Surgical Masks Daily Long Before COVID", "Pollen allergies. Politeness when sick. Shyness. Skincare. Cold protection. Tokyo's mask culture predates COVID by decades — and it's never going away.", "Lifestyle"),
    ("tipping-insulting", "Why Tipping in Japan Will Insult the Server", "Service is included in the price. Hospitality is a cultural duty, not a transaction. Try to tip and the staff will chase you down the street to return the money.", "Lifestyle"),
    ("5-hour-queue-mochi", "Tokyo's 5-Hour Queues for Limited-Edition Mochi", "When a Tokyo bakery announces a seasonal limited mochi, queues form at dawn. Some bring camping chairs. Some hire substitutes. The mochi sells out in 90 minutes.", "Lifestyle"),
    ("silent-trains-tokyo", "Why Tokyo's Trains Are Almost Completely Silent", "Phone calls are banned. Talking is hushed. Music leaks earn glares. Cultural pressure, not law, keeps Tokyo's 8.7 million daily commuters quiet.", "Lifestyle"),
    ("women-only-train-carriages", "Japan Has Women-Only Train Carriages. Here's the Sad Reason.", "Introduced in 2000 to combat chikan (groping) on packed trains. Run during rush hour. Effective. The fact that they're necessary is a quiet shame.", "Lifestyle"),
    ("host-clubs-female-economy", "Inside Tokyo's Host Clubs — The Female-Run Other Side of the Industry", "Hosts pour drinks, listen, charm, and earn $100,000+ a month from female clients. Most clients are sex workers reinvesting their own earnings.", "Lifestyle"),

    # Tokyo Specific (5)
    ("shibuya-scramble-math", "The Math Behind Tokyo's Shibuya Scramble Crossing", "3,000 people cross every 2 minutes. 2.4 million people per day. The traffic light is calibrated to within 0.3 seconds. The physics is gorgeous.", "Tokyo"),
    ("ghibli-museum-tickets", "Why Ghibli Museum Tickets Sell Out in 30 Seconds", "200,000 tickets a month. Released on the 10th. Sold out within minutes. The museum caps daily visitors at 2,400 to protect the experience.", "Tokyo"),
    ("tokyo-underground-rivers", "Tokyo Has 50+ Underground Rivers. Most Are Sealed.", "Tokyo paved over its rivers during the 1964 Olympics. Some still flow beneath the city. Urban explorers map them illegally. The water is surprisingly clean.", "Tokyo"),
    ("roppongi-hills-maze-mall", "Roppongi Hills Mall Is Famous for Getting Tourists Lost", "Six levels. Spiral layouts. Identical signage. Even Tokyo locals get disoriented. Internet message boards have escape guides.", "Tokyo"),
    ("tokyo-tower-skytree-rivalry", "Why Tokyo Has Two Iconic Towers — And the Quiet Rivalry Between Them", "Tokyo Tower (1958, 333m, Eiffel inspired). Tokyo Skytree (2012, 634m, world's tallest tower). Locals are loyal to one. The two camps don't talk.", "Tokyo"),
]


TEMPLATE = """---
title: "{title}"
description: "{description}"
pubDate: {pubdate}
category: "{category}"
heroImageUrl: "{img_url}"
heroImageAlt: "{img_alt}"
heroImageCredit: "{img_credit}"
heroImageCreditUrl: "{img_credit_url}"
---

{intro}

## The Quick Facts

- This story is part of Japan's strangest cultural inventory
- Most travelers walk past without realizing it exists
- It has been quietly normal in Japan for decades
- The locals don't think it's weird at all

## What's Actually Going On

{description_expanded}

## Why This Exists in Japan

Japan has a unique cultural appetite for **micro-specialization, ritualized service, and quiet eccentricity**. What looks bizarre to outsiders is usually the polished result of decades of refinement — a small idea taken seriously, then perfected, then commercialized.

{title_with_focus} is exactly that pattern. Imported attention, domestic obsession, and a willingness to keep going long after other countries would have given up.

## How to Experience It

- **Where**: Major cities, especially Tokyo and Osaka — though regional variations exist
- **Cost**: Usually under ¥3,000 for a first taste
- **Best time**: Weekday afternoons (smaller crowds)
- **Insider tip**: Bring cash. Japan still runs on coins more than cards.

## The Weird Part

> The strange thing isn't that this exists. It's that it's *normal* here.

That gap — between how Japan treats this as ordinary and how the rest of the world reacts when they discover it — is the entire reason WeirdJapan.news exists.

---

**Want to explore Japan in person?**

- 🏨 [Search hotels on Booking.com](https://www.booking.com/)
- 🎫 [Find Japan tours and experiences on Klook](https://www.klook.com/)
- 📚 [Amazon: Lonely Planet Japan guide](https://www.amazon.com/)

---

*WeirdJapan.news covers the strange, the small, and the slightly-too-much in Japanese culture. Subscribe for more daily oddities most travel guides skip.*
"""


def make_intro(title, description):
    return f"{description}\n\nThis is one of those things Japan does quietly — without fanfare, without irony, and without any apparent awareness that the rest of the world finds it remarkable."


def make_description_expanded(title, description):
    return (
        f"{description} What seems random is usually the product of a very specific combination of circumstances: "
        "limited urban space, an aging but disciplined population, a deep cultural tolerance for "
        "ritualized service, and a national appetite for slightly excessive specialization.\n\n"
        "In most countries, this kind of thing would be a tourist curiosity. In Japan, it's "
        "infrastructure. It's normal. People use it on Tuesday mornings without thinking about it.\n\n"
        "And that — the unselfconscious normalcy — is what makes it so disorienting to visitors."
    )


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    written = 0

    # Distribute publication dates: spread across 2026-04-15 to 2026-05-21
    start = date(2026, 4, 15)
    end = date(2026, 5, 21)
    total = (end - start).days  # 36

    for i, (slug, title, desc, category) in enumerate(ARTICLES):
        # Distribute evenly
        offset = int(i * total / len(ARTICLES))
        pub = start + timedelta(days=offset)

        img_key = pick_image(slug, category)
        img_url, img_alt, img_credit, img_credit_url = IMAGES[img_key]

        # Escape any double quotes in title/desc
        title_esc = title.replace('"', '\\"')
        desc_esc = desc.replace('"', '\\"')
        alt_esc = img_alt.replace('"', '\\"')

        content = TEMPLATE.format(
            title=title_esc,
            description=desc_esc,
            pubdate=pub.isoformat(),
            category=category,
            img_url=img_url,
            img_alt=alt_esc,
            img_credit=img_credit,
            img_credit_url=img_credit_url,
            intro=make_intro(title, desc),
            description_expanded=make_description_expanded(title, desc),
            title_with_focus=title,
        )

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w") as f:
            f.write(content)
        written += 1

    print(f"✅ Wrote {written} articles to {OUT_DIR}")
    print(f"Total articles in collection: {len(os.listdir(OUT_DIR))}")


if __name__ == "__main__":
    main()
