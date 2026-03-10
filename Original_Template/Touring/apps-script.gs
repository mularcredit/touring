/**
 * KALEOLA ZAR LIMITED - Google Apps Script
 * ==========================================
 * SETUP INSTRUCTIONS:
 * 1. Go to https://sheets.google.com and create a new spreadsheet
 * 2. Name it "Kaleola Zar Bookings"
 * 3. Add these headers to Row 1:
 *    Timestamp | Name | Email | Phone | Package | Travel Date | Message | Status
 * 4. Go to Extensions > Apps Script
 * 5. Paste this entire script, replacing any existing code
 * 6. Click "Deploy" > "New deployment"
 * 7. Choose type: "Web app"
 * 8. Set "Who has access" to "Anyone"
 * 9. Click Deploy and copy the Web App URL
 * 10. Replace SCRIPT_URL in both index.html and dashboard.html with that URL
 */

const SPREADSHEET_ID = '1Sb0KYsXv2fXBdVsRsFqRW_dblezS6DCZiqTCWNzeRg0';

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    sheet.appendRow([
      new Date().toLocaleString(),
      data.name    || '',
      data.email   || '',
      data.phone   || '',
      data.package || '',
      data.date    || '',
      data.message || '',
      'New'
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success', message: 'Enquiry received!' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  try {
    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getActiveSheet();
    const rows  = sheet.getDataRange().getValues();
    
    // First row is headers
    const headers = rows[0];
    const records = rows.slice(1).map(row => {
      const obj = {};
      headers.forEach((h, i) => obj[h] = row[i]);
      return obj;
    });
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success', data: records }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
