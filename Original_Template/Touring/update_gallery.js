const fs = require('fs');
const htmlPath = 'c:/Users/HomePC/Downloads/Touring/index.html';
const replacePath = 'c:/Users/HomePC/Downloads/Touring/replace.html';
let content = fs.readFileSync(htmlPath, 'utf8');
const replacement = fs.readFileSync(replacePath, 'utf8');
const regex = /    <!-- Start Packages Gallery [\s\S]*?<!-- End Packages Gallery -->/;
if (content.match(regex)) {
    content = content.replace(regex, replacement);
    fs.writeFileSync(htmlPath, content, 'utf8');
    console.log('Successfully replaced gallery.');
} else {
    console.log('Regex did not match.');
}

