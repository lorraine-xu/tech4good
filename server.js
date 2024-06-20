import express from 'express';
import xlsx from 'xlsx';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/data', (req, res) => {
    // Read the XLSX file from the data directory
    const workbook = xlsx.readFile(path.join(__dirname, 'data', '百度vs华为.xlsx'));
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];

    // Convert the worksheet to JSON
    const jsonData = xlsx.utils.sheet_to_json(worksheet);
    res.json(jsonData);
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
