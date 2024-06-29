const express = require('express');
const XLSX = require('xlsx');
const app = express();
app.use(express.static('public'));

app.get('/data', (req, res) => {
    const workbook = XLSX.readFile('E:\\tech4good-main\\baidu_vs_huawei.xlsx');
    const sheet_name_list = workbook.SheetNames;
    const data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[1]]);
    res.json(data);
});

app.listen(3001, () => console.log('Server started on port 3001'));
     