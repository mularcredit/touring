const fs = require('fs');
const file = 'c:/Users/HomePC/Downloads/Touring/index.html';
let html = fs.readFileSync(file, 'utf8');

const replacements = {
    "Hell's Gate National Park": "hells_gate",
    "Lake Naivasha": "naivasha",
    "Lake Elementaita": "elementaita",
    "Lake Nakuru National Park": "nakuru",
    "Masai Mara": "masai_mara",
    "Diani Beach": "diani",
    "Malindi": "malindi",
    "Watamu": "watamu",
    "Apartheid Museum": "apartheid_museum",
    "Constitution Hill": "constitution_hill",
    "Nelson Mandela Square": "mandela_square",
    "Soweto Vilakazi Street": "soweto",
    "Nelson Mandela House": "mandela_house",
    "Cradle of Humankind": "cradle",
    "Lion Walk Experience": "lion_walk",
    "Dinokeng Game Reserve": "dinokeng"
};

for (const [alt, filename] of Object.entries(replacements)) {
    const rx = new RegExp('src="assets/img/custom/package\\\\d\\\\.png" alt="' + alt + '"', 'g');
    html = html.replace(rx, 'src="assets/img/custom/destinations/' + filename + '.jpg" alt="' + alt + '"');
}

fs.writeFileSync(file, html, 'utf8');
console.log("Replaced image paths.");
