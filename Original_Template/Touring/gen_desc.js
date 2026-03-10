const fs = require('fs');
const file = 'c:/Users/HomePC/Downloads/Touring/index.html';
let html = fs.readFileSync(file, 'utf8');

const metadata = {
    "Lake Naivasha": { note: "A pristine freshwater jewel shimmering under the sun.", desc: "Glide across tranquil waters teeming with hippos. Lake Naivasha offers a serene escape, surrounded by lush acacia forests.", annotation1: "Birdwatcher's paradise", annotation2: "Freshwater sanctuary" },
    "Hell's Gate National Park": { note: "Walk amongst giants in a dramatic, ancient landscape.", desc: "Trade the safari vehicle for a bicycle as you explore towering cliffs, water-gouged gorges, and stark rock towers alongside grazing zebras.", annotation1: "Geothermal wonders", annotation2: "Cycling safaris" },
    "Lake Elementaita": { note: "A sapphire mirage nestled within the private Soysambu.", desc: "Experience exclusive luxury on the shores of this soda lake. Witness spectacular flocks of flamingos taking flight.", annotation1: "Flamingo shores", annotation2: "Private conservancy" },
    "Lake Nakuru National Park": { note: "A vibrant canvas of pink painted across alkaline waters.", desc: "Renowned globally as an ornithological spectacle, Nakuru is also a premier sanctuary for both black and white rhinos.", annotation1: "Rhino sanctuary", annotation2: "Sea of pink" },
    "Masai Mara": { note: "The quintessential African safari experience, raw and unyielding.", desc: "Home to the legendary Great Migration, the Mara's rolling savannahs host the highest concentration of big cats on earth.", annotation1: "The Great Migration", annotation2: "Apex predators" },
    "Diani Beach": { note: "Powder-white sands meeting the warm, turquoise Indian Ocean.", desc: "Consistently voted Africa's leading beach destination. Unwind in barefoot luxury or sail on a traditional dhow at sunset.", annotation1: "Endless white sand", annotation2: "Tropical luxury" },
    "Malindi": { note: "Where rich Swahili history blends effortlessly with Italian glamour.", desc: "Wander through centuries-old ruins, indulge in world-class seafood, and dive into the crystal-clear waters of the marine park.", annotation1: "Historical ruins", annotation2: "Italian flair" },
    "Watamu": { note: "An idyllic marine wonderland offering world's best snorkeling.", desc: "Nestled between pristine beaches and lush tropical forests, Watamu is a tranquil haven. Swim alongside green turtles.", annotation1: "Marine reserve", annotation2: "Turtle watching" },
    "Apartheid Museum": { note: "A profound journey through shadows into incredible resilience.", desc: "An essential, moving experience that chronicles the rise and fall of apartheid. The museum's raw, powerful exhibits offer vital understanding.", annotation1: "Historical pillar", annotation2: "Profound journey" },
    "Constitution Hill": { note: "From deep injustice to the vibrant seat of the Constitutional Court.", desc: "Walk the grounds of this former prison complex that once held Nelson Mandela. Today, it stands proudly as a living museum.", annotation1: "Living museum", annotation2: "Justice reformed" },
    "Nelson Mandela Square": { note: "The cosmopolitan heartbeat of Sandton, under a colossal icon.", desc: "Dine at world-class restaurants and shop at luxury boutiques around the majestic, towering bronze statue of Nelson Mandela.", annotation1: "Luxury shopping", annotation2: "Iconic statue" },
    "Soweto Vilakazi Street": { note: "The only street in the world to house two Nobel Peace Prize laureates.", desc: "Feel the vibrant, unyielding pulse of Soweto. Vilakazi Street is alive with public art, historic significance, and bustling local eateries.", annotation1: "Nobel heritage", annotation2: "Vibrant culture" },
    "Nelson Mandela House": { note: "A humble red-brick matchbox house preserving a global titan.", desc: "Step inside No. 8115, where Nelson Mandela lived before his imprisonment. This intimate museum houses deeply personal memorabilia.", annotation1: "Intimate history", annotation2: "Mandela's home" },
    "Cradle of Humankind": { note: "Descend into the limestone caves where humanity began.", desc: "A globally recognized World Heritage Site. Explore the Maropeng Visitor Centre and the Sterkfontein Caves, uncovering ancient fossils.", annotation1: "Origins of humanity", annotation2: "Ancient fossils" },
    "Lion Walk Experience": { note: "An adrenaline-pumping encounter with kings of the savannah.", desc: "A truly rare opportunity to walk alongside young lions in their natural habitat. Learn about conservation efforts while experiencing raw power.", annotation1: "Walking safaris", annotation2: "Close encounters" },
    "Dinokeng Game Reserve": { note: "The only free-roaming Big Five reserve situated in Gauteng.", desc: "Experience the thrill of a premier safari just outside the city. From luxury lodges to open-air game drives, Dinokeng offers spectacular adventure.", annotation1: "Big Five reserve", annotation2: "Accessible thrill" }
};

if (!html.includes('const packageData')) {
    html = html.replace("document.addEventListener('DOMContentLoaded', function() {", 
        "const packageData = " + JSON.stringify(metadata) + ";\n    document.addEventListener('DOMContentLoaded', function() {");
}

const findStr = "mBadge.innerText = String(index + 421); // Fun detail mapping to the \\"421\\" \\"422\\" numbers on the menu image";
const replaceStr = "const data = packageData[title] || {note: 'An unforgettable African experience, meticulously curated for the discerning traveler.', desc: 'Experience the breathtaking beauty of ' + title + '. This destination awaits you with an unforgettable adventure. Immerse yourself in the rich culture and stunning landscapes.', annotation1: 'Untouched wilderness', annotation2: 'Luxury experience'};\n                mBadge.innerText = String(index + 421);\n                mDesc.innerText = data.desc;\n                document.getElementById('modalNote').innerText = data.note;\n                const annotations = document.querySelectorAll('.kz-modal-annotation .annotation-text');\n                if(annotations.length >= 2) {\n                    annotations[0].innerText = data.annotation1;\n                    annotations[1].innerText = data.annotation2;\n                }";

html = html.replace(findStr, replaceStr);

// Clean up the old hardcoded inject
html = html.replace("mDesc.innerText = \\"Experience the breathtaking beauty of \\" + title + \\". \\" + desc + \\" awaits you with an unforgettable adventure. Immerse yourself in the rich culture and stunning landscapes.\\";", "");
html = html.replace("document.getElementById('modalNote').innerText = data.note;", ""); // safety cleanup if needed

fs.writeFileSync(file, html, 'utf8');
console.log('Descriptions Added!');
