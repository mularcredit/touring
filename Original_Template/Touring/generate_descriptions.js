const fs = require('fs');
const file = 'c:/Users/HomePC/Downloads/Touring/index.html';
let html = fs.readFileSync(file, 'utf8');

const metadata = {
    "Lake Naivasha": {
        note: "A pristine freshwater jewel shimmering under the Great Rift Valley sun.",
        desc: "Glide across tranquil waters teeming with hippos and exotic birdlife. Lake Naivasha offers a serene escape, surrounded by lush acacia forests and the distant allure of Mount Longonot.",
        annotation1: "Birdwatcher's paradise",
        annotation2: "Freshwater sanctuary"
    },
    "Hell's Gate National Park": {
        note: "Walk amongst giants in a dramatic landscape forged by ancient geothermal forces.",
        desc: "Trade the safari vehicle for a bicycle as you explore towering cliffs, water-gouged gorges, and stark rock towers alongside grazing zebras and majestic giraffes.",
        annotation1: "Geothermal wonders",
        annotation2: "Cycling safaris"
    },
    "Lake Elementaita": {
        note: "A sapphire mirage nestled within the private Soysambu Conservancy.",
        desc: "Experience exclusive luxury on the shores of this soda lake. Witness spectacular flocks of flamingos taking flight against the breathtaking backdrop of the Rift Valley escarpment.",
        annotation1: "Flamingo shores",
        annotation2: "Private conservancy"
    },
    "Lake Nakuru National Park": {
        note: "A vibrant canvas of pink painted across alkaline waters.",
        desc: "Renowned globally as an ornithological spectacle, Nakuru is also a premier sanctuary for both black and white rhinos, offering unforgettable encounters with Africa's rarest giants.",
        annotation1: "Rhino sanctuary",
        annotation2: "Sea of pink"
    },
    "Masai Mara": {
        note: "The quintessential African safari experience, raw and unyielding.",
        desc: "Home to the legendary Great Migration, the Mara's rolling savannahs host the highest concentration of big cats on earth. An absolute must-visit add-on for the ultimate wildlife enthusiast.",
        annotation1: "The Great Migration",
        annotation2: "Apex predators"
    },
    "Diani Beach": {
        note: "Powder-white sands meeting the warm, turquoise embrace of the Indian Ocean.",
        desc: "Consistently voted Africa's leading beach destination. Unwind in barefoot luxury, explore vibrant coral reefs, or sail on a traditional dhow as the African sun sets over the horizon.",
        annotation1: "Endless white sand",
        annotation2: "Tropical luxury"
    },
    "Malindi": {
        note: "Where rich Swahili history blends effortlessly with Italian coastal glamour.",
        desc: "Wander through centuries-old ruins, indulge in world-class seafood, and dive into the crystal-clear waters of the marine park. Malindi is a tantalizing fusion of cultures.",
        annotation1: "Historical ruins",
        annotation2: "Italian flair"
    },
    "Watamu": {
        note: "An idyllic marine wonderland offering some of the world's best snorkeling.",
        desc: "Nestled between pristine beaches and lush tropical forests, Watamu is a tranquil haven. Swim alongside green turtles and explore the magical underwater gardens of the reef.",
        annotation1: "Marine reserve",
        annotation2: "Turtle watching"
    },
    "Apartheid Museum": {
        note: "A profound journey through shadows into incredible national resilience.",
        desc: "An essential, moving experience that chronicles the rise and fall of apartheid. The museum's raw, powerful exhibits offer a vital understanding of South Africa's triumphant history.",
        annotation1: "Historical pillar",
        annotation2: "Profound journey"
    },
    "Constitution Hill": {
        note: "From a place of deep injustice to the vibrant seat of the Constitutional Court.",
        desc: "Walk the grounds of this former prison complex that once held Nelson Mandela and Mahatma Gandhi. Today, it stands proudly as a living museum and a beacon of democracy.",
        annotation1: "Living museum",
        annotation2: "Justice reformed"
    },
    "Nelson Mandela Square": {
        note: "The cosmopolitan heartbeat of Sandton, under the gaze of a colossal icon.",
        desc: "Dine at world-class restaurants and shop at luxury boutiques around the majestic, towering bronze statue of Nelson Mandela in the very vibrant center of African commerce.",
        annotation1: "Luxury shopping",
        annotation2: "Iconic statue"
    },
    "Soweto Vilakazi Street": {
        note: "The only street in the world to house two Nobel Peace Prize laureates.",
        desc: "Feel the vibrant, unyielding pulse of Soweto. Vilakazi Street is alive with public art, historic significance, bustling local eateries, and the indomitable spirit of its people.",
        annotation1: "Nobel heritage",
        annotation2: "Vibrant culture"
    },
    "Nelson Mandela House": {
        note: "A humble red-brick matchbox house preserving the legacy of a global titan.",
        desc: "Step inside No. 8115, where Nelson Mandela lived before his imprisonment. This intimate museum houses deeply personal memorabilia, offering a glimpse into the man behind the myth.",
        annotation1: "Intimate history",
        annotation2: "Mandela's home"
    },
    "Cradle of Humankind": {
        note: "Descend into the limestone caves where the story of humanity began.",
        desc: "A globally recognized World Heritage Site. Explore the Maropeng Visitor Centre and the Sterkfontein Caves, uncovering fossils that bridge the gap between our ancestors and us.",
        annotation1: "Origins of humanity",
        annotation2: "Ancient fossils"
    },
    "Lion Walk Experience": {
        note: "An adrenaline-pumping encounter with the undisputed kings of the savannah.",
        desc: "A truly rare opportunity to walk alongside young lions in their natural habitat. Learn about conservation efforts while experiencing the raw power of these magnificent predators up close.",
        annotation1: "Walking safaris",
        annotation2: "Close encounters"
    },
    "Dinokeng Game Reserve": {
        note: "The only free-roaming Big Five reserve situated in the heart of Gauteng.",
        desc: "Experience the thrill of a premier safari just outside the city. From luxury lodges to open-air game drives, Dinokeng offers a spectacular, accessible wilderness adventure.",
        annotation1: "Big Five reserve",
        annotation2: "Accessible thrill"
    }
};

