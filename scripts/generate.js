const fs = require('fs');
const path = require('path');

const packageJson = require('../package.json');
const meta = packageJson.meta;

const templatePath = path.join(process.cwd(), 'template', 'main.md');
const paragraphsPath = path.join(process.cwd(), 'source', 'paragraphs');
const outputPath = path.join(process.cwd(), 'source', 'main.md');

let content = fs.readFileSync(templatePath, 'utf8');
for (const key in meta) {
  const value = meta[key];
  content = content.replace(new RegExp(`{{${key}}}`, 'g'), value);
}

const paragraphsRaw = fs.readdirSync(paragraphsPath).map(filename => filename.split('_')).map((parts) => ({
    id: +parts[0],
    filename: parts.join('_'),
}));
const abstract = paragraphsRaw.find(paragraph => paragraph.id === 0);
const paragraphs = paragraphsRaw.filter(paragraph => paragraph.id !== 0);

if (abstract) {
    content = content.replace(new RegExp(`{{ABSTRACT}}`, 'g'), `{{paragraphs/${abstract.filename}}}`);
}
const paragraphsText = paragraphs.map(paragraph => `{{paragraphs/${paragraph.filename}}}`).join('\n\n');
content = content.replace(new RegExp(`{{PARAGRAPHS}}`, 'g'), paragraphsText);

fs.writeFileSync(outputPath, content);