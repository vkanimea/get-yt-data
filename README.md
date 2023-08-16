# get-sp-dl-report
Generate a report for a Sharepoint Site for expired sharelinks in a Document library. Parameters are SiteURL, ReportOutput, ListName {Document Library}, FolderName {Optional - Specify a folder}, RemoveSharing {Optional - Control whether to remove sharing}. Uses PnP Modules for Sharepoint. ReportOutput: csv file output : Name, RelativeURL, FileType, ShareLink, ShareLinkAccess, ShareLinkType, AllowsAnonymousAccess, IsActive, Expiration.

## Usage
```powershell
.\get-sp-rp.ps1 -SiteUrl "https://yoursharepointsite.com" -ReportOutput "C:\path\to\your\report.csv" -ListName "Your List Name"
```
Replace `"https://yoursharepointsite.com"` with the URL of your SharePoint site, `"C:\path\to\your\report.csv"` with the path where you want the report to be saved, and `"Your List Name"` with the name of the list you want to get the shared links from.

If you want to specify a log file, you can do so with the `-LogFile` parameter:
```powershell
.\get-sp-rp.ps1 -SiteUrl "https://yoursharepointsite.com" -ReportOutput "C:\path\to\your\report.csv" -ListName "Your List Name" -LogFile "C:\path\to\your\log.txt"
```
If you want to remove sharing file access, you can do so with the `-RemoveSharingFileAccess` parameter:
```powershell
.\get-sp-rp.ps1 -SiteUrl "https://yoursharepointsite.com" -ReportOutput "C:\path\to\your\report.csv" -ListName "Your List Name" -RemoveSharingFileAccess $true
```
If you want to specify a folder name, you can do so with the `-FolderName` parameter:
```powershell
.\get-sp-rp.ps1 -SiteUrl "https://yoursharepointsite.com" -ReportOutput "C:\path\to\your\report.csv" -ListName "Your List Name" -FolderName "Your Folder Name"
```
Please note that you need to have the SharePoint PnP PowerShell module installed and you need to have access to the SharePoint site.


# YouTube Data Scraper

This is a Python script that uses the YouTube Data API to fetch data about videos based on a search parameter.

## Installation

1. Clone this repository.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Replace `"YOUR_API_KEY"` in `youtube_search.py` with your actual YouTube Data API key and `"search parameter"` with the actual search parameter.

Then, run the script:

```bash
python youtube_search.py
```

This will print the titles, views, likes, and comments of the top 10 videos that match the search parameter, sorted by the number of views.