html = html.replace(/<script>[\s\S]*?document\.addEventListener\('DOMContentLoaded', function\(\) {[\s\S]*?\/\/ Find Modal Elements/, function(match) {
    
    // We will inject our data array right before the DOMContentLoaded logic
    const dataInject = 
    const packageData = ;
    document.addEventListener('DOMContentLoaded', function() {
        // Find Modal Elements;
    
    return match.replace(/document\.addEventListener\('DOMContentLoaded', function\(\) {[\s\S]*?\/\/ Find Modal Elements/, dataInject);
});

// Now update the click event handler to use this data instead of generic strings
const replacer = 
                const data = packageData[imgNode.alt] || {
                    note: "An unforgettable African experience, meticulously curated for the discerning traveler.",
                    desc: "Experience the breathtaking beauty of " + title + ". This destination awaits you with an unforgettable adventure. Immerse yourself in the rich culture and stunning landscapes.",
                    annotation1: "Untouched wilderness",
                    annotation2: "Luxury experience"
                };

                // Populate Modal mimicking the editorial style
                mBadge.innerText = String(index + 421); // Fun detail
                mCategory.innerText = cat;
                
                // Highlight the first word if it contains multiple words
                let words = title.split(' ');
                if(words.length > 1) {
                    mTitle.innerHTML = '<strong>' + words[0] + '</strong><br>' + words.slice(1).join(' ');
                } else {
                    mTitle.innerHTML = '<strong>' + title + '</strong>';
                }

                mDesc.innerText = data.desc;
                document.getElementById('modalNote').innerText = data.note;
                
                // Update the floating annotations
                const annotations = document.querySelectorAll('.kz-modal-annotation .annotation-text');
                if(annotations.length >= 2) {
                    annotations[0].innerText = data.annotation1;
                    annotations[1].innerText = data.annotation2;
                }

                mImage.src = imgSrc;
;

html = html.replace(/mBadge\.innerText =[^;]+;[\s\S]*?mImage\.src = imgSrc;/, replacer);

fs.writeFileSync(file, html, 'utf8');
console.log('Successfully injected dynamic data mapping.');
